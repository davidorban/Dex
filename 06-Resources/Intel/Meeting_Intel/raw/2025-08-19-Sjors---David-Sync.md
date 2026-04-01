# Sjors / David Sync

**Date:** 2025-08-19
**Duration:** Unknown
**Meeting ID:** 60b0fa6b-d584-47bf-863c-dda72e8c7cd4

## Participants
- *Participants not listed*

### Summary

The meeting focused on establishing a structured project organization and folder system, emphasizing the creation of readme files and the setup of a GitHub repository for collaboration. David outlined tasks for both himself and Sjors, including the creation of a private repository and ensuring GitHub access. Discussions included the transition from cloud code to Cascade for development, with David expressing concerns about the complexity of cloud code. The management of GitHub repositories, including branching strategies, was addressed, alongside the need for clarity in cloud configuration management. David also reported on the successful creation of structured transcriptions and slides for an AI tools workshop, with plans to replicate this process. Challenges in project development were highlighted, particularly regarding non-functional project buttons, and the importance of structured instructions was reiterated. Additionally, the meeting covered fundraising strategies, regulatory compliance, and potential acquisitions, with specific tasks assigned to both David and Sjors to further these initiatives.

## Full Transcript

**Unknown speaker** [11:01:56]: my hands through the air and they do whatever they want.

**Unknown speaker** [11:02:02]: Okay.

**Unknown speaker** [11:02:02]: No particular psychological reason.

**David Orban** [11:02:09]: Okay, so I think you wanted to share your screen and let me tell you that you are stupid.

**David Orban** [11:02:20]: Probably.

**Sjors Bogers** [11:02:22]: But let's start with a question.

**Sjors Bogers** [11:02:27]: I think maybe that logic is flawed, but it's good to have a few set of folders that are good to have in any new project.

**Sjors Bogers** [11:02:37]: Is that correct?

**Sjors Bogers** [11:02:38]: Is that correct?

**Sjors Bogers** [11:02:40]: So.

**David Orban** [11:02:44]: I think yesterday we mentioned prompt engineering as opposed to context engineering and it is the case that I start to wonder how to tell things or ask models things because they remember too well So I haven't yet started, but it is very likely that I will start to use incognito mode.

**David Orban** [11:03:22]: As an example, we are talking about the new brand that Tag is going to have, as it unveils its broader set of activities on top of advisory.

**David Orban** [11:03:38]: And there was a candidate that was discarded.

**David Orban** [11:03:41]: I made the research I told you about for other candidates.

**David Orban** [11:03:45]: And there is a good final, um, if not final, this, there is a good new candidate that hopefully will be approved in time so that by September it can be launched.

**David Orban** [11:03:58]: Yep.

**David Orban** [11:03:58]: And a few days ago, I, uh, told, oh, yeah.

**David Orban** [11:04:07]: In developing the brand voice, which I said I would do for Alice, the CMO.

**David Orban** [11:04:21]: I said, okay, do it not for tag, but for Uram, which is the candidate new name.

**David Orban** [11:04:31]: And now it cannot stop referring to tag as Uram.

**David Orban** [11:04:36]: Okay.

**David Orban** [11:04:38]: And I keep telling those, forget about Uram, don't worry about Uram.

**David Orban** [11:04:43]: I will tell you if it is actually adopted as the final name, right?

**David Orban** [11:04:49]: So if we complained about models remembering too little, we are already flipping into them remembering too much.

**David Orban** [11:05:04]: Another thing that I started to do is I have a prompt that looks at all my repositories and sanitizes them, looking for trivial stuff like API keys that should only be in specific environment files, never committed to GitHub, etc.

**David Orban** [11:05:29]: etc.

**David Orban** [11:05:34]: private keys for wallets hopefully don't ever happen but also just information about me that could be aggregated or surfaced and the prompt supposedly leaves harmless information in and something that is above a given threshold tries to delete it or redact it it explicitly puts between brackets

**David Orban** [11:06:05]: redacted right yeah and so I'm trying to develop the best practices that are healthy I think will be necessary and based on the right to be forgotten part of the GDP are actually a legal requirement even okay so back to your question Yes, it is very good to have a folder for each project.

**David Orban** [11:06:42]: And then another very naturally emerging necessary habit is to have the model write read me for each folder in the root of the folder.

**David Orban** [11:06:55]: And that means that you can actually put folders as subfolders in others, and then you can say, here are these two subfolders, do X with A after reading the readme, and combine it with B after reading the readme of that other one, in order to achieve the desired result Y. Yep.

**David Orban** [11:07:31]: So, so those are two good habits, yes.

**Sjors Bogers** [11:07:37]: Yeah, and I would like to set up a good logic for that.

**Sjors Bogers** [11:07:42]: So whatever I'm going to do moving forward, that the basics are covered, right?

**Sjors Bogers** [11:07:46]: Yeah, yeah.

**Sjors Bogers** [11:07:47]: But right now I feel way too clumsy to do it the right way, simply because I don't know what should be in that read-me-to-read.

**David Orban** [11:07:54]: so do you want me to show how I do it, sharing my screen instead?

**Sjors Bogers** [11:07:59]: Yeah, maybe that works as a starter, Okay.

**David Orban** [11:08:05]: So let me do it on here and then I join as a companion mode.

**David Orban** [11:08:19]: And then I can show you a bit more as well about other projects that I am active in and how and why.

**Sjors Bogers** [11:08:29]: And one other quick question, what does your setup look like on your side of the screen?

**Sjors Bogers** [11:08:36]: Because I'm doing everything on the small MacBook it's horrible, right?

**Sjors Bogers** [11:08:42]: Because you have to switch constantly through the screens.

**David Orban** [11:08:45]: Yes and no, yes and no.

**David Orban** [11:08:46]: I, I, for example, this morning I only worked on the Mac.

**David Orban** [11:08:51]: Mm-hmm.

**David Orban** [11:08:52]: I, in front of me,

**Sjors Bogers** [11:09:03]: Thank you.

**David Orban** [11:09:06]: So, in front of me, I have two monitors.

**Sjors Bogers** [11:09:14]: Yeah.

**David Orban** [11:09:15]: Connected to a normal PC.

**David Orban** [11:09:19]: Actually, it's pretty old, I should change it.

**David Orban** [11:09:23]: And if you look at the other camera, This is this is my Mac.

**David Orban** [11:09:29]: So this morning, putting the Mac on the desk, I just started working on the Mac, and then I kept working on the Mac rather than moving to the PC.

**David Orban** [11:09:42]: And yes, some things are very small, depends on if you have an 11-inch or a 13-inch Mac.

**David Orban** [11:09:58]: And my previous one was 11 inch or maybe 12. And when I was looking at the 15 inch MacBook Pro, I felt like agoraphobic too big.

**David Orban** [11:10:10]: I would get lost in the screen.

**David Orban** [11:10:14]: I'm pretty happy about this.

**David Orban** [11:10:17]: This is, I think, the 13 inch MacBook Pro, M3.

