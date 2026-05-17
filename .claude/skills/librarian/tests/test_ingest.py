"""Tests for ingest pipeline helpers (sha1, paths, manifest, atomic writes).

Full PDF→markdown extraction is covered by the real ingest run, not by unit
tests — synthesising a PDF in-process would require pulling in reportlab as a
dev dependency for marginal value. The helpers below are where regressions
would silently corrupt the cache."""
from __future__ import annotations

import json
from pathlib import Path
from unittest import mock

import pytest

import ingest
from ingest import (
    IngestStats,
    compute_sha1,
    get_page_dir,
    load_manifest,
    page_filename,
    save_failures,
    save_manifest,
)


# ---------------------------------------------------------------------------
# sha1
# ---------------------------------------------------------------------------

class TestComputeSha1:
    def test_known_content(self, tmp_path):
        p = tmp_path / "hello.bin"
        p.write_bytes(b"hello world")
        # echo -n "hello world" | sha1sum
        assert compute_sha1(p) == "2aae6c35c94fcfb415dbe95f408b9ce91ee846ed"

    def test_empty_file(self, tmp_path):
        p = tmp_path / "empty.bin"
        p.write_bytes(b"")
        assert compute_sha1(p) == "da39a3ee5e6b4b0d3255bfef95601890afd80709"

    def test_large_file_streamed(self, tmp_path):
        """Streaming sha1 must match a one-shot read for files > chunk_size."""
        import hashlib
        p = tmp_path / "big.bin"
        # 3 MB > 1 MB chunk_size → exercises the streaming loop
        data = b"x" * (3 * 1024 * 1024 + 17)
        p.write_bytes(data)
        assert compute_sha1(p) == hashlib.sha1(data).hexdigest()


# ---------------------------------------------------------------------------
# path mapping
# ---------------------------------------------------------------------------

class TestPathHelpers:
    def test_page_filename_zero_padded(self):
        assert page_filename(1) == "p0001.md"
        assert page_filename(42) == "p0042.md"
        assert page_filename(9999) == "p9999.md"

    def test_get_page_dir(self, monkeypatch, tmp_path):
        monkeypatch.setattr(ingest, "RESEARCH_ROOT", tmp_path)
        monkeypatch.setattr(ingest, "DERIVED_ROOT", tmp_path / ".derived")
        pdf = tmp_path / "Cryptocurrency" / "Stablecoin" / "foo.pdf"
        out = get_page_dir(pdf)
        assert out == tmp_path / ".derived" / "Cryptocurrency" / "Stablecoin" / "foo"


# ---------------------------------------------------------------------------
# manifest persistence
# ---------------------------------------------------------------------------

class TestManifest:
    def test_load_returns_empty_when_missing(self, monkeypatch, tmp_path):
        monkeypatch.setattr(ingest, "MANIFEST_PATH", tmp_path / "_manifest.json")
        assert load_manifest() == {}

    def test_save_and_load_roundtrip(self, monkeypatch, tmp_path):
        monkeypatch.setattr(ingest, "MANIFEST_PATH", tmp_path / "_manifest.json")
        payload = {"Cryptocurrency/foo.pdf": {"sha1": "abc", "page_count": 12}}
        save_manifest(payload)
        assert load_manifest() == payload

    def test_save_atomic_via_tmp(self, monkeypatch, tmp_path):
        monkeypatch.setattr(ingest, "MANIFEST_PATH", tmp_path / "_manifest.json")
        save_manifest({"k": "v"})
        # Make sure the .tmp file was cleaned up
        assert not (tmp_path / "_manifest.json.tmp").exists()
        assert (tmp_path / "_manifest.json").exists()

    def test_load_returns_empty_on_corrupt(self, monkeypatch, tmp_path):
        path = tmp_path / "_manifest.json"
        monkeypatch.setattr(ingest, "MANIFEST_PATH", path)
        path.write_text("{not json", encoding="utf-8")
        assert load_manifest() == {}


# ---------------------------------------------------------------------------
# failures log
# ---------------------------------------------------------------------------

class TestFailuresLog:
    def test_save_failures_includes_metadata(self, monkeypatch, tmp_path):
        monkeypatch.setattr(ingest, "FAILURES_PATH", tmp_path / "_failures.json")
        stats = IngestStats()
        stats.failures.append({"pdf": "Cryptocurrency/foo.pdf", "reason": "encrypted"})
        save_failures(stats)
        data = json.loads((tmp_path / "_failures.json").read_text())
        assert data["total_failures"] == 1
        assert data["failures"][0]["reason"] == "encrypted"
        assert "generated_at" in data

    def test_record_failure_uses_relative_path(self, monkeypatch, tmp_path):
        monkeypatch.setattr(ingest, "RESEARCH_ROOT", tmp_path)
        stats = IngestStats()
        stats.record_failure(tmp_path / "Subj" / "x.pdf", "boom")
        assert stats.errors == 1
        assert stats.failures[0]["pdf"] == "Subj/x.pdf"

    def test_record_failure_falls_back_to_str(self, monkeypatch, tmp_path):
        # PDF outside RESEARCH_ROOT — relative_to raises, fallback kicks in
        monkeypatch.setattr(ingest, "RESEARCH_ROOT", tmp_path / "other")
        stats = IngestStats()
        stats.record_failure(Path("/elsewhere/x.pdf"), "boom")
        assert stats.failures[0]["pdf"] == "/elsewhere/x.pdf"
