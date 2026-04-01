# ITAM review

**Date:** 2026-02-18
**Duration:** Unknown
**Meeting ID:** 0e5cc30f-1c0d-40d6-945f-540a270d9e7a

## Participants
- *Participants not listed*

### Summary

The meeting focused on validating a SharePoint-based IT asset management platform, with Ankit demonstrating asset creation, status changes, and action log entries using a shared testing document. They agreed to create unassigned in-stock records for newly received laptops and to explore automating data import from Intune/Active Directory. Active Directory usage, including profile photos and organizational hierarchy, was discussed and a plan to coordinate updates with Nisha was agreed. Operational items covered printer delivery, Canon technician setup, and removing a costly shared printer driver, plus arranging A3 paper availability. Finally, they reviewed email spam handling, planned a Microsoft support ticket for permanent mail-flow solutions, and assigned a bulk domain upload task using PowerShell or similar.

## Full Transcript

**Unknown speaker** [10:01:07]: again.

**Unknown speaker** [10:01:07]: Check

**David's Notetaker** [10:01:10]: my headphones settings, please.

**Ankit Choudhary** [10:01:13]: Okay, now I think I can hear you well.

**David Orban** [10:01:19]: Can you?

**David Orban** [10:01:21]: I can hear

**Ankit Choudhary** [10:01:24]: you.

**Ankit Choudhary** [10:01:24]: Without the headphones.

**Ankit Choudhary** [10:01:28]: There

**David Orban** [10:01:29]: is some issue with my headphones.

**David Orban** [10:01:32]: And is

**Ankit Choudhary** [10:01:33]: Chidem there with you?

**Ankit Choudhary** [10:01:35]: Yeah, she's in the room.

**David Orban** [10:01:37]: Same.

**David Orban** [10:01:37]: Okay, so

**Ankit Choudhary** [10:01:41]: if you use the headphones, that is

**David Orban** [10:01:42]: okay.

**David Orban** [10:01:43]: If not, probably it is better.

**David Orban** [10:01:46]: Yeah, yeah, can

**Ankit Choudhary** [10:01:48]: you hear me?

**Ankit Choudhary** [10:01:52]: Yeah, I can hear you.

**Ankit Choudhary** [10:01:54]: Yeah, now headphone is working.

**Ankit Choudhary** [10:01:56]: Thank you.

**Ankit Choudhary** [10:01:56]: Okay, wonderful.

**Ankit Choudhary** [10:01:59]: All

**David Orban** [10:01:59]: right, so

**Ankit Choudhary** [10:02:01]: let's start with

**David Orban** [10:02:02]: what the meeting is set up for, which is the asset management platform that I designed and you implemented, right?

**David Orban** [10:02:17]: So I will share my screen and you will guide me where I need to go.

**David Orban** [10:02:29]: to then test it and then we will start adopting it and hopefully substituting spreadsheets with this one, which is the objective.

**David Orban** [10:02:43]: Okay?

**David Orban** [10:02:44]: So, so let me go to

**David Orban** [10:02:54]: SharePoint and

**David Orban** [10:03:04]: here.

**David Orban** [10:03:17]: Is it any of these?

**David Orban** [10:03:18]: I don't remember.

**Ankit Choudhary** [10:03:22]: Or it's another one.

**Ankit Choudhary** [10:03:25]: Oh, it should be under Android.

**Ankit Choudhary** [10:03:29]: Go back to home.

**Ankit Choudhary** [10:03:31]: It should be under Android.

**Ankit Choudhary** [10:03:32]: This one.

**Ankit Choudhary** [10:03:38]: Androidy recent and dried you can see under the first one is I leave on IT, second one is Androidy.

**Ankit Choudhary** [10:03:46]: This one, yeah, you can click on that second one, yeah.

**Ankit Choudhary** [10:03:53]: Now on the right hand side at the top, you can see this the wheel icon next to your profile picture.

**Ankit Choudhary** [10:04:00]: Here you can see question mark this one, the settings, settings, settings, go to settings in the top, yeah.

**Ankit Choudhary** [10:04:06]: Then go to site.

**Ankit Choudhary** [10:04:08]: content third option.

**Ankit Choudhary** [10:04:12]: This one.

**Ankit Choudhary** [10:04:13]: Yeah, this one.

**Ankit Choudhary** [10:04:18]: Here you can see the IT software asset, IT hardware assets, and IT asset logs.

**Ankit Choudhary** [10:04:23]: Let's go to IT hardware asset.

**Ankit Choudhary** [10:04:32]: So I have created one test information which I added over here as well the document which you shared with me I follow that and I added this one and let's open in a separate page the document so we can compare it the test the steps which you shared with me for testing let me quickly check

**Ankit Choudhary** [10:05:07]: the asset action blocks.

**Ankit Choudhary** [10:05:14]: Okay,

**Unknown User** [10:05:15]: sorry, I clicked through the various tabs.

**Unknown User** [10:05:18]: Which, what did you want me to open another browser window with the Asana task?

