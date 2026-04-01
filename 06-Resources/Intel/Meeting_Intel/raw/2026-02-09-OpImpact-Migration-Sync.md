# OpImpact Migration Sync

**Date:** 2026-02-09
**Duration:** Unknown
**Meeting ID:** bf3973bc-fe37-4a96-838c-2331af8464bd

## Participants
- *Participants not listed*

### Summary

The meeting aligned responsibilities and timeline for a cloud-to-cloud migration from Google to Microsoft 365, covering scope, mailbox sizes (~19 GB), estimated migration duration (4–7 hours), DNS roles and record changes (MX/SPF/DMARC) without changing the registrar, billing and tenant setup requirements including credit-card and potential MFA bank confirmation, rollback and DNS backup procedures, security posture choices (temporary relaxed MFA, self-service password reset), license strategy (E3 generally, E5 for regulated users), user provisioning and pre-switch testing, and real-time coordination via a temporary Slack channel. Actionable next steps were assigned: tenant and users to be created, billing entered, migration scheduled for the proposed weekend window, DNS changes during the switchover, and post-migration hardening and reporting setup.

## Full Transcript

**David Orban** [11:58:58]: Test

**David Orban** [11:59:29]: Is there an echo maybe?

**David Orban** [11:59:30]: No, you are muted, so there is no echo.

**David Orban** [11:59:34]: Okay.

**David Orban** [11:59:35]: And if you are not muted, would there be?

**David Orban** [11:59:37]: Ankit?

**David Orban** [11:59:40]: Yes, yes, I'm not muted.

**David Orban** [11:59:44]: Okay, good.

**David Orban** [11:59:44]: And there is no echo.

**David Orban** [11:59:46]: All right.

**David Orban** [11:59:47]: Hello, Robert and welcome.

**David Orban** [11:59:49]: Hi, how are you?

**David Orban** [11:59:51]: You have a beautiful background.

**David Orban** [11:59:53]: Thank you.

**David Orban** [12:00:01]: So the objective of today's call is not operational, but to agree that we are on the same page with the things that need to happen and to agree who does what and when, so that the migration and the switchover is smooth and painless.

**David Orban** [12:00:30]: And so in order for that to go well, the call itself and that we can agree on who does what and when.

**David Orban** [12:00:45]: I prepared the document that I shared the migration guide as the reference and it is not setting stone.

**David Orban** [12:01:06]: It is for today's call.

**David Orban** [12:01:08]: And we can and we should both give voice to doubts or questions or suggest changes if anything in this guide is wrong and we want to modify it.

**Robert Mehler** [12:01:31]: Yeah, I've read through the guide.

**Robert Mehler** [12:01:33]: I've done numerous migrations.

**Robert Mehler** [12:01:36]: So my questions are, if I have a question, it's because I've read the document, and then I just have small questions that I would like to ask, meaning that everything else is fairly well understood, including have a credit card ready and everything to go, including a new window of time to run the

**Robert Mehler** [12:01:56]: migration.

**Robert Mehler** [12:01:57]: If I may, I'd like to ask a couple of questions.

**Robert Mehler** [12:02:01]: Considering that the largest and some total we have what 22 something like gig to migrate maybe a little bit more my question would be Approximately how long assuming no interruption upload download blah blah the best case scenario how long would it take I've been through transitions where it's 12

**Robert Mehler** [12:02:23]: hours DNS, TTL, 30 minutes, but nonetheless, who the hell knows until it all propagates and then the data comes in, you know, sinking, blah, blah.

**Robert Mehler** [12:02:33]: What's the estimation on basically three email boxes, no data, just email and calendar?

**Robert Mehler** [12:02:43]: And

**David Orban** [12:02:43]: so, Ankit.

**David Orban** [12:02:45]: Do you have any feedback on that?

**David Orban** [12:02:49]: Now, just to be explicit, this is from cloud to cloud.

**David Orban** [12:02:54]: We don't need to be downloading and reuploading any mailbox data.

**David Orban** [12:02:59]: Am I right?

**David Orban** [12:02:59]: Ankit?

**Ankit Choudhary** [12:03:06]: Yeah, right.

**Ankit Choudhary** [12:03:07]: If we if we are doing the cloud migration from G Suite to Office 365 and As Robert mentioned, like, we do have only one mailbox, which has most of the data is approximately 16 gig, I think, right?

