# AML Labs Demo

**Date:** 2026-02-26
**Duration:** Unknown
**Meeting ID:** 47425a9d-e97f-44ba-8a72-64c3222b02db

## Participants
- *Participants not listed*

### Summary

Nikolett demoed AML Labs: an intelligence layer that forecasts multi-jurisdictional AML/KYC requirements, scrapes registries, runs sanction/PEP screening, ranks risk and drafts client outreach. She showed a fast low-risk onboarding flow with automated data pulls and audit snapshots, then a high-risk case that triggered sanctions hits, a longer document list and compliance escalation with human-in-loop options. David probed technical, data residency and regulatory concerns (including WhatsApp use and explainability); Nikolett outlined plans for proprietary models, not storing customer data, modular integrations, periodic review automation, and audit-driven analytics. The meeting closed with David offering to champion an internal evaluation and a plan to involve Alliwan’s new head of IT.

## Full Transcript

**Nikolett Szeplaki Esq** [05:59:53]: Hi, David.

**Nikolett Szeplaki Esq** [05:59:57]: How are you today?

**David Orban** [05:59:58]: Hello, Nikki.

**David Orban** [05:59:59]: I'm well, thank you.

**David Orban** [06:00:00]: Okay,

**Nikolett Szeplaki Esq** [06:00:01]: so back in the region again.

**Nikolett Szeplaki Esq** [06:00:03]: Okay, perfect.

**Nikolett Szeplaki Esq** [06:00:07]: All right, let me cut to the chase.

**Nikolett Szeplaki Esq** [06:00:10]: We're here for a demo, right?

**Nikolett Szeplaki Esq** [06:00:11]: So I'll just quickly remind you first what you will be seeing, and then I'll show you directly.

**Nikolett Szeplaki Esq** [06:00:17]: So I don't want to take up too much of your time.

**Nikolett Szeplaki Esq** [06:00:24]: It is basically the core functionalities.

**Nikolett Szeplaki Esq** [06:00:27]: So as a reminder, we have core advanced and then professional functionalities.

**Nikolett Szeplaki Esq** [06:00:35]: That's how we basically sliced it up.

**Nikolett Szeplaki Esq** [06:00:37]: And the MVP, the minimum viable product, would be the core functionalities, which includes a document forecasting function.

**Nikolett Szeplaki Esq** [06:00:45]: That is basically the intelligence layer of the entire process.

**Nikolett Szeplaki Esq** [06:00:51]: So that intelligence layer knows exactly what are the AML- KYC requirements per jurisdiction.

**Nikolett Szeplaki Esq** [06:00:58]: So we talked about that.

**Nikolett Szeplaki Esq** [06:01:00]: One of the big advantages of this tool is that it's multi-jurisdictional, which means it cannot only handle multiple jurisdictions within the UAE, but also globally.

**Nikolett Szeplaki Esq** [06:01:11]: So for example, if you hold licenses in ADGM and SCA and then you want to expand to, God knows, to Switzerland or whatever.

**Nikolett Szeplaki Esq** [06:01:20]: That's already three, four jurisdictions whose rules and regulations you need to keep in mind.

**Nikolett Szeplaki Esq** [06:01:26]: And they are all asking for slightly different things for the same entity.

**Nikolett Szeplaki Esq** [06:01:31]: So our strength is to fine tune that, and it's the intelligence layer that does that.

**Nikolett Szeplaki Esq** [06:01:37]: So when we initiate the case, intelligence layer kicks in, and based on the information it has available, forecast the data and document requirements.

**Nikolett Szeplaki Esq** [06:01:47]: Then using those, it actually goes into outside sources to get the screening done.

**Nikolett Szeplaki Esq** [06:01:52]: So the sanction screening, negative news, also does a politically exposed person sweep.

**Nikolett Szeplaki Esq** [06:01:59]: We need to know all that.

**Nikolett Szeplaki Esq** [06:02:02]: Then it assigns the risk ranking based on what it knows and ask for any additional information that it may need.

**Nikolett Szeplaki Esq** [06:02:08]: So that is what you'll be seeing today.

**Nikolett Szeplaki Esq** [06:02:12]: Does that make

**David Orban** [06:02:13]: it up?

**David Orban** [06:02:14]: Yes, it does.

**David Orban** [06:02:15]: All

**Nikolett Szeplaki Esq** [06:02:15]: right, so let me present my screen.

**Nikolett Szeplaki Esq** [06:02:24]: All right, so it's coming up.

**Nikolett Szeplaki Esq** [06:02:27]: What you're seeing is the new case screen.

**Nikolett Szeplaki Esq** [06:02:30]: I logged in already.

**Nikolett Szeplaki Esq** [06:02:32]: I logged in as a user.

**Nikolett Szeplaki Esq** [06:02:35]: So let's say I work in the bank.

**Nikolett Szeplaki Esq** [06:02:38]: I need to start a case.

**Nikolett Szeplaki Esq** [06:02:40]: The way the case is initiated can be several ways.

**Nikolett Szeplaki Esq** [06:02:44]: It can be initiated by me as the user or the client directly.

**Nikolett Szeplaki Esq** [06:02:49]: That is not really important at this point.

**Nikolett Szeplaki Esq** [06:02:52]: What is important is to understand what happens once the case is initiated and what exactly do we need to initiate the case.

**Nikolett Szeplaki Esq** [06:03:01]: You see, I've put in very minimal information.

**Nikolett Szeplaki Esq** [06:03:04]: This is my company.

**Nikolett Szeplaki Esq** [06:03:05]: It's an existing real company.

**Nikolett Szeplaki Esq** [06:03:07]: I just need the name.

**Nikolett Szeplaki Esq** [06:03:09]: I need a contact email to communicate.

**Nikolett Szeplaki Esq** [06:03:12]: And in this case, the jurisdiction.

**Nikolett Szeplaki Esq** [06:03:15]: And I'm starting the case, but before, I'm going to start my timer.

**Nikolett Szeplaki Esq** [06:03:21]: So we can see how long this takes.

**Nikolett Szeplaki Esq** [06:03:23]: Okay, so I'm starting the timer and I'm clicking the button.

**Nikolett Szeplaki Esq** [06:03:27]: And you can see it's already working.

**Nikolett Szeplaki Esq** [06:03:29]: The case is initializing the AI model is starting the analysis.