**Unknown User** [10:05:25]: Oh, not other

**Ankit Choudhary** [10:05:26]: asana task.

**Ankit Choudhary** [10:05:27]: Could you please open that asana task?

**Ankit Choudhary** [10:05:30]: So we can find that document directly from there.

**Ankit Choudhary** [10:05:34]: The task which you assigned me.

**Ankit Choudhary** [10:05:36]: regarding this request that one.

**Ankit Choudhary** [10:06:10]: Okay.

**Ankit Choudhary** [10:06:11]: The

**Unknown User** [10:06:11]: handover, handover.

**Unknown User** [10:06:12]: It

**Ankit Choudhary** [10:06:13]: is what we are doing now?

**Ankit Choudhary** [10:06:21]: Yes.

**Ankit Choudhary** [10:06:25]: Okay.

**Ankit Choudhary** [10:06:28]: Okay.

**Unknown User** [10:06:31]: Okay.

**Ankit Choudhary** [10:06:43]: So as per this, create a new hardware asset.

**Ankit Choudhary** [10:06:47]: I created a new, I click on the new and I added all this information as mentioned.

**Ankit Choudhary** [10:06:52]: Then in fourth, it's mentioned leave status blank and click on save, then expected result.

**Ankit Choudhary** [10:07:02]: The status show in a stock default value and the status display with the gold color and icon.

**Ankit Choudhary** [10:07:08]: So it was a gold color when in a stock.

**Ankit Choudhary** [10:07:12]: If you want, you can go back and you can check over there.

**Ankit Choudhary** [10:07:16]: So right now, yeah, just scroll down on the right-hand side, move it right inside this page.

**Ankit Choudhary** [10:07:25]: From the bottom, you can move it on the right-hand side.

**Ankit Choudhary** [10:07:28]: Oh, I see.

**Ankit Choudhary** [10:07:29]: Okay.

**Ankit Choudhary** [10:07:30]: Right now, it's showing blue because I made some more changes.

**Ankit Choudhary** [10:07:33]: If you click on it, just click on it, you can see in a stock that is the, that is in a golden color.

**Ankit Choudhary** [10:07:40]: Is it working from here?

**Ankit Choudhary** [10:07:47]: scroll down so right now if you change try to change this yeah click on it so the instruction in the gold pillar nice this is what we are looking for as per the testing now you can go back that testing one okay this one where the steps mentioned for testing all right so this is working as expected

**Ankit Choudhary** [10:08:16]: then 7.2 assign the user to asset added the test as asset created above and change the status to assign so we change the status to assign from stock earlier it was in stock so I changed to assign and expected result the assigned best should be with a column icon contact icon sorry it's look like a

**Ankit Choudhary** [10:08:38]: contact picture over there on the assigned And it should be in a blue color.

**Ankit Choudhary** [10:08:44]: It's mentioned somewhere.

**Ankit Choudhary** [10:08:45]: Yeah.

**Ankit Choudhary** [10:08:46]: Status seems to blue, which is done.

**Ankit Choudhary** [10:08:49]: It's showing in a blue.

**Ankit Choudhary** [10:08:50]: And sign, it's showing this picture like a contact, small picture.

**Ankit Choudhary** [10:08:55]: Yeah.

**Ankit Choudhary** [10:08:55]: And is a blue color.

**Ankit Choudhary** [10:08:57]: So this is also completed.

**Ankit Choudhary** [10:08:59]: Okay.

**Ankit Choudhary** [10:09:01]: And not longer appear in an assigned state.

**Ankit Choudhary** [10:09:03]: So this is fine.

**Ankit Choudhary** [10:09:04]: It's not assigned.

**Ankit Choudhary** [10:09:06]: It's not assigned or in stock.

**Ankit Choudhary** [10:09:09]: Third one, create action log entry, navigate to action logs.

**Ankit Choudhary** [10:09:15]: Now we have to go back and we have to go this IT asset action log.

**Ankit Choudhary** [10:09:20]: Just go back one more steps.

**Ankit Choudhary** [10:09:22]: You can go back from the top or you can go to site content again.

**Ankit Choudhary** [10:09:26]: You can click on site content at the top.

**Ankit Choudhary** [10:09:29]: Here.

**Ankit Choudhary** [10:09:32]: Now you can go IT asset action logs.

**Ankit Choudhary** [10:09:38]: Now you can go back to the document.

**Ankit Choudhary** [10:09:43]: All right, so this is the one.

**Ankit Choudhary** [10:09:46]: Create action log entry, 7.3. I click on new.

**Ankit Choudhary** [10:09:53]: I edit all this information.

**Ankit Choudhary** [10:09:55]: And yeah, I added all the information here.

**Ankit Choudhary** [10:10:00]: And the action type is showing a sign.

**Ankit Choudhary** [10:10:04]: You can check the expected result in the document.

**Ankit Choudhary** [10:10:07]: So you can understand better, it's showing correct or not.

