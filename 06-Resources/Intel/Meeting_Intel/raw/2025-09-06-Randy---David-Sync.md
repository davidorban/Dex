# Randy / David Sync

**Date:** 2025-09-06
**Duration:** Unknown
**Meeting ID:** 454dc287-de6b-4a2d-8c89-f4d50253442d

## Participants
- *Participants not listed*

### Summary

The meeting focused on enhancing task extraction from Meet Geek recordings using AI and workflow automation, addressing challenges in filtering relevant tasks into Asana. David was tasked with hiring Shorce to improve automation and refining AI prompts to exclude irrelevant details, while Randy would provide feedback on the extraction process. Discussions also covered the hiring of a project manager, emphasizing the need for strong project management skills and clear reporting structures. Communication preferences were highlighted, particularly Michael's preference for written communication, which contrasts with the team's verbal tendencies. Additionally, updates on strategic discussions with Hydro Host were shared, including leveraging connections for potential deals, and the formation of a new international organization aimed at improving trade among smaller countries was discussed, with a significant announcement expected soon. David also proposed a future session to explore Hydrohosts' strategic implications and shared insights on a data scraper he developed for market analysis.

## Full Transcript

**David Orban** [06:00:49]: I am great, about to leave for London tomorrow.

**David Orban** [06:00:55]: Yeah, I understand that.

**David Orban** [06:00:57]: Yeah, so last week, whatever happened, you only said, oh, it's my turn now, 10 minutes before the end of the call, which was unfair, so let's start the other way around and give you all the time you need, and then I will... update you.

**Randy Boyer** [06:01:24]: So I think a couple of things.

**Randy Boyer** [06:01:25]: I'm still struggling to figure out how to take Meet Geek recordings and then make sure that I only get the tasks that are relevant into Asana.

**Randy Boyer** [06:01:42]: Meet Geek is like a Yeah, I needs there needs to be an analysis, maybe it's chat GPT that needs to take it and then do something with it and then make the the filtration to.

**Randy Boyer** [06:01:56]: Tasks that really are meaningful I mean when I say meaningful I mean just because we say that I'm going to do something or or someone else is going to do something in the meeting doesn't equal it needs to be an asana.

**Randy Boyer** [06:02:13]: Yes, and I could say, oh, yeah, I got to remember to go call, you know, well, yeah, that'll come up, that will come up as a task and it'll get put into a sign, and I don't want that.

**David Orban** [06:02:26]: Yes, yes, so I think that is a wonderful example of an area where AIs need to improve in terms of applying common sense, and The question is whether we can edit the prompt that meet geek itself uses in which case we can expect the generated list inside meet geek to adapt to our needs or if we cannot

**David Orban** [06:03:05]: then we just need to implement a workflow that downloads the transcript feeds it to whatever model we want to use cloud or chat GPT using the prompt that we at any given time like and then feed the output task list.

**Randy Boyer** [06:03:32]: My guess is we're probably my guess is we're probably if it'll be easier for us to see the latter than the former just because I don't know it's going to be that easy to get access to the internal guts of meet geek to be able and and I and I prefer going that route in any case because it confirms

**David Orban** [06:03:53]: our ownership of the process rather than for each tool relying on their degree of openness right if a tool doesn't allow us to download the whatever we use it for, we shouldn't use the tool to start with.

**David Orban** [06:04:17]: And that is not the case with mid- geek.

**David Orban** [06:04:18]: We know that we can download the transcript.

**David Orban** [06:04:21]: So that's perfect.

**David Orban** [06:04:22]: And then whatever we export from the tool, we should be able to increase its value through AI and then integrate it in some other tool.

**David Orban** [06:04:34]: So this is simply the multi-step workflow that we can even define in a general enough manner that everyone can understand and then from time to time implement in the best way possible at a given time with the expectation that it can it can improve so two things in that there is a there is a guy I

**David Orban** [06:05:03]: told you that I want to hire, his name is Shorce, and he will meet Michael in London.

**David Orban** [06:05:11]: And so I told him to get very good in using the kind of workflow automation tools that will enable us to rapidly implement something like this and every other type of thing similar and so if we hire him we will be able to to do that right away if we don't then I will tell him well tell me what you

**David Orban** [06:05:46]: did and then I will do and and so that is that is going going to happen.

**David Orban** [06:05:56]: Now, regardless of the smoothness and the general nature of the automation, it will still depend on how good our prompt is, and we can start from something as simple as apply common sense, don't include personal remarks or very fine granularity tasks in the list, right?

**David Orban** [06:06:22]: And then we can refine that input.

**Randy Boyer** [06:06:27]: Yeah, there's one other input just in case you end um, instructing source or you do it yourself.

**Randy Boyer** [06:06:35]: And that is, sometimes it just puts in really high level tasks.

**Randy Boyer** [06:06:41]: Like we start off the conversation saying, well, this is a project about X. And, you know, we, we, you know, the deliverable will ultimately be And it's like it's like for this happens all the time when I'm doing delivery, what do you call it, discovery sessions where we talk, you know, we're

**Randy Boyer** [06:07:05]: digging into the company and the ultimate goal is we're going to have a slide deck and a financials.

**Randy Boyer** [06:07:12]: And we talk about that during the first discovery session.

**Randy Boyer** [06:07:15]: So inevitably in Meet Geek it says one of the tasks is deliver, you know, is those two things.

