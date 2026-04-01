# Knowledge Transfer MVP for WebSummit - Bug bash 3

**Date:** 2025-11-06
**Duration:** Unknown
**Meeting ID:** 5cff559f-bdfe-46f5-8fca-bd9c4b2bdf97

## Participants
- *Participants not listed*

### Summary

The meeting focused on several key areas, including the organization of a bug bash for improved issue tracking, challenges in reproducing product bugs, and difficulties with the interview generation process, particularly regarding email notifications and status updates. Participants raised concerns about sign-in issues on Safari, tracking interview progress, and file upload problems, emphasizing the need for better user permissions and system functionality. Security vulnerabilities related to file uploads were discussed, alongside the necessity for budget limits on token processing. The group also addressed enhancing the interview process for better engagement and clarity, with suggestions for optimizing question quality and implementing confirmation prompts during knowledge transfer sessions. Finally, plans were made for testing voice interviews and creating a custom interview for an upcoming conference to gather user feedback.

## Full Transcript

**Panagiotis Apostolidis** [15:00:11]: Hello.

**Daniel Nowak** [15:00:42]: Hey, hello.

**Martine Haug Olsen** [15:00:55]: Hi,

**Angus Blewett** [15:00:59]: everyone.

**Angus Blewett** [15:01:03]: Yo, I'm

**Maciek Kowalski** [15:01:04]: about to merge the last fix.

**Maciek Kowalski** [15:01:10]: Adam, do you know if the chat still send start, or this has change to empty string or something.

**Adam Petroff** [15:01:16]: Yeah, it's still since start.

**Adam Petroff** [15:01:18]: Okay,

**Maciek Kowalski** [15:01:18]: fantastic.

**Maciek Kowalski** [15:01:19]: Thank you.

**Maciek Kowalski** [15:02:22]: Hello,

**Lachezar Kozhuharov (Lacho)** [15:02:22]: everybody.

**Lachezar Kozhuharov (Lacho)** [15:02:23]: How

**Marco Bettiolo** [15:02:23]: is

**Marco Bettiolo** [15:02:32]: Martin on the call.

**Marco Bettiolo** [15:02:34]: Yeah, Martin.

**Martine Haug Olsen** [15:02:35]: I think we

**Marco Bettiolo** [15:02:36]: have too many browsers listed there.

**Marco Bettiolo** [15:02:38]: Okay,

**Martine Haug Olsen** [15:02:39]: we can remove some of the

**Marco Bettiolo** [15:02:40]: space for people.

**Marco Bettiolo** [15:02:40]: I just

**Martine Haug Olsen** [15:02:41]: listed the most.

**Martine Haug Olsen** [15:02:42]: Well, it's quite big and the things are quite small.

**Martine Haug Olsen** [15:02:46]: You can size it as you want.

**Martine Haug Olsen** [15:02:48]: So I'm sure there will be space.

**Martine Haug Olsen** [15:02:50]: But yeah, we can remove one of them or two of them.

**Martine Haug Olsen** [15:02:54]: I just put the most common ones.

**Martine Haug Olsen** [15:02:56]: Maybe if a lot of people use the same.

**Martine Haug Olsen** [15:02:57]: It will be a lot of people.

**Martine Haug Olsen** [15:03:04]: I think most importantly you put on the correct

**Marco Bettiolo** [15:03:11]: flow,

**Martine Haug Olsen** [15:03:12]: because it's going to be much easier to go through all the tickets in case somebody puts duplicated ones.

**Martine Haug Olsen** [15:03:18]: Yeah, it was like two times save time reviewing.

**Martine Haug Olsen** [15:03:23]: So

**Marco Bettiolo** [15:03:24]: do you want to explain

**Martine Haug Olsen** [15:03:26]: the board so everybody

**Marco Bettiolo** [15:03:27]: can understand what you were talking about.

**Martine Haug Olsen** [15:03:29]: Yeah, should I share screen?

**Martine Haug Olsen** [15:03:32]: I don't know if everybody's in the board yet.

**Martine Haug Olsen** [15:03:34]: I don't see any arrows except Marcos, but I just split the board up a bit, because I saw that we spent a lot of time going through all the issues on the previous boards because we don't have any structure.

**Martine Haug Olsen** [15:03:50]: So now it's structured by flows and starting by the first flow, so and going through.

**Martine Haug Olsen** [15:03:55]: So at the top you have like creating organization onboarding, creating and sending interviews and next, accessing the interview and the onboarding flow there.

**Martine Haug Olsen** [15:04:05]: chat into your experience, voice, voice, voice, voice, voice, voice, and then, you can see here, what browser you use.

**Martine Haug Olsen** [15:04:16]: Yeah, and I think it should be fine.

**Martine Haug Olsen** [15:04:18]: If it's gonna be less space, just minimize, like, I mean, you can make the sizes as small as you want on the print screens and stuff, and we can zoom a lot in the sports, so I don't think it's gonna be an issue, but yeah.

**Martine Haug Olsen** [15:04:30]: And I put Slackbot on the edge, I don't know if we're supposed to test that too.

**Martine Haug Olsen** [15:04:34]: in this bug brush or not, but in case somebody's testing slash what you can put it there in that column.

**Martine Haug Olsen** [15:05:04]: So

**Marco Bettiolo** [15:05:15]: as always, I share the link to the product in the Google meet.

**Marco Bettiolo** [15:05:23]: You have the link to the Figma board to report the bugs as Martin explained.

**Marco Bettiolo** [15:05:27]: If you have problems using the Figma board there is the KT bug bash channel where you can report the bugs there.

**Marco Bettiolo** [15:05:34]: The goal of this is to register on the, on the organization, run some interviews, do a subjective evaluation of the quality of the question of the question of the question.

**Marco Bettiolo** [15:05:56]: the then to test is the voice is the voice, I should be like.

**Marco Bettiolo** [15:06:07]: Yeah, it should

**Maciek Kowalski** [15:06:12]: be like.

**Maciek Kowalski** [15:06:13]: Okay.

**Marco Bettiolo** [15:06:15]: And if you have any questions or problems at any time.

**Marco Bettiolo** [15:06:20]: Let's say we're gonna do about until.

**Marco Bettiolo** [15:06:24]: Let see, let's see, until maybe quarter to five, well, let's say the next 40, 45 minutes.

**Marco Bettiolo** [15:06:36]: So, yeah, if you have any questions, any challenges, any problems, any uncertainties, any information just ask, so we can support you.

**Marco Bettiolo** [15:06:51]: Is everybody clear, what is the first time, and I'm sure I would, but I'm actually driving.

**Marco Bettiolo** [15:07:02]: So,

**David Orban** [15:07:04]: David, I think this is the first time, and I'm sure I would, but I'm actually driving.

**David Orban** [15:07:09]: So, for

**Marco Bettiolo** [15:07:11]: the next 15

**David Orban** [15:07:12]: minutes or so, I'm not gonna be able to do much.

**David Orban** [15:07:15]: But I'm happy to keep your company.

**David Orban** [15:07:19]: Yeah,

**Marco Bettiolo** [15:07:19]: once you get to a place where you can.

**Marco Bettiolo** [15:07:22]: You can use the browser on mobile or on the desktop and test the product.

**Marco Bettiolo** [15:08:17]: Ah, Monica, are we ready to get people to review the landing page

**Marco Bettiolo** [15:08:27]: as