**Nikolett Szeplaki Esq** [06:03:34]: It's starting to scrape the database.

**Nikolett Szeplaki Esq** [06:03:36]: It's looking in the DIFC registry.

**Nikolett Szeplaki Esq** [06:03:39]: It's assigning the risk ranking.

**Nikolett Szeplaki Esq** [06:03:41]: It's doing the sanction screening.

**Nikolett Szeplaki Esq** [06:03:42]: And I can't even finish describing it.

**Nikolett Szeplaki Esq** [06:03:45]: This was 21 seconds, okay?

**Nikolett Szeplaki Esq** [06:03:49]: In 21 seconds, it basically accomplished everything you see on the right side of the screen, which is It understood that we are dealing with the company.

**Nikolett Szeplaki Esq** [06:03:58]: It understood what documents and data we need based on DIFC regulation.

**Nikolett Szeplaki Esq** [06:04:04]: It went out to the DIFC registry and actually verified my company, so it pulled all the necessary information.

**Nikolett Szeplaki Esq** [06:04:13]: It did a scrape in the sanctions lists.

**Nikolett Szeplaki Esq** [06:04:16]: assigned the risk ranking, did the risk assessment, and drafted an outreach email to the client.

**Nikolett Szeplaki Esq** [06:04:24]: Now we can see all these details on the next screen.

**Nikolett Szeplaki Esq** [06:04:28]: This is what it pulled from the DIFC website directly about my company.

**Nikolett Szeplaki Esq** [06:04:34]: It shows that I'm active, full legal name, registration number, everything that's there.

**Nikolett Szeplaki Esq** [06:04:41]: And it also shows the data sources.

**Nikolett Szeplaki Esq** [06:04:44]: So live DIF registry, known companies, supplemental registries and the aggregated results.

**Nikolett Szeplaki Esq** [06:04:53]: It is also showing the available corporate structure, which is very important for screening because you need to screen directors, shareholders, and the company itself.

**Nikolett Szeplaki Esq** [06:05:03]: So it correctly picked up that I am the director and the shareholder.

**Nikolett Szeplaki Esq** [06:05:07]: I hold all the shares and all the information available.

**Nikolett Szeplaki Esq** [06:05:10]: So this is scraped on its own.

**Nikolett Szeplaki Esq** [06:05:13]: It also did a bit of web intelligence, found my correct website and my own LinkedIn.

**Nikolett Szeplaki Esq** [06:05:19]: built a shareholder tree.

**Nikolett Szeplaki Esq** [06:05:21]: In this case, that tree is very simple.

**Nikolett Szeplaki Esq** [06:05:23]: But in other cases, it may be very complicated, but there are multiple layers.

**Nikolett Szeplaki Esq** [06:05:28]: And I will show you a high risk case as well.

**Nikolett Szeplaki Esq** [06:05:31]: So this is a low risk, easy, low hanging fruit.

**Nikolett Szeplaki Esq** [06:05:35]: Then it did a source of wealth analysis based on what it knows.

**Nikolett Szeplaki Esq** [06:05:39]: So it basically knows what the company does and where my wealth comes from.

**Nikolett Szeplaki Esq** [06:05:45]: So it combined that, but also flagged that we'll need to verify it further because it's not clear whether the company has revenue streams or not, which is fair.

**Nikolett Szeplaki Esq** [06:05:55]: It's a new company.

**Nikolett Szeplaki Esq** [06:05:57]: So it flagged for us that there may be a bit of probing to do to complete the source of wealth.

**Nikolett Szeplaki Esq** [06:06:04]: It's showing me the sanction screening results.

**Nikolett Szeplaki Esq** [06:06:06]: I have no sanctions against me, nor does my company, and it classified me as low risk.

**Nikolett Szeplaki Esq** [06:06:12]: Now, What's next is basically to do the client outreach to get those missing data and documents that it could not get from public sources.

**Nikolett Szeplaki Esq** [06:06:24]: So it did its best.

**Nikolett Szeplaki Esq** [06:06:25]: It auto-completed the certificate of incorporation.

**Nikolett Szeplaki Esq** [06:06:29]: We did the DIFC registry extract.

**Nikolett Szeplaki Esq** [06:06:32]: And it also understood who the director and shareholder are.

**Nikolett Szeplaki Esq** [06:06:35]: And DIFC is a legitimate enough source that we can rely on But it also showed me that my passport is missing and there is no commercial license.

**Nikolett Szeplaki Esq** [06:06:45]: basically drafted a client outreach email with which we can go to the client and request those things.

**Nikolett Szeplaki Esq** [06:06:52]: And we can also ask it, this is a bit of a magic to actually contact the client and tell them about the case where it stands.

**Nikolett Szeplaki Esq** [06:07:00]: So I'm going to put in my own phone number and I'm going to initiate a call to myself to give me a case summary.

**Nikolett Szeplaki Esq** [06:07:11]: just to kind of show you what that would look like.

**Nikolett Szeplaki Esq** [06:07:14]: So my phone is ringing.

**Nikolett Szeplaki Esq** [06:07:19]: Hello.

**Nikolett Szeplaki Esq** [06:07:20]: This is the AML Labs compliance team calling with an update on your KYB verification for AML Labs Technology Limited.

**Nikolett Szeplaki Esq** [06:07:29]: Your case is currently in review status.

**Nikolett Szeplaki Esq** [06:07:32]: I have the full details available if you'd like to go through anything specific.

**Nikolett Szeplaki Esq** [06:07:36]: Do you have any questions?

**Nikolett Szeplaki Esq** [06:07:38]: Yes, what documents do I need to complete the case?

**Nikolett Szeplaki Esq** [06:07:44]: Okay.

**Nikolett Szeplaki Esq** [06:07:45]: Currently, we still require the following documents.

**Nikolett Szeplaki Esq** [06:07:49]: A copy of your commercial license and director ID document, preferably a passport.

**Nikolett Szeplaki Esq** [06:07:55]: We haven't received any documents yet.

**Nikolett Szeplaki Esq** [06:08:00]: Okay, thank you.

**Nikolett Szeplaki Esq** [06:08:03]: I'll stop here, you get the idea.

**Nikolett Szeplaki Esq** [06:08:04]: This could actually turn into a conversation.

**Nikolett Szeplaki Esq** [06:08:08]: The aim is to actually give support to the client.

