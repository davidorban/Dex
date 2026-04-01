# Website Project Sync

**Date:** 2026-02-03
**Duration:** Unknown
**Meeting ID:** 3e12c7fd-ea9e-4619-8ead-496f8703ca43

## Participants
- *Participants not listed*

### Summary

The meeting focused on preparing the website for public rollout while restricting content tied to pending offshore licenses; David emphasized implementing CI/CD with separate testing and production environments. Tasks were assigned and clarified in Asana (copyright, dependencies, team listings), and Jordy was asked to analyze task dependencies. Abbas was tasked to investigate Elementor/WPML compatibility and Slack guest disconnection issues. The team agreed on translation workflow using the testing site and a cadence of meetings (next meeting Thursday), with an initial go-live target before Friday the 13th while keeping the schedule flexible.

## Full Transcript

**David Orban** [08:12:29]: Hello, Ayya, hello, Abbas.

**David Orban** [08:12:33]: Hi David, hi.

**David Orban** [08:12:35]: I am well.

**David Orban** [08:12:37]: Sorry for being late.

**David Orban** [08:12:39]: Did Jordy show up?

**David Orban** [08:12:43]: I'm sorry.

**David Orban** [08:12:45]: Did Jordy join the call and then left, or she didn't join before?

**David Orban** [08:12:51]: I

**Aya Mohamed** [08:12:52]: joined and left and left.

**David Orban** [08:12:54]: Okay, okay, and is Abbas here or he's doing something else maybe?

**David Orban** [08:13:04]: He's here, but let me ping him.

**David Orban** [08:13:05]: Yeah, probably he's away from the computer.

**David Orban** [08:13:08]: Let me ping both of them.

**David Orban** [08:13:11]: Oh, okay, he just raised his hand.

**David Orban** [08:13:14]: All right, he's here.

**David Orban** [08:13:16]: Okay, good.

**David Orban** [08:13:20]: Let me ping Jordy then.

**David Orban** [08:13:46]: Let's see.

**David Orban** [08:13:53]: Yeah, she didn't respond.

**David Orban** [08:13:55]: I didn't notice that.

**David Orban** [08:14:01]: All right, well, she will see the transcript if she doesn't join.

**David Orban** [08:14:07]: So let me share the screen with the Asana project as usual.

**David Orban** [08:14:16]: And then we will take it from there, putting everything in context a bit.

**David Orban** [08:15:21]: Okay, so you can see my screen, right?

**David Orban** [08:15:24]: Yes.

**David Orban** [08:15:26]: Okay, great.

**David Orban** [08:15:28]: Let me go back to Asana.

**David Orban** [08:15:31]: All right, so in the last sprint, mid-November, we got the website implemented based on the design that we received from A3 agency working together with Alicia on the content side and then decided not to roll it out.

**David Orban** [08:16:07]: Hello, Jordy, welcome.

**David Orban** [08:16:09]: Hello.

**David Orban** [08:16:12]: All right.

**David Orban** [08:16:13]: So we decided not to roll it out last minute, because it was necessary to have the licenses in place to do so.

**David Orban** [08:16:26]: We have two branches in our activities onshore and offshore.

**David Orban** [08:16:34]: And they require two different sets of licenses.

**David Orban** [08:16:39]: And we received last week the licenses on the onshore side of our activities.

**David Orban** [08:16:48]: So the current sprint on the website is about bringing it to the point where we can take the coming soon page off.

**David Orban** [08:17:07]: and with certain activities and who is our team, etc.

**David Orban** [08:17:11]: etc.

**David Orban** [08:17:12]: etc.

**David Orban** [08:17:13]: Being still careful not to talk explicitly about those activities that need the offshore license that we are still waiting on.

**David Orban** [08:17:27]: Maybe this will be this week or next week.

**David Orban** [08:17:31]: And then we will progressively update the website, but it will be already visible to the world.

**David Orban** [08:17:41]: So I will go through two things together today.

