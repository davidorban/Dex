# IT Assets and Intune Integration

**Date:** 2026-03-03
**Duration:** Unknown
**Meeting ID:** fd4276c8-5f48-4121-a195-0561258d8243

## Participants
- *Participants not listed*

### Summary

The meeting focused on aligning IT asset records between SharePoint, Active Directory (AD), and Intune. Ankit explained the current SharePoint hardware list structure (individual items per device), duplication issues, and that Intune syncs laptop data while peripherals require manual entry. They discussed software cataloging limitations, local admin password practices, and the need for clearer policies. David and Ankit agreed that AD contains office and manager fields, which can be exported and combined with Intune/SharePoint data for location-based enrollment reporting; Ankit will request fuller AD data from Nisha and check Intune's device location capability. The conversation closed with updates on onboarding templates and provisioning for the Nigeria team and a plan for follow-ups as needed.

## Full Transcript

**Unknown speaker** [11:02:55]: I would like to

**David Orban** [11:02:56]: understand what we can bring together what is the best way and place to manage them right so Ideally

**David Orban** [11:03:12]: everything should live in active directory right and That is the level of integration within Tune that also we should aim to have.

**David Orban** [11:03:28]: So

**David Orban** [11:03:34]: are the fields in Active Directory something we can personalize or they are fixed as far as you know.

**David Orban** [11:03:48]: Inactive directory,

**Ankit Choudhary** [11:03:49]: what what exactly are you talking about to fix?

**Ankit Choudhary** [11:03:53]: So

**David Orban** [11:03:54]: the asset tracking is now in a separate list, in a separate table, right?

**Ankit Choudhary** [11:04:06]: Correct, yes.

**Ankit Choudhary** [11:04:08]: in SharePoint in that intranet SharePoint site which you have created so we have two options mainly is a one is IT hardware asset and second one is IT software asset so I think the primary one is the IT hardware assets because that is important and we need the records of every single device or which

**Ankit Choudhary** [11:04:30]: we are providing to the users so Previously, Shidam shared that one file which she was managing earlier, and she had the information about the users who has the personal device and who get the device from our side, like a monitor, SDM cable, and the docking station.

**Ankit Choudhary** [11:04:51]: So she mentioned all the details over there.

**Ankit Choudhary** [11:04:54]: So I conclude all the information in a one Excel sheet, and I create the separate entity for every single device.

**Ankit Choudhary** [11:05:03]: if user has the mouse or keyboard so I create a separate entity for that if user has a laptop I create a separate and so I create a separate entity for every single device so now if you go to the IT hardware asset you will see could be possible you will see like my name multiple time because I get

**Ankit Choudhary** [11:05:22]: the multiple device so on that basis I created the entries over there so in the same way I'm working like If you want, I can show you.

**Ankit Choudhary** [11:05:35]: I can share you.

**David Orban** [11:05:37]: Yeah, I already see.

**David Orban** [11:05:38]: So, for example, Stephanie has a monitor, an HDMI connector and a keyboard and the mouse.

**David Orban** [11:05:47]: Correct.

**David Orban** [11:05:48]: Then you can

**Ankit Choudhary** [11:05:48]: see multiple entries for Stephanie.

**Ankit Choudhary** [11:05:51]: Yes.

**David Orban** [11:05:52]: And it is a bit weird that the column is called title.

**David Orban** [11:05:58]: In

**Ankit Choudhary** [11:05:58]: title earlier it was showing the host name of the computer the computer name basically so what I decided because that creating the confusion like like this device assigned to which user because sometimes because we did not create it particularly host name for all the user it is still confused some

**Ankit Choudhary** [11:06:15]: users name is showing under the host name and some different kind of numbers is showing under the host name because we still did not decide which kind of name we can provide to all the devices.

**Ankit Choudhary** [11:06:26]: So it is still confusion.

**Ankit Choudhary** [11:06:27]: So that's the reason under title I put the name of the users.

**Ankit Choudhary** [11:06:32]: So the confusion will be not create more here.

**David Orban** [11:06:36]: Okay.

**David Orban** [11:06:37]: And for example, I see Lee Pillay laptop twice with the same serial number.

**David Orban** [11:06:48]: Which user?

**David Orban** [11:06:52]: Lee Pillay.

**Ankit Choudhary** [11:06:55]: Lipile is one entry.

**Ankit Choudhary** [11:07:02]: If you order

**David Orban** [11:07:03]: by title.

**David Orban** [11:07:05]: I can see

**Ankit Choudhary** [11:07:06]: two entries showing for lipile.

**Ankit Choudhary** [11:07:07]: I'll check it, no worries.

