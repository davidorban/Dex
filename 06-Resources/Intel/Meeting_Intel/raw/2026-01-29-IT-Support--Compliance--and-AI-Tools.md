# IT Support, Compliance, and AI Tools

**Date:** 2026-01-29
**Duration:** Unknown
**Meeting ID:** 965edd5b-e348-45a2-a11a-8ae9831ddeef

## Participants
- *Participants not listed*

### Summary

The meeting focused on IT support operations, compliance readiness, AI tool usage, user configuration, and mandatory security briefings. Key operational decisions included adopting Asana as the ticketing and task system and SharePoint as the policy system of record to ensure auditable actions. A user raised setup issues for local development (Linux/cloud code) prompting a support ticket. The group discussed building an anonymizer box and workflow to protect data when using external LLMs and emphasized the need for training. Practical items covered included standardizing login domains, email signature practices, progressive migration of accounts to .com, and issuance/signing of acceptable use and security briefing materials.

## Full Transcript

**Speaker_00** [08:31:56]: My schedule flipped rather than one week here and three weeks in Italy.

**Speaker_00** [08:32:02]: It's three weeks here and one week in Italy.

**Speaker_00** [08:32:05]: Okay.

**Speaker_00** [08:32:05]: And that will be for the next few months.

**Speaker_00** [08:32:07]: How do you feel about it?

**Speaker_00** [08:32:09]: Well, it's not how I feel about it is how my wife and my mother and my dog and my cat and my oldest son and my grandchildren feel about it.

**Speaker_00** [08:32:19]: So I am... I need nothing, I lack nothing ever, so.

**Speaker_00** [08:32:27]: You like nothing at all?

**Speaker_00** [08:32:28]: No, lack.

**Speaker_00** [08:32:29]: Oh, lack.

**Speaker_00** [08:32:30]: I was going to say that.

**Speaker_00** [08:32:31]: No, no, I like everything.

**Speaker_00** [08:32:32]: It's the opposite.

**Speaker_00** [08:32:34]: Really?

**Speaker_00** [08:32:35]: Anyway, thank you for asking.

**Speaker_00** [08:32:41]: I have another one coming up, so that is why I'm being a bit more to the point, if you don't mind.

**Speaker_00** [08:32:49]: Thank you very much for sharing the two documents that you created.

**Speaker_00** [08:32:53]: Great, great job.

**Speaker_00** [08:32:56]: Thank you.

**Speaker_00** [08:32:57]: And the reason is because I feel you are very busy with Toby and all the other activities.

**Speaker_00** [08:33:03]: So I wanted to take it off your plate, start implementing it, and then, you know, keep you both involved as well as in, sorry, both informed as well as involved to the degree that you are able to not only observe but also to execute.

**Speaker_00** [08:33:21]: Yeah, I appreciate that understanding.

**Speaker_00** [08:33:24]: Now, the meeting today has three very simple objectives.

**Speaker_00** [08:33:34]: One, to ask you how IT can support you in your business objectives.

**Speaker_00** [08:33:43]: Yep.

**Speaker_00** [08:33:44]: Two, take a look at a few of your settings suggesting potential optimizations.

**Speaker_00** [08:33:53]: And three, sharing with you what will come more formally the acceptable use policy and mandatory security briefing documents that are part of us growing up.

**Speaker_00** [08:34:18]: Obviously there are certain systems that are already in place, email, slack, treasure rate, pipe drive.

**Speaker_00** [08:34:28]: and we will be rolling out SharePoint that will be the system of record for policies and other things that are not immutable, but they change more slowly.

**Speaker_00** [08:34:43]: Asana is going to be the system of record for tasks and decisions, the way that we Sorry, the reason for these things to be systematic is not only because it is a good practice and makes things manageable, but because having now the expectation of receiving the license shortly, I don't know, this

**Speaker_00** [08:35:18]: week, next week, whenever.

**Speaker_00** [08:35:20]: offshore, which is here, we have to be compliant.