**David Orban** [11:10:29]: If I'm not mistaken.

**Sjors Bogers** [11:10:33]: Yeah, I have the same size, but the M1 version.

**David Orban** [11:10:36]: M3 MacBook Pro of 14 inch.

**David Orban** [11:10:40]: All right, 14, not 13. And it is 2023. So next year is going to be time to change it.

**David Orban** [11:10:49]: What I would also like is to buy one of those new, um, um, little Mac cubes and potentially also the NVIDIA cube.

**David Orban** [11:11:05]: NVIDIA produced a little cube as well.

**David Orban** [11:11:08]: We'll see what kind of budget we will have.

**David Orban** [11:11:15]: Yep.

**David Orban** [11:11:15]: Okay.

**David Orban** [11:11:19]: So in terms of setup, I use a couple of browsers, ARC.

**David Orban** [11:11:27]: and DIA, they are from the same company.

**David Orban** [11:11:32]: Um, DIA is, uh, a Jentic, so directly you can start asking stuff in the browser.

**Sjors Bogers** [11:11:40]: Okay.

**David Orban** [11:11:40]: And, and it will, it will respond rather than going to do to Google, right?

**David Orban** [11:11:45]: I haven't gotten accustomed to that yet, including that I am using, um, Very little search these days.

**David Orban** [11:11:55]: Even if I have a search like question, I typically use GROC.

**David Orban** [11:12:01]: So here in ARC, I have a folder with the various links and I go to GROC, which you cannot get if you go to grog.com because of EU bullshit, but you can get if you go to X and it is now free.

**David Orban** [11:12:32]: It was available only if you were paying a member whatever on X, but now it's free.

**David Orban** [11:12:41]: And, and it says, hey, go to grog.com, but at least until recently, oh, great.

**David Orban** [11:12:52]: Okay.

**David Orban** [11:12:54]: All right.

**David Orban** [11:12:58]: So here's my history.

**David Orban** [11:13:00]: And

**David Orban** [11:13:06]: so this is one.

**David Orban** [11:13:07]: Then, of course, I have the apps for ChatGPT and for Cloud.

**David Orban** [11:13:14]: And I have windsurf and warp, right?

**David Orban** [11:13:22]: Yeah.

**David Orban** [11:13:23]: So this is my my setup and what I sometimes do is as you I code inside windsurf so this morning that is what I did and then I typically do this to get more sorry to get more screen space Right, I, this is, and then I can do this too.

**David Orban** [11:13:55]: So, this is the terminal with Clode already loaded, and I can do something like,

**David Orban** [11:14:13]: so I, sorry, I press command option C, which is the equivalent of

**David Orban** [11:14:26]: copy path, okay, to refer to a file rather than using at, because you could refer to a file with at something, okay, sorry, you see, but then I have to go the down, down, down, down, down, at least I haven't yet haven't yet found a less clumsy way to refer to files.

**David Orban** [11:14:55]: So what I do is I say add

**David Orban** [11:15:02]: smart to do to here based on the latest files in the folder.

**David Orban** [11:15:19]: So this now runs directly with Cloud rather than anything else, and then it will do whatever it will do.

**David Orban** [11:15:28]: Yeah, now let's, you are welcome to ask questions or we can start from zero, as we said, to set up something.

**Sjors Bogers** [11:15:37]: Yeah, let's start from zero, but maybe we can start with setting up the GitHub folder.

**Sjors Bogers** [11:15:45]: Okay.

**Sjors Bogers** [11:15:48]: Because that was one of the tasks I should give you access to so we can work on stuff together, right?

**Multiple speakers** [11:15:53]: Yes, yes.

**David Orban** [11:15:56]: Okay, so So I go to github.com

**David Orban** [11:16:10]: And I assume you set up your user, right?

**Sjors Bogers** [11:16:13]: Yeah.

**Sjors Bogers** [11:16:14]: Okay.

**David Orban** [11:16:16]: And then I just do a new repository.

**David Orban** [11:16:20]: And

**David Orban** [11:16:26]: I call it test for shores.

**David Orban** [11:16:35]: And I hit enter, which I shouldn't have.

**David Orban** [11:16:41]: So now it created public.

**David Orban** [11:16:44]: But it's fine.

**David Orban** [11:16:46]: There's nothing in it yet.

**David Orban** [11:16:48]: So I can go to settings and then I can make it private.

**Sjors Bogers** [11:17:07]: It did show change visibility.

**Sjors Bogers** [11:17:09]: I'm not sure that was a section you're looking for.

**David Orban** [11:17:13]: Is there a section called visibility?

**Sjors Bogers** [11:17:16]: All the way at the bottom where you just wear, where everything became red.

**Sjors Bogers** [11:17:21]: It's at visibility, the first one.

**Sjors Bogers** [11:17:24]: Isn't that what you're looking for?

**Sjors Bogers** [11:17:25]: Yes.

**David Orban** [11:17:27]: Thank you.

**David Orban** [11:17:40]: Okay, and I have 2FA with Google Authenticator.

**David Orban** [11:17:49]: Okay.

**David Orban** [11:17:49]: So I just open Authenticator on my phone.

**David Orban** [11:18:00]: Search for GitHub because I have a lot of them and I enter the code.

**David Orban** [11:18:08]: Okay.

**David Orban** [11:18:10]: So now this repository has a given URL, which is this with other settings.

**David Orban** [11:18:26]: Yeah.

**David Orban** [11:18:26]: And just to make my life easier, keep all these folders in a folder is called dev.

**David Orban** [11:18:37]: So you see here at the bottom.

**David Orban** [11:18:40]: users, David Orban, Dev.

**Sjors Bogers** [11:18:45]: Yep.

**David Orban** [11:18:45]: And this is the user that you log in with in your Mac.

**David Orban** [11:18:49]: When you, when you open your Mac.

**David Orban** [11:18:53]: So there is this folder Dev, and I will create a new folder and call it test, what is it, test, test for shores.

**David Orban** [11:19:11]: That's it.

**David Orban** [11:19:12]: And it is now empty.

**David Orban** [11:19:14]: So everything else I can do inside windsurf.

**David Orban** [11:19:21]: So I hit command shift new n for new window.

**David Orban** [11:19:28]: And I say open folder, dev test for shores.

**David Orban** [11:19:39]: I trust And then I can go here, open the terminal, increase the font size a bit for you, and I can do Git in it.

**David Orban** [11:19:59]: This is local, okay?

**David Orban** [11:20:02]: It just says, okay, it creates a .git file, right?

**David Orban** [11:20:08]: and it says, okay, it looks like we will use version control in this folder.

**David Orban** [11:20:15]: That's And now I say just test.md, and I

**David Orban** [11:20:32]: say hello, And it keeps suggesting silly things.

**David Orban** [11:20:40]: So that we can also stop and say something different like, sorry.

**David Orban** [11:20:47]: What?

**David Orban** [11:20:49]: Why am I... Okay.