**Ankit Choudhary** [10:10:11]: So expected result, item created successfully, action type, show, blue, assign, which is fine, badge with add friend icon, which is showing over the add friend icon if you see.

**Ankit Choudhary** [10:10:27]: Yeah.

**Ankit Choudhary** [10:10:27]: Okay, and it's showing up blue one.

**Ankit Choudhary** [10:10:28]: So this is also completed.

**Ankit Choudhary** [10:10:30]: Now 7.4, I think I didn't test the 7.4. navigate to navigate, switch to assign asset view and test view to assign stock.

**Ankit Choudhary** [10:10:46]: Okay, we have to go back to IT asset.

**Ankit Choudhary** [10:10:54]: Assign asset view here is at the top.

**Ankit Choudhary** [10:10:58]: Next tool, yeah, this one, click on So we're just talking about when we create any item over here, when we add any new item, that normally appear under the in- stock items.

**Ankit Choudhary** [10:11:11]: There is a view if you click here on this arrow by department missing out this one.

**Ankit Choudhary** [10:11:17]: If you click on it, you can see, no, no, just click on that again on that arrow, this one.

**Ankit Choudhary** [10:11:23]: And then you can see option here, the unassigned and in-stock, this fourth option.

**Ankit Choudhary** [10:11:30]: So normally what happened when you create any new item, that item appear here normally.

**Ankit Choudhary** [10:11:35]: But when you assign, when you change the status, assign, so it moved to the assign asset, this one, this view.

**Ankit Choudhary** [10:11:43]: So this is working now.

**Ankit Choudhary** [10:11:44]: Let me ask you question.

**Ankit Choudhary** [10:11:46]: Yeah.

**Ankit Choudhary** [10:11:47]: Would it be now the right thing to

**Unknown User** [10:11:50]: create each notebook that arrived as an asset waiting to be assigned?

**Ankit Choudhary** [10:12:04]: Sorry, could it please appear again a question?

**Ankit Choudhary** [10:12:06]: Sure, yesterday we received from ISAR

**Unknown User** [10:12:10]: from tech.

**Unknown User** [10:12:10]: Yeah,

**Ankit Choudhary** [10:12:11]: correct, three devices we received, three laptops.

**Ankit Choudhary** [10:12:14]: A number of

**Unknown User** [10:12:15]: laptops.

**Unknown User** [10:12:16]: And so in order for the asset management platform to correctly reflect reality, we should create, you should create the unassigned in stock assets corresponding to the notebooks that we have

**Unknown User** [10:12:45]: now in the process of adopting this system so it is natural that it will take a little bit of time to understand the functionality and how to use it right yes absolutely and then the next step is going to be to go by each user and make sure that we correctly reflect the reality of their system, not

**Unknown User** [10:13:14]: only in terms of hardware, but also in terms of

**Unknown User** [10:13:23]: software.

**Unknown User** [10:13:30]: who are the people who we need to concentrate on, because they still have.email on Treasury, they still have a computer that is not enrolled in INTU, INTU, right?

**Unknown User** [10:13:52]: And then we can decide, do we go by department, by tower, By, do we concentrate on the people who are farthest behind, you know, we, that is, that is, I think, one of the reasons why this is useful, because it enables us to analyze and prioritize what we do, proactively guiding us to do things that

**Unknown User** [10:14:22]: are high impact and high value.

**Unknown User** [10:14:27]: And then the next thing that we can do once this is in place is generated reports, either a simple PDF report or give a URL for dynamic reporting to Amina or Michael or whoever.

**Unknown User** [10:14:50]: who can actually see without having the writing.

**Unknown User** [10:14:54]: They have no editing ability.

**Unknown User** [10:14:57]: They cannot change values, but they can view in real time what is the situation.

**Unknown User** [10:15:06]: I understand.

**Unknown User** [10:15:07]: Okay, so this is why we started with this system.

**Unknown User** [10:15:14]: And now my next question is, rather than entering manually information.

**Unknown User** [10:15:27]: Can we pull information automatically from Intune so that at least those entries that correspond to a machine that is managed by Intune, the hardware details and the software details are automatically created?

**Ankit Choudhary** [10:15:50]: I think that is possible.

**Ankit Choudhary** [10:15:52]: That is definitely possible.

**Ankit Choudhary** [10:15:54]: I saw few articles as well.

**Ankit Choudhary** [10:15:55]: I didn't implement it yet, but I think, yes, it is possible we can grab the information from the Intune here in SharePoint.

**Ankit Choudhary** [10:16:05]: Yeah, and then I assume

**Unknown User** [10:16:08]: it will be something like this that is going to bring the information or whatever.

**Unknown User** [10:16:20]: My recommendation as you research this is not only to search the articles, but use Google Cloud, sorry, Google

**Ankit Choudhary** [10:16:35]: Cloud, just Cloud.

**Ankit Choudhary** [10:16:36]: Cloud, to use Anthropic Cloud to

