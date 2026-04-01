# AI Knowledge Hour #3 —  Introduction to Claude (Online)

**Date:** 2026-02-19
**Duration:** Unknown
**Meeting ID:** 5f7bb8fb-306a-43e3-b7d0-e2938b84c3fd

## Participants
- *Participants not listed*

### Summary

The workshop introduced Claude and its co‑work agent, demonstrating end‑to‑end capabilities including file analysis, automated reports, branded document generation, and cross‑app integrations (Asana, Drive, Slack). David and Axel showcased reusable 'skills' and live examples comparing browser execution to co‑work agents for deal research and task automation. The session included practical productivity examples—email to Asana conversion and automated weekly reports—plus discussion on governance, licensing adoption, and human oversight. Participants asked integration and template questions; several skills and templates were shared for team reuse.

## Full Transcript

**Shaheen AlShanableh** [10:58:25]: How are you, and Kit?

**Shaheen AlShanableh** [10:58:32]: Hello.

**Shaheen AlShanableh** [10:58:32]: Yeah, I'm available.

**Shaheen AlShanableh** [10:58:33]: I'm here.

**Shaheen AlShanableh** [10:58:33]: I'm waiting for David.

**Shaheen AlShanableh** [10:58:35]: I'm the team

**Ankit Choudhary** [10:58:36]: members.

**Axel Zanner-Entwistle** [11:00:56]: Hi, David.

**David Orban** [11:00:58]: All right.

**David Orban** [11:00:59]: Hello, everyone.

**David Orban** [11:01:00]: Thank you for joining.

**David Orban** [11:01:01]: And the settings of this invitation.

**David Orban** [11:01:09]: .

**David Orban** [11:01:09]: So .

**David Orban** [11:01:11]: .

**David Orban** [11:01:11]: .

**David Orban** [11:01:11]: .

**David Orban** [11:01:11]: .

**David Orban** [11:01:11]: .

**David Orban** [11:01:12]: .

**David Orban** [11:01:12]: .

**David Orban** [11:01:12]: .

**David Orban** [11:01:13]: .

**David Orban** [11:01:13]: .

**David Orban** [11:01:13]: .

**David Orban** [11:01:13]: .

**David Orban** [11:01:13]: .

**David Orban** [11:01:13]: .

**David Orban** [11:01:13]: .

**David Orban** [11:01:13]: .

**David Orban** [11:01:13]: .

**David Orban** [11:01:13]: .

**David Orban** [11:01:13]: .

**David Orban** [11:01:13]: .

**David Orban** [11:01:13]: .

**David Orban** [11:01:13]: .

**David Orban** [11:01:14]: .

**David Orban** [11:01:14]: .

**David Orban** [11:01:14]: .

**David Orban** [11:01:14]: .

**David Orban** [11:01:14]: .

**David Orban** [11:01:15]: .

**David Orban** [11:01:15]: .

**David Orban** [11:01:15]: .

**David Orban** [11:01:15]: .

**David Orban** [11:01:15]: .

**David Orban** [11:01:15]: .

**David Orban** [11:01:15]: .

**David Orban** [11:01:15]: .

**David Orban** [11:01:15]: .

**David Orban** [11:01:15]: .

**David Orban** [11:01:15]: .

**David Orban** [11:01:15]: .

**David Orban** [11:01:15]: .

**David Orban** [11:01:15]: .

**David Orban** [11:01:16]: .

**David Orban** [11:01:16]: .

**David Orban** [11:01:16]: .

**David Orban** [11:01:16]: .

**David Orban** [11:01:16]: .

**David Orban** [11:01:17]: .

**David Orban** [11:01:17]: .

**David Orban** [11:01:17]: .

**David Orban** [11:01:17]: .

**David Orban** [11:01:17]: .

**David Orban** [11:01:17]: .

**David Orban** [11:01:17]: .

**David Orban** [11:01:17]: .

**David Orban** [11:01:17]: .

**David Orban** [11:01:17]: I don't know if it started when the first of you joined, or, or when I joined as the organizer.

**David Orban** [11:01:22]: So, nodding probably, he means that it started when he joined first.

**David Orban** [11:01:33]: And if we wanted to have high production quality, then we would chop off that initial part.

**David Orban** [11:01:43]: So we'll see if that is going to be possible.

**David Orban** [11:01:46]: I had a lot of good

**Shaheen AlShanableh** [11:01:47]: discussions with Ankit.

**Shaheen AlShanableh** [11:01:49]: That should be included.

**Shaheen AlShanableh** [11:01:51]: All right, all right.

**David Orban** [11:01:53]: So, Let me share the screen and then start so that we have time for conversations and discussions.

**David Orban** [11:02:06]: And this is an introductory course, about class.

**David Orban** [11:02:15]: Now, some of you are already using the, I am.

**David Orban** [11:02:23]: I hope it is not going to be too boring for you.

**David Orban** [11:02:27]: But certainly others will benefit whether they are able to attend live or they look at the recording or they just look at the materials that that I prepare that that I'm sharing.

**David Orban** [11:02:46]: So as usual I will try to keep the presentation as possible.

**David Orban** [11:02:53]: And then periodically also maybe interrupt.

**David Orban** [11:02:59]: Please use the raise hand function to ask questions.

**David Orban** [11:03:05]: And if you feel the need absolutely feel free to interrupt.

**David Orban** [11:03:11]: Otherwise we will ask the questions after the initial.

**David Orban** [11:03:16]: So the.

**David Orban** [11:03:26]: repeated a remark that I always make and I and I want to keep making is that I do a hundred percent everything with AI.

**David Orban** [11:03:39]: So as a consequence, that I'm preparing for this workshop was also done with AI.

