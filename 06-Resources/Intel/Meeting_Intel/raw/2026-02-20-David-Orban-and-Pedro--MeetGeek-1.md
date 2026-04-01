# David Orban and Pedro: MeetGeek

**Date:** 2026-02-20
**Duration:** Unknown
**Meeting ID:** 6d2406a1-2b88-4929-9d36-e648f1cbce66

## Participants
- *Participants not listed*

### Summary

The meeting focused on four operational topics: (1) David's compliance requirement for UAE data residency and the possibility of customer-hosted storage, (2) centralizing API access so an admin can retrieve team meetings without individual keys and using automation tools to implement workflows, (3) enterprise configuration requests to disable default marketing features (transcript emails, referral widget) and manage defaults for organization-managed users, and (4) integrations and enterprise licensing including confirmation that Pipedrive integration exists and a pledge from Pedro to coordinate sales/engineering on enterprise endpoints and a proposal. Action items center on Pedro escalating technical and sales questions internally and returning a concrete enterprise/endpoint proposal, and David validating team workflow integration and awaiting the residency and enterprise details.

## Full Transcript

**David Orban** [16:31:29]: with Alibon, we are adapting it more broadly.

**Pedro Rezende** [16:31:34]: I

**David Orban** [16:31:35]: went through the flow, and I don't remember enterprise or whatever.

**David Orban** [16:31:43]: It dumped me into an introductory call where I said, sorry, I don't need it.

**Pedro Rezende** [16:31:49]: I'm a pretty advanced user.

**David Orban** [16:31:54]: So let me tell you how we use it now, what we need in the near future, and what we actually would need immediately, okay?

**David Orban** [16:32:02]: So the simplest use case for us today is for... the note- take her to join a meeting.

**Pedro Rezende** [16:32:09]: And

**David Orban** [16:32:10]: then after the meeting, we have workflows that download the transcript extract the tasks and either put it directly in Asana, which is our task management platform, or create a new project, if appropriate, etc.

**David Orban** [16:32:32]: So everything is decided on the fly.

**Pedro Rezende** [16:32:35]: And then

**David Orban** [16:32:37]: assign the tasks directly to the participants if they are named correctly in the meeting already, or since we are also recording in person using the MeetGeek app, the flow asks to name the participants before expecting to be able to assign tasks to people who it doesn't know who they are.

**David Orban** [16:33:09]: And so that is, you know, our basic way of using MidGic.

**David Orban** [16:33:17]: Now, Aldi 1 is a group of unregulated and unregulated companies headquartered in the UAE with offices in Riyadh, London, New York, and Tel Aviv.

**Pedro Rezende** [16:33:38]: And

**David Orban** [16:33:40]: under the

**David Orban** [16:33:47]: oversight of several regulatory bodies, the most important of them being those that regulate financial activities in the UAE.

**David Orban** [16:33:59]: So as far as I understand today, you do not have a a UAE data residency option.

**David Orban** [16:34:10]: And so one of the questions is whether you expect to have that possibility or with Azure or AWS or whoever else, people can bring their own cloud and then just have a meet geek on their cloud.

**David Orban** [16:34:33]: So maybe we can discuss that first.

**Pedro Rezende** [16:34:38]: Yeah, sure, sure.

**Pedro Rezende** [16:34:40]: And honestly, this is not something that I hear Nicole talking about here internally.

**Pedro Rezende** [16:34:47]: We have the two instances, so the US one and the European one.

**Pedro Rezende** [16:34:51]: Those are the two that we already have live.

**Pedro Rezende** [16:34:55]: And AU one would be, yeah, we have actually a set of clients that would probably be helping them.

**Pedro Rezende** [16:35:08]: Yeah, but that's the thing.

**Pedro Rezende** [16:35:10]: I'm being completely honest with you, David.

**Pedro Rezende** [16:35:13]: This is not something that's being talked about internally.

**Pedro Rezende** [16:35:17]: Okay.

**Pedro Rezende** [16:35:18]: So I'm forward this to them, because like I can see, this is something very important for you guys, right?

**David Orban** [16:35:25]: Yes, to the point that sooner or later, we may be forced to stop using the tool.