**David Orban** [11:20:53]: One, two.

**David Orban** [11:20:57]: Right.

**David Orban** [11:20:57]: It just invents things now, which is fine.

**David Orban** [11:21:02]: Okay.

**David Orban** [11:21:03]: So now can say... Um, here in using, uh, using cascade.

**David Orban** [11:21:14]: Where is cascade?

**David Orban** [11:21:15]: They moved it around, sorry.

**David Orban** [11:21:18]: I am lost.

**David Orban** [11:21:20]: Okay.

**David Orban** [11:21:23]: So here I can say, um, git add the dot commit push, right?

**David Orban** [11:21:30]: So this is just a lazy, my, my lazy way of telling the model.

**David Orban** [11:21:36]: to add all the files that are not already tracked.

**David Orban** [11:21:40]: The U here, this U means that it is not tracked.

**David Orban** [11:21:44]: You see, untracked.

**David Orban** [11:21:46]: Yep.

**David Orban** [11:21:46]: So the add dot means add all the files.

**David Orban** [11:21:50]: Commit means, um, whatever.

**David Orban** [11:21:56]: I don't know the difference between adding and committing.

**David Orban** [11:22:00]: And push means, uh, upload to the, to the repository.

**David Orban** [11:22:05]: And.

**David Orban** [11:22:06]: It will potentially create a meaningful commit message.

**David Orban** [11:22:15]: It depends on the model.

**David Orban** [11:22:17]: So I noticed that GPT-5, for example, is very lazy in generating the commit message.

**David Orban** [11:22:29]: And this SWE software engineer, I assume, is free, and it is a bit better.

**Sjors Bogers** [11:22:38]: So just to summarize what the push means, whatever you made local is now pushed to and saved to the GitHub.

**David Orban** [11:22:46]: Correct, right, and the folder.

**Multiple speakers** [11:22:48]: Correct, exactly.

**David Orban** [11:22:50]: And you can think of it as a very sophisticated, fine granularity backup.

**David Orban** [11:22:58]: even when you are working alone.

**David Orban** [11:23:02]: And when you work with someone else, it becomes extremely valuable, indispensable because then you know that you are not going to override each other's work.

**David Orban** [11:23:19]: Yeah.

**David Orban** [11:23:19]: Um,

**David Orban** [11:23:25]: oh yeah.

**David Orban** [11:23:26]: So, somewhere there should be out to complete, super complete.

**David Orban** [11:23:36]: Yeah, I don't know.

**David Orban** [11:23:37]: Oh, no, not auto execution.

**David Orban** [11:23:39]: There you go.

**David Orban** [11:23:40]: Turbo.

**David Orban** [11:23:41]: So it will stop asking me for permission.

**David Orban** [11:23:47]: Right, I will just say, don't bother me, go ahead.

**David Orban** [11:23:51]: I trust you.

**Sjors Bogers** [11:23:52]: But what's the reason that you now switch from doing things with cloud code in the console to doing it with cascade?

**David Orban** [11:24:02]: Yeah, I could do it with either, no reason.

**David Orban** [11:24:07]: Um, my experience is that cloud.

**David Orban** [11:24:11]: tends to overcomplicate simple tasks.

**David Orban** [11:24:15]: So they take too long.

**David Orban** [11:24:17]: The fastest actually is warp.

**David Orban** [11:24:21]: Warp is extremely to the point.

**David Orban** [11:24:25]: Okay.

**David Orban** [11:24:25]: So I could also go here.

**David Orban** [11:24:30]: You see, test for source, it already knew, I don't know if you noticed.

**David Orban** [11:24:35]: Yeah, so as I started typing, this it, yes, that's it.

**David Orban** [11:24:41]: And then, and then each of them now starts to keep a dot file, a dot model file.

**David Orban** [11:24:50]: So, yes, I say, go ahead and optimize, absolutely.

**David Orban** [11:24:53]: That is what I want.

**David Orban** [11:24:57]: And it will generate a warp.md.

**David Orban** [11:25:02]: And I already set up cloud, it would have seen cloud.md and in some way linked to right?

**David Orban** [11:25:16]: And there is very little here now, I will show you a couple of setups that will create a more meaningful model file, because this is empty.

**David Orban** [11:25:33]: And depending on what you want to do, you should adapt your model file to what what you do.

**David Orban** [11:25:42]: It can also be accomplished with the readmys and other things, but the model files are today the best practice.

**David Orban** [11:25:50]: Okay.

**David Orban** [11:25:52]: Um, so.

**David Orban** [11:25:56]: Yeah, it says, I don't know, I just did what I thought would make sense given that this is empty, right?

**David Orban** [11:26:07]: That's fine.

**David Orban** [11:26:08]: So, did

**David Orban** [11:26:16]: I tell it the, the, oh, I didn't tell it what the remote repository is.

**David Orban** [11:26:23]: Did it?

**David Orban** [11:26:26]: Um, would it help if I gave the URL of the remote, oops, um, let's copy it again.

**David Orban** [11:26:56]: because it is taking too much.

**David Orban** [11:27:01]: And I don't know, but I realized I forgot to give it the URL, right?

**David Orban** [11:27:10]: Okay, and now it is gonna be faster.

**David Orban** [11:27:16]: Okay.

**David Orban** [11:27:23]: There is even a latest trend, which is crazier, even more, because am not deploying anything with tag, right?

**David Orban** [11:27:34]: I am just working on various text files, as if it were.

**David Orban** [11:27:39]: Yeah.

**David Orban** [11:27:40]: But when I was vibe coding action here, I would trigger deployment from GitHub to Versal And then I would have a loop monitoring if the deployment was successful, read the error message, and keep working until everything, well, everything, until at least the deployment was successful.

**David Orban** [11:28:14]: And that was pretty cool, but there is a latest trend people work directly on the server so they they run cloud code on the server with the remote terminal and skip all the intermediary and it's i don't know why i don't know what the analogy can be like some extreme very extreme sport okay Okay, so

**David Orban** [11:28:55]: if we go back to to github now and we look at the code.

**David Orban** [11:29:03]: test will be there.

**David Orban** [11:29:05]: Formatted, right?

**David Orban** [11:29:09]: Big, smaller, small list, dotted list, whatever, right?

**David Orban** [11:29:16]: Yep.

**David Orban** [11:29:16]: And we can look at the MD.

**David Orban** [11:29:20]: And the github has a lot of... nice things that it interprets.

**David Orban** [11:29:28]: So I don't know if I can search inside my repository mermaid.

**David Orban** [11:29:40]: here the code is this.

**David Orban** [11:29:46]: And it, it...

**David Orban** [11:29:53]: How can No, I don't a preview.

**David Orban** [11:29:55]: There you go.

**David Orban** [11:29:56]: And it renders an org chart.

**Sjors Bogers** [11:30:01]: Yeah.

**Sjors Bogers** [11:30:01]: Right.

**David Orban** [11:30:02]: So basically what I said is, look at the new people we are hiring then update the org chart.

