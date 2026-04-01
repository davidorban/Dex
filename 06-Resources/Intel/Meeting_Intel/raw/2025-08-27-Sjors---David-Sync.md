# Sjors / David Sync

**Date:** 2025-08-27
**Duration:** Unknown
**Meeting ID:** 8f5931dd-7e03-4ddb-ae0b-682429fedfcb

## Participants
- *Participants not listed*

### Summary

The meeting focused on GitHub repository management, addressing challenges such as conflict resolution when multiple developers work on the same files and uncertainties regarding folder synchronization. David was tasked with creating a structured folder system to enhance collaboration, while Sjors was to drag the correct folder into the appropriate repository to resolve synchronization issues. The discussion also highlighted problems with the TagDex repository, including missing content and errors during updates, leading to the decision to implement an extra folder to prevent future data loss. Additionally, the need for physical backups and document iterations was emphasized, with Sjors assigned to generate iterations three and four of the documents, and David to review them later. Task assignments in Asana related to ongoing projects were also discussed, with David responsible for sending payment for the N8M plan as requested by Sjors.

## Full Transcript

**Multiple speakers** [11:02:39]: I'm smoking one how do you call it one pipe full of tobacco per day and maybe it's enough to hmm if I got my lungs I don't know hmm okay so thank you for signing the NDA Yeah, you're welcome I shared the meet geek recordings I created a team and it is not completely clear to me if now everything is

**David Orban** [11:03:19]: automatically shared we will check with this one And I don't know if you had the chance of checking out the the interface and you were able to download what you needed and so on.

**David Orban** [11:03:38]: No, not that.

**David Orban** [11:03:40]: Okay, and then I also shared the tag GitHub repository with you.

**David Orban** [11:03:46]: And I just a few minutes ago realized that I did that before pushing a lot of changes that I made during the past few days without syncing so I just did that before the call yeah I saw the text last night I pushed what I did my iterations to you to the text though not tag DAX the other one Yeah,

**Sjors Bogers** [11:04:19]: yeah, yeah.

**David Orban** [11:04:21]: So, so yeah, we are not in conflict there.

**David Orban** [11:04:25]: Let me actually pull that, and then we can maybe discuss...

**Sjors Bogers** [11:04:34]: And I have a question about the push and pull process, because if I do it to my own repository, it just instantly updates it, but if I send it to you, you have to prove to make the changes or how does that work?

**David Orban** [11:04:49]: No, um, if you push to the main branch, you have the same rights as I do, and, um, it will only alert you if you are creating a conflict with changes that I'm also working on and then there is a granular way where rather than the files being overwritten one or the other line by line we can decide

**David Orban** [11:05:24]: where we want to keep the changes so if as a developer we would be working on the same particular module the same particular file we could still keep what each of us did we would just have to reason about it extensively and And that is not the way to do it.

**David Orban** [11:06:02]: The way to do it is to push your changes to a different branch and then open an issue with a pull request where you describe what is the thing that you did, what are the tests that need to be done, And whoever is responsible then can look at the changes, run the tests, maybe run other tests, and

**David Orban** [11:06:34]: when they are satisfied, they close the pool request by merging your branch into the main branch.

**David Orban** [11:06:45]: So that is how the process works.

**David Orban** [11:06:49]: across potentially dozens or thousands of people and you know, I don't know how many steps this takes at Microsoft or Google, how many automated tools they have, automated testing for sure, but then Exactly the details, right?

**David Orban** [11:07:13]: But this is this is how it works.

**David Orban** [11:07:17]: Okay.

**David Orban** [11:07:17]: And we can decide whether we want to do that or when.

**David Orban** [11:07:20]: In the meantime, what would make sense is to work on maybe particular folders inside the repository.

**David Orban** [11:07:38]: So there could be a David folder and a Shores folder.

**David Orban** [11:07:42]: And that way you could refer to common files.

**David Orban** [11:07:47]: And then based on those common files, you could create files in your folder.

**David Orban** [11:07:52]: And then we could discuss, okay, should the files in your folder be moved in their right place instead?

