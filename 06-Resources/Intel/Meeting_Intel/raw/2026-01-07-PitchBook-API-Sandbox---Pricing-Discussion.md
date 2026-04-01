# PitchBook API Sandbox & Pricing Discussion

**Date:** 2026-01-07
**Duration:** Unknown
**Meeting ID:** be7f64da-3982-4877-bf1a-9f79a93ece80

## Participants
- *Participants not listed*

### Summary

The call focused on clarifying API pricing, use cases, and evaluation options: the customer voiced frustration at opaque public pricing and resisted high prepaid thresholds, preferring low-cost experiments. Sam proposed providing documentation and sandbox access with limited datasets for free testing, explained API call types and prepaid-per-record pricing and confirmed prepaid calls refresh during the contract. The customer described his role (head of innovation) and intent to integrate PitchBook into AI workflows, noted underused licenses, and agreed to receive documentation and run sandbox experiments to determine fit and next steps.

## Full Transcript

**Unknown speaker** [08:02:28]: Yeah, this won't

**Sam Radwan** [08:02:29]: take long, it's just to really know what would you want in terms of pricing and solution so I can send some stuff across.

**Sam Radwan** [08:02:36]: So I know you're using the platform, so you have this online usage.

**Sam Radwan** [08:02:39]: Okay, so program is sort of placed on the screen.

**Sam Radwan** [08:02:43]: Can

**David Orban** [08:02:43]: you hear me okay?

**David Orban** [08:02:44]: Yeah, I can.

**David Orban** [08:02:46]: Now, we have a certain subscription, right?

**David Orban** [08:02:51]: Correct, yes.

**David Orban** [08:02:54]: Maybe you do or you do not have access to the to your logs, but I don't think we are using the platform that much, if at all.

**David Orban** [08:03:08]: And basically what you are telling me is you aren't using the platform already, but why don't we enter into yearly agreement, we pre-paid or pre-agreed pricing, you give us more money.

**David Orban** [08:03:20]: you are basically incentivizing us to use the platform even less.

**David Orban** [08:03:25]: So I'm a bit confused.

**David Orban** [08:03:28]: And you are asking me, what do you want to use the API for?

**David Orban** [08:03:33]: Well, whatever.

**David Orban** [08:03:34]: The API is for integrating something into something else.

**David Orban** [08:03:40]: So what I want is to integrate pitchbook into our systems.

**David Orban** [08:03:44]: And I have no idea.

**David Orban** [08:03:46]: what they are going to be because I didn't scope it out and one reason I didn't scope it out is because I didn't want to think about something that I didn't know even how much it would cost.

**David Orban** [08:03:58]: Okay.

**David Orban** [08:03:59]: And really I would hope it would cost very little.

**David Orban** [08:04:02]: It's not that I am planning to siphon off your database.

**David Orban** [08:04:10]: I just want to use it within normal bounds.

**David Orban** [08:04:14]: And I have no idea what the various use cases are going to be.

**David Orban** [08:04:21]: Yeah, yeah.

**Sam Radwan** [08:04:22]: Okay, that's fine.

**Sam Radwan** [08:04:23]: Let me help you clarify some details around pricing and the use cases.

**Sam Radwan** [08:04:27]: And I'm hoping this call is not too frustrating for you.

**Sam Radwan** [08:04:31]: I'm really just trying to help you get the right answers.

**Sam Radwan** [08:04:34]: Oh, absolutely.

**Sam Radwan** [08:04:35]: Every

**David Orban** [08:04:36]: time I talk to a vendor with a website where they say pricing, and then the pricing is not there, yes, already the start is frustrating, absolutely.

**David Orban** [08:04:49]: And of course, it's not about you, it's not even about pitch book, it's when there isn't enough transparency, and then everything has to be fine-tuned, has to be discussed, and then, you know,

**Sam Radwan** [08:05:04]: whatever.

**Sam Radwan** [08:05:05]: Okay, no, no problem.

**Sam Radwan** [08:05:06]: I mean, API are custom solutions.

**Sam Radwan** [08:05:08]: So we have pricing for non- clients and we have pricing for clients like you guys.

**Sam Radwan** [08:05:12]: So pricing for clients is not something we're going to share publicly, but it's something that I can certainly share with you.

**Sam Radwan** [08:05:18]: Actually, why don't we start with that?

**Sam Radwan** [08:05:21]: That's great.

**Sam Radwan** [08:05:22]: You know, I'm really hoping this call is helpful, if anything for you.

**Sam Radwan** [08:05:27]: Well, well,

**David Orban** [08:05:30]: so whatever your flow is, So let me clarify my

**Sam Radwan** [08:05:38]: questions around use cases and what exactly do you

**David Orban** [08:05:42]: need?