**David Orban** [11:30:11]: That's what I Yeah.

**David Orban** [11:30:19]: So, back to the... back to the other repository.

**David Orban** [11:30:32]: Okay, this is, this is the repository that we just created, right?

**David Orban** [11:30:36]: With the two, with the two fives.

**David Orban** [11:30:39]: Now, one concept that you only have to worry about when you have multiple people is the different branches.

**David Orban** [11:30:48]: Typically, there are three, four branches, let's say.

**David Orban** [11:30:52]: Um, a development branch, a staging branch and the production branch.

**David Orban** [11:31:00]: And then various developers merge their code into the main developer.

**David Orban** [11:31:08]: So they work on their local machine, test something, it works, they create an issue with a pull request, to whoever manages these features, let's say, that what they work on belong to, they review their code, and then complete the pull request, which will push the code into the development branch,

**David Orban** [11:31:46]: then it is... migrated into the preview branch for final testing, and then the production branch is live.

**David Orban** [11:32:02]: Yeah.

**David Orban** [11:32:03]: And that is what people see visiting the website or using the application.

**Sjors Bogers** [11:32:08]: Right?

**David Orban** [11:32:10]: When you are working alone on your own stuff, then typically you don't have to worry about multiple branches but it is good that you know what they and what they are for okay now let's install cloud and you know you can you can with with no problem except code switching or context switching in your

**David Orban** [11:32:52]: own brain.

**David Orban** [11:32:53]: You can go from here, which is the terminal inside windsurf to here, which is warp in the same folder.

**David Orban** [11:33:05]: Absolutely no difference.

**David Orban** [11:33:08]: And whether you are working here or there is just, you know, as you, as it strikes your fancy.

**Sjors Bogers** [11:33:17]: You know, the problem is that they cannot really, the agents cannot really communicate with each other, That's separated.

**Sjors Bogers** [11:33:24]: They cannot look at the context of what the other one was doing in the conversation.

**Sjors Bogers** [11:33:29]: Correct?

**David Orban** [11:33:30]: Yeah, they can, but it's clumsy.

**David Orban** [11:33:34]: They communicate, well, So there are three ways that they can communicate.

**David Orban** [11:33:41]: One, by reading and writing files.

**David Orban** [11:33:47]: course.

**David Orban** [11:33:48]: And that is clumsy and slow.

**David Orban** [11:33:51]: Two, via MCP, and I haven't tested it.

**David Orban** [11:34:00]: Three, I will show you Claude Flow that sets up all kinds of interagent communications using a local database for enhanced memory and then that is fast and precise.

**David Orban** [11:34:30]: And yeah, this will also improve.

**David Orban** [11:34:36]: It will be so useful.

**David Orban** [11:34:39]: I'm already pitting them one against the other, right?

**David Orban** [11:34:44]: Constantly.

**David Orban** [11:34:45]: Yeah.

**David Orban** [11:34:45]: And it is useful to do that.

**David Orban** [11:34:47]: So, making that more

**David Orban** [11:34:55]: explicit rather than copy and pasting is absolutely useful.

**David Orban** [11:35:02]: And I'm sure there are already ways to do that I actually found don't know if you remember one of the tests I did a few months ago was what I called then comparator that would put the output of different different models side by side and now there there are full-blown platforms doing so I'm sure

**David Orban** [11:35:31]: that searching Actually, you know Let's search for So for something like this, I would go back to Grok.

**David Orban** [11:35:43]: And let's use Grok.com since we saw that it works.

**David Orban** [11:35:52]: So I would go like, I always, Pete, Claude and Chad GPT against each other helping each other improve the outcomes of prompts and research and whatever reasoning, but I need to copy and paste the output from one to the other and I want to avoid I am sure that there are GitHub repositories or

**David Orban** [11:36:28]: applications.

**David Orban** [11:36:31]: that enable this communication between different models.

**David Orban** [11:36:38]: Find them for

**David Orban** [11:36:44]: Okay.

**David Orban** [11:36:47]: So, all right, what we were saying is that we can go and install cloud to see what happens.

**David Orban** [11:36:55]: So I always forget Um, the particular command, and, like to go here anyway, because all the time the next command for the installation cloud flow.

**David Orban** [11:37:17]: So I know that here is the command to install cloud, this is

**David Orban** [11:37:31]: And since it was already installed, it did nothing.

**David Orban** [11:37:34]: It only checked that it is up to date.

**David Orban** [11:37:37]: Yeah.

**David Orban** [11:37:37]: And, and, uh, NPM is a global installation.

**David Orban** [11:37:41]: NPX is a local installation.

**David Orban** [11:37:44]: So I was already installing cloud globally.

**David Orban** [11:37:47]: However, think that this installation, also created the, the, the, oh, no, it didn't.

**David Orban** [11:37:56]: All Okay, I thought it would create cloud files already, but it didn't.

**David Orban** [11:38:04]: Okay.

**David Orban** [11:38:05]: There are global cloud files.

**David Orban** [11:38:10]: If we open directly dev or even David, we should see You see, here it is, cloud.md.

**David Orban** [11:38:30]: So here, cloud.md is a two, an excessively long cloud configuration file, is you will see that, yeah, this is, for example, has nothing to do with what I'm doing now.

**David Orban** [11:38:55]: It's It's relative to sensei, right?

**David Orban** [11:39:00]: So I have to clean this up.

**David Orban** [11:39:02]: Let me leave this here, so I will do that, go back to the test.

**Sjors Bogers** [11:39:09]: But does that mean that for each individual project, you should get a cloud MD file in that folder?

**David Orban** [11:39:15]: Yes, and there is a hierarchy.

**David Orban** [11:39:18]: So it looks first for the one in the folder, and if it finds it, it ignores the one in the folder above.

**David Orban** [11:39:28]: Okay.

**Sjors Bogers** [11:39:28]: And if it doesn't find it, then it looks above and so And would it make sense to have a customized cloth MD, let's say we're making a Tetris game, So you have the main folder where the standard setup is given, and then a tweaked one in the project where you are building the Tetris Yeah.

**Sjors Bogers** [11:39:53]: interact with each other.

**Sjors Bogers** [11:39:55]: So he uses the standard setup.

**David Orban** [11:39:57]: I think so.

**David Orban** [11:39:58]: I think so.

**David Orban** [11:39:59]: I don't know what to what degree, because I just said that it ignores the upper layer.

**David Orban** [11:40:03]: And if it's correct, then whatever is in the standard setup should be replicated below rather than just the difference.

**David Orban** [11:40:14]: But yeah, you can learn more and then teach Okay.

**David Orban** [11:40:20]: So, so, um, After installing Cloud, what I do I install.

**David Orban** [11:40:28]: so this is how I launch it.

**David Orban** [11:40:31]: I don't need to launch it now, but this setting, dangerously skip permissions, is what stops Cloud for keep asking stuff.

**David Orban** [11:40:40]: Yeah, it just does So this is the installation of Cloud Flow, which is the agentic setup.