**Unknown User** [10:16:39]: use Cloud Co-work and you say, hey, here is the IT asset management platform that I implemented.

**Unknown User** [10:16:51]: These are the markdown files that I followed.

**Unknown User** [10:16:55]: And all the tests are positive.

**Unknown User** [10:17:01]: My question is, what is the efficient way to bring information from active directory and in tune into this system?

**Unknown User** [10:17:12]: And then you can compare the information that you get from the articles that you research and the recommendation and the plan that that Claude creates.

**Unknown User** [10:17:27]: Okay?

**Unknown User** [10:17:28]: So that is, in my opinion, that is the right way to go about it, because the first will take you, I don't know, two weeks.

**Unknown User** [10:17:39]: The second will take you two hours.

**Unknown User** [10:17:43]: Okay.

**Unknown User** [10:17:46]: Now, this is great.

**Unknown User** [10:17:50]: And

**Unknown User** [10:17:55]: so let's agree on these two tasks.

**Unknown User** [10:17:58]: One, create the assets for the notebooks in stock, because obviously that is the starting point.

**Unknown User** [10:18:13]: The system has to match reality.

**Unknown User** [10:18:17]: Okay.

**Unknown User** [10:18:19]: And then second, let's make sure that the system serves us rather than we serving the system, right?

**Unknown User** [10:18:28]: That is why instead of entering information manually, we pull information automatically from systems that already exist.

**Unknown User** [10:18:43]: Okay.

**Unknown User** [10:18:44]: it.

**Ankit Choudhary** [10:18:44]: Yes.

**Ankit Choudhary** [10:18:48]: Now,

**Unknown User** [10:18:54]: this is great.

**Unknown User** [10:18:56]: Wonderful.

**Unknown User** [10:18:57]: And well done.

**Unknown User** [10:19:01]: Let's now aim to do also another thing, not today, but to check it as a as an objective.

**Unknown User** [10:19:20]: On the intranet itself,

**Unknown User** [10:19:27]: the team directory is today manual.

**Unknown User** [10:19:35]: Okay.

**Unknown User** [10:19:37]: It comes from a very simple spreadsheet.

**Unknown User** [10:19:42]: And instead of creating this spreadsheet manually, it should come from active directory.

**Unknown User** [10:19:51]: We mentioned this maybe a week ago or two weeks ago.

**Unknown User** [10:19:54]: You remember?

**Unknown User** [10:19:56]: I do remember

**Ankit Choudhary** [10:19:57]: and at that time I updated the reporting manager information I discussed with you as well.

**Ankit Choudhary** [10:20:03]: I updated the reporting manager the information which I However, I inform to Nisha as well, whenever she shared the username, any new hire or any username.

**Ankit Choudhary** [10:20:15]: So she should provide me the reporting manager, the phone number, the location, and the more information which she can provide me about the user.

**Ankit Choudhary** [10:20:24]: So I can update all the information at the same time in the active directory.

**Ankit Choudhary** [10:20:27]: So it will not create more problems.

**Ankit Choudhary** [10:20:29]: And second thing, because for old users, which we have already here in Aliwan, so I inform her.

**Ankit Choudhary** [10:20:37]: Whenever she have a time, she just shared the more detail about the user so I can update the information in the active directly.

**Ankit Choudhary** [10:20:42]: So in future, we get the software to create the automatic automation for the signature as you mentioned last time.

**Ankit Choudhary** [10:20:51]: So that application or that software can pick the information from active directly and create the signature automatically without any creating any problem.

**Ankit Choudhary** [10:21:00]: So yeah, I will inform to Nisha about it.

**Ankit Choudhary** [10:21:02]: Okay, and did she acknowledge

**Unknown User** [10:21:05]: this, do you, because when she provided us with some new hires, I asked her, please provide their job title and who they report to, and she did that, right, and also which tower they are at.

**Unknown User** [10:21:32]: But for example, she didn't provide the phone number, right?

**Unknown User** [10:21:37]: Correct, she not

**Ankit Choudhary** [10:21:38]: didn't provide the phone number.

**Ankit Choudhary** [10:21:40]: So, so do you think that I should also

**Unknown User** [10:21:45]: ask her because you did ask her, but she didn't.

**Ankit Choudhary** [10:21:50]: She did not have the phone number.

**Ankit Choudhary** [10:21:52]: Can we do one thing, if you agree on it, can we provide the basic access to Nisha to create the user on on exchange on our office 365. So at least she can add the user information by itself and like don't assign the license, just create the user.

**Ankit Choudhary** [10:22:10]: And then she just inform us that I created the user kindly check And whenever you have a license, assign it and this user will join from this date.

**Ankit Choudhary** [10:22:19]: And then we can process the further things like system, like laptop preparation and the software installation, everything we will take care.

**Ankit Choudhary** [10:22:26]: But she can create the user from their site.

**Ankit Choudhary** [10:22:28]: And she can just send email to us that I have already created the user with this name.

**Ankit Choudhary** [10:22:34]: And I have already filled all the information, whatever I have.