**David Orban** [11:03:56]: tell Claude, I have a workshop that is an introductory workshop for Claude prepared materials for me.

**David Orban** [11:04:11]: And I asked not only to prepare the presentation, but also to brand it with only one colors and logo and I not only.

**David Orban** [11:04:25]: asked for the presentation, but because I like to go meta, and I'm always thinking about how what we do can scale.

**David Orban** [11:04:39]: I also asked Claude to prepare the delivery guide for the workshop.

**David Orban** [11:04:50]: This is not verbatim what I will say of what I will This is the manual for someone else if they want to hold this workshop.

**David Orban** [11:05:07]: And this also was done by by by by clout.

**David Orban** [11:05:16]: Now this was just to break the ice and I'm going to Cloud is not merely a chat bot, like we have known chat GPT to be, for example, but progressively these AI assistants have become ever more powerful with capabilities that is not only.

**David Orban** [11:05:49]: I'm not only.

**David Orban** [11:05:50]: I'm not going to talk, but maybe some recommendation is that you are not, but also analyzing files, but .

**David Orban** [11:06:00]: .

**David Orban** [11:06:01]: .

**David Orban** [11:06:01]: .

**David Orban** [11:06:01]: .

**David Orban** [11:06:01]: .

**David Orban** [11:06:02]: .

**David Orban** [11:06:03]: .

**David Orban** [11:06:03]: .

**David Orban** [11:06:03]: .

**David Orban** [11:06:03]: .

**David Orban** [11:06:03]: .

**David Orban** [11:06:03]: .

**David Orban** [11:06:03]: .

**David Orban** [11:06:04]: .

**David Orban** [11:06:04]: .

**David Orban** [11:06:04]: .

**David Orban** [11:06:04]: .

**David Orban** [11:06:04]: .

**David Orban** [11:06:04]: .

**David Orban** [11:06:04]: .

**David Orban** [11:06:05]: .

**David Orban** [11:06:06]: .

**David Orban** [11:06:07]: .

**David Orban** [11:06:07]: .

**David Orban** [11:06:07]: .

**David Orban** [11:06:07]: .

**David Orban** [11:06:07]: .

**David Orban** [11:06:08]: .

**David Orban** [11:06:08]: .

**David Orban** [11:06:08]: .

**David Orban** [11:06:09]: .

**David Orban** [11:06:09]: .

**David Orban** [11:06:09]: .

**David Orban** [11:06:11]: .

**David Orban** [11:06:11]: .

**David Orban** [11:06:12]: .

**David Orban** [11:06:13]: .

**David Orban** [11:06:13]: .

**David Orban** [11:06:13]: .

**David Orban** [11:06:13]: .

**David Orban** [11:06:13]: .

**David Orban** [11:06:13]: .

**David Orban** [11:06:13]: .

**David Orban** [11:06:13]: .

**David Orban** [11:06:13]: .

**David Orban** [11:06:14]: .

**David Orban** [11:06:14]: .

**David Orban** [11:06:14]: .

**David Orban** [11:06:14]: .

**David Orban** [11:06:15]: .

**David Orban** [11:06:15]: .

**David Orban** [11:06:15]: .

**David Orban** [11:06:15]: .

**David Orban** [11:06:17]: .

**David Orban** [11:06:17]: .

**David Orban** [11:06:17]: .

**David Orban** [11:06:17]: .

**David Orban** [11:06:17]: .

**David Orban** [11:06:17]: .

**David Orban** [11:06:17]: .

**David Orban** [11:06:18]: .

**David Orban** [11:06:18]: .

**David Orban** [11:06:18]: .

**David Orban** [11:06:18]: .

**David Orban** [11:06:18]: .

**David Orban** [11:06:19]: not only a few minutes, but if the request is complex enough, even hours of work, where the request is broken down in sub-tasks and Claude execute those sub-tasks until it is done verifying its own work.

**David Orban** [11:06:42]: Now what is important is also that just very recently a month ago, a particular module became called co-work.

**David Orban** [11:06:57]: And this is what makes this is what makes this advanced agentic planning and accessible.

**David Orban** [11:07:07]: I'm going to go.

**David Orban** [11:07:13]: Now the chat mode is.

**David Orban** [11:07:16]: still available and can be useful.

**David Orban** [11:07:21]: It can not only have a conversation with you.

**David Orban** [11:07:27]: And by the way, Claude also has dictation.

**David Orban** [11:07:31]: You can.

**David Orban** [11:07:32]: Hi, Claude.

**David Orban** [11:07:35]: I am now showing your capabilities to the workshop participants.

**David Orban** [11:07:40]: Tell them hello.

**David Orban** [11:07:48]: And this will start a new chat.

**David Orban** [11:07:52]: And I'm going to start a new chat.

**David Orban** [11:07:56]: I'm going to go.

**David Orban** [11:07:57]: But you can go.

**David Orban** [11:08:01]: I'm going to go.

**David Orban** [11:08:03]: I'm going to go.

**David Orban** [11:08:06]: I'm going to be able.

**David Orban** [11:08:08]: I'm going to go.

**David Orban** [11:08:10]: I'm going to go.

**David Orban** [11:08:12]: I'm going to talk.

**David Orban** [11:08:14]: I'm going to go.

**David Orban** [11:08:15]: I'm going to You can also draft emails, reports.

**David Orban** [11:08:22]: You can, you can have it really support you in your workflow.

**David Orban** [11:08:32]: And for us, it is especially interesting and those of you who are multilingual, that is not only.

**David Orban** [11:08:45]: almost every language that we can think.

**David Orban** [11:08:49]: Now, of course, the type of support for every language is not necessarily the same.

**David Orban** [11:08:56]: And if there is support for American English and British English may be the nuances of the various Arabic variants as they are spoken in the US as opposed to Egypt or in other countries.

