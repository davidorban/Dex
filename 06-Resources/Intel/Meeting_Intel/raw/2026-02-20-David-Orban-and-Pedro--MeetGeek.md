# David Orban and Pedro: MeetGeek

**Date:** 2026-02-20
**Duration:** Unknown
**Meeting ID:** ed4b9b81-3f96-486f-a602-bfcd84fa86be

## Participants
- *Participants not listed*

### Summary

David described how his company uses MeetGeek as a note-taker feeding transcripts into Asana and emphasized needs for centralized team-level API access, UAE data residency/compliance options, and enterprise controls to disable marketing defaults. Pedro confirmed US/EU instances exist, explained team-level API flows to list meetings and hosts, and committed to escalating UAE residency and enterprise configuration requests to engineering and sales. Both discussed enterprise licensing structure and onboarding needs; Pedro will follow up with engineering and sales to propose enterprise access, pricing, and platform endpoint availability while David will trial the API flow and report any integration roadblocks.

## Full Transcript

**David Orban** [16:31:33]: I went through the flow and I don't remember enterprise or whatever.

**David Orban** [16:31:42]: And it dumped me into an introductory call where I said, sorry, I don't need it.

**Pedro Rezende** [16:31:49]: I'm

**David Orban** [16:31:51]: a pretty advanced user.

**David Orban** [16:31:54]: So let me tell you how we use it now, what we need in the near future, and what we actually would need immediately, okay?

**David Orban** [16:32:02]: So this simplest use case for us today is for the note-taker to join a meeting.

**David Orban** [16:32:10]: And then after the meeting, we have workflows that download the transcript.

**David Orban** [16:32:19]: extract the tasks and either put it directly in Asana, which is our task management platform,

**Pedro Rezende** [16:32:29]: or create

**David Orban** [16:32:29]: a new project, if appropriate, etc.

**David Orban** [16:32:32]: So everything is decided on the fly.

**David Orban** [16:32:35]: And then assign the tasks directly to the participants if they are named correctly in the meeting already.

**David Orban** [16:32:54]: The flow asks to name the participants before expecting to be able to assign tasks to people who it doesn't know who they are.

**David Orban** [16:33:08]: Perfect.

**David Orban** [16:33:09]: And so that is our basic way of using MidGic.

**David Orban** [16:33:17]: Now, AliOne is a group of unregulated and unregulated companies headquartered in the UAE with offices in Riyad, London, New York, and Tel Aviv.

**David Orban** [16:33:45]: under the oversight of several regulatory bodies, the most important of them being those that regulate financial activities in the UAE.

**David Orban** [16:33:59]: So as far as I understand today, you do not have a UAE data residency option.

**David Orban** [16:34:10]: And so one of the questions is whether you expect to have that possibility or with Azure or AWS or whoever else, people can bring their own cloud and then just have a meet geek on their cloud.

**David Orban** [16:34:35]: So maybe we can discuss that first.

**Pedro Rezende** [16:34:38]: Yeah, sure, Honestly, this is not something that I hear people talking about here internally.

**Pedro Rezende** [16:34:47]: We have the two instances, so the US one and the European one.

**David Orban** [16:34:51]: Those are the two

**Pedro Rezende** [16:34:52]: that we already have live.

**Pedro Rezende** [16:34:55]: And a U one would be, yeah, we have actually a set of clients that would probably be helping them.

**Pedro Rezende** [16:35:08]: Yeah, but that's the thing.

**Pedro Rezende** [16:35:10]: I'm being completely honest with you, David.

**Pedro Rezende** [16:35:12]: We, this is not something that's been talked about internally.

**David Orban** [16:35:17]: Okay.

**David Orban** [16:35:18]: So I'm forward this to

**Pedro Rezende** [16:35:20]: them, because like I can see, this is something very important for you guys, right?

**David Orban** [16:35:25]: Yes, to the point that sooner or later, we may be forced to stop using the tool.

