# CRM & Dashboard Sandbox Planning

**Date:** 2025-12-08
**Duration:** Unknown
**Meeting ID:** 3d7a1915-1e89-4cea-8cf2-549ab53ed71c

## Participants
- *Participants not listed*

### Summary

The meeting centered on establishing an experimental Alivan Labs sandbox and a first-dashboard application to safely test integrations using synthetic data before connecting regulated client information. David outlined broad data sources (CRM, Asana, accounting, transcripts) and a digital twin to simulate objectives; the group discussed practical CRM adoption tactics—using PipeDrive BCC to capture emails—and the need for richer PipeDrive-derived KPIs combining operational and financial metrics. Attendees agreed to exchange KPIs/OKRs, secure division head buy-in, and leverage role-based access control for controlled views prior to production integration.

## Full Transcript

**Speaker_00** [14:39:29]: I know, but you can suck it up.

**Speaker_03** [14:39:37]: So.

**Speaker_01** [14:39:39]: Yeah, with regard to the top dog reports and the dashboard you already shared with me all the morning.

**Speaker_01** [14:39:48]: I tried to have the access and to just I need to know the source for the data and how they are linking the needs or revenue side with this.

**Speaker_01** [14:40:01]: This

**Speaker_00** [14:40:02]: is completely fake.

**Speaker_01** [14:40:03]: Yeah, yeah, okay.

**Speaker_01** [14:40:05]: So the purpose is to have everything on pipe drive move here or to have an integration thing between... Okay.

**Speaker_00** [14:40:14]: So, I thought we would be starting from the thing that you guys have been working on.

**Speaker_02** [14:40:22]: Yeah.

**Speaker_00** [14:40:23]: But we can start from the opposite direction as well.

**Speaker_01** [14:40:26]: Which

**Speaker_00** [14:40:27]: is?

**Speaker_00** [14:40:27]: And I, well, to explain to you what I am doing.

**Speaker_01** [14:40:31]: Yeah, yeah,

**Speaker_00** [14:40:31]: please.

**Speaker_00** [14:40:35]: as a regulated entity, our systems are locking down, right?

**Speaker_00** [14:40:46]: With a tighter and tighter control.

**Speaker_02** [14:40:49]: Yeah.

**Speaker_00** [14:40:49]: Because we have to be compliant with whatever regulations we fall

**Speaker_01** [14:41:00]: under.

**Speaker_01** [14:41:00]: Yeah,

**Speaker_00** [14:41:01]: true.

**Speaker_00** [14:41:01]: And so we have to plan for what we need to pass certain checks and only after they pass those checks we can integrate them with data that is concerning for example the clients and so on and so forth right and Chidem and I had a meeting and she said yes and you know my experience in Germany with the

**Speaker_00** [14:41:37]: SEC whatever is the the Frankfurt Stock Exchange etc is that we standardize and then maybe in a couple of years we revisit if there is something that we need to change in

**Speaker_01** [14:41:51]: terms of having a platform to

**Speaker_00** [14:41:53]: yeah whatever solutions they chose and so I fainted And then a few minutes later I said, what did you say?

**Speaker_00** [14:42:04]: Because, yeah, especially for my area, if it were for me, we would reevaluate every two weeks what we choose and what we use, right?

**Speaker_00** [14:42:20]: And of course I understand her point of view as well.

**Speaker_00** [14:42:25]: So we need to find a balance.

**Speaker_01** [14:42:27]: Which

**Speaker_00** [14:42:27]: is to

**Speaker_01** [14:42:28]: have one platform or to have an official?

**Speaker_00** [14:42:32]: Neither.

**Speaker_00** [14:42:33]: So one platform will never work.

**Speaker_00** [14:42:38]: It is impossible to have a single black rock, which is the largest firm, our competitor with trillions of dollars under management.

**Speaker_00** [14:42:48]: doesn't have a single platform.

**Speaker_02** [14:42:51]: Okay.

**Speaker_00** [14:42:51]: They have multiple platforms that barely integrate.

**Speaker_00** [14:42:54]: They are different and it's even a bit painful to look at.

**Speaker_00** [14:43:02]: So no, having a single platform is not possible.