**Randy Boyer** [06:07:23]: That's like the end product of two months worth of work.

**Randy Boyer** [06:07:28]: I don't know that I need to be told that and you know, it's the middle level stuff.

**Randy Boyer** [06:07:37]: And it's stuff that comes into context.

**Randy Boyer** [06:07:40]: Like we'll be talking, one of the first things that we talk about is, identifying documentation that could be helpful in us understanding about the company.

**Randy Boyer** [06:07:50]: So we talk about business plans and old decks and whatever.

**Randy Boyer** [06:07:54]: And invariably the CEO says, oh yeah, there was this 39 slide deck that I did that really covers everything.

**Randy Boyer** [06:08:01]: I'll send it to you.

**Randy Boyer** [06:08:04]: That I want to cap that that I want to capture.

**Randy Boyer** [06:08:08]: I want to be able to have the AI say, you know, CEO.

**Randy Boyer** [06:08:14]: sending 39 slide deck or whatever, the task ends being, um, and, and, and, and, and so it's going to be a, I think, a process to prompt to, you know, I don't think it'll be perfect right off the bat, I think it'll take some iterations to get into a, into a zone where it's not getting too general,

**Randy Boyer** [06:08:38]: it's not doing personal stuff.

**Randy Boyer** [06:08:41]: And it's not it's not doing stupid well in some cases I don't mind a little bit of detail, I mean because the fact that someone's going to send somebody something and promise to send is a worthwhile thing to track and to and to put into the into Asana but but I mean and if I'm going to call them or

**Randy Boyer** [06:09:03]: whatever The other the other thing that trips me up is I record this in real time, you know, in person, not using the meet geek recording device, and it does a beautiful job recording.

**Randy Boyer** [06:09:17]: It transfers it directly into the platform, but it doesn't know who said what.

**David Orban** [06:09:26]: And, but it does say speaker zero, speaker one, speaker two, correct.

**David Orban** [06:09:32]: think so I believe so it does it does well yeah I think it I think it does do at least that yeah so that is another reason to apply this kind of process after exporting the transcript because then you can Midgix should to some degree be able to realize who are the people speaking.

**David Orban** [06:10:03]: Other, for example, does a pretty good job in that.

**David Orban** [06:10:08]: Because Medigik knows who are the participants by the calendar invite, and that it is just a question of realizing, oh, if this person says, Randy, thank you for your remarks, then evidently that not Randy speaking in the third person about himself.

**David Orban** [06:10:29]: but it is someone else, and so by logic it can identify the speakers, but evidently it doesn't do so, however, it can be part of our prompt.

**David Orban** [06:10:41]: That is why, rather than typically extracting the task list from the raw transcript, I first generate the structured transcript with universal with a universal prompt.

**David Orban** [06:11:02]: And then I generate the meeting minutes.

**David Orban** [06:11:05]: And then I took the two files, the structured transcript and the meeting minutes.

**David Orban** [06:11:11]: And I create the task list out of out of those.

**David Orban** [06:11:17]: And and identifying these little things, little big things that that you mentioned is crucial to make it so that others who are less patient and tolerant than you can use whatever we come up with.

**David Orban** [06:11:36]: Otherwise they would say no, this is this is still not working, come back next year.

**Randy Boyer** [06:11:44]: So yeah, so it's our to in the next relatively short period of time improve if we master pretty good translation of tasks into Asana.

**Randy Boyer** [06:12:02]: That will be big achievement for the organization.

**David Orban** [06:12:07]: Yep.

**David Orban** [06:12:08]: Yeah.

**David Orban** [06:12:09]: Yes, because it informs everything we do.

**David Orban** [06:12:16]: Everything has to do with something we want to accomplish by a given amount of time.

**David Orban** [06:12:23]: This will be the responsibility of a given person, so that is that is a project management component, yeah.

**Randy Boyer** [06:12:32]: There is a relatively good chance that we will be hiring a guy who's focused on project management.

**Randy Boyer** [06:12:41]: The debate is exactly what he will be doing, but there's quite a bit of momentum if we get this thing, if we get You know, we're getting good support, so if this continues, there's chance that Shores will have a companion to help, at least on the doing side of, you know, this person is going to be

**Randy Boyer** [06:13:11]: supportive of this whole process, because if we have a meeting, gets recorded and then we have relatively accurate prompts that for the most part get it right for Asana.

**Randy Boyer** [06:13:23]: This is this is gigantic, and that's really going to help this person.

**Randy Boyer** [06:13:27]: So he's that person's going to be really supportive of this whole endeavor.

**Randy Boyer** [06:13:32]: And we'll know, well, yeah, probably not so sure when gets back from from the UK what he's going to do, but I think it's highly likely he'll get hired.

**David Orban** [06:13:43]: And do you know if Shervin already knows who he wants to hire?

**Randy Boyer** [06:13:51]: On this particular, Well, he's had a meeting with this particular person.

**Randy Boyer** [06:13:59]: Um, if you think, if you think it's going to be this person or Shores, I don't know that that's the right.

**David Orban** [06:14:07]: No, no, no, no, no, I know, I know that Shores, uh, when I brought him up, Michael said, well, there is no budget for him and, and that's fair.

**David Orban** [06:14:18]: Well, there wasn't a budget for me either.

**David Orban** [06:14:21]: So just as the budget for me was created out of thin air.