**Monika Nowak** [15:08:30]: well.

**Maciek Kowalski** [15:09:00]: I need to say that work, animation, and everything.

**Ben Peeri** [15:09:06]: So sweet, like, I am.

**Ben Peeri** [15:09:11]: Is

**Lachezar Kozhuharov (Lacho)** [15:09:26]: it

**Marco Bettiolo** [15:09:26]: reproduceful.

**Ben Peeri** [15:09:30]: I'm trying and I'm trying to reproduce itself one time.

**Ben Peeri** [15:09:35]: So I went to the page, it chose the list.

**Ben Peeri** [15:09:38]: Then there was an action of refresh on the page and then got corrupted.

**Ben Peeri** [15:09:42]: And I didn't have developer mode open.

**Ben Peeri** [15:09:45]: I opened it and now I'm trying to replicate it and it doesn't happen again.

**Ben Peeri** [15:09:48]: So I'm not sure.

**Ben Peeri** [15:09:50]: I get

**Adam Petroff** [15:09:51]: it once as well, actually, but now I refresh and it doesn't happen anymore.

**Ben Peeri** [15:09:57]: Yeah, it comes and goes like maybe there is another server on the file almost like that doesn't have the state.

**Ben Peeri** [15:10:10]: It's like you usually see this type of thing like when you have a Kubernetes and it's not stateless.

**Ben Peeri** [15:10:15]: And like, you hit, I may

**Lachezar Kozhuharov (Lacho)** [15:10:17]: the code for one of the code for one node and the node is how

**Ben Peeri** [15:10:18]: we use another one.

**Lachezar Kozhuharov (Lacho)** [15:10:20]: Yeah, we merged the QPRs right before this.

**Lachezar Kozhuharov (Lacho)** [15:10:22]: So I'm wondering if it got redeployed maybe that's why.

**Ben Peeri** [15:10:27]: Can you say that again, sorry?

**Ben Peeri** [15:10:28]: We

**Lachezar Kozhuharov (Lacho)** [15:10:28]: merged a couple of well, I merged a couple of PRs right before the bugbush.

**Lachezar Kozhuharov (Lacho)** [15:10:34]: So it's possible that it's been redeploying just now.

**Ben Peeri** [15:10:38]: Okay, that will explain that yeah.

**Ben Peeri** [15:10:40]: Yeah.

**Ben Peeri** [15:10:42]: Okay, cool, thank you.

**Ben Peeri** [15:10:45]: Emails don't

**Panagiotis Apostolidis** [15:10:46]: work, maybe we don't have the quota from recent.

**Panagiotis Apostolidis** [15:10:52]: So we are hitting the limit because we are all signing in.

**Panagiotis Apostolidis** [15:10:55]: They

**Daniel Nowak** [15:10:56]: did.

**Daniel Nowak** [15:10:56]: I just created an interview and got an invite.

**Panagiotis Apostolidis** [15:11:01]: I mean, authentication emails maybe.

**Martine Haug Olsen** [15:11:15]: My mind never finishes to generate to generate,

**Valerio Francescangeli** [15:11:20]: to see, it is changed to read.

**Martine Haug Olsen** [15:11:25]: The status is changed already.

**Martine Haug Olsen** [15:11:28]: So it seems like the same issue that we had last time with the test of the same issue that we had last time we tested that it doesn't manage to handle a lot of people maybe at the same time.

**Martine Haug Olsen** [15:11:44]: Yeah, I've received

**Daniel Nowak** [15:11:45]: it, when the status changed to invite.

**Martine Haug Olsen** [15:11:49]: Yeah, if it's changed and invited.

**Martine Haug Olsen** [15:11:50]: It means that it's created interview successfully and it's, yeah, it's ready and you should receive the invite.

**Martine Haug Olsen** [15:11:57]: But I've been stuck on generating for a very long time.

**Martine Haug Olsen** [15:12:00]: Usually it's quite fast.

**Martine Haug Olsen** [15:12:04]: So something is going on.

**Angus Blewett** [15:12:17]: Um, yeah, on generating the invite.

**Angus Blewett** [15:12:21]: It took like three minutes, and then the email came through.

**Angus Blewett** [15:12:24]: So I'll just work through the interview now.

**Martine Haug Olsen** [15:12:28]: Okay, so maybe it's just a, is it, did anyone back in people?

**Martine Haug Olsen** [15:12:32]: Is it handling requests like after each other?

**Martine Haug Olsen** [15:12:35]: So it will do like first one person and then the other and like.

**Martine Haug Olsen** [15:12:39]: No,

**Lachezar Kozhuharov (Lacho)** [15:12:41]: until it should be multi-traded.

**Lachezar Kozhuharov (Lacho)** [15:12:45]: I'm not seen any errors related to, well, I'm not seen any errors actually in the back end.

**Martine Haug Olsen** [15:12:50]: So maybe mine is just super slow then.

**Martine Haug Olsen** [15:12:53]: And it seems like it's waiting for the other to finish before, since it's so slow.

**Ben Peeri** [15:12:59]: So yeah, I also try to create a new interview and it's like it's stuck in and getting everything ready for you for like five minutes now.

**Ben Peeri** [15:13:13]: Oh, it's finally completed.

**Ben Peeri** [15:13:14]: It just took a while.

**Ben Peeri** [15:13:21]: For

**Mariam Khachatryan** [15:13:21]: me, when I created the interview and copy the link.

**Mariam Khachatryan** [15:13:24]: When I open the link, it's showing that it's completed.

**Ben Peeri** [15:13:30]: So we send the email to the invite to the person before the interview questions are already.

**Ben Peeri** [15:13:36]: I think we invoke this send the minute we are generating the interview.

**Ben Peeri** [15:13:41]: Maybe the email, sending to the customer should be delayed by five minutes.

**Ben Peeri** [15:13:45]: So you have enough time to populate the questions before the person gets the email, go to the website and then you have to wait for the interview to be ready.

**Panagiotis Apostolidis** [15:13:55]: It's

**Martine Haug Olsen** [15:13:56]: supposed to be sent only when the questions are ready.

**Lachezar Kozhuharov (Lacho)** [15:14:00]: Yeah.

**Panagiotis Apostolidis** [15:14:02]: It's a task that happens right after the questions are generated in a bucket.

**Panagiotis Apostolidis** [15:14:07]: Yeah, so why is it still

**Ben Peeri** [15:14:09]: showing me when I go in that interview is not ready.

**Ben Peeri** [15:14:12]: Is something else building?

**Ben Peeri** [15:14:14]: Can

**Panagiotis Apostolidis** [15:14:14]: you phrase

**Ben Peeri** [15:14:18]: the page?

**Ben Peeri** [15:14:19]: It finished like three seconds ago, but like I generate an interview for myself.

**Panagiotis Apostolidis** [15:14:27]: Oh.

**Adam Petroff** [15:14:34]: So

**Ben Peeri** [15:14:35]: I went in, I'll generate an interview for my other mailbox.

**Ben Peeri** [15:14:39]: The two seconds after generating that I went into that interview.

**Ben Peeri** [15:14:45]: And it shows that it's still processing the interview.

**Ben Peeri** [15:14:52]: Let me, I can do a screenshot if you want.

**Ben Peeri** [15:14:58]: Maybe adding a

**Panagiotis Apostolidis** [15:14:58]: small delay.

**Panagiotis Apostolidis** [15:15:01]: It will do the For me,