**Speaker_00** [14:43:06]: So what I did is, one, to establish a sandbox, okay, a separate domain where we can experiment.

**Speaker_00** [14:43:20]: Whoever wants to bring ideas, whoever wants to bring tools, we can try and see whether they are important enough to then evaluate, do the tools pass the checks.

**Speaker_00** [14:43:36]: If they pass the checks, then we talk to Chidem.

**Speaker_00** [14:43:40]: and we say sorry you have to integrate this because one the tool passes the checks and two it is very important we already tested it this is the reason why we need it okay so that is the purpose of the of the, not of the dashboard of the Alivan Labs sandbox.

**Speaker_00** [14:44:03]: I registered this domain.

**Speaker_01** [14:44:05]: For filtering the systems we are using.

**Speaker_00** [14:44:07]: For testing, for experimenting, without touching client data, without doing any regulated any.

**Speaker_00** [14:44:14]: So this is, you know, we could be building a video game, we could be building a social network, whatever.

**Speaker_00** [14:44:21]: Instead, we are simulating the activities with synthetic data, with fake data, okay?

**Speaker_00** [14:44:31]: So, the first application of this approach, of this experimental approach that doesn't need permission from anyone, not the regulators, and of course Michael knows, it's not that I'm doing it without Michael knowing, but I didn't even ask permission.

**Speaker_00** [14:44:53]: I just told him, I am doing this.

**Speaker_00** [14:44:55]: Okay.

**Speaker_00** [14:44:56]: Yeah.

**Speaker_00** [14:44:57]: The first application of this approach is the dashboard.

**Speaker_02** [14:45:02]: Yeah.

**Speaker_00** [14:45:03]: Where the dashboard shows what we could do in order to serve our purpose in a way that no third party tool will ever serve.

**Speaker_00** [14:45:17]: Because every third party tool will only do a little bit of what we need, or maybe a lot of what we need, but if there is 20% missing, and you pick up the phone and say, can you please do that 20%?

**Speaker_00** [14:45:31]: They will say, okay, get in line, next release, maybe in two years, maybe in one year, whenever it is, maybe we will do it or not, even if you need it, right?

**Speaker_00** [14:45:41]: But instead, integrating the data from the various sources, we can have what we need exactly.

**Speaker_00** [14:45:51]: Exactly what we need and we can iterate, oh well, not right away, but iterating and then very rapidly improving we can have what we need and what we want.

**Speaker_00** [14:46:03]: So what are those data sources?

**Speaker_00** [14:46:06]: Everything.

**Speaker_00** [14:46:08]: that is the AI speaking.

**Speaker_02** [14:46:11]: I

**Speaker_00** [14:46:11]: see.

**Speaker_00** [14:46:11]: Literally everything.

**Speaker_00** [14:46:14]: Everything.

**Speaker_00** [14:46:16]: Yeah.

**Speaker_00** [14:46:18]: trivial, Asana for task management, pipe drive for CRM, the meeting transcripts, the accounting data, budget data, both forecast and then, you know, real-time.

**Speaker_01** [14:46:41]: Yeah, yeah, yeah, comparison between actuals and forecast.

**Speaker_00** [14:46:43]: Expenses, revenues, projections, everything.

**Speaker_00** [14:46:48]: and even metadata.

**Speaker_00** [14:46:53]: For example, it is not here, it's not represented yet, but I will create a visualization of that as well.

**Speaker_00** [14:47:00]: I already created a digital twin of the organization where every function, every person, every activity is represented

**Speaker_02** [14:47:10]: so

**Speaker_00** [14:47:11]: that we can simulate what we want to maximize.

**Speaker_00** [14:47:16]: Do we want to maximize revenues or long-term upside?

**Speaker_00** [14:47:21]: Do we want to maximize geographical coverage or depth of presence here, or whatever else?

**Speaker_00** [14:47:31]: and then we can simulate how outside events impact our business in different ways.

**Speaker_00** [14:47:41]: Thanks, thanks.

**Speaker_00** [14:47:43]: So that is the reason because I wanted to show something that every person

**Speaker_02** [14:47:54]: that

**Speaker_00** [14:47:54]: they understand, right?

**Speaker_00** [14:47:56]: Because it is their own stuff.