**David Orban** [06:14:27]: It is just a question of how important we believe that person can be and how much value they can bring rapidly.

**David Orban** [06:14:36]: So when you were saying that there was this new hire that was being considered, if the person is not yet identified and the job offer to them is not imminent.

**David Orban** [06:14:54]: Then I was wondering whether we could.

**David Orban** [06:14:58]: So let me take a step back.

**David Orban** [06:15:02]: Is this new person going to be reporting to you?

**Randy Boyer** [06:15:06]: It's not clear.

**Randy Boyer** [06:15:11]: me tell you the genesis of this person's involvement in the hiring process.

**Randy Boyer** [06:15:18]: Two years ago or whatever, Amy and I were looking at a particular piece of software.

**Randy Boyer** [06:15:25]: think it was a paint that was some kind of a payment system for internal use, we're using zero, so if you have an internal, I think you probably are already using it, well, there was a there was product here.

**Randy Boyer** [06:15:41]: That was that was coming out of the UAE.

**Randy Boyer** [06:15:43]: I can't remember what his name.

**Randy Boyer** [06:15:44]: Something passed was the name of I can't remember precisely.

**Randy Boyer** [06:15:49]: But anyway, there was a salesperson and a relationship manager with that company that was working with Amy and and also had some some access to Michael.

**Randy Boyer** [06:16:05]: This is when we were like, you know, five people.

**Randy Boyer** [06:16:09]: And, you know, we just, you know, he showed great patience, he was really good, he's one of these few salespeople that could talk to you weekly, you don't feel like he was pushing you, or, you know, he wasn't being pest.

**Randy Boyer** [06:16:26]: That's really hard because most people either don't, you know, call you and then never call you back, or they're pests and call you every day, and, you know, they're just doing whatever their sales force tells them to do.

**Randy Boyer** [06:16:40]: which again that doesn't work either so so this guy was really sophisticated in the way he communicated with people and then the product not to his but he wasn't part of the leadership team of the product he was just working with the team anyway it failed so he went on to work with another company

**Randy Boyer** [06:16:59]: that was doing application development out of India so he was he's an Indian guy but he's I've been living here for.

**Randy Boyer** [06:17:12]: don't know, most of his life in Abu Dhabi, and his English is really good.

**Randy Boyer** [06:17:19]: There's a lot of English people that speak, a lot of Indian people that speak English because they're in India, and they have such a strong Indian accent, it's just really difficult.

**Randy Boyer** [06:17:29]: See, this is the guy who lives, who's spent his entire life the UAE and his English quite good.

**Randy Boyer** [06:17:36]: So, so, So he then came back to us and had some interface with Amy, Michael and I, when he was in that role a year ago.

**Randy Boyer** [06:17:47]: we said many meetings with this company because they were telling, you know, they were making some traction with some big companies working with some key players here, and this is long before that you were on the scene.

**Randy Boyer** [06:18:05]: And we were had, I don't know, three, four, five meetings with them and, and then I attended like a day-long conference and, and anyway, it ended up that we decided that we weren't going to do a partnership.

**Randy Boyer** [06:18:21]: So we stopped talking to the company.

**Randy Boyer** [06:18:25]: But this guy was part of that team and was part of all this, and he did a, you know, good job being an interface.

**Randy Boyer** [06:18:34]: And then, I don't know, a month ago, two months ago, Michael, I don't know how, this guy pops and talking to Michael said, hey, I'm around, if you're around, let's have dinner or whatever.

**Randy Boyer** [06:18:50]: So they had dinner or whatever, and then he and Mike, he and Amy and he, Michael and Amy and this guy had dinner, you know, a month ago or so.

**Randy Boyer** [06:19:01]: And he said, yeah, yeah, I'm, you know, freelancing, whatever, and looking for in the next thing.

**Randy Boyer** [06:19:06]: And they said, oh, well, we're hiring a whole bunch of people.

**Randy Boyer** [06:19:12]: I used to talk to Randy, because he needs project management, and you got the skill set.

**Randy Boyer** [06:19:16]: so I then met with him last week, and I had a big conversation about this guy with Sherwin.

**Randy Boyer** [06:19:25]: Because in the context, we're talking to a number of people.

**Randy Boyer** [06:19:29]: There's a woman who from Slovenia who we're talking to there's a guy from Russia that we're talking to analysts.

**Randy Boyer** [06:19:41]: In addition to all of this, Sherwin's talking to a number of players that he knows from past jobs in more middle level positions within the finance or the finance team within investment banking.

**Randy Boyer** [06:19:53]: So Sherwin's basically talking to about six to ten people.

**Randy Boyer** [06:19:59]: And in that context, he's looking for people that have specific skills, but also have some generalizable ability to be slotted in different divisions.

**Randy Boyer** [06:20:11]: And project management is one of those things where every division needs good project managers people that are attentive to detail can track tasks and have good communication skills.

**Randy Boyer** [06:20:22]: And this guy needs all of those things.

**Randy Boyer** [06:20:25]: And so, so I was, when Amy and Michael said, go talk to Randy, I was thinking, I was going to get a project manager for my things.

**Randy Boyer** [06:20:36]: So then I talked to Sherwin, he goes, oh, wow, this is great, we've been like, bye, now we can do, he can do this, he can do that, he can do that, fantastic, I want to see So they yesterday.