**Ankit Choudhary** [11:07:09]: I'll try to remove the duplicates from here.

**Ankit Choudhary** [11:07:11]: Okay.

**David Orban** [11:07:13]: Now, what relationship does this have with active directory, if any?

**David Orban** [11:07:25]: Okay,

**Ankit Choudhary** [11:07:26]: so the SharePoint information or the details which we have here in the SharePoint site.

**Ankit Choudhary** [11:07:32]: This is something because suppose I receive a new request from the user.

**Ankit Choudhary** [11:07:40]: There are two things, one I can edit manually over here directly from the SharePoint site and second one suppose if I enroll any device in in tune.

**Ankit Choudhary** [11:07:48]: So that device information will replicate over here in this sharepoint site.

**Ankit Choudhary** [11:07:54]: So laptop information will be sync over here.

**Ankit Choudhary** [11:07:57]: This is fine, but the keyboard, mouse or monitor information will not replicate.

**Ankit Choudhary** [11:08:03]: So I need to add those information here directly in this site.

**David Orban** [11:08:07]: So in that sense, it is correct that it is separate.

**David Orban** [11:08:12]: We cannot and should not rely entirely

**Ankit Choudhary** [11:08:16]: an active directory.

**Ankit Choudhary** [11:08:17]: Correct, correct.

**Ankit Choudhary** [11:08:18]: Because active directory, it will only appear the laptop information, not the keyboard, mouse,

**David Orban** [11:08:23]: or other information over there.

**David Orban** [11:08:24]: Yes.

**David Orban** [11:08:27]: Now, what about the software part?

**David Orban** [11:08:32]: So the IT software assets

**Ankit Choudhary** [11:08:36]: list.

**Ankit Choudhary** [11:08:38]: So in software part, I was looking, but it is a bit confusing for me.

**Ankit Choudhary** [11:08:43]: What exactly we want over here?

**Ankit Choudhary** [11:08:46]: Because suppose we have Asana, company portal, Chrome, these are the software which we publish from the from the Intune.

**Ankit Choudhary** [11:08:59]: And what exactly our end goal?

**Ankit Choudhary** [11:09:04]: Our end goal is to understand which kind of software user using in their laptop because it depends on the requirement of the user.

**Ankit Choudhary** [11:09:11]: Suppose I'm the user, I need this particular software for my requirement.

**Ankit Choudhary** [11:09:16]: X, Y, Z, if any other user using their laptop and that person is working in a different department, so it could be possible that user using a different software or could be possible there is some software that user wanted to install manually, which is not published from the Intune.

**Ankit Choudhary** [11:09:34]: We want only those software information which is, which we publish from the Intune, or we need all the information detailed by the users, which user using in their laptop.

**Ankit Choudhary** [11:09:45]: So this is confusing over here.

**Ankit Choudhary** [11:09:49]: And this create a more complications when we're creating the rules over here.

**Ankit Choudhary** [11:09:55]: Well,

**David Orban** [11:10:00]: we need to... cataloging the applications installed through the portal is trivial because by definition a notebook that is enrolled in Intune will have the software installed through the portal and there is no surprise about that and as a consequence we have to gather different information, not just

**David Orban** [11:10:38]: about the software that is already in the portal.

**David Orban** [11:10:44]: Now, is it true, is it correct that the, that without the admin access, the users cannot install additional software, right?

**David Orban** [11:11:03]: Absolutely.

**Ankit Choudhary** [11:11:04]: There's a few software which I think user can install, but everything user cannot.

**David Orban** [11:11:16]: And so that means that for their company provided computer, they would have to tell us what they need.

**David Orban** [11:11:27]: Absolutely,

**Ankit Choudhary** [11:11:28]: absolutely.

**Ankit Choudhary** [11:11:28]: Suppose user want to install any printer software.

**Ankit Choudhary** [11:11:32]: So by default, user cannot install the printer software from their side because when user trying to install it, it will spawn for the password.

**Ankit Choudhary** [11:11:39]: So user need to reach out to me for the password.

**Ankit Choudhary** [11:11:44]: I will provide the password to the user and then user can use that password temporary and then user can use it for the installation.

**Ankit Choudhary** [11:11:51]: And I'm not sure if there any approval process or not, because right now we just go ahead and provide the password directly, because in a lot of organizations, I saw this scenario that particular requests should be approved from their manager, and then we provide the password and all.

**Ankit Choudhary** [11:12:08]: Okay, we

**David Orban** [11:12:09]: will go there later.

**David Orban** [11:12:12]: And you told me that the password is temporary, so they can only use it once, and then if they need to