**Mariam Khachatryan** [15:15:03]: it's created, send it, but when I'm opening the link, it's showing completed.

**Mariam Khachatryan** [15:15:09]: And when I'm going inside of the interview, it says that there is no conversation history.

**Mariam Khachatryan** [15:15:14]: It

**Adam Petroff** [15:15:18]: seems

**Mariam Khachatryan** [15:15:18]: it not generate the questions, but send the invite.

**Mariam Khachatryan** [15:15:23]: No,

**Martine Haug Olsen** [15:15:23]: that's correct.

**Martine Haug Olsen** [15:15:25]: Actually, you're not supposed to see the questions there.

**Martine Haug Olsen** [15:15:28]: The old UI that we've had was wrong.

**Martine Haug Olsen** [15:15:31]: So now it is no conversation history because the user, the lever person hasn't answered anything.

**Martine Haug Olsen** [15:15:37]: Once you answer something that place will be populated with the question and the answer.

**Mariam Khachatryan** [15:15:42]: Okay then why the link showing that it's completed?

**Martine Haug Olsen** [15:15:47]: Which link are you referring to?

**Mariam Khachatryan** [15:15:50]: Can I just create the interviews

**Martine Haug Olsen** [15:15:52]: one?

**Martine Haug Olsen** [15:15:56]: I

**Mariam Khachatryan** [15:15:57]: just create interview, and it is, and it's sent email to me and I'm open with this, and it says that it's completed.

**Martine Haug Olsen** [15:16:05]: Okay, I won't be able to access your interview because I can't go.

**Martine Haug Olsen** [15:16:15]: I mean, to be plugged in as you.

**Martine Haug Olsen** [15:16:17]: But please make screenshots and explain like the steps you did

**Mariam Khachatryan** [15:16:21]: to

**Martine Haug Olsen** [15:16:21]: produce it.

**Adam Petroff** [15:16:23]: I'll check the database at least to see what's the status of the interview.

**Mariam Khachatryan** [15:16:32]: It's invited, showing invited.

**Adam Petroff** [15:16:35]: It's showing ready.

**Adam Petroff** [15:16:37]: So if you go to the link, it should send you to onboarding.

**Mariam Khachatryan** [15:16:44]: Yeah, let me check one thing and I will answer your question.

**Mariam Khachatryan** [15:17:39]: Is the

**Ben Peeri** [15:17:39]: finished response, and you think we just added to the voice interview.

**Mariam Khachatryan** [15:17:46]: You know what is the strangest thing that when I'm opening it with Chrome, it's working.

**Mariam Khachatryan** [15:17:52]: When I'm opening it with Safari, it says that it is completed.

**Adam Petroff** [15:17:57]: And are you logged in with the same user?

**Adam Petroff** [15:18:00]: Yes.

**Adam Petroff** [15:18:05]: Can you share a screenshot?

**Mariam Khachatryan** [15:18:11]: Thank

**Ben Peeri** [15:18:38]: you.

**Maciek Kowalski** [15:19:20]: So I don't see, I don't see any errors in the back end.

**Maciek Kowalski** [15:19:25]: Same, I have the same problem.

**Maciek Kowalski** [15:19:30]: It's just generating.

**Maciek Kowalski** [15:19:32]: And did you check your emails.

**Maciek Kowalski** [15:19:33]: Cause I got an email,

**Martine Haug Olsen** [15:19:36]: even though it was still, just generating.

**Lachezar Kozhuharov (Lacho)** [15:19:39]: And did you check your emails because I got an email, even though it was still kind of showing a generating, then when I refreshed it, it wasn't generating.

**Martine Haug Olsen** [15:19:48]: I did not receive an email either, so that, we cannot see

**Maciek Kowalski** [15:19:53]: like, that there is no like Q, the, everything is in the, we cannot see like, that there is like item, any item in the database that this is being generated just in the runtime, right.

**Adam Petroff** [15:20:20]: Miriam, did you share the screen is.

**Adam Petroff** [15:20:54]: So

**Marco Bettiolo** [15:20:55]: on Safari, I cannot sign in, I cannot sign in, I will sign it out and now

**Marco Bettiolo** [15:21:07]: I cannot sign in anymore on Safari.

**Marco Bettiolo** [15:21:08]: I'll try.

**Marco Bettiolo** [15:21:09]: I haven't signed out again from somewhere.

**Valerio Francescangeli** [15:21:16]: I'll try.

**Valerio Francescangeli** [15:21:18]: haven't signed out yet.

**Valerio Francescangeli** [15:21:20]: Maybe I should let me just sign in again from somewhere else.

**Valerio Francescangeli** [15:21:23]: and I know, and I'm going to

**Valerio Francescangeli** [15:21:52]: I was able to use Safari, Valeria?

**Marco Bettiolo** [15:22:08]: Yes.

**Marco Bettiolo** [15:22:10]: I get a forever spinner, so I know what what to

**Valerio Francescangeli** [15:22:23]: I am using Safari 26. So far it

**Panagiotis Apostolidis** [15:22:46]: works from me, I just, I just tried

**Valerio Francescangeli** [15:22:51]: I've recorded something, for the on board thing, where, I don't go away, when I, when I lose focus.

**Valerio Francescangeli** [15:23:08]: I don't know how.

**Valerio Francescangeli** [15:23:10]: My priority it is, but it is kind of knowing that, need to pretty much use the mouse.

**Valerio Francescangeli** [15:23:16]: If I use tab, it's just, it's there forever.

**Valerio Francescangeli** [15:24:14]: Thank

**Adam Petroff** [15:25:31]: Thank

**Adam Petroff** [15:26:10]: Thank

**Valerio Francescangeli** [15:28:16]: I've generated another interview, I'll link for another person, and that one went straight through.

**Valerio Francescangeli** [15:28:22]: But the first one I created, it was like 20 minutes ago.

**Valerio Francescangeli** [15:28:27]: It's still stuck on generating.

**Valerio Francescangeli** [15:28:29]: Can

**Rana Muhammad Usama** [15:28:45]: you share the invitation with

**Rana Muhammad Usama** [15:29:19]: Was

**Ben Peeri** [15:29:19]: there any thought about, I think about that.

**Ben Peeri** [15:29:21]: It's like, I'm talking about.

**Ben Peeri** [15:29:23]: It's like, I'm talking about, I'm like, I'm talking to that thing.

**Ben Peeri** [15:29:28]: I'm like, I'm talking to that thing.

**Ben Peeri** [15:29:30]: I'm like, I'm

**Charlie Patterson** [15:29:31]: talking to that.

**Charlie Patterson** [15:29:31]: I'm like, how

**Ben Peeri** [15:29:32]: is it's going to take another four hours, eight hours.

**Ben Peeri** [15:29:36]: Like, I don't have any tracking.

**Ben Peeri** [15:29:38]: And like, I found myself getting pissed after a few minutes.

**Ben Peeri** [15:29:40]: Like, I'm like, I don't have any, any tracking.

**Ben Peeri** [15:29:45]: And like, I found myself getting pissed after a few minutes, Okay, so, how many more questions are going to be, will I be able to finish it before my next meeting, blah, blah, blah, blah.

**Ben Peeri** [15:29:56]: Like, I need some more Germanistic information about the interview.

**Panagiotis Apostolidis** [15:30:07]: If you click and session, you can see how many of the answer, and how many there are left.