**Nikolett Szeplaki Esq** [06:08:12]: If they don't understand the requirements or they don't know where to get something from, they can actually talk to the assistance as opposed to having to go back and forth with a live person or waiting for an email reply.

**Nikolett Szeplaki Esq** [06:08:26]: Now, what is a very important feature and I don't want to gloss over it is the audit report.

**Nikolett Szeplaki Esq** [06:08:35]: This is usually missing from most most providers out there, but it's in my opinion, having worked in this field is the most important.

**Nikolett Szeplaki Esq** [06:08:45]: This is a snapshot at the time of onboarding, which captures all the information.

**Nikolett Szeplaki Esq** [06:08:50]: It basically tells me everything that I collected what the system made a decision on what data it scraped and from where and it created this very compact audit trail which I can easily show to any regulator if they ask me about the the life cycle of basically the client relationship so you see as

**Nikolett Szeplaki Esq** [06:09:16]: the registry verification director, shareholders, beneficial owners of screening results, web intelligence, and also the analysis that it did on its own with a complete audit trail.

**Nikolett Szeplaki Esq** [06:09:28]: This is not possible to produce in most legacy systems.

**Nikolett Szeplaki Esq** [06:09:33]: And this is where most audits become really onerous because people start scraping this together manually from email exchanges and documents and data stored in different sources.

**Nikolett Szeplaki Esq** [06:09:45]: So I'm trying to prevent that and kind of think in a forward thinking way.

**Nikolett Szeplaki Esq** [06:09:50]: What if you get your first audit?

**Nikolett Szeplaki Esq** [06:09:51]: How will you demonstrate what decisions your compliance officer made and what decisions your system made to actually pass that client?

**Nikolett Szeplaki Esq** [06:10:02]: Now, the reason I wanted to show you a lower risk client first, because this is easy.

**Nikolett Szeplaki Esq** [06:10:06]: And once we get confidence in the system, this can actually pass without human review.

**Nikolett Szeplaki Esq** [06:10:12]: So if we get confident enough that these cases are accurate, this is a very good case for what we call straight through processing.

**Nikolett Szeplaki Esq** [06:10:21]: So without manual intervention or human intervention, this can go from zero all the way to account onboarding.

**Nikolett Szeplaki Esq** [06:10:29]: And that's a very big efficiency gig.

**Nikolett Szeplaki Esq** [06:10:31]: But we'll have to get there.

**Nikolett Szeplaki Esq** [06:10:33]: It's not day one.

**Nikolett Szeplaki Esq** [06:10:35]: We have to build confidence in the system.

**Nikolett Szeplaki Esq** [06:10:38]: So let me stop here before I move on to the high risk.

**Nikolett Szeplaki Esq** [06:10:42]: What specific questions do you have?

**Nikolett Szeplaki Esq** [06:10:43]: Does it make sense?

**David Orban** [06:10:47]: Yes, I have three, questions,

**Nikolett Szeplaki Esq** [06:10:52]: but before that

**David Orban** [06:10:53]: remark, wonderful and very nice to see it in at play And I will be wearing a different hat rather than the AI and innovation enthusiast.

**David Orban** [06:11:08]: I will be the skeptical conservative client representing the regulated entity who is worried about adopting something so science fictiony.

**David Orban** [06:11:24]: What are the models that you are using it?

**David Orban** [06:11:27]: And what is their geographical location?

**Nikolett Szeplaki Esq** [06:11:34]: Well, these are basically proprietary models that we are building, so it's small language models and definitely, my technology partner can answer these better, so maybe I'll just ask him to get back with you on that.

**Nikolett Szeplaki Esq** [06:11:51]: This is obvious.

**David Orban** [06:11:52]: Okay, no problem.

**Nikolett Szeplaki Esq** [06:11:53]: No problem.

**David Orban** [06:11:55]: And you are using multiple models, so for example, the phone call is likely to be done via 11 labs, for example, while other things are done by other models, so each of them needs to be understood in terms of geographical location.

**David Orban** [06:12:21]: The data residency of your own offering of your customers, your users' details, where is that?

**Nikolett Szeplaki Esq** [06:12:36]: Well, it's basically we, our plan is not to store the customer data ourselves.

**Nikolett Szeplaki Esq** [06:12:42]: We're just providing the platform to use it.

**Nikolett Szeplaki Esq** [06:12:45]: So we'll have to define how this information goes into the database of the actual end client.

**Nikolett Szeplaki Esq** [06:12:52]: So we will not be retaining any data if that's what you're asking.

**David Orban** [06:12:57]: And then, you know, ideally, and I have seen systems that work that way.

**David Orban** [06:13:08]: You would be able, you could be able to actually offer the person going through the KYC, KYB process to be contacted via WhatsApp, especially in the region.

**David Orban** [06:13:30]: Yeah.

**David Orban** [06:13:31]: Using that will be very, very powerful.

**David Orban** [06:13:35]: And it is something I recommend you explore.

**David Orban** [06:13:43]: That's

**Nikolett Szeplaki Esq** [06:13:44]: a good point.

**Nikolett Szeplaki Esq** [06:13:46]: quandry I have about that is sharing personal information over WhatsApp, whether that is at all acceptable by the regulator.

**Nikolett Szeplaki Esq** [06:13:55]: I know that real estate firms do it all the time.

**Nikolett Szeplaki Esq** [06:13:58]: They ask you for all the details.

**Nikolett Szeplaki Esq** [06:14:01]: There is still a very big resistance inside of myself as a compliance person because it's not... Of course.

**Nikolett Szeplaki Esq** [06:14:09]: But first I would want to explore how the regulator feels about that.

**Nikolett Szeplaki Esq** [06:14:13]: If they are okay with it, Absolutely.

**Nikolett Szeplaki Esq** [06:14:16]: I can also make it into a communication tool, but if the regulator is not okay with sharing personal information via WhatsApp, I would probably limit that to just being kind of the chat function that you have just seen.

**Nikolett Szeplaki Esq** [06:14:29]: Yeah.

**David Orban** [06:14:31]: And then What you said last is very interesting and I wonder if you explore the regulatory implications.

**David Orban** [06:14:46]: You basically said that you feel that it is okay to go from end to end with AI-assisted processes with no human in the

**Nikolett Szeplaki Esq** [06:15:02]: If it's lower risk than it is.