**Ankit Choudhary** [12:03:20]: It's 19, over 19 gig.

**Ankit Choudhary** [12:03:22]: 19 gig.

**Ankit Choudhary** [12:03:24]: Okay.

**Ankit Choudhary** [12:03:25]: So I don't think so it will take a long time.

**Ankit Choudhary** [12:03:28]: It will take maximum four to five hours only, I think, more than, it will not go more than that.

**Ankit Choudhary** [12:03:35]: It will, let's done within the four to five hours.

**Ankit Choudhary** [12:03:38]: And second thing is the internet speed, which we are using right now for migration.

**Ankit Choudhary** [12:03:43]: if it is good, so I don't think so it will take a long time.

**Ankit Choudhary** [12:03:46]: It will be done very soon.

**Ankit Choudhary** [12:03:48]: So

**Robert Mehler** [12:03:49]: I'm gonna say six to seven, just to be safe.

**Robert Mehler** [12:03:52]: And then the DNS propagation, I wanna talk about that, which is in order for us, our DNS is hosted by Squarespace, which is owned by Google.

**Robert Mehler** [12:04:05]: So we have to move Do we have to move the domain name to it to, we don't, I see David saying no, we can keep it or we can just put a text file into the DNS, the point.

**Robert Mehler** [12:04:18]: So,

**David Orban** [12:04:19]: so there are four technical components to this, four different roles and four different entities.

**David Orban** [12:04:33]: One is the registrar, who is holding and renewing the domain name.

**David Orban** [12:04:42]: In this case, opimpact.com.

**David Orban** [12:04:46]: And you don't need to change that.

**David Orban** [12:04:49]: The second, which most people believe must be the same, but that is actually not the case, is who is managing the DNS, who is managing the records that tell the computers of the world, Where is the website?

**David Orban** [12:05:10]: Where is the anything, whatever else.

**David Orban** [12:05:14]: And then specifically for our case, who is managing email?

**David Orban** [12:05:20]: That is the second thing.

**David Orban** [12:05:23]: The name server.

**David Orban** [12:05:27]: The third thing is what are the particular records in the DNS And specifically for email, there are today not only the MX records, which are basic and have been there for 40, 50 years for SMTP, but these days modern male deliverability also requires additional records so that The recipients of the

**David Orban** [12:06:04]: mail know that you are not trying to pretend to be OP impact.

**David Orban** [12:06:10]: And there's a consequence they send your email to the inbox rather than into the spam folder.

**David Orban** [12:06:15]: Yeah, I'm familiar with that.

**David Orban** [12:06:17]: Okay.

**David Orban** [12:06:18]: And the fourth is the person who has the username and the password and the two-factor authentication.

**David Orban** [12:06:28]: whether over text message or hopefully with an authenticator app, who is able to get into the name server DNS section and update the records with the new information.

**David Orban** [12:06:48]: And yes, this can require the text record as well.

**David Orban** [12:06:53]: which, for example, will tell Microsoft that you have ownership of opimpact.com.

**David Orban** [12:07:03]: And Ankit can tell us if it is indeed needed or not, and is together or separate or precede the MX records being added.

**David Orban** [12:07:12]: But to go back to the beginning, and the first question you asked Robert You don't need to move anything.

**David Orban** [12:07:21]: You don't need to change your registrar.

**Robert Mehler** [12:07:31]: Yeah, let me share with you a screen of the actual DNS.

**Robert Mehler** [12:07:35]: Let me if you see.

**David Orban** [12:07:36]: You just did, you just did, and then you unshared it.

**David Orban** [12:07:39]: Now we can see it.

**David Orban** [12:07:40]: Yes, we can see.

**David Orban** [12:07:41]: Yeah, so this

**Robert Mehler** [12:07:43]: is DNS in Squarespace, all the e-records, C-name, a host file, and then the DMARC down here.

**Robert Mehler** [12:07:53]: During, when we're migrating, So this is the area that we'll be working in.

**Robert Mehler** [12:08:01]: I obviously I'm going to want to make sure that our SPF and a DMARC are also being changed properly here.

**Robert Mehler** [12:08:11]: My thinking is that we're going to have an open session.

**Robert Mehler** [12:08:15]: We're going to do this.

**Robert Mehler** [12:08:17]: You'll send to me an email the exact text so that we don't, or on Teams you send a chat so I can run the inputs in here.