**David Orban** [08:05:42]: The volume?

**David Orban** [08:05:43]: No, no, no, no.

**David Orban** [08:05:44]: I can't stop you because I'm not going to pay $10,000 or $100,000 for something that I don't even know how we are going to use, right?

**David Orban** [08:05:52]: That's right.

**David Orban** [08:05:53]: So this is exactly how you stop people using your platform.

**David Orban** [08:05:58]: And that's it.

**David Orban** [08:05:59]: That's it.

**David Orban** [08:06:00]: So I know I'm going to pick up the phone.

**David Orban** [08:06:03]: talk to chubby brain, whatever they are called now, and ask, hey, do you want our business?

**David Orban** [08:06:11]: Because evidently, PG-Book doesn't want our business, because I told them, listen, I don't even know how I'm going to use the API, and they said, why don't you fork over 10K, and then you can think of how you use the API?

**David Orban** [08:06:28]: Right?

**David Orban** [08:06:28]: That is what this table tells me.

**David Orban** [08:06:31]: I'm just a little confused, and, you know, Okay, let me just take a step back.

**Sam Radwan** [08:06:37]: I'm the account manager of.

**Sam Radwan** [08:06:40]: Of your team here at Pitchbook.

**Sam Radwan** [08:06:41]: And I think your colleagues have already sort of worked with us.

**Sam Radwan** [08:06:45]: And we have

**David Orban** [08:06:47]: a... No, no, of course.

**David Orban** [08:06:48]: And obviously, I'm not going to terminate our agreement.

**David Orban** [08:06:51]: It's not in my power.

**David Orban** [08:06:52]: We already subscribe.

**David Orban** [08:06:55]: My role is head of innovation.

**David Orban** [08:06:58]: Cool.

**David Orban** [08:06:58]: I am in charge of integrating AI workflows.

**David Orban** [08:07:03]: Yes.

**David Orban** [08:07:03]: I am developing all kinds of things that my colleagues find cool.

**David Orban** [08:07:08]: And I would love to integrate pitchbook into these workflows.

**David Orban** [08:07:14]: Right.

**David Orban** [08:07:15]: But no, I'm not going to propose that to, you know, to... to start with this threshold.

**David Orban** [08:07:27]: That's OK,

**Sam Radwan** [08:07:28]: David.

**Sam Radwan** [08:07:28]: That's totally fine.

**Sam Radwan** [08:07:29]: I mean, you know, you guys do have access to what we do through our online platform, and that's fine.

**Sam Radwan** [08:07:36]: Clients that work with Pitchbook and need to integrate into their workflows with AI automation.

**Sam Radwan** [08:07:43]: They will find this type of pricing reasonable, depending on the type of volume that you need.

**Sam Radwan** [08:07:47]: Clearly you don't, but simply because it's not something that I don't think you fully understand how this could even give any value to your team, which is why you find this price a bit unreasonable in two minutes.

**Sam Radwan** [08:07:59]: We're not trying

**David Orban** [08:08:00]: to... No, no, no.

**David Orban** [08:08:01]: It's, it's... And, you know, we are not entering into the detail of whatever the call covers, right?

**David Orban** [08:08:10]: What kind of the API returns a data set.

**David Orban** [08:08:14]: So what is the data set?

**David Orban** [08:08:16]: Yes.

**David Orban** [08:08:17]: And then I think it is $1 per API call.

**David Orban** [08:08:21]: And so one dollar per data set.

**David Orban** [08:08:25]: Yeah.

**David Orban** [08:08:25]: And I'm sure it is very much worth it.

**David Orban** [08:08:32]: Apologies.

**David Orban** [08:08:33]: What

**Sam Radwan** [08:08:33]: the problem?

**Sam Radwan** [08:08:34]: What is the problem then?

**Sam Radwan** [08:08:35]: Because I was hoping to give you

**David Orban** [08:08:36]: my clarity on technicalities and conventions.

**David Orban** [08:08:40]: Yes.

**David Orban** [08:08:41]: So the problem is simple.

**David Orban** [08:08:47]: Currently, I'm running experiments.

**David Orban** [08:08:51]: Okay.

**David Orban** [08:08:52]: And I'd rather run experiments that cost zero and then cost more and more as they pool their utility.

**David Orban** [08:09:01]: Yeah.

**David Orban** [08:09:02]: Then run an experiment and say, hey, why don't we start spending $10,000 to buy

**Sam Radwan** [08:09:08]: something that... I wouldn't ask you to do that.

**Sam Radwan** [08:09:11]: We can get you in a sandbox environment, we can test it.

**Sam Radwan** [08:09:16]: I would have gone to this part later on during the call, but if this is something that you want to evaluate or try or test and see if it actually works for you, we wouldn't ask you, we wouldn't charge you anything until you really know if it works or not.

