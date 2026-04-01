# AI Knowledge Hour #3 —  Introduction to Claude (Online)

**Date:** 2026-02-19
**Duration:** Unknown
**Meeting ID:** 9d564513-f45b-4a16-b8a7-dc8d23718cb7

## Participants
- *Participants not listed*

### Summary

The workshop provided an introduction to Claude’s advanced capabilities, demonstrating file ingestion, long-running agentic tasks via co-work, browser-based research, and integrations with apps like Asana, Slack, and Microsoft 365. David presented practical examples—branded presentations, folder analysis, automated weekly reports—showing how Claude converts inputs into deliverables and project tasks. A live research task compared browser execution and co-work outputs, producing spreadsheets for verification. Axel demonstrated reusable 'skills' for repeatable automation and encouraged sharing via Slack; Stephanie and others discussed applying templates and ERP linkage. The session closed with adoption metrics and remarks on supervision, branding, and next-step sharing of artifacts for reuse.

## Full Transcript

**Unknown speaker** [10:58:32]: I'm here.

**Unknown speaker** [10:58:33]: I'm waiting

**Ankit Choudhary** [10:58:34]: for David and the team

**Shaheen AlShanableh** [10:58:36]: members.

**Axel Zanner-Entwistle** [11:00:56]: Hi, David.

**David Orban** [11:00:58]: All right.

**David Orban** [11:00:59]: Hello, everyone.

**David Orban** [11:01:00]: Thank you for joining.

**David Orban** [11:01:01]: And the settings of this invitation.

**David Orban** [11:01:09]: .

**David Orban** [11:01:09]: .

**David Orban** [11:01:09]: .

**David Orban** [11:01:11]: .

**David Orban** [11:01:11]: .

**David Orban** [11:01:11]: .

**David Orban** [11:01:11]: .

**David Orban** [11:01:12]: .

**David Orban** [11:01:12]: .

**David Orban** [11:01:12]: .

**David Orban** [11:01:12]: .

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

**David Orban** [11:01:14]: .

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

**David Orban** [11:01:15]: .

**David Orban** [11:01:15]: .

**David Orban** [11:01:15]: .

**David Orban** [11:01:15]: .

**David Orban** [11:01:15]: .

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

**David Orban** [11:01:17]: .

**David Orban** [11:01:17]: I don't know if it started when the first of you joined, or when I joined as the organizer.

**David Orban** [11:01:22]: So, nodding probably, he means that it started when he joined first.

**David Orban** [11:01:33]: And if we wanted to have high production quality, then we would chop off that initial part.

**David Orban** [11:01:43]: So we'll see if that is going to be possible.

**Shaheen AlShanableh** [11:01:46]: I had a lot of good discussions with Ankit.

**Shaheen AlShanableh** [11:01:49]: That should be included.

**Shaheen AlShanableh** [11:01:51]: All right, all right.

**David Orban** [11:01:53]: Let me share the screen and then start so that we have time for conversations and discussions.

**David Orban** [11:02:06]: And this is an introductory course, about the class.

**David Orban** [11:02:14]: Now, some of you are already using the, I am.

**David Orban** [11:02:23]: I hope it is not going to be too boring for you.

**David Orban** [11:02:27]: But certainly others will benefit, whether they are able to attend live or they look at the recording or they just look at the materials that that I prepared that I'm sharing.

**David Orban** [11:02:46]: So as usual I will try to try to keep the presentation as possible.

**David Orban** [11:02:53]: And then periodically also maybe interrupt.

**David Orban** [11:02:59]: Please use the raise hand function to ask questions.

**David Orban** [11:03:05]: And if you feel the need, absolutely feel free to interrupt.

**David Orban** [11:03:11]: Otherwise we will ask the questions after the initial presentation.

**David Orban** [11:03:19]: So the.

**David Orban** [11:03:26]: repeated a remark that I always make and I and I want to keep making is that I do a hundred percent everything with AI.

**David Orban** [11:03:39]: So as a consequence, that I'm preparing for this workshop was also done with AI.

**David Orban** [11:03:48]: What I did as a matter of fact is to go here and tell Claude, I have a workshop.

**David Orban** [11:04:03]: That is an introductory workshop for Claude prepared materials for me.

**David Orban** [11:04:11]: And I asked not only to prepare the colors the presentation but also to brand it with only one colors and I not only.

**David Orban** [11:04:25]: asked for the presentation, but because I like to go meta and I'm always thinking about how.

**David Orban** [11:04:37]: What we do can scale.

**David Orban** [11:04:42]: also asked Claude to prepare the delivery guide for the workshop.

**David Orban** [11:04:50]: This is not verbatim what I will say, of course, this is the manual for someone else, if they want to hold this workshop.

**David Orban** [11:05:07]: And I'm going to go, I'm and this also was done by by by clout.

**David Orban** [11:05:16]: Now this was just to break the ice and to make because Claude is not merely a chat bot, like we have known chat GPT to be, for example, but I'm and .

**David Orban** [11:05:42]: I'm going to be.

**David Orban** [11:05:44]: I'm going.

**David Orban** [11:05:46]: with capabilities that are not only a conversation and maybe some recommendation that you can trust or not, but also analyzing files, I'm going to be, I'm going to go with the and I'm going go with the people, I'm going to go with your local folders.

**David Orban** [11:06:17]: for a long time, not only a few minutes, but if the request is complex enough, even hours of work, where the request is broken down in sub-tasks, and Claude execute those sub-tasks until it is done verifying its own work.

**David Orban** [11:06:42]: Now what is important is also that Just very recently, a month ago, a particular module became available called co-work.

**David Orban** [11:06:57]: And this is what makes this is what makes this advanced, agentic, planning and I'm going to talk.