**Robert Mehler** [12:08:25]: This doesn't change.

**Robert Mehler** [12:08:26]: Obviously I can authenticate.

**Robert Mehler** [12:08:28]: As you can see, I'm an admin.

**Robert Mehler** [12:08:29]: I have access to all this.

**Robert Mehler** [12:08:30]: So that's verified in here.

**Robert Mehler** [12:08:36]: Yes.

**David Orban** [12:08:38]: So let me confirm.

**David Orban** [12:08:39]: Let me confirm.

**David Orban** [12:08:40]: This is exactly how it's going to work.

**David Orban** [12:08:43]: And you don't change the A record.

**David Orban** [12:08:45]: You don't change the C name there.

**David Orban** [12:08:53]: I don't think that matters.

**David Orban** [12:08:55]: You will change the MX and you will change the custom records with SPF and the DMARC.

**David Orban** [12:09:04]: Yeah.

**David Orban** [12:09:05]: So let's talk about

**Robert Mehler** [12:09:06]: that a second.

**Robert Mehler** [12:09:06]: That's the moment in time when, first of all, obviously prior to the migration, I've already sent two emails to two people that will be migrating off of Google to Office 365, and that requires downtime.

**Robert Mehler** [12:09:20]: Do not send email.

**Robert Mehler** [12:09:22]: And I presume that emails that are being sent to us are somehow being warehoused somewhere in some cash.

**Robert Mehler** [12:09:27]: We'll get them when we get to the new client or into the new environment.

**Robert Mehler** [12:09:32]: But my hope and desire, and I'll soon tell you the data is that we would start this somewhere in the evening to allow the six, seven hours and hopefully by, let's say eight, nine in the morning next day.

**Robert Mehler** [12:09:44]: Male DNS propagation is taking place and we can begin seeing population.

**Robert Mehler** [12:09:49]: We start seeing, you know, the fluttering of email into the inbox.

**Robert Mehler** [12:09:53]: It takes time specifically for Aden.

**Robert Mehler** [12:09:55]: It will take quite a long time for his local client to repopulate.

**Robert Mehler** [12:10:02]: That's been my experience.

**Robert Mehler** [12:10:04]: I don't know how that works.

**Robert Mehler** [12:10:05]: So I think this is important that we can verify that I have access at the moment of migration.

**Robert Mehler** [12:10:11]: Okay, all that can happen.

**Robert Mehler** [12:10:12]: Obviously you have a credit card ready and available.

**Robert Mehler** [12:10:14]: By the way, I presume I have all the right information.

**Robert Mehler** [12:10:17]: So that's kind of what we're saying, you know, it's just email and calendar and no data.

**David Orban** [12:10:24]: Yeah, so with the risk of being redundant, hopefully not ridiculous to use the card these days.

**David Orban** [12:10:35]: You not only need, if it is not your own, if it is Eden's, for example, you not only need name, card number, and then the three digits.

**David Orban** [12:10:45]: You also need the billing address.

**David Orban** [12:10:49]: And when you hit enter, it may trigger a 2FA, an MFA, where in the bank app, he may need to confirm, even if it is a test chart.

**David Orban** [12:11:03]: So excellent.

**David Orban** [12:11:05]: So he may need to be available.

**Robert Mehler** [12:11:08]: Right, and therefore, part of my question on today's call is, we could go ahead, right, between today, this week, even as a Munich Security Conference and already do some of this, pre-set it up.

**David Orban** [12:11:26]: Yes, so the steps that I see are for Unkit to set up all OP Impact.

**David Orban** [12:11:38]: on Microsoft.com, which is the tenant.

**David Orban** [12:11:43]: And then he will have a username and a password, and he will give it to you.

**David Orban** [12:11:53]: At that point, there is no 2FA set on that yet.

**David Orban** [12:11:58]: That's fine.

**David Orban** [12:12:00]: So you can be, because it is just temporary, there is no security concern.

**David Orban** [12:12:05]: So with the username and the password, you will be able to enter and add the credit card information.

**David Orban** [12:12:14]: And to confirm, yes, this is possible, depending on, on, on, on ankits availability, maybe not today, maybe tomorrow morning.

**David Orban** [12:12:23]: And then you can take whatever time you need to finish the next phase, which is the entering of the billing information.

**David Orban** [12:12:32]: And then Ankit can go ahead and start adding the users.