**Panagiotis Apostolidis** [15:30:12]: It count

**Ben Peeri** [15:30:13]: in the wrong way.

**Ben Peeri** [15:30:14]: So it shows us one.

**Ben Peeri** [15:30:16]: I just dropped a message about that.

**Ben Peeri** [15:30:19]: But I don't know, how many more I have left you, so.

**Charlie Patterson** [15:30:24]: Yeah, for sure.

**Charlie Patterson** [15:30:25]: We need to work on train progress and figure out how to do that.

**Ben Peeri** [15:30:35]: the list.

**Ben Peeri** [15:30:35]: Federico, it was stuck to me on zero.

**Ben Peeri** [15:30:38]: But then like I, there was one question, all of a sudden, he jumped So I wonder why was always zero.

**Ben Peeri** [15:30:45]: And like, one of the questions, he decided to kind of like how.

**Ben Peeri** [15:30:49]: And the rest is just completely ignored on the counting.

**Ben Peeri** [15:30:56]: Yeah, that's

**Federico Rampazzo** [15:30:57]: different from how it was behaving in the previous bugbash.

**Federico Rampazzo** [15:30:59]: So yeah, it looks like a regression.

**Adam Petroff** [15:31:03]: You're talking about the number of answered questions in the top?

**Adam Petroff** [15:31:07]: Yeah.

**Adam Petroff** [15:31:09]: Yeah, I think it's not counting the question in until you answer all the follow-ups to that question.

**Adam Petroff** [15:31:20]: I

**Federico Rampazzo** [15:31:20]: think, yeah,

**Adam Petroff** [15:31:25]: because like, if you say something in an answer, it kind picks some like kind of questions out of that.

**Adam Petroff** [15:31:35]: And yeah, I think we need to fix how it is counting.

**Valerio Francescangeli** [15:32:39]: Thank you.

**Valerio Francescangeli** [15:32:39]: Thank

**Ben Peeri** [15:33:12]: Can anyone answer my question on the files?

**Ben Peeri** [15:33:14]: How can I see the list of files uploaded to the interview?

**Ben Peeri** [15:33:18]: How can I delete a file if I accidentally uploaded the wrong file.

**Lachezar Kozhuharov (Lacho)** [15:33:42]: I don't go, no, I don't, I think there, did we scrap the list of files or is is it bug that it's missing.

**Ben Peeri** [15:33:54]: I accidentally uploaded a picture of my, my, my, my, my, I'm naked baby in the shower and oops, I need to delete that.

**Ben Peeri** [15:34:01]: I don't want it in the chat, but.

**Ben Peeri** [15:34:08]: It's not only that the user cannot see the files.

**Ben Peeri** [15:34:11]: Can delete them, can see them.

**Ben Peeri** [15:34:14]: Can see them.

**Ben Peeri** [15:34:15]: Can see them.

**Ben Peeri** [15:34:16]: Like, I don't think HR should be able to see those files.

**Ben Peeri** [15:34:25]: Like I don't think HR should be able to see those files, but they should be able to delete files or clear files.

**Ben Peeri** [15:34:38]: These files can also be used to poison the bot.

**Ben Peeri** [15:34:42]: Yeah, yeah, yeah, mean, please report the

**Lachezar Kozhuharov (Lacho)** [15:34:59]: bug and I guess we'll fix it.

**Lachezar Kozhuharov (Lacho)** [15:35:03]: It's

**Ben Peeri** [15:35:04]: not just, I think you need to scrape for content is basically

**Lachezar Kozhuharov (Lacho)** [15:35:14]: what we do here as well.

**Lachezar Kozhuharov (Lacho)** [15:35:27]: Because the knowledge base is.

**Lachezar Kozhuharov (Lacho)** [15:35:30]: a sense say, replica.

**Ben Peeri** [15:35:55]: I don't.

**Ben Peeri** [15:35:56]: I don't, I would just able to upload some poems.

**Ben Peeri** [15:35:58]: So there is a problem.

**Ben Peeri** [15:36:30]: So,

**David Orban** [15:36:30]: I just answered three, four questions in the session.

**David Orban** [15:36:50]: The interface said, thank, thank.

**David Orban** [15:36:52]: The only the first turn was shown, question.

**David Orban** [15:36:55]: And then I went back again.

**David Orban** [15:37:00]: The first turn was shown, question and then I went back again.

**David Orban** [15:37:07]: I was shown question and then I went back again now for a second time.

**David Orban** [15:37:15]: And the entire conversation was shown.

**David Orban** [15:37:18]: So probably just due to a delay, it was confusing.

**Ben Peeri** [15:39:54]: So, I was trying to upload, I'm going

**Ben Peeri** [15:40:03]: to upload, I'm to, but files shared, has not increased count to my, so I'm going to, so, I'm going to, I don't know if that, I'm going to, I'm going to What,

**Adam Petroff** [15:40:26]: what, what,

**Ben Peeri** [15:40:31]: what,

**Ben Peeri** [15:40:38]: it did give me upload successful when I try that.

**Ben Peeri** [15:40:43]: I'll try that.

**Ben Peeri** [15:40:45]: I'll try it yourself.

**Valerio Francescangeli** [15:40:47]: I'm having a somewhat similar issue.

**Valerio Francescangeli** [15:40:51]: It says two questions answer is two questions answered.

**Valerio Francescangeli** [15:40:58]: Yeah, I don't know.

**Valerio Francescangeli** [15:41:02]: I'll start refreshing when it says two.

**Adam Petroff** [15:41:09]: Can you share your interview ID.

**Valerio Francescangeli** [15:41:15]: And once, I even try to send back exactly what the answer was, and it was okay with It was like, oh, that's a really interesting thing that you say.

**David Orban** [15:41:29]: So I was able to Attach an image to your conversation.

**David Orban** [15:41:36]: And then, uh, the model says, I'm a tagged space the AI and cannot, I am cannot see or process and.

**David Orban** [15:41:54]: And so if it can upload

**David Orban** [15:42:10]: images, then the model should not claim.

**David Orban** [15:42:19]: Yeah,

**Adam Petroff** [15:42:20]: so the way it currently works is you.

**Adam Petroff** [15:42:23]: The agent doesn't really see the files that you upload They are passed to the final replica, which is then available in select.

**Adam Petroff** [15:42:35]: Yeah, we kind of want it to make the agent see the files, but it was kind of more complex.

**Adam Petroff** [15:42:41]: So, because the MVP time limitation, we just opted for this simpler approach.

**Adam Petroff** [15:42:50]: But in the future, I think it would be for sure good for the agent to be available to be mindful of the files.

**David Orban** [15:43:15]: Okay, so when I click on the home button with a session open, there is a, the indication that it works, but it doesn't, it does nothing.

**David Orban** [15:43:28]: It says overview, but when I click nothing.

**Adam Petroff** [15:43:48]: Yeah, we should probably hide that icon, because the the lever, the interviewer actually doesn't is, they just have the interview.

**David Orban** [15:44:07]: Now, when I end the session, it says four questions answered in progress.

**David Orban** [15:44:13]: So this is also delayed.

**David Orban** [15:44:17]: per degree that will confuse the interviewe.

**Ben Peeri** [15:44:43]: Adam, do we have to go.

**Ben Peeri** [15:44:48]: I

**David Orban** [15:45:05]: have to go, but this was fun.

**David Orban** [15:45:06]: Thank you.