**David Orban** [08:17:50]: One is the list of new tasks created in the or from the list, rather, where Michael said that he took a look at the website, and these are the things that he sees that we need to update.

**David Orban** [08:18:18]: And you see, it's quite thorough, including details like copyright, etc.

**David Orban** [08:18:23]: Fantastic.

**David Orban** [08:18:25]: So, there were these tasks that came out as a consequence.

**David Orban** [08:18:34]: And some of them are trivial, some of them are more delicate and complicated.

**David Orban** [08:18:40]: OK, so the second set of tasks that I we are going to mention and then I'm going to create and we will have to be very careful about is that.

**David Orban** [08:19:00]: We have been quotation marks played with very little responsibility or consequences because the website wasn't visible.

**David Orban** [08:19:10]: So if behind the splash screen something went wrong, that is fine.

**David Orban** [08:19:17]: From now on, since the website will be visible, we're not playing anymore.

**David Orban** [08:19:23]: We have to be 100% available all the time.

**David Orban** [08:19:28]: And so we will need to implement so- called CICD processes, continuous integration, continuous delivery.

**David Orban** [08:19:36]: So we will have a development website and a production website, and any change we make will be done on the development website first.

**David Orban** [08:19:49]: It will be shown, it will be approved, and then we will propagate that into the production website.

**David Orban** [08:19:58]: And so this is the second set of tasks that we will need to go through.

**David Orban** [08:20:04]: And this covers both features and content.

**David Orban** [08:20:12]: So only when a feature is good and tested, it can be published.

**David Orban** [08:20:19]: Only when a piece of content is good and approved, it can be published and so And let me just create a task, a design, see, oops.

**David Orban** [08:20:39]: Awesome, yes.

**David Orban** [08:20:42]: Or the website.

**David Orban** [08:20:45]: And I will do that.

**David Orban** [08:20:47]: Let's say tomorrow.

**David Orban** [08:20:50]: Okay.

**David Orban** [08:20:52]: Any questions so far?

**David Orban** [08:20:54]: No.

**David Orban** [08:21:00]: And it is wonderful to have the team back.

**David Orban** [08:21:07]: Hopefully we will work in a manner that is not stressful and we are not in a panic and we don't have very tight deadlines.

**David Orban** [08:21:29]: Leverage your availability if that were to happen, but the objective is to avoid to to be in that situation of deadlines that are not calculated well.

**David Orban** [08:21:48]: Aya received her only one email in the meantime, graduating to be part of the team.

**David Orban** [08:21:58]: As I understand, Aya, you are halftime with Alivan today, correct?

**Aya Mohamed** [08:22:04]: Some what?

**Aya Mohamed** [08:22:06]: You are not

**David Orban** [08:22:06]: full-time, you are halftime.

**David Orban** [08:22:09]: Oh, yes, yes, that's And of course you will manage your own time and then assignments.

**David Orban** [08:22:18]: Because I don't have visibility of everything you have to do.

**David Orban** [08:22:21]: So just please alert me if you have something urgent.

**David Orban** [08:22:27]: That means that you cannot look the website or whatever.

**David Orban** [08:22:31]: Okay.

**David Orban** [08:22:31]: Okay.

**David Orban** [08:22:35]: All right.

**David Orban** [08:22:35]: So let's now look at each of the tasks.

**David Orban** [08:22:40]: So update copyright as trivial, Abbas, you take care of it.

**David Orban** [08:22:44]: Perfect.

**David Orban** [08:22:46]: OK, so here I will add a subtask for Eden.

**David Orban** [08:22:56]: First of all, this should be broken in two separate things because the Israel Office is something that should be on the offices section.

**David Orban** [08:23:22]: Okay.

**David Orban** [08:23:23]: And I will confirm with Michael.

**David Orban** [08:23:35]: Confirm with Michael that it is okay to put a photo of Tel Aviv and the address of the Israel office on the offices section together with Riyad and the other places.