**Speaker_00** [14:47:57]: So they say, oh wow, this is good, or they say, no, this doesn't make sense or whatever else,

**Speaker_02** [14:48:02]: right?

**Speaker_00** [14:48:03]: And I don't know if you looked, but there is, so here, for

**Speaker_02** [14:48:06]: example,

**Speaker_00** [14:48:08]: in advisory or KRs, as an example, if the objective is to have a given number of clients, and those clients come from having been able to speak to a given number of targets, then we can check are we in line with that?

**Speaker_00** [14:48:33]: This is the objectives, K results and then key performance indicators that from a management point of view are

**Speaker_01** [14:48:43]: informative or like

**Speaker_00** [14:48:44]: giving the updates related to it.

**Speaker_00** [14:48:46]: And giving them the opportunity to say wow David needs help

**Speaker_02** [14:48:52]: yeah

**Speaker_00** [14:48:52]: because he's really not able to achieve his objectives and then they can either give help to David or fire David you know whatever they want to

**Speaker_02** [14:49:03]: decide

**Speaker_00** [14:49:04]: okay so so each area has a very specific another one is in the family office where not only we have who are the families and what are their assets and what are the services that we provide to them, but even what type of philanthropy they are following and we are supporting them in their

**Speaker_00** [14:49:34]: philanthropic activities and ambitions, right?

**Speaker_00** [14:49:38]: So a lot of different

**Speaker_02** [14:49:40]: ways.

**Speaker_02** [14:49:41]: Now,

**Speaker_00** [14:49:42]: back to, if this is clear, right?

**Speaker_00** [14:49:45]: So, sandbox to experiment.

**Speaker_00** [14:49:47]: The first illustration of what we can be experimenting is the dashboard, right?

**Speaker_00** [14:49:54]: And now we can talk about specifically the CRM of what ideas maybe you already have to mine the data, in order to surface information, right?

**Speaker_02** [14:50:15]: I see.

**Speaker_00** [14:50:17]: So I don't know if you already have any idea.

**Speaker_01** [14:50:20]: Yeah, actually I'm studying how we have now dashboards here on the system of pipe drive, but primarily The goal should be is from the finance perspective what I want to see from the performance from the things that we need to know about the leads we have the raw data and how these data are qualified

**Speaker_01** [14:50:43]: to be informative and upon the information we are getting from the dashboard or the elementary analysis of what type of customer we have the sector we are serving and so we would go to the level of qualified data or prospective customers or investors based on this we would check the conversion rates

**Speaker_01** [14:51:02]: the sales based KPIs that would tell us how where we are in the pipeline as well as the conversion to active projects we would have and the number of projects owned or won't we already won based on the analysis so we can have the utilization metrics clarified and so I'm working on this from what we

**Speaker_01** [14:51:27]: have already and getting the idea of what should we have from the dashboard perspective and the preparing this to set with Ivan and work on this together and then we can integrate whatever we would have this on the system

**Speaker_00** [14:51:42]: on the dashboard So you report to Toby, right?

**Speaker_03** [14:51:48]: Sherwin.

**Speaker_00** [14:51:49]: To Sherwin.

**Speaker_00** [14:51:52]: Because I believe you are almost ready to ask Sherwin to please send an email that everyone is obliged to use the CRM.

**Speaker_00** [14:52:04]: Aren't you almost there?

**Speaker_03** [14:52:06]: I mean, he already sent one like

**Speaker_00** [14:52:08]: that.

**Speaker_00** [14:52:08]: He did?

**Speaker_00** [14:52:09]: Yeah.

**Speaker_00** [14:52:09]: And not a lot of people

**Speaker_03** [14:52:12]: cared.

**Speaker_03** [14:52:12]: And you know, off the back of that, I arranged the training, which we did with, well,

**Speaker_00** [14:52:17]: New York, yeah.

**Speaker_03** [14:52:18]: With the New York team.

**Speaker_00** [14:52:18]: And did you do the other one too?

**Speaker_03** [14:52:20]: No, because nobody else from the people that I emailed replied.

**Speaker_00** [14:52:24]: I see.

**Speaker_03** [14:52:25]: So I need to do another chase now to capture all those people.