**Nikolett Szeplaki Esq** [06:15:05]: Yeah, in my view, but I might.

**Nikolett Szeplaki Esq** [06:15:07]: So in an investment bank specifically, one client will not just open one account.

**Nikolett Szeplaki Esq** [06:15:12]: Okay.

**Nikolett Szeplaki Esq** [06:15:13]: So I might preface what I said with saying that when they open their first account.

**Nikolett Szeplaki Esq** [06:15:20]: Maybe it's more prudent to have a human in the loop.

**Nikolett Szeplaki Esq** [06:15:23]: But when subsequent accounts are open for the same person, it is okay to have them go through straight through processing because that's already done today.

**Nikolett Szeplaki Esq** [06:15:34]: Any banking entity that has even minimal automation does that.

**Nikolett Szeplaki Esq** [06:15:38]: So there's the start difference is, for example, HSBC versus Morgan Stanley.

**Nikolett Szeplaki Esq** [06:15:44]: HSBC does not have straight through processing.

**Nikolett Szeplaki Esq** [06:15:47]: In fact, they re-onboard the client every time it does, it opens a new account.

**Nikolett Szeplaki Esq** [06:15:53]: Which is crazy.

**Nikolett Szeplaki Esq** [06:15:55]: It is ludicrous.

**Nikolett Szeplaki Esq** [06:15:56]: Why onboard the same client over and over when all they do is just expand their relationship with you?

**Nikolett Szeplaki Esq** [06:16:03]: Morgan Stanley doesn't do that.

**Nikolett Szeplaki Esq** [06:16:06]: It operates on an order place or principle basis.

**Nikolett Szeplaki Esq** [06:16:09]: So it means you, David Orban, if you have already been onboarded and I have your ID.

**Nikolett Szeplaki Esq** [06:16:15]: I verified your identity and I verified where you live and I did all the screening.

**Nikolett Szeplaki Esq** [06:16:20]: If you come and open multiple accounts with me, even if it's a joint account, you are already clear.

**Nikolett Szeplaki Esq** [06:16:26]: I'm not going to keep asking you for your information.

**Nikolett Szeplaki Esq** [06:16:30]: But for that, even the account, the client reference data structure needs to be set up accordingly so it can handle that.

**Nikolett Szeplaki Esq** [06:16:39]: So I think there are two stages.

**Nikolett Szeplaki Esq** [06:16:42]: Stage number one, it's already accepted practice in the banking industry that once you have onboarded a client, subsequent onboarding, don't need to start over.

**Nikolett Szeplaki Esq** [06:16:53]: So that their straight-through processing is absolutely fine.

**Nikolett Szeplaki Esq** [06:16:58]: Second step would be what if we don't even monitor first initial onboarding because we trust the system so much for a low risk client that we say, okay, if it's low risk and meets this criteria, can open its first account.

**Nikolett Szeplaki Esq** [06:17:13]: That is a bit of a stretch and we'll need to prove that the system is reliable enough and accurate enough and have that kind of risk appetite where we are okay with that.

**David Orban** [06:17:29]: What you mentioned about HSBC is it's not only frustrating, it's infuriating.

**Nikolett Szeplaki Esq** [06:17:36]: And

**David Orban** [06:17:37]: it is the classic bureaucratic wall that clients hate.

**David Orban** [06:17:45]: And I talk about first-person experience.

**David Orban** [06:17:48]: I bank with HSBC.

**Nikolett Szeplaki Esq** [06:17:50]: Oh, there you

**David Orban** [06:17:51]: go.

**David Orban** [06:17:58]: How does the system avoid, if it does already, or it is in your plan, to fall into some similar pattern when we are talking about multiple jurisdictions, where it would be easy and lazy to ask for the maximum number of documents possible rather than the minimum

**Nikolett Szeplaki Esq** [06:18:23]: that

**David Orban** [06:18:23]: satisfies all of them.

**David Orban** [06:18:27]: Is that something that you are planning to map out or have you already?

**David Orban** [06:18:34]: Yeah, that's

**Nikolett Szeplaki Esq** [06:18:35]: very much at the core of what is my expertise, right, to define the base, because the base is always the same.

**Nikolett Szeplaki Esq** [06:18:44]: You're always looking at where the money is coming from, where is it going, who is involved.

**Nikolett Szeplaki Esq** [06:18:51]: So you need to establish that there is, you need to establish you're dealing with person or a company, in case of a company, you need to make sure it's active, and then you go and probe into the individuals, the directors and shareholders.

**Nikolett Szeplaki Esq** [06:19:07]: So there is a base that's acceptable anywhere, anywhere and everywhere.

**Nikolett Szeplaki Esq** [06:19:12]: And I intend to map out the nuances, in fact, to teach the brain, this intelligence layer to be able to forecast the differences only.

**Nikolett Szeplaki Esq** [06:19:22]: Instead of taking the lazy approach, take the most efficient approach where you are building on the base and on the local nuances to actually tweak the list to only ask for what you really need and satisfy multiple jurisdictions that has been my task and specialty during the last six years of my

**Nikolett Szeplaki Esq** [06:19:44]: career with Morgan Stanley

**David Orban** [06:19:47]: All right.

**David Orban** [06:19:48]: Okay.

**David Orban** [06:19:49]: Let's go and see the tricky

**Nikolett Szeplaki Esq** [06:19:51]: case.

**Nikolett Szeplaki Esq** [06:19:52]: Yeah.

**Nikolett Szeplaki Esq** [06:19:52]: Okay.

**Nikolett Szeplaki Esq** [06:19:54]: Just one more thing I want to show you before that is actually, no, that's fine.

**Nikolett Szeplaki Esq** [06:20:02]: Let's go there.

**Nikolett Szeplaki Esq** [06:20:04]: I just want to show you this case is dashboard.

**Nikolett Szeplaki Esq** [06:20:07]: Because right now we are in the user view, right?

**Nikolett Szeplaki Esq** [06:20:10]: So I to see all my cases.

**Nikolett Szeplaki Esq** [06:20:12]: I need to be aware of what the functionalities would be.

**Nikolett Szeplaki Esq** [06:20:15]: that would be required by a user.

**Nikolett Szeplaki Esq** [06:20:17]: So this is just kind of shows all the statuses, the risk rankings, when the case was created, jurisdiction.