**David Orban** [11:07:08]: I'm going to talk.

**David Orban** [11:07:13]: Now, the chat mode is.

**David Orban** [11:07:16]: still available and can be useful.

**David Orban** [11:07:21]: It can not only have a conversation with you.

**David Orban** [11:07:27]: And by the way, Claude also has dictation.

**David Orban** [11:07:31]: You can.

**David Orban** [11:07:32]: Hi, Claude.

**David Orban** [11:07:35]: I am now showing your capabilities to the workshop participants.

**David Orban** [11:07:39]: Tell them hello.

**David Orban** [11:07:48]: And this will start a new chat.

**David Orban** [11:07:52]: And I'm going to start a new chat.

**David Orban** [11:07:56]: I'm going to start the chat is always available, but you can't be.

**David Orban** [11:08:05]: I'm going to go.

**David Orban** [11:08:06]: I'm going to go.

**David Orban** [11:08:07]: I'm going to go.

**David Orban** [11:08:07]: I'm going to talk.

**David Orban** [11:08:08]: I'm going to talk about.

**David Orban** [11:08:09]: But you can add the documents, PDFs, spreadsheets, Microsoft Word documents, and You can also draft emails, reports.

**David Orban** [11:08:22]: You can, you can have it really support you in your workflow.

**David Orban** [11:08:32]: And for us, it is especially interesting.

**David Orban** [11:08:35]: And those of you who are multilingual, that is not only.

**David Orban** [11:08:45]: almost every language that we can think.

**David Orban** [11:08:49]: Now, of course, the type of support for every language is not necessarily the same.

**David Orban** [11:08:56]: And if there is support for American English and British English may be the nuances of the various Arabic variants as they are spoken in the US as opposed to Egypt or in other countries.

**David Orban** [11:09:15]: is not that precise.

**David Orban** [11:09:19]: But still, I think it can help a lot, knowing that if one doesn't speak Arabic, we can feed, chat, Arabic texts, or I'm going to understand what is what is going on.

**David Orban** [11:09:35]: then create output that is in Arabic as well.

**David Orban** [11:09:40]: And then, of course, verify if that output is good before sending off an email in Arabic without having checked So, here is an example that Claude created to you to show you, the at-edge documents, create a one page executive summary, identify key risks, recommend the next steps and format as a

**David Orban** [11:10:07]: structured report, right.

**David Orban** [11:10:09]: And this can be about anything.

**David Orban** [11:10:13]: So, for example, yesterday, Michael asked me to analyze a treasure it, to understand what are the folders that could be optimized, who could be identified as the best person among the many who have not only owner but manager access to the to the folder.

**David Orban** [11:10:44]: And it created, based on the information that I am really nice of the dashboard we can is how the various folders are in terms of members, in terms of really cool visual and cool visualizations.

**David Orban** [11:11:20]: And then, now that we have that we have that is that really that is create a plan for, um, for improving with the highest impact, what can be done.

**David Orban** [11:11:42]: And then I told Claude to see the plan a in a in an email to be, which, which, which I then I am, I'm going create And I changed the email.

**David Orban** [11:12:02]: So for example, I didn't say that he needs to decide too much because then why is he delegating?

**David Orban** [11:12:10]: I said that I will decide it.

**David Orban** [11:12:14]: So this is an illustration of the kind simple things, relatively simple things that chat mode already supports.

**David Orban** [11:12:25]: Why do I say simple?

**David Orban** [11:12:28]: Because I manually exported the treasurate and I'm just said, you know, do the analysis and it was fast and simple.

**David Orban** [11:12:50]: And now.

**David Orban** [11:12:53]: Now, the whole work, I'm going to do more, I'm going to do more.

**David Orban** [11:12:56]: It integrates with apps.

**David Orban** [11:13:01]: It works in a secure sandbox that is under your control.

**David Orban** [11:13:08]: it creates files in a particular folder.

**David Orban** [11:13:12]: You can see how it is working on the the task, but I don't and the Ability to look at a particular folder is really very, very powerful.

**David Orban** [11:13:34]: So all of us have messy folders.

**David Orban** [11:13:39]: Sc, for example, that are collected.

**David Orban** [11:13:43]: And I like to do is something like this is something like this, where I tell, as, as you can see it here.

**David Orban** [11:13:53]: reorganize my screenshots, folder, not by date, but actually look at the screenshot and the .

**David Orban** [11:14:07]: And this is a .

**David Orban** [11:14:08]: I'm going to is a .

**David Orban** [11:14:10]: I'm to go.

**David Orban** [11:14:14]: I'm going to that it can .

**David Orban** [11:14:20]: .

**David Orban** [11:14:20]: .

**David Orban** [11:14:20]: .

**David Orban** [11:14:20]: .

**David Orban** [11:14:21]: .

**David Orban** [11:14:21]: .

**David Orban** [11:14:21]: .

**David Orban** [11:14:21]: .

**David Orban** [11:14:21]: .

**David Orban** [11:14:22]: .

**David Orban** [11:14:22]: .

**David Orban** [11:14:23]: .

**David Orban** [11:14:23]: .

**David Orban** [11:14:23]: .

**David Orban** [11:14:24]: .

**David Orban** [11:14:24]: .

**David Orban** [11:14:24]: .

**David Orban** [11:14:24]: .

**David Orban** [11:14:24]: .

**David Orban** [11:14:25]: .

**David Orban** [11:14:25]: .

**David Orban** [11:14:25]: .

**David Orban** [11:14:25]: .

**David Orban** [11:14:25]: .

**David Orban** [11:14:25]: .

**David Orban** [11:14:25]: .

**David Orban** [11:14:26]: .

**David Orban** [11:14:27]: .