**Ankit Choudhary** [11:12:19]: install something else.

**Ankit Choudhary** [11:12:20]: We can generate it again.

**Ankit Choudhary** [11:12:21]: We can change the password later, yes.

**Ankit Choudhary** [11:12:26]: But

**David Orban** [11:12:26]: if we don't change it, but if we don't change it, it is still working.

**Ankit Choudhary** [11:12:33]: Let me show you one thing.

**Ankit Choudhary** [11:12:39]: Share my screen.

**Ankit Choudhary** [11:12:45]: Can you see my screen?

**Ankit Choudhary** [11:12:46]: Yes.

**Ankit Choudhary** [11:12:48]: So like this is, these are the devices and these are the compliance.

**Ankit Choudhary** [11:12:52]: So let me open this Anna's laptop here.

**Ankit Choudhary** [11:12:55]: This is Anna device.

**Ankit Choudhary** [11:12:58]: And if you go to local admin password, this is the password for the local admin, for example.

**Ankit Choudhary** [11:13:07]: so when she wanted to install any third- party software which is not published from our site it will ask for this password and this is the admin account like this is the user account which she need to enter over there so she need to use this information to install the application and after the

**Ankit Choudhary** [11:13:26]: installation we can simply do the from here let me show you

**Ankit Choudhary** [11:13:41]: From the overview, we have option over here rotate the local admin password.

**Ankit Choudhary** [11:13:47]: So once I'll click on rotate the local admin password, then the password which I provided that will change.

**Ankit Choudhary** [11:13:54]: So the same password which I provided to her, that password will not work anymore in the future.

**Ankit Choudhary** [11:13:59]: After the installation will work for

**David Orban** [11:14:02]: her.

**David Orban** [11:14:09]: Here we are in in tune.

**David Orban** [11:14:13]: Yes.

**David Orban** [11:14:14]: Is the location, the physical location of the device tracked anyway?

**Ankit Choudhary** [11:14:36]: If I understand you correctly, you are saying suppose if anyone lost the device and how we can drag that device, correct?

**Ankit Choudhary** [11:14:43]: Yes.

**Ankit Choudhary** [11:14:45]: Well, that option should be available, but I need to check right now I'm not sure.

**Ankit Choudhary** [11:14:52]: Okay,

**David Orban** [11:14:52]: please take note and let me know.

**David Orban** [11:14:56]: Okay.

**Ankit Choudhary** [11:15:12]: Okay.

**David Orban** [11:15:13]: And for each user we have on inactive directory a

**David Orban** [11:15:26]: information about what office they are in, right?

**David Orban** [11:15:30]: Yes.

**David Orban** [11:15:33]: Can you show me that?

**David Orban** [11:15:40]: This is the

**Ankit Choudhary** [11:15:41]: active directory.

**Ankit Choudhary** [11:15:43]: And suppose, let me.

**Ankit Choudhary** [11:15:47]: This is my account.

**Ankit Choudhary** [11:15:51]: And if I go to devices.

**Ankit Choudhary** [11:15:52]: So right now, this is the devices which I'm using right now, but this is the main device which is compliant.

**Ankit Choudhary** [11:16:10]: So mouth.

**Ankit Choudhary** [11:16:16]: So this device, the last one, this is and roll in Intium.

**Ankit Choudhary** [11:16:21]: This is the other device like the laptop which I'm using right now here in my home.

**Ankit Choudhary** [11:16:26]: I think this one is this one is the same one.

**Ankit Choudhary** [11:16:31]: I use this account on multiple device, but right now this one is the Android which I'm using from the office.

**Ankit Choudhary** [11:16:45]: Bitlogger keys here.

**Ankit Choudhary** [11:16:47]: Sorry, could you please repeat again your question what what you were looking for?

**Ankit Choudhary** [11:16:51]: That's that's

**David Orban** [11:16:51]: okay.

**David Orban** [11:16:52]: So you as a person work in a given office.

**David Orban** [11:16:58]: And we we have the ability to record that information of of what is that you are at ADACS and that your office number is 4371 or whatever it is.

**David Orban** [11:17:14]: Where is it?

**David Orban** [11:17:16]: Where can we record that?

**David Orban** [11:17:18]: That information

**Ankit Choudhary** [11:17:19]: we can record over here under the overview.

**Ankit Choudhary** [11:17:22]: Let me show you under properties.

**Ankit Choudhary** [11:17:26]: So here is the complete information about the user.

**Ankit Choudhary** [11:17:28]: So suppose I am working edX tower, so I need to just put the office location over here.

**Ankit Choudhary** [11:17:35]: So I can mention the room number is this, edX tower, something like that.