**David Orban** [12:12:43]: And then everything is ready for the migration to be triggered.

**Robert Mehler** [12:12:52]: Postmigration or during the migration, we're just going to add an array to for an additional email order.

**Robert Mehler** [12:12:59]: So, you know, that's nothing, just we'll just be aware of that.

**Robert Mehler** [12:13:03]: Okay, so.

**Robert Mehler** [12:13:04]: Perfectly fine.

**Robert Mehler** [12:13:05]: Good.

**Robert Mehler** [12:13:05]: So the next 48 hours.

**Robert Mehler** [12:13:08]: We can go ahead and set this up.

**Robert Mehler** [12:13:11]: I'll get the billing address, which I do not have, and I did not think through MFA.

**Robert Mehler** [12:13:16]: So I will do it at an hour that I can make sure that Aden could be available for.

**Robert Mehler** [12:13:22]: Great point.

**Robert Mehler** [12:13:22]: Thank you very much.

**Robert Mehler** [12:13:23]: I really appreciate those fine details.

**Robert Mehler** [12:13:26]: And then really after he has the billing and set up the users, we're in a pause, because we want to wait for the date that we're going to begin the migration, correct?

**Robert Mehler** [12:13:33]: Good.

**Robert Mehler** [12:13:34]: So that's pre-launch.

**Robert Mehler** [12:13:36]: Let's talk about dates, if I may.

**Robert Mehler** [12:13:38]: I originally wrote the 19th.

**Robert Mehler** [12:13:41]: That is no longer the scenario that we're looking at.

**Robert Mehler** [12:13:46]: I would like to see a scenario in which we possibly start Saturday night the 14th and push through like 6 p.m. Saturday night Israel time.

**Robert Mehler** [12:14:03]: and we'll start just basically start running it through there so that we can get to Sunday morning, which obviously means that I need to be awake, blah, blah, blah, all those things, I presume, but that's really our window that we're interested in right now.

**David Orban** [12:14:16]: Okay, so Ankit has been available previous weekends, so Ankit, please confirm if that is possible for you to push the button that needs to be pushed on Saturday 14th.

**David Orban** [12:14:36]: Evening time.

**Ankit Choudhary** [12:14:39]: Sure, I can try.

**Ankit Choudhary** [12:14:40]: You can provide me the like I should have the credential for the login for the admin.

**Ankit Choudhary** [12:14:48]: So yes, I think I can proceed with that.

**Ankit Choudhary** [12:14:52]: Okay.

**Ankit Choudhary** [12:14:52]: Now you

**Robert Mehler** [12:14:53]: need admin to the DNS.

**Robert Mehler** [12:14:56]: or we're going to be doing this for office 365. Okay, good.

**Robert Mehler** [12:15:00]: Okay.

**Robert Mehler** [12:15:00]: So you need to start the migration.

**Robert Mehler** [12:15:02]: So I need the office 365 access so I can start that migration there.

**Robert Mehler** [12:15:06]: Excellent.

**Robert Mehler** [12:15:06]: Yeah, which, which, which hand kit

**David Orban** [12:15:08]: by definition you have because you will be the one starting to set it up.

**David Orban** [12:15:11]: Yeah, right.

**David Orban** [12:15:12]: And then, and then, and then after the migration, just to be extra clear, Robert, you have the option to delete his user.

**David Orban** [12:15:25]: depriving us from access to your Microsoft tenant, or keep it so that we can keep helping you in whatever need you have, right?

**David Orban** [12:15:37]: Yeah,

**Robert Mehler** [12:15:37]: listen, I'm perfectly happy.

**Robert Mehler** [12:15:40]: We'll get to that in a second.

**Robert Mehler** [12:15:42]: I want to follow through on the migration logic path before we get to cyber.

**Robert Mehler** [12:15:49]: All that stuff.

**Robert Mehler** [12:15:50]: Okay.

**Robert Mehler** [12:15:50]: Yeah.

**Robert Mehler** [12:15:52]: Let's go into a place where something didn't work.

**Robert Mehler** [12:15:55]: What is the fallback plan?

**Robert Mehler** [12:15:57]: Email, like our email, we can point back to the MX record on Google and we'll hold and try to figure out what happened, right?

**Robert Mehler** [12:16:03]: Correct.

**David Orban** [12:16:03]: So the interface in the DNS should allow you to download the DNS records as a text file in order to have a backup.