**David Orban** [11:40:50]: It uses NPX, so it's a local installation.

**David Orban** [11:40:56]: And that is why it is actually doing things.

**David Orban** [11:40:59]: And as you see, it created a lot of files.

**David Orban** [11:41:05]: Yep.

**David Orban** [11:41:06]: Uh, dot flow, dot cloud, cloud, cloud.md.

**David Orban** [11:41:12]: Git ignore, blah, blah, blah.

**Multiple speakers** [11:41:14]: All I have one question about the permission can you go one step back where you just showed me dangerously ignore that step I didn't launch that I just told you that is how I would launch Yeah, but I have a question about it.

**Sjors Bogers** [11:41:30]: So I was watching the tutorial and the guy who set permissions and thinks it wasn't allowed to But obviously I don't know what these things mean, right?

**Sjors Bogers** [11:41:41]: And he skipped over it really fast.

**Sjors Bogers** [11:41:43]: And I saw other examples where those permissions were only four lines and he had 12 lines.

**Sjors Bogers** [11:41:48]: Sure.

**David Orban** [11:41:49]: I go all the Everything.

**Sjors Bogers** [11:41:54]: Okay.

**Sjors Bogers** [11:41:56]: Yeah.

**Sjors Bogers** [11:41:56]: Isn't it smart to, to make a distinction between things that should never We'll see.

**David Orban** [11:42:08]: Okay.

**David Orban** [11:42:11]: Okay.

**David Orban** [11:42:11]: Okay, so after this, I could launch Cloud Flow, Swarm, Swarm, Surprise Shores, with a clever demo.

**David Orban** [11:42:28]: Some graphics.

**David Orban** [11:42:32]: Make good.

**David Orban** [11:42:36]: It must work.

**David Orban** [11:42:41]: One shot.

**David Orban** [11:42:46]: I have, what, sorry.

**David Orban** [11:42:54]: That quote is because I didn't close something.

**David Orban** [11:42:57]: Cloud, flow, swarm, surprise, shores.

**David Orban** [11:43:01]: All right, it is good.

**David Orban** [11:43:02]: What's going

**David Orban** [11:43:14]: Okay, I can do also, can launch cloud and then paste that thing.

**David Orban** [11:43:27]: Right?

**David Orban** [11:43:27]: So it is complaining about the cloud file in my folder.

**David Orban** [11:43:32]: So evidently it is reading both.

**David Orban** [11:43:34]: It is reading both the local and the bigger or the upper right?

**David Orban** [11:43:53]: Okay, so let copy this again.

**David Orban** [11:44:10]: and then it will do something.

**David Orban** [11:44:13]: So, having given something as stupid as this, it will have to make a lot of choices, not only what to do, but also what tools to employ in order to do And you see, it creates these various agents.

**David Orban** [11:44:39]: So this is the coordinator.

**David Orban** [11:44:40]: This is the initializing.

**David Orban** [11:44:43]: And then there is an architect, which does creative direction.

**David Orban** [11:44:49]: There's a coder for the graphics.

**David Orban** [11:44:52]: There's a coder for animation.

**David Orban** [11:44:54]: Optimizer for performance.

**David Orban** [11:44:58]: Here is the coordinator.

**David Orban** [11:45:01]: And then this is the task that creates the list.

**David Orban** [11:45:07]: So now can start seeing what decided to do.

**David Orban** [11:45:14]: HTML5 canvas-based graphics engine, okay.

**David Orban** [11:45:17]: Particle systems with physics, interactive AI swarm, smooth animations, sound effects, and audio visits, it's too ambitious.

**David Orban** [11:45:27]: It will not make it.

**David Orban** [11:45:31]: I mean, all right, maybe, but I think it's over doing So, while we are waiting, let me show you what I did yesterday.

**David Orban** [11:45:49]: When I was in Abu Dhabi, I did sorry, for some reason the Yeah, for some reason the indexing of my apps screwed So I have to hunt for them here Never do that, so I don't know where they Okay.

**David Orban** [11:46:16]: So when I, in Abu Dhabi.

**Sjors Bogers** [11:46:18]: Before you jump into this story, I have a quick question in between.

**Sjors Bogers** [11:46:21]: Yes.

**Sjors Bogers** [11:46:22]: In the video I was watching the guy said that built into cloud code, you can force it to, there were different classifications, and I think it's called think, extra think and hyperthink, or something Are you familiar Yeah.

**David Orban** [11:46:38]: And, um, I don't want to have to make those decisions.

**David Orban** [11:46:46]: And GPT-5 does that for It has a router, internal router, invisible to the user that decides to which particular model to send your query inside an invisible wrapper.

**David Orban** [11:47:09]: And so, One, I don't know how it is done.

**David Orban** [11:47:15]: Two, I'm sure you can learn.

**David Orban** [11:47:17]: Three, I think it's useless because it is granular and the models will absorb very fast that kind decision.

**David Orban** [11:47:35]: Yeah.

**David Orban** [11:47:36]: So created two Not created.

**David Orban** [11:47:44]: I held two workshops.

**David Orban** [11:47:49]: One about digital assets and the other about AI tools and recorded my voice and the screen, as often happens, especially because it was just five people, not 50. It was very interactive.

**David Orban** [11:48:09]: I didn't very much follow the slides even.

**David Orban** [11:48:15]: But people who didn't attend wanted, since they know that I record everything, wanted to have the recording.

**David Orban** [11:48:25]: And instead of giving them recording, worked with or reworked it with Claude or Claude Flo.

**David Orban** [11:48:46]: creating a transcription and that probably I did with Claudia manually because I was lazy and then starting from the transcription let find it I created a structured sorry

**David Orban** [11:49:17]: Starting from the raw transcription, which is, which is this Right, it's impossible to read.

**David Orban** [11:49:29]: created a structured transcription with segments where there is an introduction and the narration.

**David Orban** [11:49:41]: Okay.

**David Orban** [11:49:46]: I created using Manus the slides that correspond to these segments.

**David Orban** [11:49:55]: Okay.

**David Orban** [11:49:58]: And then gave the prompt to use the API key and this is the only thing I gave this API key and the voice ID.

**David Orban** [11:50:15]: I don't remember, oh yeah.

**David Orban** [11:50:20]: I did one test with this one, but then I stopped, I will show you.

**David Orban** [11:50:26]: So I said, take the slides and I manually exported them in JPEG rather than doing it programmatically So take the slides, and use a standard voice that is good for the introduction, then that particular voice ID for the narrator, create an MP, an MPEG-4 for each.

**David Orban** [11:51:05]: And by the way, here's a music that I created.

**David Orban** [11:51:09]: So fade fade out.

**David Orban** [11:51:15]: And don't know if

**David Orban** [11:51:33]: you can hear the audio actually.

**Sjors Bogers** [11:51:36]: And it took the voice from 11 labs or were it?

**David Orban** [11:51:39]: So if you hear, you will

**Sjors Bogers** [11:51:55]: Very faint.

