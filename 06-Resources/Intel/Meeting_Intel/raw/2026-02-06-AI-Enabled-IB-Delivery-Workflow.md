# AI‑Enabled IB Delivery Workflow

**Date:** 2026-02-06
**Duration:** Unknown
**Meeting ID:** 2cd68094-65d8-4bb4-b731-9065666d6a27

## Participants
- *Participants not listed*

### Summary

The meeting focused on defining and templating an end-to-end IB origination-to-delivery workflow and leveraging AI (Claude skills/plugins) to automate templates, folder structures, and CRM enrichment. Attendees discussed practical steps: consolidating existing IB documents into a single folder, training AI on IB profiles and branding, using AI to generate proposals/teasers and pitch training with recorded feedback, and standardizing data room features (watermarking, analytics). Operational tooling choices and integrations were debated (MidGic for recordings, PitchBook API cost vs. browser scraping), and contracting structure (single CSA with internal SLA) and infrastructure risks from rapid AI/compute changes were noted. Several action items were assigned including collecting documents and setting up recording tooling.

## Full Transcript

**Speaker_00** [05:34:46]: for IB.

**Speaker_00** [05:34:47]: Well, this is what we can do.

**Speaker_00** [05:34:50]: And so what this is, is, at least in my world, in the advisory world, we go through an origination process that then goes into a delivery process because we sign a client, In this area of origination, we actually sign a contract.

**Speaker_00** [05:35:10]: So now we have to deliver.

**Speaker_00** [05:35:12]: And so delivery starts.

**Speaker_00** [05:35:13]: And we've already done some of this already in terms of discovery and pitch deck and whatnot.

**Speaker_00** [05:35:20]: But this is the flow that we do.

**Speaker_00** [05:35:23]: But all these things can be templatized.

**Speaker_00** [05:35:26]: you know, meta-ized, templateized in cloud or whatever tool is the best.

**Speaker_01** [05:35:34]: Well, so here is, and this is

**Speaker_00** [05:35:38]: very,

**Speaker_01** [05:35:38]: very, very useful, absolutely.

**Speaker_01** [05:35:42]: So as you know, I want to share my belief that becoming an organization that improves its ability to execute can only come through learning and learning in turn is only possible, or at least at scale, if we have a culture of written communication.

**Speaker_01** [05:36:08]: And as a consequence, while it is great to just chat about something and then, oh, okay, then you will do it, right?

**Speaker_01** [05:36:17]: Yeah, yeah, yeah, I will do it.

**Speaker_01** [05:36:19]: recording as much as possible on Asana is crucial.

**Speaker_01** [05:36:23]: And I see these as two different Asana templates that can get duplicated for each project.

**Speaker_01** [05:36:36]: And what is now very good is that whether co-worked directly or in other ways, humans and AI can work together on a sauna, both filling it, updating it, analyzing it for a critical path, finding gaps.

**Speaker_00** [05:36:57]: Oh, that's true, and all that is right.

**Speaker_00** [05:37:01]: But the thing that will make this just so seamless and powerful is to make sure that co-work has been told what what are the context yeah the good the key context and so for instance before we even do an initial meeting we have We have a template that guides the person having the meeting with the

**Speaker_00** [05:37:38]: target that's based on the investment bank client profile and the new distribution requirements that Greg Wallace putting together.

**Speaker_00** [05:37:47]: And so, and so, so, and then of course that gets recorded, but we have to figure out how to do that part.

**Speaker_00** [05:37:55]: Okay,

**Speaker_01** [05:37:56]: so let me interject there, because just yesterday maybe, Claude released what they call plugins.

**Speaker_01** [05:38:11]: that are shareable collections of skills, and the skills in turn tell Claude exactly these kinds of things about a context.

**Speaker_01** [05:38:23]: So we will be able, rather than just manage a prompt repository, which was one of the questions, Shagin answered it.

**Speaker_01** [05:38:32]: we will be able to manage a repository of skills that will map the behavior of cloud on the practices and processes that IB uses.

**Speaker_01** [05:38:49]: Now, the process is abstract, but it will be also able to translate that into a procedure which is relative to a particular set of tools.

**Speaker_01** [05:39:00]: And I can show you just now an example because yesterday's presentation, because I did it literally 10 minutes before the meeting, the workshop was not on brand.

**Speaker_01** [05:39:17]: So this morning, Claude having announced it, I created the skill that knows everything about only one branding, and I just said, okay, redo the presentation based on this branding,

**Speaker_00** [05:39:34]: right?

**Speaker_00** [05:39:34]: So

**Speaker_01** [05:39:34]: that is an example of how this maps.

**Speaker_00** [05:39:37]: Sure, so we tell Cloud what the IB profile requirements are, including the distribution requirements, and now it knows it forever.