**David Orban** [12:16:14]: And then every decent name service name server platform allows you to do that.

**David Orban** [12:16:22]: Worst come to worst if they were not to allow that.

**David Orban** [12:16:25]: I'm not too familiar with Squarespace.

**David Orban** [12:16:28]: If they were not able to give you a backup with a one click with a single click, you just copy the current DNS records manually a text file and you save it on your computer.

**David Orban** [12:16:43]: And the rollback is very simply, whatever is the reason, unforeseen reason, the rollback is to point the DNS back to Google.

**David Orban** [12:16:57]: Okay, good.

**Robert Mehler** [12:16:58]: I'm doing that literally as we speak.

**Robert Mehler** [12:17:00]: I mean, obviously I'm copying all that because there is no vault, there's no backup that I can find in Squarespace, so that's fine.

**Robert Mehler** [12:17:10]: Okay, that makes sense.

**Robert Mehler** [12:17:13]: Now, relating to the other point, Ankit and ongoing.

**Robert Mehler** [12:17:21]: Look, I don't know what will be at Aliwan, but over on this side, do have an intent to implement Intune up to a point, mobile security.

**Robert Mehler** [12:17:32]: I do want to then do a confirmation on continuity recovery, or basically what's our data retention policy to make sure adheres.

**Robert Mehler** [12:17:43]: And then, you know, I'll try to go in and find out, but I wouldn't mind if I was able to produce quarterly reports on data users, just set up the reporting infrastructure.

**Robert Mehler** [12:17:55]: And I don't know what other security measures in Office 365 related to email, spam.

**Robert Mehler** [12:18:04]: I mean, if we have D-Mark Spiff, that helps a bit, but we have you know, listen, because the issue is that There's gonna be email traffic between us.

**Robert Mehler** [12:18:12]: Why would I wanna send to you potential emails and get you infected and vice versa, right?

**Robert Mehler** [12:18:17]: So the health of our systems, we should try to maintain parity.

**David Orban** [12:18:24]: Right, yes.

**David Orban** [12:18:26]: So we have in tune as well, and we have Microsoft Defender with all its policies, Right now our security score is 45 and Ankit tells me good.

**David Orban** [12:18:42]: Whatever the number is, and we will

**Robert Mehler** [12:18:46]: try to improve Wait, so E3 comes with E3, we're getting the E3 license.

**Robert Mehler** [12:18:52]: So you

**David Orban** [12:18:53]: need E5 for certain things.

**David Orban** [12:18:57]: For example, Miray, yeah, Miray will need E5 because E5 supports purview which if well configured gives you fundamental assistance in labeling information appropriately for a regulated person and regulated activities.

**David Orban** [12:19:26]: Okay,

**Robert Mehler** [12:19:27]: so we'll all do that.

**Robert Mehler** [12:19:28]: No,

**David Orban** [12:19:29]: well, so we are 60 people.

**David Orban** [12:19:32]: And we're not just gonna give money for nothing to Microsoft.

**Robert Mehler** [12:19:36]: Right, but we're paying for the license.

**Robert Mehler** [12:19:39]: I

**David Orban** [12:19:39]: understand.

**David Orban** [12:19:40]: I'm talking about Ali one in Abu Dhabi.

**David Orban** [12:19:43]: Okay.

**David Orban** [12:19:43]: So we are going to keep on E3, the people who are not regulated, and we are only going to move to E5 the people who are regulated.

**Robert Mehler** [12:19:55]: Right.

**Robert Mehler** [12:19:56]: So, well, it'll be myself, Eden.

**Robert Mehler** [12:20:01]: and probably Uri, we're all on the fund, and I'm gonna be doing a lot of compliance work, so it's okay, I mean, and Miray, and Miray.

**Robert Mehler** [12:20:09]: Well, for sure, Miray, and the co-GP, Aden, and then, and then I'm handling information, and so, well, Uri, so, listen, the price difference is not gonna, you know, we're only three people, you're completely

**David Orban** [12:20:21]: a different order of magnitude, so that's a really important note.

**David Orban** [12:20:24]: I just wanted, I just wanted to provide you the full picture, and this, Again, it needs a bit of handholding because if you leave the labeling unleashed, then everything becomes suddenly super secret and untouchable.

**David Orban** [12:20:44]: You cannot print, you cannot forward, you cannot copy and paste, you cannot do a lot of things that we want to do, right?