**Multiple speakers** [11:51:57]: No, it's very loud, so you would Okay.

**David Orban** [11:52:01]: How can I?

**David Orban** [11:52:02]: Actually, it's not too big, so will drop it on WhatsApp.

**David Orban** [11:52:16]: Shit.

**David Orban** [11:52:31]: Help If you look at the icon of the screen.

**David Orban** [11:52:36]: Huh?

**Multiple speakers** [11:52:37]: Top Yeah,

**David Orban** [11:53:22]: It's

**David Orban** [11:53:30]: funny how Meta thinks nothing about privacy.

**David Orban** [11:53:34]: You cannot even, oh, you Can No, you cannot hide the sidebar.

**Sjors Bogers** [11:53:43]: Yeah.

**David Orban** [11:53:43]: It's so Okay, so you can download it Yeah.

**Multiple speakers** [11:53:52]: I What?

**Sjors Bogers** [11:53:57]: I'm listening and watching right

**Sjors Bogers** [11:54:27]: Yeah, so it's a clone of your own voice, right?

**David Orban** [11:54:30]: Yes.

**David Orban** [11:54:33]: And what I like about it is that compresses an hour of rambling into 17 minutes of crisp delivery.

**David Orban** [11:54:48]: And it is completely scalable.

**David Orban** [11:54:53]: And adaptive, because rather than having to wonder, okay, how am, how am I gonna map the original slides to what actually the narrator said generates a new set of slides that have a better match.

**David Orban** [11:55:13]: So I am pleased and I'm gonna do now the same for the AI tools workshop.

**David Orban** [11:55:23]: And these are just examples that I'm giving.

**David Orban** [11:55:26]: All right.

**David Orban** [11:55:27]: So in the meantime, mind- blowing demo is ready and I no trust that it will actually work.

**David Orban** [11:55:48]: Okay.

**David Orban** [11:55:49]: So illustrating itself.

**David Orban** [11:55:54]: And it is animating something.

**David Orban** [11:55:56]: And, uh, or it did.

**David Orban** [11:56:00]: Spone agent, burst.

**David Orban** [11:56:05]: I don't know Click anywhere to attract swarm.

**David Orban** [11:56:10]: I'm clicking.

**David Orban** [11:56:11]: Yeah.

**David Orban** [11:56:13]: 60 frames per second, but nothing happens.

**Sjors Bogers** [11:56:19]: All So, So yeah, yeah, I'm sorry, but it is nice, it's a nice B. I have a theory and I'm not sure if it's correct, even before we started discussing this opportunity, I told you that I was making a drum sequencer for friend, right, a few weeks ago.

**David Orban** [11:56:44]: There are there are Easter it says press M for personalized message.

**David Orban** [11:56:53]: Hold space for quantum burst and then what, chaos mode, key five for wild effects, chaos.

**David Orban** [11:57:03]: Yeah, but there's nothing.

**David Orban** [11:57:06]: So I could say something like this.

**David Orban** [11:57:09]: So you can just select the screen and say, but nothing shows on the screen.

**David Orban** [11:57:23]: and then you paste the screenshot.

**David Orban** [11:57:27]: And here, I didn't run cloud flow.

**David Orban** [11:57:36]: The demo is loading, but the canvas isn't rendering the agents.

**David Orban** [11:57:39]: Let me fix this immediately.

**David Orban** [11:57:41]: So we'll These are the cycles, the normal cycles that you do.

**Sjors Bogers** [11:57:48]: Sorry, you were saying that you have a hypothesis Yeah, so a while ago I created the drum sequencer and I made really simple, And then it it turned out that I had to upload sounds for it to have sounds to otherwise it wasn't working.

**Sjors Bogers** [11:58:06]: So yesterday I tried to do that again with bit manually orchestrating the agent.

**Sjors Bogers** [11:58:13]: So I had an art director to make it look nice, a UX UI guide to optimize.

**Sjors Bogers** [11:58:19]: yeah the usage of buttons and things and another role i think it was just the developer to create the actual so it came up with brilliant story how to do stuff and then the end result was nothing that worked something that you just did it what it could do but when you once you pressed the button

**Sjors Bogers** [11:58:39]: said it's not assigned and i tried to troubleshoot it and it just didn't but i feel like if you start very simple and add on you get much better results than Starting with a big.

**David Orban** [11:58:52]: Yeah, so there are two things I would say.

**David Orban** [11:59:03]: is always better to know what instructions it is executing rather than giving it a complete freedom.

**David Orban** [11:59:12]: Yeah, and that instruction can be the architecture, but then you Yeah, it

**David Orban** [11:59:32]: doesn't That's fine.

**Sjors Bogers** [11:59:34]: I have the exact same problem yesterday.

**David Orban** [11:59:38]: So you can have the architecture and the description, the PRD as it is called the whole but then make it work on one at rather than just say, do One at a time be consistent about And there may be other ways, but the PRD, I do it with code guide whoop, dev.

**David Orban** [12:00:30]: Yeah, these are the various projects that designed I showed this at one of the meetings a few months ago.

**David Orban** [12:00:46]: What is very interesting about this is that it is decently adaptive, so you describe the project in a few sentences and then invites you to give more detail, asking you questions, and the questions are generated based on your short description.

**David Orban** [12:01:11]: Yeah.

**David Orban** [12:01:11]: And if you are lazy, you can generate the answers to the questions.

**David Orban** [12:01:16]: Of course.

**David Orban** [12:01:20]: Okay.

**Multiple speakers** [12:01:21]: And do you have a plan for this, or you just use the free No, I'm paying for Yeah, I'm paying for a lot Okay.

**David Orban** [12:01:35]: what we saw, regardless of the result, right?

**David Orban** [12:01:40]: What we saw is creating the GitHub repository.

**David Orban** [12:01:53]: It's here somewhere.

**David Orban** [12:01:57]: Creating the GitHub repository.

**David Orban** [12:02:00]: Oh, now we can do one more push, So I can go here, actually, let me push from So I say again, just get, can say, all the files to the GitHub repository and push to the remote branch.

**Sjors Bogers** [12:02:34]: And what exactly is the difference between repository and the remote Yeah, I expressed myself incorrectly.

**David Orban** [12:02:44]: What I wanted to say is to track all the files, but it understood.

**David Orban** [12:02:50]: So don't leave any files behind.

**David Orban** [12:02:52]: That's what I wanted So now I say run and then I say don't bother

**David Orban** [12:03:09]: You see, add all project files, including cloud agents, documentation, and demo.

**David Orban** [12:03:14]: Nice, And now it pushed it and it is summarizing it and it's done.

**David Orban** [12:03:22]: And if we go here we refresh, we will see everything.

**David Orban** [12:03:33]: right, JavaScript, HTML, shell, Or we can say something like, um, where are the, sorry.

**David Orban** [12:03:50]: We can say

**David Orban** [12:04:18]: So if you look at what the repository is about, trying to understand and create a file that explains