**Sam Radwan** [08:09:28]: The way it usually works.

**Sam Radwan** [08:09:30]: We would get an understanding of the universe you want to extrapolate from Facebook the data points, so the type of information that you need to feed through the API.

**Sam Radwan** [08:09:41]: We don't have to discuss this now.

**Sam Radwan** [08:09:43]: I can send you some information.

**Sam Radwan** [08:09:44]: And when you have more sort of clarity on the details, we can get into that.

**Sam Radwan** [08:09:50]: down the line and then when that is all sort of determined we can get you and the team on a sandbox environment you test it you see how it works and if you want to go ahead with it fine if you don't and that's also totally okay

**David Orban** [08:10:05]: okay so wonderful yes please send me the documentation okay and then give me access to the sandbox okay without requiring me to have already clarity.

**David Orban** [08:10:17]: It is using the sandbox that will give me clarity.

**Sam Radwan** [08:10:23]: Yes, we would need We can take this by email.

**Sam Radwan** [08:10:27]: We need additional information of what you need to test on the sandbox.

**Sam Radwan** [08:10:30]: We can't give you our entire universe of data to test, but we can give you a temporary access and the team to a set of data that you want to evaluate.

**Sam Radwan** [08:10:40]: This will give you an idea of what the format looks like, the accuracy of the information looks like compared to what you already have with us.

**David Orban** [08:10:47]: Okay, and I'll share some stuff with you.

**David Orban** [08:10:51]: One sec.

**David Orban** [08:10:52]: Is the documentation is the documentation such that without looking at the sandbox I can imagine the types of things that we would want to do?

**David Orban** [08:11:06]: Yes,

**Sam Radwan** [08:11:07]: yes, of course.

**Sam Radwan** [08:11:07]: So I'm sharing my screen now.

**Sam Radwan** [08:11:09]: This is the type of API calls we have.

**Sam Radwan** [08:11:12]: So from a qualitative point of view, you get different type of calls.

**Sam Radwan** [08:11:17]: We have broken these down by macro types, if you like.

**Sam Radwan** [08:11:22]: So you have the general information, you have the specific portfolio companies and points.

**Sam Radwan** [08:11:26]: Each one of those is a different type of call.

**Sam Radwan** [08:11:30]: I'll share this document with you because it covers portfolio companies, deals, funds, and obviously from managers.

**Sam Radwan** [08:11:35]: And

**David Orban** [08:11:36]: each of these calls basically costs a dollar prepaid.

**David Orban** [08:11:40]: Each

**Sam Radwan** [08:11:41]: of these calls cost a prepaid pricing.

**Sam Radwan** [08:11:43]: Yes, that's right.

**Sam Radwan** [08:11:44]: And then you find a breakdown further.

**Sam Radwan** [08:11:47]: So for each macro type and type of call, you have a whole list of data that get.

**Sam Radwan** [08:11:54]: So for example, if you want to call the entity people, You get all this bunch of information around any given entity.

**Sam Radwan** [08:12:05]: So on and so forth when it comes to portfolio companies.

**Sam Radwan** [08:12:08]: And if you scroll down, you'll be invested.

**Sam Radwan** [08:12:12]: It's quite self-explanatory, but if you have any questions, let me know, or we can clarify.

**David Orban** [08:12:17]: Okay, so once again, as you scroll down, each API calls a return data structure is detailed, right?

**David Orban** [08:12:39]: So when we are talking about entity people, I will have each of those filled up.

**David Orban** [08:12:48]: Correct.

**David Orban** [08:12:48]: And I pay $1 for the entire record.

**David Orban** [08:12:53]: Is that

**Sam Radwan** [08:12:53]: correct?

**Sam Radwan** [08:12:54]: That's correct.

**Sam Radwan** [08:12:55]: The entire code.

**Sam Radwan** [08:12:56]: It would refresh over time, because that's our job to keep data updated on our end, but it won't cost you anything in the future because you called it once, and as it refreshes, I think this is important to know.

**Sam Radwan** [08:13:07]: Over time, you already have that call in your system, and you already paid for it once.

**Sam Radwan** [08:13:13]: I

**David Orban** [08:13:13]: see, so the NPPID is the identifier that will... that we paid for and then additional calls to the same entity ID don't cost more money and

**Sam Radwan** [08:13:29]: that's how it technically matches on your end but as I said it's our job to I think one of the core values of API is that we in the back end are working on keeping the information updated over time you paid for it once and you keep it as it is and it refreshes automatically on your end obviously As

**Sam Radwan** [08:13:45]: we, as the agreement expires next year, then we will refresh the whole setting and you will pay for it again.

**Sam Radwan** [08:13:53]: But yeah, no.

**Sam Radwan** [08:13:54]: Yeah,