**Speaker_00** [05:39:48]: And so it can go to that.

**Speaker_01** [05:39:50]: Now, what of these do you already exist?

**Speaker_01** [05:39:55]: all of them or

**Speaker_00** [05:39:57]: none of them or some of them.

**Speaker_00** [05:39:59]: Some of them.

**Speaker_00** [05:40:00]: I don't know that, you know, you may have done some things that I don't know, but the origination at up to five, I don't think any of that exists in cloud.

**Speaker_01** [05:40:12]: Well, no, no, no.

**Speaker_01** [05:40:13]: not independently.

**Speaker_01** [05:40:15]: Do these files exist?

**Speaker_01** [05:40:17]: Do these practices exist?

**Speaker_00** [05:40:18]: No, these practices don't exist, but some of the information exists.

**Speaker_00** [05:40:21]: For instance, we have a document that lists the requirements for an IB client.

**Speaker_00** [05:40:27]: We do not have a document that, and we kind of have a document that Nicola created that provides a bit more in terms of distribution requirements.

**Speaker_00** [05:40:40]: So without a huge lift we can have number one, we can

**Speaker_01** [05:40:44]: train.

**Speaker_01** [05:40:45]: The reason I'm asking is because we can do two maybe more things, more approaches.

**Speaker_01** [05:40:52]: One approach is that if most of this exists, I take it, analyze it, maybe refine or restructure, streamline it or make it consistent and coherent, then that's one.

**Speaker_01** [05:41:08]: The other, if most of this does not exist, then I just tell the AI to invent it.

**Speaker_01** [05:41:17]: And then we have to go through to see if actually matches the way that we want to work rather than taking something and then not finding it fit for a purpose.

**Speaker_01** [05:41:25]: So

**Speaker_00** [05:41:26]: it's... Do you recommend the first or the second?

**Speaker_00** [05:41:31]: Well, I think it depends on the... Some of these things are done, and some of these things... Some of these things, the first one would work, and some of the things the second one we'd have to

**Speaker_01** [05:41:40]: do.

**Speaker_01** [05:41:40]: Would it be easy for you to give me what exists, without pointing me in five different directions?

**Speaker_00** [05:41:48]: Sure, I can tell you what exists, and when it doesn't

**Speaker_01** [05:41:52]: exist.

**Speaker_01** [05:41:53]: Giving it to me means, you know, just a folder, one folder.

**Speaker_01** [05:42:00]: the various documents, would you be able to collect them and put them in a spare folder,

**Speaker_00** [05:42:05]: rather than

**Speaker_01** [05:42:05]: me hunting for them, because you

**Speaker_00** [05:42:07]: already

**Speaker_01** [05:42:07]: know where they are.

**Speaker_00** [05:42:08]: Sure, sure, I can do that.

**Speaker_00** [05:42:09]: I can that.

**Speaker_00** [05:42:10]: Let me just tell you, let me just give you a sense.

**Speaker_00** [05:42:16]: A couple of files can be used to create one.

**Speaker_00** [05:42:20]: The Trezrit file template folder structure is, I mean, it's in, if you go to a client and then you see the folder structure, that's what we have to always replicate.

**Speaker_00** [05:42:33]: And I don't

**Speaker_01** [05:42:33]: know how to, You just help co- work, look at that folder structure and create a template.

**Speaker_01** [05:42:39]: Yeah.

**Speaker_00** [05:42:40]: Okay.

**Speaker_01** [05:42:40]: Because it is able to create folders,

**Speaker_00** [05:42:43]: right?

**Speaker_00** [05:42:43]: Right, right, right.

**Speaker_01** [05:42:43]: Subfolders.

**Speaker_01** [05:42:44]: So

**Speaker_00** [05:42:45]: that's easy.

**Speaker_00** [05:42:47]: Yeah.

**Speaker_00** [05:42:48]: Qualifying document, we don't have, we'll have to, you know, this is something that we could tell Cloud to try.

**Speaker_00** [05:42:58]: Yeah.

**Speaker_00** [05:42:59]: And then we could edit it.

**Speaker_00** [05:43:01]: pre- proposal template, we may not need it.

**Speaker_00** [05:43:05]: We may be able to go directly to a proposal template.

**Speaker_00** [05:43:08]: Okay.

**Speaker_01** [05:43:10]: Is this maybe more like a presentation?

**Speaker_01** [05:43:13]: A

**Speaker_00** [05:43:14]: pre-proposal is we go through this to and fro with a client in two meetings where... What we can

**Speaker_01** [05:43:22]: deliver, what do you need and how do they match?

**Speaker_00** [05:43:24]: Yeah, so we go to them and say, what do you need?

**Speaker_00** [05:43:26]: And then they send us, we have a meeting and they send us an email that kind of describe what they, Matt, what they think they need.

