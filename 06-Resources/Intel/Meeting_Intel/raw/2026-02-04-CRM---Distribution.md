# CRM | Distribution

**Date:** 2026-02-04
**Duration:** Unknown
**Meeting ID:** 6f27828b-21b6-4a2d-bb9f-caae7a019b7b

## Participants
- *Participants not listed*

### Summary

The meeting focused on operationalizing Pipedrive for distribution: defining business ownership (Greg/Nicola) and technical ownership (David), provisioning a sandbox, and sequencing configuration versus data-cleaning. Actions include Isel cleaning/importing investor data with David providing automation tools and Ivan configuring fields and visibility. The team reviewed Pipedrive labels, access controls, audit logging, reporting capabilities, and debated appropriate granularity for the packaging stage and whether project management (Asana or Pipedrive projects) should track sub-tasks. The group also agreed to create templates and processes for third-party introducers and to document workflow requirements for further configuration.

## Full Transcript

**David Orban** [06:00:57]: Hello,

**David Orban** [06:01:26]: did I

**Greg Wall** [06:01:28]: Hello, Greg.

**Greg Wall** [06:01:31]: Last time I saw you here was in person.

**Greg Wall** [06:01:35]: There you go.

**Greg Wall** [06:01:37]: That's wonderful.

**Greg Wall** [06:01:38]: Hi guys, hi Greg.

**Greg Wall** [06:01:40]: Hey.

**Greg Wall** [06:01:40]: Hello, how are you?

**Greg Wall** [06:01:42]: I do have, I have Nicola sitting here next to you.

**Greg Wall** [06:01:46]: Hi there.

**Greg Wall** [06:01:47]: We're tag tag tag on the one on the one computer here.

**Greg Wall** [06:01:54]: Very good.

**Greg Wall** [06:01:54]: Hi, Michael, please introduce you.

**Greg Wall** [06:01:58]: Hi, Toby.

**Greg Wall** [06:02:03]: There you go.

**Greg Wall** [06:02:05]: Greg, let's do you.

**Toby O'Connor** [06:02:07]: Greg, let's do a few minutes after this call if you've got a few, if you've got a second just on our meeting tomorrow.

**Toby O'Connor** [06:02:14]: I do.

**Toby O'Connor** [06:02:16]: Yeah, I just want to get coordinated for that.

**Greg Wall** [06:02:19]: That's absolutely fine.

**Greg Wall** [06:02:20]: I've got plenty to tell you.

**Greg Wall** [06:02:23]: Okay.

**Greg Wall** [06:02:25]: Good, good.

**Greg Wall** [06:02:27]: Okay.

**Greg Wall** [06:02:29]: So is this it?

**Greg Wall** [06:02:31]: We've got everyone.

**Greg Wall** [06:02:33]: I think

**Ivan Fattorusso** [06:02:34]: so, let me just check who else was on the M- might.

**Ivan Fattorusso** [06:02:39]: Axel was on it as well.

**Ivan Fattorusso** [06:02:41]: Axel should be on it.

**Ivan Fattorusso** [06:02:45]: I haven't seen him this morning.

**Ivan Fattorusso** [06:02:52]: I tell you,

**Toby O'Connor** [06:02:52]: you got to be able to handle an evening out, get in the

**Ivan Fattorusso** [06:02:57]: office.

**Ivan Fattorusso** [06:02:57]: Let me see if I can find it.

**Ivan Fattorusso** [06:02:59]: Yeah, hold on, I'll have a look.

**Ivan Fattorusso** [06:03:02]: I don't have to say,

**Toby O'Connor** [06:03:03]: you had a joint function last night, didn't we?

**Toby O'Connor** [06:03:05]: How is it, Axel,

**Greg Wall** [06:03:07]: figuring out how the tide is not?

**Greg Wall** [06:03:10]: So is there Andy reporting to you,

**Toby O'Connor** [06:03:15]: doesn't it?

**Toby O'Connor** [06:03:19]: All right, let's get going.

**Toby O'Connor** [06:03:25]: He's not out at the, no, I'm sorry, it's not out having a coffee or something stupid.

**Toby O'Connor** [06:03:30]: Yeah, Civey's right.

**Toby O'Connor** [06:03:38]: Let me get going.

**Toby O'Connor** [06:03:39]: Okay, yeah.

**Toby O'Connor** [06:03:42]: Hey,

**Greg Wall** [06:03:43]: John, would you like to kick off?

**Greg Wall** [06:03:44]: What would you like me to kick off?

**Greg Wall** [06:03:45]: Yeah, yeah, I guess maybe maybe,

**Ivan Fattorusso** [06:03:50]: maybe Toby, because I think Toby, you were the one that, like sort of were the originator of this call.

**Ivan Fattorusso** [06:03:56]: Yeah,

**Toby O'Connor** [06:03:57]: okay, so Isel sits, Greg, in our little IB area, right.

**Toby O'Connor** [06:04:08]: Like a lot of people that actually isn't necessarily in IB, but it sits with the group, which is great.

**Toby O'Connor** [06:04:13]: So in the context of what we're trying to do to bring greater focus and accountability and effectiveness of our distribution effort, the thought was to leverage the investor base for distribution.

**Toby O'Connor** [06:04:36]: And that's part one.

**Toby O'Connor** [06:04:39]: Part two is, you know, David's got into this new role around technology, but obviously has the skill sets around AI.

**Toby O'Connor** [06:04:52]: So what I've done is kind of allocated Xcel, who should be on the call to be a resource to this, and a bit of a link into the team here.

**Toby O'Connor** [06:05:04]: So if, for example, we're doing the weekly sheets for the Thursday meeting, right?

**Toby O'Connor** [06:05:11]: It should have the four or five mandates we've got on the pipeline, da, da, da, da, right?

**Toby O'Connor** [06:05:15]: He should help you guys make sure everything is right for that, the way that you want it.

**Toby O'Connor** [06:05:20]: I've also put him in, direct link with David, because he's got pretty good technical skill sets, I think, and very interested in working with David on the AI.

**Toby O'Connor** [06:05:32]: So it's kind of a good combination, right?

**Toby O'Connor** [06:05:35]: And what I was trying to get is really two things sorted out.

**Toby O'Connor** [06:05:39]: One is as many of our investor contacts as possible into the CRM so we can organize them and have access to them, and then use any AI tools to be able to you know, help whoever's working on the deal quickly kind of assorting within our pool of people, investors, you know, who's relevant to whatever

**Toby O'Connor** [06:06:02]: situation.

**Toby O'Connor** [06:06:03]: So that was a very simple step.

**Toby O'Connor** [06:06:06]: You know, I think Nate was very helpful yesterday.

**Toby O'Connor** [06:06:10]: He's in the board meeting right now, it's why he's not on this call.

**Toby O'Connor** [06:06:13]: He's very helpful yesterday, right, as I'm dumping a huge number of investors into it.

**Toby O'Connor** [06:06:18]: So that's a good start, right?

**Toby O'Connor** [06:06:20]: And if we can do that, you know with with Greg and Nicola and me and I'm sure we'll have quite a valuable pool of people that we could go to, right?

**Toby O'Connor** [06:06:33]: So that was really the simple objective.

**Toby O'Connor** [06:06:35]: Right now, Isel puts into Ivan, right, who's, we all sit together in IB.

**Toby O'Connor** [06:06:43]: So that's the overview.

**Toby O'Connor** [06:06:48]: Okay,

**Greg Wall** [06:06:49]: good.

**Greg Wall** [06:06:50]: Well, why don't I start by saying a couple of things.

**Greg Wall** [06:06:55]: So firstly, so is Zell's given just a bit of background and overview here?

**Greg Wall** [06:07:00]: Isell's given Nicola and I think as everybody's aware, Nicola in particular has been playing around with it, and she can probably talk for herself here, but she's been playing around with it.

**Greg Wall** [06:07:16]: She and I have got some ideas about what we would like to do with it.

**Greg Wall** [06:07:27]: Nicola has composed a whole bunch of questions, I guess, at this point in time, for us to understand certain things around how it's structured and what we can and can't do so that we can further refine what we can do from a distribution point of view with the investors, and particularly managing

**Greg Wall** [06:07:48]: them through the process.

**Greg Wall** [06:07:50]: Greg, I do it the

**Toby O'Connor** [06:07:51]: other way around.

**Toby O'Connor** [06:07:51]: I'd say, I kind of have a quick look at what Ezel's got, and then I would come back to Ezel and David and Axel with what you want.

**Toby O'Connor** [06:08:04]: I kind of,

**Greg Wall** [06:08:04]: sorry to jump in.

**Greg Wall** [06:08:05]: I think that's more or less what I have done.

**Greg Wall** [06:08:09]: Okay.

**Greg Wall** [06:08:10]: Just to give you, in my head, it's at two levels.

**Greg Wall** [06:08:14]: So I said, I don't expect you to have to have digested yet.

**Greg Wall** [06:08:22]: I don't know if it's best use of time here to go through them all.

**Greg Wall** [06:08:26]: Some of them are quite key.

**Greg Wall** [06:08:31]: Well, the first thing, this is me.

**Greg Wall** [06:08:33]: which I feel I feel a little tweak in the live system, which is why I sent a note.

**Greg Wall** [06:08:40]: Is there a, I called it sandpit.

**Greg Wall** [06:08:42]: Sorry, David.

**Greg Wall** [06:08:43]: Shows my, how old my history is.