**Ben Peeri** [15:46:08]: Charlie, are you

**Ben Peeri** [15:46:23]: Does the, if, we, if we, do we have any limit on tokens on what the user, like, is there.

**Ben Peeri** [15:46:35]: We don't want an interviewer to be longer than X amount of tokens.

**Ben Peeri** [15:46:39]: And the angle I'm asking that that because we don't look at file size that we are uploading.

**Ben Peeri** [15:46:46]: But I don't think that file size is the only thing that we need to look Because if I'm gonna upload text file that is two megs, embedding that text file is gonna cost an arm and a leg because it is so big and have so much content.

**Ben Peeri** [15:47:01]: So I can do an economical attack by upload in a lot of text files.

**Ben Peeri** [15:47:09]: Yeah, that's a very point.

**Ben Peeri** [15:47:13]: It's also a problem.

**Federico Rampazzo** [15:47:24]: It's a very good point.

**Federico Rampazzo** [15:47:25]: And it's also a problem that we since say I think we are not really preventing people from, we are not protecting ourselves from that kind of attack.

**Federico Rampazzo** [15:47:34]: But if you think about that,

**Ben Peeri** [15:47:35]: like an employee that is living is not always a happy person.

**Ben Peeri** [15:47:42]: Like I'm gonna show those guys, I'm gonna make them pay.

**Ben Peeri** [15:47:47]: Yeah,

**Adam Petroff** [15:47:47]: honestly, we didn't spend much time and energy worrying about security because for now we're trying to just make it is so that is so that we can make a nice demo on the web summit.

**Ben Peeri** [15:48:01]: No, for the demo, I think it's fine, but I don't think it's just a security thing.

**Ben Peeri** [15:48:05]: I think it's a product thing, which is why I was asking if Charlie is here, because at the end of the day, think we should give them like a budget on how many tokens we can process in a document format.

**Ben Peeri** [15:48:17]: And if they want to upload more, no problem, we'll send you whatever you want, just pay us more.

**Ben Peeri** [15:48:22]: We'll process all the text files you want.

**Ben Peeri** [15:48:24]: But we want to make sure.

**Ben Peeri** [15:48:25]: It's coming from our pocket, right.

**Ben Peeri** [15:48:28]: So there needs to be like part of the public subscription.

**Ben Peeri** [15:48:30]: They should need to be a limit on how many files are processed or are allowed as part of how many interviews are allowed.

**Ben Peeri** [15:48:38]: should be tied to that package.

**Ben Peeri** [15:48:43]: It's just net quantity of interviews.

**Ben Peeri** [15:48:46]: It's it's the volume of each interview in content, in documents, in length, in everything.

**Adam Petroff** [15:51:19]: Ben, Ben, just doing my interview,

**Ben Peeri** [15:51:34]: man.

**Ben Peeri** [15:51:35]: Oh,

**Adam Petroff** [15:51:37]: sorry, I didn't want to disturb

**Ben Peeri** [15:51:39]: the... Yeah, no, no, I was doing the interview on the side, like, doing some testing.

**Rana Muhammad Usama** [15:53:12]: I have a donated an interview for Marco, but I have the interview is not, we are preparing So it should not, it should validate the invitation and the username before proceeding for the best for the interview interview.

**Adam Petroff** [15:53:37]: That's a nice

**Ben Peeri** [15:53:59]: Is there any way to interrupt her and kind of start answering without her like, the entire question.

**Ben Peeri** [15:54:13]: Like, did we completely disable the interruption detection?

**Adam Petroff** [15:54:20]: Yeah, yeah, yeah, Macho did it is a manual turn.

**Adam Petroff** [15:54:25]: by clicking the button.

**Adam Petroff** [15:54:28]: Maybe you want to do kind of like a lot of issues and not enough time to solve all of them.

**Adam Petroff** [15:54:38]: So for now it's manual.

**Ben Peeri** [15:54:40]: Maybe you want to do kind of like a hybrid kind of like having that click but also have it recognize when I'm starting to answer what she is talking because it put in your mute and like I have to wait until she's finishing.

**Ben Peeri** [15:54:56]: It doesn't flow like a human conversation that way, right, because people like to jump into other people to interact.

**Lachezar Kozhuharov (Lacho)** [15:56:34]: Anybody actually completed an interview.

**Lachezar Kozhuharov (Lacho)** [15:56:42]: Yeah.

**Federico Rampazzo** [15:56:42]: Yeah, it's definitely long.

**Federico Rampazzo** [15:56:45]: Yeah,

**Charlie Patterson** [15:56:52]: it's definitely long.

**Charlie Patterson** [15:56:52]: Yeah, we can solve that problem.

**Federico Rampazzo** [15:56:59]: Also I'm thinking like if you have to give a demo, what are we got a demo.

**Federico Rampazzo** [15:57:02]: I mean, it's going to be a one hour session.

**Federico Rampazzo** [15:57:07]: Maybe we can think about a few examples of nice question that to show that our assistant is capturing some information that will not capture that you will not capture normally because that is pretty good with a follow-up question you can get some nice insights.

**Charlie Patterson** [15:57:21]: Yeah, I mean, I'm only sure to sneak out of the

**Martine Haug Olsen** [15:57:30]: I'll have to jump out for a bit, but I will be back for the review later for that.

**Martine Haug Olsen** [15:57:36]: Meeting later for the ones of us.

**Martine Haug Olsen** [15:57:38]: We're going to that.

**Martine Haug Olsen** [15:57:40]: See

**Ben Peeri** [15:59:00]: Did

**Panagiotis Apostolidis** [15:59:14]: anyone manage to test the slag bot?

**Lachezar Kozhuharov (Lacho)** [15:59:28]: I

**Mariam Khachatryan** [15:59:29]: guess, I test it, but not today, yesterday.

**Mariam Khachatryan** [15:59:30]: Did you change anything during today?

**Mariam Khachatryan** [15:59:32]: Yeah,

**Panagiotis Apostolidis** [15:59:34]: there were some updates on the system prompt of the book of the replicas and.

**Panagiotis Apostolidis** [15:59:40]: The change in the model instead of using high quality.

**Panagiotis Apostolidis** [15:59:46]: It uses sonnet.

**Panagiotis Apostolidis** [15:59:48]: And some formatting changes, you now can render and markdown.

**Mariam Khachatryan** [15:59:52]: Okay, I will go over one more Thank

**Panagiotis Apostolidis** [15:59:55]: you.

**Panagiotis Apostolidis** [15:59:56]: Ben,

**Mariam Khachatryan** [16:00:00]: you're

**Mariam Khachatryan** [16:00:11]: mighty.

**Ben Peeri** [16:00:42]: Yeah, I was doing my interview.

**Ben Peeri** [16:00:46]: Charlie, not have an indication on where I am in the journey.

**Ben Peeri** [16:00:51]: Even asking the chatbot, how many more questions I have left.

**Ben Peeri** [16:00:56]: How much more time should I tell for this interview?

**Ben Peeri** [16:00:59]: How should I plan to finish that interview?

**Ben Peeri** [16:01:02]: Can I finish this interview in one sitting on The chatbot doesn't give me any context about where I am in that journey of that interview.

**Ben Peeri** [16:01:13]: So I think we need to kind of like, I think we need to kind of like, hey, keep going, you only have a few more questions.

**Ben Peeri** [16:01:29]: it's very, very long.