**Ankit Choudhary** [10:22:37]: And now you can proceed with the further, assign the license and create the system for her, for that user.

**Ankit Choudhary** [10:22:45]: all the other tasks we can manage but she can create the user from their side only.

**Ankit Choudhary** [10:22:50]: We can provide the basic access just to create the user.

**Ankit Choudhary** [10:22:53]: Absolutely.

**Ankit Choudhary** [10:22:55]: Yes.

**Unknown User** [10:22:59]: Do you prefer if I do that rather than you?

**Unknown User** [10:23:04]: I can provide the access.

**Ankit Choudhary** [10:23:06]: We can provide the user administrative access to her.

**Ankit Choudhary** [10:23:08]: So she can create this.

**Ankit Choudhary** [10:23:08]: Why don't we do this?

**Ankit Choudhary** [10:23:09]: Why don't we do this?

**Unknown User** [10:23:11]: Send me the link that she should use.

**Unknown User** [10:23:16]: And then I will send her the email with the link.

**Unknown User** [10:23:23]: And then maybe she takes it more seriously.

**Ankit Choudhary** [10:23:29]: Okay.

**Ankit Choudhary** [10:23:31]: right.

**Ankit Choudhary** [10:23:31]: Okay.

**Ankit Choudhary** [10:23:33]: So

**Unknown User** [10:23:34]: I will wait for you to provide me this link and that will be a very good step as well.

**Unknown User** [10:23:38]: Yes.

**Unknown User** [10:23:56]: Does active directory support natively photo of the person, a profile picture?

**Unknown User** [10:24:05]: Is there a field in active directory where that can go as well?

**Ankit Choudhary** [10:24:11]: I think user can upload their photo from their side as well.

**Ankit Choudhary** [10:24:15]: I understand, and obviously

**Unknown User** [10:24:17]: that happens when you manage your account, right?

**Unknown User** [10:24:24]: And I always wanted to be able to go to something like this and explore the organization.

**Unknown User** [10:24:37]: And this is what I would like to be complete.

**Unknown User** [10:24:47]: So that the organization is visible to the user.

**Unknown User** [10:24:52]: The

**Ankit Choudhary** [10:24:52]: hierarchy you're talking about Well, also, also,

**Unknown User** [10:24:59]: is it true that none of these people have a profile picture?

**Unknown User** [10:25:03]: can't believe I mean, evidently, because you have Marinda has it, but no one else.

**Unknown User** [10:25:10]: So I think they

**Ankit Choudhary** [10:25:11]: didn't upload from the Office 365 side.

**Ankit Choudhary** [10:25:14]: That's right.

**Ankit Choudhary** [10:25:14]: And I would like

**Unknown User** [10:25:16]: to upload And then they can say, oh, I don't like it.

**Unknown User** [10:25:21]: Can you change And then then we will change it, right?

**Unknown User** [10:25:25]: But it should be something that each of us has.

**Unknown User** [10:25:31]: Because it is a very important way, in my opinion, to create a team so that we know everyone how they look like.

**Unknown User** [10:25:43]: You know, we are human, we like that.

**Unknown User** [10:25:46]: Absolutely.

**Unknown User** [10:25:47]: When we had the orientation with Hiba on Monday, remember telling her, please upload your profile picture.

**Unknown User** [10:26:00]: And she didn't.

**Unknown User** [10:26:04]: Right?

**Unknown User** [10:26:06]: So back to the question, is

**Unknown User** [10:26:13]: there in active directory a place where the profile picture can be stored.

**Unknown User** [10:26:23]: And it's okay if you don't have the answer, just find the answer, okay?

**Unknown User** [10:26:28]: Sure.

**Unknown User** [10:26:30]: All I think we can

**Ankit Choudhary** [10:26:35]: do it.

**Ankit Choudhary** [10:26:37]: Their option is available in Active Directory as And the same picture is showing here.

**Ankit Choudhary** [10:26:44]: which I uploaded from my outlook or from my teams because everything sync with each other.

**Ankit Choudhary** [10:26:51]: So if user upload the picture from their side as well, that will appear in our active directory.

**Ankit Choudhary** [10:26:57]: Perfect.

**Ankit Choudhary** [10:26:58]: Okay.

**Ankit Choudhary** [10:27:00]: So also, also, you know, I'm

**Unknown User** [10:27:04]: ignorant and lazy.

**Unknown User** [10:27:06]: Give me the entry point where I can explore active directory data fields and and relationships and and the hierarchical view of the organization, ideally, right?

**Unknown User** [10:27:25]: So let's work on that as well.

**Unknown User** [10:27:31]: Now, you said one of the things you said, let's discuss it on our call.

**Unknown User** [10:27:41]: I don't remember what it was.

**Unknown User** [10:27:44]: Yes.

**Unknown User** [10:27:44]: That is about

**Ankit Choudhary** [10:27:45]: the printer.