**David Orban** [11:09:15]: is not that precise.

**David Orban** [11:09:19]: But still, I think it can help a lot, knowing that if one doesn't speak Arabic, we can feed, chat, Arabic texts, or I'm going to understand what is what is going on.

**David Orban** [11:09:34]: And then create output that is in Arabic as well.

**David Orban** [11:09:40]: And then, of course, verify if that output is good before, sending off an email in Arabic without having checked it.

**David Orban** [11:09:51]: So, here is an example that Claude created to you to show you, analyze the at-edge documents, create a one-page executive summary, identify key risks, recommend the next steps and format as a structured report, right.

**David Orban** [11:10:10]: And this can be about anything.

**David Orban** [11:10:13]: So, for example, yesterday, Michael asked me to analyze a treasure it, to understand what are the folders that could be about optimized.

**David Orban** [11:10:32]: identified as the best person among the many who have not only owner but manager access to the to the folder.

**David Orban** [11:10:43]: And it created, based on the information that I am really nice.

**David Orban** [11:10:55]: am a really how the various folders are in terms of members, in terms of really cool visual and good and cool visualizations.

**David Orban** [11:11:20]: And then what I did is to say, okay, now that we have that is that is, okay now that we have that create a plan for, um, for improving with the highest impact, what can be done.

**David Orban** [11:11:42]: And then I told Claude to see the plan in a in a in an email to be, which, which I then, I am, I am going to create the plan, in an email And I changed the email.

**David Orban** [11:12:02]: So for example, I didn't say that he needs to decide too much because then why is he delegating?

**David Orban** [11:12:11]: I said that I will decide it.

**David Orban** [11:12:15]: So this is an illustration of the kind of simple things, relatively simple things that chat mode already supports.

**David Orban** [11:12:25]: Why do I say simple?

**David Orban** [11:12:29]: I manually exported the treasurate and I'm just said, you know, do the analysis and it was fast and simple.

**David Orban** [11:12:50]: And now the whole work.

**David Orban** [11:12:54]: I'm going to do more.

**David Orban** [11:12:55]: I'm going to do more.

**David Orban** [11:12:56]: It integrates with apps.

**David Orban** [11:13:01]: It works in a secure sandbox that is under your control.

**David Orban** [11:13:07]: And it creates files in a particular folder.

**David Orban** [11:13:12]: You can see how it is working on the task, but I'm going to go.

**David Orban** [11:13:21]: And the Ability to look at a particular folder is really very, very powerful.

**David Orban** [11:13:34]: So all of us have messy folders.

**David Orban** [11:13:39]: Sc, for example, that are collected.

**David Orban** [11:13:43]: And I like to do is something like this is something like this, where I tell, as, as you can see it here.

**David Orban** [11:13:54]: reorganize my screenshots folder, not by date, but actually look at the screenshot and decide where it should go for what the image represents and this is a .

**David Orban** [11:14:17]: It, it can execute because of what now AI can do.

**David Orban** [11:14:26]: So, you know, just showing you is a few of that it's of that, it is a, it, it not, it is not.

**David Orban** [11:14:42]: So, for example, here it says book content, and this particular image is not about a book.

**David Orban** [11:14:52]: It is a music video that I created and you can find on YouTube with obviously AI.

**David Orban** [11:15:02]: But it is okay.

**David Orban** [11:15:03]: In my experience, it is perfectly fine to give a task to AI that it will execute to, I don't know, let's say 90% precision and then add the remaining 10% because that 90% will be 10% more than I would do by myself, ever.

**David Orban** [11:15:28]: I would not spend the time categorizing my screenshots because it is just too boring.

**David Orban** [11:15:36]: I wouldn't want to do it is useful right.

**David Orban** [11:15:40]: And this is just a simple example of how this can work.

**David Orban** [11:15:47]: Now, let me show you one other thing, which is very useful and important, and it is the ability for cloud to work on the browser.

**David Orban** [11:16:04]: And I don't know if in my in my... Ally one identity.

**David Orban** [11:16:13]: I actually added the extension.

**David Orban** [11:16:18]: Yes, it is not there.

**David Orban** [11:16:20]: So let me switch profiles to my Gmail identity.

**David Orban** [11:16:25]: And here for sure the extension is there.

**David Orban** [11:16:30]: Here is closed.

**David Orban** [11:16:32]: So I open the extension and then I can say things like

**David Orban** [11:16:43]: What can I say, let me see.

**David Orban** [11:16:46]: Let me see.

**David Orban** [11:16:47]: Gutter research field forms.

**David Orban** [11:16:52]: Okay, it doesn't say in particular an example.

**David Orban** [11:16:58]: Why don't you guys help me with an example if you have something that you want to suggest.

**Ivan Fattorusso** [11:17:09]: for it to research all the deals that have been done in, I don't know if research is a good example, research all the deals that have been done in the UAE in the last 30 days and surface the deals that are in the pharmaceutical in the pharmaceutical space.

**David Orban** [11:17:40]: execute a thorough research for investment banking deals that have been completed in the UAE in in 2006 in the pharmaceuticals and I'm going to the end of the end of the end of the end of the end of the end of and some additional columns that you believe are useful in a spreadsheet.

**Ivan Fattorusso** [11:18:19]: So, actually let's do one thing.

**Ivan Fattorusso** [11:18:24]: So we

**David Orban** [11:18:25]: will execute it here in the browser where it is already working by creating the type of Google search that would generate good results.

**David Orban** [11:18:40]: It is now working.

**David Orban** [11:18:43]: All right.

**David Orban** [11:18:44]: But let's also, in parallel, I'm sorry, in cloud co-work as a as a new task.