**David Orban** [11:14:28]: .

**David Orban** [11:14:30]: .

**David Orban** [11:14:30]: .

**David Orban** [11:14:30]: .

**David Orban** [11:14:30]: .

**David Orban** [11:14:30]: .

**David Orban** [11:14:30]: .

**David Orban** [11:14:31]: .

**David Orban** [11:14:31]: .

**David Orban** [11:14:31]: .

**David Orban** [11:14:31]: .

**David Orban** [11:14:31]: .

**David Orban** [11:14:31]: .

**David Orban** [11:14:31]: .

**David Orban** [11:14:31]: .

**David Orban** [11:14:31]: .

**David Orban** [11:14:32]: .

**David Orban** [11:14:32]: .

**David Orban** [11:14:32]: .

**David Orban** [11:14:32]: .

**David Orban** [11:14:32]: .

**David Orban** [11:14:32]: .

**David Orban** [11:14:32]: .

**David Orban** [11:14:32]: .

**David Orban** [11:14:32]: .

**David Orban** [11:14:32]: .

**David Orban** [11:14:33]: .

**David Orban** [11:14:33]: .

**David Orban** [11:14:33]: .

**David Orban** [11:14:33]: .

**David Orban** [11:14:33]: .

**David Orban** [11:14:33]: .

**David Orban** [11:14:33]: .

**David Orban** [11:14:34]: .

**David Orban** [11:14:34]: .

**David Orban** [11:14:34]: .

**David Orban** [11:14:34]: .

**David Orban** [11:14:34]: .

**David Orban** [11:14:34]: .

**David Orban** [11:14:34]: .

**David Orban** [11:14:34]: .

**David Orban** [11:14:34]: .

**David Orban** [11:14:34]: .

**David Orban** [11:14:34]: .

**David Orban** [11:14:35]: .

**David Orban** [11:14:35]: .

**David Orban** [11:14:35]: .

**David Orban** [11:14:35]: .

**David Orban** [11:14:35]: .

**David Orban** [11:14:35]: .

**David Orban** [11:14:36]: .

**David Orban** [11:14:36]: .

**David Orban** [11:14:36]: .

**David Orban** [11:14:36]: .

**David Orban** [11:14:36]: .

**David Orban** [11:14:36]: .

**David Orban** [11:14:36]: .

**David Orban** [11:14:37]: .

**David Orban** [11:14:37]: .

**David Orban** [11:14:37]: .

**David Orban** [11:14:37]: .

**David Orban** [11:14:37]: .

**David Orban** [11:14:37]: .

**David Orban** [11:14:37]: .

**David Orban** [11:14:40]: .

**David Orban** [11:14:40]: .

**David Orban** [11:14:40]: .

**David Orban** [11:14:40]: .

**David Orban** [11:14:40]: .

**David Orban** [11:14:40]: .

**David Orban** [11:14:40]: .

**David Orban** [11:14:40]: .

**David Orban** [11:14:40]: .

**David Orban** [11:14:40]: .

**David Orban** [11:14:40]: .

**David Orban** [11:14:41]: .

**David Orban** [11:14:41]: .

**David Orban** [11:14:41]: .

**David Orban** [11:14:41]: .

**David Orban** [11:14:41]: .

**David Orban** [11:14:41]: .

**David Orban** [11:14:41]: .

**David Orban** [11:14:41]: .

**David Orban** [11:14:41]: .

**David Orban** [11:14:41]: .

**David Orban** [11:14:41]: .

**David Orban** [11:14:41]: .

**David Orban** [11:14:41]: .

**David Orban** [11:14:42]: .

**David Orban** [11:14:42]: So, for example, here it says book content, and this particular image is not about a book.

**David Orban** [11:14:52]: It is a music video that I created and you can find on YouTube with obviously AI.

**David Orban** [11:15:02]: But it is okay.

**David Orban** [11:15:03]: In my experience, it is perfectly fine to give a task to AI that it will execute to, I don't know, let's say 90% precision, and then add the remaining 10% because that 90% will be 10 times more than would do by myself, ever.

**David Orban** [11:15:28]: I would not spend the time categorizing my screenshots because it is just too boring.

**David Orban** [11:15:36]: I wouldn't want to do it is useful, right.

**David Orban** [11:15:40]: And this is just a simple example of how this can work.

**David Orban** [11:15:47]: Now, let me show you one other thing which is very useful and important.

**David Orban** [11:15:53]: And it is the ability for cloud to to work on the browser.

**David Orban** [11:16:04]: I don't know if in my my... Ally one identity.

**David Orban** [11:16:13]: I actually added the extension.

**David Orban** [11:16:18]: Yes, it is not there.

**David Orban** [11:16:20]: So let me switch profiles to my Gmail identity.

**David Orban** [11:16:23]: And here for sure extension is there.

**David Orban** [11:16:30]: Here is closed.

**David Orban** [11:16:32]: So I open the extension and then I can say things like.

**David Orban** [11:16:43]: What can I say, that one let me see.

**David Orban** [11:16:46]: Let me see.

**David Orban** [11:16:49]: Gutter research field forms.

**David Orban** [11:16:51]: Okay, it doesn't say particular an example.

**David Orban** [11:16:58]: Why don't you guys help me with an example if you have something that you want to suggest.

**Ivan Fattorusso** [11:17:09]: for it to research all the deals that have been done in, I don't know if research is a good example, research all the deals that have been done in the UAE in the last 30 days and surface the deals that are in the pharmaceutical in the pharmaceutical space.

**David Orban** [11:17:40]: execute a thorough research for investment banking deals that have been completed in the UAE 2006 in the form of the end of the end of the end of the end of the end of and some additional columns that you are useful in a spreadsheet.

