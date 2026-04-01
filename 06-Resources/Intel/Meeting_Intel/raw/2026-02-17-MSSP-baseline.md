# MSSP baseline

**Date:** 2026-02-17
**Duration:** Unknown
**Meeting ID:** 593ae5d1-5314-44d1-991b-a8873fe6dd2e

## Participants
- *Participants not listed*

### Summary

The meeting combined a personal health update with focused operational planning for IT security and infrastructure. Participants confirmed remote-work arrangements and HR follow-up, reviewed the current Microsoft tenant and domain status, and enumerated existing security tools (Defender, BitLocker, Intune). They agreed to favor Microsoft E5 capabilities and to be cautious about costly third-party solutions, discussed pending migrations and data residency for upimpact.fund and Treasury, and prioritized consolidating documents (H1 priorities, IT architecture landscape) and vendor conversations. Key action items include finalizing H1 priorities, checking data residency settings, registering a capital domain, and ensuring stakeholders can review versioned documents.

## Full Transcript

**Cigdem Kemi** [10:01:04]: What about now?

**David Orban** [10:01:06]: Now I can hear you.

**Cigdem Kemi** [10:01:07]: Yes.

**Cigdem Kemi** [10:01:10]: Good.

**Cigdem Kemi** [10:01:12]: Maybe

**David Orban** [10:01:12]: your headset is not working.

**David Orban** [10:01:13]: Yeah, whatever.

**David Orban** [10:01:19]: Okay, so two objectives in the meeting now.

**David Orban** [10:01:25]: One is the MSSP baseline.

**David Orban** [10:01:30]: And the second may be Any alignment we need or clarification on the documents that you are actively working on so that we.

**David Orban** [10:01:44]: Well, we align and prioritize as it should be.

**David Orban** [10:01:49]: OK, but before we start with either.

**David Orban** [10:01:54]: You said that you were going to do some checkups.

**David Orban** [10:01:59]: How is everything going?

**David Orban** [10:02:01]: Yeah, it's

**Cigdem Kemi** [10:02:03]: going well.

**Cigdem Kemi** [10:02:03]: Today I was also like almost three hours in the hospital from 8 until 11.30. So, yeah, I have to take now like 10 days medication, like every six hour.

**Cigdem Kemi** [10:02:16]: Like I have to vote with this package of medicine with me 10 days and then I have to go again.

**Cigdem Kemi** [10:02:22]: to give some tests they want to you know measure some results before they make an overall diagnosis and yeah I think it's progressing but it's very stressful and yeah but it's it's good I'm still optimistic that I will handle it and and and

**David Orban** [10:02:43]: the the the medical system is very opaque right the I don't know in your case and and with the doctors that you are seeing but they don't have the time for you to ask all the questions that you would want or to explain it over and over again.

**David Orban** [10:03:01]: Yes.

**David Orban** [10:03:04]: And that is a pity.

**David Orban** [10:03:05]: And of course you should think about it independently, but if I were in your situation, I would absolutely feed everything to chat GPT or Claude.

**David Orban** [10:03:22]: Okay.

**David Orban** [10:03:23]: Not because I would trust them with any decision or diagnosis, but exactly because they have the patience to explain, to clarify.

**David Orban** [10:03:39]: to answer every question with all the time, right?

**David Orban** [10:03:45]: So they complement each other perfectly.

**David Orban** [10:03:49]: The human doctor under time pressure, but with all their expertise makes the decisions.

**David Orban** [10:03:59]: You, on the other hand, talk to the AI about your condition because you need deeper, A broader understanding.

**David Orban** [10:04:11]: And so the two go hand in hand.

**David Orban** [10:04:16]: Yes,

**Cigdem Kemi** [10:04:17]: actually, yeah, I should try this.

**Cigdem Kemi** [10:04:19]: I'm still waiting for my medical records.

**Cigdem Kemi** [10:04:21]: I have to get it from the doctor because I want to be like transferred to Cleveland now.

**Cigdem Kemi** [10:04:28]: have a second opinion from them and not rush into any surgery.

**Cigdem Kemi** [10:04:32]: So because it's life- changing in the end.

**Cigdem Kemi** [10:04:35]: And I'm also now ordered to get very high dose of specific vitamins.

**Cigdem Kemi** [10:04:42]: And yeah, I will see.