**David Orban** [11:07:59]: And that is already what I'm doing basically, just not with a human, with the AI, because I'm using for that purpose the temp folder.

**David Orban** [11:08:13]: We could have maybe inside the time folder, we could have David and Shores, and then we know that whatever is inside David and Shores should be somewhere else, for whatever reason.

**David Orban** [11:08:31]: And the algorithmic dependency of everything inside our repository is much loser.

**David Orban** [11:08:43]: than what a traditional program would be so the probability of us breaking something today is close to zero the worst that can happen is that we duplicate some functionality like a given workflow and then when we trigger the workflow the results could vary depending on what version of that

**David Orban** [11:09:14]: functionality the model stumbles upon first.

**David Orban** [11:09:18]: Yeah, right?

**David Orban** [11:09:19]: Something like that.

**David Orban** [11:09:21]: Sometimes it happens to me because I generate templates and then I forget about them and generate similar things or maybe I generate a family of templates and one already existed before but it is now also part of the family so It is now in two ways.

**David Orban** [11:09:43]: And sometimes I run sanity checks.

**David Orban** [11:09:49]: I ask, hey, do you see duplications, and then which is better?

**David Orban** [11:09:56]: And typically, there's no doubt.

**David Orban** [11:10:00]: One of them is much better than the other.

**David Orban** [11:10:02]: And then I say, okay, just keep the best one and the other you can delete.

**David Orban** [11:10:07]: Okay, cool.

**David Orban** [11:10:08]: Yeah, things like that.

**David Orban** [11:10:10]: One of the posts on X that I shared with you is interesting

**David Orban** [11:10:21]: because

**David Orban** [11:10:37]: The risk of being just crazy rather than a genius when you're alone is high.

**David Orban** [11:10:48]: Yeah.

**David Orban** [11:10:50]: Okay, so I stopped myself and this is it, so I will pull all.

**David Orban** [11:11:04]: Let's see what it says.

**David Orban** [11:11:06]: Actually, let me join as usual.

**David Orban** [11:11:36]: Okay,

**David Orban** [11:12:02]: so, um, This was a few days ago.

**David Orban** [11:12:09]: And then I did this right now.

**David Orban** [11:12:14]: It's already up to date.

**David Orban** [11:12:17]: Oh, either you didn't push or you pushed to a different branch, automatically maybe.

**David Orban** [11:12:25]: Okay, so let's look.

**David Orban** [11:12:27]: Actually, let's do this.

**David Orban** [11:12:29]: My, sorry.

**David Orban** [11:12:31]: My friend Shors, S- J-O-R-S, please remember the spelling.

**David Orban** [11:12:39]: He worked on the repository and he says he pushed some changes.

**David Orban** [11:12:47]: Maybe they are on another branch and he didn't create a merge request.

**Sjors Bogers** [11:13:01]: I think I already found the issue.

**David Orban** [11:13:05]: Okay.

**Sjors Bogers** [11:13:07]: Let me paste it here.

**Sjors Bogers** [11:13:09]: I think I just took the wrong folder.

**Sjors Bogers** [11:13:10]: So I did it in your workshop file instead of the tech decks.

**Sjors Bogers** [11:13:17]: Looking at this.

**Sjors Bogers** [11:13:18]: Oh, I understand.

**David Orban** [11:13:19]: Yes.

**Sjors Bogers** [11:13:20]: Here, this is the focus from my terminal.

**David Orban** [11:13:24]: Okay, so you put the... digital asset exchange iteration in the workshop folder.

**Sjors Bogers** [11:13:33]: Yeah, looks like it.

**Sjors Bogers** [11:13:34]: I just made a mistake.

**David Orban** [11:13:36]: Yeah.

**David Orban** [11:13:36]: Okay, no problem, just manually move it to the other one.

**Sjors Bogers** [11:13:54]: Um, I don't think that would work actually because I, I copy the, um, the correct folder from your GitHub, right?

**Sjors Bogers** [11:14:05]: I duplicate it my, uh, local device, right?