**Charlie Patterson** [16:01:41]: But bone mind, we do want it to be, we're trying to capture everything everybody knows about their job and put it into a better job of structuring that experience.

**Ben Peeri** [16:01:52]: It's also about like my activation, right, because as I answer that, and it's the same tone, the same person, the same thing.

**Ben Peeri** [16:01:59]: It's all like staying that way.

**Ben Peeri** [16:02:01]: I'm losing interest, I'm losing patience.

**Ben Peeri** [16:02:06]: It doesn't trigger me to continue that conversation.

**Ben Peeri** [16:02:10]: It's all so, so flat.

**Ben Peeri** [16:02:13]: And like, it's like, it's like running a marathon and you don't know where the end is.

**Ben Peeri** [16:02:18]: It's just, it's all flat ground.

**Ben Peeri** [16:02:19]: It's all the same scenery.

**Ben Peeri** [16:02:24]: How do you make sure that I don't end interview right now because like, okay, I had enough and continue to engage me in that conversation.

**Ben Peeri** [16:02:32]: That's kind of like what I'm thinking.

**Lachezar Kozhuharov (Lacho)** [16:02:50]: I mean, I just, I'm going to ask you, how long it took you to answer the question of the question of the end.

**Ben Peeri** [16:03:03]: I'm like, okay.

**Ben Peeri** [16:03:04]: I'm like, okay.

**Mariam Khachatryan** [16:03:10]: Yeah.

**Mariam Khachatryan** [16:03:11]: Have

**Ben Peeri** [16:03:11]: we measured how long it takes us.

**Ben Peeri** [16:03:13]: How an interview.

**Ben Peeri** [16:03:16]: How long is an interview?

**Charlie Patterson** [16:03:18]: No, but we can, but we can, I think that, as, I think of the last time I left the job.

**Charlie Patterson** [16:03:23]: It me quite a while.

**Charlie Patterson** [16:03:26]: It took me quite a while.

**Charlie Patterson** [16:03:28]: It me quite a lot of the head on pay it.

**Charlie Patterson** [16:03:33]: It took me quite a while to get everything out of my head onto paper.

**Charlie Patterson** [16:03:38]: you know, it's not a short process.

**Charlie Patterson** [16:03:42]: yeah, one of the things we need to optimise for is, What does your progress look I guess for us, we should be focusing on the quality the information.

**Charlie Patterson** [16:03:55]: And when

**Lachezar Kozhuharov (Lacho)** [16:03:57]: kind of the, I guess for us, we should be focusing on the quality of the information.

**Lachezar Kozhuharov (Lacho)** [16:04:02]: And when you kind the kind of the kind of.

**Ben Peeri** [16:04:14]: It's more than that.

**Ben Peeri** [16:04:15]: I'm thinking also how it posed the questions because it goes through the role context, then role responsibilities.

**Ben Peeri** [16:04:29]: Maybe some context switching through the interview actually makes sense.

**Ben Peeri** [16:04:35]: I'm not like asking the same pool of question on the same because person lose interest if you stay on the same place.

**Ben Peeri** [16:04:43]: You might also want to capture it's a like, if we know it's a long journey, and we know it's a multi- session journey.

**Ben Peeri** [16:04:50]: My mental EQ Ben's position today tomorrow morning is not going to be the When I feel slightly different, my answers are going to be slightly different.

**Ben Peeri** [16:05:01]: And maybe when I answered a specific pool of questions in one day, I was biased in one way.

**Ben Peeri** [16:05:07]: When I asked the second pool of questions and I'm biased in a different way in that day.

**Ben Peeri** [16:05:11]: The fact that we are doing all those questions in one point of course, I'm like, from mental state, and not like from a few mental states over a couple of days, a couple of sessions.

**Ben Peeri** [16:05:28]: We spice things up, mix those questions, ask them in a different order, ask them in a different way, spread that in different sessions.

**Ben Peeri** [16:05:39]: I hope I make sense

**Charlie Patterson** [16:05:50]: Yes, it does make sense.

**Charlie Patterson** [16:05:51]: But yeah, I think it's a problem we can try tackle more after interview with the interview with a shorter list of people

**Ben Peeri** [16:06:06]: For the demo, maybe you want to have kind of like an interview with a shorter list of questions and not like what do we have like your 18 6666, so one, two, three, four, five, six.

**Ben Peeri** [16:06:26]: So we're gonna show the completion really fast.

**Ben Peeri** [16:06:35]: We

**Charlie Patterson** [16:06:35]: don't need to complete it.

**Charlie Patterson** [16:06:37]: That's fine.

**Charlie Patterson** [16:06:41]: We'll have a, we're gonna have demo.

**Charlie Patterson** [16:06:43]: We have a demo version setup of the Slack bot.

**Charlie Patterson** [16:06:46]: So we'll have some interviews so we can show the interview process looks like.

**Charlie Patterson** [16:06:50]: And they won't have a slack bike, and then I can go and show, so the one that's really pretty trained.

**Ben Peeri** [16:06:57]: Okay.

**Ben Peeri** [16:06:57]: Another thing I was thinking about earlier, and I'm going to try that later today.

**Ben Peeri** [16:07:00]: So I'm going to try to take your interviewer, and I'm going to try to open a chat GPT voice on my and I'm going to tell chat GPT pretend the open peer and interview on my behalf, and let it run LM to LM and then the human doesn't need to be in the loop for testing.

**Ben Peeri** [16:07:19]: And we can, so

**Egil Möller** [16:07:35]: for the whole, for the text interview, we actually have that.

**Egil Möller** [16:07:38]: We have a script that runs the full interview.

**Egil Möller** [16:07:43]: Oh, the full.

**Egil Möller** [16:07:45]: That's how we've done evaluations where we've evaluated different prompts, system prompts.

**Egil Möller** [16:07:51]: In the back end.

**Egil Möller** [16:07:52]: If you look in the scripts directory, there is a script called simulate interview that does But that is only for text.

**Egil Möller** [16:07:59]: It does not handle the voice.

**Ben Peeri** [16:08:01]: And it does your measure the time.

**Ben Peeri** [16:08:02]: It gets a person to speak and the time.

**Egil Möller** [16:08:05]: It gets one question.

**Egil Möller** [16:08:09]: Then run an LLM gets answer, sends that in, then run an LLM, gets an answer, sends that in, then run.

**Ben Peeri** [16:08:20]: So it's not batching and sending all the answers.

**Ben Peeri** [16:08:22]: No,

**Egil Möller** [16:08:23]: no.

**Egil Möller** [16:08:24]: So it takes the same time, except.

**Egil Möller** [16:08:27]: For the time of the time the user would take to type a question of the question of the question.

**Egil Möller** [16:08:34]: going to

**Ben Peeri** [16:08:40]: do a test later today and see how long it took me to complete an interview.

**Ben Peeri** [16:08:44]: I'm just going to let the LM run it and kind of like answer my behalf and see how well it works for voice

**Ben Peeri** [16:08:57]: Do we have a recording the voice?

**Ben Peeri** [16:09:01]: Yeah.

**Ben Peeri** [16:09:02]: Yeah.

**Adam Petroff** [16:09:12]: Yeah, if the chat mode.

**Adam Petroff** [16:09:18]: You should see the complete history.

**Ben Peeri** [16:09:21]: No, I'm asking, do we save like the voice file in a voice format or not.

**Adam Petroff** [16:09:27]: Pro'm probably not.