**Greg Wall** [06:08:45]: If there is a test sandbit system to have a real good play in.

**Greg Wall** [06:08:50]: It's clearly, I don't want to state the obvious best, it's the opposite of best practice to be playing, working out, test data, etc.

**Greg Wall** [06:08:58]: in a live system.

**Greg Wall** [06:08:59]: So personally, I feel very uncomfortable doing that.

**Greg Wall** [06:09:02]: So I think, did you to sort of see if we could have access to a...

**David Orban** [06:09:10]: I don't know who is moderating the call, but whoever is moderating the call should not is that I raised my hand in order to interject.

**David Orban** [06:09:25]: Nicola, yes.

**David Orban** [06:09:27]: I not only reached out to Ivan, but then I wrote to Pi Drive who responded in the positive.

**David Orban** [06:09:35]: We will have a sandbox set momentarily in order to explore the functionality and the possibility of configuring the system in order to be fit for purpose without touching the live one, right?

**David Orban** [06:09:53]: So that is already in motion.

**David Orban** [06:09:58]: That's great.

**Greg Wall** [06:09:59]: So I've just got, I won't go through every line item in Isle, but I think there's a few pieces that I think it's worth raising.

**Greg Wall** [06:10:06]: And it's just what I found I completely take on board.

**Greg Wall** [06:10:10]: I might have picked up the wrong stick.

**Greg Wall** [06:10:13]: In terms of user rights, I'm hoping a lot of what we're asking is config.

**Greg Wall** [06:10:18]: I was, I just picked went on to, and entry of a investor.

**Greg Wall** [06:10:27]: I was able to modify all the data that been set up, which, again, concerned me.

**Greg Wall** [06:10:34]: If I'm creating investors' contacts, I don't know if it's a user rights config.

**Greg Wall** [06:10:39]: I would expect any of my contacts that I'm the owner of, cannot be modified thereafter by another user.

**Greg Wall** [06:10:51]: So is

**David Orban** [06:10:51]: that... Let me the way that

**David Orban** [06:11:01]: the system is set up now needs to be improved, right?

**David Orban** [06:11:07]: And anything that you find that is either concerning or not according to best practice or even more strongly put, non-compliant, please.

**David Orban** [06:11:23]: Let's take note and then put it in a system where we can track how the CRM configuration is progressively improved in order to match our expectations, the regulator's expectations and so on, right?

**David Orban** [06:11:42]: Isel is not a technical resource for administering pipe drive.

**David Orban** [06:11:49]: and ISO correct me if you would like to do that.

**David Orban** [06:11:55]: But I believe that it is not useful to burden her with that technical task.

**David Orban** [06:12:03]: She's useful in being dedicated to aggregating, cleaning, importing,

**David Orban** [06:12:15]: to you, Greg, and you, Eric.

**David Orban** [06:12:20]: So, Nicole.

**David Orban** [06:12:23]: Sorry, Nicole.

**David Orban** [06:12:24]: My apologies.

**David Orban** [06:12:28]: And if we are aligned on that, then as IT, I will take ownership of the configuration tasks.

**David Orban** [06:12:38]: and and make them and make them make them.

**David Orban** [06:12:44]: It will not be an immediate execution.

**David Orban** [06:12:49]: Nicolain, you will not find it to be the way you want it tomorrow, but we will agree what is an acceptable process.

**Greg Wall** [06:12:59]: Okay, what's probably best use of time then?

**Greg Wall** [06:13:02]: I don't think I included you on the email these pieces that I think there's some, yeah, hopefully, conflict.

**Greg Wall** [06:13:13]: A bit like a lot of the areas are one to one.

**Greg Wall** [06:13:17]: think labels, etc.

**Greg Wall** [06:13:18]: Whereas I'd certainly expect many areas to be a many to one relationship.

**Greg Wall** [06:13:23]: As an example, in high level industry sectors assigned to an investor.

**Greg Wall** [06:13:33]: It's very rare.

**Greg Wall** [06:13:34]: for that's definitely, most of our investors anyway, know, cover multiple business sectors.

**David Orban** [06:13:42]: I totally understand the point.

**David Orban** [06:13:45]: And yes, I also agree.

**David Orban** [06:13:46]: The best is if you forward me the email you originally sent with either the attachment or the body of the email listing your concerns.

**David Orban** [06:13:58]: And then I will ask questions if they are not clear and then just proceed listing the tasks in our ticketing system so that they can be implemented And then, of course, I will also, the owner of the CRM function, at least as I know, is Ivan.

**David Orban** [06:14:19]: So the architecture of the CRM based on your requests, changes, so much that I believe Ivan should be involved.

**David Orban** [06:14:30]: I will also run it by Ivan and then he will say, well, I didn't think of it or I did his agree with it, so we will handle those.

**David Orban** [06:14:39]: But what I expect is that 90% of the things that you want, Nicola, are reasonable, and they will be just straight away

**Ivan Fattorusso** [06:14:49]: implemented.

**Ivan Fattorusso** [06:14:50]: I would suggest before doing that particular exercise, I think it's worth doing a brief demo where we actually, I show you on screen how it had how it's been customized, how it's been set up, how we intended on using Because once we go through that, I think the questions then become more obvious and

**Ivan Fattorusso** [06:15:12]: relevant and we can address them more precisely.

**Ivan Fattorusso** [06:15:20]: So let's do a demo first and then address

**David Orban** [06:15:22]: those questions.

**David Orban** [06:15:24]: Are you planning to do the demo now?

**David Orban** [06:15:27]: I

**Ivan Fattorusso** [06:15:27]: wasn't planning on doing it.

**Ivan Fattorusso** [06:15:28]: I had suggested that perhaps we do it.

**Ivan Fattorusso** [06:15:33]: I had suggested that perhaps we do in our distribution call tomorrow, because everyone's on that call, but I don't know if Toby, you thought that was

**Toby O'Connor** [06:15:44]: the right for him to do it.

**Toby O'Connor** [06:15:46]: Yeah, let me just jump in.

**Toby O'Connor** [06:15:47]: So it's not clear to me that Ivan is the natural owner of the CRM system.

**Toby O'Connor** [06:15:56]: I think it works quite well just given where everybody sits right now, and as his zazzel gets settled in.

**Toby O'Connor** [06:16:02]: And Iban's, you know, here has a pretty good grip of where we've been.

**Toby O'Connor** [06:16:09]: That, you know, he continues to do that.

**Toby O'Connor** [06:16:14]: But I wouldn't necessarily say that that that's Ivan's day job, right?

**Toby O'Connor** [06:16:20]: He's got other things to do.

**Toby O'Connor** [06:16:24]: common I would make is.

**Toby O'Connor** [06:16:28]: So the CRM is across the whole organization or whatever the mandate is.

**Toby O'Connor** [06:16:34]: So I'm coming at it very specifically from a distribution site.

**Toby O'Connor** [06:16:37]: So if I'm Greg and Nicola, what I'm trying to do is provide more structure and support to centralize effectiveness of how we approach both the mandate, the potential mandates that are coming on, which we have to take a decision on and whether it's a good use of our time to take them on based on our

**Toby O'Connor** [06:17:07]: view of success.

**Toby O'Connor** [06:17:09]: And then the mandates that we have, you know, effectively and crisply going out to the investors directly from Greg and Nicola or using other team members, right?

**Toby O'Connor** [06:17:22]: Now, that's all I'm trying to do.

**Toby O'Connor** [06:17:24]: In my, Toby, in my role as investors,

**Toby O'Connor** [06:17:33]: and do we have a way of capturing, because we're doing meetings the whole time.

**Toby O'Connor** [06:17:38]: We've got like Barone doing it, you know, Daniel, all these people are touching investors, right?

**Toby O'Connor** [06:17:43]: I had a early morning meeting this today with Asim, you know, he's got investors, right?

**Toby O'Connor** [06:17:47]: He's meeting with him in Dubai today.

**Toby O'Connor** [06:17:49]: Is, do we have a way of capturing those?

**Toby O'Connor** [06:17:51]: So when something in the, The external medical side pops up.

**Toby O'Connor** [06:18:00]: Something in the manufacturing side, something in the services side pops up.

**Toby O'Connor** [06:18:06]: There's just a way of capturing, sorry, there's a way of just organizing that information in a way that distribution can very effectively then go, okay, this is who I should be focusing on.

**Toby O'Connor** [06:18:19]: That's really my objective.

**Toby O'Connor** [06:18:21]: My last comment, and I'll shut up.

**Toby O'Connor** [06:18:23]: is I think for tomorrow, I've invited Sherwin on the call.

**Toby O'Connor** [06:18:27]: I'm looking to to Greg to run that call and I wanted to have a session, which is not this session, right?

**Toby O'Connor** [06:18:36]: And thank you for setting this one up, which is quite crisp to, you know, we're getting all organized around the CRM.

**Toby O'Connor** [06:18:43]: So whether we do the, you know, a demo, I don't really care.

**Toby O'Connor** [06:18:48]: I'd probably suggest not on that, but I did want to dedicate five or 10 minutes with a Zell maybe to give a little bit of a little bit of what he's trying to accomplish, or we're trying to accomplish around distribution, right?

**Toby O'Connor** [06:19:03]: That would be my objective tomorrow.

**Toby O'Connor** [06:19:04]: I don't think, I think the distribution call is the distribution call.

**Toby O'Connor** [06:19:07]: We should go through our five mandates, right?