**Randy Boyer** [06:20:50]: And I'm and he's a he's very personable, very good person, so I'm a, and Sherman's quite emotionally high emotional intelligence, so I think that I will hit it off.

**Randy Boyer** [06:20:59]: And so we have this person that has a good skill set that can be slotted almost anywhere.

**Randy Boyer** [06:21:07]: So when you ask me, well, what, know, who's got him and what his role I don't know, I only know that I think there's a good chance he's going to get hired.

**David Orban** [06:21:17]: Okay, that's all I know.

**David Orban** [06:21:20]: Leaving aside whether Shores could do or could have done what this person is going to be doing,

**David Orban** [06:21:32]: will definitely be a bit more vocal about in certain roles reversing depressing trend that Michael made explicit other day.

**David Orban** [06:21:50]: when Chigdom was being introduced to everyone, being almost proud of how technically, technologically unsophisticated our team is.

**David Orban** [06:22:05]: So everything else being the same, you know, investment banking experience or whatever other advisory experience or wealth management experience, My recommendation will be to try and find people who are also technically or technologically savvy.

**David Orban** [06:22:28]: I don't see that as as a detriment to their employability by by our team.

**David Orban** [06:22:35]: And I will go even further.

**David Orban** [06:22:40]: We should.

**David Orban** [06:22:43]: At least with a couple of questions during the time that we have available to evaluate ask them what they think about AI.

**David Orban** [06:22:54]: And if they are rabidly against AI, if they say AI is bullshit and then we should do, we should have nothing to do with it.

**David Orban** [06:23:05]: I would endeavor that that kind of a rat flag against hiring Sure.

**David Orban** [06:23:11]: So this this definitely will be something that I will share with with Michael and Shervin and then they will take it under advisement in in one way or another.

**David Orban** [06:23:26]: Now, yes, back to the point that you were making with or without shorts, we will be able to help this person, tell me his name again.

**David Orban** [06:23:40]: It's Nidian, Nidian.

**Randy Boyer** [06:23:44]: Nidian.

**David Orban** [06:23:46]: Nidian.

**Multiple speakers** [06:23:48]: So we will be able to help Nidian to um um um increase his efficiency and throughput as long embraces the workflows that we will, we will, we will suggest that he's very open to what we're knowing, you know, having spent, I don't know, and I've spent in total probably 20, hours with And I'm a just

**Randy Boyer** [06:24:37]: my feeling is he's not going to be an anti AI user is going to be a pro AI user pro AI user there are other people that I know that that that that in our team thank goodness they're no longer with our team but they would have been just horrendously difficult to get to use okay Talking about AI and

**David Orban** [06:25:01]: our plans, after sending it to him at the beginning of August, Michael found the time to comment on my AI first strategy document and sent a very long and thoughtful reply.

**David Orban** [06:25:20]: he didn't copy And I appreciated his insight.

**David Orban** [06:25:36]: Some of it is perfectly fine.

**David Orban** [06:25:37]: You why promise that, or why even mention the ludicrous 100x increase, I believe is possible if the other side is just too incredulous to believe it.

**David Orban** [06:25:56]: 10x is already fine.

**David Orban** [06:25:58]: or where he says that we need to empower people and that rather than talking about AI transformation we can say that it is AI power, they are AI founded because Gough and Ali 1 are being built.

**David Orban** [06:26:28]: So they can be built with AI right from the stock, all very remarks.

**David Orban** [06:26:35]: Then he made one that I absolutely didn't reply to.

**David Orban** [06:26:41]: I kind of ignored, because I disagree and it didn't matter voicing my disagreement, where he says, well, and the AI can only help with digital processes, it cannot help with physical workflows, looking at the construction site and how it is going, overseeing the building of a road.

**David Orban** [06:27:08]: So those remain.

**Multiple speakers** [06:27:11]: That's not true, though, that's not true.

**Randy Boyer** [06:27:12]: And that is not true.

**Randy Boyer** [06:27:14]: Yeah, I mean, there's a real sophisticated visual capture to and analyze where things are at or whatnot.

**Randy Boyer** [06:27:22]: It capture, you know, the state the road and construction.

**David Orban** [06:27:28]: or driving driving the the excavator.

**David Orban** [06:27:32]: Hey, buddy, self- driving is a thing.

**David Orban** [06:27:35]: I know he doesn't, he very much dislikes Elon Musk, the Chinese are getting into self-driving big time.

**David Orban** [06:27:44]: And so the efficiency of even building processes where an excavator can be operated, three times or, or five times more.

**David Orban** [06:27:58]: than before because it never needs to stop.

**David Orban** [06:28:04]: Some of these are not even battery operated, but there's a thick cable going to And so it's not even, it doesn't even need to stop for recharging.

**David Orban** [06:28:16]: And so if you want to go fast, you can go fast in a construction.

**David Orban** [06:28:21]: That is why I asked the question to the Dutch guy, you were there, right, the architect.

**David Orban** [06:28:27]: When I was in at the architect meeting.

**Randy Boyer** [06:28:30]: Oh, you were not.

**Randy Boyer** [06:28:31]: I had an interview.

**Randy Boyer** [06:28:34]: I was in an interview.

**David Orban** [06:28:36]: And it was not earth shaking as a meeting goes, but it was decent.

**David Orban** [06:28:42]: And I asked him about the speed with which the Chinese are building.

**David Orban** [06:28:49]: And he was on the fence about it, whether it is good or bad.