**Ankit Choudhary** [10:27:46]: You told me to go to Al-Sila for the printer, but I checked with Azhar.

**Ankit Choudhary** [10:27:52]: The printer will come tomorrow and the technician who set up the printer in our location in Al-Sila, because in Al-Sila, I think our user is sitting in the Regus office in the 24th floor, I believe, right?

**Ankit Choudhary** [10:28:08]: And the situation is same over there.

**Ankit Choudhary** [10:28:10]: They have completely Wi-Fi network.

**Ankit Choudhary** [10:28:12]: They do not have any LAN or anything over there.

**Ankit Choudhary** [10:28:14]: I check with Azhar.

**Ankit Choudhary** [10:28:15]: So same kind of problem will create again there.

**Ankit Choudhary** [10:28:19]: So temporary what I can do, we have a USB cable.

**Ankit Choudhary** [10:28:24]: I check with Azhar, he just informed me like the print, with the printer, there is no USB cable.

**Ankit Choudhary** [10:28:30]: They're providing any USB cable with the printer.

**Ankit Choudhary** [10:28:33]: So last time I ordered one USB cable for the printer.

**Ankit Choudhary** [10:28:37]: Let me stop you.

**Ankit Choudhary** [10:28:38]: I think I

**Unknown User** [10:28:39]: bought one when I bought the router.

**Unknown User** [10:28:42]: So checking the cupboard.

**Unknown User** [10:28:44]: The cable talking

**Ankit Choudhary** [10:28:47]: Yes.

**Ankit Choudhary** [10:28:47]: And there should be.

**Ankit Choudhary** [10:28:48]: Yeah, we do.

**Ankit Choudhary** [10:28:49]: We do have a cable.

**Ankit Choudhary** [10:28:50]: I know.

**Ankit Choudhary** [10:28:50]: Okay.

**Ankit Choudhary** [10:28:51]: But tomorrow when they deliver the printer,

**Unknown User** [10:28:55]: do they unpack it as well.

**Unknown User** [10:28:57]: So they take away the packaging material, etc.

**Unknown User** [10:29:01]: Or tomorrow is just the delivery.

**Unknown User** [10:29:03]: Just the delivery.

**Unknown User** [10:29:04]: Just

**Ankit Choudhary** [10:29:04]: the delivery tomorrow.

**Ankit Choudhary** [10:29:06]: After two days, engineer or the technician will come the cannon from the cannon side and he will like open box and unbox the printer over there and then he will just show someone who will who is available over there he just turn on and give some test printer and that's it.

**Ankit Choudhary** [10:29:33]: I know that these are two separate moments

**Unknown User** [10:29:36]: and yes, you don't need to be there for the delivery, as long as they don't leave it on the corridor or they don't leave it in the, you know, elevator shaft, you it has to be in the office.

**Unknown User** [10:29:51]: So are we sure that today, as the package arrives, it will be put in the office?

**Unknown User** [10:29:58]: Yes,

**Ankit Choudhary** [10:29:59]: as I told him, like you do not need to come today for delivery.

**Ankit Choudhary** [10:30:02]: But at the time of setup, complete setup, you have to come if like, suppose if I need to set up for my users, so I have to go to set up the printer.

**Ankit Choudhary** [10:30:11]: In that case, I have to there, but for delivery, you do not need to come Okay, today is the delivery

**Unknown User** [10:30:20]: tomorrow.

**Unknown User** [10:30:20]: Tomorrow is the delivery and the box will in the office.

**Unknown User** [10:30:26]: Correct.

**Unknown User** [10:30:26]: Correct.

**Unknown User** [10:30:27]: It will be inside the office.

**Unknown User** [10:30:30]: right.

**Unknown User** [10:30:30]: Absolutely.

**Unknown User** [10:30:31]: Yes.

**Unknown User** [10:30:32]: Is Maria aware that this big box is arriving?

**Unknown User** [10:30:38]: I'm not Can you please make Maria aware so that she knows?

**Unknown User** [10:30:44]: Okay, I'll inform Because Veron said to coordinate with Maria, okay?

**Unknown User** [10:30:50]: Okay.

**Unknown User** [10:30:52]: Now, you said in two days the Canon engineer will or after two days.

**Unknown User** [10:31:00]: Do you mean on Friday or Monday?

**Unknown User** [10:31:03]: On Monday.

**Unknown User** [10:31:05]: So on Monday the Canon engineer will come.

**Unknown User** [10:31:08]: Do you know if it is in the morning or in the afternoon?

**Unknown User** [10:31:13]: I'm not sure right

**Ankit Choudhary** [10:31:16]: Make sure

**Unknown User** [10:31:17]: that that you know, because yes, I want you to be Sure.

**Unknown User** [10:31:27]: And it's fine if you need to be there half a day, no problem.

**Unknown User** [10:31:31]: You just work with your computer there.

**Unknown User** [10:31:33]: Actually, it could be good do one thing.

**Unknown User** [10:31:38]: Let's discuss it today, right now, but close the printer issue before.