**Ankit Choudhary** [11:17:42]: Okay, and here is

**David Orban** [11:17:43]: the manager as well, manager information.

**David Orban** [11:17:47]: And where is the role?

**David Orban** [11:17:52]: Job title

**Ankit Choudhary** [11:17:52]: is here.

**David Orban** [11:17:53]: Oh, job title, okay, perfect.

**David Orban** [11:17:56]: Other information like contact information,

**Ankit Choudhary** [11:17:58]: other information if you would like to enter over here, so we can add the other information here.

**Ankit Choudhary** [11:18:04]: We have other tabs as well, like contact information, identity, and variant control on-premises, on-premises

**David Orban** [11:18:12]: not required here.

**David Orban** [11:18:13]: We are not using it.

**David Orban** [11:18:14]: Is there a way to see this in a list view and edit it in a list view, like we have it for the SharePoint lists?

**David Orban** [11:18:26]: For all this

**Ankit Choudhary** [11:18:26]: information?

**David Orban** [11:18:30]: Or maybe, because I want to make sure that everyone's office location is recorded, right?

**David Orban** [11:18:40]: And then we can say, we can answer questions from Michael who is saying, okay, but how many of the notebooks in Abu Dhabi are enrolled in iTunes?

**David Orban** [11:19:00]: And we can associate the location of the person with the enrollment status of their computer.

**David Orban** [11:19:11]: All

**Ankit Choudhary** [11:19:12]: right.

**Ankit Choudhary** [11:19:13]: So this is possible.

**Ankit Choudhary** [11:19:15]: I can do this by a PowerShell.

**Ankit Choudhary** [11:19:17]: I think that is possible from the Microsoft Graph PowerShell.

**Ankit Choudhary** [11:19:21]: But I need the information which I think Nisha can provide.

**Ankit Choudhary** [11:19:27]: Well,

**David Orban** [11:19:28]: yes, the active directory information has to be full, correct?

**David Orban** [11:19:33]: Absolutely.

**Ankit Choudhary** [11:19:34]: So once Nisha will provide me, because last, I think, last two or three times, I saw like, whenever she shared the information of the user, she provided the reporting manager and the location of the user as well.

**Ankit Choudhary** [11:19:47]: But before that, whatever information she provided the username, she never provided me the role and the other information.

**Ankit Choudhary** [11:19:54]: So if she can create one list for me where she can mention the relevant information which she wanted me to update in the in this active directory, I can do this, but I need those information from her.

**David Orban** [11:20:08]: Correct, correct.

**David Orban** [11:20:10]: Okay.

**David Orban** [11:20:12]: And maybe tomorrow, if we are in the office, we can ask her directly.

**Ankit Choudhary** [11:20:18]: Sure, sure, sure.

**Ankit Choudhary** [11:20:20]: Okay.

**Ankit Choudhary** [11:20:21]: Yeah, okay.

**David Orban** [11:20:33]: Can

**David Orban** [11:20:42]: you show me if in active directory there is a place to record a profile picture of a person?

**Ankit Choudhary** [11:20:52]: Let me check.

**Ankit Choudhary** [11:20:57]: In active directory, let me check if it's possible from active directory.

**Ankit Choudhary** [11:21:10]: I think this is the option to apply a camera here.

**Ankit Choudhary** [11:21:13]: The user can upload it manually or I can also upload the picture for the user.

**David Orban** [11:21:33]: But I never did

**Ankit Choudhary** [11:21:33]: from the PowerShell, but we can try if it's possible from the PowerShell, but I think it could be complicated because we need to provide the location on our system, then we have to run the PowerShell command for everyone.

**Ankit Choudhary** [11:21:47]: So we can do

**David Orban** [11:21:48]: this.

**David Orban** [11:21:49]: If I wanted to play around and generate reports myself, is Power BI a good way to do it?

**David Orban** [11:22:00]: report

**Ankit Choudhary** [11:22:01]: for which kind of report you would like to create for example

**David Orban** [11:22:06]: intersecting

**David Orban** [11:22:11]: information coming from the hardware asset sharepoint site with the active director information telling me where are the offices where the people work and then being able to say that 60% at Adax is enrolled in Intune, that 50% in Alcela is enrolled in Intune, and I don't know, 0% in New York or

**David Orban** [11:22:48]: London are enrolled in Intune, whatever it is.

**Ankit Choudhary** [11:22:56]: So you can, I think you can directly export the result or the output from the Intune.

**Ankit Choudhary** [11:23:02]: Because if I go to properties, what information we have here.