**Sjors Bogers** [11:14:10]: And then I created new work, place the folder in there, and then I asked to upload just that folder.

**Sjors Bogers** [11:14:17]: And I just made a mistake there, so wouldn't it be easier to undo the push that I did, and then do it to the correct one?

**David Orban** [11:14:29]: So if you manually move the folder from one repository to the other, both version control systems will be updated.

**David Orban** [11:14:40]: The workshop repository will realize that the folder is missing, and the DAX repository will realize that there is a new folder that appeared, and then you push both.

**Sjors Bogers** [11:14:58]: Yeah, I understand that logic, but I'm not sure if that works with how I did because The folder that I created is not in the tech workshops on my local environment, Yeah, no, I understand, but there is a copy of both repositories in your local environment, isn't that correct?

**David Orban** [11:15:18]: There should be, yeah.

**David Orban** [11:15:19]: Okay, so what I'm saying move it, I literally say drag it in the finder interface.

**David Orban** [11:15:29]: So, so there is, I can show it what I would be doing on my machine, okay?

**David Orban** [11:15:37]: So, here are all the repositories, and then two in particular, and I open another window.

**David Orban** [11:15:45]: Is it too small, or you can see I can see it, okay.

**David Orban** [11:15:49]: So, here is TagDax.

**Sjors Bogers** [11:15:59]: How did you do the same thing twice?

**Sjors Bogers** [11:16:04]: Opening the two windows.

**David Orban** [11:16:07]: Control new, control new, control new.

**David Orban** [11:16:10]: I mean comments, sorry.

**David Orban** [11:16:12]: Just new finder windows on the Mac.

**David Orban** [11:16:15]: This is a, this is the Mac finder.

**Sjors Bogers** [11:16:19]: Yeah, yeah, I know.

**Sjors Bogers** [11:16:23]: Okay.

**David Orban** [11:16:23]: So, sorry, one sec.

**David Orban** [11:16:36]: Darcy, come on.

**David Orban** [11:16:40]: One second, I have to close the door.

**David Orban** [11:16:42]: No worries.

**David Orban** [11:17:00]: Okay, so this is Tag Workshops, this is TagDax.

**David Orban** [11:17:05]: And let's assume that the folder

**David Orban** [11:17:19]: instead of being in workshops, shit.

**David Orban** [11:17:25]: Come on, instead of being in workshops, okay, should be in decks.

**Sjors Bogers** [11:17:34]: Yeah, and the reason I thought it wouldn't work is because I thought that that folder that I pushed to your repository would not be in the wrong place on my local device, but I now checked and I see if and in the wrong place and in the place where I originally worked in in the correct place.

**Sjors Bogers** [11:17:54]: So if I will now drag it.

**Sjors Bogers** [11:17:59]: Because where it went wrong, it's not, I didn't create the folder in the wrong place and then pushed it.

**Sjors Bogers** [11:18:06]: I created in the right place, but then pushed it to the wrong link.

**David Orban** [11:18:12]: Oh, so you told, you told Git to synchronize it with the wrong remote repository.

**Multiple speakers** [11:18:23]: Yeah, so you have two links, one, one workshop and one is your deck.

**David Orban** [11:18:26]: But did you push the entire repository, because that means that now, tag your one, whatever, is... I haven't seen the movie The Fly, but I assume that is what happened.

**Sjors Bogers** [11:18:45]: I think what I did is just take the folder I worked in out of the repository and ask to add that to what you made.

**Sjors Bogers** [11:18:55]: Okay, it's only one folder that should be there, but it's now in the workshop folder and now I'm looking at my local files and I have the the folder in your correct environment that I duplicated there I put my new work.

**Sjors Bogers** [11:19:10]: And then that folder I asked to push to get up, but I used the wrong link.

**Sjors Bogers** [11:19:15]: So it ended up in the wrong file.

**Sjors Bogers** [11:19:16]: And now it's the same exact folder exists in two places, the correct one and the wrong.

**Sjors Bogers** [11:19:21]: So if I drag it into the correct, then you have a duplicate of that folder.

**Sjors Bogers** [11:19:25]: So, okay.