**Pedro Rezende** [16:35:35]: Just, you know, either the

**David Orban** [16:35:37]: regulator or our compliance

**Pedro Rezende** [16:35:39]: officer

**David Orban** [16:35:40]: could put the food down and say, sorry, no can't

**Pedro Rezende** [16:35:44]: do, or

**David Orban** [16:35:46]: at least Chop are used in half, you know, not exactly half, but there are unregulated uses, for example, an internal meeting or technology meeting or whatever it is, a vendor meeting,

**Pedro Rezende** [16:36:02]: fine.

**David Orban** [16:36:03]: Client meetings, no, right?

**David Orban** [16:36:06]: So since the most valuable are the client meetings, not being able to use MeetGig for client meetings would be pretty bad.

**David Orban** [16:36:17]: For sure, for sure.

**David Orban** [16:36:19]: Yeah,

**Pedro Rezende** [16:36:20]: technically speaking, I don't know how our team could implement that if we need to buy more storage in, we use AWS.

**Pedro Rezende** [16:36:28]: So if we need to buy storage in their instance, so it could be live for the clients.

**Pedro Rezende** [16:36:35]: But I'll talk to them about it.

**Pedro Rezende** [16:36:37]: because he's the one that can decide.

**Pedro Rezende** [16:36:40]: And like I said, we have other clients that probably be also helpful for them.

**David Orban** [16:36:45]: Okay, perfect.

**David Orban** [16:36:48]: So let me mention a few additional things.

**David Orban** [16:36:53]: The way that we set up the API calls is through individual keys.

**Pedro Rezende** [16:37:00]: And

**David Orban** [16:37:01]: instead what we would like to do is to have a centralized way manage the conversations because really feels like the product today looks at the team from a building perspective, but then nothing else.

**David Orban** [16:37:24]: It's fine, it's a first step, but we would want to have the ability with the consent of the individual users who use it in the company, of course, to not have to for each get the API key and then have a multitude of these workflows, to have it centralized.

**Pedro Rezende** [16:37:54]: But if you don't mind sharing, David, how is actually set it?

**Pedro Rezende** [16:37:59]: Because I'm trying to understand how you would need all those keys.

**Pedro Rezende** [16:38:06]: Do you need their meeting content, for example?

**David Orban** [16:38:10]: Yeah, so not of external users, the internal users, right?

**David Orban** [16:38:15]: Colleague A, colleague B, colleague C, each use meet geek.

**David Orban** [16:38:20]: And today, unless I am mistaken, there isn't a key available that allows me to download their meetings with a single setup.

**David Orban** [16:38:31]: I need to generate individual keys for each of those.

**David Orban** [16:38:35]: and then juggle the keys in the workflow itself.

**David Orban** [16:38:41]: So my question is, if there are today or on the roadmap, there calls that look at the organization overall.

**David Orban** [16:38:55]: And first of all, of course, to extend our existing workflow, but then it and other things like provisioning users or stopping users or upgrading users, etc.

**David Orban** [16:39:09]: We believe that today everything should be possible via API, not just a limited set of functions.

**Pedro Rezende** [16:39:19]: No, yeah, for sure.

**Pedro Rezende** [16:39:20]: And I was going to say that I think this is already possible.

**Pedro Rezende** [16:39:24]: If I understood correctly what you mean.

**Pedro Rezende** [16:39:28]: of course I just need to understand those users that you your internal users.

**David Orban** [16:39:34]: Yes.

**David Orban** [16:39:35]: Are like

**Pedro Rezende** [16:39:36]: they set in different teams or they are like

**David Orban** [16:39:40]: single user.

**David Orban** [16:39:41]: No, no, no, no, no, no, no, in one So I'm talking about, let me share my screen with you,

**Pedro Rezende** [16:39:50]: Because...

**Pedro Rezende** [16:39:55]: Okay.

**Pedro Rezende** [16:39:56]: I'm sorry, I belong.

**Pedro Rezende** [16:39:58]: I push