**David Orban** [16:35:35]: Just, you know, either the regulator or our compliance

**Pedro Rezende** [16:35:39]: officer could

**David Orban** [16:35:40]: put the food down and say, sorry, no can't do.

**David Orban** [16:35:45]: Or at least shop are used in half, you know, not exactly half, but there are unregulated uses, for example, an internal meeting or technology meeting or whatever it is, a vendor meeting,

**Pedro Rezende** [16:36:02]: fine.

**David Orban** [16:36:03]: Client meetings, no, right?

**David Orban** [16:36:06]: So since the most valuable are the client meetings, not being able to use MeetGig for client meetings would be pretty bad.

**David Orban** [16:36:17]: For sure, for sure.

**David Orban** [16:36:19]: Yeah, technically

**Pedro Rezende** [16:36:20]: speaking, I don't know how our team could implement that if we need to buy more storage.

**Pedro Rezende** [16:36:27]: We use AWS, so if we need to buy storage in their instance, so it could be live for the clients.

**Pedro Rezende** [16:36:34]: But I'll talk to them about it, because he's the one that can decide.

**Pedro Rezende** [16:36:40]: And like I said, we have other clients that would probably be also helpful for them so okay

**David Orban** [16:36:46]: perfect so let me mention a few additional things sure The way that we set up the API calls is through individual keys.

**Pedro Rezende** [16:37:00]: And

**David Orban** [16:37:01]: instead what we would like to do is to have a centralized way to manage the conversations because it really feels like the product today looks at the team from a building perspective, but then nothing else.

**David Orban** [16:37:23]: It's fine, it's a first step, but we would want to have the ability with the consent of the individual users who use it in the company, of course, to not have to for each get the API key and then have a multitude of these workflows, but to have it centralized.

**Pedro Rezende** [16:37:54]: But if you don't mind sharing, David, how is it actually set it?

**Pedro Rezende** [16:37:58]: Because I'm trying to understand how you would need all those keeps, like Do you need their meeting content, for example?

**David Orban** [16:38:09]: Yeah, so not of external users, the internal users, right?

**David Orban** [16:38:15]: Colleague, colleague B, colleague C, each use meet geek.

**David Orban** [16:38:20]: And today, unless I am mistaken, there isn't a key available that allows me to download their meetings with a single setup.

**David Orban** [16:38:31]: I need to generate individual keys for each of those.

**David Orban** [16:38:35]: and then juggle the keys in the workflow itself.

**David Orban** [16:38:40]: So my question is,

**Pedro Rezende** [16:38:43]: if

**David Orban** [16:38:45]: there are today or on the roadmap, there are API calls that look at the organization overall.

**David Orban** [16:38:55]: And first of all, of course, to extend our existing workflow.

**David Orban** [16:38:59]: But then, it and other things like provisioning users or stopping users or upgrading users, etc.

**David Orban** [16:39:08]: We believe that today everything should be possible via API, not just a limited set of functions.

**Pedro Rezende** [16:39:19]: No, yeah, for sure.

**Pedro Rezende** [16:39:21]: I was going to say that, I think this is already possible.

**Pedro Rezende** [16:39:24]: If I understood correctly what you need.

**Pedro Rezende** [16:39:27]: But course I just need to understand those users that you have, your internal users.

**David Orban** [16:39:34]: Yes.

**David Orban** [16:39:35]: Are like

**Pedro Rezende** [16:39:36]: they set in different teams or they are like single

**David Orban** [16:39:40]: user.

**David Orban** [16:39:41]: No, no, no, no, no, no, in one team.

**David Orban** [16:39:44]: So I'm talking about, let me share my screen with you,

**Pedro Rezende** [16:39:49]: okay?

**Pedro Rezende** [16:39:50]: Yeah.

**Pedro Rezende** [16:39:54]: Okay.

**David Orban** [16:39:55]: And sorry, I belong.

**David Orban** [16:39:58]: I push the button.

**David Orban** [16:39:59]: Am I here twice now or just once?

**David Orban** [16:40:01]: No, no,

**Pedro Rezende** [16:40:01]: no, just once.