**David Orban** [11:19:26]: So the beauty of Git is that it can address and resolve mass that is much worse than you believe you created.

**David Orban** [11:19:40]: So I'm sure we can we can resolve quickly.

**Sjors Bogers** [11:19:46]: So before you come up with a solution, let me think about it.

**Sjors Bogers** [11:19:53]: So I learned something as well.

**Sjors Bogers** [11:19:54]: Sure.

**Sjors Bogers** [11:19:57]: If I would try to fix this, I would just say yesterday I made a mistake doing the push.

**Sjors Bogers** [11:20:03]: It went this folder, but it had to go to this link.

**Sjors Bogers** [11:20:07]: Then you make this change and then it will delete it.

**Sjors Bogers** [11:20:10]: in all the environments, right?

**David Orban** [11:20:13]: Yeah.

**David Orban** [11:20:14]: Yeah, and in a single prompt, I would both explain and then say what it should do.

**David Orban** [11:20:21]: So I would not only give the wrong or the mistaken repo, but also the correct repo.

**Sjors Bogers** [11:20:29]: Yeah, yeah, of course.

**David Orban** [11:20:30]: Interesting one command, yes.

**David Orban** [11:20:35]: Mm-hmm.

**David Orban** [11:20:35]: You want to go ahead and do that?

**Multiple speakers** [11:20:37]: Yeah, so I'm trying to try to just to see, so here we are, that's right.

**David Orban** [11:20:43]: So we are in workshops and here is the folder that you pushed.

**Sjors Bogers** [11:20:57]: Yeah.

**David Orban** [11:20:57]: In workshops, there is DAX, and that is what should not be there.

**David Orban** [11:21:02]: Yeah.

**David Orban** [11:21:04]: So go ahead and do it.

**Sjors Bogers** [11:21:40]: And the correct folder is GitHub, David Orban, TechDex, right?

**Sjors Bogers** [11:22:06]: Working

**Sjors Bogers** [11:22:37]: Little errors.

**David Orban** [11:22:41]: No, I'm, I'm looking at this is amazing all the time.

**David Orban** [11:22:48]: It comes up with a hallucinated name, what tag stands for.

**David Orban** [11:22:57]: Okay.

**David Orban** [11:22:57]: And, and all my cloud.md files.

**David Orban** [11:23:02]: It's the entrepreneurs group, remember.

**David Orban** [11:23:06]: And I always have to check because says, yeah, whatever, tag.

**David Orban** [11:23:15]: No, I said, give me the change log of this repo and I thought it would see and show the decks change, but doesn't.

**David Orban** [11:23:34]: Okay.

**David Orban** [11:23:34]: Yeah, I don't know why.

**David Orban** [11:23:36]: Okay, so, did it complete on your side?

**Sjors Bogers** [11:23:39]: No, because it gave a lot of errors and now it's trying to redo it again.

**David Orban** [11:23:55]: Okay, but it already did something.

**David Orban** [11:24:05]: It's not here anymore.

**David Orban** [11:24:25]: iteration one, iteration two.

**David Orban** [11:24:27]: And this one is called iterations, plural.

**Sjors Bogers** [11:24:34]: I should before this one.

**David Orban** [11:24:36]: Okay, not yet.

**Sjors Bogers** [11:25:00]: What's

**Sjors Bogers** [11:25:28]: going Still working on it.

**Sjors Bogers** [11:25:33]: Okay, it just said the complete TagDex strategic analysis now properly located at GitHub, David Orban, TagDex, three main short iterations.

**David Orban** [11:25:50]: Oh, short iterations, yes, it's here.

**David Orban** [11:25:53]: Now.

**Sjors Bogers** [11:25:54]: But on my end, it looks like there's just empty folders and no content in the folders anymore.

**David Orban** [11:26:05]: Yep, correct, no content.

**Sjors Bogers** [11:26:08]: I have no clue how that happens.

**David Orban** [11:26:12]: So you believe you don't have it either in one place nor in the other place?

**Sjors Bogers** [11:26:20]: double checking right