**David Orban** [11:19:00]: Let's go.

**David Orban** [11:19:04]: folder and then say exactly the same thing.

**David Orban** [11:19:10]: And then we will be able to compare the difference.

**David Orban** [11:19:13]: Okay.

**David Orban** [11:19:16]: Remind me to look at it again, because it may ask me some questions.

**David Orban** [11:19:23]: And if I don't answer, it will just stay there patiently wait and we come back and just see the question instead of the results.

**David Orban** [11:19:32]: Okay.

**David Orban** [11:19:34]: Thank you, Ivan, for suggesting that that.

**David Orban** [11:19:37]: David, can

**Ivan Fattorusso** [11:19:38]: jump in with one more thing.

**Ivan Fattorusso** [11:19:40]: Of course.

**Ivan Fattorusso** [11:19:41]: Just what you did right now, which is that you, in co-work, you told to.

**Ivan Fattorusso** [11:19:49]: Associate the Aliwan bunch folder, right, which is where you have all your Aliwan documents, but what's the purpose of that, given that the task is largely to.

**Ivan Fattorusso** [11:20:02]: filter through the internet to find those deals, right.

**Ivan Fattorusso** [11:20:07]: What's the purpose of linking the folder to

**David Orban** [11:20:11]: it.

**David Orban** [11:20:11]: That is a good question.

**David Orban** [11:20:13]: And we may end up realizing that it wasn't useful or needed.

**David Orban** [11:20:19]: And sometimes these advanced AI tools surprise us by doing things that we didn't even think So the simplest that I can imagine is that it will decide not only to produce a spreadsheet, but also to produce a document and then the document and maybe even the spreadsheet will be formatted with only one

**David Orban** [11:20:46]: branding because that particular folder contains the skill which is something we will look at the in a few minutes that enables Claude to apply the only one branding right.

**David Orban** [11:21:02]: That is the simplest thing that comes into my mind.

**David Orban** [11:21:05]: A little more sophisticated contextual enrichment, I'm going be, I'm going to go.

**David Orban** [11:21:23]: going to that we only want something that is more than 50 million dollars in transaction or a hundred million dollars in transaction value, right.

**David Orban** [11:21:38]: And it could very well be possible that is looking at my folders, it comes to that conclusion by its rather than me having to tell it.

**David Orban** [11:21:53]: And whether this is the case or not, we will see in the live execution of the of the particular task.

**David Orban** [11:22:05]: okay.

**David Orban** [11:22:07]: So, oh, there you go.

**David Orban** [11:22:10]: There was an example.

**David Orban** [11:22:11]: I just skipped a head and created one asking you, Ivan, or I'm asking all of you and Ivan, you provided that example.

**David Orban** [11:22:20]: create a branded presentation about our first quarter results using the data in the spreadsheet apply only one brand colors include charts for revenue and headcount etc.

**David Orban** [11:22:34]: So this could be something useful in in finance or board presentations and it is a very, very simple thing to do.

**David Orban** [11:22:48]: I can maybe show you something similar.

**David Orban** [11:22:53]: Let me see, if I have it here.

**David Orban** [11:22:58]: I don't know, actually here.

**David Orban** [11:23:10]: So, here.

**David Orban** [11:23:16]: to discuss the IT budget, right, that is the IT budget, right that is the head count and what is the head count and what the head count what are the head count and what are the money on and what we are going to have.

**David Orban** [11:23:43]: And it started from a spreadsheet, right.

**David Orban** [11:23:48]: And in order to prepare for the meeting, created this presentation and then sent it to Jerry and Amina so that we would share the same understanding.

**David Orban** [11:24:00]: And then I also did something else which is here and it is actually a line by line, explanation of what we are spending money on, an explanation of what those tools are for.

**David Orban** [11:24:25]: So that someone who is not technical and has not a lot of time, can say, oh, okay, this is what this is what this is and then it's, you know, a few hundred or a few thousand And it, and now I understand, okay.

**David Orban** [11:24:47]: And so this is exactly the type of example, that we were, we were looking at before.

**David Orban** [11:24:59]: So, an important thing is that is that is able to able to real Data and my let's see if there are examples.

**David Orban** [11:25:20]: Okay, there is so before before showing you examples and then maybe the the the the presentation also.

**David Orban** [11:25:32]: In our case, are very useful for Microsoft 365 itself, email and calendar, asana for tasks, slack.

**David Orban** [11:25:44]: And so let me show you a couple of examples.

**David Orban** [11:25:48]: So I already told you yesterday, Michael asked me asked to create the the analysis of treasure right.

**David Orban** [11:26:06]: And hopefully, I remember exactly how where it was, but.

**David Orban** [11:26:16]: so that So, we exchanged an email, his last email to me was.

**David Orban** [11:26:23]: And so that for me was the go ahead that is what I am.

**David Orban** [11:26:32]: And I simply said, what did I say, transformed the points in the email thread into asana tasks.

**David Orban** [11:26:42]: And actually, Claude created an asana project, the thread that Michael, the title of the email that Michael sent me was great versus good.

**David Orban** [11:26:55]: And so there are three sections And this is interactive, you see.

**David Orban** [11:27:03]: So I can, I am now inside Claude.

**David Orban** [11:27:08]: And rather than going out into Asana, I can click on these, look at the description and then say, okay, this Judith is too ambitious or let's mark it as complete and whatever else.

**David Orban** [11:27:32]: I can just click and go go to assana to see that particular project and work there.

**David Orban** [11:27:42]: And then what I did, added unc it so that he would have visibility as we go and implement all these things.

**David Orban** [11:27:50]: And I added Michael so that he also would know that I am executing on the proposal that he approved with his thanks.

**David Orban** [11:28:02]: reply.