**Cigdem Kemi** [10:04:46]: Litamins

**David Orban** [10:04:47]: are always good somehow I know I know nothing close to close to nothing very little but vitamins of course take as much as you want because the body is able to eliminate the excess so That is something that you should not at all be worried about take as much or more.

**David Orban** [10:05:11]: I am not aware of vitamin sorting ever anyone, right?

**David Orban** [10:05:19]: So.

**David Orban** [10:05:21]: So, yeah.

**David Orban** [10:05:24]: As it as it is eliminated, maybe you notice some color change and you go like, wow.

**David Orban** [10:05:30]: So yellow, or I don't know, whatever it is.

**David Orban** [10:05:34]: I hope I can reverse aging

**Cigdem Kemi** [10:05:35]: after all the vitamin shots, because I get it as injection to my veins directly, a very high dose in serum packages.

**Cigdem Kemi** [10:05:45]: And this actually what the Cleveland doctor ordered.

**Cigdem Kemi** [10:05:48]: He said I should start with that until the other results from the medication come.

**Cigdem Kemi** [10:05:54]: Because he said many things can be already be avoided or solved in the face of really getting a lot of vitamins, especially vitamin C and vitamin E for the liver.

**Cigdem Kemi** [10:06:07]: Yeah, some other things.

**Cigdem Kemi** [10:06:09]: So I'm very curious, but it's very exhausting to take a lot of those things and then you feel a bit busy for an hour and yeah.

**David Orban** [10:06:16]: Yeah, and that is certainly true both having to go to the hospital and then waiting and then the procedures and then concentrating to be precise with taking all the medications and everything.

**David Orban** [10:06:36]: That is indeed a lot of stress.

**David Orban** [10:06:40]: And yeah, there is very little, apart from breathing deeply, and try to try to find ways everyone with their own approach to keep stress at bay or to release stress.

**David Orban** [10:07:01]: Some people would go to the gym and fight or punch or run.

**David Orban** [10:07:08]: Other people would meditate.

**David Orban** [10:07:11]: Each person may have their own way to cope with stress, but the reality is that it is certainly complicated and stressful.

**David Orban** [10:07:22]: All right.

**David Orban** [10:07:25]: And you are you are at home, so that's good.

**David Orban** [10:07:29]: Yes, thank you.

**David Orban** [10:07:32]: Amina asked me, I think last week, last Friday, and I told her, yes, Chidem and I are aligned that when she needs, she works from home, I measure her outcomes.

**David Orban** [10:07:48]: and not the number of hours that she's sitting on a chair in the office.

**David Orban** [10:07:53]: So that is, I think, a good way to make sure that we measure what matters.

**David Orban** [10:08:03]: Because if I force you to be in the office and I would, you know, take the hours that you spent sitting at your chair, but nothing would come out of it.

**David Orban** [10:08:16]: I don't think that would be the good approach.

**David Orban** [10:08:18]: So I will confirm with Amina that we have this arrangement and and that's it.

**David Orban** [10:08:27]: So

**Cigdem Kemi** [10:08:28]: let's... I have also sent this letter from the hospital today that I was three hours in the hospital so they can also deduct from sick days if they want.

**Cigdem Kemi** [10:08:38]: Nisha has it, so it should be fine, I think.

**Cigdem Kemi** [10:08:43]: Perfect, perfect.

**Cigdem Kemi** [10:08:46]: Now we can share this.

**Cigdem Kemi** [10:08:49]: I don't know what MSSP stand for, but I think we can start discussing about good things.

**David Orban** [10:08:58]: stands for Manage Security Service Provider.

**David Orban** [10:09:02]: Oh, okay.

**David Orban** [10:09:03]: Yes.

**David Orban** [10:09:04]: And so the What what you are showing and sharing right now is a document that that you created.

**David Orban** [10:09:18]: Yes,

**Cigdem Kemi** [10:09:20]: the regarding your request, this is your request, and I just put the architectural landscape here, I can open it also open in bilateral and then I mentioned that before we can speak to the vendors for the managed security services.

**Cigdem Kemi** [10:09:37]: We should have certain things in place, and that's why I wanted to just go through this document, whatever is feasible.

**Cigdem Kemi** [10:09:46]: And it's just my thought, maybe you can, of course, decide if you want to do this before or after you speak to the vendors.