**David Orban** [06:28:54]: But he did remark that things in the UAE go faster than he expected, which is And Michael also has the reading my reply, what AI am I using are actually just for my interest, because I am calibrating my ability to work out which AI is doing what and which I prefer my own Is your reply fixer

**David Orban** [06:29:25]: generated or something so of course I confirm that it done together with the AI and and giving him the details of how and so so that's that's great because you know he could have made a 180 degree turn after reading the document rather than contributing it to it constructively, and that would have

**David Orban** [06:29:56]: been said.

**Randy Boyer** [06:29:57]: Oh, yes, one other thing to, to, I might have told you this before, it bears repeating.

**Randy Boyer** [06:30:04]: See, even with all of the talk about, making sure that you talk to people and you and he prefers, face to face as opposed to, you know, remote, all this other Is the way that he, he gets information, believe it or is you writing something and him reading He doesn't, he's, as verbal as he is,

**Randy Boyer** [06:30:38]: prefers.

**Randy Boyer** [06:30:40]: to read it.

**Randy Boyer** [06:30:40]: He is a book reader from as a child, and he absorbs by reading.

**Randy Boyer** [06:30:48]: So you writing a thoughtful plan that he then could read is how he prefers to get his information and to discuss really difficult things.

**Randy Boyer** [06:31:00]: And everyone else doesn't get that.

**Randy Boyer** [06:31:02]: I mean, if you talk to anybody in the organization, they say, oh, yeah, I'll just have a meeting with Michael.

**Randy Boyer** [06:31:06]: We'll just chat about it or whatever.

**Randy Boyer** [06:31:08]: No, if you really, really want to communicate with them, you write Yeah, and did you have the chance of sharing this with others, and they didn't follow your advice, or you didn't I have told, I tell people as I meet and they're communicating with Michael, I say, and by the, oh, by the way, if you

**Randy Boyer** [06:31:32]: really want to communicate with them, do it in writing.

**Randy Boyer** [06:31:34]: But it falls by the wayside because he's so approachable, personable, and people don't like to write, it's too hard.

**Randy Boyer** [06:31:43]: They want to talk, they just, everybody wants to talk, even Michael, he's a hypocrite, he wants you to write to but he will how he communicates to you, so voice record something and say, and then you have to stop spirit and then take notes and whatever.

**Randy Boyer** [06:32:06]: So he he is a hypocrite.

**David Orban** [06:32:11]: He wants you write, he doesn't want to Here is a good If he leaves you five or ten minute WhatsApp voice recording, transcribe it with, with mid-geek.

**David Orban** [06:32:26]: Sure.

**Multiple speakers** [06:32:27]: It takes you two minutes and then you can read the transcription or you can go Okay, analyze this for me, tell chat GPT to analyze it for you and Yeah, even with all of that, whatever the transcription, well, I think I will have to put it into a better transcription engine because what it he's got

**Randy Boyer** [06:32:53]: an accent, number one.

**Randy Boyer** [06:32:55]: And when he talks about names, a lot, a lot of this, a lot of the messages relate to, he talked to so and so and that, and the other thing in this company, whatever, and they always get the names wrong.

**Randy Boyer** [06:33:05]: Yeah.

**Randy Boyer** [06:33:07]: So, no clue what he's, what they're talking about.

**Multiple speakers** [06:33:10]: We have a candidate for that as well, and you can test it already if you want.

**David Orban** [06:33:15]: It's called Gladia, G-L-A-D-I-A, Gladia.

**David Orban** [06:33:22]: G-L-A-A.

**David Orban** [06:33:24]: DIA, gladia.

**Multiple speakers** [06:33:29]: Okay, gladia.

**David Orban** [06:33:30]: And what does gladia So gladia is originally for developers, but they have a playground.

**David Orban** [06:33:44]: So if you register and you don't use it as a developer, but just upload

**David Orban** [06:33:54]: it will be perfectly happy to and it is paid per use but an hour of transcription costs like I don't know 50 cents and and it doesn't charge by the hour it charges by the second maybe or by the minute I don't know so so it's extremely you can prepay you can like do a prepay yeah you you can you can

**David Orban** [06:34:21]: pay a twenty dollars credit yeah yeah Go down the credit.

**David Orban** [06:34:26]: Okay.

**David Orban** [06:34:26]: Okay.

**David Orban** [06:34:27]: So you can already test but what is beautiful about it is it can go extremely sophisticated in terms of personalized vocabulary it learns the voice prints of people so that it can associate names to And for me, mean, there are But for me, it is really one of the best today.

**David Orban** [06:34:59]: Okay, great.

**Randy Boyer** [06:35:02]: I will play it.

**Randy Boyer** [06:35:05]: Yes, And then the last thing I wanted to mention you, and we don't have to get into it deeply because Sherwin and Michael will talk to you about in And that is, we've come full circle I don't know, two months ago, hella, talk to you about hydro host and said, oh, we need to talk to somebody to do

**Randy Boyer** [06:35:31]: due diligence.

**Randy Boyer** [06:35:33]: And we had a series of talks with remotely.

**Randy Boyer** [06:35:39]: Then they came about a week ago or last week, at the beginning week, not last week, I mean, the week prior to the week we just had, they were here on Monday, Tuesday, Wednesday, and we had several meetings with And got deeply into everything, so we have much better idea of what we want to do.