**Toby O'Connor** [06:19:09]: We should go through our pipeline, and we should go through what we're going through, and then we have dedicated five, 10 minutes on what we're doing with the CRM.

**Toby O'Connor** [06:19:17]: I kind of like to show and to hear that, and that's it.

**Toby O'Connor** [06:19:22]: That would be my suggestion to that.

**Toby O'Connor** [06:19:24]: Don't me.

**Toby O'Connor** [06:19:27]: Sorry, please,

**Greg Wall** [06:19:29]: go ahead.

**Greg Wall** [06:19:30]: No, just on your first point there, Toby.

**Greg Wall** [06:19:32]: I I'm taking lot different approach, but a bit of a longer term view.

**Greg Wall** [06:19:38]: Absolutely, I can see even just, playing, probably not of the best word, using the system for a relatively short amount of time, that to capture who we're going to talk to you for these currently five clients.

**Greg Wall** [06:19:52]: When are we going to talk to them?

**Greg Wall** [06:19:53]: Yeah, I can see that can be done today.

**Greg Wall** [06:19:56]: That's not problem.

**Greg Wall** [06:19:57]: I think where my head is at is longer term, this is going to be our Alouan's investor database.

**Greg Wall** [06:20:08]: Client client and client number eight further along the line because my history is very much system based.

**Greg Wall** [06:20:16]: If I haven't got a system containing data of a high integrity, I'm going to cause myself issues further down the line.

**Greg Wall** [06:20:25]: So I guess I wanted to get it set to, absolutely not to slow anything down.

**Greg Wall** [06:20:31]: But I wanted to get it set as good as we can from the start rather than create ourselves a problem further down.

**Greg Wall** [06:20:40]: Does that make sense?

**Greg Wall** [06:20:42]: So yes, absolutely.

**Greg Wall** [06:20:43]: We can put in people that are being spoken to in the next couple of weeks for Axel, for instance.

**Greg Wall** [06:20:49]: Easy done.

**Greg Wall** [06:20:50]: How, however, if those 20 have just got their name and number, more or less against How do I know in six months time whether they're likely to be interested in my client number eight?

**Greg Wall** [06:21:03]: Do you see what I mean, where I'm going?

**Greg Wall** [06:21:05]: But I think the answer is just to find a balance between the two.

**Greg Wall** [06:21:08]: We don't want to slow the rollout and the use of the system down whatsoever, but we just need to find a way that we're actually capturing data that can be of use in the future, think.

**Greg Wall** [06:21:20]: Yeah,

**Toby O'Connor** [06:21:20]: no, I mean, I expect in that system, Ezel, to have areas of sector focus.

**Toby O'Connor** [06:21:27]: So name, organization, contact, email and mobile, sectors of interest, size, right?

**Toby O'Connor** [06:21:37]: Yeah.

**Toby O'Connor** [06:21:38]: Geography, something like that, right?

**Toby O'Connor** [06:21:40]: And then what David's got, right, is the overlay of maybe there's some tools that we overlay with the CRM that help help, help with that.

**Toby O'Connor** [06:21:52]: But we're saying the same thing.

**Toby O'Connor** [06:21:53]: I mean, I think, how many contacts did Nate give you yesterday?

**Izel Sequeira** [06:22:00]: It doesn't?

**Izel Sequeira** [06:22:01]: About

**Toby O'Connor** [06:22:01]: 8,800, yeah.

**Toby O'Connor** [06:22:04]: So huge numbers, and I'm sure that information was very garbled.

**Toby O'Connor** [06:22:09]: Yeah, right.

**Toby O'Connor** [06:22:10]: I'm sure it's going to take a long time to go through 8,000 contacts.

**Toby O'Connor** [06:22:14]: Exactly, yeah.

**Toby O'Connor** [06:22:15]: To do what Nicolet just said, right?

**Toby O'Connor** [06:22:18]: But actually having 8,000 contacts is somebody could start, right, from where we were two days ago.

**Toby O'Connor** [06:22:24]: Yeah.

**Toby O'Connor** [06:22:24]: If you're

**David Orban** [06:22:24]: Greg and Nicolet and Nate and everybody try to figure out these things.

**David Orban** [06:22:28]: So let's take a step back.

**David Orban** [06:22:30]: We mixing three things.

**David Orban** [06:22:34]: One is laying down an architecture that is solid and can accept.

**David Orban** [06:22:41]: Second, data sets that are clean enriched at the right level.

**David Orban** [06:22:50]: to be used today and tomorrow with different clients without having to ask ourselves if we are doing the right thing or we are wasting our time contacting investors that are irrelevant.

**David Orban** [06:23:06]: So all of those are doable and given our situation very pragmatically, all three are gonna be done at the same time.

**David Orban** [06:23:16]: We are cleaning data while we are least we are not architecting or re-architecting the system.

**David Orban** [06:23:30]: So it is just like it is.

**David Orban** [06:23:31]: If we started a year ago, then in a month we could completed the architecture, but we didn't, it's fine.

**David Orban** [06:23:41]: but it is reality.

**David Orban** [06:23:43]: We have we have to understand that and embrace Now, Toby.

**David Orban** [06:23:51]: Let me ask your

**Toby O'Connor** [06:23:52]: question, So you're absolutely right.

**Toby O'Connor** [06:23:54]: That's the outcome, So that's the outcome, if you're Toby or Greg or Nicolet or whoever, right?

**Toby O'Connor** [06:24:00]: That's the outcome that we want.

**Toby O'Connor** [06:24:02]: There's a process to that.

**Toby O'Connor** [06:24:05]: Is that what, let me ask you, this question is, so what support do you need working with David, to be able to achieve that.

**Toby O'Connor** [06:24:23]: Either of you could answer that question, right.

**Toby O'Connor** [06:24:27]: But that is exactly right, David, those three points, we're not mixing them.

**Toby O'Connor** [06:24:32]: That's the outcome that we want to achieve, right?

**Toby O'Connor** [06:24:34]: And I recognize it'll take a period of time to get that.

**Toby O'Connor** [06:24:37]: Well, the

**David Orban** [06:24:37]: reason I highlighted it is because ideally one would sit down, design the architecture of the CRM, then clean the CRM and then receive mandates and contact the subset of investors that they would based on the first two steps.

**David Orban** [06:24:58]: That would be wonderful.

**David Orban** [06:25:00]: And it is okay, we are not in that situation.

**David Orban** [06:25:03]: We are doing the three things, as long as we understand that there are still three different things.

**David Orban** [06:25:08]: Why it is worth doing that because will um.

**David Orban** [06:25:16]: And I will support Issel in giving her tools to efficiently clean the data, rather than than manually one by one.

**David Orban** [06:25:33]: And then potentially we will have also, as you call Toby, overlays, to make sure that the filtering and the selection also good in whatever ways we will One question to you, Toby.

**David Orban** [06:25:49]: You said that Ivan is the owner of the situation as is.

**David Orban** [06:25:55]: And that.

**David Orban** [06:25:56]: Well,

**Toby O'Connor** [06:25:56]: or he was.

**Toby O'Connor** [06:25:58]: Just in terms of where we are right now, his Zell's reporting line is to Yvon, right?

**Toby O'Connor** [06:26:05]: I don't necessarily

**David Orban** [06:26:05]: think that needs to be the case in six months.

**David Orban** [06:26:09]: I understand.

**David Orban** [06:26:10]: And what I need is for you to point me to the person that is my reference for the business decisions around how the CRM should be structured, right?

**David Orban** [06:26:27]: Because Nikola made some comments, and as an example, what fields are what kind and things like that.

**David Orban** [06:26:39]: They need to be translated into architecture, and I not shy to make those decisions, but it should come from the business unit.

**David Orban** [06:26:51]: It shouldn't come from me to

**Toby O'Connor** [06:26:53]: say, Nicola, your suggestion is correct.

**Toby O'Connor** [06:26:56]: There's two comments.

**Toby O'Connor** [06:26:56]: So this specific call is to distribution efficiency.

**Toby O'Connor** [06:27:01]: So the business owner is, if choose or two people, it would be Greg and Nicola, because they're likely to be the the leaders of how that's used, right.

**Toby O'Connor** [06:27:19]: Now, Ivan, for certainly this period of time.

**Toby O'Connor** [06:27:22]: with Azel needs to be part of that, but it's not his technical skill set do that.

**Toby O'Connor** [06:27:29]: But he understands the legacy and he's a very good transition into where we go.

**Toby O'Connor** [06:27:34]: The second comment I make is, I'm very aware, Azel's got a broader mandate than just distribution, right?

**Toby O'Connor** [06:27:40]: So, and you flow into that, David.

**Toby O'Connor** [06:27:43]: So this conversation with Azel is bigger than just distribution.

**Toby O'Connor** [06:27:50]: that make sense?

**Ivan Fattorusso** [06:27:51]: Can I also just just jump in and say we are actually a lot closer to where we need to be than maybe as perceived at the moment because I think the system has been set up in we're probably like over 80% of the way there in terms those three buckets architecture the data cleansing is is a huge

**Ivan Fattorusso** [06:28:17]: priority and that's what is Zell's been working on, you know.

**Ivan Fattorusso** [06:28:21]: And if there's tools that can facilitate that, David, I think.

**Ivan Fattorusso** [06:28:25]: But I think there's going to be hard to use AI because there's currently about 150 investors in the database.

**Ivan Fattorusso** [06:28:32]: I don't see any other way.

**Ivan Fattorusso** [06:28:34]: other than to query it one by one of each contact to