**Speaker_03** [14:52:29]: But actually, before doing that, I'm actually going back through into the CRM to review all the users that we have and actually be a bit more critical of who actually needs to

**Unknown speaker** [14:52:40]: be in

**Speaker_03** [14:52:41]: the... who actually needs to

**Speaker_00** [14:52:42]: be a user.

**Speaker_00** [14:52:42]: Because the lowest hanging fruit, in my opinion, that could ease the pain is to start using the BCC in their email.

**Speaker_01** [14:52:56]: What is the BCC?

**Speaker_00** [14:52:57]: BCC stands for blind carbon

**Speaker_01** [14:53:00]: copy.

**Speaker_01** [14:53:00]: Like the CC thing, right?

**Speaker_00** [14:53:02]: So it's another field.

**Speaker_01** [14:53:04]: Oh, but what should we use this for?

**Speaker_00** [14:53:08]: So the CRM allows you to capture the emails that you are sending by simply adding an email address that is not visible to the person that you are emailing because you are putting it on the BCC field.

**Speaker_02** [14:53:29]: I see,

**Speaker_00** [14:53:30]: huh?

**Speaker_00** [14:53:30]: The BCC field stands for blind carbon copy.

**Speaker_00** [14:53:34]: Okay, perfect.

**Speaker_00** [14:53:35]: So PipeDrive says you say Ali1123 at PipeDrive.com or something like that.

**Speaker_00** [14:53:42]: Oh, you're

**Speaker_01** [14:53:42]: adding the PipeDrive email, so it can sync the details related to customers and people are sending to each other.

**Speaker_00** [14:53:50]: Correct.

**Speaker_00** [14:53:51]: And the reason why that is, I call that a low- hanging fruit is because it doesn't take effort from the person, they use the same system as before, Outlook, and the record is created at least, and then their communication is captured with the prospective clients or whatever.

**Speaker_00** [14:54:17]: and that is something that everyone should be doing.

**Speaker_00** [14:54:21]: I

**Speaker_03** [14:54:21]: need to check, I don't know if you know whether, if you BCC someone that doesn't exist in the system, I don't know if it creates a new user.

**Speaker_03** [14:54:29]: I think it will only work if that person,

**Speaker_00** [14:54:31]: if that, a new customer.

**Speaker_00** [14:54:33]: Customer,

**Speaker_03** [14:54:33]: sorry, no user,

**Speaker_00** [14:54:34]: customer.

**Speaker_00** [14:54:35]: I think you, well, it should, it should.

**Speaker_00** [14:54:37]: I guarantee that it is a setting that you can, maybe it keeps it in a special category, but absolutely.

**Speaker_03** [14:54:47]: I don't know, but worth

**Speaker_01** [14:54:52]: checking.

**Speaker_01** [14:54:52]: And this for like

**Speaker_00** [14:54:54]: updating the

**Speaker_01** [14:54:54]: information from the customer

**Speaker_00** [14:54:56]: or

**Speaker_01** [14:54:56]: like having the active customer's details reflected on the system?

**Speaker_00** [14:55:00]: No, the reason I was mentioning this is because if our team doesn't universally use the CRM, you know, not from you to me, not internally, but in our external communications, then there's nothing to analyze.

**Speaker_00** [14:55:19]: There's no data to capture.

**Speaker_00** [14:55:20]: Yeah, but I'm thinking

**Speaker_01** [14:55:21]: of the email itself, it's a stage of having the customer already signed the contract, so we are information based on this.

**Speaker_01** [14:55:27]: No, no, no, no.

**Speaker_00** [14:55:28]: It's not

**Speaker_03** [14:55:28]: necessarily just the customer.

**Speaker_03** [14:55:29]: In fact, it's not predominantly the customers.

**Speaker_03** [14:55:32]: It's more prospects, it's more people that are not yet customers.

**Speaker_03** [14:55:38]: It's

**Speaker_01** [14:55:38]: more of the... Like from the lead phase, like from the industry

**Speaker_03** [14:55:42]: phase.

**Speaker_01** [14:55:42]: Yes, yes,

**Speaker_03** [14:55:43]: yes.

**Speaker_03** [14:55:43]: Customers are also in there, but it's more like...

**Speaker_01** [14:55:45]: I need to check from which stage it's capturing that information from the early stage.