**Ivan Fattorusso** [11:18:19]: So, actually, let's do one thing.

**Ivan Fattorusso** [11:18:24]: So we

**David Orban** [11:18:25]: will execute it here in the browser, where it is already working with the type of Google search that would generate good results.

**David Orban** [11:18:40]: It is now working.

**David Orban** [11:18:43]: All right.

**David Orban** [11:18:44]: But let's also, in parallel, I'm sorry, in cloud co-work as as a new task.

**David Orban** [11:19:00]: Let's go.

**David Orban** [11:19:04]: folder and then say exactly the same thing.

**David Orban** [11:19:10]: And then we will be able to compare the difference.

**David Orban** [11:19:13]: Okay.

**David Orban** [11:19:16]: Remind me to look at it again, because it may ask me some questions.

**David Orban** [11:19:22]: And if I don't answer, it will just stay there patiently waiting and we come back and just see the question instead of the results.

**David Orban** [11:19:32]: Okay.

**David Orban** [11:19:34]: Thank you, Ivan, for suggesting David,

**Ivan Fattorusso** [11:19:37]: can jump in with one more thing.

**Ivan Fattorusso** [11:19:40]: Of course.

**Ivan Fattorusso** [11:19:41]: Just what you did right now, which is that you, in co-work, you told it to associate the Aliwan bunch folder, which is where you have all your Aliwan documents, what's the what's the purpose of that the task is largely to filter through the internet to find those deals, right.

**Ivan Fattorusso** [11:20:07]: What's the purpose of linking the folder to

**David Orban** [11:20:11]: That is a good question.

**David Orban** [11:20:13]: And we may end up realizing that it wasn't used for or needed.

**David Orban** [11:20:19]: And sometimes these advanced AI tools.

**David Orban** [11:20:25]: I don't even think.

**David Orban** [11:20:29]: So the simplest that I can.

**David Orban** [11:20:32]: imagine is that it will decide not only to produce a spreadsheet, but also to produce a document and then the document and maybe even the spreadsheet will be formatted with only one branding because that particular folder contains the skill which is something we will look at in a few minutes that

**David Orban** [11:20:57]: enables clothed to apply the only one branding right That is the simplest thing that comes into my mind.

**David Orban** [11:21:05]: A little more sophisticated contextual enrichment, going to be, I'm to go.

**David Orban** [11:21:22]: I'm going to that we only want something that is more than 50 million dollars in transaction or a hundred million dollars in transaction value, right.

**David Orban** [11:21:39]: it could very well be possible that is looking at my folders, it comes to that conclusion by rather than me having to tell it.

**David Orban** [11:21:53]: And whether this is the case or not, we will see in the live execution of the of the particular task.

**David Orban** [11:22:05]: okay.

**David Orban** [11:22:07]: So, oh, there you go.

**David Orban** [11:22:10]: There was an example.

**David Orban** [11:22:11]: I just skipped a head and created one asking you, Ivan, I'm asking all of you and Ivan, you provided that example.

**David Orban** [11:22:20]: create a branded presentation about our first quarter results using the data in the spreadsheet apply only one brand colors include charts for revenue and headcount etc.

**David Orban** [11:22:34]: So this could be something useful in in finance or board presentations and it is a very, very simple thing to do.

**David Orban** [11:22:48]: I can maybe show you something similar.

**David Orban** [11:22:53]: Let me see if I have here.

**David Orban** [11:22:59]: don't know, actually here.

**David Orban** [11:23:10]: So.

**David Orban** [11:23:11]: here it is the presentation.

**David Orban** [11:23:16]: to discuss the IT budget, right, that is the IT budget, right, that the head the headcount, and what the head count what are the project and what are the projections and what we are going to have, and what we are going to And it started from a spreadsheet, right.

**David Orban** [11:23:48]: And in order to prepare for the meeting, created this presentation and then sent it to Jerry and Amina so that we would share the same understanding.

**David Orban** [11:24:00]: And then I also did something else which is here and it actually a Line by line, explanation of what we are spending money on an explanation of what those tools for so that someone who is not technical and has not a lot of time can say, okay, this is what this is, and then it, you know, a few

**David Orban** [11:24:39]: hundred or a few thousand dollars, and it, and now I understand, okay.

**David Orban** [11:24:47]: And so this is exactly the type of example that we were, we were looking at before.

**David Orban** [11:24:59]: So, an important thing is that Clode able to real time interrogate my.

**David Orban** [11:25:12]: Let's see if there are examples.

**David Orban** [11:25:20]: Okay, there is, before, before showing you examples and then maybe the presentation also shares These plugins.

**David Orban** [11:25:32]: In our case, are very useful for Microsoft 365 itself, email and calendar, asana for tasks, slack and so let me show you a couple of examples.

**David Orban** [11:25:48]: So I already told you yesterday, Michael asked me to create the the analysis of treasure right.

**David Orban** [11:26:06]: And hopefully, I remember exactly how where it was, but.

**David Orban** [11:26:16]: so that So, we exchanged an email, his last email to me And so that for me was the go ahead that is what I And I simply said, what did I say, transformed the points in the email thread into asana tasks.

**David Orban** [11:26:42]: And actually, Claude created an asana project, the thread that Michael, the title of the email that Michael sent me was great versus good.

**David Orban** [11:26:55]: And so there are three sections And this is interactive, you see.

**David Orban** [11:27:03]: So I can, I am now inside Claude.

**David Orban** [11:27:08]: And rather than going out into Asana, I can click on these, look at the description and and say, okay, this Judith is too ambitious, or let's mark it as complete and whatever else.

**David Orban** [11:27:32]: I can just click and go go to Assana to see that particular project and work there.