**Speaker_00** [05:43:34]: And then we send back a pre-per-polls with saying, is this what you're saying?

**Speaker_00** [05:43:38]: Did we correctly

**Speaker_01** [05:43:40]: understand you?

**Speaker_01** [05:43:41]: And isn't it the case that you didn't ask, but you should be asking for this as well on top?

**Speaker_01** [05:43:46]: Because we know from other experience that it should want it.

**Speaker_00** [05:43:51]: that all of that's true, but psychologically clients don't like things going too fast.

**Speaker_00** [05:43:57]: You can't sit, I mean, I mean in a meeting and I could have all these tools and I could sit there and I could rush them back through this whole process to get where they really need, but there's a gestation or a, you know, there's a digestion thing here where the people have to talk amongst each

**Speaker_00** [05:44:19]: other and do a few things internally, whatever.

**Speaker_00** [05:44:21]: And so we can utilize AI to suggest to them what we think they need, that they may not know what they need off to the side, and we could use that to push them along, but we can't get it too automated because they're gonna react badly, especially in this country.

**Speaker_00** [05:44:47]: Meetings are 80% tit- chat and 20% business.

**Speaker_00** [05:44:53]: Yeah.

**Speaker_01** [05:44:58]: And so this is not, is it like a conversation template?

**Speaker_00** [05:45:05]: Almost?

**Speaker_00** [05:45:06]: Yeah, yeah.

**Speaker_00** [05:45:07]: Like an interaction template.

**Speaker_00** [05:45:08]: It's like... What ends up happening here is it gets to a point where we are fairly confident that it's someone we want to work with here.

**Speaker_00** [05:45:25]: And so then we suggest the kinds of things that we could do, and then they react and say, yeah, we think, We think that we need market entry, we need to raise some money, we need to do these three things.

**Speaker_00** [05:45:41]: We think, yeah, that makes sense.

**Speaker_00** [05:45:43]: Let's do that.

**Speaker_00** [05:45:45]: Or, you know, we want to get into the market and we need to meet some partners or whatever.

**Speaker_00** [05:45:52]: And so they say to their needs in their needs language, but it doesn't match how we think about it, we think about it in terms of market entry and capital raise.

**Speaker_00** [05:46:03]: So we take their thing and then we feed back to them their language with a little bit of our language, because we're gonna have to end up getting to the drafting of the CSA, which is in our language.

**Speaker_00** [05:46:17]: And so so that's what the pre- proposal and proposal template attempt to do is is to match the needs and what we do and get a meeting of the minds in terms of what they would like to do.

**Speaker_00** [05:46:32]: Yeah.

**Speaker_00** [05:46:33]: And so how you do that, we've done it in many, many different ways, but I think that we could use AI to circumvent the pre-proposal template.

**Speaker_00** [05:46:49]: Okay.

**Speaker_00** [05:46:50]: We just jump from here to the proposal template.

**Speaker_00** [05:46:54]: And this is a word document.

**Speaker_00** [05:46:57]: The proposal

**Speaker_01** [05:46:57]: template is a word document.

**Speaker_00** [05:47:03]: There are some elements in our IB team that like doing proposals and slides, and there are some of us that like to do it in a word document, and there's not a, there hasn't been a decision on what we should be doing

**Speaker_01** [05:47:22]: there.

**Speaker_01** [05:47:22]: Well, and the advantage of using AI is that there is an abundance of intelligence So both can be templatized and it is less of an effort to keep them in sync as they change.

**Speaker_01** [05:47:35]: So that's actually good.

**Speaker_01** [05:47:37]: The CSA, however, is the thing, the legal language that gets signed, right?

**Speaker_01** [05:47:43]: Correct.

**Speaker_01** [05:47:44]: Am I right that when both market entry and capital raise are needed, the contracting entities, ALC, however, it subcontracts the market entry back to ALM?

**Speaker_01** [05:47:57]: So

**Speaker_00** [05:47:57]: that's

**Speaker_01** [05:47:58]: correct.

**Speaker_01** [05:47:58]: It is not going to set up a parallel structure to do market entry to ALM.

**Speaker_00** [05:48:04]: No, no, no, no.

**Speaker_00** [05:48:04]: It will not be duplicated.

**Speaker_00** [05:48:06]: The two

**Speaker_01** [05:48:06]: will be the same.

**Speaker_00** [05:48:09]: The CSA will be one CSA with them internally will have something, but the client will never know any of them see that.

**Speaker_01** [05:48:18]: I'm just saying that the people are the same.

**Speaker_01** [05:48:22]: The ALC contract as it develops market entry will use the ALM people.

**Speaker_00** [05:48:30]: Yes, and there's discussions now with this, we're using some consultants that are right there to help us with compliance, and they're teaching us how ADGM is requiring... This is trifecta?