**Pedro Rezende** [16:40:04]: But what I was going to say that I've already built some automations for other clients where we first get the meeting ideas from the team.

**Pedro Rezende** [16:40:12]: So the API call that we do is for the team itself.

**Pedro Rezende** [16:40:16]: We get a list

**David Orban** [16:40:17]: of ideas

**Pedro Rezende** [16:40:19]: and the hosts.

**Pedro Rezende** [16:40:20]: And then after we get this information, we start delivering the other calls, you know.

**Pedro Rezende** [16:40:25]: And at least for what I understood, this could work

**David Orban** [16:40:29]: for you.

**David Orban** [16:40:30]: Okay, great.

**David Orban** [16:40:31]: I will check and then if I stumble upon some roadblock, I will let you know.

**David Orban** [16:40:37]: Now, in the same spirit, we would like not to have to manually tell people to disable certain features that we appreciate your marketing department loves, but your enterprise clients hate, which serve your viral marketing needs, but not necessarily the needs of your users, such as sending everyone,

**David Orban** [16:41:06]: every participant, the transcript by default, rather than keeping it turned off.

**David Orban** [16:41:15]: And if someone wants to turn it on, fine.

**David Orban** [16:41:17]: But we don't need, we are not paid to advertise meet geek and we don't want to advertise meet geek.

**David Orban** [16:41:24]: We want to use meet geek.

**David Orban** [16:41:25]: We are already paying you for using meet geek, so that's

**Pedro Rezende** [16:41:29]: And today,

**David Orban** [16:41:29]: when a new user joins, we have to tell them, turn it off, and they don't turn it off, and then everyone complains.

**David Orban** [16:41:37]: And this is a strong push against using your platform.

**Pedro Rezende** [16:41:42]: I see.

**Pedro Rezende** [16:41:42]: So with

**David Orban** [16:41:43]: individual users, that kind of ride-all marketing trick serves a positive purpose.

**David Orban** [16:41:50]: In an enterprise use case, it is the opposite.

**David Orban** [16:41:54]: People are actively saying, let's not use MeetGeek because it is polluting our conversations.

**David Orban** [16:42:01]: It is the advertising itself to our clients.

**David Orban** [16:42:06]: So we want to have a way to keep using you and turn off those things by default.

**Pedro Rezende** [16:42:17]: Okay.

**Pedro Rezende** [16:42:17]: I can't talk to my engineering team.

**Pedro Rezende** [16:42:21]: Let me just check here's something.

**Pedro Rezende** [16:42:23]: David.

**Pedro Rezende** [16:42:37]: I'm just checking here.

**Pedro Rezende** [16:42:39]: how many users you have and how many

**David Orban** [16:42:42]: users.

**David Orban** [16:42:43]: So right now, you will see we have, you can't check in two ways, right?

**David Orban** [16:42:48]: The team probably has three, four users, not more.

**David Orban** [16:42:52]: And you will say maybe another half a dozen users on the same domain that are not yet part of the team.

**David Orban** [16:42:59]: And we will need to consolidate that.

**David Orban** [16:43:03]: However, we have 60 people now We will be over a hundred in six months.

**Pedro Rezende** [16:43:11]: And I

**David Orban** [16:43:12]: just declared the mid geek to be the standard rather than the hodgepodge of, uh, you know, otter and, and, uh, uh, fire fly and, uh, and,

**Pedro Rezende** [16:43:28]: uh, and,

**David Orban** [16:43:29]: uh, all, all the others.

**David Orban** [16:43:31]: Yeah.

**David Orban** [16:43:31]: And just to confirm the single reason why it's mid geek is because of the API.

**David Orban** [16:43:38]: Okay, very simply.

**David Orban** [16:43:40]: So that is why I'm saying we are in a critical moment when adoption is growing as well as pushback.

**David Orban** [16:43:51]: That is why we need to find a way to turn off the things that make people dislike meet geek now.

**Pedro Rezende** [16:44:00]: For sure, for sure.

**Pedro Rezende** [16:44:03]: That's the only issue that I think we would find every time, even if we find a way to configure for your team to not have this automatic email.

**Pedro Rezende** [16:44:16]: By default, the users would need to be under your management.