**David Orban** [08:23:51]: Because the alternative is that he says, no, no, no, we only want to list Eden in the team, but not put Israel in the offices.

**David Orban** [08:24:03]: So we have to clarify that.

**David Orban** [08:24:05]: And I will try to get that clarification today.

**David Orban** [08:24:09]: Okay.

**David Orban** [08:24:15]: And here I add the dependency.

**David Orban** [08:24:18]: This depends on that.

**David Orban** [08:24:22]: Okay.

**David Orban** [08:24:25]: All right.

**David Orban** [08:24:26]: Now, yeah, I will ask this from Veron.

**David Orban** [08:24:36]: Danya, okay.

**David Orban** [08:24:40]: I need to ask Danya because last time she said that she didn't want to be on the website.

**David Orban** [08:24:54]: I will ask this as well.

**David Orban** [08:24:56]: This you can do directly bus for Miray.

**David Orban** [08:25:02]: Amy, you can do directly Ross's bio you can fix.

**Haider** [08:25:15]: You are assigning tasks to yourself.

**Haider** [08:25:19]: Oh, oh, sorry.

**David Orban** [08:25:21]: Thank you for the correction.

**David Orban** [08:25:23]: And Abbas, if something is not clear, please ask, but you should be able to do this.

**David Orban** [08:25:37]: Okay, so.

**David Orban** [08:25:45]: Okay, I think this should be done by Nick.

**David Orban** [08:25:52]: And so, yeah, this you can do a bus.

**David Orban** [08:26:05]: And I think we are done here.

**David Orban** [08:26:07]: Perfect.

**David Orban** [08:26:08]: So, the next thing that we should do is to understand how the flow of work will proceed in terms of design, content, implementation, and the various confirmations, right?

**David Orban** [08:26:35]: So I will work on that.

**David Orban** [08:26:39]: Otherwise, we will always go without understanding we can do something and can we go live.

**David Orban** [08:26:52]: So this is clarify production process.

**David Orban** [08:27:04]: And how do we correctly integrate the team, making sure that content design, implementation, testing, confirmation and authorization to go live, happened smoothly without hiccups.

**David Orban** [08:27:32]: And I will try that by Thursday.

**David Orban** [08:27:37]: Okay.

**David Orban** [08:27:42]: So, we should always have the dependencies of the tasks as fine-tuned as possible, what depends on what.

**David Orban** [08:27:58]: We don't have a problem taking only one capital off the website.

**David Orban** [08:28:04]: That depends on nothing.

**David Orban** [08:28:06]: But putting Daniel on the team's page depends on me getting confirmation from her.

**David Orban** [08:28:12]: And after that she can be put on the team's page.

**David Orban** [08:28:16]: So these are two examples.

**David Orban** [08:28:18]: One, there is no dependency.

**David Orban** [08:28:19]: The other is dependency.

**David Orban** [08:28:21]: And I would like to ask you, Jordy, to analyze and then add these dependencies.

**David Orban** [08:28:29]: Okay, and you and I can work separately as needed.

**David Orban** [08:28:34]: Okay.

**David Orban** [08:28:35]: Then let's talk about, okay, actually let me add that as a task, sorry.

**David Orban** [08:29:01]: Okay.

**David Orban** [08:29:02]: Now,

**David Orban** [08:29:22]: Aya.

**David Orban** [08:29:24]: I forwarded an email Because I miss read I thought the email said now it works with Elementor, but it turns out I was wrong and the email said it does not work with Elementor.

**David Orban** [08:29:43]: So, Abbas, please analyze that email.

**David Orban** [08:29:54]: and discuss with Aya what does that mean for our translation process?

**David Orban** [08:30:01]: Because we don't want to have to copy and paste things manually.

**David Orban** [08:30:04]: It could very well mean that we downgrade Elementor, if necessary, in order to be able to use WPML, which is more important, right?

**David Orban** [08:30:16]: You see what I mean?

**David Orban** [08:30:19]: Yeah, yeah, exactly, yeah.