**Speaker_03** [14:55:51]: As soon as there's an email, like that you capture that information.

**Speaker_03** [14:55:55]: But obviously this is... just for the purpose of tracking emails.

**Speaker_03** [14:55:59]: And I agree, this is the low

**Speaker_00** [14:56:01]: hanging fruit.

**Speaker_00** [14:56:02]: It is so that you can pull people in rather than imposing it and then, you know, creating conflict.

**Speaker_00** [14:56:14]: This is an easy way to get them also to understand the advantage.

**Speaker_03** [14:56:20]: Yeah, but for the purpose of extracting then useful data, Emails alone is not going to provide much other than the amount of emails that we're sharing that have been sent to this

**Speaker_02** [14:56:33]: person.

**Speaker_00** [14:56:35]: That's another question.

**Speaker_00** [14:56:36]: um so the the record created then can be enriched with information and and then what information is added on top is another question yes of course

**Speaker_01** [14:56:53]: okay so we can start by adding this but we need to analyze them like we can start with from where we are now the things we're working on for the dashboard and the meetings we're going to have with people.

**Speaker_01** [14:57:07]: And then have the emails as well to be included from a part of the process to capture the data.

**Speaker_01** [14:57:15]: And then we should start analyzing what we have on Pad Drive and then reflect if we have this sun back

**Speaker_00** [14:57:23]: in.

**Speaker_00** [14:57:23]: So today we have almost nothing.

**Speaker_00** [14:57:24]: We have less than 800 people in total.

**Speaker_01** [14:57:30]: Yeah.

**Speaker_00** [14:57:31]: and there isn't much to analyze out of 800 people.

**Speaker_03** [14:57:35]: Well, it depends what you want to analyze from the internet.

**Speaker_03** [14:57:39]: There's already enough there to analyze the amount of leads, the conversion rate, how many deals we won, how long a deal sits in a certain stage of the pipeline, more of the sales related

**Speaker_00** [14:57:50]: stuff.

**Speaker_00** [14:57:53]: the quantitative data of how many leads we want is relatively easy because it doesn't depend on pipe drive if we can look at the invoices right then as soon as we want something it means there has been an invoice to the clients And part of the education and the training and the really development of

**Speaker_00** [14:58:15]: our processes, I think should include the opposite as well.

**Speaker_00** [14:58:21]: Why we think we lost the deal.

**Speaker_00** [14:58:24]: That is maybe even more important.

**Speaker_00** [14:58:26]: Which is

**Speaker_03** [14:58:26]: captured in pipe drive.

**Speaker_03** [14:58:28]: When you mark it as a lost, you either mark it as one or lost once it gets to... and then you have to mark the reason why.

**Speaker_03** [14:58:35]: Okay.

**Speaker_03** [14:58:36]: But the reasons are customized.

**Speaker_03** [14:58:39]: You cannot customize your reasons.

**Speaker_01** [14:58:42]: It's a

**Speaker_03** [14:58:43]: predefined list.

**Speaker_03** [14:58:44]: Okay.

**Speaker_01** [14:58:45]: So I believe it would be more useful to have our internal assessment of what we have on pipe drive and how we should create the different dashboards to be ready and then we should have this

**Speaker_00** [14:58:57]: in use.

**Speaker_00** [14:58:58]: So obviously your investment in learning the pipe drive reporting is wonderful and I'm not saying that you shouldn't do that.

**Speaker_00** [14:59:13]: Besides that which you are already doing, If you started to think about enlist, what are the indicators that in your opinion are useful that can be extracted from the data?

**Speaker_00** [14:59:30]: Yeah, I already

**Speaker_01** [14:59:31]: have the list of the main KPIs for each division.

**Speaker_01** [14:59:36]: based on which aspects we should consider ourselves utilizing our resources in terms of the people are working on something, our capabilities as, like we have the investment banking team, the investment banking team is capable of doing or providing specific services.

**Speaker_01** [14:59:52]: Based on this regulated, unregulated thing, we need to have the KPIs up on

**Speaker_00** [14:59:57]: which we are

**Speaker_01** [14:59:57]: capturing that

**Speaker_00** [14:59:58]: I also independently developed the same so I will be happy to send you my KPIs and OKRs and then we can see.