**Randy Boyer** [06:36:00]: And there's two, there's two areas, there's three areas of interest.

**Randy Boyer** [06:36:06]: First area of interest is strategic.

**Randy Boyer** [06:36:09]: Because to hear them talk, particularly the CEO, he's on speed dial with Jensen.

**Randy Boyer** [06:36:20]: he was talking to Jensen like every time we having a meeting, there would be a call and he go, oh, I have to take this, and it's Jensen Wong, you know.

**Randy Boyer** [06:36:30]: It just, he clearly someone who's talking daily.

**Randy Boyer** [06:36:38]: So there's a strategic value to someone who's talking to the CEO of Keep Second thing um, Jensen Wong has basically told the CEO, Erwin Aaron the CEO of hydro host is he's Aaron strategically he wants to try to close as many deals with large telecoms and countries as much as possible they just did a

**Randy Boyer** [06:37:12]: big big deal with it Verizon and they did a sovereign deal with El Salvador and they're and Aaron spearheading the conversations and they're talking to some other big telecoms and other big mean not big sovereigns but sovereigns Like Paraguay and it was two or three others that it could be Malaysia

**Randy Boyer** [06:37:36]: that they're talking to.

**Randy Boyer** [06:37:36]: Anyway, there was few.

**Randy Boyer** [06:37:37]: And he said, that's I'm helping Jensen do.

**Randy Boyer** [06:37:43]: If you know any telecoms or if you have conversations with Sovereigns, this is of highest priority to that perked my ears because I'm, I have a close relationship with with the chief of staff of the prime minister of Jamaica who just won re- election two days ago and he wants to when after they pick

**Randy Boyer** [06:38:10]: the cabinet which is happening in the next two or three weeks us to meet with him advisors and cabinet people to talk about a whole array discussion including AI including digital currency including, um, uh, well, I I see a trip to Jamaica in my future.

**Randy Boyer** [06:38:40]: Including, including, um, sovereign wealth advising because Jamaica just discovered oil and gas in, uh, a, in a volume that's about the same as Guyana, which is just a little bit smaller than Venezuela.

**Randy Boyer** [06:38:57]: And easier to get to it's in it's in shallower water and easier to and closer to the island than Guyana's.

**Randy Boyer** [06:39:04]: So there's all this stuff so so They're clearly a target for doing a sovereign deal for Nvidia, but we're also and the prime minister is the lead of Karakon.

**Randy Boyer** [06:39:19]: There's a rotation among all the Caribbean countries of who chairs the Caribbean community like the European community the Caribbean community is 23 countries and the Jamaican prime minister is the leader of the 23 countries so if there's I mean he's got a lot of leverage right now to do a whole

**Randy Boyer** [06:39:40]: bunch of stuff that he wants to do pretty quickly which is why he wants to talk to and he believes that the UAE the UAE if you saw some of my posts the UAE announced to the world that they're creating a new Group of countries.

**Randy Boyer** [06:39:58]: They're, they're basically fed up with the US, China, India, Brazil.

**Randy Boyer** [06:40:03]: You know, these big countries are trying force way with little countries.

**Randy Boyer** [06:40:10]: So they're creating a new organization of little countries.

**Randy Boyer** [06:40:13]: And they've got like 10, it's, it's start, the core is Singapore, UAE, New Zealand, and Norway.

**Randy Boyer** [06:40:26]: And they're they're they're wanting to in the next few months.

**Randy Boyer** [06:40:35]: They're wanting to announce 20, 30, 40, 50 countries, smaller that are creating this and the purpose of the of the organization is to streamline to streamline trade, currency, finance, all the things that are broken with these big countries that they're trying to use their power to manipulate the

**Randy Boyer** [06:41:05]: small countries.

**Randy Boyer** [06:41:06]: For instance, I don't know if you knew this, but Ghana and Jamaica have been thrashed by International Monetary Fund and the World because they've taken steps in their country to to protect and stabilize their currency.

**Randy Boyer** [06:41:26]: That's totally against the IMF.

**Randy Boyer** [06:41:29]: They want everything to be totally, you don't touch it, let the world do what it does, let your currency fly all over the place, because if you touch it, then that's So Ghana said we know what we need to do.

**Randy Boyer** [06:41:45]: And they, for the last year, have been gentle things to keep their currency protected so that inflation's been and the currency fluctuations very modest.

**Randy Boyer** [06:41:56]: been under control so make is doing the same thing and they're getting huge flack from the big countries so so this is it there's a new there's a new big uh development among all of the small countries that saying listen We don't want to screw up world.

**Randy Boyer** [06:42:23]: We liked having free trade.

**Randy Boyer** [06:42:25]: We like transparent trade.

**Randy Boyer** [06:42:27]: We don't like tariffs.

**Randy Boyer** [06:42:29]: We, know, we quick payment.

**Randy Boyer** [06:42:34]: We the future of digital in terms of speeding things up, making it more transparent, protecting against corruption, being able, you know, all this, we like all those things.

**Randy Boyer** [06:42:46]: So we and we see the big countries screwing up.

**Randy Boyer** [06:42:50]: So we want to get together, have a new organization, And it's happening, they're going to have a big announcement in October or November, and then they're having a big conference next July, and I don't know that they've come up with an official but, you know, it'll, it's going to be mostly small and