**Cigdem Kemi** [10:09:57]: We have to actually, I don't know if you have a list, but we should create a list of things that have been done already.

**Cigdem Kemi** [10:10:04]: It's not so much, but it's still a lot of minor work because we had the entry ID, we had the email migration, the domain migration, the creation of different email addresses for each legal entity.

**Cigdem Kemi** [10:10:18]: Some other things we have this like Microsoft Defender, security setup.

**Cigdem Kemi** [10:10:24]: We had the upgrade of the devices from home to pro edition.

**Cigdem Kemi** [10:10:28]: It was a bit messy.

**Cigdem Kemi** [10:10:30]: We did a lot of work, but nothing to strengthen our infrastructure so far.

**Cigdem Kemi** [10:10:36]: The infrastructure is still just the Azure cloud, and we have the E365 licenses for Ali1 Group, like for Ali1.com, Ali1 email, and Alcasma and TEG still.

**Cigdem Kemi** [10:10:50]: We have selected people who have the TEG email address.

**Cigdem Kemi** [10:10:53]: And then we have outside of the Microsoft licenses, we have just some defender configurations.

**Cigdem Kemi** [10:11:01]: We have the BitLocker and we have every user now linked to the Entra ID via Intune, which offers also single sign on.

**Cigdem Kemi** [10:11:11]: And we don't need to all the time sign in during the day.

**Cigdem Kemi** [10:11:17]: then like we have only those things and then it would be good to have some infrastructure license also and then when when you know the like the service provider he asked for what how is your infrastructure or what have you built so far or what what do you plan to protect we can say okay we plan to

**Cigdem Kemi** [10:11:40]: integrate some core services like the ERP or the capital system and then we have the infrastructure as platform as a service or infrastructure as a service or whatsoever and i have it's just a bit more because i try to always add some explanation so that you can understand you know and follow me but

**Cigdem Kemi** [10:12:04]: if it's not necessary you can just stick on the keywords and microsoft e5 licensing it will help you know to have increased security standards that's why i would prefer that we can say at least we are in discussions and we are planning to integrate PIS service and Microsoft E5 licensing as a

**Cigdem Kemi** [10:12:27]: standard and then to have maybe some jurisdictional data mappings and pure view tools to also help the cybersecurity provider to do their work in the infrastructure if it's needed to.

**Cigdem Kemi** [10:12:43]: Yes.

**David Orban** [10:12:44]: And of course, then everything will have to also conform to the base policies that in terms of data protection, in terms of compliance, we are going to adopt.

**David Orban** [10:13:03]: And in that sense, I asked to be able to speak to trifecta, which is looking like outsourced compliance service that that we are going to use, but I haven't been able to do that yet.

**David Orban** [10:13:25]: Now, let's take a step back.

**David Orban** [10:13:28]: As I understand, we one Microsoft tenant.

**David Orban** [10:13:36]: Is that correct or we have multiple tenants?

**David Orban** [10:13:39]: We have actually

**Cigdem Kemi** [10:13:40]: one because the old tenant we don't have access to and there is nothing we have moved.

**Cigdem Kemi** [10:13:46]: I have moved together already in the beginning with the help of Mahendra the old TG tenant into the new tenant because it was we had to really cut the domain it was not able to really have There in the old tenant.

**Cigdem Kemi** [10:14:05]: We don't have like admin rights.

**Cigdem Kemi** [10:14:07]: It was linked to another hosting server.

**Cigdem Kemi** [10:14:09]: So we transferred everything.

**Cigdem Kemi** [10:14:12]: But the hosting of the domain for TEG is still somewhere else.

**Cigdem Kemi** [10:14:17]: Michael can say more about it.

**Cigdem Kemi** [10:14:19]: But doesn't matter.

**Cigdem Kemi** [10:14:20]: It doesn't bother us anymore.

**Cigdem Kemi** [10:14:22]: We still have to control over the TEG because we have moved the domain.

**Cigdem Kemi** [10:14:26]: It's still under Microsoft.

**Cigdem Kemi** [10:14:28]: So Microsoft has moved it for us to our new tenant.

**Cigdem Kemi** [10:14:32]: And we can manage and create email addresses or disable or whatever.

**Cigdem Kemi** [10:14:40]: But we don't have access to the domain itself.