**Toby O'Connor** [06:28:38]: be able to.

**Toby O'Connor** [06:28:39]: Well, hang on a second, Eva, let me cut you off there.

**Toby O'Connor** [06:28:41]: And probably got to hop up another call in two minutes.

**Toby O'Connor** [06:28:44]: Yeah.

**Toby O'Connor** [06:28:45]: So let David make that assessment, right?

**Toby O'Connor** [06:28:48]: So this is what I'm trying to do is get the people who properly know what they're talking about to have the oversight.

**Toby O'Connor** [06:28:55]: So I bet you, David has a very good idea.

**Toby O'Connor** [06:28:59]: right of like two or three tools that would work very well for this right.

**Toby O'Connor** [06:29:05]: And that's what I want him to do once Zell has got kind of the framework.

**Toby O'Connor** [06:29:11]: And of course, if there's something that David thinks Zell should be doing to make that more effective now as we're building it.

**Toby O'Connor** [06:29:17]: You know, that, you know, but I wouldn't make the assumption that we have to do it one by one, right?

**Toby O'Connor** [06:29:27]: I would be a bit horrified if, if Nate puts in us 8,000 contacts, and then we have to do an AI tool one by one.

**Toby O'Connor** [06:29:35]: I mean, I think there's probably a better way of doing that, but I know.

**Toby O'Connor** [06:29:39]: I don't think you do either.

**David Orban** [06:29:45]: cleaning and making sure that the data is usable is the first AI can help also doing some very thorough research, scraping publicly available information that can enrich the data with things like sector, stage of investment and other components.

**David Orban** [06:30:16]: So all of that is eminently possible.

**David Orban** [06:30:20]: Obviously, nothing is better than having personal knowledge and personal relationships, and the two go hand in hand.

**David Orban** [06:30:29]: They are not, you know, exclusive or competing.

**Toby O'Connor** [06:30:37]: I'm just going to hop off, but but my last comment would be, you know, I think for the call tomorrow, the distribution call.

**Toby O'Connor** [06:30:45]: You, I think you should lead that CRM session, that part of it for five, 10 minutes, right?

**Toby O'Connor** [06:30:51]: Using Azel, right?

**Toby O'Connor** [06:30:53]: But say, because I think you play a critical, you understand where we've been and what we have.

**Toby O'Connor** [06:31:00]: And where we're trying to go, right.

**Toby O'Connor** [06:31:05]: And you allow Azel to kind of come in with what she's got and what she's trying to do.

**Toby O'Connor** [06:31:09]: And then you allow Greg and Nicola to make any comments on the back of that.

**Toby O'Connor** [06:31:13]: That's how I'd handle that five, 10 minutes.

**Toby O'Connor** [06:31:16]: But what I'm trying to show is that we've got some direction of what of travel here, right?

**Toby O'Connor** [06:31:23]: That's it.

**Toby O'Connor** [06:31:25]: And

**Greg Wall** [06:31:25]: can I just say, I know you've got to run, Toby, but Nicol and I've got a very good idea of what we need out of this system.

**Greg Wall** [06:31:33]: I think you did.

**Greg Wall** [06:31:34]: I just want to say that as a core process, we've been through it, we've identified what we want, we identified the things that we need, and we can talk to David Nizel and others about those things.

**Greg Wall** [06:31:46]: It might be perfect and we'll build on it, but we've got a very good idea of what

**Toby O'Connor** [06:31:51]: I think that's perfect, and I would expect you that.

**Toby O'Connor** [06:31:54]: That's what you want to start with that on the CRM.

**Toby O'Connor** [06:32:01]: Yeah, absolutely, you can start and then, Yvon, say kind of where we are in that with Zell.

**Toby O'Connor** [06:32:06]: I mean, that could be another way of handling that five, 10 minutes on the call

**Greg Wall** [06:32:10]: Okay, sure.

**Greg Wall** [06:32:11]: Now, you wanted to chat some time Toby,

**Toby O'Connor** [06:32:13]: just before Yeah, just give me 10 minutes and then you know how to chat.

**Toby O'Connor** [06:32:19]: Okay, Yeah, so I'll send an invite in minutes.

**Toby O'Connor** [06:32:22]: Yeah.

**Toby O'Connor** [06:32:22]: Okay.

**Toby O'Connor** [06:32:23]: Stay

**Ivan Fattorusso** [06:32:24]: and use this remaining time.

**Greg Wall** [06:32:27]: Yeah, I think so.

**Greg Wall** [06:32:30]: Nicole, do you to...

**David Orban** [06:32:33]: Oh, there you Okay, so I will leave shortly as well, but I wanted to make sure that we clear on a few things that I think are aligned with Toby.

**David Orban** [06:32:47]: And if we are not, then Ivan or Greg, probably you need to make sure that it is I don't think today is a good investment on Isolstein to learn how to design and implement the CRM system on the back end pipe drive.

**David Orban** [06:33:09]: She should she should, and unless IZel you believe you believe you should.

**David Orban** [06:33:23]: This is what I And if you are not contrary, would be taking Nicola's questions, turn them specification together with Nicola, a hundred more that you may have or however many.

**David Orban** [06:33:49]: since we need to change the base URL of the CRM anyway, which is now the entrepreneurs group.pipedrive.com, a very simple solution, Ivan, is to architect from the ground up the thing cloning the current site on AliBonggroup.piperive.com, introducing the changes that that Nikola suggests, and I still

**David Orban** [06:34:27]: haven't gotten the answer, who approving those requests, because it can be Nikola.

**David Orban** [06:34:38]: and just execute But if it is not the two of us, then someone else needs to that makes sense.

**David Orban** [06:34:47]: That is how we want to do David, please proceed.

**David Orban** [06:34:51]: So I asked the question and Toby

**Ivan Fattorusso** [06:34:54]: didn't answer.

**Ivan Fattorusso** [06:34:55]: think was quite clear that it's kind of Greg and Nicola's ultimately their leading distribution and I think It was pretty clear to me, he they're ultimately making those refinements and making those calls, right?

**Ivan Fattorusso** [06:35:10]: Okay, so you are

**David Orban** [06:35:11]: confirming that you are transferring the authority of making design and architecture decisions on the CRM from yourselves Yeah, yeah, I

**Greg Wall** [06:35:24]: mean, I think.

**Greg Wall** [06:35:26]: Yeah, yeah, yeah, so yes, just to confirm,

**David Orban** [06:35:31]: just to confirm the CRM is the system of record for context.

**David Orban** [06:35:36]: So we will have other views on a richer database, on a broader database where there will be marketing context, where there will be vendor context and so Because as of right now, we don't want to handle multiple databases.

**David Orban** [06:35:54]: But yes, for as long as investors are concerned, the architectural decisions and the implementation decisions, I will take them and and implement I would,

**Ivan Fattorusso** [06:36:09]: like I suggested earlier, sorry, Greg, quick one.

**Ivan Fattorusso** [06:36:12]: I think probably all four, all five of right now should run through the system on a share screen and you guys can share the questions that you've raised already as we go through it in the system itself and we can even make the changes in real time because it's really quite quick to do That's a

**Ivan Fattorusso** [06:36:35]: suggestion.

**Ivan Fattorusso** [06:36:36]: I feel like that would be the quickest way to And just one more thing in terms of David, you said it's the we need to change the domain URL from entrepreneurs to Aliwan.

**Ivan Fattorusso** [06:36:48]: I believe you probably know better than me, but I believe that's just we can change that without having to replicate this the whole system again.

**Ivan Fattorusso** [06:36:57]: That's

**David Orban** [06:36:58]: correct.

**David Orban** [06:36:59]: So that's correct.

**David Orban** [06:37:00]: That's fine.

**David Orban** [06:37:01]: Yeah.

**David Orban** [06:37:01]: That's correct.

**David Orban** [06:37:05]: Okay, Do you

**Ivan Fattorusso** [06:37:08]: guys agree with what I just suggested?

**Ivan Fattorusso** [06:37:10]: Yes,

**David Orban** [06:37:13]: and I don't think I need to there when you share the screen and make the changes.

**David Orban** [06:37:21]: Nicola, maybe if you want to do that the way that Ivan described, you can send me the spreadsheet updating the rows where some of the things you asked are already Yeah,

**Greg Wall** [06:37:36]: I've just pinged you the spreadsheet and I was going to say that's definitely version 0.0.0. And I'm going to supplement it with, Greg and I've walked through from a workflow perspective, how we see various types of communication going.

**Greg Wall** [06:37:52]: So going to add to Yeah, so just, I mean, by all means, it's all still I'm just sitting expectations that I'm certainly going to be adding to it, I'm

**David Orban** [06:38:04]: Yes, no, no, no, I was surprised how short the list was already, so feel free.

**David Orban** [06:38:10]: That's why I said 100 when I said before the number of things.

**David Orban** [06:38:14]: Absolutely.

**David Orban** [06:38:16]: Okay.

**David Orban** [06:38:17]: So, Ivan, you suggested that you want to and make these changes If you can it, I will leave the calls, and then Nicola will let me know what you guys actually updated live,

**David Orban** [06:38:39]: Ivan, do you want to discuss anything else before No, I

**Ivan Fattorusso** [06:38:43]: think we're clear, and, you know, Greg, Nicola, do you want to do it now?

**Ivan Fattorusso** [06:38:48]: Do you want to use the

**Greg Wall** [06:38:49]: remaining 20 minutes, or do you want to do it another time?