**Randy Boyer** [06:43:10]: medium-sized countries, I've already told you some of the ones I've already joined, and it's from all over world, but the fact that Singapore, New and Norway are and UAE are the core starting members is amazing and strong and Jamaica could easily be there and they could easily bring the whole

**Randy Boyer** [06:43:36]: Caribbean with them the Prime Minister likes what he hears Okay, so So yeah, so Jamaica is just an example of of a sovereign.

**Randy Boyer** [06:43:55]: So so so there's there's the there's the there's the strategic relationship with Nvidia, which seems to be an important company the world.

**Randy Boyer** [06:44:05]: I'm not saying they're the only players, I'm just saying that they're important, particularly Secondly, Nvidia's trying to break the stranglehold of Amazon, Microsoft, and this old model of, you know, we, we, Amazon, control the stack in data You do business with us.

**Randy Boyer** [06:44:30]: We make all the money, dole out little bits to everybody we, and we are not going to tell you how much make.

**Randy Boyer** [06:44:36]: And then, Nvidia basically.

**Randy Boyer** [06:44:40]: with its newest chip, basically disintermediating most And so, and so, you know, there's a competition between the big techs and some of the new players about how all of this should happen, you what should be the future of data centers.

**Randy Boyer** [06:45:01]: And so, so we're trying to We're trying to figure out strategically whether relationship We're trying to figure out whether what they have makes, you know, we need to do due diligence on who they what their technology really does, just so that we really truly know who And then there's the financial

**Randy Boyer** [06:45:32]: piece, what they've done is cleverly with the help of NVIDIA created some financial structures whereby It's kind like car companies setting up a finance Yeah, absolutely.

**Randy Boyer** [06:45:47]: Yeah, so they put together these structures that they are offering to any investor and basically saying, invest, know, 10, 50, 100 million, whatever you can, whatever want to, million, whatever.

**Randy Boyer** [06:46:02]: You come in as a private investor, we'll guarantee you a 10% return or something that's good.

**Randy Boyer** [06:46:08]: And we'll take this money and we'll use it to build data centers and to buy NVIDIA chips to power these data And just like car companies selling cars to individuals.

**Randy Boyer** [06:46:23]: So we're looking at also potentially making some money on the finance And remember, the UAE wants to be a player in terms of financing data centers world.

**Randy Boyer** [06:46:37]: They're already doing it in Malaysia and Ghana.

**Randy Boyer** [06:46:40]: They talked about a $1.5 trillion deal with the US.

**Randy Boyer** [06:46:44]: Incidentally, from what I understand, they said it to a peace trump, and they have no intention of actually doing it.

**Randy Boyer** [06:46:55]: Be that as it may, they're still really doing it in other countries, and this and the other countries are small countries.

**Randy Boyer** [06:47:03]: Ghana, Malaysia.

**Randy Boyer** [06:47:04]: They're going around the world helping to set up regional AI So all of this kind circles around a number of strategic initiatives are compatible with us and what we know and our experience and what the UAE wants so it's bundled together.

**Randy Boyer** [06:47:27]: So the basic idea is, and Sherwin and Michael won't into as much of the strategy as I just did with They're going say we need to do due diligence technically and we need do due diligence financially to figure out these guys real and can you help us pick a third party that we also have a relationship

**Randy Boyer** [06:47:48]: guy called Marvin Aval is I don't know if you've ever met or not who's a very technical technical guy and was a technical advisor to what's her name There's a woman investor, he's been investing for 50 years in Silicon Valley.

**Randy Boyer** [06:48:09]: you know, ultra high net And she's very famous, and I can't remember her name.

**Randy Boyer** [06:48:14]: Esther, Esther Dyson.

**Randy Boyer** [06:48:15]: Esther He's, he's, um, he's Esther Dyson's tech Oh, nice, very And so, and so, so, So what they're going to ask you is they're going to say, David, can you work with Marvin and help us find someone who can do the tech due diligence on hydro notes and to hear Michael.

**Randy Boyer** [06:48:42]: You know we'd be comfortable spending.

**Randy Boyer** [06:48:45]: don't know 20 25 30 40 thousand dollars or whatever some amount of money to figure this out and then Sherwin Let's get them, let's get them to pay because they're going to have to prove themselves to other people, so let's have them, I don't want to get into that conversation, but, but I don't care

**Randy Boyer** [06:49:04]: who pays the consultant, but they need to get paid and we need to do it.

**Randy Boyer** [06:49:08]: This is really front and center, and we need to make pretty much in the next month or so, so we need to just And you will be hit with this, and you know, when you get London.

**David Orban** [06:49:22]: That's that's wonderful and I'm looking forward to it.

**David Orban** [06:49:29]: And

**David Orban** [06:49:36]: we don't have the time to do it now, but maybe you and I should have a session dedicated to talking about hydrohosts, because there things that it appears no one is considering.

**David Orban** [06:49:51]: I'm pretty sure Hydrohosts are considering, but very, very interesting, both in terms of what is the Nvidia strategy and what they are protecting from, not only the Chinese, but they about to be disrupted in their stronghold, which is through a different means.

**Randy Boyer** [06:50:15]: Oh, and they're expecting to be acquired by All right.

**David Orban** [06:50:22]: good.

**David Orban** [06:50:23]: And then why does it make sense to go all over the world to quotation marks small countries.

**David Orban** [06:50:30]: And it is because of the energy availability, which may not be there in the US anymore.