**David Orban** [08:13:55]: it's good to know that you pay for it once throughout the whole agreement.

**David Orban** [08:13:57]: Okay, yeah, yeah, that is good.

**David Orban** [08:14:02]: Together with this documentation, can you also send more than just the table that you flashed on the screen?

**David Orban** [08:14:10]: Is there a TNCs around that 10K that we start with or whatever?

**Sam Radwan** [08:14:17]: Yeah, I think I can share with you an empty draft with the TNCs conclude.

**Sam Radwan** [08:14:26]: So you can take a look at

**David Orban** [08:14:27]: that.

**David Orban** [08:14:28]: And can you send me also the pricing?

**David Orban** [08:14:32]: Sure.

**David Orban** [08:14:33]: Okay.

**David Orban** [08:14:42]: All right.

**David Orban** [08:14:44]: Okay.

**David Orban** [08:14:46]: Anything else that I should ask apart from apologizing for the antagonistic

**Sam Radwan** [08:14:51]: attitude.

**Sam Radwan** [08:14:54]: I'm hoping you'd have a good rest of the day.

**Sam Radwan** [08:14:57]: I don't know, you know, I know you guys have an access to our platform, and I should have started maybe introducing myself, and I'm the account manager of your company here at Pittsburgh, and I'll be looking after our relationship on different fronts as we evolve.

**Sam Radwan** [08:15:11]: The current account that you guys have with us is being used.

**Sam Radwan** [08:15:15]: So I know you have the perception that it's not really used as much.

**Sam Radwan** [08:15:20]: But is

**David Orban** [08:15:21]: it used to the fullest of its, you know, we subscribe, I think for 10

**Sam Radwan** [08:15:27]: licenses, right?

**Sam Radwan** [08:15:29]: Correct, yes.

**Sam Radwan** [08:15:30]: So this is up to, you guys have got seven at the minute.

**Sam Radwan** [08:15:33]: You've got three unused licenses.

**Sam Radwan** [08:15:36]: So it's definitely underused.

**David Orban** [08:15:38]: I wouldn't even the seven people, the seven named people, and I don't know what is the distribution of the experience amongst your users.

**David Orban** [08:15:48]: If you have a Bloomberg terminal subscription, you use it every day, all day.

**David Orban** [08:15:53]: So maybe it is not the same for a pitch book, it is more occasional on an as needed basis.

**David Orban** [08:15:59]: But if you compare your typical user with our seven named users, I think you will find that It's not that as intensive as it should be, right?

**David Orban** [08:16:10]: And that is why I'm saying we are on the same side.

**David Orban** [08:16:13]: My objective is to increase the use of Pitchbook in order for it to be better integrated in our workflows, in our lookups, enriching CRM, allowing people to prepare for meetings or whatever else, right?

**David Orban** [08:16:29]: And rather than doing it manually to do it in a fashion that comes, yeah, that comes... easy to them rather than, oh, you know, even even the login into page book is, oh, I have to log in again, it expired, whatever else.

**David Orban** [08:16:45]: It is just an obstacle, right?

**David Orban** [08:16:47]: So that is where I'm coming from.

**David Orban** [08:16:51]: So I'm looking forward to your email with the details, I will work out some experiments.

**David Orban** [08:16:58]: Send them back to you.

**David Orban** [08:17:00]: You will say yes or no.

**David Orban** [08:17:04]: I will be allowed to test them out in the sandbox or not.

**David Orban** [08:17:08]: And then we will take it from there.

**David Orban** [08:17:11]: No problem.

**David Orban** [08:17:11]: A loop

**Sam Radwan** [08:17:11]: in the right person that can set up the sandbox for you.

**Sam Radwan** [08:17:14]: Let us know what you need to test.

**Sam Radwan** [08:17:15]: And yeah, we can we can go from there.

**Sam Radwan** [08:17:19]: On the platform side of things, this is a separate conversation.

**Sam Radwan** [08:17:23]: We don't have to tackle it now.

**Sam Radwan** [08:17:25]: But if you like, we can arrange In a range of quick session where you tell us exactly what you need from our service and how you want us to support you and the team moving forward and hopefully we can pick up the usage overall, not just for yourself, but you know, you guys are, I'd say mid-market,

**Sam Radwan** [08:17:45]: new clients that we have, you have spare licenses, and yeah, it's within our customer success team also to make sure you guys are fully using the service so it can justify renewal in the future.

**David Orban** [08:17:56]: So, but that's just a sad note.

**David Orban** [08:17:59]: Okay, thank you, Sam.

**Sam Radwan** [08:18:02]: Cool, thanks.

**Sam Radwan** [08:18:03]: Bye-

---
*Backed up from MeetGeek on 2026-03-30 08:49*