**David Orban** [08:30:21]: Okay, Aya, do you follow?

**David Orban** [08:30:23]: Yes.

**David Orban** [08:30:37]: This

**David Orban** [08:30:47]: is a good way.

**David Orban** [08:30:50]: Regarding

**Aya Mohamed** [08:30:51]: communicating with Abbas, I don't think he has my new slack.

**Aya Mohamed** [08:30:58]: So

**David Orban** [08:30:58]: for some reason, Abbas constantly disconnects from Slack.

**David Orban** [08:31:04]: And that's very annoying.

**David Orban** [08:31:07]: So I will decide if to give Abbas and Jordy an only one email or not.

**David Orban** [08:31:14]: We will see what should happen.

**David Orban** [08:31:18]: the meantime, have to invite both to the Slack project.

**David Orban** [08:31:25]: So let me do that.

**David Orban** [08:31:30]: Okay.

**David Orban** [08:31:30]: Thank you for reminding

**David Orban** [08:31:44]: And

**David Orban** [08:32:01]: Abbas, can you please research and let me know why is this disconnecting this disconnecting?

**David Orban** [08:32:08]: want to invite people to invite guests like Jordy and you and just stay there, not being kicked out automatically.

**David Orban** [08:32:17]: Okay?

**David Orban** [08:32:19]: Okay, all right.

**David Orban** [08:32:24]: Actually, you know what?

**David Orban** [08:32:25]: Abbas don't do that.

**David Orban** [08:32:26]: Anki.

**David Orban** [08:32:27]: Let me... Let me... You see my... You see my image, even if I'm sharing my screen, right?

**David Orban** [08:32:42]: Yes.

**David Orban** [08:32:42]: And Abbas and Jordy, can you turn on the camera momentarily?

**Jordy** [08:32:47]: my camera is on, I don't know why it's not showing.

**Jordy** [08:32:50]: Oh, it's the

**David Orban** [08:32:53]: minus bandwidth.

**David Orban** [08:32:55]: Yeah, bandwidth, sorry.

**David Orban** [08:32:57]: So please meet Ankit.

**David Orban** [08:33:00]: Ankit is in our team helping with all kinds of IT issues.

**David Orban** [08:33:07]: Jordy, Abbas and Ayya are working on the website.

**David Orban** [08:33:11]: Okay.

**David Orban** [08:33:12]: Project manager, developer, and Arabic translator.

**David Orban** [08:33:17]: Okay.

**David Orban** [08:33:17]: And they are respectively in Seoul, in Pakistan, and in Egypt.

**David Orban** [08:33:22]: All right.

**David Orban** [08:33:24]: And so what I would like you is to research why single channel guest in Slack is kicked out automatically after a time.

**David Orban** [08:33:40]: It's weird, just spurt here, let's... No, because... No, the issue you me.

**David Orban** [08:33:49]: Yeah, oh, yeah, I will open the ticket, yes.

**David Orban** [08:33:53]: Sorry.

**David Orban** [08:33:54]: Before

**Aya Mohamed** [08:33:55]: I had Aliwan email, mine used to get kicked out because says, it's a full trial.

**Aya Mohamed** [08:34:03]: That was the reason Yes.

**Aya Mohamed** [08:34:14]: Yes,

**David Orban** [08:34:14]: so don't know.

**David Orban** [08:34:17]: Maybe it is linked to the fact, it is not linked to the fact that you have a Slack workspace because Jordy is kicked out as well.

**David Orban** [08:34:28]: So, I don't Jordy is from, oh, David Orban has a workspace.

**David Orban** [08:34:37]: Oh, okay.

**David Orban** [08:34:43]: This will be

**David Orban** [08:34:54]: it.

**David Orban** [08:35:13]: Okay.

**David Orban** [08:35:20]: All right, so you are back and you will be able to see the previous messages.

**David Orban** [08:35:24]: The only thing is that it may not be the same identity that you will be posting with, whatever.