**David Orban** [16:39:59]: button.

**David Orban** [16:40:00]: Am I here twice now

**Pedro Rezende** [16:40:01]: or just once?

**Pedro Rezende** [16:40:01]: No, no, no, just once.

**Pedro Rezende** [16:40:04]: But what I was going to say that I've already built some automations for other clients where we first get the meeting ideas from the team.

**Pedro Rezende** [16:40:12]: So the API call that we do is for the team itself.

**Pedro Rezende** [16:40:16]: We get a list of IDs and the hosts.

**Pedro Rezende** [16:40:20]: And then after we get this information, we delivering the other calls, you know.

**Pedro Rezende** [16:40:26]: And at least for what I understood,

**David Orban** [16:40:29]: this could work Okay, great.

**David Orban** [16:40:31]: I will check and then if I stumble upon some roadblock, I will let know.

**David Orban** [16:40:37]: Now, in the same spirit, we would like not to have to manually tell people to disable certain features that we appreciate your marketing department loves, but your enterprise clients which serve your viral marketing needs, but not necessarily the needs of your users, such sending everyone, the every

**David Orban** [16:41:08]: participant, the transcript by default, rather than keeping it turned off.

**David Orban** [16:41:15]: And if someone wants to turn it on, fine.

**David Orban** [16:41:17]: But we don't need, we are not paid to advertise Meet Geek.

**David Orban** [16:41:22]: And we don't want to advertise Meet Geek.

**David Orban** [16:41:24]: We want to use Meet Geek.

**David Orban** [16:41:26]: We are already paying you for using Meet Geek, so

**Pedro Rezende** [16:41:28]: it.

**Pedro Rezende** [16:41:29]: And today, when

**David Orban** [16:41:30]: a new user joins, we have to tell turn it off, and they don't turn it off, and then everyone complains.

**David Orban** [16:41:38]: And this is a strong push against using

**Pedro Rezende** [16:41:41]: your platform.

**Pedro Rezende** [16:41:42]: I see.

**David Orban** [16:41:43]: with individual users, that kind of ride-all marketing trick serves a positive purpose.

**David Orban** [16:41:50]: In an enterprise use case, it is the opposite.

**David Orban** [16:41:54]: People are actively saying, let's not use MeetGeek because it is polluting our conversations.

**David Orban** [16:42:02]: It is the advertising itself to our clients.

**David Orban** [16:42:06]: So we want to have way to keep using and turn off those things by default.

**Pedro Rezende** [16:42:18]: Okay.

**Pedro Rezende** [16:42:18]: I can't talk to my engineering team.

**Pedro Rezende** [16:42:21]: Let me just check here's something.

**Pedro Rezende** [16:42:24]: David.

**Pedro Rezende** [16:42:37]: I'm just checking here many users you have and how many

**David Orban** [16:42:42]: you... So right now, right now you will see we have... You can check in two ways, right?

**David Orban** [16:42:48]: The team probably has three, four users, not more.

**David Orban** [16:42:52]: And you will say maybe another half a dozen users on the same domain that are not yet part of the And we will need to consolidate that.

**David Orban** [16:43:03]: However, 60 people now.

**David Orban** [16:43:08]: will be over 100 in six

**Pedro Rezende** [16:43:10]: months.

**David Orban** [16:43:11]: And I just declared the meat geek to be the standard rather than the hodgepodge of, otter and firefly and, and,

**Pedro Rezende** [16:43:28]: and

**David Orban** [16:43:30]: all the others.

**David Orban** [16:43:31]: And just to confirm, the single reason why it's meet geek is because of the Okay, very So that is why I'm saying we are in a critical moment when adoption is growing as well as pushback.

**David Orban** [16:43:51]: That is why we need to find a way to turn off the things that make people dislike meet geek

**Pedro Rezende** [16:44:00]: For sure, for sure.

**Pedro Rezende** [16:44:04]: the only issue that I think we would find every time, even if find a way to configure for your team to not have this automatic email by default.