**Pedro Rezende** [16:44:20]: I understand.

**David Orban** [16:44:21]: No, I understand.

**Pedro Rezende** [16:44:22]: That would be the only thing for this to work.

**Pedro Rezende** [16:44:25]: Of

**David Orban** [16:44:25]: course, of course, clear.

**Pedro Rezende** [16:44:27]: But for sure, no, we already have this kind of setting.

**Pedro Rezende** [16:44:33]: This normally enabled for the enterprise clients.

**Pedro Rezende** [16:44:37]: And when we say enterprise, it's the actual subscription enterprise level.

**Pedro Rezende** [16:44:44]: And I can talk to my team because I've seen here you, at least under your email, you have two business licenses, right?

**Pedro Rezende** [16:44:55]: The others, there should be more on a free tier.

**Pedro Rezende** [16:45:00]: And we are in the process of upgrading them.

**Pedro Rezende** [16:45:04]: And similarly, if possible, I would like to turn off the referral widget.

**Pedro Rezende** [16:45:16]: Because again,

**David Orban** [16:45:17]: I don't need my team to be distracted by

**Pedro Rezende** [16:45:22]: earning

**David Orban** [16:45:24]: extra $50.

**David Orban** [16:45:24]: Yeah, I can write.

**David Orban** [16:45:27]: Yeah, I'm paying them enough.

**David Orban** [16:45:29]: you know, let them do their job rather than wondering if they should promote MeetGit for $50 more.

**David Orban** [16:45:39]: I will pay them $50 to get that icon off, right?

**David Orban** [16:45:45]: I understand.

**David Orban** [16:45:46]: Yeah, yeah.

**David Orban** [16:45:47]: Honestly, it's

**Pedro Rezende** [16:45:48]: boring for me also, like every time that I didn't try to scroll or do something, I always click there, my mistake.

**Pedro Rezende** [16:45:56]: Honestly, I don't know if this one would be that easy.

**Pedro Rezende** [16:46:00]: Okay.

**Pedro Rezende** [16:46:01]: Only if Dan decided to take it off for everyone.

**Pedro Rezende** [16:46:05]: I think this could be for good, but I don't think we can just take the icon out for you and your

**David Orban** [16:46:12]: team.

**David Orban** [16:46:13]: No, okay, I

**Pedro Rezende** [16:46:14]: understand.

**Pedro Rezende** [16:46:15]: But I can talk to

**David Orban** [16:46:17]: Okay, what else?

**David Orban** [16:46:19]: So I mentioned the big things.

**David Orban** [16:46:25]: Then there are little things like that may matter to people who don't use the API, even though if they click, they see it right there, because you have a certain number of connectors And our current CRM is pipe drive.

**David Orban** [16:46:49]: And you don't have a connector with pipe drive.

**David Orban** [16:46:51]: You have with HopSpot and Salesforce, I think.

**David Orban** [16:46:55]: And so a simple question is whether you have pipe drive on the roadmap at all.

**Pedro Rezende** [16:47:02]: Pipe drive, you learn that it's already here.

**Pedro Rezende** [16:47:07]: Yeah, we already have with Pipe drive.

**David Orban** [16:47:13]: Oh, you have it?

**David Orban** [16:47:14]: I miss that then.

**David Orban** [16:47:14]: That's great.

**David Orban** [16:47:16]: Let

**Pedro Rezende** [16:47:16]: me share my screen here.

**Pedro Rezende** [16:47:20]: I don't know if you're seeing.

**David Orban** [16:47:22]: Yeah, I am seeing it.

**Pedro Rezende** [16:47:24]: You mean, oh, there it is.

**Pedro Rezende** [16:47:25]: Yep, yeah, that one.

**Pedro Rezende** [16:47:26]: Okay, okay, okay.

**Pedro Rezende** [16:47:27]: Perfect.

**Pedro Rezende** [16:47:28]: Yeah, no, I

**David Orban** [16:47:29]: totally miss that.

**David Orban** [16:47:30]: Perfect.

**David Orban** [16:47:31]: Okay.

**David Orban** [16:47:32]: Nice.

**David Orban** [16:47:33]: Oh,