**David Orban** [08:35:32]: Not a huge problem.

**David Orban** [08:35:34]: Okay.

**David Orban** [08:35:36]: So back to Asana.

**David Orban** [08:35:41]: Let me... before I forget and take

**David Orban** [08:36:16]: So back to the website.

**David Orban** [08:36:27]: Okay.

**David Orban** [08:36:28]: And let's go back to the older tasks as well, because some of them we neglected because we learned that we wouldn't go live, right?

**David Orban** [08:36:40]: So let's look at those as well.

**David Orban** [08:36:44]: to make sure that we are not going live with something being forgotten that was actually important.

**David Orban** [08:36:54]: And let me see if I'm being late on another meeting.

**David Orban** [08:37:03]: Okay, I'm not.

**David Orban** [08:37:04]: All right.

**David Orban** [08:37:05]: So thank you for this kickoff today.

**David Orban** [08:37:11]: We assigned all the tasks, the deadlines.

**David Orban** [08:37:17]: Jordan is going to work on dependencies.

**David Orban** [08:37:21]: I will ask if we have a go live date.

**David Orban** [08:37:28]: And if we do, probably it is going to be flexible.

**David Orban** [08:37:31]: So we will try to get ready by that date, but it's not going to be a huge pressure, hopefully.

**David Orban** [08:37:41]: Any any questions before we end the call?

**David Orban** [08:37:49]: I was

**Aya Mohamed** [08:37:49]: going to ask about the timeline, but you just said there's no specific date.

**David Orban** [08:37:55]: So I think there will be a date, and let's say if it is less than two weeks, I will try to get it to two weeks.

**David Orban** [08:38:05]: But if our group said, oh, we need a month, no, that would be loose.

**David Orban** [08:38:13]: We have to be faster than that, okay?

**David Orban** [08:38:15]: So for the moment, let's keep in mind to have it go live before next Friday, 13th.

**David Orban** [08:38:30]: I think that is reasonable.

**David Orban** [08:38:32]: And if it needs to be faster, I will let you know, but I need to collect information internally.

**David Orban** [08:38:42]: Okay.

**David Orban** [08:38:43]: Abbas, Jordy, any questions from your side?

**Haider** [08:38:49]: Yes, I have just one question.

**Haider** [08:38:53]: Where are, what are we doing with the new pages we discussed about?

**Haider** [08:38:57]: Are we doing them?

**Haider** [08:39:05]: The answer is we have to drive that process

**David Orban** [08:39:10]: because we are not working with the designer anymore, Ahmed and company from A3 Agency.

**David Orban** [08:39:19]: So we are not going to get those ideas from them.

**David Orban** [08:39:26]: This means Abbas and Aya and Jordy.

**David Orban** [08:39:33]: that you can you should come up with ideas on how to make the website better.

**David Orban** [08:39:40]: Where the first is fit for purpose.

**David Orban** [08:39:47]: So how are the websites of other companies that are like us?

**David Orban** [08:39:52]: What is the objective that we want to achieve with the website?

**David Orban** [08:39:56]: And as a consequence, work towards implementing that.

**David Orban** [08:40:01]: In the example that I remember is you were saying, Abbas, that we should have the team page separately.

**David Orban** [08:40:09]: And there are a gazillion things, of course, that we will be able to do.

**David Orban** [08:40:17]: so, yes, I encourage you to do that.

**David Orban** [08:40:24]: should these pages live on the development side, Or should we have actually three, because typically they are three.

**David Orban** [08:40:35]: Development, test and production.

**David Orban** [08:40:39]: Because if we want the experiments to be more exotic, then we don't want to frighten the people who need to approve changes going live, because they would be confused.

**David Orban** [08:40:59]: Are they approving the team page that is separate from the home page now?

**David Orban** [08:41:03]: Or are they approving the changes on the home page only, So it could be the case that we need more than two websites.

**David Orban** [08:41:14]: In the meantime, I will set up I think I will call it testing, testing and and production.