**David Orban** [12:04:34]: And we'll see if it does actually.

**David Orban** [12:04:38]: to, I don't know if I showed you this before.

**David Orban** [12:04:43]: This is, this is how I work, right?

**David Orban** [12:04:54]: I have all the craft here, right, is nothing to do with anything.

**David Orban** [12:05:03]: And there, sometimes files get accumulated in the main folder.

**David Orban** [12:05:10]: So periodically I say clean up the route and then it moves the files where they belong.

**David Orban** [12:05:19]: And then I have, um, Here, for example, I have documents meetings.

**David Orban** [12:05:31]: And then I have, for example, yesterday met this Digimax.

**David Orban** [12:05:39]: And this is the meeting, the restructured meeting transcript, right?

**David Orban** [12:05:50]: Sorry, no, this is the transcript.

**David Orban** [12:05:55]: Yes.

**David Orban** [12:05:57]: So this is what we say, to the And these are the minutes, which is more about actions, items, and owners, etc.

**David Orban** [12:06:09]: And then somewhere there should be also an investment memo.

**David Orban** [12:06:17]: Let me

**David Orban** [12:06:22]: Where memo digi there so rather than being where it should is still here in the temp folder I should tell move it to a more appropriate because there is an investment folder and this should be And then this is still manual, but what I do that there is an origination folder,

**David Orban** [12:07:10]: which the files for the CRM basically, Yeah.

**David Orban** [12:07:19]: And so here is Digimax.

**David Orban** [12:07:22]: And I put these files in a word format so that others are not freaking out because they don't know what the .md but they can just double click here.

**David Orban** [12:07:35]: And so what matters is the investment memo that already in the title says pass.

**David Orban** [12:07:44]: And so here it is, how do I And this kind of formatting, you know, is

**David Orban** [12:08:01]: automatic from the markdown.

**David Orban** [12:08:05]: Yeah.

**David Orban** [12:08:05]: And the style sheet of the document creates So.

**David Orban** [12:08:14]: We don't yet have formally established investment committee and investment decision procedures, but I am pretending as if we had Yep.

**Sjors Bogers** [12:08:33]: from this I understand one of your roles is also to have investor

**David Orban** [12:08:43]: And this morning, for example, what I did was something pretty important because

**David Orban** [12:08:56]: created prompt to research

**David Orban** [12:09:32]: Sorry.

**David Orban** [12:09:37]: Okay, back here.

**David Orban** [12:09:42]: I created a prompt to research the features and the regulatory criteria for an onshore digital asset exchange under the ESCA regulations.

**David Orban** [12:10:11]: And I ran it with GPT- 5, with Claude, with GROC, and then I started to understand better what this was all about, what is the situation, now I created And I took note of all the progress of the various enhancements.

**David Orban** [12:10:39]: And then I created a draft that will become 10- page proposal with executive summary, etc.

**David Orban** [12:10:52]: And I created a three-page policy brief.

**David Orban** [12:10:58]: And this structured work, you see, for example, rather than doing it inside the main tech folder, I did it in a separate folder.

**David Orban** [12:11:14]: Yeah, the other day, because Digimax, the guy I said no because I immediately told him that we would pass, right?

**David Orban** [12:11:26]: And he also asked me, but would you be an advisor?

**David Orban** [12:11:29]: And I said, all right, send me your proposal how you are going pay or pay with equity to be an advisor, and we can So said, let's sign an NDA.

**David Orban** [12:11:50]: And bullshit, I'm going to meet with hundreds of companies.

**David Orban** [12:11:54]: I can't sign an NDA with So since we didn't have I created a framework.

**David Orban** [12:12:01]: Oh, you see the pollution of Yeah.

**David Orban** [12:12:07]: Um, so I created a, a, a framework to, to sign or, or, or not sign an NDA and when it makes sense and when, when it doesn't make sense, right?

**David Orban** [12:12:20]: And, uh, since we are a regulated entity, It is very important to have a policy for everything.

**David Orban** [12:12:33]: And then, in order not to die under the weight of all of those policies, develop a system that checks that you are compliant automatically.

**David Orban** [12:12:46]: That will key.

**David Orban** [12:12:48]: Yeah.

**David Orban** [12:12:53]: So any other question with regards to how this whole thing works.

**Sjors Bogers** [12:13:01]: Um, I had a question earlier, but it slipped my mind when you're switching stories.

**Sjors Bogers** [12:13:08]: I'm sure we'll, pop up time.

**Sjors Bogers** [12:13:13]: Um, Maybe what I can do is set up what you did do a test example here for you to look at and then share it with you so you on GitHub directly, mean, and then I meet your account, right, to David my username is David It will surprise quite unexpected.

**David Orban** [12:13:42]: Yeah, that's perfect.

**Sjors Bogers** [12:13:47]: What's there anything from the video?

**Sjors Bogers** [12:13:57]: Slip my mind for now.

**Sjors Bogers** [12:13:58]: I'm sure it will pop up once I give it a again.

**Sjors Bogers** [12:14:03]: Okay, where Yeah, and I had another question not related to the coding side but you said yesterday they're raising either 40 or 50 million, is to create the war chest to do investments or just the assets to grow the business So, no, there are already LP commitments.

**David Orban** [12:14:28]: LP stands for limited partners.

**David Orban** [12:14:32]: for the fund, target is 2 billion and there are commitments for 1 And that is to make the investments.

**David Orban** [12:14:43]: Yeah.

**David Orban** [12:14:43]: The 40 or 50 million has two separate uses.

**Multiple speakers** [12:14:53]: or 15 million are for another license, whatever it is, I don't And the remainder are operational, it's operational Okay, but you said you don't know what that license is for, right?

**Sjors Bogers** [12:15:12]: Because I have no experience with license and things like that, but it's 15 million for just having a license, not very

**Sjors Bogers** [12:15:26]: Or is it just a barrier for entry for other people to make it very complicated to it.

**Sjors Bogers** [12:15:31]: That could also case.

**David Orban** [12:15:34]: So there all kinds of barriers.

**David Orban** [12:15:40]: And the capital requirement is a relatively minor barrier.

**David Orban** [12:15:47]: Organizational requirements and compliance requirements higher, but the most important barrier is that just because you satisfy everything that is needed, you may still not get the license.

**David Orban** [12:16:09]: Yeah.

**David Orban** [12:16:09]: So, so tag having been told they will get a license is the most important And then everything else checkbox.

**David Orban** [12:16:23]: Now, whether is a good idea to get the license or not, we'll But what Tag expects is it already has one license.

**David Orban** [12:16:36]: This is another license, and you ask me what it is for, I have no And, and, you know, I will learn and find out in detail this, that other.

**David Orban** [12:16:45]: The proposal for the own short digital asset exchange is again another So there will be always a new But without the digital asset exchange, including the two or however many licenses that we already and the one that we are about to The expectation, let's say by mid next is to earn $10 million per

**David Orban** [12:17:22]: month in commissions.