**Speaker_00** [05:48:50]: Yeah, I believe so.

**Speaker_00** [05:48:50]: I believe so.

**Speaker_00** [05:48:52]: Okay.

**Speaker_00** [05:48:53]: I didn't, I wasn't in the meeting, but I believe it's trifecta that's doing it.

**Speaker_00** [05:48:58]: Or it's not them, it's one of these guys.

**Speaker_00** [05:49:01]: I thought it was, I thought it was these guys, because I just saw them all together yesterday in this conference room.

**Speaker_00** [05:49:09]: There's some, there's some audit trail where if The people that do work that's regulated are added up and then there's a fee or a guarantee.

**Speaker_00** [05:49:33]: There's some financial hit.

**Speaker_00** [05:49:37]: based on the number of people that do the regulatory

**Speaker_00** [05:49:53]: there's some way to deal with that that that we have to track.

**Speaker_00** [05:49:56]: Sure.

**Speaker_00** [05:49:57]: And that is one of the reasons why we would do what you just said, where we would sign an ALC contract, and then we would have

**Speaker_01** [05:50:05]: internal A. Yeah.

**Speaker_01** [05:50:07]: An SLA internally.

**Speaker_01** [05:50:08]: Yes.

**Speaker_01** [05:50:09]: So we mentioned the Treasury file template and how we are going to abstract it out of an existing one.

**Speaker_01** [05:50:15]: Correct.

**Speaker_01** [05:50:16]: And for delivery, again, not too much in detail, how much of this does exist, discovery, packaging, distribution.

**Speaker_01** [05:50:25]: in terms of templates, how much does exist?

**Speaker_00** [05:50:28]: Well, the discovery we were working on, so we have quite a bit of that done.

**Speaker_00** [05:50:33]: And then we do have something that, we have an engine that Samuel created And I don't know how, because the tool sets I think are changing.

**Speaker_00** [05:50:46]: I'm not quite sure exactly where that is, but we've been doing that.

**Speaker_00** [05:50:50]: The thing that we don't have, but would be fairly easy to do if we've got this discovery to pitch deck stuff under control is getting the teaser, because it's very formulaic.

**Speaker_00** [05:51:07]: And we could take, we could take the output to the pitch deck and we could create a first version of the teaser.

**Speaker_00** [05:51:16]: You

**Speaker_01** [05:51:17]: mean, I would call it a one page, or the, like,

**Speaker_00** [05:51:20]: yeah.

**Speaker_00** [05:51:21]: It's okay.

**Speaker_00** [05:51:21]: It's one or two pages.

**Speaker_00** [05:51:23]: It depends on, yeah, it just depends on the situation.

**Speaker_00** [05:51:26]: Sure, sure.

**Speaker_00** [05:51:30]: Then, and then packaging is actually a bit more because now Greg and Nicholas say, well, We need more than your ability to pitch.

**Speaker_00** [05:51:43]: We need for there to be, and they're right about this.

**Speaker_00** [05:51:47]: I'm not suggesting that they're wrong about this, but what they want to make sure is in the packaging stage, we also help them build the data room and populate the data room appropriately.

**Speaker_00** [05:51:59]: And then one thing they don't have is, and we need to set up some tracking and and proactively make sure that it gets done is training the pitcher on how to pitch because most of the people that we work with are lousy pitchers and they need four or five dress rehearsals to get into the range of

**Speaker_00** [05:52:29]: being

**Speaker_01** [05:52:30]: okay.

**Speaker_01** [05:52:30]: Do you think they would be, well, because what we could do already is to have someone on camera with them in a meeting, Zoom or whatever, record the meeting, including the video.

**Speaker_01** [05:52:47]: where the AI not only looks at the transcript, but actually the facial expressions, the emotional content, and help the advisor give structured feedback on how to improve the pitching.

**Speaker_00** [05:53:01]: Oh, absolutely would be helpful.

**Speaker_00** [05:53:03]: Okay.

**Speaker_00** [05:53:04]: And what I found is 98% of the time the pitcher loves the training.

**Speaker_00** [05:53:12]: Because they realize it.

**Speaker_00** [05:53:13]: They realize that

**Speaker_01** [05:53:14]: they're... Because it's a low- hanging fruit.

**Speaker_01** [05:53:17]: To get better when you are very bad, it's relatively easy.

**Speaker_00** [05:53:21]: Yeah, and they don't realize how bad they are until they're recorded the first time.

**Speaker_00** [05:53:24]: And then they look at it and they go, oh my God, I'm that bad.

**Speaker_00** [05:53:26]: Yeah,

**Speaker_01** [05:53:27]: yeah, yeah, very good.

**Speaker_01** [05:53:28]: Now, you mentioned the data room.