**Greg Wall** [06:38:52]: I'm always a person to do it while we're facing Let's get it

**David Orban** [06:38:59]: done.

**David Orban** [06:38:59]: Okay.

**David Orban** [06:39:00]: I don't like I don't like putting it off.

**David Orban** [06:39:02]: comfort.

**David Orban** [06:39:03]: Fantastic.

**David Orban** [06:39:04]: And I'm looking forward to the updated and expanded list

**Greg Wall** [06:39:09]: from you, Nicola.

**Greg Wall** [06:39:10]: Okay, thank you.

**Greg Wall** [06:39:11]: Bye-bye.

**Greg Wall** [06:39:12]: Thanks, David.

**Greg Wall** [06:39:14]: I just need a quick comfort break.

**Greg Wall** [06:39:16]: back.

**Greg Wall** [06:39:21]: By the way, I

**Ivan Fattorusso** [06:39:22]: know if know you're having network issues.

**Ivan Fattorusso** [06:39:26]: You don't necessarily need to be on the remaining part of this call, because we're just going through pipe drive in a bit more detail.

**Ivan Fattorusso** [06:39:34]: So I think it was just that the start, Toby, was mentioning your involvement in distribution and the operational side of you're free to jump off if you Okay, no

**Greg Wall** [06:39:46]: worries.

**Greg Wall** [06:39:47]: Excellent.

**Greg Wall** [06:39:47]: Excellent, before Yes, I've been, I just want to say, don't think I've forgotten about you.

**Greg Wall** [06:39:54]: I absolutely have it.

**Greg Wall** [06:39:56]: In terms of what Toby has said about you being a resource there and coordinating a range of things.

**Greg Wall** [06:40:04]: We are going through pipe drive thing.

**Greg Wall** [06:40:07]: We're defining systems and dropping out of that is going to be effectively how we work.

**Greg Wall** [06:40:13]: And we're just trying to define that.

**Greg Wall** [06:40:14]: So don't think I'm not thinking about you got you in the back of my head.

**Greg Wall** [06:40:20]: Well, I'm saying, a sit type, and the way that we're in.

**Greg Wall** [06:40:26]: Okay,

**Axel Zanner Entwistle** [06:40:30]: brilliant, sounds good.

**Axel Zanner Entwistle** [06:40:31]: No worries, that's all.

**Axel Zanner Entwistle** [06:40:32]: Yeah, obviously, it's the nature of the beast, isn't it?

**Axel Zanner Entwistle** [06:40:36]: It's lots, I think, yeah, as you said, so yeah, no worries.

**Axel Zanner Entwistle** [06:40:43]: I'm on standby, whatever you whenever you're ready, give me a shout, and I'm

**Greg Wall** [06:40:49]: help.

**Greg Wall** [06:40:49]: Okay, good on you.

**Greg Wall** [06:40:50]: Thanks,

**Axel Zanner Entwistle** [06:40:51]: Brilliam.

**Axel Zanner Entwistle** [06:40:51]: Pleasure to see you, Greg.

**Axel Zanner Entwistle** [06:40:52]: And apologies for not getting my camera on.

**Axel Zanner Entwistle** [06:40:55]: As Yvon mentioned, having some connection issues at the minute.

**Axel Zanner Entwistle** [06:40:59]: So yeah, look forward to working

**Greg Wall** [06:41:05]: All right, take care.

**Greg Wall** [06:41:05]: Bye-bye.

**Ivan Fattorusso** [06:41:09]: right.

**Ivan Fattorusso** [06:41:10]: Can everyone see the screen?

**Ivan Fattorusso** [06:41:12]: Yeah.

**Ivan Fattorusso** [06:41:14]: Okay, yeah, no, I guess.

**Ivan Fattorusso** [06:41:19]: I'll run through it.

**Ivan Fattorusso** [06:41:22]: What I see is the chronological or kind of logical way that the system is generally set up.

**Ivan Fattorusso** [06:41:28]: So this is the main contact section where you've all of the people that are currently in the database.

**Ivan Fattorusso** [06:41:35]: The filtering functionality in Pipedrive is pretty good.

**Ivan Fattorusso** [06:41:40]: So eventually we want to get to a place we can say like person, label, is investor and they like to invest in renewables and they are situated in the US and they like to do you

**Greg Wall** [06:42:05]: mind I ask questions as we go along

**Ivan Fattorusso** [06:42:08]: sorry or should I let you just please no no no do you interrupt That's too

**Greg Wall** [06:42:15]: negative a word.

**Greg Wall** [06:42:17]: first piece there is a investor.

**Greg Wall** [06:42:20]: It's also quite a generic label.

**Greg Wall** [06:42:22]: Investors, aside from sectors that they're interested in.

**Greg Wall** [06:42:26]: They might be VC, PE, hedge, et cetera, whatever.

**Greg Wall** [06:42:31]: Am I right in saying at this level, you just keep it high level.

**Greg Wall** [06:42:36]: They're an investor as opposed I don't know, I don't know.

**Ivan Fattorusso** [06:42:42]: Is that Yeah, so at this level, it is just the sort It's an investor.

**Ivan Fattorusso** [06:42:49]: Most high level, I'll go into shortly, there is a, there is also a It has been set up such that we do go one level deeper and tag, whether they're a family office, whether they're a VC, whether they're private equity firm, right?

**Ivan Fattorusso** [06:43:06]: So we do go deeper that.

**Ivan Fattorusso** [06:43:08]: So I'll get to that in a sec.

**Ivan Fattorusso** [06:43:10]: But let me just chat you through the labeling system, right?

**Ivan Fattorusso** [06:43:15]: Because investor is one of the labels.

**Ivan Fattorusso** [06:43:19]: And then you've got clients.

**Ivan Fattorusso** [06:43:23]: So for example, let's see, let's take a quick look, right, clients.

**Ivan Fattorusso** [06:43:27]: These are all our current clients that were mandated who we have an active mandate to distribute, right?

**Ivan Fattorusso** [06:43:36]: this is largely what you guys have also seen in the in the deal distribution sheet, right, that Toby has circulated a few times.

**Ivan Fattorusso** [06:43:51]: Then you've got former clients, people who used to work with, but no longer do.

**Ivan Fattorusso** [06:43:56]: Then we've got prospects, right, and prospect like investor is quite a broad term right now, because prospects Could be investment banking prospects who will one day turn into clients if we get mandated But prospects as of right now are also potential companies that we might invest in ourselves as

**Ivan Fattorusso** [06:44:20]: Adliwan later down Or they might be wealth management prospects.

**Ivan Fattorusso** [06:44:27]: So the term prospect at this level is really a broad Then you've got investors like we just discussed.

**Ivan Fattorusso** [06:44:39]: And these additional bits, service providers, you who in often, in many cases, we might have partnership agreements with, for example.

**Ivan Fattorusso** [06:44:51]: That's something that Lee is working on in his capacity the director of channel partnerships.

**Ivan Fattorusso** [06:44:57]: He's look, he's like, we have referral agreements, right?

**Ivan Fattorusso** [06:45:02]: That can either refer us business or that we can use as sources of distribution.

**Ivan Fattorusso** [06:45:07]: So that's for example, you know, within here you'll find whatever CSPs, you might find law firms, you might find other advisory firms, etc.

**Ivan Fattorusso** [06:45:16]: Then you got government contacts, anyone who works within government really, that's pretty straightforward, media and press.

**Ivan Fattorusso** [06:45:24]: So this is more kind of skewed towards what Alicia is doing from a marketing perspective, PR.

**Ivan Fattorusso** [06:45:30]: She does know a lot of people in that space and therefore we're capturing them in the And then portfolio slash investments companies, fundamentally investees, companies are within our portfolio, which at this stage is still extremely limited.

**Ivan Fattorusso** [06:45:48]: I mean, I think we only have one in here, which is one of the companies that is within the Israeli fund that we have and one of them has been invested into.

**Ivan Fattorusso** [06:46:01]: as we grow and as we start to make investments, then we'll also be tagging those, And one comment I'll make as well right now that... You know, we're by no means at the stage where this is perfect, but I think the thinking behind it has been, you know, there's been quite a bit of thinking behind it

**Ivan Fattorusso** [06:46:25]: but the general premise is, and that's what we're here to do, make improvements.

**Ivan Fattorusso** [06:46:29]: So if there suggestions, changes, improvements that we can make, then obviously this is what this for.

**Ivan Fattorusso** [06:46:36]: So that clear as in terms of the overall labeling system.

**Ivan Fattorusso** [06:46:41]: Obviously as far as distribution goes, it's largely, it's largely this label that we're interested

**Greg Wall** [06:46:48]: And just a side on these screens, it's something haven't been able to determine.

**Greg Wall** [06:46:52]: Can do I have autonomy to do my own screen layouts so I can choose which columns I want on each

**Ivan Fattorusso** [06:47:02]: screen or is fixed?

**Ivan Fattorusso** [06:47:03]: You can, yeah, you can drag drop columns.

**Ivan Fattorusso** [06:47:07]: You can, you can also select what columns you want to add and see in your

**Greg Wall** [06:47:13]: layout, yeah.

**Greg Wall** [06:47:14]: Okay, that was the type thing I didn't want to try out on the live system.

**Greg Wall** [06:47:18]: Okay, thank

**Ivan Fattorusso** [06:47:19]: Yeah, Right, okay, so then let's now like dive a little bit into investors, right, of investors.