**Cigdem Kemi** [10:14:42]: It's hosted somewhere else.

**Cigdem Kemi** [10:14:43]: Anything else is in GoDaddy.

**Cigdem Kemi** [10:14:46]: And in GoDaddy, we can manage our domains.

**Cigdem Kemi** [10:14:50]: And in the entry ID, it's Ali van group.

**Cigdem Kemi** [10:14:52]: I think it's called Ali van group.

**Cigdem Kemi** [10:14:54]: This is our only entry ID, although there is also the email address for Al-Kazna and TEG is also there.

**Cigdem Kemi** [10:15:01]: But it's just the name of the domain there, it was no point of opening a new tenant and maybe paying extra fees for just one Al-Kasna email address so we can, at this stage, we can put everything together in one domain, it has no, no consequences, because it's just the technical infrastructure.

**Cigdem Kemi** [10:15:22]: Later, when we are, you know, a grown and well-established company, we can still decide on opening new entry IDs.

**David Orban** [10:15:28]: But right now.

**David Orban** [10:15:30]: Is there, as far as you know, any email address also for Alivan Capital or not yet?

**Cigdem Kemi** [10:15:39]: Alivan.com.

**Cigdem Kemi** [10:15:40]: Everyone is under Alivan.com.

**Cigdem Kemi** [10:15:42]: For Alivan Capital, we should potentially, you know, secure a new domain, email domain for Alivan Capital, which we didn't consider.

**Cigdem Kemi** [10:15:52]: Everyone is Alivan.com.

**David Orban** [10:15:54]: So I confirm that there are like a dozen domains, and one of them is Aliwan.capital, and whether it's the right one or Aliwancapital.com is better.

**David Orban** [10:16:08]: Those are the decisions that will be taken further.

**Cigdem Kemi** [10:16:14]: think it's better for branding, Aliwancapital.com.

**Cigdem Kemi** [10:16:18]: then

**David Orban** [10:16:19]: yeah also also you know just like we noticed with dot email many clients do not automatically recognize and turn into a hyperlink if your extension is weird so dot capital would be obviously routed by the DNS but it wouldn't be clickable yeah whether whether a website or an email address It would

**David Orban** [10:16:49]: always cause these little hiccups.

**David Orban** [10:16:51]: So I definitely agree there.

**David Orban** [10:16:54]: Now, you mentioned that we have an Al-Kazna email.

**David Orban** [10:16:59]: It's only for one

**Cigdem Kemi** [10:17:00]: person, it's only Michael.

**David Orban** [10:17:02]: okay.

**David Orban** [10:17:03]: Yeah, so far in this stage.

**David Orban** [10:17:05]: Yeah.

**David Orban** [10:17:06]: Okay, all right.

**David Orban** [10:17:09]: Okay, very good.

**David Orban** [10:17:10]: But we have the

**Cigdem Kemi** [10:17:11]: domain also in GoDaddy, and we have linked it with our Entra ID, you know, updated to DNS servers.

**Cigdem Kemi** [10:17:18]: in order to have it in the enter ID and to create email addresses if we need to, but this is, you know, like I'm waiting for any, like, how do you say, someone has to tell me we need, we need email addresses.

**Cigdem Kemi** [10:17:33]: Right now we don't need it, it's like.

**David Orban** [10:17:35]: Of course, of course.

**David Orban** [10:17:39]: So, so.

**Cigdem Kemi** [10:17:42]: The thing is also why we need to secure our infrastructure right now at least set the baseline in order to later integrate the systems, define on data orchestration layer and orchestration process and also on a data management system which we will need later have all the master data in our

**Cigdem Kemi** [10:18:09]: infrastructure right now we don't have anything we cannot plan to implement any master data management system There because we don't have any data, nothing, we are not operating yet.

**Cigdem Kemi** [10:18:22]: But later, maybe next year, it will be in discussion, and then it will be easier if we have for instance the platform as a service where we don't need so many resources and development efforts like the infrastructure as a service where with every system integration we have additional efforts and we

**Cigdem Kemi** [10:18:46]: need to buy in the knowledge also and the resources which will not be very well manageable That's why we need to decide right now on the foundational things.

**Cigdem Kemi** [10:19:08]: How do you plan to set up the data security in your infrastructure and what do you want to protect in fact?