**Sjors Bogers** [11:26:27]: So

**Sjors Bogers** [11:26:34]: I have traces of it, but it's all empty folders on both sides.

**David Orban** [11:26:39]: Okay, let me see.

**David Orban** [11:26:40]: So

**David Orban** [11:26:45]: there was a folder up to a few minutes ago in the repository called

**David Orban** [11:26:57]: iterations or something like that.

**David Orban** [11:27:02]: Now it is gone.

**David Orban** [11:27:03]: Can you look in the repo history and recover it?

**David Orban** [11:27:22]: Yep, I can't, oh, no deletions, only additions.

**David Orban** [11:27:34]: Sorry,

**David Orban** [11:27:42]: I...

**David Orban** [11:28:09]: Sorry, I meant that you should check in the history of the remote main branch, not in the local

**David Orban** [11:28:48]: Thank

**David Orban** [11:30:57]: Thank

**David Orban** [11:31:40]: Why

**David Orban** [11:31:50]: did it clean the history?

**David Orban** [11:31:58]: It cleaned the history, that is not ideal, right?

**David Orban** [11:32:05]: Well, not you, your model, your clawed or whatever.

**David Orban** [11:32:12]: There isn't anything to compare because the history was cleaned.

**Multiple speakers** [11:32:15]: Yeah, exactly.

**Sjors Bogers** [11:32:18]: I just copied the situation and I'm trying to troubleshoot here in the chat.

**Sjors Bogers** [11:32:27]: In our conversation here.

**Sjors Bogers** [11:32:29]: I don't know if you noticed.

**David Orban** [11:32:32]: Which chat, sorry?

**David Orban** [11:32:35]: Here the chat on the... Oh, on... So it says, yeah.

**Sjors Bogers** [11:32:41]: Current situation, the four iteration folders.

**Sjors Bogers** [11:32:45]: We were successfully pushed to tech workshops yesterday.

**Sjors Bogers** [11:32:54]: Let's see.

**Sjors Bogers** [11:32:56]: And then as it was trying to undo It only took half of the work and it deleted everything on my local device as well.

**Sjors Bogers** [11:33:08]: And then it said, okay, I see what the problem Um, let me see what's on your local device to recover and now it cannot recover it because it doesn't exist there anymore.

**Sjors Bogers** [11:33:17]: Ah, Jesus.

**Sjors Bogers** [11:33:20]: And why you did this, I have no clue.

**David Orban** [11:33:23]: Of course, of course.

**David Orban** [11:33:25]: Um, all right.

**David Orban** [11:33:32]: Your biological memory is intact.

**David Orban** [11:33:38]: And you could tell it to do whatever you told it to do yesterday.

**David Orban** [11:33:43]: Yeah, and I still have the prompt, right?

**Sjors Bogers** [11:33:44]: So, yeah.

**Sjors Bogers** [11:33:47]: Yeah.

**David Orban** [11:33:47]: So the result will be slightly different for whatever random reasons, but it will go in the same direction.

**Sjors Bogers** [11:33:56]: But.

**Sjors Bogers** [11:33:57]: The stuff that has been completed, as you see in this activity history that you have on screen right now.

**Sjors Bogers** [11:34:05]: Is possible to go back to that or is that just an update message that doesn't contain any of the work?

**David Orban** [11:34:13]: No, as far as I know, the fact that the history has been cleaned makes it so that it is not possible to go back.

**Sjors Bogers** [11:34:24]: Okay.

**David Orban** [11:34:26]: As far as I know, I may be wrong.

**Sjors Bogers** [11:34:32]: Is it worth thinking about preventing this in the future, working with an extra folder or something like Well, sure.

**Sjors Bogers** [11:34:45]: Because now it's just trial and error and it might have been boosted to begin with, but if it's actual work, one.

**David Orban** [11:34:51]: So, so yes, definitely, and yeah, good.

**David Orban** [11:35:09]: Yeah, I don't know.

**David Orban** [11:35:14]: don't know what caused it and why it took this kind crazy decision based on what you told it.

**David Orban** [11:35:23]: No idea.