**Robert Mehler** [12:20:52]: You just saved, you know, it was a great help what you just mentioned.

**Robert Mehler** [12:20:58]: So that was great.

**David Orban** [12:20:59]: Okay, Now, we were talking about the time of the switchover and rollback.

**David Orban** [12:21:11]: That is what we were covering, right?

**David Orban** [12:21:14]: Yeah.

**David Orban** [12:21:17]: So please, Robert, go

**Robert Mehler** [12:21:18]: ahead with your questions.

**Robert Mehler** [12:21:19]: So we confirmed that it will be starting around 6.30 or so Saturday, February the 14th.

**Robert Mehler** [12:21:28]: That will be a weekend.

**Robert Mehler** [12:21:30]: And hopefully by Sunday morning, I will be up and we'll start checking how it's going.

**Robert Mehler** [12:21:36]: And then when they get into the office, I'm going to want to, I do not want to provide tech support for something I don't know.

**Robert Mehler** [12:21:47]: But if we have to set up the email client and make sure they start receiving or downloading or how do they access it first, I guess online, Office 365 online, and then we can set up their email client with whatever the right mapping is to exchange.

**Robert Mehler** [12:22:00]: I think that that would be very useful as to close out the project.

**David Orban** [12:22:06]: Okay, so, um, so, Ankit, um, Is it possible to start with a relatively low security and then harden afterwards so there is not too much back and forth.

**David Orban** [12:22:29]: Let me give you two specific examples.

**David Orban** [12:22:34]: I would like the ability of self provisioning password resets enabled so that if someone misplaces their password and admin is not needed, but they can reset their password.

**David Orban** [12:22:53]: That's one example a security posture that, Robert, you may want to change off the was, but this weekend, think it is okay, and it just avoids confusion about the fact

**Robert Mehler** [12:23:11]: that someone cannot clog in, okay?

**Robert Mehler** [12:23:14]: Fantastic Okay.

**Robert Mehler** [12:23:16]: The second

**David Orban** [12:23:19]: setting that I would wonder if we can just keep in a loose fashion.

**David Orban** [12:23:31]: And Ankit, tell me if it is even possible, because maybe Microsoft doesn't allow it.

**David Orban** [12:23:39]: just for the weekend not to have 2FA.

**David Orban** [12:23:43]: So for the weekend to have username and password that you That's it.

**David Orban** [12:23:48]: Is it possible or 2FA is something that must be there right from the start?

**Ankit Choudhary** [12:23:58]: All right, so let me start giving the answer for your first question.

**Ankit Choudhary** [12:24:03]: First you ask about the password like admin should not every time It's like suppose if any user lost the password, so user can reset the password by their own, right?

**Ankit Choudhary** [12:24:14]: So absolutely that is possible.

**Ankit Choudhary** [12:24:16]: Okay, we can make the changes accordingly.

**Ankit Choudhary** [12:24:18]: So user can reset the password by their Because whenever user trying to reset the password, it will ask for the questions like for the phone number or the email address, which user added over there as a security.

**Ankit Choudhary** [12:24:30]: whenever user will reset the password, it will again ask for the email address and the phone number which user provided at the time of MFA.

**Ankit Choudhary** [12:24:38]: So user can reset the password after that.

**Ankit Choudhary** [12:24:40]: This is absolutely fine, and this is possible.

**Ankit Choudhary** [12:24:43]: that's the first answer of your question.

**Ankit Choudhary** [12:24:45]: Second That was about the multi-factor authentication.

**David Orban** [12:24:53]: Yes.

**David Orban** [12:24:54]: The reason I asked if it is possible not to have is because whether using Microsoft authenticator or outlook itself, producing the security code.

**David Orban** [12:25:15]: There's always a little bit of confusion on the side of users is kind of a chicken and right?

**David Orban** [12:25:21]: And I want to avoid that confusion.

**David Orban** [12:25:26]: to make sure that they know they can get in their email on the browser as simply as possible, and then in a second time next week, rather than during the weekend, set the multi-factor authentication with whatever Robert wants whether it is Outlook or authenticator, even Robert, the possibility,

**David Orban** [12:25:55]: since you are probably already using to keep using Google Authenticator, which is perfectly fine, and there is nothing wrong with it, It's code generator.

**David Orban** [12:26:06]: That's okay.