**Speaker_00** [08:35:26]: And in order to be compliant, we have to record what we do in a manner that is auditable.

**Speaker_00** [08:35:35]: And for every action recorded, we have to be able to say who when and why and under which authority to that particular action.

**Speaker_00** [08:35:48]: So for everything we will have a system of record.

**Speaker_00** [08:35:51]: So our CRM is the system of record for contacts and clients, etc.

**Speaker_00** [08:36:00]: Our system of records for policies, processes and SOPs is SharePoint.

**Speaker_00** [08:36:08]: Our system of record for tasks and decisions is a sauna and so on.

**Speaker_00** [08:36:14]: And so my question to you is as much or as little that you have an insight on how this year is gonna fold out for you, do you see something that could help you that you don't yet have.

**Speaker_00** [08:36:37]: Let me give you an example.

**Speaker_00** [08:36:40]: I sit down with Jan

**Speaker_01** [08:36:41]: and

**Speaker_00** [08:36:42]: he told me, yeah, I will have real estate to map, and I will have probably paper documents to scan and to store, and all the craziness to untangle, and not only that has to be done well, but again it has to be done compliance, right?

**Speaker_00** [08:37:07]: So that is a very clear example.

**Speaker_00** [08:37:09]: Or I sat down with Asim,

**Speaker_00** [08:37:15]: our colleague doing sovereign banking in Pakistan, and he told me about his desire to cross-reference our networks of opportunities because he feels that it is underutilized and he volunteered as a as a participant in providing the information first so that there is something to cross-reference

**Speaker_00** [08:37:45]: because today we have nothing right so he will brain dump this set of stuff that he has 50 different things up to $50 billion of opportunities and what they mean or they imply and then I will do the same with other people as well, right?

**Speaker_00** [08:38:02]: So these are two examples of either platforms or processes that are not in place that these two colleagues highlighted as something that they would benefit from.

**Speaker_00** [08:38:14]: So the question to you is, do you see something similar or different that you know you could benefit from?

**Speaker_01** [08:38:21]: I kind of want to wait until you just talk about the security and compliance stuff, because that would be, for me, my biggest concern would just be around how we can protect our data while also using third-party tools.

**Speaker_01** [08:38:38]: Yes.

**Speaker_01** [08:38:40]: And how, like...

**Speaker_00** [08:38:42]: And that is a very, very good point, something that I did not mention.

**Speaker_00** [08:38:48]: because the simplest label for that is training.

**Speaker_01** [08:38:52]: Yeah.

**Speaker_00** [08:38:52]: So you need a training about maturing a clear understanding of how to use tools that allow you to work with and for clients while being compliant.

**Speaker_01** [08:39:07]: Yeah.

**Speaker_01** [08:39:07]: I think in particular with AI though, if we would have a system that like anonymizes the data

**Speaker_00** [08:39:14]: or

**Speaker_01** [08:39:14]: something, that's the kind of

**Speaker_00** [08:39:15]: thing I'm

**Speaker_01** [08:39:16]: talking about.

**Speaker_01** [08:39:16]: Yes.

**Speaker_00** [08:39:20]: And if you want, I can answer what I am aiming to build, even though if we don't have it yet, because yesterday I was sitting with Axel, I think Axel, I don't remember one of the two, I think Axel, who said, well, we could use co-pilot to anonymize, and then we can use ChatGPT And I told him, well,

**Speaker_00** [08:39:46]: co- pilot already is outside because he thought it was not.

**Speaker_00** [08:39:52]: Instead, what I am planning to do is literally an anonymizer box.

**Speaker_00** [08:40:00]: either sitting here or sitting at G42, depending on how big the box needs to be.

**Speaker_00** [08:40:05]: And then when we can afford it, when we will have the capacity to manage it and set it up.

**Speaker_00** [08:40:12]: But the kind of LLM that would need to go through documents in order to allow us to send them to Claude or to chat is not as sophisticated as those need to be there, right?