**Unknown User** [10:31:47]: So, Isar should tell you Canon directly.

**Unknown User** [10:31:54]: when the canon engineer is coming is it in the morning or in the afternoon ideally what time and then you should be there with the canon engineer making sure that you learn everything that needs to be learned to connect the printer to a windows notebook a mac notebook that that you know You know,

**Unknown User** [10:32:24]: double- sided print, collated print, A3 print, all those kinds of things.

**Unknown User** [10:32:34]: Probably our arrangement includes A4 paper, but I don't know if it includes A3 paper, the larger paper, So talk to Marinda, and ask her if you can bring paper to that location so that the printer is ready to print both A4 and A3, okay?

**Unknown User** [10:33:09]: All right.

**Unknown User** [10:33:10]: And as I told you, I will cover the cost of your transportation and you need to tell how to send you the money.

**Unknown User** [10:33:23]: Okay.

**Unknown User** [10:33:31]: And just to be super sure, please ask for confirmation that the packaging material will be dealt either by tech or by canon, so that we don't have to think about how to throw away all the cardboard and all the plastic.

**Unknown User** [10:33:55]: Okay.

**Unknown User** [10:33:56]: Okay.

**Unknown User** [10:33:58]: All right.

**Unknown User** [10:34:01]: let's go back to what you can do for the rest of the time that you are in Alcila, either because you are waiting for the technician because they are late.

**Unknown User** [10:34:12]: or they were on time, but it is good for you to spend another couple of hours doing something And what you can do is to go to everyone in the Alcila office on the 25th floor and delete the printer driver for the tech printer.

**Unknown User** [10:34:44]: Did make you full member already or not yet?

**Unknown User** [10:34:49]: I am now gonna make you full member because this is ridiculous.

**Unknown User** [10:35:00]: Sorry

**Unknown User** [10:36:41]: Okay, so I made you a full member to the Slack channel.

**Unknown User** [10:36:47]: Okay.

**Unknown User** [10:36:48]: Or Slack workspace, which means that you can be a member of the various channels as needed.

**Unknown User** [10:36:59]: And you will see all the public channels, okay, which you couldn't see before.

**Unknown User** [10:37:04]: And I see in a bunch of channels.

**Unknown User** [10:37:16]: And I will say Monday, Ankit will walk around and ask you to let him delete tech printer.

**Unknown User** [10:37:46]: What

**Ankit Choudhary** [10:37:47]: is a stack printer driver?

**Ankit Choudhary** [10:37:50]: Their own printer, their different printer.

**Ankit Choudhary** [10:37:54]: That's So on the corridor,

**Unknown User** [10:38:01]: outside of the Liban office, there is a shared printer for everyone.

**Unknown User** [10:38:08]: Okay.

**Unknown User** [10:38:09]: And that I don't know, 10 times more expensive to use than ours.

**Unknown User** [10:38:17]: And I just received a request from finance to please check because they spent 5,000 dirham for printing using the shared printer last And they shouldn't.

**Unknown User** [10:38:36]: So rather than just asking them, please use the tech printer, sorry, the only one printer, which is in their office.

**Unknown User** [10:38:46]: We will delete the printer driver.

**Unknown User** [10:38:50]: Understand.

**Unknown User** [10:38:52]: And by the way, it could very well be that one of the reasons they are using the shared printer is because it has A3.

**Unknown User** [10:39:07]: And they don't realize that the other printer has A3 as Because when they select the other printer, it says, sorry, I print A3 because I don't have paper.

**Unknown User** [10:39:21]: Okay.

**Ankit Choudhary** [10:39:24]: rather than bringing just

**Unknown User** [10:39:26]: package of 500 A3, bring two.

**Unknown User** [10:39:33]: And you feel 24 printer with A3, and you feel the 25th level printer with A3 If you remember, actually, I don't remember where is the printer in the office, it's there 4368

**Ankit Choudhary** [10:40:00]: Well, the only room

**Unknown User** [10:40:04]: Yes.

**Unknown User** [10:40:05]: No, no, sorry, what did I think 4368,

**Ankit Choudhary** [10:40:09]: the room number you required last time.

**Ankit Choudhary** [10:40:12]: That's in addux.

**Ankit Choudhary** [10:40:13]: That's in

**Unknown User** [10:40:14]: Yeah, okay.

**Unknown User** [10:40:17]: Okay.

**Unknown User** [10:40:19]: The room shared by everyone, Randy, Ivan, Toby, Hela has a printer in And I was just trying to remember where physically is the printer, but it's in Okay.

**Unknown User** [10:40:44]: Anything else that we want to cover on this

**Ankit Choudhary** [10:40:47]: meeting?

**Unknown User** [10:41:13]: What's your suggestion?

**Ankit Choudhary** [10:41:17]: Temporary I added that domain, which considered as a, like as per the Microsoft, the mail flow rule will also not able to protect those kind of email, which is considered as a highly spam.