**David Orban** [12:26:06]: Yeah, yeah, whoever is using whatever, they should be able to keep using it, So, Ankit, that is the reason I asked whether it is possible to start without two- factor authentication.

**Ankit Choudhary** [12:26:20]: All right, So the answer is earlier, Microsoft enable the MFA for every user in the organization, but now when we buy the portal, when we get the portal, the data security default option, which is by default on.

**Ankit Choudhary** [12:26:35]: But yes, we can disable it.

**Ankit Choudhary** [12:26:38]: option is enabled, then MFA is enabled by default for everyone.

**Ankit Choudhary** [12:26:41]: But what we can do when we buy portal, we can disable that option.

**Ankit Choudhary** [12:26:46]: So MFA will disable automatically for every user and then the robot can configure the MFA later if you want.

**Ankit Choudhary** [12:26:53]: You can enable that feature, then

**David Orban** [12:26:54]: MFA will enable for everyone.

**David Orban** [12:26:56]: Okay, so now we know it's possible and Robert, you have to be the one who confirms whether this is how you want to proceed.

**David Orban** [12:27:05]: Again, not recommended in the medium or long term for sure, just for this weekend.

**Robert Mehler** [12:27:12]: Yep.

**Robert Mehler** [12:27:13]: Makes sense.

**Robert Mehler** [12:27:15]: Okay, perfect.

**Robert Mehler** [12:27:17]: Path to resistance and less tech support issues.

**Robert Mehler** [12:27:21]: That's

**David Orban** [12:27:22]: Okay, so to recap, Sorry, not recap.

**David Orban** [12:27:26]: Next question to you on kit.

**David Orban** [12:27:29]: As you define the users mailboxes, you can start with password.

**David Orban** [12:27:41]: And then what I would not recommend To allow them to keep that password.

**David Orban** [12:27:51]: We want to make sure.

**David Orban** [12:27:54]: that during the switchover, whenever they log they actually have to change the password.

**Robert Mehler** [12:28:02]: Correct.

**Robert Mehler** [12:28:02]: And we should have a complex password.

**Robert Mehler** [12:28:06]: Well, you're right.

**Robert Mehler** [12:28:07]: You're right.

**Robert Mehler** [12:28:08]: Because if you don't start out this way,

**David Orban** [12:28:11]: totally, I really appreciate this.

**David Orban** [12:28:14]: And you know, you know, we don't want to have the ability to get into the mailbox, At no And I think that this way we can prove that we don't have that ability, Yeah.

**Ankit Choudhary** [12:28:32]: Okay.

**Ankit Choudhary** [12:28:34]: Yes.

**Ankit Choudhary** [12:28:36]: Robert, good thing, you can manage the things from your side, because if suppose if you are the admin, so you can decide which kind of password user can create, you can modify the things as per your requirement.

**Ankit Choudhary** [12:28:48]: If you want more complicated, suppose you want that user should create the password at least 14 characters.

**Ankit Choudhary** [12:28:53]: included at the rate sign, these special characters, numbers, alphabet, small alphabet, so you can modify the things as per your requirement.

**Ankit Choudhary** [12:29:02]: as per your policy, user can create the password, you have to inform to the user that you have to create at least 14 character password and you have to use these kind of things over there, this kind of social, then if you walk.

**Ankit Choudhary** [12:29:15]: Let me add one thing,

**David Orban** [12:29:16]: Robert, we are in the process of testing and then we'll be adopting and rolling out to everyone, password manager that I love.

**David Orban** [12:29:31]: So there is certainly a bias, and I have been using it for years with all of my companies, and it is called one password.

**David Orban** [12:29:42]: Yeah, sure.

**David Orban** [12:29:43]: And there are at least two reasons.

**David Orban** [12:29:47]: One, I have seen extremely unsecure password behaviors with my eyes in the team and i must prevent the second is that one password business it's a business license nine dollars a month per person a bit less if you buy yearly introduces very useful features in addition like break glass procedures so

**David Orban** [12:30:27]: that if someone is on holiday Mars and they are unreachable and they have you can to their passwords and it is enterprise ready, it is compliant, so everything is recorded and auditable with multiple admins and and division of roles and so So when we talk about passwords that must be complex, And we

**David Orban** [12:31:02]: tell our users, by the way, you cannot write them down.

**David Orban** [12:31:06]: We put them in an impossible situation.

**David Orban** [12:31:10]: That is why the password manager is important.