**Nikolett Szeplaki Esq** [06:20:24]: This is just an overall dashboard view, which we can enhance into infinity as to what the user wants to see.

**Nikolett Szeplaki Esq** [06:20:33]: In terms of a more complicated case, I'm going to pick one that I know has a sanction hit against And then we are going to see what happens there.

**Nikolett Szeplaki Esq** [06:20:45]: This one, ARC's financial engineering, I know, has some issues with it.

**Nikolett Szeplaki Esq** [06:20:51]: So, as I started, it's already scraping the database, basically, and it's done.

**Nikolett Szeplaki Esq** [06:20:59]: So, in 20 seconds, again, it did all the steps that are on the right side of the screen, and it clearly identified that there is sanctions hit.

**Nikolett Szeplaki Esq** [06:21:10]: So it went through everything, grab the database, try to find the internet footprint, and now here we are with the results.

**Nikolett Szeplaki Esq** [06:21:18]: It's showing me accurately that this entity is actually suspended by the DFSA.

**Nikolett Szeplaki Esq** [06:21:24]: It could find no web intelligence, which is very interesting.

**Nikolett Szeplaki Esq** [06:21:31]: looks like this company is already done.

**Nikolett Szeplaki Esq** [06:21:33]: They close the website, they don't even have a digital footprint anymore.

**Nikolett Szeplaki Esq** [06:21:39]: And we could find no information on the UBOs.

**Nikolett Szeplaki Esq** [06:21:44]: So what it did for me, it analyzed the risk indicators.

**Nikolett Szeplaki Esq** [06:21:48]: alerted me to the fact that there is a sanctions match by the US Department of Treasury.

**Nikolett Szeplaki Esq** [06:21:55]: So there are multiple sanctions sources.

**Nikolett Szeplaki Esq** [06:21:57]: This is one of them, and this is a direct hit for the entity.

**Nikolett Szeplaki Esq** [06:22:02]: And based on that, it elevated the risk from the initial medium that it gave it to high.

**Nikolett Szeplaki Esq** [06:22:08]: So here are basically the risk factors, which in the real MVP we will define based on FATF and local regulations, what those risk factors look like.

**Nikolett Szeplaki Esq** [06:22:21]: It also forecasted documents based on the entity type.

**Nikolett Szeplaki Esq** [06:22:25]: You see how the documents because this is a high- risk client.

**Nikolett Szeplaki Esq** [06:22:28]: It's a much longer list.

**Nikolett Szeplaki Esq** [06:22:30]: So it's not just mindlessly forecasting the same thing.

**Nikolett Szeplaki Esq** [06:22:33]: You saw how short my list was for a low-risk entity.

**Nikolett Szeplaki Esq** [06:22:38]: And now this one is way longer because of the high-risk nature.

**Nikolett Szeplaki Esq** [06:22:44]: But not only that, it also drafted an outreach and escalation to the compliance officer.

**Nikolett Szeplaki Esq** [06:22:50]: which we can send within the workflow.

**Nikolett Szeplaki Esq** [06:22:52]: It doesn't need to be emailed, but this is just a demonstration that actually did an escalation email outlining all the problems, number one being the sanctions match, the regulatory suspension, that we have no information about beneficial ownership.

**Nikolett Szeplaki Esq** [06:23:09]: And now we move on to the human in the loop review, where that human needs to decide whether to outright reject the case or accept the case or basically whether they need more information.

**Nikolett Szeplaki Esq** [06:23:22]: So this is a more complicated case and it plays out a bit differently.

**Nikolett Szeplaki Esq** [06:23:27]: But we still get the same thing.

**Nikolett Szeplaki Esq** [06:23:29]: So we can see the data sources, we can even see the audit trail, I can show it to you.

**Nikolett Szeplaki Esq** [06:23:37]: And then here we have approved, rejected, request more information, which is more internally for the compliance officer.

**Nikolett Szeplaki Esq** [06:23:45]: I'll show you this audit trail as well.

**David Orban** [06:23:50]: So, I don't know if it is time already for questions.

**David Orban** [06:23:57]: Yes, anytime it's time

**Nikolett Szeplaki Esq** [06:23:58]: for questions.

**David Orban** [06:24:08]: avoiding to lose time with a client that is so evidently someone you cannot on board very useful and there will be a certain number where the case is very clear and don't know if I mean, whether that is handled automatically or not, whether the rejection or declining to service their needs is

**David Orban** [06:24:42]: something that the AI writes and says, or how it happens, the relationship manager telling them, sorry, we cannot do business with you, whatever it is.

**David Orban** [06:24:56]: What do you expect will be the role of the system in the borderline cases, and how will your users integrate the platform in their decision- making process where they can legally on board the client and from a regulatory point of view it is fine but based on the dynamics or based on the mission of

**David Orban** [06:25:32]: the of the company.

**David Orban** [06:25:35]: They just decide that they don't want to deal with those particular categories of borderline cases.

**David Orban** [06:25:48]: Do you expect that you will be able to integrate additional parameters or additional learning even in the system that helps with that or, I mean, for sure, the MVP, but even further along, you believe that should be left outside of the system.

**Nikolett Szeplaki Esq** [06:26:13]: Well, what we can do in that case, I definitely wouldn't send an immediate rejection to obviously.

**Nikolett Szeplaki Esq** [06:26:22]: What I would do in this case is escalate, because there may be a mistake, maybe they just didn't use the right entity.

**Nikolett Szeplaki Esq** [06:26:30]: There is another entity that is perfectly functional and meets our criteria.

**Nikolett Szeplaki Esq** [06:26:36]: And this is the way I would handle it is to summarize everything that we found, instead of having the compliance officer to look into it one by one and do string searches, which they do today actually spend a lot of time on additional research.

**Nikolett Szeplaki Esq** [06:26:51]: We would just give them all the information to make an informed decision and then leave it up to them to communicate with the relationship manager.

**Nikolett Szeplaki Esq** [06:27:02]: At the end of the day, the relationship manager probably the most human element of all this, because they have direct contact with the client, and that has its own sensitivities, its own strategies as to how you talk to a high net worth client or a family office, etc.

**Nikolett Szeplaki Esq** [06:27:21]: even attempt to try to automate that.

**Nikolett Szeplaki Esq** [06:27:24]: I see my role as giving them maximum information and even additional research can be done through my system by the compliance officer to get comfort, whether to sign off on