**Ankit Choudhary** [10:41:31]: Like those emails will not bypass the mail flow rules well.

**Ankit Choudhary** [10:41:36]: So as per the Microsoft, Microsoft recommended to add those kind of sender into the tenant allow and block And that is only for 45 days.

**Ankit Choudhary** [10:41:46]: That is not a permanent.

**Ankit Choudhary** [10:41:48]: Really?

**Ankit Choudhary** [10:41:48]: Yes.

**Unknown User** [10:41:53]: And

**Unknown User** [10:42:01]: basically, I think

**Ankit Choudhary** [10:42:02]: the issue was happening with that particular center because their SPF is not picturing from projected, but I cannot explain this to Michael.

**Ankit Choudhary** [10:42:14]: No, no, that's okay.

**Ankit Choudhary** [10:42:15]: That's okay.

**Unknown User** [10:42:18]: how do other people live?

**Unknown User** [10:42:24]: Do they have humans dedicated to adding records to the allow list?

**Unknown User** [10:42:34]: And that is what they do every day, each day for all their lives?

**Unknown User** [10:42:40]: I

**Ankit Choudhary** [10:42:40]: know.

**Ankit Choudhary** [10:42:41]: It's a very, like I need one person for this particular task only, who always do this rightly, rightly, rightly.

**Ankit Choudhary** [10:42:48]: Exactly.

**Unknown User** [10:42:51]: Tell Mahindra, tell Mahindra, good news, we need another person just for this.

**Unknown User** [10:42:58]: It's crazy.

**Unknown User** [10:42:59]: Okay,

**Unknown User** [10:43:06]: I'm planning to open one

**Ankit Choudhary** [10:43:06]: ticket with the Microsoft.

**Ankit Choudhary** [10:43:08]: if they have something in a background.

**Ankit Choudhary** [10:43:11]: So if they can suggest Okay.

**Ankit Choudhary** [10:43:15]: In the meantime, in the meantime,

**Unknown User** [10:43:19]: a task for is to generate a domain names, airlines, hotels, standard platforms for software, et cetera, etc.

**Unknown User** [10:43:40]: And maybe it will be a thousand, maybe it'll be between a million, It's a list, And a task for you is to make that you upload this in bulk.

**Ankit Choudhary** [10:44:07]: I'm okay with that.

**Ankit Choudhary** [10:44:08]: Because you cannot manually create all the

**Unknown User** [10:44:09]: list

**Ankit Choudhary** [10:44:11]: in I'll check it.

**Ankit Choudhary** [10:44:13]: If there is a PowerShell command to add all of them in a bulk.

**Ankit Choudhary** [10:44:17]: That's not a problem.

**Ankit Choudhary** [10:44:18]: I'll find it.

**Ankit Choudhary** [10:44:20]: But the second thing, if email consider as a highly spam, then the same thing will happen.

**Ankit Choudhary** [10:44:27]: The mail flow rule will not able to bypass the spam, like spam filtering will not able to bypass the mail flow rule and then start moving to the quarantine.

**Ankit Choudhary** [10:44:37]: So the important thing which we need to understand, if any email, which is important for us, and those emails are considered as an highly spam, then how we can bypass those emails from the spam filtering and those emails should be moved in our inbox.

**Ankit Choudhary** [10:44:53]: So on that basis, I'm trying to open one ticket with the Microsoft to understand, is there any way through which we can do it, because temporary solution, like As I mentioned, it's added for 45 days, but this is just for 45 days.

**Ankit Choudhary** [10:45:07]: We need it for permanent.

**Ankit Choudhary** [10:45:09]: So I'm just planning to open one ticket with the Microsoft to understand, is there any way through which we can the email or the domain of any particular sender from whom the email which we are receiving that is really important.

**Ankit Choudhary** [10:45:24]: And the emails are considered as a highly spam, we want those emails anyhow in our inbox.

**Ankit Choudhary** [10:45:30]: So your spam filtering should be bypassed.

**Ankit Choudhary** [10:45:32]: and those emails should be moved in our inbox.

**Ankit Choudhary** [10:45:36]: I'm thing.

**Ankit Choudhary** [10:45:39]: Okay, so let's see.

**Ankit Choudhary** [10:45:40]: Yeah, it's

**Unknown User** [10:45:42]: urgent, so please raise that ticket with Microsoft and I will still generate that list of domains and then yeah,

**Ankit Choudhary** [10:45:48]: what be done.

**Ankit Choudhary** [10:45:49]: Okay, sure, sure, sure,

**Ankit Choudhary** [10:45:56]: Yeah, that's it.

**Ankit Choudhary** [10:45:57]: The small things we'll discuss later, no problem over.

**Ankit Choudhary** [10:46:00]: There's a lot of small things coming in the mind and I'm working, yes, you can discuss later.

**Ankit Choudhary** [10:46:04]: These are the important one which we discuss already.

**Ankit Choudhary** [10:46:06]: Thank you.

---
*Backed up from MeetGeek on 2026-03-30 08:43*