**Pedro Rezende** [16:44:18]: The users wouldn't need to be under your management.

**David Orban** [16:44:21]: I understand.

**David Orban** [16:44:22]: No, I understand.

**David Orban** [16:44:23]: That would be the only thing for this to work.

**David Orban** [16:44:26]: Of course, of

**Pedro Rezende** [16:44:27]: Clear.

**Pedro Rezende** [16:44:28]: But for sure.

**Pedro Rezende** [16:44:29]: No, we already have this kind of setting.

**Pedro Rezende** [16:44:34]: This normally enabled for the enterprise clients.

**Pedro Rezende** [16:44:37]: And when I say enterprise, it's the actual subscription enterprise level.

**Pedro Rezende** [16:44:44]: um we i can talk to my team because i've seen here at least under your email you have two business licenses right the others

**David Orban** [16:44:57]: there there should be there should be more on a free and and we are in the process of uh you know upgrading them And similarly, if possible, I would like to turn off the referral because again, don't need my team to be distracted earning extra $50.

**Pedro Rezende** [16:45:25]: Yes, I write.

**David Orban** [16:45:28]: Yeah, I'm paying them enough.

**David Orban** [16:45:30]: You know, let them do their job rather than wondering if they should promote MeetGit for $50 I will pay them $50 to get that icon off,

**Pedro Rezende** [16:45:46]: I understand.

**Pedro Rezende** [16:45:47]: Yeah, yeah.

**Pedro Rezende** [16:45:48]: Honestly, it's boring for me also, like every time that I didn't try to scroll or do something, I always click my mistake.

**Pedro Rezende** [16:45:56]: Honestly, I don't know if this one would be that Okay, only like Dan decided to take it off everyone.

**Pedro Rezende** [16:46:06]: I think this could be for good, but I don't think we just take the icon out for you and your

**David Orban** [16:46:13]: team.

**David Orban** [16:46:14]: No, okay, I

**Pedro Rezende** [16:46:15]: understand.

**Pedro Rezende** [16:46:16]: But I can talk to

**David Orban** [16:46:17]: him.

**David Orban** [16:46:18]: Okay, what else?

**David Orban** [16:46:20]: So I mentioned the big things.

**David Orban** [16:46:25]: Then there are little things like That may matter to people who don't use the API, even click, they see it right there, because you have a certain number of connectors and our current CRM is pipe drive.

**David Orban** [16:46:50]: You don't have a connector with PipeDrive.

**David Orban** [16:46:52]: You have with HopSpot and Salesforce, And so a simple question is whether you have PipeDrive on the roadmap

**Pedro Rezende** [16:47:03]: PipeDrive?

**Pedro Rezende** [16:47:04]: Let me share here.

**Pedro Rezende** [16:47:10]: Yeah, we already have with

**David Orban** [16:47:12]: PipeDrive.

**David Orban** [16:47:13]: Oh, you have it?

**David Orban** [16:47:14]: I miss that then.

**David Orban** [16:47:15]: That's great.

**David Orban** [16:47:16]: Let

**Pedro Rezende** [16:47:18]: me share my here.

**Pedro Rezende** [16:47:21]: I don't know if you're

**David Orban** [16:47:21]: seeing.

**David Orban** [16:47:22]: Yeah, I am seeing it.

**David Orban** [16:47:24]: You mean this one?

**David Orban** [16:47:25]: Yeah,

**Pedro Rezende** [16:47:26]: that one.

**Pedro Rezende** [16:47:26]: Okay,

**David Orban** [16:47:28]: Perfect.

**David Orban** [16:47:28]: Yeah, no, we... I totally miss that.

**David Orban** [16:47:30]: Perfect.

**Pedro Rezende** [16:47:32]: Nice.

**Pedro Rezende** [16:47:33]: Oh, yeah, at least

**David Orban** [16:47:34]: something.

**Pedro Rezende** [16:47:35]: You're in my labor right now.