**David Orban** [12:17:26]: On the volume of business that goes through the entity.

**David Orban** [12:17:35]: So if that is true, then yeah it is a good as long as you have 15 million dollars it is it is absolutely a and do you know where those those 40 50 million come from is it from the same parties that are also the very very interestingly they want proof that you can attract investors rather than they

**David Orban** [12:18:10]: giving you money to be a player who is allowed to sit at the table

**David Orban** [12:18:32]: There's one main investor from Singapore, and then there are, let's say, this is the anchor investor.

**David Orban** [12:18:39]: He put in the first 15 And then there are others that are from the UK, from Nigeria.

**David Orban** [12:18:48]: And, yeah, and I don't remember.

**David Orban** [12:18:53]: Maybe there's another couple.

**David Orban** [12:18:55]: Yeah.

**David Orban** [12:18:56]: But you're not part of these conversations, No, I mean, I mean, I ask and I am given answers, but I am not part of the fundraising effort.

**David Orban** [12:19:10]: Yeah.

**David Orban** [12:19:11]: Yeah.

**David Orban** [12:19:11]: And do you know what type marketing activities they're So until the end of the year, it will be still a soft launch.

**David Orban** [12:19:23]: Because it is all about relationships that are already in place.

**David Orban** [12:19:30]: And there's a lot of jealousy and politics.

**David Orban** [12:19:36]: So I don't know when they will decide that the time is right to be proud loud, maybe or much But until the end of the year, there will be private events that will be organized.

**David Orban** [12:19:59]: in all of the places where there are offices in Abu Dhabi, in London, in New York, etc.

**David Orban** [12:20:08]: with 50 or 100 people invited.

**David Orban** [12:20:13]: then, I don't know, much else.

**Sjors Bogers** [12:20:22]: Correct me if I'm wrong, but usually with these type of funds you, you start with one small fund, you prove that you're capable of growing it, and then the next 10x bigger or five times bigger, you repeat those steps, Yes, now two things.

**David Orban** [12:20:37]: First, I respond to the fund question something that is important.

**David Orban** [12:20:47]: Decisive capital, which is the name of fund.

**David Orban** [12:20:53]: is small, a billion dollars is, is what you is to prove we deploy efficiently and expected good returns.

**David Orban** [12:21:09]: The person who is going to come to manage decisive, her name is Miray, I don't remember the last name, Miray previously deployed 15 So it is small So for her, this small.

**David Orban** [12:21:37]: So that's the first answer.

**David Orban** [12:21:38]: The second answer is that tag, or whatever it is going to be called, does... five, six different things of which investing this capital is just It does investment banking, which means matching companies with investors and earning money It does wealth management and asset management.

**David Orban** [12:22:20]: And I don't know what is the difference?

**Sjors Bogers** [12:22:23]: Asset management is part of wealth Why wealth management is the goal of making the future assets safe, basically.

**Sjors Bogers** [12:22:35]: And you do that by managing some of the assets, right?

**Sjors Bogers** [12:22:39]: So one is a category underneath the umbrella of the other.

**David Orban** [12:22:42]: Makes sense.

**David Orban** [12:22:44]: In the tag org chart, they are at the same Yeah.

**David Orban** [12:22:51]: So head of asset management does not report to the head of wealth management.

**Sjors Bogers** [12:22:57]: Okay.

**David Orban** [12:22:58]: And then there family services, both concierge services to families that want to relocate Singapore or China Africa to Abu Dhabi or other things.

**David Orban** [12:23:19]: I don't know, whatever Then there Alkaf, which is the untangling of the inheritance, right?

**David Orban** [12:23:39]: And then there are the most recent, which sovereign relations.

**David Orban** [12:23:50]: setting up the Pakistani sovereign wealth then probably doing something in the Caribbean for various Caribbean countries.

**David Orban** [12:24:11]: Michael will meet the president of Nigeria.

**David Orban** [12:24:19]: I think in a couple of weeks to discuss a new waterway for the entire country or something.

**David Orban** [12:24:34]: Okay.

**David Orban** [12:24:34]: In partnership with the port of Abu and each of these Pakistani wealth Waterway for Nigeria.

**David Orban** [12:24:53]: Each of these is in the order hundreds of billions, if not trillions of Can you compare that with the, basically the Emirati equivalent to what the Chinese are doing with their new And one thing that you didn't ask and I didn't tell, is, okay, and what is the the likely outcome is that Uram will be

**David Orban** [12:25:30]: acquired by one of the established uh, Emirati banks.

**David Orban** [12:25:40]: Okay.

**David Orban** [12:25:40]: And whether this acquisition will be before or after, it, Yuram also expects to go public on the Emirati stock exchange.

**David Orban** [12:25:53]: And your potential negotiation with either whomever you will negotiate with Michael or the person in HR, etc.

**David Orban** [12:26:04]: I don't Having component in your payment package that is equity.

**David Orban** [12:26:13]: could see an and we are talking about as little as three, four And so that is also something that makes it interesting.

**Sjors Bogers** [12:26:31]: And is those realistic looking at my position in the organization to get equity?

**David Orban** [12:26:38]: I have idea.

**David Orban** [12:26:39]: So in my current agreement there is no because contractors don't get equity and wanted to simplify having a contractor agreement migrate into employment agreement the first opportunity and then I will have bonuses and And, and you should ask.

**David Orban** [12:27:13]: make sure that you Yeah.

**David Orban** [12:27:15]: Don't be shy No, no, I'll ask.

**David Orban** [12:27:18]: word.

**David Orban** [12:27:19]: Okay.

**David Orban** [12:27:22]: And then the worst that can happen is they tell Yeah.

**Sjors Bogers** [12:27:27]: And I'll tell him, okay, what do I need to earn it?

**David Orban** [12:27:30]: Exactly.

**David Orban** [12:27:31]: Perfect.

**David Orban** [12:27:33]: Perfect.

**David Orban** [12:27:34]: Yes.

**Sjors Bogers** [12:27:39]: But wouldn't it be smart in your case to have a hybrid form, just for So that you have a small employment where you get the equity and the rest is contract stuff so you play around with that money and don't get, I don't know what the tax rate is in Italy, but... Yeah, yeah, yeah, I would never pay

**David Orban** [12:27:56]: myself here.

**David Orban** [12:27:58]: Even if I have an employment agreement, I would leave that in Dubai and move here what is needed.

**David Orban** [12:28:12]: Yeah.

**David Orban** [12:28:16]: Okay.

**David Orban** [12:28:16]: Okay.

**David Orban** [12:28:16]: Absolutely.

**Sjors Bogers** [12:28:24]: So, tomorrow I'll make sure to set the Okay, and same You want to tell

**Sjors Bogers** [12:28:40]: Yeah, that Okay.

**David Orban** [12:28:48]: All right.

**Sjors Bogers** [12:28:50]: Okay.

**Sjors Bogers** [12:28:50]: Thanks

---
*Backed up from MeetGeek on 2026-03-30 09:04*