**Nikolett Szeplaki Esq** [06:27:43]: or AMLKYC, I'm not police or the regulator.

**Nikolett Szeplaki Esq** [06:27:47]: I just facilitate for them to do the necessary checks as quickly as possible and then make the appropriate risk and business decision.

**Nikolett Szeplaki Esq** [06:27:57]: So I would leave it to company to define its own risk appetite.

**Nikolett Szeplaki Esq** [06:28:03]: Okay.

**David Orban** [06:28:06]: Now, one thing that emerged in the past couple of months and it is getting adopted very widely in AI tools is, on one hand, the ability to schedule tasks that get executed periodically, and on the other hand, even more ambitiously, aggressively, a proactive attitude where the tool and the platform

**David Orban** [06:28:37]: either suggests or actually executes things that were not directly asked by the user of the tool.

**David Orban** [06:28:47]: And the applicability to your case of this trend, which really has just started over the past couple of months, is that

**David Orban** [06:29:05]: The duties are not done just because someone is on board, they are ongoing.

**Nikolett Szeplaki Esq** [06:29:13]: Exactly.

**David Orban** [06:29:14]: And so whether it is every month, every three months or on a near real-time basis, but the platform could support that.

**David Orban** [06:29:27]: And the second, and not enough of a specialist to even hypothesize what that could be.

**David Orban** [06:29:36]: But the platform could look at the blind base more holistically, both in their aggregate as well as how they evolved in time.

**David Orban** [06:29:57]: allow the user to reason about whether, I don't know, their team is going in the right direction and onboarding clients that that are well aligned with with the goals or for whatever reason they are started they started to to develop opportunities and relationships that are less well aligned and

**David Orban** [06:30:27]: this wouldn't be maybe the deciding factor, but it could be a good component in understanding strategic views of the company.

**Nikolett Szeplaki Esq** [06:30:42]: Yeah, that's actually all.

**Nikolett Szeplaki Esq** [06:30:47]: Well, so let me take it apart.

**Nikolett Szeplaki Esq** [06:30:50]: So I was hearing two things.

**Nikolett Szeplaki Esq** [06:30:52]: One is the ongoing obligations, which I very much plan for.

**Nikolett Szeplaki Esq** [06:30:57]: But it's in my advanced tool bucket.

**Nikolett Szeplaki Esq** [06:30:59]: That's why I brought back the slides.

**Nikolett Szeplaki Esq** [06:31:01]: So this periodic review automation and the multi- jurisdictional compliance is is considered advanced tools because every jurisdiction we kind of need to train and build out so as we expand we also build our offerings but to touch on periodic review specifically yes it is an ongoing requirement and

**Nikolett Szeplaki Esq** [06:31:24]: this is the one that's the trickiest to do if you do not have the right data model Because at onboarding, onboarding is kind of low- hanging fruit in the way that all the information you receive is fresh.

**Nikolett Szeplaki Esq** [06:31:37]: So you're not dealing with an outdated database that you have to scrape information from.

**Nikolett Szeplaki Esq** [06:31:43]: Just go out into the World Wide Web and these paid providers and you receive things from the client and it's very clean.

**Nikolett Szeplaki Esq** [06:31:50]: But then the next part to make, that's why we need to work with whoever is using the tool to make sure that they store the data and information in a way that when the time comes and they are ready and we are ready, we can apply our periodic review automation on top of that because that needs to be a

**Nikolett Szeplaki Esq** [06:32:09]: scheduled test.

**Nikolett Szeplaki Esq** [06:32:10]: How often do you need to do this periodic refresh of the client depends on the risk ranking of the client.

**Nikolett Szeplaki Esq** [06:32:17]: So the risk ranking needs to be monitored.

**Nikolett Szeplaki Esq** [06:32:20]: Any ongoing sanctions hits, sanctions, PEP, negative news hits need to be taken into consideration between Boomboarding being completed and periodic review starting because if we get a hit in between that might alter the risk ranking of the client, which brings the review forward.

**Nikolett Szeplaki Esq** [06:32:39]: So there is an art to it, like for example, in the high risk client, you do refresh yearly, medium risk every two years, low risk every three years, it's a big drain on resources, right?

**Nikolett Szeplaki Esq** [06:32:51]: So let's say you have a risk ranking that is kind of, it's active, it's not, it's not, a static score that remains like that forever and ever.

**Nikolett Szeplaki Esq** [06:33:01]: People can become peps or they can get a sanctions hit or do something that doesn't please the regulator and then get on some list.

**Nikolett Szeplaki Esq** [06:33:11]: Our ongoing monitoring, every company needs to have ongoing monitoring will inform us.

**Nikolett Szeplaki Esq** [06:33:17]: So that is a trigger event, first of all, when we get additional information from the client.

**Nikolett Szeplaki Esq** [06:33:23]: And we need to be able to use that trigger event to schedule the upcoming review or either start it immediately.

**Nikolett Szeplaki Esq** [06:33:30]: So it's very much in my plan because I want to provide really, truly an end-to-end client life cycle relationship with goes from onboarding to trigger event to periodic review to potential offboarding the client becomes, let's say, inactive.

**Nikolett Szeplaki Esq** [06:33:48]: So that was one.

**Nikolett Szeplaki Esq** [06:33:49]: And then did I answer that your satisfaction?

**David Orban** [06:33:53]: Yes, and the second was to see both in aggregate and in time how these profiles support the companies' business

**Nikolett Szeplaki Esq** [06:34:10]: development.

**Nikolett Szeplaki Esq** [06:34:11]: Yes.

**Nikolett Szeplaki Esq** [06:34:12]: And the answer is, again, yes, especially because We plan on having very detailed audit trail.

**Nikolett Szeplaki Esq** [06:34:22]: So what can we glean from a good audit trail?

**Nikolett Szeplaki Esq** [06:34:25]: From an audit trail, we can pull, okay, what is the nature of business for the entities we are onboarding?

**Nikolett Szeplaki Esq** [06:34:31]: Where is their source of wealth coming from?

**Nikolett Szeplaki Esq** [06:34:33]: Are we getting very risky going into things like mining and oil extraction and a lot people from high risk jurisdictions.

**Nikolett Szeplaki Esq** [06:34:45]: What is our risk profile looking like?

**Nikolett Szeplaki Esq** [06:34:47]: We can't look at that.