**David Orban** [06:50:39]: Every energy source has been tapped, including generators, the turbines, You cannot buy a turbine be deployed for the next five, 10 The the Siemens and GE supply chain is completely So very, very Okay, that's That great.

**David Orban** [06:51:11]: A little, I don't know if you saw it, probably you didn't because you didn't have But I just want to brag a bit because I had a lot of fun.

**David Orban** [06:51:22]: I had a lot of fun writing this.

**Randy Boyer** [06:51:29]: Oh, yeah, yeah, yeah.

**Randy Boyer** [06:51:31]: I don't know exactly what I'm looking at, but it looked cool.

**Multiple speakers** [06:51:34]: Yes, exactly.

**David Orban** [06:51:36]: That's exactly point.

**David Orban** [06:51:39]: Luke came to me and I was trying to download the data from the open data section of the ESCA website about the licensed companies, and couldn't hire someone to do it manually, but I would need to find them and pay them and it would take time, Couldn't AI do this, and after the data is downloaded, I

**David Orban** [06:52:06]: would like a matrix representing the So that we that, yes, indeed, our license is unique because we say that we are the only ones, but this can And so it took me a couple of and I not only wrote the scraper that downloaded the data that created the spreadsheet, which I also gave to Luke because he

**David Orban** [06:52:42]: wanted to play with the data himself.

**David Orban** [06:52:45]: Then I created pivot table that says, okay, what are the most popular licenses?

**David Orban** [06:52:52]: And what are the companies with the most number of licenses?

**David Orban** [06:52:56]: And then there are others like what are the markets, Dubai versus Abu Dhabi and so on and forth.

**David Orban** [06:53:05]: But I did this, which represents five dimensions in, in, what's the problem?

**David Orban** [06:53:15]: Okay.

**David Orban** [06:53:16]: It doesn't want to play like this.

**David Orban** [06:53:18]: I will play like because play before.

**David Orban** [06:53:24]: Yeah.

**David Orban** [06:53:25]: So this represents five dimensions license type, sector analysis, geographic analysis, complexity, and each time you change the business sector, license category, city location, license and spheres you are looking at.

**David Orban** [06:53:51]: And then you hover on a sphere and it updates which company that so I Oh, you see.

**Randy Boyer** [06:54:01]: okay.

**Randy Boyer** [06:54:01]: So basically you have very complicated against six or whatever, whatever is, seven categories, views that you can just click on and you see that view, click on it, see view.

**Multiple speakers** [06:54:16]: And each time there is something to be noted.

**David Orban** [06:54:20]: So for example, if you look here, you see that there are outliers.

**David Orban** [06:54:26]: And so you can ask yourself, okay, Who is that outlier and So it turns out that Russell Haima an emerging market that started issuing licenses just in the past few And at a glance, you can start understanding the dynamics of the rather than staring at a website that presents you one by one the

**David Orban** [06:54:56]: licensed companies and you understand nothing.

**Randy Boyer** [06:54:59]: Right, allows you understand the interrelationship.

**Multiple speakers** [06:55:06]: Yeah, yeah.

**Randy Boyer** [06:55:08]: And so, so are we, are we unique?

**David Orban** [06:55:12]: Well, I am still not exactly sure what our licenses are going to be, and on top of that, we will have, we will be by definition unique, because we have at least one or two licenses that are issued just for us and no one else has right?

**David Orban** [06:55:33]: That's true.

**David Orban** [06:55:34]: So we will be unique, right?

**David Orban** [06:55:36]: Okay.

**David Orban** [06:55:37]: Yeah, yeah.

**David Orban** [06:55:38]: But I will ask Luke what his own conclusions are then we can have little, you know, success story.

**David Orban** [06:55:46]: Oh, another little success story I showed it Alicia And then she didn't after her bringing it up a second time, I explained it and this time she did it, and apparently it works for her, as I expected it would, and he's happy because I told her, install chat GPT on your and take a of the handwritten

**David Orban** [06:56:22]: notes and charts that you like to draw in your notebook and tell chat GPT to interpret and describe it and that will allow you to easily share your thinking with the rest of And and she she's very happy about how the process works because it allows her you know, using and and charting and graphing

**David Orban** [06:56:55]: and brainstorming, but then creates rapidly something that she can communicate So I want to start taking all of these little wins and create internal case histories so that build the basis people being happy about the approach and then others hopefully embracing Cool.

**Multiple speakers** [06:57:27]: Sounds great.

**David Orban** [06:57:28]: All right.

**Randy Boyer** [06:57:29]: Thank you very We have to, yeah, yeah.

**Randy Boyer** [06:57:32]: Great.

**Randy Boyer** [06:57:32]: I have go too.

**David Orban** [06:57:33]: Yeah.

**David Orban** [06:57:36]: And we don't have typically things on in the at the start of the week, so our Thursday, I will, you know, set it up again, and I will follow your request and set it up in the afternoon rather than the Yeah, everybody's, everybody's packing meetings between 10 Everybody, I mean, I literally can't go

**Multiple speakers** [06:58:05]: to lunch anymore, because I, every day I start meetings at 10 and I finish at two, but it's Okay, so I will do it at three And and then next week we should also finalize one or more slots when we sit down when I'm Yeah, absolutely.

**Randy Boyer** [06:58:35]: Thank you.

**Randy Boyer** [06:58:36]: Thanks,

---
*Backed up from MeetGeek on 2026-03-30 09:01*