**Speaker_01** [05:53:34]: Yes.

**Speaker_01** [05:53:35]: Do you expect at the stage where we engage with clients like this that they don't have any data room subscription?

**Speaker_01** [05:53:46]: And so we will provide it to them as part of the engagement itself.

**Speaker_00** [05:53:52]: Many of them already have raised money before, and so they have some kind of a data room.

**Speaker_01** [05:54:00]: Also if they have board meetings with remote board members, distributing board materials.

**Speaker_00** [05:54:06]: Many, you know, these days most of our

**Speaker_01** [05:54:11]: clients have something.

**Speaker_01** [05:54:12]: But maybe it would be useful to have something ready as a backup.

**Speaker_01** [05:54:17]: Just in case,

**Speaker_00** [05:54:18]: right?

**Speaker_00** [05:54:18]: That would be good.

**Speaker_00** [05:54:19]: And

**Speaker_01** [05:54:19]: in that case.

**Speaker_00** [05:54:21]: For two reasons.

**Speaker_00** [05:54:22]: So that they have something that they can use if there's nothing that exists, but also as an example.

**Speaker_01** [05:54:28]: Yeah.

**Speaker_01** [05:54:29]: And am I right that there are some minimum features and that the ability to automatically watermark the documents with the email of the recipient is a good feature.

**Speaker_01** [05:54:44]: Let me tell you why I think that is good.

**Speaker_01** [05:54:47]: Because I very, very dislike it when I receive a URL for a pitch deck where downloading is disabled.

**Speaker_01** [05:54:58]: But I understand on the other side the paranoia of something that is just circulates freely.

**Speaker_01** [05:55:06]: On the other hand, if my email is on the page, then yeah, I'm not gonna just spread it around, right?

**Speaker_01** [05:55:13]: Because I know that the leak will be caught right away.

**Speaker_01** [05:55:20]: So there may be others, but this is, oh, another is of course, statistics, who even opened it.

**Speaker_01** [05:55:30]: Sure,

**Speaker_00** [05:55:30]: it's very

**Speaker_01** [05:55:31]: useful.

**Speaker_01** [05:55:32]: When it is available.

**Speaker_01** [05:55:33]: Who, how much time they spent on the various pages, those kinds of

**Speaker_00** [05:55:40]: things.

**Speaker_00** [05:55:40]: That'd be hugely useful.

**Speaker_00** [05:55:42]: Yeah, yeah, yeah.

**Speaker_00** [05:55:43]: Particularly to distribution, because then they get a sense of whether people really are interested.

**Speaker_00** [05:55:46]: Yeah, okay,

**Speaker_01** [05:55:48]: okay.

**Speaker_01** [05:55:48]: and let's move to the last point of delivery distribution okay so this is this is almost the other funnel for origination origination not of clients but origination

**Speaker_00** [05:56:05]: of

**Speaker_01** [05:56:05]: investors right where we need a smooth workflow that enables enriching a profile in the CRM.

**Speaker_01** [05:56:19]: It's

**Speaker_00** [05:56:20]: not only enriching, it's one of the big problems is just getting people to, see, nobody's like you, nobody's recording everything and doing this all.

**Speaker_00** [05:56:31]: So most people are either don't want to do anything and they want to tell someone else to do it.

**Speaker_00** [05:56:44]: That's one profile.

**Speaker_00** [05:56:45]: And the other profile is they have their preferred thing and they just want to dump a bunch of information in that preferred thing, whether it's Slack, whether it's WhatsApp.

**Speaker_00** [05:56:56]: They just want to dump, they had a meeting, and then they just want to dump it in something and then have someone that relates to the database put it into the form that it needs to be.

**Speaker_00** [05:57:08]: What they don't realize is that they're gonna be either writing it or speaking it anyway.

**Speaker_00** [05:57:14]: So if as long as they had a little bit of training to make sure that they covered, you know, if they had a little cheat sheet of like five things that they have to make sure to say, then they can use AI to do everything else.

**Speaker_00** [05:57:32]: And so part of this is where do we want to go right now?

**Speaker_00** [05:57:38]: I've been working in this area for more than 20 years and never, the only time that you get everything in there is when you've got someone who gets fired if they don't do it, right?

**Speaker_00** [05:57:53]: And we're not gonna do that.

**Speaker_00** [05:57:56]: The way that we are, we're not gonna say, okay, if you don't do this, you're gonna get fired.

**Speaker_00** [05:58:02]: That's not gonna happen.

**Speaker_00** [05:58:03]: But then what's gonna happen is it's just not gonna get done very well and we have to make it the least friction as possible and if, and it seems like the least friction is to do a recording.

**Speaker_00** [05:58:22]: Yeah.

**Speaker_00** [05:58:22]: Is to just, and to teach how to do that recording.