**Nikolett Szeplaki Esq** [06:34:49]: We can also look at what decisions are the humans making.

**Nikolett Szeplaki Esq** [06:34:53]: Do we keep overriding very risky cases and accepting them into our portfolio, or are we being too conservative and turning clients away that are not even that risky, but we are afraid to make the risk decisions to work with them?

**Nikolett Szeplaki Esq** [06:35:07]: There's all kinds of information we can glean about the organization, only if we do the audit trail, right, and storing the information, right?

**Nikolett Szeplaki Esq** [06:35:16]: That's kind of my soapbox data.

**David Orban** [06:35:21]: Yeah,

**David Orban** [06:35:35]: applicability of AI, of course, to lot of processes is wonderful.

**David Orban** [06:35:46]: And depending on the approach, it supports or needs either a lot of work or some additional post hoc reasoning make it explainable.

**David Orban** [06:36:06]: We didn't look at the summaries too much in detail.

**David Orban** [06:36:12]: I remember a paragraph or two that explain why a given risk score has been attributed to a potential client.

**David Orban** [06:36:31]: How do you, how do you, how strongly you feel that these explanations are are important and how, as a consequence, how do you expect to, what do you expect from them?

**Nikolett Szeplaki Esq** [06:36:50]: Well the risk score is usually based on very clear factors.

**Nikolett Szeplaki Esq** [06:36:58]: I would say about 80% of risk factors is very clear.

**Nikolett Szeplaki Esq** [06:37:03]: Like, are you from a high risk jurisdiction?

**Nikolett Szeplaki Esq** [06:37:05]: Yes or no.

**Nikolett Szeplaki Esq** [06:37:06]: Is the company from a high risk jurisdiction?

**Nikolett Szeplaki Esq** [06:37:09]: Yes or no.

**Nikolett Szeplaki Esq** [06:37:10]: Are you mining?

**Nikolett Szeplaki Esq** [06:37:11]: Are you a casino?

**Nikolett Szeplaki Esq** [06:37:12]: Are you a money service business?

**Nikolett Szeplaki Esq** [06:37:14]: Yes or no.

**Nikolett Szeplaki Esq** [06:37:15]: So there is like no real decision to be made.

**Nikolett Szeplaki Esq** [06:37:18]: Where it becomes an art a little bit is the source of wealth.

**Nikolett Szeplaki Esq** [06:37:23]: like kind of gathering enough data to understand where and usually that's very rare that for example for high net worth individuals or an opaque structure it's available online so a little probing and research combined with information from the client that's where the source of wealth will be born

**Nikolett Szeplaki Esq** [06:37:44]: from but everything else is kind of black and white so It's important and it's relatively easy to code, except maybe the source of wealth.

**Nikolett Szeplaki Esq** [06:37:54]: And it does become important because it changes everything about the client.

**Nikolett Szeplaki Esq** [06:37:58]: It changes the frequency with which you look at it again and again, like the refresh schedule.

**Nikolett Szeplaki Esq** [06:38:05]: It also, for high-risk clients, you need more information.

**Nikolett Szeplaki Esq** [06:38:09]: collect more data and document you need to do enhanced the diligence it's much more operational work and more onerous for the client as well so it's important to fine-tune your risk ranking in the way that doesn't hinder business entirely but still needs regulatory requirement and there is some

**Nikolett Szeplaki Esq** [06:38:30]: leeway in that i mean some actually some firm still person calculates it manually based on factors and there is a human decision whereas other more advancement have an algorithm and like kind of a probability analysis in in i mean obviously it's black and white that you don't explain to the and

**Nikolett Szeplaki Esq** [06:38:59]: Sorry, the the customer of your client, right?

**Nikolett Szeplaki Esq** [06:39:05]: The UBO that you are filing a suspicious activity report on them.

**Nikolett Szeplaki Esq** [06:39:10]: Of course, you can't.

**Nikolett Szeplaki Esq** [06:39:13]: You are

**David Orban** [06:39:14]: not allowed.

**David Orban** [06:39:14]: You are not allowed.

**David Orban** [06:39:15]: On the other hand, I wonder what is the tension or even the contradiction between some of those requirements the desire an entity to cultivate relationships.

**David Orban** [06:39:37]: And certain jurisdictions like Europe where high- risk AI applications cannot make automated decisions, they need to be explainable AI is a big

**Nikolett Szeplaki Esq** [06:39:58]: thing in Europe, right?

**David Orban** [06:40:00]: And it is a bit like when GDPR requests to require you to delete customer data, and then guess what?

**David Orban** [06:40:11]: In particular, their email actually should be very, very secret blacklist Otherwise you risk of sending them an email because you inadvertently reacquire their address

**Nikolett Szeplaki Esq** [06:40:26]: because

**David Orban** [06:40:26]: they enter it in a form or you bought a list from a legitimate source that includes but they already told you not to send an email.

**David Orban** [06:40:38]: So you have the high priority, no email ever list, which includes

**Nikolett Szeplaki Esq** [06:40:45]: them.

**David Orban** [06:40:48]: violating the letter of the GDPR, but following the spirit of the GDPR, right?

**David Orban** [06:40:57]: So, and I speak from experience because am active in crypto.

**David Orban** [06:41:07]: And, and you know, I have multiple banking relationships, and some of them are

**Nikolett Szeplaki Esq** [06:41:13]: still,

**David Orban** [06:41:14]: they are still in panic.

**David Orban** [06:41:17]: They, they have an allergic fit if they hear the word crypto, right?

**David Orban** [06:41:23]: let alone receiving a wire transfer from a crypto exchange that is the result of you having sold crypto into fiat and then sending them the money and they go like oh my god look at where this money is coming

**Nikolett Szeplaki Esq** [06:41:38]: yeah so

**David Orban** [06:41:41]: but but still even in those cases you know and in the crypto industry this is legendary that that the banking has been so pervasive as to lead to reforms or at least attempted reforms in Canada and in other places because it was very frequent, never explained, always totally opaque.

**David Orban** [06:42:22]: I wonder what do you think your platform could help with that and how you see that in general.

**Nikolett Szeplaki Esq** [06:42:36]: There's a lot to unpack here, so I'm trying to locate the precise question here.

**David Orban** [06:42:42]: Well, the simplest way, well, not the simplest, the most ambitious way to look at it is, And how do you think the AML posture of KYB, not AM.