**David Orban** [11:27:42]: And then what I did, added unkit so that he would have visibility as we go and implement all these things.

**David Orban** [11:27:50]: And I added Michael so that he also would know that I am executing on the proposal that he approved with his thanks.

**David Orban** [11:28:02]: reply.

**David Orban** [11:28:03]: And need to tell him what is happening, because he can just look at the project and see that one thing is already complete and the other's hopefully will be complete within the deadlines.

**David Orban** [11:28:23]: So this is an example of how.

**David Orban** [11:28:31]: Let me give you also another example.

**David Orban** [11:28:35]: I have been, since I joined last July, I'm going.

**David Orban** [11:28:58]: is.

**David Orban** [11:29:02]: compiled with many components.

**David Orban** [11:29:07]: Here, in particular, you can see, it uses my emails that I sent from last week, the .

**David Orban** [11:29:18]: .

**David Orban** [11:29:18]: .

**David Orban** [11:29:19]: .

**David Orban** [11:29:19]: .

**David Orban** [11:29:19]: .

**David Orban** [11:29:19]: .

**David Orban** [11:29:19]: .

**David Orban** [11:29:19]: .

**David Orban** [11:29:20]: .

**David Orban** [11:29:20]: .

**David Orban** [11:29:20]: .

**David Orban** [11:29:20]: .

**David Orban** [11:29:20]: .

**David Orban** [11:29:23]: .

**David Orban** [11:29:24]: .

**David Orban** [11:29:25]: .

**David Orban** [11:29:31]: What else?

**David Orban** [11:29:33]: Asana, of course, asana tasks completed, then it compiles, the, the, the report,

**David Orban** [11:29:49]: where I say weekly report, and then.

**David Orban** [11:30:02]: So, I send it to Amina and copy Michael, and it you very thorough.

**David Orban** [11:30:11]: Oh, and it matches my role charter, So the report is prepared.

**David Orban** [11:30:27]: I need to document how I am working against those objectives that that the role charter and I codified, right.

**David Orban** [11:30:39]: Or And it's fine.

**David Orban** [11:30:42]: The report is not aiming to say that I'm perfect.

**David Orban** [11:30:56]: So if the conclusion that I actually not able to work towards those goals.

**David Orban** [11:31:07]: That is perfectly fine, at least from my point of view.

**David Orban** [11:31:14]: that I can share with my manager and say, hey, I need to redistribute some of my responsibilities or there are some blockers that stop me from achieving my goals.

**David Orban** [11:31:27]: But that is the kind of measuring and sharing the reality makes very natural challenges management rather than creating panic- panic inducing crises or emergencies that otherwise could arise.

**David Orban** [11:31:46]: So this is another illustration of how I use cloud plug-in's is actually That is a lot of is lot of is a lot turning something that would be impossible to do, because it would take eight days to prepare seven-day report and instead I just say, put it together.

**David Orban** [11:32:18]: And then of course I review before sending it to Michael and Amina, making some adjustments and it is really very You know, I even enjoy It is I find it not only useful but joyful.

**David Orban** [11:32:37]: Something that would be really a chore.

**David Orban** [11:32:40]: And I would hate to do if if it were not for these tools.

**Ivan Fattorusso** [11:32:46]: David, can I ask a question Yes.

**Ivan Fattorusso** [11:32:50]: Um, you had in the, you had Asana directly integrated within with the, you showed us that example, uh, was that, how did you do that, what was the, how did you create that connection?

**Ivan Fattorusso** [11:33:05]: Magic?

**David Orban** [11:33:08]: So, uh, so settings, uh, and uh, somewhere here there are plugins.

**David Orban** [11:33:19]: Now, okay.

**David Orban** [11:33:21]: If I don't find uh, forgive uh, no, because the, uh, there the nomenclature changes, uh, uh, uh, the creators cloud change, how they call certain things from time to time.

**David Orban** [11:33:52]: So settings, connectors, and then you can connect the various things, right?

**Ivan Fattorusso** [11:33:57]: Okay.

**Ivan Fattorusso** [11:33:57]: And these are obviously pre-existing, it looks like.

**Ivan Fattorusso** [11:34:00]: So Asana, Microsoft Slack, these inbuilt, but there isn't, for example, pipe drive,

**David Orban** [11:34:09]: Great question.

**David Orban** [11:34:10]: So that is a bit more advanced topic.

**David Orban** [11:34:16]: But it is absolutely possible to create connectors for things that are not natively connected.

**David Orban** [11:34:25]: And at the end there is absolutely no difference.

**David Orban** [11:34:30]: And we will not cover that today, but you and I can work on that to make it available.

**David Orban** [11:34:36]: And that is how for example, I push my contacts to pipe drive.

**David Orban** [11:34:45]: with no delay and no burden because I'm because I use Claude to do the heavy lifting for Yeah,

**Ivan Fattorusso** [11:34:57]: so if you had, for example, both pipe drive asana or whatever, which is it doesn't matter.

**Ivan Fattorusso** [11:35:06]: If you had two systems both connected, you could have those two systems speaking to each other via Claude.

**David Orban** [11:35:12]: Yes, and the example, that I typically use is Midgik and Asana.

**David Orban** [11:35:20]: Okay.

**David Orban** [11:35:21]: And neither, sorry, no, Asana has a native integration, but Midgik doesn't.

**David Orban** [11:35:27]: And so I pull the the meeting transcripts and then extract the tasks and push the asana tasks out of the meetings automatically.

**David Orban** [11:35:41]: Yeah.

**David Orban** [11:35:42]: And again, again, sometimes it's not perfect, but I would never do manually.

**David Orban** [11:35:50]: So correcting that slight imperfect what is the task title, what is the task description, what is the task description or who it is assigned takes so that is absolutely worth it.