**David Orban** [08:41:23]: And then probably soon we will decide that we need development as well.

**David Orban** [08:41:27]: And it is in the development side that we will have the more radical changes before they are promoted to

**David Orban** [08:41:43]: testing.

**David Orban** [08:41:44]: All right?

**David Orban** [08:41:48]: Okay.

**David Orban** [08:41:50]: Okay, so anything please post on Slack.

**David Orban** [08:41:55]: I will probably post a summary, a little summary on Slack as well.

**David Orban** [08:42:01]: And then we will resume.

**David Orban** [08:42:08]: I don't think we need a daily stand up like we did during the crunch time.

**David Orban** [08:42:18]: twice a week for sure.

**David Orban** [08:42:21]: we will see if next week may be, you know, something like Wednesday, Thursday, Friday.

**David Orban** [08:42:27]: So today is Tuesday.

**David Orban** [08:42:29]: Let's set the next meeting for Thursday.

**David Orban** [08:42:32]: Does it work for both of you the same time, both, all three of you at the same time, and hopefully I will not be late?

**David Orban** [08:42:44]: Yes, towards me.

**Haider** [08:42:54]: Okay,

**David Orban** [08:42:54]: and believe it or not, Microsoft doesn't have a feature that allows you to duplicate calendar invite.

**David Orban** [08:43:01]: Amazing.

**David Orban** [08:43:04]: You have to write it all the time all over.

**David Orban** [08:43:19]: Okay.

**David Orban** [08:43:21]: Can I ask something?

**David Orban** [08:43:25]: No, the time for questions, it's Okay, bye-

**Aya Mohamed** [08:43:28]: bye.

**Aya Mohamed** [08:43:30]: Yes, you Okay, I wanted to know, so whenever a page is updated, I translated on the spot.

**Aya Mohamed** [08:43:38]: Or how do I know if it's updated?

**David Orban** [08:43:46]: Okay.

**David Orban** [08:43:50]: So regards to translations, You both the translator and the approval.

**David Orban** [08:44:01]: Yes, when it comes to That's it.

**David Orban** [08:44:04]: That's it.

**David Orban** [08:44:08]: So the English content gets approved, then you translate.

**David Orban** [08:44:13]: And when both the English and the Arabic are available, we publish.

**David Orban** [08:44:18]: But you translate on the test site and we promote The new content from the test site to the development site.

**David Orban** [08:44:30]: So, this is something that we didn't do previously.

**David Orban** [08:44:34]: Yes.

**David Orban** [08:44:36]: But now with the CICD process, continuous in integration, continuous development, probably the other way whatever.

**David Orban** [08:44:45]: This process is a bit new.

**David Orban** [08:44:50]: So you will be mainly working on the testing site and not on the live site.

**David Orban** [08:44:56]: You will no one will touch the live site.

**David Orban** [08:45:01]: Only a computer process will move when we push a button, the content from the testing site to the live Okay, and that will be relatively ceremonial.

**David Orban** [08:45:15]: We will we will agree.

**David Orban** [08:45:17]: Are we ready?

**David Orban** [08:45:19]: Everything is tested.

**David Orban** [08:45:20]: Everything is authorized.

**David Orban** [08:45:21]: OK, push a button, go And we will do You know, maybe once a week or once every two weeks.

**David Orban** [08:45:31]: We will not tweak the live site every day.

**David Orban** [08:45:34]: No, that not that is not possible because we are a bank and we are serious.

**David Orban** [08:45:40]: We are professionals.

**Aya Mohamed** [08:45:46]: Okay.

**Aya Mohamed** [08:45:49]: Are Yep.

**Aya Mohamed** [08:45:53]: Wonderful.

**Aya Mohamed** [08:45:53]: Thank you, bye-

**David Orban** [08:45:54]: Thank you.

**David Orban** [08:45:56]: Bye- bye.

**Haider** [08:45:56]: Thank you.

---
*Backed up from MeetGeek on 2026-03-30 08:45*