**David Orban** [06:43:05]: How do you think the KYB posture of financial institutions should evolve with richer understanding and Is it too ambitious to believe that it could even help regulators?

**Nikolett Szeplaki Esq** [06:43:30]: I don't think it's too ambitious because what I'm trying to create actually creating more transparency for 95% of the cases.

**Nikolett Szeplaki Esq** [06:43:45]: focus is not so much on the edge cases, because there will always be the hard cases, the tough cases where multiple escalations and decisions need to be made, but for the rest that are kind of low hanging fruit, a low or medium risk client who just wants to invest, wants to open an account, why make

**Nikolett Szeplaki Esq** [06:44:06]: it so hard for them?

**Nikolett Szeplaki Esq** [06:44:07]: So the premise, basically what I'm pushing here and what I'm promoting Let's make those cases the most efficient they can be with a clear audit trail that also helps regulators to understand as to how institution is thinking about this whole AML-K-YB, whether they have the logic right.

**Nikolett Szeplaki Esq** [06:44:33]: I think it would make everyone's lives easier, but there will always be the reluctance to deal with crypto providers that you're describing.

**Nikolett Szeplaki Esq** [06:44:42]: I've lived it as well.

**Nikolett Szeplaki Esq** [06:44:46]: I think where I see that becoming an issue is with the source of wealth, you know, pulling the source of wealth of an individual together.

**Nikolett Szeplaki Esq** [06:44:56]: And that will always depend on the risk appetite of that particular organization as how much of that they accept or not.

**Nikolett Szeplaki Esq** [06:45:03]: So that I don't think my platform can change.

**Nikolett Szeplaki Esq** [06:45:11]: audits a lot more straightforward, show the regulator the good intentions behind the operations you're doing your best to abide by the law.

**Nikolett Szeplaki Esq** [06:45:22]: And this is the way you're thinking about it, and this is the way you're pulling and storing your information.

**Nikolett Szeplaki Esq** [06:45:28]: So in my mind, it would create efficiency and accuracy, which both parties could benefit from regulator and the bank or financial institution.

**David Orban** [06:45:40]: The last is more of a remark than not a question, because obviously in your MVP or obviously I believe in your MVP is not going to be there.

**David Orban** [06:45:53]: But another trend, very important in SaaS platforms is their ability to interface other tools, either via APIs or via MCP.

**David Orban** [06:46:10]: In particular, the ability to be friendly towards AI tools that can then deep and the integration of your platform within the organization in a seamless manner.

**David Orban** [06:46:24]: And I would strongly encourage you to put it relatively high on your roadmap of futures to be

**Nikolett Szeplaki Esq** [06:46:35]: implemented.

**Nikolett Szeplaki Esq** [06:46:37]: Well, even the MVP itself will be able to do that.

**Nikolett Szeplaki Esq** [06:46:41]: So I don't plan all the screening and those background things that you saw going on.

**Nikolett Szeplaki Esq** [06:46:47]: those will we will be connecting to another provider i'm not going to build my own screening system when for example comply advantage is available and it seems like a very agile amazing tool to tap into that's and everything we are building is modular like i also want to cater to the companies that

**Nikolett Szeplaki Esq** [06:47:08]: already have something in place but maybe they don't have this intelligence layer that can forecast regulatory requirements for them, or they don't have the document review part.

**Nikolett Szeplaki Esq** [06:47:21]: They should be able to buy modular parts of what I'm building.

**Nikolett Szeplaki Esq** [06:47:25]: And I'm not sure if this is the same to what you're referring, but definitely modularity is high on my list and also not necessarily building everything, but tapping into other sources.

**David Orban** [06:47:37]: Yeah, so it is the complement to that, where rather than talking about how easy it is for you to build a tool, it is how easy for your users to integrate the tool into their systems.

**David Orban** [06:47:51]: Yeah, yeah, I agree.

**David Orban** [06:47:53]: So not only leveraging those connections, but exposing similar connections to your users.

**Nikolett Szeplaki Esq** [06:48:01]: Yeah, makes sense.

**David Orban** [06:48:05]: All right, so thank you very much.

**David Orban** [06:48:07]: This was very useful and I am definitely going to continue championing your evaluation, the evaluation of your platform inside Alibwan.

**David Orban** [06:48:32]: We just hired the head of IT that is going to allow me to go back and concentrate to innovation that that I did the before this interval started three, four months ago.

**David Orban** [06:48:56]: I don't know whether employing a tool like this will fall into one or the other of these two baskets, but I will make sure that the new person joining is aware of our conversation.

**David Orban** [06:49:10]: I know that you are also having ongoing ones with other people.

**David Orban** [06:49:16]: As you said, you are starting to know everyone.

**Nikolett Szeplaki Esq** [06:49:21]: Yeah, I mean, I have, so Charlie is the next one, but I'm having a bit of a hard time pinning him down for an actual appointment, but hopefully tomorrow will be

**David Orban** [06:49:33]: okay, okay, well, keep me up to date.

**David Orban** [06:49:36]: Thank you very much, congrats for having reached so far so past as being able to show the platform and I don't know how far you are from actually putting in the hands of of paying customers, but that will be of course the next wonderful milestone.

**Nikolett Szeplaki Esq** [06:50:03]: Well, you know, it all depends on the technology partner that you haven't met yet.

**Nikolett Szeplaki Esq** [06:50:08]: So it's an ex-colleague of mine from Morgan Stanley.

**Nikolett Szeplaki Esq** [06:50:11]: He's the one who helped put this demo together.

**Nikolett Szeplaki Esq** [06:50:15]: If we can come to an agreement that he does this for sweat equity for me, then we can have a minimum viable product by the end of April.

**Nikolett Szeplaki Esq** [06:50:24]: So very fast.

**David Orban** [06:50:25]: Wonderful.

**David Orban** [06:50:26]: That would be

**Nikolett Szeplaki Esq** [06:50:27]: a big win, but we are still negotiating, so I'm hopeful.

**David Orban** [06:50:32]: Okay.

**David Orban** [06:50:33]: Thank you very much.

**David Orban** [06:50:34]: Thank you.

**David Orban** [06:50:35]: Have day.

**David Orban** [06:50:36]: Bye-bye.

---
*Backed up from MeetGeek on 2026-03-30 08:42*