**David Orban** [11:28:04]: I don't need to tell him what is happening, because he can just look at the project and see that one thing is already complete and the other's hopefully will be complete within the deadlines.

**David Orban** [11:28:23]: So this is an example of how.

**David Orban** [11:28:31]: Let me give you also another example.

**David Orban** [11:28:36]: I have been, since I joined last July, going.

**David Orban** [11:28:58]: is.

**David Orban** [11:29:02]: compiled with many components.

**David Orban** [11:29:07]: Here, in particular, you can see, it uses my emails that I sent from last week, the .

**David Orban** [11:29:19]: The .

**David Orban** [11:29:20]: My .

**David Orban** [11:29:20]: .

**David Orban** [11:29:21]: .

**David Orban** [11:29:23]: .

**David Orban** [11:29:26]: What is .

**David Orban** [11:29:28]: .

**David Orban** [11:29:31]: What else?

**David Orban** [11:29:33]: Assana, of course, asana tasks completed, and then it compiles, the, the, the report,

**David Orban** [11:29:51]: say, weekly report, and, and And, so I send it to Amina and and copy Michael and it is very thorough.

**David Orban** [11:30:11]: Oh, and it matches my role is, right.

**David Orban** [11:30:19]: So the report is prepared with the contextual and that.

**David Orban** [11:30:27]: I need to document how I am working against those objectives that that the role charter and I codified, right.

**David Orban** [11:30:39]: Or not.

**David Orban** [11:30:40]: And it's fine.

**David Orban** [11:30:42]: The report is not aiming to say that I'm perfect.

**David Orban** [11:30:56]: So if the conclusion that I am actually not able to work towards those goals.

**David Orban** [11:31:07]: That is perfectly fine, at least from my point of view.

**David Orban** [11:31:14]: that I can share with my manager and say, hey, I need to redistribute some of my responsibilities or there are some blockers that stop me from achieving my goals.

**David Orban** [11:31:27]: But that is the kind of measuring and sharing reality that makes very natural challenges management rather than creating panic- panic inducing crises or emergencies that otherwise could arise.

**David Orban** [11:31:46]: So this is another illustration of how I use cloud plug-in's is actually, that is a lot of is lot of is a turning something that would impossible to do, because it would take me eight days to prepare seven-day report.

**David Orban** [11:32:14]: And instead, I just say, put it together.

**David Orban** [11:32:18]: And then, of course, I review before sending it to Michael and Amina, making some adjustments and it is really very... You know, I even enjoy It is I find it not only useful but joyful.

**David Orban** [11:32:37]: Something that would be really a chore.

**David Orban** [11:32:40]: And I would hate to do if if it were not for these tools.

**David Orban** [11:32:46]: David,

**Ivan Fattorusso** [11:32:46]: can I ask a question Yes.

**Ivan Fattorusso** [11:32:50]: You had in the, you had Asana directly integrated within Cloud just now, right, you showed us that example.

**Ivan Fattorusso** [11:33:02]: Was that, how did you do that?

**Ivan Fattorusso** [11:33:03]: What was the, how did you create that connection?

**Ivan Fattorusso** [11:33:05]: Magic?

**David Orban** [11:33:09]: So settings.

**David Orban** [11:33:15]: So settings.

**David Orban** [11:33:18]: settings.

**David Orban** [11:33:19]: Now, if I don't find uh, forgive me, no, because the, uh, there So the nomenclature changes, uh, even, uh, the creators cloud change, how they call certain things from time to time.

**David Orban** [11:33:52]: So settings, connectors, and then you can connect the various things, right.

**Ivan Fattorusso** [11:33:57]: Okay.

**Ivan Fattorusso** [11:33:57]: And these are obviously pre-existing, it looks like.

**Ivan Fattorusso** [11:34:00]: So Asana, Microsoft Slack, these inbuilt, but there isn't, for example, pipe drive,

**David Orban** [11:34:09]: Great question.

**David Orban** [11:34:10]: So that is a bit more advanced topic.

**David Orban** [11:34:16]: But it is absolutely possible create connectors for things that are not natively connected.

**David Orban** [11:34:25]: And at the end there is absolutely no difference.

**David Orban** [11:34:30]: And we will not cover that today, but you and I can work on that to make it available.

**David Orban** [11:34:36]: And that is how for example, I push my contacts to pipe drive.

**David Orban** [11:34:45]: with no delay and no burden because I'm because I use Claude to do the heavy lifting for Yeah,

**Ivan Fattorusso** [11:34:57]: so if you had, for example, both pipe drive and asana or whichever, it doesn't matter.

**Ivan Fattorusso** [11:35:06]: If you had two systems both connected, you could have those two systems speaking to each other via Claude.

**David Orban** [11:35:12]: Yes, and the example, that I typically use is meet geek and asana.

**David Orban** [11:35:20]: Okay.

**David Orban** [11:35:21]: And neither, sorry, no, asana has a native uh, integration, but meet, meet geek doesn't.

**David Orban** [11:35:27]: And so I pull the the meeting transcripts and then I extract the tasks and push the assana tasks out of the meetings automatically.

**David Orban** [11:35:41]: Yeah.

**David Orban** [11:35:42]: And again, again, sometimes it's not perfect, but I would never do manually.

**David Orban** [11:35:50]: So correcting that slight imperfect on what is the task title, what is the task description, what is the task description or who it is assigned takes so little that is absolutely worth Michael often shares on slack his his evaluation.

**David Orban** [11:36:11]: that he believes his own productivity increases on balance just four or five percent and I am astonished by that assessment because my, the way perceive it should be able to measure is that my point my, my, the way I perceive If not 10 times, at least three, four times.