**Speaker_00** [08:40:32]: So, Kimmy, or I'm not saying Lama, but let's say Kimmy, that's my candidate today, could be running on the box and then going out, and there would be a workflow for all of that.

**Speaker_01** [08:40:49]: Okay, that's the main thing for me.

**Speaker_01** [08:40:51]: Okay.

**Speaker_01** [08:40:52]: The other thing as well is, just getting set up locally on this computer with cloud code.

**Speaker_01** [08:41:02]: For some reason, the Linux, the remote Linux, I can't even, I don't even understand the technicalities of it, but just getting set up with the Linux and then the server simulation thing so that I can then run cloud code on VS code.

**Speaker_01** [08:41:17]: For some reason, windsurf, I couldn't get it to work on this computer.

**Speaker_00** [08:41:21]: Is this one of the newer

**Speaker_01** [08:41:22]: ones?

**Speaker_01** [08:41:23]: Yeah, this is one of the new company ones.

**Speaker_01** [08:41:27]: That's like a specific IT problem.

**Speaker_00** [08:41:29]: This is a ticket.

**Speaker_00** [08:41:30]: This

**Speaker_01** [08:41:31]: is a support ticket.

**Speaker_00** [08:41:32]: Yeah, yeah.

**Speaker_00** [08:41:33]: So I don't want to waste your time with it.

**Speaker_00** [08:41:34]: No,

**Speaker_01** [08:41:34]: no, no.

**Speaker_01** [08:41:35]: I could maybe get anchored to the... No, no.

**Speaker_01** [08:41:37]: You

**Speaker_00** [08:41:38]: wish.

**Speaker_00** [08:41:39]: You, I wish.

**Speaker_00** [08:41:44]: So I told Amina or Michael when they gave me this wonderful challenge that I'm inspired by the, I don't remember the name of the Japanese founder of billion-dollar companies that published the book and it's entitled something like the toilet cleaning philosophy, where he The founder, billionaire of

**Speaker_00** [08:42:09]: those companies comes into work every morning and cleans the toilet and then does whatever rest he needs to do, right?

**Speaker_00** [08:42:17]: And I haven't tried yet.

**Speaker_00** [08:42:20]: That's right.

**Speaker_00** [08:42:23]: But yes, you know, we have no one else, so something like this cannot be delegated to you to Ankit.

**Speaker_00** [08:42:31]: I have to help you to do it, and I will.

**Speaker_00** [08:42:34]: And I will get to it, probably not today, but now that I know I will get it.

**Speaker_00** [08:42:42]: Cool.

**Speaker_00** [08:42:43]: And evidently, I need to socialize better the fact that no one should wait to log a ticket through email or Slack.

**Speaker_00** [08:42:56]: We will publish the Asana form soon that will allow you to log a

**Speaker_01** [08:43:00]: ticket.

**Speaker_01** [08:43:04]: Yeah, of course you can't.

**Speaker_01** [08:43:06]: Yeah,

**Speaker_00** [08:43:07]: thanks.

**Speaker_00** [08:43:07]: We have a ticketing system on our son.

**Speaker_00** [08:43:08]: Actually, let me show you.

**Speaker_00** [08:43:10]: Sorry, if you don't mind.

**Speaker_00** [08:43:11]: It should be interesting for you.

**Speaker_00** [08:43:16]: That's background.

**Speaker_00** [08:43:18]: Thank you.

**Speaker_00** [08:43:20]: And while we are working, Claude is working as well.

**Speaker_00** [08:43:27]: For the 7HR 100, what should they point to instead?

**Speaker_00** [08:43:35]: Replace with

**Unknown speaker** [08:43:38]: Internet.

**Speaker_00** [08:43:40]: What's the status of January, items mixed.

**Unknown speaker** [08:43:45]: Okay.

**Speaker_01** [08:43:46]: This is the new... Yeah, co-work.

**Speaker_01** [08:43:49]: Okay.