**David Orban** [11:36:06]: Uh, Michael often shares on slack his his evaluation.

**David Orban** [11:36:11]: that he believes his own productivity increases on balance just 4, 5% and I am astonished by that assessment because my, way perceive it should be able to measure it is that my product is that my, the way I perceive it and I If not 10 times, at least three, four times.

**David Orban** [11:36:46]: The increase is so radical that there are things I would never even attempt to if didn't have these tools.

**David Orban** [11:36:55]: And where I have to manually intervene, it is still radically more convenient than not attempting to do them.

**David Orban** [11:37:09]: And let's go back.

**David Orban** [11:37:13]: Oh, let's see how it is going Oh, it's still working.

**David Orban** [11:37:18]: Oh, it created already spreadsheet.

**David Orban** [11:37:21]: It just didn't tell this is something that is happening today.

**David Orban** [11:37:28]: tried to hide it from all But that is why when I clicked for example in the weekly report, we didn't see what I wrote.

**David Orban** [11:37:38]: And, and here, the same thing is happening.

**David Orban** [11:37:41]: The task has been executed, but the output that I should receive from cloud is not being written in the interface.

**David Orban** [11:37:51]: And I think this is just today's in how the tool is behaving.

**David Orban** [11:37:58]: Because it is being constantly updated and built and when you start in particular co-work.

**David Orban** [11:38:06]: You are actually alerted about the fact that it is an early research preview and that all kinds of things can happen.

**David Orban** [11:38:17]: But again, it's still worth Okay, so we can look at the spreadsheet and here Okay, so.

**David Orban** [11:38:36]: exclusive distribution agreement.

**David Orban** [11:38:39]: Oh, and by the if you remember, add the columns that you think are useful.

**David Orban** [11:38:49]: So deal is not a column I It actually decided to categorize the deals, I would And there are 11 deals that it identified.

**David Orban** [11:39:09]: Okay.

**David Orban** [11:39:10]: So I will send this spreadsheet to Ivan, and then you can see if they exist or if they famous hallucinations.

**David Orban** [11:39:21]: Let's let's look at the other one as well which was executed on on the browser.

**David Orban** [11:39:28]: And it found eight rather 11. And so you can, you can compare the two spreadsheets that have been generated.

**David Orban** [11:39:45]: Okay.

**David Orban** [11:39:53]: The skills very useful and without having been alerted but I would like Axel to talk to talk about them.

**David Orban** [11:40:05]: because not only he already created skills, but he actually shared with the entire team that they would be reusable by others and this is going to be the next step in productivity because just like slack is useful if you use it in public channels rather than secret conversations in direct messages

**David Orban** [11:40:29]: that no one can learn no one can realize they are even happening The same is with AI tools.

**David Orban** [11:40:37]: The more we are able to share so that others can reuse and learn, the more powerful our use is going to be.

**David Orban** [11:40:46]: So, Excel, over you.

**Axel Zanner-Entwistle** [11:40:59]: It's pretty cool.

**Axel Zanner-Entwistle** [11:41:00]: I think, you know, when you've done a process from scratch with our good Dr. Claude.

**Axel Zanner-Entwistle** [11:41:09]: You go through it, you kind of like, yeah, this has this is the output we want.

**Axel Zanner-Entwistle** [11:41:16]: Can you create me a skill that I can use in future?

**Axel Zanner-Entwistle** [11:41:19]: And it'll do a bunch of processing and then it will give you a little file that you can download.

**Axel Zanner-Entwistle** [11:41:24]: which obviously, as David mentioned, I've shared in the Slack channel on the AI native IB.

**Axel Zanner-Entwistle** [11:41:32]: And then all you need to do is when in Claude there, you go to I think it's capabilities.

**Axel Zanner-Entwistle** [11:41:40]: So yeah, if David clicks on capability.

**Axel Zanner-Entwistle** [11:41:45]: Maybe if you to go to settings and then go.

**Axel Zanner-Entwistle** [11:41:52]: Doesn't go to the chat and then go Oh, look,

**David Orban** [11:41:56]: look, it's it Let me let me gracefully exit and then reload it and hopefully it will collaborate.

**David Orban** [11:42:07]: Do you think it is accessible from the browser as

**Axel Zanner-Entwistle** [11:42:13]: don't know, but I could share my screen to walk you through it.

**Axel Zanner-Entwistle** [11:42:19]: Yeah.

**Axel Zanner-Entwistle** [11:42:22]: Chess screen.

**Axel Zanner-Entwistle** [11:42:23]: There we go.

**Axel Zanner-Entwistle** [11:42:26]: So, can you all see my good John Claude Dunham.

**Axel Zanner-Entwistle** [11:42:30]: Yes.

**Axel Zanner-Entwistle** [11:42:32]: Once we're here, you go to capabilities.

**Axel Zanner-Entwistle** [11:42:35]: So from your settings thing over here, you come to capabilities.

**Axel Zanner-Entwistle** [11:42:42]: And then you scroll down to skills.

**Axel Zanner-Entwistle** [11:42:49]: So you can see here two skills that I've created.

**Axel Zanner-Entwistle** [11:42:52]: And so you can search skill, existing skills if you've got a bunch.

**Axel Zanner-Entwistle** [11:42:59]: Or if you don't have any, you just click ad.

**Axel Zanner-Entwistle** [11:43:02]: And then you can drop either create one with Claude from write instructions.

**Axel Zanner-Entwistle** [11:43:09]: or if you've already gone through the process of creating a skill, then you just upload the skill by dragging and dropping there.

**Axel Zanner-Entwistle** [11:43:19]: And so once you've done that, you can reuse it.