**Adam Petroff** [16:09:29]: No, I don't think

**Ben Peeri** [16:09:45]: Do you have a capability to do that, to save the file?

**Ben Peeri** [16:09:55]: I'm like, I'm

**Adam Petroff** [16:10:04]: thinking travel---------- like, the library the software we're using.

**Ben Peeri** [16:10:15]: Like, yeah, you can send, you can say it from Vosky to have it stored on the side.

**Ben Peeri** [16:10:20]: That will also drive our cost higher.

**Ben Peeri** [16:10:23]: Maybe that can be an add- on or something later.

**Egil Möller** [16:15:22]: I'm going to have Ted out.

**Egil Möller** [16:15:23]: So bye, See

**Adam Petroff** [16:15:30]: tomorrow.

**Valerio Francescangeli** [16:15:42]: I need to go to I'm, I'm,

**Valerio Francescangeli** [16:15:54]: I'm sure I'll answer more five.

**Valerio Francescangeli** [16:15:58]: It's like, it's like, am.

**Valerio Francescangeli** [16:16:00]: It's a, I don't know, how long should I possibly, at what point.

**Valerio Francescangeli** [16:16:08]: One could literally this all I have to say about the argument.

**Valerio Francescangeli** [16:16:12]: Stop asking me the same Or like, stop asking me what more information

**Federico Rampazzo** [16:16:21]: Yeah, I agree.

**Federico Rampazzo** [16:16:23]: We have the same

**Valerio Francescangeli** [16:16:30]: Okay.

**Valerio Francescangeli** [16:16:34]: See Bye.

**Lachezar Kozhuharov (Lacho)** [16:16:36]: Federico.

**Lachezar Kozhuharov (Lacho)** [16:16:37]: Take

**Ben Peeri** [16:16:37]: a look at the video I uploaded in the

**Ben Peeri** [16:17:50]: So one way to test the voice end to end.

**Ben Peeri** [16:18:11]: Yeah, so I'm going to let those but, but I would like to remove the click, every time, because that means I need to be a human in loop to just click proceed every time.

**Ben Peeri** [16:18:21]: If we have that interruption enabled back, we can do like end-to-end testing with that and really see, okay, how long it took them to finish the conversation without us needing to do it ourselves.

**Ben Peeri** [16:18:37]: So you can kind of create digital twins of personas based on sense, and then let those personas from sensei do the interview for you.

**Ben Peeri** [16:18:51]: see what I'm going with that.

**Lachezar Kozhuharov (Lacho)** [16:19:08]: She's much, I that he had something.

**Lachezar Kozhuharov (Lacho)** [16:19:12]: I don't know how we could enable that back.

**Lachezar Kozhuharov (Lacho)** [16:19:17]: But he might be able to.

**Ben Peeri** [16:19:25]: That can be a really cool demo.

**Ben Peeri** [16:19:26]: Like, you know, you know, you connect that to your digital avatar and then they do the interview for you too.

**Lachezar Kozhuharov (Lacho)** [16:19:33]: Yeah, then, yeah.

**Ben Peeri** [16:19:44]: But yeah, I'm going to let it run later today, I think it's going to be like six to eight hours to finish an interview.

**Ben Peeri** [16:19:52]: I think it's going to be a lot of time for me to really seriously finish an like if it's eight hours really, I need to know that before I go in because when I get this that request, I would think it's 15, 20 minutes.

**Ben Peeri** [16:20:07]: I would not think like a multi-day job that now I need So I

**Lachezar Kozhuharov (Lacho)** [16:20:13]: think I was like, I think

**Ben Peeri** [16:20:15]: I was like, I think the customer

**Lachezar Kozhuharov (Lacho)** [16:20:19]: what you what, like when I'm done knowledge transfer, when I'm leaving a place, usually it is a multi-day with, you know, multiple sessions, different So.

**Lachezar Kozhuharov (Lacho)** [16:20:32]: Because you have done.

**Lachezar Kozhuharov (Lacho)** [16:20:32]: We just need to probably manage

**Ben Peeri** [16:20:34]: education.

**Ben Peeri** [16:20:34]: You know what you expect.

**Ben Peeri** [16:20:36]: But when you get a message in an

**Lachezar Kozhuharov (Lacho)** [16:20:37]: email.

**Ben Peeri** [16:20:40]: What would you think it is the time is going to take it with the boss think.

**Ben Peeri** [16:20:43]: Yeah, We should either expectation or maybe have some built--in like.

**Ben Peeri** [16:20:48]: It's probably going to be different than what I would think.

**Lachezar Kozhuharov (Lacho)** [16:20:54]: So I just download me like a new walkout app, right.

**Lachezar Kozhuharov (Lacho)** [16:20:59]: it's

**Ben Peeri** [16:21:02]: It's more like, like, you know how like, so I just download me like a new walking app, right.

**Ben Peeri** [16:21:08]: So It's like, this, like, trying to be like a lot about that as well.

**Ben Peeri** [16:21:13]: Yeah.

**Ben Peeri** [16:21:13]: It's like, if I do like a good set.

**Ben Peeri** [16:21:16]: It's like doing me these stupid claps and like like confetti shit on the screen.

**Ben Peeri** [16:21:21]: Kind of like getting engaged, right.

**Ben Peeri** [16:21:23]: So it's a lot about that as

**Lachezar Kozhuharov (Lacho)** [16:21:27]: Yeah.

**Ben Peeri** [16:21:28]: Right.

**Ben Peeri** [16:21:29]: It's like, oh, yeah, good answer.

**Ben Peeri** [16:21:30]: But there is no feedback here.

**Ben Peeri** [16:21:32]: like, it's a pure machine, this Kind of like, it's hard, especially when it's a very long conversation.

**Ben Peeri** [16:21:41]: Yeah, You need to say some good job, well done, good answer.

**Ben Peeri** [16:21:48]: You are the rockstar.

**Ben Peeri** [16:21:50]: We start to see your living, blah, blah, blah.

**Ben Peeri** [16:21:57]: Yeah, but when

**Alessandro Huaroto** [16:21:57]: I do something like that with boss or something similar, Ben, normally I always have the estimation So definitely we have to

**Ben Peeri** [16:22:08]: Like, I did that earlier today, man, I was like, 45 minutes in, I'm like, I'm like, I don't look my way, in progress.

**Ben Peeri** [16:22:15]: like, how much more time.

**Alessandro Huaroto** [16:22:19]: No, it has to be, has to be 100%.

**Alessandro Huaroto** [16:22:20]: Or the risk that someone just close it and say, it.

**Alessandro Huaroto** [16:22:27]: That's it.

**Alessandro Huaroto** [16:22:29]: Yeah,

**Ben Peeri** [16:22:30]: I think that's a good situation.

**Ben Peeri** [16:22:31]: The bad situation is that he gives you bad info just like, That that's the walls.

**Ben Peeri** [16:22:38]: Like, how do you scrape that that in for later that.

**Ben Peeri** [16:23:08]: If I'm clicking end session, it's, it's, it's, it's public, I said, our interview, said, I said, I said, I said, I'm not doing it Will I get a follow------- it's pending.

**Ben Peeri** [16:23:35]: You should go ahead and go ahead and the moment.

**Ben Peeri** [16:23:39]: But it's a good

**Adam Petroff** [16:23:42]: feedback.

**Alessandro Huaroto** [16:23:45]: But it's a good feedback.