**Ivan Fattorusso** [06:47:27]: We've currently got 160 people that are tagged as an investor in the database.

**Ivan Fattorusso** [06:47:33]: Now, Isil is going through an exercise, which is kind of the key cornerstone and exercise to begin with that we need to do is to query all of these investors and to actually determine whether these guys are real active credible investors, right?

**Ivan Fattorusso** [06:47:56]: historically we've probably put people in here that we've done it quite loosely.

**Ivan Fattorusso** [06:48:02]: So we are going through right now and exercise to genuinely determine whether these guys are, you know, an accurate set of investors that we can take deals So that's the first thing, right?

**Ivan Fattorusso** [06:48:15]: And we're going to have to all the time.

**Ivan Fattorusso** [06:48:18]: But as long as we get this first set of investors right, we put very of stringent to ensure that any new investors that go into the database match a certain criteria and they they really, we can be confident of the fact that everything that goes in there is is solid, right?

**Ivan Fattorusso** [06:48:43]: So now I'll actually go into one of them, for example, this guy.

**Ivan Fattorusso** [06:48:52]: So there's the person's profile.

**Ivan Fattorusso** [06:48:57]: This person was created over a year And clearly nothing has really happened with this person because otherwise if there had been emails, it would all be logged here.

**Ivan Fattorusso** [06:49:11]: ask,

**Greg Wall** [06:49:12]: sorry to interrupt, that's one of my questions on my spreadsheet.

**Greg Wall** [06:49:17]: You've got relationship manager.

**Greg Wall** [06:49:19]: And then you've also got top the

**Izel Sequeira** [06:49:24]: Am I right, saying the owner is the person who has created the entry?

**Izel Sequeira** [06:49:29]: Oh, sorry, I'm sorry.

**Ivan Fattorusso** [06:49:34]: Yeah, you're right, Nicola.

**Ivan Fattorusso** [06:49:36]: This is the person that sort of entered it into the system.

**Ivan Fattorusso** [06:49:41]: Okay, okay.

**Ivan Fattorusso** [06:49:42]: Or actually, Michael, Michael, Michael.

**Ivan Fattorusso** [06:49:47]: Because from on a,

**Greg Wall** [06:49:52]: from a, from a distribution perspective, which goes back to the piece I raised when David was on in terms of user rights, that is extremely worrying that take this was an example in theory.

**Greg Wall** [06:50:04]: You could go in the way, you know, you could go in effect, being a bit territorial of Yeah.

**Greg Wall** [06:50:12]: Because suddenly someone could go in and change the ownership.

**Ivan Fattorusso** [06:50:16]: So, yeah, so Nicola, on that point, there is a way to address that.

**Ivan Fattorusso** [06:50:22]: There there isn't a way to like lock things.

**Ivan Fattorusso** [06:50:27]: So anyone who has an on the technically is able to edit stuff.

**Ivan Fattorusso** [06:50:36]: However, I think the best way to address that particular point is that when you add people onto the system, you you can toggle the visibility, right?

**Ivan Fattorusso** [06:50:49]: for example, if you did want to be relatively, you know, protective and you did want to ensure that other people didn't necessarily play around or do anything unbecoming with any of the the context You can make it such the contact is only visible and global admins.

**Ivan Fattorusso** [06:51:11]: Global admins are very few people.

**Ivan Fattorusso** [06:51:13]: Currently it's myself, David That is up for discussion who remains global admin, but ultimately it's probably going to be one or two people end, So, so you can be able to keep them highly private.

**Ivan Fattorusso** [06:51:33]: You can do that.

**Ivan Fattorusso** [06:51:34]: And that means nobody else will be able to see them and change But they will be

**Greg Wall** [06:51:40]: visible.

**Greg Wall** [06:51:41]: if I just said it everyone could see.

**Greg Wall** [06:51:43]: This is just a generic system question.

**Greg Wall** [06:51:46]: And someone did decide to change it, maybe by mistake even.

**Greg Wall** [06:51:50]: Do I get notified as the original owner that a change has been made to one of my line

**Ivan Fattorusso** [06:51:56]: I think you know, channel

**Izel Sequeira** [06:52:01]: log like, you know, audit trail, so you can actually see who did that, but I don't think we get notified as now.

**Ivan Fattorusso** [06:52:10]: I think you can get notified via obligations.

**Ivan Fattorusso** [06:52:14]: So wait, let me just see, so change.

**Ivan Fattorusso** [06:52:16]: That

**Greg Wall** [06:52:16]: would be another way, obviously, well.

**Greg Wall** [06:52:18]: By this.

**Greg Wall** [06:52:19]: You can have a look at this

**Ivan Fattorusso** [06:52:20]: change log a bit, Nicholas.

**Ivan Fattorusso** [06:52:22]: I just changed the source from external to and it shows that I made that So actually everything that changes here is actually recorded.

**Ivan Fattorusso** [06:52:34]: Okay.

**Ivan Fattorusso** [06:52:39]: So that is effectively a way to monitor if any changes have been made.

**Ivan Fattorusso** [06:52:45]: But also there is, I believe there is a way to, if you did want to get point where you actually get notified if any changes We could do that because you can set up a workflow automation, which basically sets up a thing which says, any field changes, send me email, for example.

**Greg Wall** [06:53:07]: Yeah.

**Greg Wall** [06:53:10]: Okay.

**Ivan Fattorusso** [06:53:13]: So, coming back here.

**Ivan Fattorusso** [06:53:15]: mean, this is all relatively clear.

**Ivan Fattorusso** [06:53:19]: Do stop me if you want add anything.

**Ivan Fattorusso** [06:53:26]: It was the

**Greg Wall** [06:53:27]: disorganization bit that was concerning.

**Greg Wall** [06:53:29]: The high level industry and industry sector.

**Greg Wall** [06:53:37]: I'm pretty sure they're both one to one, i.e.

**Greg Wall** [06:53:39]: you can only assign one which really somewhat problematic.

**Ivan Fattorusso** [06:53:47]: Right.

**Ivan Fattorusso** [06:53:47]: So I think I know what you mean here, Nicolaf.

**Ivan Fattorusso** [06:53:50]: So actually, this industry sector bit at the company level.

**Ivan Fattorusso** [06:53:56]: So it doesn't really apply to an investor because, I mean, you might, for an investor, you might say financial I mean, let's just say broad level.

**Ivan Fattorusso** [06:54:06]: It's a financial services, it's actually, it's actually not financial services.

**Ivan Fattorusso** [06:54:10]: But for an investor, this really doesn't apply.

**Ivan Fattorusso** [06:54:13]: But for the purpose of what we want, which is to be able tag what sectors investors are interested there is this subsection, right?

**Ivan Fattorusso** [06:54:24]: So for any, these three specific labels, an investor is one of them, and is obviously the one that relates to what we're doing here in distribution.

**Ivan Fattorusso** [06:54:33]: There's this.

**Ivan Fattorusso** [06:54:33]: There's this is a multiple option field.

**Greg Wall** [06:54:45]: I mean, that makes sense.

**Greg Wall** [06:54:46]: I would question.

**Greg Wall** [06:54:47]: I think it does actually apply at the organization level

**Ivan Fattorusso** [06:54:53]: mean, I guess an investor would just be...

**Greg Wall** [06:55:01]: I think the key is, as long practically every value at an investor is a many to one relationship, including, know, they might do P and they debt, they might do both, nothing, almost.

**Greg Wall** [06:55:20]: Thinking off the top of my head can be a one-to-one relationship.

**Greg Wall** [06:55:23]: long as everywhere, I've got an option to assign multiple

**Ivan Fattorusso** [06:55:28]: and I think Yeah, I think, so this bit really needs a bit more thought.

**Ivan Fattorusso** [06:55:35]: It needs to be built out, right?

**Greg Wall** [06:55:37]: It's the other thing think that I couldn't find, again, happy that it's me being paying enough The country where an investor actually, where their mandate allows them to I can see where the company itself is based, the HQ, But where they are allowed, what regions they're allowed to invest in.

**Greg Wall** [06:56:04]: It's also a completely different kettle I couldn't find where we that.

**Ivan Fattorusso** [06:56:10]: We can add that all here, right?

**Ivan Fattorusso** [06:56:12]: So beyond target sectors, which is the most basic We can add here, you know, what geographies they tend what instruments that, you know, do they do equity debt?

**Ivan Fattorusso** [06:56:27]: You know, we can do those stuff, what taking with ticket size that.

**Ivan Fattorusso** [06:56:31]: So think it's probably

**Greg Wall** [06:56:35]: up to you.

**Greg Wall** [06:56:35]: Is that something that you could do front end, as it were, or is that a David No, I can do that.

**Greg Wall** [06:56:41]: To me, that's config screen But then it needs an entry in the database, doesn't

**Ivan Fattorusso** [06:56:47]: I can do that because I'm a global admin, as is David, as is Isol So I can go right now into the data and I can create a new custom pick its right, and I can create it.

**Ivan Fattorusso** [06:57:10]: can make, I can create geography.

**Ivan Fattorusso** [06:57:13]: And so this is the key point probably Nicola, yourself and Greg, want to have a little think, if you haven't already done so as to what are the precise fields that we want to have in this in this box, beyond just the target What do we want to have, right?

**Ivan Fattorusso** [06:57:36]: Because this This bit here is fundamentally the most important bit, because this is what allows in three to six months to use that filter functionality to really hone in on the right investors that correspond to any given Yeah.