**Speaker_00** [05:58:25]: I had a

**Speaker_01** [05:58:25]: specific meeting about it with ISIL and I'm going to ask her how come she hasn't started testing the workflow that I described.

**Speaker_01** [05:58:37]: I'm curious because it looks to me an important actually low- hanging fruit and we had the Australian dinner and I'm sure since then other meetings or events where this testing could have started.

**Speaker_00** [05:58:58]: I think she's someone that you need to tell her what to do and that she comes up with the thought.

**Speaker_00** [05:59:04]: I don't know that she's worked with AI, so I don't think, I don't know, I just

**Speaker_01** [05:59:09]: don't know.

**Speaker_01** [05:59:10]: She thinks she did, but she doesn't know.

**Speaker_01** [05:59:14]: Okay, so yes, this is the first and then the extracting of contact information that is relevant and well selected.

**Speaker_01** [05:59:26]: So pitchbook wants $11,000 to start using their API.

**Speaker_00** [05:59:37]: What do you mean start using?

**Speaker_01** [05:59:39]: What does that

**Speaker_00** [05:59:40]: mean?

**Speaker_01** [05:59:40]: That I call them up and I said, hey, I want to not click on your stupid screen, but I want to connect our computer to your computer so that we can do the selections, blah, blah, blah.

**Speaker_01** [05:59:52]: And they said, sure, no problem, just hand over $11,000 and then you can start.

**Speaker_01** [05:59:58]: And that includes 11,000 contacts.

**Speaker_01** [06:00:02]: but it is unfathomable to me that they are putting a barrier as high as that to even start.

**Speaker_01** [06:00:09]: Rather than saying, sure, give me a credit card and every 20 contacts, we will charge you $20.

**Speaker_01** [06:00:14]: Okay.

**Speaker_01** [06:00:16]: So that unfortunately for me is a showstopper because I'm not gonna go and ask for, after we pay the subscription, which we are not even using, or not to the degree that we should, to ask

**Speaker_00** [06:00:33]: for

**Speaker_01** [06:00:33]: another $11,000 is just horrible.

**Speaker_01** [06:00:40]: So, I don't know what the solution is, but Well, actually, I had a solution in mind, which is that Claude has a browser plug-in, which is what I mentioned in the workshop when ISIL spoke and she didn't realize that is what she should have been describing, not the spreadsheet that had nothing to do

**Speaker_01** [06:01:11]: with it.

**Speaker_01** [06:01:12]: Linkedin doesn't want, at least PitchTech has an expensive API.

**Speaker_01** [06:01:20]: LinkedIn doesn't even have an API because they don't want you to get access to their data.

**Speaker_01** [06:01:26]: However, Cloud has a browser plugin that allows Claude to click around the screen, select text, copy the text and put it in a spreadsheet, etc.

**Speaker_01** [06:01:39]: etc.

**Speaker_01** [06:01:40]: So what I want to do with PitchDeck is the same, put a computer, tell PitchBook, sorry, PitchBook, put a computer, tell Claude, please find 10 investors of this particular stage industry geography and whatever other parameters and it will do it.

**Speaker_00** [06:02:10]: Yeah, but also even with our database, it's a constraint, it's a constraint, it's constrained and in two ways.

**Speaker_00** [06:02:23]: Peach book is constrained?

**Speaker_00** [06:02:24]: No, no, no, the CRM.

**Speaker_00** [06:02:27]: It's constrained not from cloud doing anything, from people doing anything, because what people will do is they'll go to CR, they won't use cloud.

**Speaker_00** [06:02:41]: What I'm suggesting is why not use cloud for everything?

**Speaker_00** [06:02:44]: So I don't care that it's in, I don't care if it's in pitch book or if I don't care if it's in the CRM system, whatever.

**Speaker_00** [06:02:50]: You just ask cloud.

**Speaker_00** [06:02:52]: You just had a conversation.

**Speaker_00** [06:02:54]: Exactly, exactly.

**Speaker_00** [06:02:55]: Exactly.

**Speaker_00** [06:02:55]: Correct.

**Speaker_00** [06:02:56]: That's what it needs to be.

**Speaker_00** [06:02:57]: Because right now the thinking is it's got to be in the CRM and oh, I have to query the CRM against the field.

**Speaker_00** [06:03:03]: That's what people are thinking.

**Speaker_00** [06:03:04]: Yeah,

**Speaker_01** [06:03:04]: yeah, yeah.

**Speaker_01** [06:03:05]: Okay, so there are two, three different tasks here that are equally important.

**Speaker_01** [06:03:17]: One is to set up the processes in the back end.

**Speaker_01** [06:03:22]: The second is to show and train and excite people in the front end.

**Speaker_01** [06:03:28]: And then the third, which is just absolutely fundamental, is to measure whether it is used, it is helpful, and it is really effective.