**Pedro Rezende** [16:47:37]: So, yeah, you can already join here.

**Pedro Rezende** [16:47:39]: You can create the workflows or select specific What for it to Perfect.

**Pedro Rezende** [16:47:49]: Perfect.

**Pedro Rezende** [16:47:49]: Perfect.

**Pedro Rezende** [16:47:51]: Okay.

**David Orban** [16:47:52]: And yes, that is, of course, what I am using.

**Pedro Rezende** [16:47:59]: And

**David Orban** [16:47:59]: what how can part that I can just make the call and understand, what about the, yeah, okay, so that is the

**Pedro Rezende** [16:48:14]: Yeah, what I would recommend to you, let's say you're the manager account.

**Pedro Rezende** [16:48:20]: don't have like every, to have everyone's key.

**Pedro Rezende** [16:48:24]: You just have to be, at least, let me open here a team, just so you can't understand better.

**Pedro Rezende** [16:48:31]: Oh, I think this I'll to create here.

**Pedro Rezende** [16:48:35]: There is a permission here that you can see everyone can view the meetings, no, you view the meetings of others, but they can view yours.

**Pedro Rezende** [16:48:46]: That would be a good configuration.

**Pedro Rezende** [16:48:50]: The configuration itself here, it doesn't matter, right?

**Pedro Rezende** [16:48:54]: It's just to show you there are a different set of rules and you can also set yours.

**Pedro Rezende** [16:49:01]: You being admin, you being the owner of team.

**Pedro Rezende** [16:49:04]: Every time you do a call to the API, you will get the information of everyone there is inside there, all their meetings, all their meeting IDs, right?

**Pedro Rezende** [16:49:13]: So the flow that you would need to do here is like have only key, to do the call API.

**Pedro Rezende** [16:49:21]: You would do a call for the And after you do the you get the information specifically meetings You just do the get meeting so you can get all the information specifically for the you Perfect.

**Pedro Rezende** [16:49:42]: Yeah, instead

**David Orban** [16:49:43]: doing that with

**Pedro Rezende** [16:49:44]: a lot of things, think this would

**David Orban** [16:49:46]: easier.

**David Orban** [16:49:47]: Correct.

**David Orban** [16:49:48]: Absolutely.

**David Orban** [16:49:49]: That is great.

**David Orban** [16:49:50]: All

**Pedro Rezende** [16:49:51]: Okay, so.

**Pedro Rezende** [16:49:53]: Do you any kind of automation tool or like it, because if I

**David Orban** [16:49:57]: can... What is everyone using?

**Pedro Rezende** [16:50:01]: Well, at least I'm using NHM.

**Pedro Rezende** [16:50:03]: think it's

**David Orban** [16:50:04]: the... Oh, okay,

**Pedro Rezende** [16:50:05]: okay, no.

**David Orban** [16:50:07]: We are using, so, and Nathan is the workflow tool.

**David Orban** [16:50:14]: Perfect.

**David Orban** [16:50:16]: But in order to write whatever code,

**Pedro Rezende** [16:50:20]: we use cloud,

**David Orban** [16:50:21]: cloud.

**David Orban** [16:50:22]: Sure,

**Pedro Rezende** [16:50:23]: for sure, for sure, for sure,

**David Orban** [16:50:24]: sure.

**Pedro Rezende** [16:50:26]: Yeah, no, if you cloud code, what I would recommend actually give command to read our API and just asking him to build this workflow.

**Pedro Rezende** [16:50:38]: You know, get things meeting and afterwards, get meeting.

**Pedro Rezende** [16:50:41]: Actually, I have this part.

**Pedro Rezende** [16:50:43]: So it's just call before it to get the list meetings.

**Pedro Rezende** [16:50:48]: It will be very,

**David Orban** [16:50:49]: easy.

**David Orban** [16:50:50]: And is there an API call to create teams?

**David Orban** [16:50:54]: So can I tell Claude, hey, take all the users, put them team, set this permission, and then