**Ankit Choudhary** [11:23:06]: We can try to export the data because it could be possible.

**Ankit Choudhary** [11:23:10]: And what I'm thinking, I think location will also appear over here in this one.

**Ankit Choudhary** [11:23:16]: If we export the Android device information, I'm not sure it will appear the location or not.

**Ankit Choudhary** [11:23:26]: But it will appear to the location, so it will be easy for you to filter it out.

**Ankit Choudhary** [11:23:32]: And then you can, on that basis, you can check which user using their laptop from Alcira and which user using their laptop in the edX.

**Ankit Choudhary** [11:23:41]: Something like that.

**Ankit Choudhary** [11:23:43]: Okay.

**Ankit Choudhary** [11:23:45]: But the way in the power BI, I'm not sure how to use I'm sure, I'm exactly not sure how it will work.

**Ankit Choudhary** [11:23:52]: Okay.

**Ankit Choudhary** [11:23:53]: Or we can export the properties information and then you can filter it out.

**David Orban** [11:23:59]: Okay.

**David Orban** [11:24:03]: All right.

**David Orban** [11:24:07]: So,

**David Orban** [11:24:15]: I will play around with this and then and then see what questions to ask about it eventually.

**David Orban** [11:24:33]: Now the offboarding of AI is complete, I've seen And the onboarding of the Nigeria team is ongoing.

**David Orban** [11:24:51]: Have you been able to create the Slack users and the Asana

**Ankit Choudhary** [11:24:55]: users?

**Ankit Choudhary** [11:24:58]: Yes, I provided the Asana, SLAG, Nitro, Testroid.

**Ankit Choudhary** [11:25:04]: So these four software access I have already provided to them.

**Ankit Choudhary** [11:25:08]: And today I work with the Ron as well, and I fix his team's issue and SLAG issue.

**Ankit Choudhary** [11:25:14]: So now he's able to log in in both application.

**Ankit Choudhary** [11:25:17]: I'm not sure he need these Asana, Testroid, or other application.

**Ankit Choudhary** [11:25:24]: If you allow me, I can create the the accounts for for him, but I'm not sure he need those accounts.

**Ankit Choudhary** [11:25:31]: And shall I consider him as a new hire?

**Ankit Choudhary** [11:25:33]: Shall I add him in onboarding?

**Ankit Choudhary** [11:25:37]: We are

**David Orban** [11:25:38]: talking about the Nigeria team.

**David Orban** [11:25:41]: No,

**Ankit Choudhary** [11:25:41]: I'm talking about the wrong one.

**Ankit Choudhary** [11:25:42]: Nigeria for Nigerian user, I already created the onboarding template.

**Ankit Choudhary** [11:25:47]: But for Ron, should I need, do I need to create the onboarding template for?

**Ankit Choudhary** [11:25:52]: Oh, no,

**David Orban** [11:25:54]: no, no.

**David Orban** [11:25:55]: At least for the moment, he doesn't need to use Asana or Treasury, no.

**David Orban** [11:26:01]: Okay, cool.

**David Orban** [11:26:05]: Ron will go back to Australia and he will keep managing his separate business, but he will be here for until the end of April.

**David Orban** [11:26:17]: because he will hire someone working for him, but being permanently based in Abu Dhabi.

**David Orban** [11:26:27]: So that person will also need an Aldi one email, slack, and maybe they will also need more, but we will understand that separately.

**David Orban** [11:26:47]: Okay.

**David Orban** [11:26:48]: Sure.

**David Orban** [11:26:50]: All right.

**David Orban** [11:26:52]: So these were the things that I wanted to ask.

**David Orban** [11:26:58]: Anything from your side?

**Ankit Choudhary** [11:27:01]: David, I'm good.

**Ankit Choudhary** [11:27:04]: If something will come in mind, I'll definitely ask Okay,

**David Orban** [11:27:09]: okay.

**David Orban** [11:27:10]: And do we know if tomorrow we are back in the office yet?

**David Orban** [11:27:16]: Not

**Ankit Choudhary** [11:27:17]: update.

**Ankit Choudhary** [11:27:18]: I'm still waiting for the update from because last time I saw Miranda's email where she mentioned like we need to work on two days, but I didn't get any update from the Miranda or any other team members.

**Ankit Choudhary** [11:27:33]: still waiting.

**David Orban** [11:27:34]: Okay.

**David Orban** [11:27:36]: All right.

**David Orban** [11:27:37]: Thank you.

**David Orban** [11:27:37]: Thanks, David.

**Ankit Choudhary** [11:27:39]: You have a great day.

---
*Backed up from MeetGeek on 2026-03-30 08:42*