**Speaker_01** [06:03:42]: Totally agree.

**Speaker_01** [06:03:43]: This is something that Shervin is very keen on as well.

**Speaker_01** [06:03:47]: And I think Toby too.

**Speaker_01** [06:03:50]: At least two, three people mentioned it to me to make sure that we have a good way to build teams, ad hoc IB teams.

**Speaker_00** [06:04:00]: Yeah.

**Speaker_00** [06:04:03]: New subject.

**Speaker_00** [06:04:06]: Recording.

**Speaker_00** [06:04:08]: We need a standardized way of recording that's not going to be blocked by having to make a payment or whatever.

**Speaker_00** [06:04:14]: So I'm working, I'm having meetings and you're invited and you tentatively accepted.

**Speaker_00** [06:04:20]: So I'm not sure if you're going to be there or not.

**Speaker_00** [06:04:22]: It would be good if you could be there this afternoon's meeting.

**Speaker_00** [06:04:25]: But the initial meeting was recorded by them in Otter.

**Speaker_00** [06:04:28]: I don't have Otter.

**Speaker_00** [06:04:29]: I don't want to yet pay for yet another tool for another bunch of months.

**Speaker_00** [06:04:35]: I need this company to decide that it's going to have

**Speaker_01** [06:04:41]: recording stuff.

**Speaker_01** [06:04:42]: Yes, and the company decided and it is MidGic.

**Speaker_01** [06:04:45]: Okay.

**Speaker_01** [06:04:46]: And I think you even have the invitation to join the Aldiwan team on MidGic.

**Speaker_01** [06:04:52]: and you can start adding...

**Speaker_00** [06:04:56]: Okay.

**Speaker_00** [06:04:57]: Okay, because I have two... This will make it three.

**Speaker_00** [06:05:01]: Two of which, I can't... One is

**Speaker_01** [06:05:04]: personal, one is TG, and now only one.

**Speaker_00** [06:05:06]: Correct.

**Speaker_01** [06:05:07]: Yeah.

**Speaker_00** [06:05:08]: And I can't get them to stop the other two.

**Speaker_01** [06:05:12]: Yeah, I can.

**Speaker_01** [06:05:13]: I will sit down to your computer and do that.

**Speaker_00** [06:05:16]: Okay, all

**Speaker_01** [06:05:16]: right.

**Speaker_01** [06:05:18]: Okay, I also had another subject.

**Speaker_01** [06:05:19]: And by the way, when I do in-person recordings, I always forget that the beginning is good to say who are the participants because our names are not on the windows,

**Speaker_00** [06:05:29]: right?

**Speaker_01** [06:05:30]: So David, of course, isn't always there, and the other is Randy.

**Speaker_01** [06:05:37]: And okay.

**Speaker_01** [06:05:41]: And it may come to me, but what was your other company?

**Speaker_00** [06:05:46]: No, no, no, that was it.

**Speaker_00** [06:05:46]: That was it.

**Speaker_00** [06:05:47]: We just covered it.

**Speaker_00** [06:05:48]: And that is not for me?

**Speaker_00** [06:05:50]: No, no, this is not for you.

**Speaker_00** [06:05:51]: But it's a beautiful mind map.

**Speaker_00** [06:05:52]: I love mind maps.

**Speaker_00** [06:05:54]: This is for Dentalytics, we're trying to figure out how to simplify.

**Speaker_00** [06:05:59]: But who created that?

**Speaker_00** [06:06:02]: Us

**Speaker_01** [06:06:02]: or them?

**Speaker_01** [06:06:03]: Yeah, them.

**Speaker_01** [06:06:03]: Okay, because they've never seen us doing a mind map.

**Speaker_00** [06:06:06]: Yeah, no, this was the... Have you ever used

**Speaker_01** [06:06:09]: mind

**Speaker_00** [06:06:10]: maps?

**Speaker_00** [06:06:11]: Yeah, yeah, I just... It's not how I think.

**Speaker_00** [06:06:15]: Okay.

**Speaker_00** [06:06:16]: Sure.

**Speaker_00** [06:06:18]: So I've used them, but it never really jelled with me because I have a different way of thinking than how mind maps work.

**Speaker_00** [06:06:26]: But

**Speaker_01** [06:06:27]: anyway, so that's all I have.

**Speaker_01** [06:06:29]: So the announcements tonight, I don't know if you saw on Slack, I said there will be some announcements came and they are just mind-blowing.

**Speaker_01** [06:06:42]: The new version of Cloud, OpenAI announced a very, very expensive solution, but I hope Cloud replicates it because it is It is explicitly designing AI coworkers.

**Speaker_01** [06:07:01]: And today it needs special personalization and handholding.