**David Orban** [11:35:24]: Maybe the word.

**David Orban** [11:35:24]: No, and no idea how to, how to be more careful because it doesn't seem to me that what you said it should do is so dangerous, right?

**David Orban** [11:35:37]: Maybe Maybe we could have actually made a physical copy before, right?

**David Orban** [11:35:47]: The physical folder, like I said.

**David Orban** [11:35:50]: Something like that could be good.

**David Orban** [11:35:52]: To have

**David Orban** [11:35:57]: not only the online backup, but a local backup as well.

**David Orban** [11:36:02]: I actually have that.

**David Orban** [11:36:05]: not of everything but some stuff somewhere you see backup there you go so this is not synchronized remotely and it is a backup and I and I also have backup physically on disks I moderately paranoid Okay, so why don't we do this?

**David Orban** [11:36:35]: You redo the work to generate the iterations three and four, if I'm mistaken, right?

**David Orban** [11:36:44]: One and two are already there, so you generate three and four.

**Sjors Bogers** [11:36:48]: Yeah, but it's not there because it's empty folders.

**David Orban** [11:36:51]: Oh, one and two is empty as well?

**Sjors Bogers** [11:36:55]: Yeah, it's just an empty folder.

**Sjors Bogers** [11:36:58]: So placed the new followers, but there's no documents in it.

**Sjors Bogers** [11:37:02]: And in total it should have been 44 documents and I don't know, 1900 lines.

**David Orban** [11:37:08]: Okay.

**David Orban** [11:37:11]: And do you have the prompts to do everything?

**Sjors Bogers** [11:37:14]: I think I only have the prompt for the last so iteration four.

**David Orban** [11:37:18]: Okay, so sorry, do iteration four.

**David Orban** [11:37:22]: Yeah, can say?

**David Orban** [11:37:24]: And I am... fatalistic enough not to think that one, two, three could have been the gold mine that we are looking for, right?

**David Orban** [11:37:32]: Yeah, that's Yeah.

**David Orban** [11:37:35]: So, generate iteration four.

**David Orban** [11:37:39]: Do it after we speak, and then later in the afternoon I will go and check.

**David Orban** [11:37:47]: Just ping me on WhatsApp when I can, And then just a smaller update.

**David Orban** [11:38:00]: It wasn't explicit and it became explicit yesterday I was expected to be in London too.

**David Orban** [11:38:10]: Okay.

**David Orban** [11:38:11]: So I will be in London and I didn't bring your name up as we agreed.

**David Orban** [11:38:17]: So I will leave September 7 and fly back to Italy September 10. And there will be an event organized by TAG with the Tel Aviv team there as well.

**David Orban** [11:38:34]: And there will be about 50 people, investors, family offices, bunch of startups that are presenting from Israel.

**David Orban** [11:38:46]: And I will have a meeting with IMS, which is a two, I think two billion dollar venture studio, with a very large portfolio of successful companies that they incubated an equity for work model.

**David Orban** [11:39:15]: And they would like us to invest in them, 10 million dollars, I think.

**David Orban** [11:39:26]: And so we will be discussing that.

**David Orban** [11:39:29]: They are also looking forward to setting up in the UAE, and we will be discussing that.

**David Orban** [11:39:35]: And that is on the 8th in the morning.

**David Orban** [11:39:42]: And the event is on the evening of the 9th.

**David Orban** [11:39:48]: And in the middle, I will have some free time to do other things or just to work.

**Sjors Bogers** [11:39:55]: Okay, and to be clear, between the 7th and the 10th, you're going to be in London, right?

**David Orban** [11:40:02]: That is, yes, that, so I fly Sunday the 7th in the afternoon, and I am back I think Thursday the 10, whatever it is, also in the afternoon, yes.

**Sjors Bogers** [11:40:22]: Okay, that means we have, what, 20 days, is that correct, no, it's less, it's 10 days, to do For me to figure out if I can maybe talk to Brad sooner.

**Multiple speakers** [11:40:43]: But he wanted to do it face to face, right?