**Pedro Rezende** [16:47:33]: yeah, at least

**David Orban** [16:47:34]: something.

**Pedro Rezende** [16:47:36]: Delivered right now.

**Pedro Rezende** [16:47:37]: So yeah, you can already join here.

**Pedro Rezende** [16:47:39]: You can create the workflows or So like specific, what do you want for it to create?

**David Orban** [16:47:46]: Perfect.

**David Orban** [16:47:49]: Perfect.

**David Orban** [16:47:49]: Perfect.

**Pedro Rezende** [16:47:50]: Okay.

**David Orban** [16:47:52]: And yes, that is of course what I am

**Pedro Rezende** [16:47:57]: using.

**David Orban** [16:47:58]: And so what, how can I A part that I can just make the call and understand.

**David Orban** [16:48:06]: But what about the... Yeah, okay, so that is the theme.

**Pedro Rezende** [16:48:14]: Yeah, what I would recommend to you, let's say you're the manager of the account.

**Pedro Rezende** [16:48:20]: You don't have, like, to have everyone's key.

**Pedro Rezende** [16:48:24]: You just have to be, at least, let me just open here a team, just so you can't understand better.

**Pedro Rezende** [16:48:31]: Oh, I think this one, no.

**Pedro Rezende** [16:48:34]: I'll try to create here.

**Pedro Rezende** [16:48:35]: There is a permission here that you can see everyone can view the meetings, no, UV meetings of others, but they can view yours.

**Pedro Rezende** [16:48:46]: That would be a good configuration.

**Pedro Rezende** [16:48:49]: The configuration itself here, it doesn't matter, right?

**Pedro Rezende** [16:48:54]: It's just to show you there are a different set of rules and you can also set yours.

**Pedro Rezende** [16:48:59]: But you being the admin, you being the owner of this team, every time you do a call to the API, you will get the information of everyone that is inside there, all their meetings, all their meeting IDs, right?

**Pedro Rezende** [16:49:13]: So the flow that you would need to do here.

**Pedro Rezende** [16:49:16]: It's like have only one key, yours, to do the call to the API.

**Pedro Rezende** [16:49:21]: You would do a call for the team meetings.

**Pedro Rezende** [16:49:24]: And after you do the, you'll get all the list of meetings that are inside this team.

**Pedro Rezende** [16:49:31]: You just do a, actually this You just do the get meeting so you can get all the information specifically for the meetings that you want.

**David Orban** [16:49:41]: Perfect.

**Pedro Rezende** [16:49:42]: Yeah, instead of doing that with a lot of things, I think this would be easier.

**David Orban** [16:49:47]: Correct.

**David Orban** [16:49:47]: Absolutely.

**David Orban** [16:49:48]: That is great.

**David Orban** [16:49:50]: All right.

**David Orban** [16:49:51]: Okay, so...

**Pedro Rezende** [16:49:53]: Do you use any kind of automation tool or like, because if I can...

**David Orban** [16:49:58]: What is everyone using?

**Pedro Rezende** [16:50:00]: Well, at least I'm using NHM.

**Pedro Rezende** [16:50:02]: No, I think it's

**David Orban** [16:50:03]: the... Oh, okay, okay.

**David Orban** [16:50:05]: No.

**David Orban** [16:50:07]: We are using... So, Nathan is the workflow tool.

**Pedro Rezende** [16:50:13]: Perfect.

**David Orban** [16:50:15]: But in order to write whatever code, we use Claude.

**David Orban** [16:50:20]: Claude.

**David Orban** [16:50:22]: Sure, for

**Pedro Rezende** [16:50:22]: sure, for sure, for sure, for sure.

**Pedro Rezende** [16:50:26]: Yeah, no, so if you use Claude code, what I would recommend you is actually Give him a command to read our API documentation and just ask him to build this workflow.

**Pedro Rezende** [16:50:37]: You know, get things, a thing, and afterwards, get meeting.

**Pedro Rezende** [16:50:41]: Actually, I have this part.

**Pedro Rezende** [16:50:43]: So it's just another call before it to get the list of meetings.

**Pedro Rezende** [16:50:47]: It will be very, very easy.