**Cigdem Kemi** [10:19:14]: And then we don't want them to offer us like a Palo Alto solution, which is also for data security, but this is a separate tool.

**Cigdem Kemi** [10:19:23]: I know it's international standard, but it's too much for us.

**Cigdem Kemi** [10:19:25]: We don't need it at this stage.

**Cigdem Kemi** [10:19:27]: We can have the same result with Microsoft tools that are within our licenses, within the E5 license.

**Cigdem Kemi** [10:19:37]: We can have it covered with poor view and maybe some other tools.

**Cigdem Kemi** [10:19:42]: We don't need to pay Palo Alto licenses, which may be in discussion after two, three years, but not right now, for instance.

**Cigdem Kemi** [10:19:50]: And that's why we need to be careful that we don't allow them to do whatever they want, and then they will charge us high fees.

**Cigdem Kemi** [10:19:57]: So we have to see whatever is possible within our business license with Microsoft and it's covered makes sense to start with that.

**Cigdem Kemi** [10:20:05]: And then we can book their services to assess if something else is more needed or it covers already whatever we need.

**Cigdem Kemi** [10:20:15]: Yes,

**David Orban** [10:20:16]: yes.

**David Orban** [10:20:17]: So forgive my confusion.

**David Orban** [10:20:21]: know you shared the folder with me with all the files and this one is inside that folder as well, I assume, right?

**David Orban** [10:20:32]: I

**Cigdem Kemi** [10:20:32]: sent you also even in the evening yesterday an email with the links so you can click on the links and open it as a web browser, but I can also you don't want the web browser I can

**David Orban** [10:20:43]: I want the browser absolutely.

**David Orban** [10:20:45]: Yes, so then we have the email also.

**Cigdem Kemi** [10:20:55]: Yes,

**David Orban** [10:20:56]: I see, okay, H1, three actions and IT architecture, perfect.

**David Orban** [10:21:04]: And okay, and just so that I have the context, can you maybe in the chat also share the folder that contains the document?

**Cigdem Kemi** [10:21:20]: where is my folder?

**Cigdem Kemi** [10:21:23]: Alivan IT.

**Cigdem Kemi** [10:21:25]: Now this is also one thing I asked Ankit to merge Alivan with Alivan IT because now we have two cloud storages and when I work on my Alivan storage on my you know here and then I cannot find it in Alivan IT I have to upload it again, which is our shared teams group folder and I don't know I will ask

**Cigdem Kemi** [10:21:49]: him if he could manage to find out how to merge those.

**Cigdem Kemi** [10:21:52]: Otherwise, this is the, actually, let me check how I can send you.

**Cigdem Kemi** [10:22:00]: This is

**David Orban** [10:22:00]: the folder, Alivan IT.

**David Orban** [10:22:02]: I will go there on Teams myself.

**David Orban** [10:22:05]: Just leave the screen if you don't mind shared.

**David Orban** [10:22:09]: I'm going there on another computer.

**David Orban** [10:22:14]: And what we need

**Cigdem Kemi** [10:22:14]: to consider, which is still open, and in my opinion, a bit urgent, Because we should not start doing any infrastructure configuration without having all the domains covered, op impact.fund is still not covered and protected against cyber attacks or nothing, because they don't have the Microsoft

**Cigdem Kemi** [10:22:35]: license, they are just having, I don't know, whatever is, how is their email?

**Cigdem Kemi** [10:22:41]: Sorry, sorry, he's not protected.

**Cigdem Kemi** [10:22:43]: Upimpact.Fund, the people we

**David Orban** [10:22:45]: still could not move them.

**David Orban** [10:22:49]: So let me update you on that.

**David Orban** [10:22:50]: They decided to migrate to their own Microsoft tenant rather than be part of ours.

**David Orban** [10:23:00]: And we are assisting them with that migration away from Google Workspace to Microsoft 365. And the migration was scheduled to happen this past weekend.

**David Orban** [10:23:12]: But they stopped because they didn't know if the data residency should be Israel or the US.

**David Orban** [10:23:24]: I think it's

**Cigdem Kemi** [10:23:25]: US, Miré said it already in two weeks ago, three weeks ago.

**Cigdem Kemi** [10:23:29]: And,

**David Orban** [10:23:31]: and you know, whether we.