**Speaker_01** [08:43:50]: It's incredible.

**Speaker_00** [08:43:52]: That's not included in... Hang on, let me check.

**Speaker_00** [08:43:54]: No, no, pro, because it was max for a couple of weeks.

**Speaker_00** [08:43:57]: Yeah.

**Speaker_00** [08:43:57]: And now it's pro as well, but the Mac only, not Windows.

**Speaker_00** [08:44:01]: Yeah, because I didn't see you when I installed it the other day.

**Speaker_00** [08:44:04]: But this is not what I wanted to show you.

**Speaker_00** [08:44:08]: So it's

**Speaker_01** [08:44:08]: just

**Speaker_00** [08:44:09]: classic, just good.

**Speaker_00** [08:44:09]: What I want to show you is that in Asana, we have portfolios.

**Speaker_00** [08:44:17]: So this is the IT portfolio where you can see all the projects in all the, sorry, all the tickets for all the projects in the portfolio.

**Speaker_00** [08:44:30]: And... Are they really 588?

**Speaker_00** [08:44:32]: Mm-hmm.

**Speaker_00** [08:44:33]: Incredible.

**Speaker_00** [08:44:34]: And not just support tickets in general.

**Speaker_00** [08:44:38]: because I have an intranet project, I have a website project, I have onboarding, off boarding, I have minimum viable secure operations, IT governance, and you know, whatever else, lots of stuff.

**Speaker_00** [08:44:54]: And by the way, I am doing something like Oh, no, it died.

**Speaker_00** [08:45:06]: Shit.

**Speaker_00** [08:45:07]: Okay.

**Speaker_00** [08:45:08]: That was a terminal.

**Speaker_00** [08:45:11]: And what I would have showed you is that I am taking the transcriptions of my meetings and creating asana tasks automatically.

**Speaker_00** [08:45:17]: And I have scripts.

**Speaker_00** [08:45:19]: that are doing it daily now, but probably I will have to do it twice a day at least.

**Speaker_00** [08:45:26]: And then I am creating the emails that I am sending out to people.

**Speaker_00** [08:45:33]: For example, sorry.

**Speaker_00** [08:45:37]: Let me show you.

**Speaker_00** [08:45:40]: Let me show you.

**Speaker_00** [08:45:41]: Yesterday, I sent out something like here.

**Speaker_00** [08:45:53]: I said it.

**Speaker_00** [08:45:55]: I mean, the AI told me to say, and that is, by the way, non-compliant.

**Speaker_00** [08:46:00]: Internally, we can do that thing.

**Speaker_00** [08:46:02]: But externally, we cannot say the AI told me to say it.

**Speaker_00** [08:46:06]: Yeah.

**Speaker_00** [08:46:07]: All right.

**Speaker_00** [08:46:07]: So I read them, of course, but this is the point that I create a list of tasks for other people, not only for myself, but for other people as well.

**Speaker_00** [08:46:19]: And then I tell them, listen, I will review those tasks, and you should too.

**Speaker_00** [08:46:22]: But here is what comes out of our conversation, right?

**Speaker_00** [08:46:25]: Now, back to Asana and ticketing, we have... for our overage resolution time because this is the point that now with this we can actually measure because we have the data of how we are supporting our users and then they can say oh no I want you to reply in two minutes and we say okay maybe I want

**Speaker_00** [08:46:55]: you to resolve it in 20 minutes okay but our SLA our service level agreement with ourselves is of a certain level right now, right?

**Speaker_00** [08:47:09]: So this project has a form and we haven't published it yet.

**Speaker_00** [08:47:14]: So on top of sending it with email, logging it on Slack, people will be able to sort of fill the form, and my message is going to don't wait around until you have a meeting with me and hold back as soon as you have a problem just log it and then we will handle it you know we will establish the

**Speaker_00** [08:47:33]: priority and when we can get to it and do we need to hire another couple unkit whatever it is okay yeah very nice all right so