**David Orban** [12:31:14]: And I'm just sharing with you, which is the one that we picked.

**David Orban** [12:31:20]: OK. So.

**David Orban** [12:31:31]: Let's make something explicit.

**David Orban** [12:31:34]: Ankit will create right away only normal users, but he will also create at least one admin user, which is you, Robert.

**David Orban** [12:31:44]: And so as soon as you want, you can start looking at the Microsoft 365 admin interface.

**David Orban** [12:32:01]: And you could even, if you wanted, start using the temporary

**David Orban** [12:32:12]: domain access credentials to test, for example, the browser access or things like that, because they are available before the MX propagates with the opimpact.onmicrosoft.com and then your user, it's already It will have a different name after the DNS propagation, but it will be the same.

**David Orban** [12:32:46]: You just have to change the login, right?

**David Orban** [12:32:52]: whenever we start creating, Ankit starts creating the users and you receive your credentials, you can log and you can start looking

**Robert Mehler** [12:33:02]: Okay.

**Robert Mehler** [12:33:04]: Yeah, I'm not going to be able to get to it right now, but Yeah,

**David Orban** [12:33:10]: whenever it is, whenever you want.

**David Orban** [12:33:12]: I'm just saying that it is So, so Saturday a given time, and we will put it in writing, we will start the MX, we will start the DNS migration.

**David Orban** [12:33:33]: When you wake the best case scenario is that everything is flowing.

**David Orban** [12:33:38]: In the worst case scenario, we will revert the DNS.

**David Orban** [12:33:49]: I don't need to speculate about what could be there in between.

**David Orban** [12:33:53]: don't know.

**David Orban** [12:33:55]: We will I'm

**Robert Mehler** [12:33:57]: pretty confident.

**Robert Mehler** [12:33:58]: This is not a complicated migration.

**Robert Mehler** [12:34:01]: Yeah.

**Robert Mehler** [12:34:02]: But the level of detail here is obviously very, very useful and very important.

**Robert Mehler** [12:34:08]: So I appreciate that.

**Robert Mehler** [12:34:09]: Thank you.

**Robert Mehler** [12:34:11]: And what comes after?

**Robert Mehler** [12:34:12]: Maybe

**David Orban** [12:34:13]: we will prepare a list.

**David Orban** [12:34:15]: So things like the settings that you want to revert, like the multifactor authentication and other things, And we will be

**Robert Mehler** [12:34:27]: happy to... I think that would be useful if there was a list of things, and then I can research.

**Robert Mehler** [12:34:31]: That would be profoundly useful.

**Robert Mehler** [12:34:36]: So think what I will do is on my side actions.

**Robert Mehler** [12:34:41]: I have to get the rest of the credit card details.

**Robert Mehler** [12:34:43]: I think we should already send a calendar invite for 6.30 on the 14th teams.

**Robert Mehler** [12:34:49]: And by then will, I will confirm when I have the credit, the rest of the credit card details so we can pre-pre-pre-pre-pre-pre-pre-prepair the environment, everything up till the point of DNS migration.

**Robert Mehler** [12:35:05]: We can just get it into place.

**Robert Mehler** [12:35:07]: Okay.

**Robert Mehler** [12:35:10]: How should we communicate?

**Robert Mehler** [12:35:12]: Email to me is a little bit stiff and slow.

**Robert Mehler** [12:35:16]: How do you prefer to operate this Slack or Teams messaging?

**Robert Mehler** [12:35:21]: What should we do in a

**David Orban** [12:35:22]: group?

**David Orban** [12:35:22]: We can create a temporary Slack channel that is private.

**David Orban** [12:35:29]: And we will sunset it after the migration.

**David Orban** [12:35:32]: And in the meantime, we do everything there.

**David Orban** [12:35:35]: I will set it up and invite the two Excellent.

**David Orban** [12:35:43]: I think we're All So thank you, Ankit, also for your availability over the weekend.

**David Orban** [12:35:52]: Thank you, Robert, and we will proceed with all the details that we Thank you, gentlemen.

**Robert Mehler** [12:36:01]: Appreciate all this.

**Robert Mehler** [12:36:02]: This has really been very helpful to me.

**Robert Mehler** [12:36:03]: Thank Okay,

**Ankit Choudhary** [12:36:06]: Ciao.

---
*Backed up from MeetGeek on 2026-03-30 08:44*