**Speaker_01** [15:00:07]: Yeah,

**Speaker_00** [15:00:08]: from the

**Speaker_01** [15:00:08]: finance perspective we can have

**Speaker_00** [15:00:09]: this

**Speaker_01** [15:00:10]: along with the tech side perspective.

**Speaker_01** [15:00:12]: Okay.

**Speaker_02** [15:00:13]: Okay, wonderful.

**Speaker_01** [15:00:16]: Let's have our thing first and then we should have the meeting based on how to grab everything together and present

**Speaker_00** [15:00:24]: it.

**Speaker_00** [15:00:24]: So in terms of visualizing the data, an advantage of this approach is that at any level and by the way not today but tomorrow

**Speaker_02** [15:00:38]: the

**Speaker_00** [15:00:39]: access will be so-called Rbac role-based access control so that someone will only see their division and others will see everything and whatever in between right so One advantage of this approach is that as long as the systems are connected, people don't need to switch.

**Speaker_00** [15:01:06]: Oh, I'm looking at this here, I'm looking at that there, but they have a unified view.

**Speaker_00** [15:01:11]: They have a unified view,

**Speaker_02** [15:01:12]: right?

**Speaker_00** [15:01:14]: So I am already able to, both from a programmatic point of view to interface with pipe drive that works perfectly.

**Speaker_00** [15:01:29]: as well as Asana and meet geek and other things.

**Speaker_00** [15:01:33]: So the basis is there.

**Speaker_01** [15:01:37]: Okay.

**Speaker_01** [15:01:38]: Okay, perfect.

**Speaker_01** [15:01:39]: Okay.

**Speaker_01** [15:01:40]: Thank

**Speaker_00** [15:01:40]: you so

**Speaker_01** [15:01:40]: much for that.

**Speaker_00** [15:01:41]: Thank you.

**Speaker_03** [15:01:41]: So what are the next steps?

**Speaker_03** [15:01:42]: We're going to share the OKRs PPI?

**Speaker_00** [15:01:44]: Yes, yes.

**Speaker_00** [15:01:46]: Yes, that's right.

**Speaker_00** [15:01:47]: So we will, we will exchange these documents to see what what is the same, what is different, and then obviously the division heads have to get buying from them that they agree those KPIs are correct and then they have to share them with their team

**Speaker_01** [15:02:20]: They would have their operating KPIs and there are the financial KPIs.

**Speaker_01** [15:02:25]: The financial KPIs is the finance perspective of what the operations should

**Unknown speaker** [15:02:30]: be.

**Speaker_01** [15:02:31]: From the operation side, they have their team, they need to analyze how, for example, if Ivan part of the team, they need to analyze how Ivan is utilizing his time between managing reporting and having meetings and having calls and all the journey from having a prospect customer in order to have the

**Speaker_01** [15:02:52]: active project.

**Speaker_01** [15:02:52]: If you have some number of analysts as well as how they are utilizing their meetings or how they are utilizing the information received from the customer.

**Speaker_01** [15:03:03]: They have operating KPIs.

**Speaker_01** [15:03:06]: You would have the operating side of dashboards and the financial side.

**Speaker_01** [15:03:11]: From a business partner perspective, we would have both combined so we can have the conversion rate combined with the revenue amount we received, so we have the taste of the finance with the business as well.

**Speaker_01** [15:03:23]: So we would have both of them

**Speaker_00** [15:03:24]: together.

**Speaker_00** [15:03:25]: And indicators like the margin of contribution of each division and whether they are...

**Speaker_01** [15:03:31]: Yeah, based on the financial data,

**Speaker_00** [15:03:32]: we would

**Speaker_01** [15:03:32]: have the operational side

**Speaker_00** [15:03:34]: as

**Speaker_01** [15:03:34]: well involved.

**Speaker_00** [15:03:36]: Okay.

**Speaker_01** [15:03:37]: Okay, so I will just fire me with you guys and then we can go

**Speaker_00** [15:03:41]: together.

**Speaker_00** [15:03:42]: Okay, very

**Unknown speaker** [15:03:44]: good.

---
*Backed up from MeetGeek on 2026-03-30 08:50*