**Speaker_00** [08:47:48]: Those things that you mentioned, training and the anonymizing AI are fantastic and I don't think you have to come up with anything more.

**Speaker_00** [08:48:03]: If you do, that in this meeting, the objective was for you to highlight things that IT can help you with, objective achieved.

**Speaker_00** [08:48:13]: Okay, great.

**Speaker_00** [08:48:13]: Objective achieved, very good, very good.

**Speaker_00** [08:48:16]: And of course, if you have more, I'm not saying you shouldn't say, absolutely.

**Speaker_00** [08:48:21]: Tell me, tell me more, but this is already very, very valuable.

**Speaker_00** [08:48:25]: because technically I already submitted the budget but I can of course it's gonna be continually revised anyway of how the budget looks like what it is dedicated to etc.

**Speaker_00** [08:48:42]: etc.

**Speaker_00** [08:48:45]: Okay, so the second part of the meeting is that we look at a few of your settings.

**Speaker_00** [08:48:55]: And do you have your phone with you as well?

**Speaker_00** [08:48:57]: Yes.

**Speaker_00** [08:48:58]: Okay.

**Speaker_00** [08:48:59]: Is this a company device?

**Speaker_00** [08:49:02]: Perfect.

**Speaker_00** [08:49:04]: So open Outlook, however you use it.

**Speaker_00** [08:49:12]: And show me your signature settings.

**Speaker_00** [08:49:17]: And my objective is to lower the cognitive load of the tools so that people are not going crazy.

**Speaker_00** [08:49:27]: Perfect.

**Speaker_00** [08:49:28]: This is exactly what I want, so that when there are several replies, half of the email is not occupied by signatures.

**Speaker_01** [08:49:36]: Yeah, perfect.

**Speaker_00** [08:49:38]: Show me the same on your phone.

**Speaker_00** [08:49:44]: And this is a personal device, right?

**Speaker_00** [08:49:45]: Yeah.

**Unknown speaker** [08:49:46]: Okay.

**Speaker_00** [08:49:51]: I don't have one on my phone.

**Speaker_00** [08:49:54]: You don't have a signature in your phone.

**Speaker_00** [08:49:55]: Perfect.

**Speaker_00** [08:49:56]: Because many of us advertise Microsoft without being paid for it.

**Speaker_00** [08:50:00]: So my question is, do you want to tell everyone that you wrote your email without look?

**Speaker_00** [08:50:06]: Because if you don't, why don't you take the signature off?

**Speaker_00** [08:50:11]: Okay, very good.

**Speaker_00** [08:50:14]: You, as everyone else, are still logged in to treasure it with your dot email account.

**Speaker_00** [08:50:21]: I know, I noticed that the day.

**Speaker_00** [08:50:23]: Yeah.

**Speaker_00** [08:50:23]: And that will be very painful, unavoidable, until we abandon treasure it.

**Speaker_00** [08:50:29]: But, yeah, you will have to go through logging in your browser with dot com.

**Speaker_00** [08:50:35]: keeping your app on .email, inviting yourself to all the folders.

**Speaker_01** [08:50:40]: Yeah,

**Speaker_00** [08:50:41]: okay, just the same as the... Asking someone else to invite you if you are a user instead of a manager.

**Speaker_01** [08:50:46]: Do we have the, so we have the aliwan.com account set up for treas right now, we can start doing that migration.

**Speaker_00** [08:50:53]: No, because we don't have 100 licenses rather than 50.

**Speaker_01** [08:50:57]: Yeah,

**Speaker_00** [08:50:58]: okay.

**Speaker_00** [08:50:58]: So I am doing it progressively with people because it is important but not urgent.

**Speaker_01** [08:51:03]: Yeah,

**Speaker_00** [08:51:04]: of course.

**Speaker_00** [08:51:04]: So just one by one until everybody is ticked

**Speaker_01** [08:51:07]: off.

**Speaker_00** [08:51:08]: Okay.