**Alessandro Huaroto** [16:23:46]: But something

**Alessandro Huaroto** [16:23:52]: now.

**Alessandro Huaroto** [16:23:52]: And I'm going to have it

**Ben Peeri** [16:23:53]: at the moment.

**Ben Peeri** [16:23:53]: But it's a good feedback.

**Ben Peeri** [16:23:54]: But but something to think about later.

**Ben Peeri** [16:23:56]: If I go to end session right and I click end session.

**Ben Peeri** [16:24:01]: It end the session.

**Ben Peeri** [16:24:02]: It doesn't even ask me, are you sure you want to end the Are you sure you want to end the session?

**Ben Peeri** [16:24:08]: I should be some type of activation.

**Ben Peeri** [16:24:09]: Hey, only two more minutes, only two questions for another five minutes.

**Ben Peeri** [16:24:15]: Would you Getting to stay a little bit longer.

**Ben Peeri** [16:24:18]: Allow him to exit, but ask him, are you sure?

**Ben Peeri** [16:24:22]: It's really important.

**Ben Peeri** [16:24:23]: We need to finish that.

**Ben Peeri** [16:24:25]: And maybe like, if I do say, okay, let me out.

**Ben Peeri** [16:24:28]: I don't want to do Oh, do you want me to call you are at eight o'clock this time to continue the interview.

**Ben Peeri** [16:24:34]: It needs it needs to continue engage me, even when I click the end

**Ben Peeri** [16:24:49]: I don't know if you got me because going in and

**Alessandro Huaroto** [16:24:53]: I think that what you say,

**Ben Peeri** [16:24:55]: before, about, like, the email that, not a voice interview assistant.

**Ben Peeri** [16:24:57]: I'm a text based interviewer, please provide.

**Ben Peeri** [16:25:01]: Sorry,

**Alessandro Huaroto** [16:25:03]: No, I say that what you say before about like the email that I'm like, thank you.

**Alessandro Huaroto** [16:25:09]: If you have some session in progress or if you have some steps that you are missing, it's really, really because it will like remind you.

**Alessandro Huaroto** [16:25:20]: Because like the problem, that you can, I'm going pay people, right to do this when they're leaving the company.

**Alessandro Huaroto** [16:25:32]: Maybe they can be not so motivated, right.

**Alessandro Huaroto** [16:25:34]: And

**Ben Peeri** [16:25:35]: that's exactly the point.

**Alessandro Huaroto** [16:25:37]: Yes.

**Ben Peeri** [16:25:39]: yeah.

**Ben Peeri** [16:25:39]: And maybe like a dashboard with widgets to see how far people from completion.

**Ben Peeri** [16:25:46]: What do you need to do, almost thinking like, hey, where is Daniel?

**Ben Peeri** [16:25:51]: Like he's activating customers in HubSpot, And when we see the user is having a churn, it doesn't do stuff.

**Ben Peeri** [16:25:57]: We send the marketing email, we get engagements.

**Ben Peeri** [16:26:00]: They need to be some type of a CRM funnel for activation and making sure that the user don't fall off before I complete the Because we only generate a summary, I think we have really, to be,

**Alessandro Huaroto** [16:26:25]: I think we have really two.

**Alessandro Huaroto** [16:26:27]: But maybe some of some of this is already on the Maybe Adam,

**Charlie Patterson** [16:26:33]: It is,

**Charlie Patterson** [16:26:39]: It is not the focus right now, it is, I would do something that we Monday and week.

**Ben Peeri** [16:26:45]: I think it's, for my experience in the last couple of days, it's demoable.

**Ben Peeri** [16:26:50]: It works well.

**Ben Peeri** [16:26:51]: It does what you want it

**Charlie Patterson** [16:26:54]: But

**Ben Peeri** [16:26:54]: the only thing that I would do is guardrail those questions and I kind do kind of like a Taylor interview a small pool of questions.

**Charlie Patterson** [16:27:06]: But we'll only be showing, we'll only have like five minutes to show demo.

**Charlie Patterson** [16:27:10]: Like, we're not going to be able to show them the whole interview.

**Charlie Patterson** [16:27:13]: So we can just run through a few questions of it and show them how it works.

**Charlie Patterson** [16:27:16]: And that will be sufficient.

**Charlie Patterson** [16:27:20]: But yeah, their key focus after this would be like, how we improve the quality of the interview, show progress and all those business.

**Ben Peeri** [16:27:30]: But yeah.

**Ben Peeri** [16:27:30]: How about like making a custom interview for that conference?

**Ben Peeri** [16:27:35]: Instead of asking questions about work, ask them five questions about the conference.

**Ben Peeri** [16:27:40]: They just been to the conference.

**Ben Peeri** [16:27:42]: How was the How was the hotel.

**Ben Peeri** [16:27:44]: How is the facility?

**Ben Peeri** [16:27:46]: Think about as an exit interview after being in the conference.

**Ben Peeri** [16:27:49]: It's basically the same and it's something that just experienced that They can answer you five questions quickly and then you can show them how the knowledge transfer their experience in the conference for the rest of the And you can do like like an interview with five questions in five minutes

**Ben Peeri** [16:28:08]: about that conference and show it to them end

**Ben Peeri** [16:28:28]: Charlie, which

**Alessandro Huaroto** [16:28:29]: is.

**Alessandro Huaroto** [16:28:29]: Charlie, going to ask something Something

**Charlie Patterson** [16:28:36]: Yeah,

**Alessandro Huaroto** [16:28:38]: it's

**Alessandro Huaroto** [16:28:48]: a nice feedback, Ben.

**Alessandro Huaroto** [16:28:49]: I'm trying to do the same, with some CHRO, you know, in my network.

**Alessandro Huaroto** [16:28:54]: I'm trying to do the same to do the same to do the same to get like some feedback from them they will be one that actually then they will use the platform.

**Alessandro Huaroto** [16:29:01]: So it's also extremely relevant see.

**Alessandro Huaroto** [16:29:05]: what they

**Ben Peeri** [16:29:13]: think, asking someone on something fresh, he just experienced that day and show how you can capture his knowledge or whatever experience it was, work, entertainment, restaurant, whatever is, it's a knowledge The type of knowledge can be whatever, But if you go to the, recent memory on something that

**Ben Peeri** [16:29:33]: just experienced that day or day before, and you ask them about that, that they can really connect to what you are

**Ben Peeri** [16:30:03]: Okay, phone back.

**Panagiotis Apostolidis** [16:30:35]: Are we're going to

**Charlie Patterson** [16:30:46]: done.

**Charlie Patterson** [16:30:46]: I Mark is per meeting in for the last.

**Charlie Patterson** [16:30:52]: I think most people of I think most people of I, have any other feedback, but thank you all.

**Charlie Patterson** [16:31:06]: But thank you all.

**Ben Peeri** [16:31:11]: Appreciate it.

**Ben Peeri** [16:31:12]: Thank all.

**Charlie Patterson** [16:31:18]: Appreciate it.

**Charlie Patterson** [16:31:20]: all.

**Charlie Patterson** [16:31:21]: it.

**Charlie Patterson** [16:31:25]: Thank you.

**Lachezar Kozhuharov (Lacho)** [16:31:26]: Bye.

**Ben Peeri** [16:31:28]: Bye.

**Ben Peeri** [16:32:04]: Oh,

---
*Backed up from MeetGeek on 2026-03-30 08:53*