**David Orban** [11:36:46]: The increase is so radical that there are things I would never even attempt to do if didn't have these tools.

**David Orban** [11:36:55]: And where have to manually intervene, it is still radically more convenient than not attempting to do them.

**David Orban** [11:37:09]: And so let's go back.

**David Orban** [11:37:13]: Oh, let's see how it is going here.

**David Orban** [11:37:17]: it's still working.

**David Orban** [11:37:18]: Oh, it created already spreadsheet.

**David Orban** [11:37:21]: It just didn't tell this is something that is happening today.

**David Orban** [11:37:29]: tried to hide it from all of But that is why when I clicked for example in the weekly report, we didn't see what I wrote.

**David Orban** [11:37:38]: And, and here the same thing is happening.

**David Orban** [11:37:41]: The task has been executed, but the output that I should receive from cloth is not being written in the interface.

**David Orban** [11:37:51]: And I think this is just today's quirk in how the tool is behaving because it is being constantly updated and built and when you start in particular co-work.

**David Orban** [11:38:06]: You are actually alerted about the fact that it is an early research preview and that all kinds of things can happen.

**David Orban** [11:38:17]: But again, it's still worth Okay, so we can look at the spreadsheet and here they Okay, so.

**David Orban** [11:38:36]: exclusive distribution agreement.

**David Orban** [11:38:39]: Oh, and by the if you remember, I said, add the columns that you think are useful.

**David Orban** [11:38:50]: So deal type is not a column I It actually decided to categorize the deals, I would And there are 11 deals that it identified.

**David Orban** [11:39:09]: Okay, so I will send this spreadsheet to Ivan, and then you can see if they exist or if they famous hallucinations.

**David Orban** [11:39:21]: Let's let's look at the other one as well which was executed on on the browser.

**David Orban** [11:39:28]: And it found eight rather 11. And so you can, you can compare the two spreadsheets that have been generated.

**David Orban** [11:39:45]: Okay.

**David Orban** [11:39:53]: The skills very useful.

**David Orban** [11:39:58]: And without having been alerted but I would like Axel to talk.

**David Orban** [11:40:05]: Because not only he already created skills, but he actually shared them with the entire team that they would be reusable others.

**David Orban** [11:40:17]: And this is going to be the next step in productivity because just like slack is useful if you use it in public channels rather than secret conversations in direct messages that no one can learn from no one can realize they are even happening The same is with AI tools.

**David Orban** [11:40:37]: The more we are able to share so that others can reuse and learn.

**David Orban** [11:40:42]: The more powerful our use is going to be.

**David Orban** [11:40:46]: So, Axel, over

**Axel Zanner-Entwistle** [11:40:55]: I started talking without being on you.

**Axel Zanner-Entwistle** [11:40:57]: Yeah, so it's pretty cool.

**Axel Zanner-Entwistle** [11:41:00]: I think, you know, when you've done a process from scratch with our good Dr. Claude.

**Axel Zanner-Entwistle** [11:41:09]: You go through it, you say, kind of like, yeah, this has been, this is the output we want.

**Axel Zanner-Entwistle** [11:41:16]: Can you create me a skill that I can use in future?

**Axel Zanner-Entwistle** [11:41:19]: And it'll do a bunch of processing and then it'll give you a little file that you can download, which obviously as as David mentioned, I've shared in the Slack channel on the AI native IB.

**Axel Zanner-Entwistle** [11:41:32]: And then all you need to do is when include there you go to I think it's capabilities.

**Axel Zanner-Entwistle** [11:41:40]: So yeah, if David clicks on capability.

**Axel Zanner-Entwistle** [11:41:45]: Maybe if you go yeah, to settings and then capabilities.

**Axel Zanner-Entwistle** [11:41:52]: Doesn't, doesn't.

**Axel Zanner-Entwistle** [11:41:53]: Maybe if you go to exit go to the chat and then go Oh,

**David Orban** [11:41:56]: look it's it hung.

**David Orban** [11:41:59]: Let me let me.

**David Orban** [11:42:02]: gracefully exit and then and then reload it and hopefully it will collaborate.

**David Orban** [11:42:06]: Do you think it is accessible from the browser as

**Axel Zanner-Entwistle** [11:42:13]: don't know, but I could share my screen to walk you through Yeah.

**Axel Zanner-Entwistle** [11:42:19]: Yeah.

**Axel Zanner-Entwistle** [11:42:22]: Let's share screen.

**Axel Zanner-Entwistle** [11:42:25]: There we go.

**Axel Zanner-Entwistle** [11:42:26]: So can you all see my good Jean-Claude Once we're here, you go to capabilities.

**Axel Zanner-Entwistle** [11:42:35]: So from from your settings thing over here, hit settings, you come to capabilities.

**Axel Zanner-Entwistle** [11:42:43]: And then you scroll down to skills.

**Axel Zanner-Entwistle** [11:42:46]: So you can do skills.

**Axel Zanner-Entwistle** [11:42:50]: So you can see here two skills that I've created.

**Axel Zanner-Entwistle** [11:42:53]: And so you can search skill, existing skills if you've got a bunch, or if you don't have any, you just click on ad.

**Axel Zanner-Entwistle** [11:43:01]: And then you can drop, either create one with Claude from scratch, write instructions, or if you've already gone through the process of creating a skill, then you just upload the skill by dragging and dropping there.

**Axel Zanner-Entwistle** [11:43:19]: And so once you've done that, you can reuse it.

**Axel Zanner-Entwistle** [11:43:23]: You can use Claude, you can tell Claude specifically.

**Axel Zanner-Entwistle** [11:43:26]: So like the Alouan briefing skill.

**Axel Zanner-Entwistle** [11:43:29]: So in any chat, once you've uploaded You can tell Claude, use Alil 1 briefing skill to create me a briefing document on the content I've just attached.