**Speaker_01** [06:07:08]: They put two engineers in your organization and then they design the AI employees.

**Speaker_01** [06:07:16]: Wow.

**Speaker_01** [06:07:17]: And so that's where we are going.

**Speaker_01** [06:07:20]: And for the moment, we will be doing it in-house, but

**Speaker_00** [06:07:24]: yeah.

**Speaker_00** [06:07:24]: That's, yeah.

**Speaker_00** [06:07:26]: And then there's also the articles that I've been seeing late that barely keeping up with the compute, just barely.

**Speaker_00** [06:07:37]: Yeah, well.

**Speaker_00** [06:07:38]: We're gonna hit that, we're gonna hit the wall here soon and many tools.

**Speaker_01** [06:07:42]: Yes, and that is why the announcements by SpaceX are so important because they will be, overcoming the bottlenecks by TSMC not being able to produce enough chips for everyone, and overcoming the bottleneck of not there being enough gas generators, gas turbines to power the data centers, is they will

**Speaker_01** [06:08:06]: build new what they call tarot fabs for chips, and they will deploy one million satellites in space, communicating with lasers to collect solar energy and do inference in space.

**Speaker_00** [06:08:27]: Isn't that going to take a little bit of time?

**Speaker_01** [06:08:29]: the million.

**Speaker_00** [06:08:31]: Well, I mean, or have they already tested it and they know it works and they're... Yeah, yeah.

**Speaker_00** [06:08:36]: So they just, it's just

**Speaker_01** [06:08:37]: a... Starlink is that.

**Speaker_01** [06:08:39]: Starlink satellites,

**Speaker_00** [06:08:40]: they

**Speaker_01** [06:08:40]: are 10,000 now in the orbit.

**Speaker_00** [06:08:43]: They

**Speaker_01** [06:08:43]: already communicate with lasers amongst themselves.

**Speaker_00** [06:08:46]: That's not the part.

**Speaker_00** [06:08:47]: It's the powering.

**Speaker_00** [06:08:49]: The powering.

**Speaker_01** [06:08:50]: Yeah, they are solar powered already.

**Speaker_01** [06:08:53]: The Starlink satellites are solar powered.

**Speaker_00** [06:08:56]: but are they powering compute out in space.

**Speaker_00** [06:09:00]: Yes, because

**Speaker_01** [06:09:02]: they are doing computation.

**Speaker_01** [06:09:04]: They are even doing AI computation.

**Speaker_01** [06:09:07]: Their

**Speaker_00** [06:09:07]: AI

**Speaker_01** [06:09:07]: computation is specialized, it's been forming, it's encryption,

**Speaker_00** [06:09:13]: it's

**Speaker_01** [06:09:13]: all kinds of things.

**Speaker_01** [06:09:15]: So the computation load will shift and the types of chips will be different, more dedicated to it, but it's not, actually it is rocket science because they are launching rockets to deliver them, but yeah, they will do it.

**Speaker_00** [06:09:35]: The government, the government.

**Speaker_00** [06:09:38]: It'll be interesting to see, a lot of people don't want, a lot of people hate Elon Musk.

**Speaker_00** [06:09:43]: And don't trust them.

**Speaker_00** [06:09:44]: Including Michael.

**Speaker_00** [06:09:46]: Yeah, and don't trust him.

**Speaker_00** [06:09:48]: And so it's a scary thought that he's going to be controlling the future of AI.

**Speaker_01** [06:09:54]: Well, the others got to compete better.

**Speaker_00** [06:09:56]: Yeah, yeah, yeah,

**Speaker_01** [06:10:03]: yeah,

**Unknown speaker** [06:10:04]: yeah, yeah, yeah,

**Speaker_01** [06:10:05]: yeah.

**Speaker_01** [06:10:05]: Yeah.

**Speaker_01** [06:10:05]: And actually, almost simultaneously, Amazon, not Amazon, Beezus, Jeff Beezus, and Google.

**Speaker_01** [06:10:12]: and maybe others as well, but I know about these two, announced practically the same thing.

**Speaker_01** [06:10:21]: With less fanfare, less visionary evangelism, a bit more modest scale as well, but they announced the same

**Speaker_00** [06:10:35]: thing.

**Speaker_00** [06:10:35]: Okay.

**Speaker_00** [06:10:38]: Oh, this thing's moving really fast.

**Speaker_00** [06:10:43]: Have you, I have never seen anything that is moving as fast as this.

**Speaker_00** [06:10:49]: Anything that we've ever seen has not been moving this fast.

**Speaker_01** [06:10:53]: When they were with their goggles in the last seconds before in the New Mexico desert, the nuclear explosion went off, that was this fast, but nothing

**Speaker_00** [06:11:09]: else.

---
*Backed up from MeetGeek on 2026-03-30 08:45*