**David Orban** [10:23:37]: have that information and believe it is the right information.

**David Orban** [10:23:41]: We executing this case, and we will only execute after we receive confirmation from, this case, Robert, right?

**David Orban** [10:23:53]: So I agree legal entity a US entity.

**David Orban** [10:23:59]: and it should be in the US, but we have to wait until Robert confirms.

**Cigdem Kemi** [10:24:10]: Okay.

**Cigdem Kemi** [10:24:10]: Another point regarding data residency is what we can do immediately without any additional effort is to really check and request the data residency for our Treasury account, Alivan, to UAE instead of Europe or wherever it is right now.

**Cigdem Kemi** [10:24:28]: And then

**David Orban** [10:24:29]: it doesn't have a UAE location.

**Cigdem Kemi** [10:24:34]: They have the cloud server, Azure cloud server, and Rita, she asked me to check if a UAE is available.

**Cigdem Kemi** [10:24:42]: I don't know if you did check or not.

**Cigdem Kemi** [10:24:44]: I didn't have the time to check it.

**Cigdem Kemi** [10:24:46]: I'm also not sure if I'm still admin or not.

**Cigdem Kemi** [10:24:50]: We can check in the data residency options and select because they are cloud.

**Cigdem Kemi** [10:24:58]: based and the Azure cloud which is perfect we are also in the Azure cloud and Azure cloud is in the UAE available so it

**David Orban** [10:25:05]: should be possible okay so so these are all good points and no you shouldn't worry about them but whenever something like this comes into your mind just assign me the task okay okay so do you have an idea great Do you

**Cigdem Kemi** [10:25:26]: should it's in my document.

**Cigdem Kemi** [10:25:29]: It's here in the document mentioned, but I can assign you a task also.

**Cigdem Kemi** [10:25:34]: I wanted to, you know, to read the document and then you can give me feedback.

**Cigdem Kemi** [10:25:38]: You can also open the Azana task if you want.

**David Orban** [10:25:41]: now,

**David Orban** [10:25:46]: sorry, okay, so if I go to general and shared.

**David Orban** [10:25:53]: This is it.

**David Orban** [10:25:54]: Alivan IT.

**Cigdem Kemi** [10:25:55]: Yeah, I'm there.

**Cigdem Kemi** [10:25:57]: I'm looking

**David Orban** [10:25:58]: at exactly the same screen as you And then this H1 document, where is It's in a

**Cigdem Kemi** [10:26:07]: subfolder.

**Cigdem Kemi** [10:26:08]: Strategy maybe.

**Cigdem Kemi** [10:26:10]: H1, three action items here.

**Cigdem Kemi** [10:26:12]: Yeah, and the strategy.

**Cigdem Kemi** [10:26:14]: Okay, perfect.

**David Orban** [10:26:19]: So that's great.

**David Orban** [10:26:26]: A

**David Orban** [10:26:31]: feel free to confirm out of the three things that I proposed and then other things that you already had under development.

**David Orban** [10:26:45]: What are the ones that you want to work on?

**David Orban** [10:26:55]: is to be able to save a PDF that is version 1.0 of those documents.

**David Orban** [10:27:09]: With regards to that, we don't need to discuss it now.

**David Orban** [10:27:13]: Just, you know, when you wrote last week Q1 Priorities, I responded, rather than Q1, which is end of March.

**David Orban** [10:27:25]: Let's look at end of February.

**David Orban** [10:27:29]: Okay, break it down.

**David Orban** [10:27:30]: And so that is what I want you to have as a perspective.

**David Orban** [10:27:36]: What can you accomplish over the next two weeks in terms of documents?

**David Orban** [10:27:41]: Okay.

**Cigdem Kemi** [10:27:42]: Yeah.

**Cigdem Kemi** [10:27:43]: I can clarify.

**Cigdem Kemi** [10:27:44]: I would prefer to finalize the action items that I have defined in this document, H1 priorities, and maybe add something else and then really to, yeah, get Position and start, you know, to discuss also with the Microsoft vendor about the platform as a service about, you know, having an approach,

**Cigdem Kemi** [10:28:05]: aligning on an approach and working on that.

**Cigdem Kemi** [10:28:08]: This will also already require some time efforts, you know, to, to make a detailed description of how we want to approach What are the next steps?