**Sjors Bogers** [11:40:46]: Yeah, but if it keeps being postponed all the time.

**Sjors Bogers** [11:40:50]: Maybe I should just bring it up and see if I can join you guys in London anyway.

**David Orban** [11:41:02]: Yeah, of course.

**David Orban** [11:41:04]: And I don't have full visibility on Michael's calendar.

**David Orban** [11:41:10]: So it could be that he says, sorry, I don't have time now.

**Sjors Bogers** [11:41:18]: Yeah, I understand.

**David Orban** [11:41:20]: But, you know, we can check when you Yeah.

**Sjors Bogers** [11:41:26]: Yeah, yesterday in a call with Mike and Brad about AccuFy.

**Sjors Bogers** [11:41:31]: Brad again said that the transfer hadn't happened.

**Sjors Bogers** [11:41:35]: The funds didn't happen.

**Sjors Bogers** [11:41:37]: He was expecting that day or tomorrow.

**Sjors Bogers** [11:41:40]: I didn't hear anything yesterday and I will be speaking to him his morning in a few hours, in three hours from So if it's going to be today, it probably wouldn't have happened because so early.

**Multiple speakers** [11:41:54]: And maybe I hear something from Well, it also depends where the guy is.

**David Orban** [11:41:59]: Isn't he all the time in Singapore too?

**Sjors Bogers** [11:42:02]: Yeah, not in Singapore, but he's constantly on the move.

**David Orban** [11:42:06]: If he's in Asia, it's already evening.

**David Orban** [11:42:11]: But, you know, it doesn't matter.

**David Orban** [11:42:13]: So,

**David Orban** [11:42:20]: so, um, So what you are saying is, your preference would have been to talk to Brad face to face in Turkey or in Dubai.

**David Orban** [11:42:31]: But given that nothing is happening day after day, week after week, you are deciding to talk to him online instead.

**Sjors Bogers** [11:42:44]: I think so.

**David Orban** [11:42:45]: Yeah.

**David Orban** [11:42:45]: Okay.

**David Orban** [11:42:46]: All right.

**David Orban** [11:42:48]: So if you are able to do that this week, Then we have basically the entire next week to see if Michael is still

**David Orban** [11:43:14]: with the conversation.

**David Orban** [11:43:15]: I'm sure it will be very cathartic in the sense that it is something you want to do and it is not even about the outcome, it is just to have exactly.

**David Orban** [11:43:33]: Yeah.

**David Orban** [11:43:35]: So I'm looking forward to your update about the iteration.

**David Orban** [11:43:42]: Yes.

**David Orban** [11:43:44]: And feel free assign yourself tasks in Asana,

**David Orban** [11:43:57]: So that things that are hanging in the air like NA10 or other things or looking at the links that I share with you that we need to revisit maybe or not forgotten.

**David Orban** [11:44:09]: And while you are doing that, feel free to assign tasks to me as well, stuff that you think I should be doing.

**David Orban** [11:44:17]: Okay?

**Sjors Bogers** [11:44:19]: All right.

**Sjors Bogers** [11:44:20]: About N8M.

**Sjors Bogers** [11:44:22]: Originally, I had about a week to test that's a free trial, right?

**Sjors Bogers** [11:44:28]: And that has run out, so I won't be able to do anything unless I get a plan on adding.

**David Orban** [11:44:33]: that's fine.

**David Orban** [11:44:35]: Just tell me how much and I will send you the Thank All right, bye-bye.

**Sjors Bogers** [11:44:43]: All right, and tomorrow we didn't decide on... Oh, sorry.

**David Orban** [11:44:50]: Yeah, same time.

**Sjors Bogers** [11:44:52]: Yeah, that works.

**Sjors Bogers** [11:44:54]: Okay, see I'll try not to mess up.

**David Orban** [11:44:59]: You can blame the models.

**Sjors Bogers** [11:45:00]: It's... Yeah, I'm pretty sure it's a user error at this Yeah, okay, bye.

**Sjors Bogers** [11:45:07]: Thanks,

---
*Backed up from MeetGeek on 2026-03-30 09:02*