**Axel Zanner-Entwistle** [11:43:23]: You can use Claude.

**Axel Zanner-Entwistle** [11:43:24]: You can tell Claude specifically.

**Axel Zanner-Entwistle** [11:43:26]: So like the only one briefing skill.

**Axel Zanner-Entwistle** [11:43:28]: So in any chat, once you've uploaded You can tell Claude, use Alde 1 briefing to create me a briefing document on the content I've just And so what it will then?

**Axel Zanner-Entwistle** [11:43:42]: It'll access the skill that you've created and it'll exactly what the skill tells it to do.

**Axel Zanner-Entwistle** [11:43:48]: So you don't need to recycle instructions.

**Axel Zanner-Entwistle** [11:43:52]: And then obviously depending its output, you might need to refine like You may find if a skill has just been created.

**Axel Zanner-Entwistle** [11:44:02]: It doesn't work perfectly.

**Axel Zanner-Entwistle** [11:44:03]: So even though you've iterated it through a few times from scratch with one It doesn't necessarily capture all the ways that Claude might think of something differently.

**Axel Zanner-Entwistle** [11:44:13]: So you then reiterate with the output you want and then simply update it.

**Axel Zanner-Entwistle** [11:44:20]: So with the other one briefing skill, I've actually updated that one and already in the Slack channel.

**Axel Zanner-Entwistle** [11:44:28]: I updated the thread with the latest version of the skill.

**Axel Zanner-Entwistle** [11:44:32]: And so all you do once you've done that is say, we've now created an output, having started from the skill that I originally taking into account all the iterations we made.

**Axel Zanner-Entwistle** [11:44:46]: Can you please update the so that next time you get the correct output first And it'll then do the exact same thing.

**Axel Zanner-Entwistle** [11:44:55]: It'll take everything, create a skill for you.

**Axel Zanner-Entwistle** [11:44:57]: You can download it and then share through Slack and upload it to your thing.

**Axel Zanner-Entwistle** [11:45:03]: You can then delete the skill or replace it here well.

**Axel Zanner-Entwistle** [11:45:09]: And that's that's pretty much it.

**Axel Zanner-Entwistle** [11:45:11]: So, you know, I'll do one briefing documents.

**Axel Zanner-Entwistle** [11:45:14]: If we need a briefing on our template, we simply use put in the information we want Claude and it generates a one to two page briefing document with follow-up

**Ivan Fattorusso** [11:45:27]: Can we see inside the skill itself, axle?

**Ivan Fattorusso** [11:45:29]: Just curious to see what's inside Yeah,

**Axel Zanner-Entwistle** [11:45:32]: so you can open in the chat bit, it'll actually show you all this.

**Axel Zanner-Entwistle** [11:45:37]: So you could literally copy and paste it But for sharing, it's useful to have the thing downloaded.

**Axel Zanner-Entwistle** [11:45:48]: So this

**Ivan Fattorusso** [11:45:49]: was all done by you prompting it in a in classic just chat style.

**Ivan Fattorusso** [11:45:56]: Yeah.

**Ivan Fattorusso** [11:45:57]: But then it created the right sort of coding and language or whatever you want to, it created the right instructions, Yeah, yeah.

**Ivan Fattorusso** [11:46:07]: Okay.

**Ivan Fattorusso** [11:46:07]: Precisely.

**David Orban** [11:46:08]: So thank you, Axel.

**David Orban** [11:46:11]: This is very And two things.

**David Orban** [11:46:16]: One, a simple example of a skill, a similar one that I created for branding and how I improved it.

**David Orban** [11:46:27]: In the first iteration, it was using the logo, for whatever reason, it always stretched without respecting the original aspect ratio.

**David Orban** [11:46:40]: So I just corrected in the saying, hey, this aspect ratio is wrong, compare it with the original aspect ratio.

**David Orban** [11:46:58]: and then update the with this And from then when it creates, um, branded documents, will use the logo, right.

**David Orban** [11:47:16]: The second thing that is important in what Axel said and and even understood is that used to an important skill last you know, two months ago or three months and experts online would tell, that the job of the future.

**David Orban** [11:47:42]: You have to become a prompt engineer.

**David Orban** [11:47:45]: You have to learn the secret source of course.

**David Orban** [11:47:50]: And for only $49.99 cents, I will sell you the course that teaches you the skills that will last you for the next 100 is now Because rather than have very carefully write the prompt.

**David Orban** [11:48:12]: You tell the AI to write the problem.

**David Orban** [11:48:18]: But we can look into it, but we don't to.

**David Orban** [11:48:26]: And I

**David Orban** [11:48:35]: didn't have yet the time to explain this to Amina or Michael, for sure, I'm I'm sure I'm sure.

**David Orban** [11:48:49]: There is an executive summary, and I'm sure that they read the executive summary, one paragraph, but the 12 pages that are not They are for AI's.

**David Orban** [11:49:04]: They should feed my weekly report to the AI's and ask the Is David performing week after Is he delivering on what the goals Um, can I help in some way eliminating blockers and .

**David Orban** [11:49:28]: And I'm .

**David Orban** [11:49:34]: And you can .

**David Orban** [11:49:42]: And should think think a lot of the out of the You can, of course, provide a spreadsheet or the presentation to your Wonderful.

**David Orban** [11:49:53]: But the really useful use of those artifacts, those outputs, those files, is going to come from your ability to feed it to the end of the next section can be established out of that, but the process.

**David Orban** [11:50:11]: And this is going to be more and more evident as we connect systems together we will supervise the systems.

**David Orban** [11:50:21]: We will approve the actions, especially in regulated activities.

**David Orban** [11:50:28]: Um, at least today, you can release a document without, uh, I'm going to uh, take our responsibility.