**Greg Wall** [06:57:58]: Okay, we'll take that, I'll take that.

**Greg Wall** [06:58:05]: So what we'll do in my one or 1.1 of my questions requirements.

**Greg Wall** [06:58:10]: I'll Cool.

**Greg Wall** [06:58:13]: To the level of specificity of what I would ideally

**Ivan Fattorusso** [06:58:20]: Yeah.

**Ivan Fattorusso** [06:58:24]: And the ones, high value relationship, the term, I mean, what does high value relationship actually mean, high level access?

**Ivan Fattorusso** [06:58:35]: Again, what does that actually mean?

**Ivan Fattorusso** [06:58:36]: These, this entire box is very much up discussion and up for improvement.

**Ivan Fattorusso** [06:58:45]: And I said, this is the key, this is really key bit for the distribution purposes.

**Ivan Fattorusso** [06:58:56]: I think, I think that's sort of

**Greg Wall** [06:59:02]: at that level of detail.

**Greg Wall** [06:59:03]: I think that covers it.

**Greg Wall** [06:59:05]: don't know if you had a chance to see my other questions at a non-specific workflow level are more systems like emails.

**Greg Wall** [06:59:14]: I can understand we want to sync our email systems.

**Greg Wall** [06:59:17]: And I understand that the net result will be email flooding system.

**Greg Wall** [06:59:26]: How is the key.

**Greg Wall** [06:59:28]: There must, David, I'm sure it's got an AI tool.

**Greg Wall** [06:59:34]: Otherwise, three or four different users would be trawling through a raft of emails, putting together a different story and no one coming up with exactly the status.

**Greg Wall** [06:59:50]: make sense?

**Greg Wall** [06:59:51]: I think it's a case of, haven't got my lipid I can't be in the camera.

**Greg Wall** [07:00:00]: Unless data is actually effectively then what's the point of having almost.

**Greg Wall** [07:00:07]: But I think that's probably a David thing because his his I've used AI tools before to do sort of we call it moderate.

**Greg Wall** [07:00:16]: So that's probably separate.

**Greg Wall** [07:00:18]: And then more, I just want to steer the more.

**Greg Wall** [07:00:25]: I just want to steer on strategically what files are expected to be Because in my head, pipe drive a document repository.

**Greg Wall** [07:00:35]: what treasures use No, for, yeah, so I've got a number tools, it.

**Greg Wall** [07:00:41]: Assana.

**Greg Wall** [07:00:42]: Anyway, overall, a bit of clarity on, strategically, which system is supposed to be used if that sense.

**Greg Wall** [07:00:51]: Yeah.

**Greg Wall** [07:00:52]: The other side, I don't know if you want to do it now, but we went through what we expect our workflow to be.

**Greg Wall** [07:00:59]: I haven't shared And this what we think.

**Greg Wall** [07:01:05]: So I'm just got it in front of me just to see what other sort of questions might come up.

**Greg Wall** [07:01:09]: Reporting is a big don't know if there's a separate reporting tool that overlays Yeah.

**Greg Wall** [07:01:18]: But obviously reports that need to generate in order to manage the function is And then the flip side of that is reports the wider management well.

**Greg Wall** [07:01:31]: Yeah, we have.

**Greg Wall** [07:01:32]: Is it going to be a separate reporting tool?

**Greg Wall** [07:01:34]: Do you know?

**Greg Wall** [07:01:34]: No, no.

**Ivan Fattorusso** [07:01:35]: There's an inbuilt, there's an inbuilt analytics section, which will be able to everything.

**Ivan Fattorusso** [07:01:42]: We'll be able to create reports very sort of detailed, based on everything we just went through quite customized.

**Greg Wall** [07:01:53]: to customize it.

**Greg Wall** [07:01:55]: So in theory, I'd be to generate a report for this particular client.

**Greg Wall** [07:02:02]: thinking aloud at moment.

**Greg Wall** [07:02:04]: For this particular client, how many investors touched overall?

**Greg Wall** [07:02:09]: How many and how many remaining?

**Greg Wall** [07:02:14]: And even on a per investor how often have we engaged them and for which client?

**Greg Wall** [07:02:22]: Because our process, we very much keep our all our investors And by that, even if we haven't deal for them.

**Greg Wall** [07:02:31]: We touch base with them and say, hey, how are going?

**Greg Wall** [07:02:34]: Don't forget about us.

**Greg Wall** [07:02:36]: Just to keep So we'd need to that.

**Greg Wall** [07:02:40]: And then key for efficiency, we'd want for each stage of the workflow.

**Greg Wall** [07:02:47]: for how long has a client remained in a particular stage because I think that can be very good management to see where their potential inefficiencies and where we've got opportunities to improve effectively.

**Greg Wall** [07:03:04]: Yeah.

**Greg Wall** [07:03:07]: So that type of thing, other sort of reports that we'd be for.

**Greg Wall** [07:03:11]: All of

**Ivan Fattorusso** [07:03:11]: that can be done, Nicola.

**Ivan Fattorusso** [07:03:14]: And it's done in several different ways.

**Ivan Fattorusso** [07:03:17]: I mean, this is the fundraising and distribution pipeline, Which, again, needs work.

**Ivan Fattorusso** [07:03:23]: And definitely one of the key areas that you guys also should think about is whether these right stages.

**Greg Wall** [07:03:31]: And what do, what I do first thing tomorrow, I'll write up all my notes on the workflow, and this will create version two of my questions.

**Greg Wall** [07:03:39]: But just I'm very aware of the time just quickly as an example.

**Greg Wall** [07:03:43]: your far left one there, the packaging, the packaging is made up of, I think about six different functions from a distribution perspective.

**Greg Wall** [07:03:56]: I think I might have copied you on what I called my shopping I need to change the words I So in other CRMs I've used, you have a swim lane, but you sub-categories within a swim lane, so you can see at which point of the overall function a client What I wouldn't want is for each of the six areas just

**Greg Wall** [07:04:21]: activities held there, because we need to be able to for example, percentage of each component Does sense?

**Ivan Fattorusso** [07:04:36]: Sorry, Nicole, I don't know if I... Say no, it's quite all right.

**Ivan Fattorusso** [07:04:39]: Yeah, I didn't So I've

**Greg Wall** [07:04:42]: got packaging.

**Greg Wall** [07:04:43]: So I've got the financial metrics analysis.

**Greg Wall** [07:04:51]: Right.

**Greg Wall** [07:04:53]: Um, in previous investor feedback.

**Greg Wall** [07:04:56]: So just few of them.

**Greg Wall** [07:04:57]: Um, um, collateral, collateral, um, so no.

**Greg Wall** [07:05:04]: So I would want to see each of the six components.

**Greg Wall** [07:05:10]: involved in the overall packaging workflow.

**Greg Wall** [07:05:14]: Well, don't want it to be, I mean, you could say, or they could each have their individual swim lane, but then that's a bit OTT, Yeah.

**Greg Wall** [07:05:26]: If there's another layer within the packaging that we could split that could But the key is me and my many one.

**Greg Wall** [07:05:38]: I think like we said in our call the other day, most activities are not sequential.

**Greg Wall** [07:05:44]: Yeah.

**Greg Wall** [07:05:45]: So we need to be able to capture a client would need to appear in more than section with an associated percentage Right, I see.

**Greg Wall** [07:05:59]: I'll write this up to try and hopefully explain better.

**Greg Wall** [07:06:02]: No,

**Ivan Fattorusso** [07:06:02]: no, I see what When you say, like, that is going into quite a lot of detail.

**Ivan Fattorusso** [07:06:09]: As you it's not sequential and stuff happens a bit concurrently so like, yeah, I guess it just really just depends how much detail makes sense to go packaging alone, as it is right now, isn't detailed enough, which is fair.

**Ivan Fattorusso** [07:06:31]: We But when you say percentage complete, how would you do you measure percentage complete?

**Greg Wall** [07:06:40]: You're supposed to ask difficult questions.

**Izel Sequeira** [07:06:43]: Maybe like the timeline process of that particular stage that do.

**Izel Sequeira** [07:06:47]: Let's say that packaging for financials you have around a week or something, and then we could track

**Greg Wall** [07:06:56]: And let me at great risk, let me open here, make a smile.

**Greg Wall** [07:07:03]: But to give you a, to kind give you an You know, if you look at the financial model, that is going to take some and there's a whole bunch of stuff going on with it.

**Greg Wall** [07:07:16]: And we're probably going to want some on where that's up to and if there's any kind issues with it here, like from management right?

**Greg Wall** [07:07:29]: So that's financial modeling, sensitivity analysis, You know, generating pitch decks, you know.

**Greg Wall** [07:07:38]: There's a whole bunch stuff that has to get done in what we now call packaging before it gives the distribution.

**Greg Wall** [07:07:46]: There's a whole bunch that have done.

**Greg Wall** [07:07:50]: How we monitor, how monitor where they're to, is kind of the next discussion, and I'm not sure about that yet, but all I'm saying is there's a of some categories.

**Ivan Fattorusso** [07:08:02]: Which is, yeah, absolutely clear.

**Ivan Fattorusso** [07:08:04]: mean, whether that level of detail, think, would make sense to go in Asana.

**Ivan Fattorusso** [07:08:11]: I don't know if you guys have heard of Asana or know that we use Asana as a project management that, for me, that level of granularity doesn't necessarily sit in that sales pipeline.

**Ivan Fattorusso** [07:08:23]: That level of granularity is something that we track and project management tool.