**Speaker_00** [08:51:09]: Are you okay with Nitro?

**Speaker_00** [08:51:10]: Did you install it and use it?

**Speaker_00** [08:51:12]: Yeah.

**Speaker_00** [08:51:12]: Okay.

**Speaker_00** [08:51:13]: Do you use DocuSign or you don't need

**Speaker_01** [08:51:16]: DocuSign?

**Speaker_01** [08:51:17]: I don't need DocuSign, but I'm sure I will

**Speaker_00** [08:51:20]: eventually.

**Speaker_00** [08:51:20]: Yeah, of course.

**Speaker_00** [08:51:22]: You want to.

**Speaker_00** [08:51:23]: Let me see, I actually have a thing.

**Speaker_00** [08:51:37]: Yeah, pipe drive, you use it, hopefully.

**Speaker_00** [08:51:41]: Yeah, okay.

**Speaker_00** [08:51:42]: And you are logged in with .com in pipe drive?

**Speaker_01** [08:52:06]: Is this your... No, it's just meat cake,

**Speaker_00** [08:52:10]: is it?

**Speaker_00** [08:52:12]: Yes.

**Speaker_00** [08:52:12]: And we will probably adopt it.

**Speaker_00** [08:52:15]: And we will adopt Claude as well.

**Speaker_00** [08:52:31]: Yep, dot com.

**Speaker_00** [08:52:32]: Okay, perfect.

**Speaker_00** [08:52:37]: You are .com.

**Speaker_00** [08:52:38]: Oh, yeah, this is Shidem.

**Speaker_00** [08:52:42]: You are .com on Slack as well, because these are the people still .em.

**Speaker_01** [08:52:45]: Yeah.

**Unknown speaker** [08:52:48]: Okay.

**Speaker_00** [08:52:52]: So, Slack, yes.

**Speaker_00** [08:52:54]: Asana, can you check?

**Speaker_01** [08:52:59]: Asana, I think I'm at .com as well, but I'll confirm.

**Speaker_00** [08:53:04]: Sorry?

**Speaker_00** [08:53:05]: .com.

**Speaker_00** [08:53:05]: Okay, because some people are still .tg.

**Speaker_00** [08:53:08]: Oh, really?

**Speaker_00** [08:53:08]: Or at tg.

**Speaker_00** [08:53:09]: Okay.

**Speaker_00** [08:53:11]: Okay, so last thing, let me show you just a glance.

**Speaker_00** [08:53:17]: You will receive it.

**Speaker_00** [08:53:19]: It's a totally trivial thing.

**Speaker_00** [08:53:22]: Sure.

**Speaker_00** [08:53:23]: Mandatory security briefing, why it matters, passwords, MFA, what not to do, data classification and storing.

**Speaker_00** [08:53:35]: We are rolling out SharePoint.

**Speaker_00** [08:53:38]: fishing, compromise, social engineering, go slow, don't act in haste, report a security incident, that you are still responsible for protecting the company

**Speaker_00** [08:54:09]: is exactly that, the acceptable use policy, which is telling you that there are rules to use technology, it applies to everyone, what is your responsibility, data classification, again a little bit of overlap, what you cannot do, that you can use your personal device, however, we will enroll it in

**Speaker_00** [08:54:41]: our corporate management platform, which includes remote vibe, for example, but you can ask to have a corporate device instead.

**Speaker_00** [08:54:57]: and that we are not gonna look at your email or your personal email.

**Speaker_00** [08:55:05]: We are under normal circumstances also not gonna look at your corporate email, but you have to be aware that it is still corporate stuff, including that you are responsible, you have to report incidents, and that violations are serious.

**Speaker_00** [08:55:21]: You know, pretty simple stuff, and you will sign this as well, okay?

**Speaker_00** [08:55:28]: Great.

**Speaker_00** [08:55:29]: That's it.

**Speaker_00** [08:55:30]: Thank you so

---
*Backed up from MeetGeek on 2026-03-30 08:46*