**David Orban** [11:50:45]: And it is not the AI producing the insight.

**David Orban** [11:50:48]: It is you producing the insight or the advice or the investment recommendation or whatever with a certain degree of AI support, whatever oversight and approval and responsibility by.

**David Orban** [11:51:12]: ever more efficient connected systems that work together in order in order to make us work

**David Orban** [11:51:24]: let me go back Oh yeah, so this is the example.

**David Orban** [11:51:28]: And as you can see this presentation is also on brand.

**David Orban** [11:51:36]: It uses the colors, it uses the logos, There you go, here's the And now back to opening up for more questions.

**David Orban** [11:51:54]: Stephanie, I know I can always count for the question.

**Stephanie Tannoury** [11:52:04]: No, today I will not ask David, because from the beginning, I'm not focusing too much because we have some task here.

**Stephanie Tannoury** [11:52:11]: So maybe on the future, I have small, I have small Let's say what Axel say regarding this skill.

**Stephanie Tannoury** [11:52:20]: So if you have a template, monthly template on internal finance here, and we can implement there and let's say we link our ERP to this one, or it

**David Orban** [11:52:30]: could right.

**David Orban** [11:52:33]: Definitely, by template you mean an excel sheet or you mean a kind of a report format, whichever You can create a skill that respects that template or report format.

**David Orban** [11:52:48]: Absolutely.

**David Orban** [11:52:50]: great.

**David Orban** [11:52:51]: Yes.

**David Orban** [11:52:51]: And maybe you can even ask, this is my template.

**David Orban** [11:52:58]: Do you have any suggestions to improve Can it be more effective?

**David Orban** [11:53:03]: Can it be clear as I want to communicate and work together with colleagues?

**David Orban** [11:53:10]: And then either reject or adopt that suggestion, I always like to try and go beyond.

**David Orban** [11:53:31]: Challeng is challenging myself and challenging the AI to me, I will not heed, I will not

**Stephanie Tannoury** [11:53:49]: Okay, okay, thank you.

**Stephanie Tannoury** [11:53:50]: you.

**Stephanie Tannoury** [11:53:55]: Hello,

**Shaheen AlShanableh** [11:53:59]: ask a question.

**Shaheen AlShanableh** [11:54:01]: I'm good.

**Shaheen AlShanableh** [11:54:01]: I'm just started using core today.

**Shaheen AlShanableh** [11:54:05]: Cloud for the past I could tell it's a new trend.

**Shaheen AlShanableh** [11:54:09]: At least everyone from L.E.1 have moved to Claude.

**David Orban** [11:54:14]: Thank you, David.

**David Orban** [11:54:15]: Well, it in the leapfrogging of tools.

**David Orban** [11:54:24]: As of today, everyone's.

**David Orban** [11:54:29]: Claude is okay.

**David Orban** [11:54:32]: Is this going stay the same over the next three That will be very interesting.

**David Orban** [11:54:40]: And if want to check out what is at the leading or even.

**David Orban** [11:54:46]: It not part of today's workshop, if you are curious and you have Just check out what is happening with open claw, CLAW, which, which agent and I have already set an only one open claw, that secretly training and fine--tuning, to be able do certain things.

**David Orban** [11:55:29]: And the difference between what was possible until, know, two weeks ago and now, is that these open claw agents just don't stop.

**David Orban** [11:55:43]: They never stop.

**David Orban** [11:55:45]: They work 24-7 with the desire of being And what means to be useful, depends on how you And they can be very powerful.

**David Orban** [11:55:58]: And as a consequence, they have to be kept on a short And the reason why I mention is because the original of open claw was Claude bought.

**David Orban** [11:56:15]: And, entropic, the makers of Claude, but felt it was a name that was too close to It could be confused.

**David Orban** [11:56:24]: So they told the creator to please change And the creator did change name, he was miffed.

**David Orban** [11:56:39]: And through the explosion of interest, of millions of people that started to use open rather than joining entropic.

**David Orban** [11:56:50]: Three or four days ago, he decided to amount of millions of dollars that we don't Not meta that offered many more millions of but open And open claw is part now of a foundation where it stays open source, but a future version of chat GPT or whatever the product is going to be based on his insights

**David Orban** [11:57:27]: and his abilities, is going to come from open AI, going to be this new agentic, but go.

**David Orban** [11:57:43]: And, by the way, if you want to test it on your own, and you are already using Manus, already integrated, open And so you can play Without having the responsibility of setting it up, keeping it secure, updating it, all the geeky things developers love do, but normal people shouldn't be

**David Orban** [11:58:14]: Back to your question.

**David Orban** [11:58:17]: The adoption of cloth spread I am excited by We have about 20 licenses already in the company, including Michael, including Amina, including Luke.

**David Orban** [11:58:31]: Luke is one of the most advanced users also using a cloud code that we didn't mention.

**David Orban** [11:58:44]: the ability to also show oh, not here, sorry.

**David Orban** [11:58:56]: I'm logged in with the with the wrong thing Yeah, sorry.

**David Orban** [11:59:04]: Yeah, sorry.

**David Orban** [11:59:05]: Anyway, there is a there is a

**David Orban** [11:59:14]: There is an admin that shows And so I can confirm that most of the people who asked and received license are using daily.

**David Orban** [11:59:31]: I'm very happy And we'll see how it evolves.

**David Orban** [11:59:35]: All So anyone, a last question, Isel, No,

**Izel Sequeira** [11:59:43]: David, nothing from Okay,

**David Orban** [11:59:47]: Thank you very much, everyone.

**David Orban** [11:59:50]: I will the editor transcript and also the so that all of you but also those who couldn't attend live.

---
*Backed up from MeetGeek on 2026-03-30 08:43*
