"""Tests for the canonical subject/geography taxonomy."""
from pathlib import Path

import pytest

from _categories import (
    ALLOWED_SUBJECTS,
    derive_subject_geography,
    validate_subject,
    validate_subject_or_raise,
)


class TestDeriveSubjectGeography:
    """Path-to-(subject, geography) mapping must handle real-world quirks."""

    def test_absolute_path_with_subject_and_geography(self):
        p = Path("/Users/x/Dex/06-Resources/Research/Cryptocurrency/Stablecoin/foo.pdf")
        subj, geo = derive_subject_geography(p)
        assert subj == "Cryptocurrency"
        assert geo == "Stablecoin"

    def test_relative_path_with_subject_and_geography(self):
        p = Path("Cryptocurrency/Stablecoin/foo.pdf")
        subj, geo = derive_subject_geography(p)
        assert subj == "Cryptocurrency"
        assert geo == "Stablecoin"

    def test_pdf_directly_under_subject_returns_no_geography(self):
        p = Path("/x/Research/Cryptocurrency/foo.pdf")
        subj, geo = derive_subject_geography(p)
        assert subj == "Cryptocurrency"
        assert geo is None

    def test_leading_whitespace_stripped(self):
        """Tresorit export produces folders with leading spaces."""
        p = Path("/x/Research/ Uncategorised [Sorting Needed]/file.pdf")
        subj, geo = derive_subject_geography(p)
        assert subj == "Uncategorised [Sorting Needed]"

    def test_unknown_subject_returned_verbatim(self):
        """Validation is a separate step; derivation returns what's on disk."""
        p = Path("/x/Research/NotARealCategory/foo.pdf")
        subj, _ = derive_subject_geography(p)
        assert subj == "NotARealCategory"


class TestValidateSubject:
    @pytest.mark.parametrize("subject", sorted(ALLOWED_SUBJECTS))
    def test_each_allowed_subject_passes(self, subject):
        ok, err = validate_subject(subject)
        assert ok is True
        assert err == ""

    def test_unknown_subject_returns_actionable_error(self):
        ok, err = validate_subject("ImaginaryCategory")
        assert ok is False
        assert "ImaginaryCategory" in err
        assert "User Guide" in err
        assert "_categories.py" in err

    def test_validate_or_raise_silent_on_valid(self):
        validate_subject_or_raise("Cryptocurrency")  # must not raise

    def test_validate_or_raise_raises_on_invalid(self):
        with pytest.raises(ValueError, match="Unknown research Subject"):
            validate_subject_or_raise("NotReal")