**Ivan Fattorusso** [07:08:29]: And then, and then my suggestion at this point, not having really thought about it too packaging just remains as one simple column, but then all the granularity of what you just talked about goes into the project Suggestion, but again, I think more for us to think

**Greg Wall** [07:08:49]: about.

**Greg Wall** [07:08:49]: Is it a sign I look to Yeah, because I'm very reticent about using multiple tools.

**Greg Wall** [07:08:56]: that.

**Greg Wall** [07:08:57]: Just my experience talking here.

**Greg Wall** [07:08:59]: The rest of people, Yeah.

**Greg Wall** [07:09:02]: Do they link Asana and pipe link?

**Greg Wall** [07:09:05]: Talk

**Ivan Fattorusso** [07:09:05]: to each other.

**Ivan Fattorusso** [07:09:06]: do link.

**Ivan Fattorusso** [07:09:07]: Yeah, they do.

**Ivan Fattorusso** [07:09:09]: The result, there's also a project there's also a project management feature in So actually that might be the answer.

**Ivan Fattorusso** [07:09:18]: If it's not, you know, seamlessly integrating between Asana drive, We may, we may decide to use the project management feature in pipe drive, which based on what you guys are saying I feel like might be the right answer if that's It's pretty much the it's pretty much that stage, but it's more

**Ivan Fattorusso** [07:09:42]: project management T in that it allows you to assign tasks, look know, tick them off in a very project management way, whereas that what we just looked at look at is more of the sales pipeline.

**Ivan Fattorusso** [07:09:55]: which is slightly

**Greg Wall** [07:09:59]: I think that's one we can think I think that's one can think just to underline the kind of the, in very, very good time here.

**Greg Wall** [07:10:13]: underline, kind of, just to underline kind of using a real example.

**Greg Wall** [07:10:16]: If you look at Axel, Heal, for instance, Ivan, that you're very with.

**Greg Wall** [07:10:21]: I think we signed August, some time that.

**Greg Wall** [07:10:27]: technically they've been in packaging from all the structure But there's been a whole heap of stuff Right throughout process.

**Greg Wall** [07:10:38]: But from a pipe drive perspective, they're just in packaging for Yeah,

**Ivan Fattorusso** [07:10:45]: exactly.

**Ivan Fattorusso** [07:10:46]: But I think that raises an entirely another question, think, guys, should be involved in the case of Axle Hill, we started, yeah.

**Greg Wall** [07:11:00]: That's me ticking things.

**Greg Wall** [07:11:01]: Don't worry, Toby and I are on that.

**Greg Wall** [07:11:02]: So we're, that's definitely going happen.

**Greg Wall** [07:11:06]: Yeah.

**Greg Wall** [07:11:06]: Yeah.

**Greg Wall** [07:11:08]: OK, John, that.

**Greg Wall** [07:11:10]: That's

**Greg Wall** [07:11:15]: no, enough.

**Greg Wall** [07:11:16]: I think probably what's best just, I will write up my remaining quest, hopefully in a clear way for people easier.

**Greg Wall** [07:11:31]: And we'll also outline at a level our workflow from a distribution.

**Greg Wall** [07:11:35]: That's what I'm Oh, right.

**Greg Wall** [07:11:37]: Okay.

**Greg Wall** [07:11:37]: They're all my questions.

**Greg Wall** [07:11:38]: I'll wrap Yeah.

**Greg Wall** [07:11:41]: And then we can use that as the base and we can go from there.

**Greg Wall** [07:11:43]: I won't be able to do it I have to do it in the morning.

**Greg Wall** [07:11:47]: So that's morning well.

**Greg Wall** [07:11:50]: Yeah.

**Ivan Fattorusso** [07:11:52]: Oh, good.

**Ivan Fattorusso** [07:11:54]: Good, good.

**Ivan Fattorusso** [07:11:55]: This is useful, because I think when we have the distribution call tomorrow, we've aligned quite well.

**Ivan Fattorusso** [07:12:02]: So I think, yeah, we're good place.

**Greg Wall** [07:12:07]: Yeah.

**Greg Wall** [07:12:08]: I think everything I wanted to onto, I don't know.

**Greg Wall** [07:12:11]: In our call last week, we suggested that we could use, or it was suggested Axel Hill as like a dry And use, everyone use their proposed workflows, blah, I'm not quite sure how realistic didn't mean Fartre.

**Greg Wall** [07:12:37]: terms of, yeah.

**Greg Wall** [07:12:38]: I'm thinking more about the sort of the offline communication we've got to resolve, bit like if Peter Bartlett's going to involved.

**Greg Wall** [07:12:46]: I'm assuming he won't be allowed or you shouldn't allowed.

**Greg Wall** [07:12:50]: login to you know, you know, you're sharing all of that with an external consultant or consultant or whatever.

**Greg Wall** [07:13:01]: So how do we wrap him into the process communications he had his, because we're going to be very leaning on him quite heavily for investors, best doors for Axel.

**Greg Wall** [07:13:14]: Look, it's a very point, Nicol.

**Greg Wall** [07:13:15]: So it's that type, those are much of our type questions, the process, which needs to be sorted by the system, but are actually dependent sort of wider discussions really.

**Greg Wall** [07:13:25]: And just, I just want to kind of emphasize What Nicol has said is going to be a very, very common scenario with every client.

**Greg Wall** [07:13:36]: We are going to have partner keep agreements which Lee is putting in place various parties who will go out and find investors and introduce investors for us.

**Greg Wall** [07:13:45]: How capture or manage their an overall project management way because they're our client.

**Greg Wall** [07:13:57]: and who?

**Greg Wall** [07:13:58]: How and who?

**Greg Wall** [07:13:59]: sense?

**Greg Wall** [07:14:00]: Because I can tell you right now, Peter Bartlett or Bartlett has got a whole bunch of potential investors for XLHeal here Australia.

**Greg Wall** [07:14:09]: Yeah.

**Greg Wall** [07:14:10]: So as we sit here, what

**Ivan Fattorusso** [07:14:14]: And is he going to provide, what is he going to provide an Excel sheet of content?

**Greg Wall** [07:14:20]: What is he actually?

**Greg Wall** [07:14:21]: We haven't had the conversations.

**Greg Wall** [07:14:23]: It's like, I think it's probably I mean, I don't know, really don't know.

**Greg Wall** [07:14:27]: the... And let's just say that he gets material and he goes and talks to his investors and works out of course.

**Greg Wall** [07:14:36]: Let's just say that he does that without our involvement.

**Greg Wall** [07:14:38]: He then turns up to us and says, I've got six investors who How do we manage that, right?

**Greg Wall** [07:14:45]: Because they're his investors, he's going to be liaising with them.

**Greg Wall** [07:14:50]: He's going to be managing them.

**Greg Wall** [07:14:51]: We need all of their details in our system, but how do we do that?

**Greg Wall** [07:14:55]: I mean, you see where I'm going,

**Ivan Fattorusso** [07:14:57]: right?

**Ivan Fattorusso** [07:14:58]: That is going to happen week.

**Ivan Fattorusso** [07:15:00]: Yeah, I mean, I mean, it just comes down to really, he's going to have to provide at some point throughout the process.

**Ivan Fattorusso** [07:15:07]: He's going to have to provide that list investors, the contacts, at the very least, if not the communication, which I wouldn't expect

**Greg Wall** [07:15:16]: Right, but still he will likely be owner, I mean, being the realistic owner, not from a database perspective, but being the realistic owner of that relationship, he's manage it.

**Greg Wall** [07:15:28]: But we're still going to want to track where they're up to

**Ivan Fattorusso** [07:15:35]: just just, you know, periodic catch-ups with him, right?

**Greg Wall** [07:15:41]: It requires... Maybe.

**Greg Wall** [07:15:42]: But we need to think of the execution of that.

**Greg Wall** [07:15:45]: What does he... And I'm only saying this so you two can think this.

**Greg Wall** [07:15:50]: Yeah.

**Greg Wall** [07:15:50]: Does he produce... a small report or does he send to for Toby to upload.

**Greg Wall** [07:15:57]: Does he send it to ISIL for ISIL to upload?

**Ivan Fattorusso** [07:16:00]: Yeah.

**Ivan Fattorusso** [07:16:01]: How do we do this?

**Ivan Fattorusso** [07:16:03]: But they're just things we need a little templated report thing, right?

**Ivan Fattorusso** [07:16:08]: That everyone can fill in.

**Izel Sequeira** [07:16:10]: That can then... I think that's what we discussed earlier also, right?

**Izel Sequeira** [07:16:13]: If everybody could fill it and it would be easier for them

**Ivan Fattorusso** [07:16:18]: Right.

**Ivan Fattorusso** [07:16:18]: All right, guys, guys.

**Ivan Fattorusso** [07:16:22]: We do too.

**Ivan Fattorusso** [07:16:24]: But yeah, we can chat further tomorrow.

**Ivan Fattorusso** [07:16:25]: Thank you guys.

**Ivan Fattorusso** [07:16:26]: Thank you.

**Ivan Fattorusso** [07:16:27]: We'll see you.

**Ivan Fattorusso** [07:16:27]: Thank you.

**Ivan Fattorusso** [07:16:28]: Thank you.

**Ivan Fattorusso** [07:16:29]: Thanks guys.

**Ivan Fattorusso** [07:16:30]: Bye-bye.

---
*Backed up from MeetGeek on 2026-03-30 08:45*