**Cigdem Kemi** [10:28:18]: Should we talk to the Microsoft window first, like to logic era or to the cyber security people or you know.

**David Orban** [10:28:27]: Sure, so the.

**David Orban** [10:28:38]: We will have to consolidate the documents including the priorities and then deliver them and give visibility to Amina and anyone else who wants to have visibility in a manner that they understand and that if they need to provide feedback, they can provide feedback, right?

**David Orban** [10:29:06]: And whether it good or not, the creation of the binder was aiming to accomplish exactly this.

**David Orban** [10:29:21]: So okay, work on the H1 priorities as well.

**David Orban** [10:29:28]: Another

**Cigdem Kemi** [10:29:29]: thing is also, I'm sorry for interrupting you, the IT architecture landscape, but for this, I'm already running a deep analysis on the processes process flows in order to set them right, but I cannot finalize them in two weeks.

**Cigdem Kemi** [10:29:45]: I worry, especially when I'm alone and I don't have full insights in every division.

**Cigdem Kemi** [10:29:50]: I'm not like an overall general expert and that's why I need to align and I need to wait also for you to schedule some more workshops.

**Cigdem Kemi** [10:29:59]: I can work on that, but I will not finalize it until end of February.

**Cigdem Kemi** [10:30:04]: Maybe a high level view, broad view, but not all detailed processes.

**Cigdem Kemi** [10:30:08]: What I found out already is that advisory and investment banking.

**Cigdem Kemi** [10:30:15]: Since we don't have any systems, they are creating workflows to onboard clients right now because they are, you know, having origination business advisory business via Slack and linked to Azana.

**Cigdem Kemi** [10:30:31]: Okay, it's a solution, but it's not compliant at all because we are feeding Slack and Azana with overall client information, phone number, deal size, name, everything.

**Cigdem Kemi** [10:30:43]: And it stays there.

**Cigdem Kemi** [10:30:45]: And it violates data residency roles, the rules, and also the Chinese walls, everyone can see And it's a Nazana group.

**Cigdem Kemi** [10:30:55]: And it's not protected at all, but I aligned now with Isel, she should not keep the confidential data longer than a couple of weeks and really focus on deleting them is whenever she has moved them to pipe drive, but she said this is her only workflow, she doesn't have any other workflow, and

**Cigdem Kemi** [10:31:14]: otherwise she doesn't know how to proceed, and also like the people in advisory investment banking, this highlights the need to have a system, an ARP system, CRM system, actually, because pipe drive doesn't offer those kind of workflows also.

**Cigdem Kemi** [10:31:30]: is very limited.

**Cigdem Kemi** [10:31:32]: Yeah, the time being, we continue like that, but we are not like...

**David Orban** [10:31:37]: Yes, so I hear and have to go to my next meeting.

**David Orban** [10:31:43]: Yeah.

**David Orban** [10:31:45]: Please work on those documents, and anytime you find a dependency, rather than feeling blocked by just insert a placeholder.

**David Orban** [10:32:02]: If it existed, this is how it would look This is a plausible way for investment banking or asset management to proceed.

**David Orban** [10:32:13]: Waiting for their confirmation, waiting for their input, this is the assumption.

**David Orban** [10:32:21]: That is how I want you to be able to go ahead without feeling paralyzed because you are not receiving the feedback or the input that you need.

**David Orban** [10:32:34]: Okay?

**David Orban** [10:32:36]: Yes.

**Cigdem Kemi** [10:32:37]: And just on, I can also write in the document, you know, based on my research, Microsoft Dynamics is much better for the capital and for the advisory investment banking business than Odo, actually.

**Cigdem Kemi** [10:32:52]: Yes,

**David Orban** [10:32:54]: we will discuss Okay.

**David Orban** [10:32:56]: And we will consolidate our recommendation and how to proceed for the moment.

**David Orban** [10:33:05]: Very simply, there is no money for either.

**David Orban** [10:33:07]: Yeah, very simple.

**David Orban** [10:33:09]: So, okay.

**David Orban** [10:33:10]: Not a Okay.

**David Orban** [10:33:13]: Thank

**Cigdem Kemi** [10:33:14]: you.

**Cigdem Kemi** [10:33:14]: Bye-bye.

---
*Backed up from MeetGeek on 2026-03-30 08:44*