**David Orban** [16:50:50]: And is there an API call to create themes?

**David Orban** [16:50:53]: So can I tell Claude, hey, take all the users, put them in a team, set this permission, and then proceed?

**Pedro Rezende** [16:51:02]: No, no, actually the only ones that you have right now to actually do something right it would be to download a meeting or to upload a meeting right so those would be the only ones to create a team you actually need to go on our platform create a team

**David Orban** [16:51:21]: associate so yeah that is that is what i mean uh apis should cover every aspect of a of a platform even claude on tropic doesn't understand that you cannot upgrade your account telling cloud to upgrade it, right?

**David Orban** [16:51:41]: And just like on MeetGeek, there isn't any API call to go from a free license to a business license.

**Pedro Rezende** [16:51:55]: I won't say to you that we don't have that because honestly we do but not like for everyone

**David Orban** [16:52:03]: it's not exposed publicly or it is yeah exactly like the the customers that have the enterprise subscription, they have different calls that they can do

**Pedro Rezende** [16:52:14]: like

**David Orban** [16:52:14]: the ad hoc

**Pedro Rezende** [16:52:16]: meeting, for example.

**David Orban** [16:52:17]: So we will definitely consider using the enterprise license or upgrading to the enterprise license.

**David Orban** [16:52:26]: I assume everyone has to be on the same enterprise tier.

**David Orban** [16:52:30]: It cannot be differentiated by user, is that correct?

**Pedro Rezende** [16:52:34]: No, no, no, you can like, We have a minimum.

**Pedro Rezende** [16:52:38]: It would, like the thing with enterprise that we always like try to fit under your company.

**Pedro Rezende** [16:52:47]: So it's not something called set for everyone, but let's say you have like 50 people using Meet Geek.

**Pedro Rezende** [16:52:54]: We will say like, oh, try to at least five have enterprise levels, so they can be the admins, they can be the managers, and then everyone can be free, they can be pro, it doesn't matter.

**Pedro Rezende** [16:53:04]: Okay, okay,

**David Orban** [16:53:05]: that's great.

**David Orban** [16:53:05]: You

**Pedro Rezende** [16:53:05]: know, just need to record their meetings, it's fine.

**Pedro Rezende** [16:53:10]: But what I can do here also, I'll talk to Carol, because she deals with the sales part itself.

**Pedro Rezende** [16:53:17]: Yeah.

**Pedro Rezende** [16:53:18]: I'll talk to her because, like I said, the enterprise is something more custom.

**Pedro Rezende** [16:53:23]: Yeah.

**Pedro Rezende** [16:53:24]: The feedbacks that you already gave, I can talk to her first, go like, okay, let's try to work something for David.

**Pedro Rezende** [16:53:31]: I'll talk to my engineer, see all the endpoints that we can or cannot give you access to.

**Pedro Rezende** [16:53:37]: And she gives you a proposal, like, okay, you will have this kind of access and five, two, three license minimum should be at her price.

**Pedro Rezende** [16:53:47]: Like, this is something that she can work on.

**Pedro Rezende** [16:53:50]: Okay,

**David Orban** [16:53:50]: perfect.

**David Orban** [16:53:51]: All right, thank you very much for all your help.

**David Orban** [16:53:53]: I'm looking forward to further contact and confirmation.

**David Orban** [16:53:58]: And yeah, hopefully I can overcome the resistance internally and keep using the product that are more widely.

**David Orban** [16:54:08]: For

**Pedro Rezende** [16:54:08]: sure, David.

**Pedro Rezende** [16:54:08]: And like I think I did introduce myself, but I'm your customer success engineer here inside Mikik.

**Pedro Rezende** [16:54:14]: So every time you have any kind of help with the technical part our product, Just send me an email and I'll be out in town.

**David Orban** [16:54:23]: right.

**David Orban** [16:54:23]: Okay.

**David Orban** [16:54:24]: Thank you very much.

**David Orban** [16:54:25]: Good to meet you.

**David Orban** [16:54:26]: Bye.

**David Orban** [16:54:26]: Bye.

---
*Backed up from MeetGeek on 2026-03-30 08:43*