**Pedro Rezende** [16:51:02]: proceed?

**Pedro Rezende** [16:51:03]: No, no, actually the only ones that you have right now to to actually do something right it would be to download meeting or to upload a meeting right so those would be the only ones to create a team you actually need to go on platform create a team associate yeah

**David Orban** [16:51:23]: that is that is what i mean uh apis should cover every aspect of a of a platform even claude on tropic doesn't understand that you cannot upgrade your account telling Claude to upgrade it, right?

**David Orban** [16:51:42]: And just like on there isn't any API call to go a free license to a business

**Pedro Rezende** [16:51:56]: I won't say to you that we don't have that because honestly do But not like

**David Orban** [16:52:03]: everyone.

**David Orban** [16:52:04]: It's not exposed publicly or it

**Pedro Rezende** [16:52:06]: is, yeah.

**Pedro Rezende** [16:52:07]: Exactly.

**Pedro Rezende** [16:52:07]: Like the customers that have the enterprise subscription, they have different

**David Orban** [16:52:13]: calls that they can do,

**Pedro Rezende** [16:52:15]: like the ad hoc meeting,

**David Orban** [16:52:17]: for example.

**David Orban** [16:52:18]: So we will definitely consider using the enterprise license or upgrading to the enterprise license.

**David Orban** [16:52:26]: I assume everyone has to be the same enterprise tier.

**David Orban** [16:52:31]: It cannot be differentiated by user, correct?

**Pedro Rezende** [16:52:35]: No, no, no, you can, like, We have minimum.

**Pedro Rezende** [16:52:39]: would like the thing with enterprise that we always like try fit under your company.

**Pedro Rezende** [16:52:47]: So it's not something called set for everyone, but let's say like 50 people Geek.

**Pedro Rezende** [16:52:55]: We will like, oh, try to at least five have enterprise levels, so they can be the admins, they can be the managers, and then everyone can be free, they can be pro, it doesn't matter.

**Pedro Rezende** [16:53:05]: Okay, okay, that's great.

**Pedro Rezende** [16:53:06]: You know, just need to record their meetings, fine.

**Pedro Rezende** [16:53:11]: But what I can do here also, I'll talk to Carol, because she deals with the sales part Yeah.

**Pedro Rezende** [16:53:19]: I'll talk to her because, like I said, the enterprise is something

**David Orban** [16:53:23]: custom.

**Pedro Rezende** [16:53:24]: Yeah.

**Pedro Rezende** [16:53:25]: The feedbacks that you already gave, I can talk to her first, go okay, try work something for David.

**Pedro Rezende** [16:53:32]: I'll talk to my engineer, see all the endpoints that we can or cannot give to.

**Pedro Rezende** [16:53:38]: And she gives you a proposal, like, okay, you will have this kind of access five, two, three license minimum should be her price.

**David Orban** [16:53:47]: Like, this is something that on.

**David Orban** [16:53:50]: Okay, perfect.

**David Orban** [16:53:52]: All right, thank you very much for all your help.

**David Orban** [16:53:54]: I'm looking forward to further contact and confirmation.

**David Orban** [16:53:59]: And yeah, hopefully I can overcome the resistance internally and keep using the product that are more

**Pedro Rezende** [16:54:08]: widely.

**Pedro Rezende** [16:54:08]: For sure, David.

**Pedro Rezende** [16:54:09]: And like I think I did introduce myself, but I'm your customer success engineer here inside Mikik.

**Pedro Rezende** [16:54:15]: So time you need any kind of help with the technical part of product, Just send

**David Orban** [16:54:22]: email and I'll able to talk.

**David Orban** [16:54:24]: All right.

**David Orban** [16:54:24]: Okay.

**David Orban** [16:54:25]: Thank you

**Pedro Rezende** [16:54:25]: very much.

**Pedro Rezende** [16:54:26]: to meet

---
*Backed up from MeetGeek on 2026-03-30 08:43*