**Axel Zanner-Entwistle** [11:43:41]: And so what it will do then?

**Axel Zanner-Entwistle** [11:43:43]: It'll access the skill that you've created and it'll do exactly what the skill tells it to do.

**Axel Zanner-Entwistle** [11:43:48]: So you don't need to recycle the instructions.

**Axel Zanner-Entwistle** [11:43:52]: And then obviously depending its output, you might need to refine like You may find if a skill has just been created.

**Axel Zanner-Entwistle** [11:44:02]: It doesn't work perfectly.

**Axel Zanner-Entwistle** [11:44:03]: So even though you've iterated it through a few times from scratch with one it doesn't necessarily capture all the ways that Claude might think of something differently.

**Axel Zanner-Entwistle** [11:44:13]: So you then reiterate with the output you want and get it and then simply update it.

**Axel Zanner-Entwistle** [11:44:20]: So with the other one briefing skill, I've actually updated that one and already in the slack channel.

**Axel Zanner-Entwistle** [11:44:28]: I updated the thread with the latest version of the skill.

**Axel Zanner-Entwistle** [11:44:33]: And so all you do once you've done that is say, we've now created an output, having started from the skill that I originally built, taking into account all the iterations we made.

**Axel Zanner-Entwistle** [11:44:46]: Can you please update the skill so that next time you get the correct first time.

**Axel Zanner-Entwistle** [11:44:53]: And it'll then do the exact same thing.

**Axel Zanner-Entwistle** [11:44:55]: It'll take everything, create a skill for You can download it and then share through Slack and upload it to your thing.

**Axel Zanner-Entwistle** [11:45:04]: You can then delete the skill or replace it here well.

**Axel Zanner-Entwistle** [11:45:07]: And that's that's pretty much it.

**Axel Zanner-Entwistle** [11:45:11]: So, you know, I'll do one briefing documents.

**Axel Zanner-Entwistle** [11:45:15]: If we need briefing on our template, we simply use put in the information we want Claude and it generates a one to two page briefing document with follow-up Can we see

**Ivan Fattorusso** [11:45:27]: inside the skill itself, axle?

**Ivan Fattorusso** [11:45:29]: Just curious to see what's inside

**Axel Zanner-Entwistle** [11:45:31]: Yeah, so you can open in the chat bit.

**Axel Zanner-Entwistle** [11:45:36]: It'll actually show you all this.

**Axel Zanner-Entwistle** [11:45:37]: So you could literally copy and paste it But for sharing, it's useful to have the thing downloaded.

**Ivan Fattorusso** [11:45:48]: So this was all done by you prompting it in a in a classic just chat style.

**Ivan Fattorusso** [11:45:56]: Yeah.

**Ivan Fattorusso** [11:45:57]: But then created the right sort of coding and language or whatever you want to, it created the right instructions, right.

**Ivan Fattorusso** [11:46:05]: Yeah, yeah.

**Ivan Fattorusso** [11:46:07]: Okay.

**Ivan Fattorusso** [11:46:07]: Precisely.

**Ivan Fattorusso** [11:46:08]: So

**David Orban** [11:46:09]: thank you, Axel.

**David Orban** [11:46:11]: This is very And two things.

**David Orban** [11:46:17]: a simple example of a skill, a similar one that I created for branding and how I improved it.

**David Orban** [11:46:27]: In the first iteration, it was using the logo, for whatever reason, it always stretched without respecting the original aspect ratio.

**David Orban** [11:46:40]: So I just corrected in the chat, saying, hey, this aspect ratio is wrong, compare it with the original aspect ratio.

**David Orban** [11:46:58]: and then update the skill with this knowledge.

**David Orban** [11:47:03]: And from then when it creates, um, branded documents, will use the logo, right.

**David Orban** [11:47:16]: The second thing that is important in what Axel said and and even understood is that used to An important skill last year, you know, two months ago or three months experts online would tell, that the job of the future.

**David Orban** [11:47:42]: You have to become a prompt engineer.

**David Orban** [11:47:46]: You have to learn the secret source of course.

**David Orban** [11:47:50]: And for only $49.99 cents, I will sell you the course that teaches you the skills that last you for the next 100 years, is now Because rather than have to very carefully write the prompt.

**David Orban** [11:48:12]: You tell the AI to write the problem.

**David Orban** [11:48:19]: But we can look into but we don't need to.

**David Orban** [11:48:26]: And I

**David Orban** [11:48:35]: didn't have yet the time to explain this to Amina, or Michael, for is, sure, I'm I'm overwhelmed by my and I'm There is an executive summary, and I'm sure that they read the executive summary, one paragraph, but the 12 pages that are not They are for AI's.

**David Orban** [11:49:04]: They should feed my weekly report to the AI's and ask the Is David performing week after Is delivering on what the goals Um, can I help in some way eliminating blockers and obstacles, mean, how weekly reports is .

**David Orban** [11:49:34]: And you can, and I should think a lot of the out of the You can, of course, provide a spreadsheet or the presentation to your colleague.

**David Orban** [11:49:51]: Wonderful.

**David Orban** [11:49:53]: But the really useful use of those artifacts, those outputs, those files, is going to come from your ability to feed it to the end of the next section can be established out of that, but the process.

**David Orban** [11:50:12]: And this is going to be more and more evident as we connect systems together, and we will supervise the systems.

**David Orban** [11:50:21]: We will approve the actions, especially in regulated activities.

**David Orban** [11:50:28]: At least today, you can release a document with the document without.

**David Orban** [11:50:39]: I'm take our responsibility.

**David Orban** [11:50:45]: And it is not the AI producing the insight.

**David Orban** [11:50:48]: It is you producing the insight, or the advice or the investment recommendation or whatever a certain degree of AI support, whatever that the oversight and approval and responsibility by human is.

**David Orban** [11:51:15]: that work together in order to make us work

**David Orban** [11:51:24]: let me go back this.

**David Orban** [11:51:27]: Oh yeah, so this is the example.

**David Orban** [11:51:29]: And as you can see this presentation is also on brand.

**David Orban** [11:51:36]: It uses the colors, it uses the logos, There you go.

**David Orban** [11:51:44]: Here is the And, and now back to opening up for more questions.

**David Orban** [11:51:54]: Stephanie, I know I can always count of for asking a question.

**David Orban** [11:51:59]: Go Hi, hello everyone.

**Stephanie Tannoury** [11:52:04]: No, today I will not ask David, because from the beginning, I'm not focusing too much because we have some task here.

**Stephanie Tannoury** [11:52:11]: So maybe on the future.

**Stephanie Tannoury** [11:52:12]: I have small, I have small Let's say what Axel say regarding this skill.

**Stephanie Tannoury** [11:52:21]: So if you have a template, monthly template on internal finance here, and we can implement there and let's say we link our ERP to this one, or it

**David Orban** [11:52:30]: could be right.

**David Orban** [11:52:33]: Definitely, you by template you mean an excel sheet or you mean a kind of a report format, whichever You can create a skill that respects that template or report format.

**David Orban** [11:52:48]: Absolutely.

**David Orban** [11:52:50]: great, yes.

**David Orban** [11:52:51]: And maybe you can even ask, this is my template.

**David Orban** [11:52:58]: Do you have any suggestions to improve Can it be more effective?

**David Orban** [11:53:03]: Can it be clearer as I want to communicate and work together with colleagues?

**David Orban** [11:53:10]: And then you either reject or adopt that suggestion, I always like to try and go beyond.

**David Orban** [11:53:20]: So using AI rather than just replicating what I already do and what I already know how do.

**David Orban** [11:53:31]: Challeng is challenging myself and challenging

**David Orban** [11:53:41]: the AI to make me, I will not heed, I will not

**Stephanie Tannoury** [11:53:49]: Okay, okay, thank you.

**Stephanie Tannoury** [11:53:55]: Hello, ask a question.

**Stephanie Tannoury** [11:54:01]: I'm good.

**Shaheen AlShanableh** [11:54:01]: I'm just started using co-work today.

**Shaheen AlShanableh** [11:54:05]: Cloud for the past I could tell us a new trend.

**Shaheen AlShanableh** [11:54:09]: At least everyone from L.E.1 have moved to cloud.

**Shaheen AlShanableh** [11:54:14]: Thank

**David Orban** [11:54:14]: you, David.

**David Orban** [11:54:15]: Well, It in the leapfrogging of tools as of today everyone's.

**David Orban** [11:54:29]: Clode is okay.

**David Orban** [11:54:32]: Is this going stay the same over the next three That will be very interesting.

**David Orban** [11:54:40]: And if want to check out what is at the leading or even bleeding edge of AI.

**David Orban** [11:54:49]: It is not part of today's workshop, if you are curious and you have Just check out what is happening with open claw, CLAW, which is a agent and I have already set and I am one open claw that secretly training and fine--tuning, to be able do certain things.

**David Orban** [11:55:29]: And the difference between what was possible until, you two weeks ago and now, is that these open claw agents just don't stop.

**David Orban** [11:55:43]: They never stop.

**David Orban** [11:55:45]: They work 24-7 with the desire of being And what means to be useful, depends on how you And they can be very powerful.

**David Orban** [11:55:58]: And as a consequence, they have to be kept on a short And the reason why I mention is because the original of open claw was Claude bought.

**David Orban** [11:56:15]: And, entropic, the makers of Claude, but felt it was a name that was too close to It could be confused.

**David Orban** [11:56:24]: So they told the creator to please change And the creator did change he was miffed.

**David Orban** [11:56:39]: And through the explosion of interest, of millions of people that started to use open rather than joining entropic, three or four days he decided to join for an amount of millions of dollars that we don't even Not meta that offered many more millions of dollars, but open And open claw is part now of

**David Orban** [11:57:10]: a foundation it stays open source, but the future version of chat GPT or whatever the product is going to be based on his insights and his abilities, it is going to come from open AI, I am going to this new agentic, to go.

**David Orban** [11:57:43]: And by the way, if you want to test it on your own and you are already using Manus, already integrated, open And so you can play Without having the responsibility of setting it up, keeping it secure, updating it all the geeky things that developers love do but normal people shouldn't be bothered

**David Orban** [11:58:14]: back to your question, The adoption of Claude spread I am excited by We have about 20 licenses already in the company, including Michael, including Amina, including Luke.

**David Orban** [11:58:31]: Luke is one of the most advanced users also using a cloud code that we didn't mention have.

**David Orban** [11:58:44]: the ability to also show you, oh, not here, I'm logged in with the with the thing Yeah, sorry.

**David Orban** [11:59:04]: Yeah, there is there is a

**David Orban** [11:59:14]: There is an admin that shows And so I can confirm that most of the people who asked and received license are using daily.

**David Orban** [11:59:31]: I'm very happy And we'll see how it evolves.

**David Orban** [11:59:35]: right.

**David Orban** [11:59:36]: So anyone, a last question, Isel, Ankit?

**Izel Sequeira** [11:59:43]: No, David, nothing from my Okay, Thank you very much,

**David Orban** [11:59:48]: everyone.

**David Orban** [11:59:50]: I will the editor transcript, as and also the so that all of you, but also those who couldn't attend live.

---
*Backed up from MeetGeek on 2026-03-30 08:43*
