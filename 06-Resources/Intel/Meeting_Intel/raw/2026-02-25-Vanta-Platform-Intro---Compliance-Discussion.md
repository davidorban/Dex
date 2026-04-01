# Vanta Platform Intro & Compliance Discussion

**Date:** 2026-02-25
**Duration:** Unknown
**Meeting ID:** fa87aa5a-1685-43e1-932e-51b6549de640

## Participants
- *Participants not listed*

### Summary

The meeting covered Alliwan's company context and key stakeholders, followed by a detailed Vanta product overview emphasizing automated evidence collection via many native integrations and support for custom regulatory frameworks. Discussion addressed regional regulatory coverage and Microsoft/Azure integration needs, implementation effort and readiness assessment, vendor/third-party risk capabilities, pricing tiers based on headcount in scope, audit partner support, data residency concerns (data stored in Germany and primarily metadata), AI-driven policy suggestions and bulk document analysis, and specific follow-ups: David will send a recap with outstanding questions and Matthew will follow up by email with pricing and integration details.

## Full Transcript

**David Orban** [12:00:38]: That's done that.

**David Orban** [12:01:41]: Hello,

**Matthew Oliver** [12:01:42]: David.

**Matthew Oliver** [12:01:43]: Hi, Matthew.

**Matthew Oliver** [12:01:43]: How are you?

**Matthew Oliver** [12:01:44]: I'm good.

**Matthew Oliver** [12:01:45]: Sorry about keeping you waiting.

**Matthew Oliver** [12:01:47]: Nice to meet you.

**Matthew Oliver** [12:01:48]: A

**David Orban** [12:01:48]: full minute.

**David Orban** [12:01:49]: Oh, my God.

**David Orban** [12:01:54]: All right.

**David Orban** [12:01:55]: So thank you for sending the PDF ahead.

**Matthew Oliver** [12:01:59]: Sure.

**Matthew Oliver** [12:02:04]: I

**David Orban** [12:02:04]: have a bunch of questions that if I had received the PDF earlier, then I could have maybe sent you via email.

**Matthew Oliver** [12:02:14]: And

**David Orban** [12:02:17]: I am happy to just rattle them off.

**David Orban** [12:02:19]: Yes, of

**Matthew Oliver** [12:02:20]: course.

**Matthew Oliver** [12:02:20]: And you can tell me if you have the answers or

**David Orban** [12:02:22]: not, and if you're not, then you can follow up with an email, which is fine.

**David Orban** [12:02:28]: Of

**Matthew Oliver** [12:02:28]: course.

**Matthew Oliver** [12:02:29]: So first, let me tell you

**David Orban** [12:02:31]: a bit about who we are and what we do so you have a better picture.

**Matthew Oliver** [12:02:38]: Al-liwan is the

**David Orban** [12:02:40]: first... Abudabi headquartered GCC based investment bank

**Matthew Oliver** [12:02:48]: of a merchant bank tradition.

**David Orban** [12:02:50]: We participate as a principal in the deals we structure with the offices in Abu Dhabi, Riyad, London, New York and Tel Aviv.

**Matthew Oliver** [12:03:05]: with investment banking,

**David Orban** [12:03:07]: asset management, wealth management

**Matthew Oliver** [12:03:19]: and $10 billion

**David Orban** [12:03:22]: under management as our starting point holding category 1 licenses from ESCA and 3C licenses from ADGN.

**Matthew Oliver** [12:03:40]: I

**David Orban** [12:03:41]: don't know how much of that is comprehensible for you or not, given the acronym salad that I rattled

**Matthew Oliver** [12:03:51]: off.

**Matthew Oliver** [12:03:54]: What

**David Orban** [12:03:55]: matters is that we have both regulated and unregulated activities, both onshore and offshore activities.

**David Orban** [12:04:03]: And in terms of the regulators, we are subject to several jurisdictions,

**Matthew Oliver** [12:04:08]: not only UAE, but Saudi and

**David Orban** [12:04:11]: the UK and others that I didn't even mention because they will be coming later on in Switzerland and so on.

**Matthew Oliver** [12:04:23]: So

**David Orban** [12:04:24]: I am head of innovation and

**David Orban** [12:04:31]: temporarily I'm also covering for head of IT.

**David Orban** [12:04:37]: The new person is coming on board end of March.

**Matthew Oliver** [12:04:42]: And we will

**David Orban** [12:04:44]: see exactly who will handle the relationship.

**David Orban** [12:04:48]: Most likely it will be the new person.

**Matthew Oliver** [12:04:52]: I will be happy to be in

**David Orban** [12:04:55]: the loop.

**David Orban** [12:04:56]: And any decision that we will take regarding going ahead or not, having a pilot or not and whatever else is going to come Q2, but more likely Q3.

**Matthew Oliver** [12:05:11]: Okay, sure.

**David Orban** [12:05:15]: All right.

**David Orban** [12:05:17]: Any other question before I started mine?

**David Orban** [12:05:19]: No, not

**Matthew Oliver** [12:05:20]: at all.

**Matthew Oliver** [12:05:21]: Nice to meet you.

**Matthew Oliver** [12:05:22]: All right,

**David Orban** [12:05:23]: wonderful.

**David Orban** [12:05:24]: So what kind of... knowledge and coverage you have in the region in terms of regulatory coverage with ADGM, with ESCA on a UAE level.

**Matthew Oliver** [12:05:43]: Okay.

**Matthew Oliver** [12:05:43]: Have you had a

**David Orban** [12:05:45]: chance of setting things up for clients in the region?

**David Orban** [12:05:50]: Sure.

**Matthew Oliver** [12:05:52]: So worthwhile maybe going a tiny step back, and then I can help you with answering those questions.

**Matthew Oliver** [12:05:56]: So as you probably gathered, so from Vanta is really what we call a trust management tool to help manage compliance and security.

**Matthew Oliver** [12:06:04]: Now, what we've done is we've built out essentially native integrations across 400 different platforms that allow us to be able to extract the evidence required to manage and maintain frameworks.

**Matthew Oliver** [12:06:15]: Today, controls and policies that we have automated tests for from those integrations, allow us to map to 42 global frameworks out of the box.

**Matthew Oliver** [12:06:29]: Now those are like the sensor, but ISO, SOC2, NIST, PCI, GDPR, and everything else in between.

**Matthew Oliver** [12:06:39]: We have today about 15,000 clients.

**Matthew Oliver** [12:06:43]: I'm responsible for leading the go-to market with the Middle East.

**Matthew Oliver** [12:06:46]: I'm currently sat talking to you today from Dubai.

**Matthew Oliver** [12:06:48]: I spent four years living here.

**Matthew Oliver** [12:06:49]: I just recently moved back to London a few months back.

**Matthew Oliver** [12:06:52]: So I'm bouncing between backwards and forwards to the Middle East.

**Matthew Oliver** [12:06:56]: We have about 42 clients across the GCC today.

**Matthew Oliver** [12:07:00]: They range from investment authorities through to startup companies, through to late stage conversations with the likes of airlines, through to service providers, through to conglomerates.

**Matthew Oliver** [12:07:11]: Now, to answer your question in a more succinct way, local regulations, the likes of ADGM, the IFC, if needs be, as well.

**Matthew Oliver** [12:07:25]: We don't have those out of the box, but we have the ability to create what we call custom frameworks, which then can allow you to map controls against those specific frameworks by way of uploading the controls that you need and then we can make sure the system is managing those policies and managing

**Matthew Oliver** [12:07:42]: the tests if you like for those individual controls in order to get to a compliance ready state so the short answer is not out of the box no the short answer is the capability is there yes and it's something we can help you with now what we're seeing and I'm learning I've been working with some

**Matthew Oliver** [12:08:02]: CISOs and security leaders and folks just like yourself since starting with ANTA.

**Matthew Oliver** [12:08:07]: And really, my mandate is very simple.

**Matthew Oliver** [12:08:10]: I've given myself, listen, learn what the region needs.

**Matthew Oliver** [12:08:12]: And it seems like the general theme at the moment is that most organizations are leaning towards global frameworks because it's just the easiest way to start or maintain, or even moving away from a manual process that is maybe resource heavy to be able to then start to leverage automation for

**Matthew Oliver** [12:08:31]: compliance, a tool like us to be able to relieve that burden on what is typically with across different silos or even IT themselves.

**Matthew Oliver** [12:08:41]: So it feels like at the moment there's a number of reasons why people are changing.

**Matthew Oliver** [12:08:45]: I'm not necessarily concerned about ESCA and ADGM being something that you need, because it's something we can support you with.

**Matthew Oliver** [12:08:51]: It's all, I'm just very interested when I send a bit about the compliance today and how you're managing that.

**Matthew Oliver** [12:08:55]: And what, what, what, what, what, what is, what does that look like for you internally?

**Matthew Oliver** [12:09:00]: Cause it seems like obviously you, So

**David Orban** [12:09:02]: we are a Microsoft 365 Azure shop with E5 in particular and purview

**Matthew Oliver** [12:09:12]: setting policies or

**David Orban** [12:09:15]: reflecting the policies

**Matthew Oliver** [12:09:18]: and implementing the various

**David Orban** [12:09:21]: Chinese roles and access role- based access controls and so on, right?

**Matthew Oliver** [12:09:27]: And in that sense,

**David Orban** [12:09:30]: I would assume that your integration in the Microsoft world is deep, both with purview and try the in-tune.

**David Orban** [12:09:38]: And do you pull compliance signals from conditional access policies as well?

**David Orban** [12:09:45]: What we

**Matthew Oliver** [12:09:45]: do is we take... We take control data, metadata, settings data.

**Matthew Oliver** [12:09:52]: So that's, I mean, I need to check and see what we've mapped in terms of those particular products.

**Matthew Oliver** [12:09:57]: Give you a good example, Azure is a good example.

**Matthew Oliver** [12:10:00]: I probably can have

**David Orban** [12:10:02]: a quick check, but I think really what we're seeing at the moment

**Matthew Oliver** [12:10:04]: is that There's a number of integrations.

**Matthew Oliver** [12:10:07]: What I'd like to do, David, is actually spend a bit of time, not today, if that's okay, because I'm just keen to understand a bit more about what we're looking for, but we can take you through the platform.

**Matthew Oliver** [12:10:14]: And I'll give you, I think that'll ask a number of questions for you.

**Matthew Oliver** [12:10:18]: But I think, you know, that, and what we can do is we can spend some time in the integrations and show you the type of data and the depth data we're taking out.

**Matthew Oliver** [12:10:25]: And that's signaled by the tests that we're automating for you, basically a list of things that just don't need to be done manually.

**Matthew Oliver** [12:10:33]: Okay.

**David Orban** [12:10:34]: Now, we are a lean team and we want to use tools that make us efficient

**Matthew Oliver** [12:10:46]: and that in turn don't require

**David Orban** [12:10:49]: a lot of handholding and ongoing maintenance.

**David Orban** [12:10:57]: The little that you know currently, how would you estimate a realistic implementation and then a maintenance effort for someone like us?

**Matthew Oliver** [12:11:08]: So very quickly, our CEO built the system 10 years ago.

**Matthew Oliver** [12:11:13]: She was a Dropbox paper developer because she was actually asked as part of the product release to ship, and then the last minute asked to go and submit a SOC2 framework, and she had no idea what she was doing.

**Matthew Oliver** [12:11:23]: So her team had to drop tools, and she and the team... had to go manually gather the evidence.

**Matthew Oliver** [12:11:28]: So really, once they've worked out that most of it was around them in the tech stack that they were using day to day, they manually collected it, shipped the product and achieved SOC 2, but then she felt actually must be a better way.

**Matthew Oliver** [12:11:39]: And that's why Banta was born.

**Matthew Oliver** [12:11:41]: And the aim was to help scaling companies become self-sufficient by the nature of the depth of integrations we built.

**Matthew Oliver** [12:11:47]: If we can automate that evidence collection to either get to a framework for the first time, or automate through the integrations, essentially what is a manual GRC program today?

**Matthew Oliver** [12:11:58]: That is the key objective of our business, and that's where we've excelled in the last 10 years.

**Matthew Oliver** [12:12:03]: We aim to have our clients as self-sufficient as possible, but you have an abundance of support behind you in varying forms.

**Matthew Oliver** [12:12:11]: But the actual integrations are designed so they are essentially one click or two clicks at most.

**Matthew Oliver** [12:12:17]: So you click and connect, and once we connect, you then upload some of the policies that we need to if we haven't already automated those.

**Matthew Oliver** [12:12:23]: So let's just say, for example, you use SharePoint and your policy today are sat in SharePoint.

**Matthew Oliver** [12:12:27]: We will connect in SharePoint with mostly mainly read- only APIs.

**Matthew Oliver** [12:12:31]: We do have by direction if we need to, but mainly really only APIs.

**Matthew Oliver** [12:12:37]: And those individual integrations will read that data and of course start to map the controls against the frameworks that you're working towards.

**Matthew Oliver** [12:12:46]: If it's ISO, if it's in this case, ADGM, a custom framework that we can build, that becomes the North Star everything you do in terms of your security and your infrastructure setup.

**Matthew Oliver** [12:12:55]: And the system is designed to map and make suggestions on those areas of controls that are either out of step, out of beat, away from achieving or maintaining an AGGM regulation.

**Matthew Oliver** [12:13:07]: Yeah?

**David Orban** [12:13:07]: Okay.

**David Orban** [12:13:09]: So we are onboarding, obviously, multiple enterprise vendors and MSSP, ERP, and HRIS and whatever they are.

**Matthew Oliver** [12:13:24]: How can, if

**David Orban** [12:13:26]: Vanta can manage the vendor assessment, track SLA's met vendor risks to our own controls framework?

**David Orban** [12:13:38]: Yeah,

**Matthew Oliver** [12:13:38]: it's a really good question, David.

**Matthew Oliver** [12:13:39]: So in short, we can, and we can do it quite well.

**Matthew Oliver** [12:13:41]: I mean, the vendor risk and the ability in that Vanta has been designed for that very reason.

**Matthew Oliver** [12:13:46]: So once we've actually achieved the framework, we've spent the last five years developing that risk element of a platform as well, and that sits within vendor and third party risk.

**Matthew Oliver** [12:13:55]: So yes, you can set your own risk parameters and when it comes to vendors, we can start to almost collate thread assessments of those individual vendors as well, vulnerability tests as well against those vendors too.

**Matthew Oliver** [12:14:07]: So any particular critical vulnerability that might flag up, we can keep a close eye on those as well.

**David Orban** [12:14:12]: You are projecting a 90- day readiness.

**David Orban** [12:14:20]: Is that with the assumption that there is an existing ISMS in place or Vanta can help at the foundation stage and still maintain that launch window?

**David Orban** [12:14:35]: Yeah,

**Matthew Oliver** [12:14:35]: so good point.

**Matthew Oliver** [12:14:36]: So I think with your, let's say for Azure and, you know, I think you said Intra as well, and a few other technology products that you perhaps are using as well?

**Matthew Oliver** [12:14:46]: Are you using a task tracker like Jira or GitLab or do you know these?

**Matthew Oliver** [12:14:51]: Asana.

**David Orban** [12:14:52]: Asana, okay, great.

**David Orban** [12:14:53]: Okay, so all these are

**Matthew Oliver** [12:14:54]: native integrations.

**Matthew Oliver** [12:14:55]: So what we would do is we connect into those and collate, essentially what we find is, let's pretend, for example, we're going for ISO 27001. Just keep it super simple for the moment.

**Matthew Oliver** [12:15:03]: What we do is that ISO 27001 example I gave you that 90 days is probably relatively quite conservative and it means that we connect you and assemble all the evidence out of the box directly from those integrations straight away and then we see and give you from pretty much the day one a map of how

**Matthew Oliver** [12:15:22]: of a percentage of how close you are to being ready for that individual framework so there could be for example some policies that are missing all the policies that we picked up maybe need to be slightly reworded or maybe updated to meet the regulations for this particular framework that are working

**Matthew Oliver** [12:15:36]: towards.

**Matthew Oliver** [12:15:37]: It could be that there's perhaps controls that they're missing or just haven't been carried out.

**Matthew Oliver** [12:15:40]: Maybe we need to create some custom controls because you've got a very unique setup in certain area.

**Matthew Oliver** [12:15:45]: Maybe you've got perhaps a couple of entities that we need to keep a close eye on, maybe there's a, whatever it might be.

**Matthew Oliver** [12:15:51]: The idea is that there is probably a teeny bit of a gap that we work, but what we do is we'd show you in the platform exactly what is that 20% delta, exactly what controls, policies, whatever it might be, that needs to be changed, and we'll walk you through in the platform how to update those in

**Matthew Oliver** [12:16:07]: line with that North Star being ISO or ADGM.

**Matthew Oliver** [12:16:11]: And

**David Orban** [12:16:12]: your pricing model is based on a per user and per connector or just one or just the other.

**Matthew Oliver** [12:16:20]: No, it's actually on headcount, David.

**Matthew Oliver** [12:16:21]: So it's actually headcount in scope.

**Matthew Oliver** [12:16:23]: So let's just say you had 100 people in the business.

**Matthew Oliver** [12:16:25]: But actually, let's say, Only, let's say, 80 of those are relevant to the framework that you're working towards.

**Matthew Oliver** [12:16:30]: In this case, they're regulated by ADGM.

**Matthew Oliver** [12:16:32]: Their work, their roles are regulated by ADGM.

**Matthew Oliver** [12:16:35]: Then 80 will be in scope, and we would price based on that bracket.

**Matthew Oliver** [12:16:38]: It's not a headcount.

**Matthew Oliver** [12:16:39]: So you can have a number of users, doesn't matter, but it's more about the headcount in scope.

**Matthew Oliver** [12:16:44]: That's how we price it to keep it fair.

**Matthew Oliver** [12:16:46]: Yeah.

**David Orban** [12:16:48]: And you have bands of prices?

**David Orban** [12:16:51]: We do.

**Matthew Oliver** [12:16:53]: We do.

**Matthew Oliver** [12:16:54]: So it's an annual subscription price.

**Matthew Oliver** [12:16:56]: There's no setup cost.

**Matthew Oliver** [12:16:57]: It's all just one license, David.

**Matthew Oliver** [12:16:59]: And then what we do is we have tiers, essentially, one's called essentials, which is typically those that are starting out.

**Matthew Oliver** [12:17:05]: So think tech startups, for example, or those that are maybe I've got a handful of employees that need to get compliant because the customer is requiring it, for example.

**Matthew Oliver** [12:17:14]: So they're starting out.

**Matthew Oliver** [12:17:15]: Then we have what's called plus, which is those that are got a framework.

**Matthew Oliver** [12:17:18]: There's an established business there.

**Matthew Oliver** [12:17:20]: Maybe there's a couple of frameworks they've got already in place.

**Matthew Oliver** [12:17:22]: They need to maintain it.

**Matthew Oliver** [12:17:23]: There's stress on the teams in terms of pressure on workload, but they're still very much in growth mode.

**Matthew Oliver** [12:17:29]: Then there's those organizations that I like to call, they're pretty much running in regulatory environments.

**Matthew Oliver** [12:17:34]: That's professional.

**Matthew Oliver** [12:17:36]: And there's a number of things we can do.

**Matthew Oliver** [12:17:37]: That's where the more the risk comes in.

**Matthew Oliver** [12:17:40]: So professional always kind of includes the risk element behind that.

**Matthew Oliver** [12:17:43]: So when you're talking about third party vendor risk management as an example, that typically sits within what we call the professional tier.

**Matthew Oliver** [12:17:50]: Good examples would be with the professional is that the ability to be able to maintain those companies, in those, in this case, the regulated industries you're working in, you may have, you may send out high, quite in dense, quite comprehensive security questionnaires to your vendors.

**Matthew Oliver** [12:18:11]: Equally from your clients, they may send questionnaires back to you.

**Matthew Oliver** [12:18:14]: So that's also a resource in the business that we take away and automate that risk, the completion for, because obviously the integrations we've got, all the data is basically built within the integration.

**Matthew Oliver** [12:18:24]: So we work with that.

**Matthew Oliver** [12:18:25]: So that's something we can do.

**Matthew Oliver** [12:18:26]: And that tends to come out of the professional package.

**Matthew Oliver** [12:18:29]: The tier beyond that, David, is Enterprise, where we can start building some, get a bit creative with the GRCP around.

**Matthew Oliver** [12:18:34]: So

**David Orban** [12:18:35]: assuming that professional is enough at least to start and we don't have

**Matthew Oliver** [12:18:38]: needs that we cannot

**David Orban** [12:18:42]: implement using your tools and we don't require you to come in and do something specific.

**David Orban** [12:18:50]: What are we talking about?

**David Orban** [12:18:52]: What is the price?

**David Orban** [12:18:54]: I need

**Matthew Oliver** [12:18:54]: to just do a quick check.

**Matthew Oliver** [12:18:55]: Remind me of the head count you've got in scope from what I've just given

**David Orban** [12:18:58]: you, David.

**David Orban** [12:19:01]: So we are currently 68 people growing rapidly hiring two, three people per week almost.

**David Orban** [12:19:10]: But out of those, probably just to make a rough estimation, half of them are regulated and half of them are non-regulated.

**David Orban** [12:19:22]: Okay,

**Matthew Oliver** [12:19:23]: so we'll say maybe up to 40, 50, for example, in time or regularly, so that's fine.

**Matthew Oliver** [12:19:29]: If I'm honest with you, I need to circle back.

**Matthew Oliver** [12:19:30]: I don't have it off the top of my head.

**Matthew Oliver** [12:19:32]: No

**David Orban** [12:19:32]: problem.

**David Orban** [12:19:33]: Because we have sort of, I think

**Matthew Oliver** [12:19:35]: there's like 21 to 50, and I want to think, and I just need to make sure that if professional is needed, and maybe there's something I forget, and I'm only two months into the company, so you have to do forgive me on that side.

**Matthew Oliver** [12:19:45]: But I wanted to check to see risk is included in plus, because if it is, then we can think about starting point from you and then we can scale and it's obviously a bit cheaper for you as well.

**Matthew Oliver** [12:19:55]: Okay.

**Matthew Oliver** [12:19:55]: And then we can think about then what that could be from that.

**Matthew Oliver** [12:19:59]: So if you don't mind, I can float some initial cost over to you by email if that would work for you.

**Matthew Oliver** [12:20:02]: Is that okay?

**David Orban** [12:20:03]: So I will follow our meeting with an email based on what we discussed and either

**Matthew Oliver** [12:20:09]: remaining questions or things like that, and then

**David Orban** [12:20:11]: you can respond to that.

**David Orban** [12:20:14]: Of course.

**David Orban** [12:20:15]: And my last few questions, since

**Matthew Oliver** [12:20:19]: we scheduled this for half an hour,

**David Orban** [12:20:23]: you mentioned European auditors.

**David Orban** [12:20:27]: Do you have audit partners in the region as well?

**David Orban** [12:20:32]: No,

**Matthew Oliver** [12:20:32]: well, we have connect, we have, so the short answer is established, we have established partners, yes, that have experienced in the region.

**Matthew Oliver** [12:20:43]: Are they got offices in the region?

**Matthew Oliver** [12:20:45]: No, we've got clients that we've supported on audit partners that we work with to date.

**Matthew Oliver** [12:20:51]: So I'll give you an example, we work with the likes of Prescient and A-Line is a good example.

**David Orban** [12:20:55]: Those organizations are global, I

**Matthew Oliver** [12:20:58]: think they're HQ out of the US as well.

**Matthew Oliver** [12:21:00]: They, we over the years have worked very closely with the likes of the BSI and also the audit partner network from that has naturally grown and been organic because a lot of our R&D is working with audit community to make sure that what we're doing is obviously audit friendly and also more

**Matthew Oliver** [12:21:18]: importantly gets the audit process down as much as possible so our partners are very carefully set because they know the platform we're on board them with the platform so If a regional audit partner is needed for you, then we can certainly reach out and start having some conversations.

**Matthew Oliver** [12:21:34]: But if you've already got one in mind that you work with today, we'll happily work with them, isn't it?

**Matthew Oliver** [12:21:39]: Really, without talking, because I can show you when we meet again, there is essentially what I learned I call it the audit model, it's part of the platform, but it's an audit feature where when you are for nature of the business, nature of the product and how it's designed, The integrations are

**Matthew Oliver** [12:21:55]: built, we collect the evidence, you ready everything through maybe creation of the controls and policies we talked about.

**Matthew Oliver** [12:22:03]: And then once you're ready, you're 100% ready for that regulation, that framework, whatever it is that you're working towards, the auditor essentially self-serves from the platform.

**Matthew Oliver** [12:22:11]: You do it within the platform.

**Matthew Oliver** [12:22:13]: So it means that it reduces the need for them to actually be in the offices for weeks and weeks on end for drawn months and months of audit processes.

**Matthew Oliver** [12:22:19]: It can be reduced to hours in time in terms of contact time, but actually what you're then doing is you're landing just a self-server in the platform and then they can communicate with you.

**Matthew Oliver** [12:22:28]: This policy needs to be updated because this regulation in ADGM has certainly changed.

**David Orban** [12:22:33]: And the data itself is stored where?

**David Orban** [12:22:36]: Do you have data residency?

**David Orban** [12:22:38]: That's what we

**Matthew Oliver** [12:22:38]: want to talk No, we don't.

**Matthew Oliver** [12:22:40]: So in full transparency today, it's something that's coming up regularly.

**Matthew Oliver** [12:22:45]: So I'm very acutely aware of this.

**Matthew Oliver** [12:22:46]: So we obviously got clients in Saudi.

**Matthew Oliver** [12:22:48]: We got clients in UAE.

**Matthew Oliver** [12:22:49]: I've got the data today's stored in Germany.

**Matthew Oliver** [12:22:53]: Okay.

**Matthew Oliver** [12:22:54]: But

**David Orban** [12:22:54]: what I wanted to, and when we start peeling pack

**Matthew Oliver** [12:22:57]: the need and the concern, it links to usually two things.

**Matthew Oliver** [12:23:01]: One is that it sits within a mandate that the business is choosing to follow, because personal data is obviously a big no when it comes in terms of leaving the kingdom or leaving in this case, the region.

**Matthew Oliver** [12:23:14]: What we're seeing at the moment is that what we do is we take control data.

**Matthew Oliver** [12:23:17]: It's essentially metadata, it's not personal.

**Matthew Oliver** [12:23:19]: So it's nothing to do with David or Matthew.

**Matthew Oliver** [12:23:21]: Yeah.

**David Orban** [12:23:22]: It's the metadata behind the scene.

**David Orban** [12:23:23]: So that's what we're

**Matthew Oliver** [12:23:23]: taking.

**Matthew Oliver** [12:23:24]: So when you get into it, it's actually something that is not causing too much of an issue.

**Matthew Oliver** [12:23:29]: Yeah,

**David Orban** [12:23:29]: but yeah, that's right.

**David Orban** [12:23:30]: But if you're working, let's say with Saudi

**Matthew Oliver** [12:23:32]: and you've got a couple of ministries or piff back businesses or even perhaps businesses that are requiring you to move towards a summer regulation, then naturally the NCA, which is obviously the Cybersecurity Association controls around data kicks in and of course that's so hard now, right?

**Matthew Oliver** [12:23:46]: It's a gray.

**David Orban** [12:23:46]: Yeah.

**David Orban** [12:23:47]: So there's, there's, as long as

**Matthew Oliver** [12:23:49]: the business is able to defend, if called upon by the authorities to say, you've got this data, where is it stored?

**Matthew Oliver** [12:23:56]: and it's not personal to linking back, we can talk about that.

**Matthew Oliver** [12:23:59]: So I know you're regulated, but I just want to be transparent with you.

**Matthew Oliver** [12:24:02]: It's not in the UAE.

**Matthew Oliver** [12:24:03]: I've actually had a lot of enterprise organizations in this region say, okay, well, look, if we were to work with you, could you commit to putting something in the, because we're AWS, there's one in UAE.

**Matthew Oliver** [12:24:14]: Obviously, AWS in Saudi is going live, I think, July.

**Matthew Oliver** [12:24:17]: So technically it's very doable, but it's just a prioritization from the board in the US.

**David Orban** [12:24:23]: So I can't commit to that today, unfortunately, sir, but I

**Matthew Oliver** [12:24:25]: can say that the right people are aware of And as we scale the region and scale the business, then, of course, it becomes an easy conversation.

**David Orban** [12:24:33]: Okay.

**David Orban** [12:24:35]: And the last one you mentioned AI.

**David Orban** [12:24:39]: What is it besides a great buzzword today?

**David Orban** [12:24:44]: Is it generating policy drafts?

**David Orban** [12:24:46]: Is it automating evidence collection besides and beyond what previous generation of tools that you built were already doing.

**David Orban** [12:24:55]: What does it consist of?

**David Orban** [12:24:58]: Yeah,

**Matthew Oliver** [12:24:58]: of course.

**Matthew Oliver** [12:24:59]: Another solid question.

**Matthew Oliver** [12:25:00]: I think what we do is, the nature of what we do is the depth of integrations we're pulling out that data at source and quite possibly the first time in one place.

**Matthew Oliver** [12:25:13]: So the AI is more generative.

**Matthew Oliver** [12:25:14]: So a good use case would be you are uploading your policies for the first time.

**Matthew Oliver** [12:25:19]: The North Star in this case is going to be, let's say, ADGM, we've mapped the controls, the tests to those individual framework, in this case, ADGM.

**Matthew Oliver** [12:25:30]: We now, the system now knows that ADGM is the guy, is the goal.

**Matthew Oliver** [12:25:34]: We want to make sure that everything's aligning to ADGM.

**Matthew Oliver** [12:25:37]: What will happen is the We'll look at those controls and then start to look at the policies and sweep to see any gaps in those policies, anything that needs to be amended or suggested.

**Matthew Oliver** [12:25:50]: Okay, that's one use case.

**Matthew Oliver** [12:25:51]: And again, it's probably easy to just show you when we speak again.

**Matthew Oliver** [12:25:54]: The second use

**David Orban** [12:25:55]: case.

**David Orban** [12:25:55]: And yes, sorry, please.

**David Orban** [12:25:57]: No, it's just going to say

**Matthew Oliver** [12:25:58]: a second use case, which is really powerful for our clients.

**Matthew Oliver** [12:26:00]: is that can be done also on bulk so you can sweep all the documents, and that doesn't have to be policies, it can be any documents you like.

**Matthew Oliver** [12:26:06]: You can upload just a, you can do it, you know, run a document on a train, upload it, and what am I missing situation, and it will just tell you.

**David Orban** [12:26:14]: The other element is when you're

**Matthew Oliver** [12:26:17]: putting in the good work, let's just say you're moving to, know, SOC 2 or ISO as an example, just to keep it simple again, The ISO 27001, the framework that you've done, so let's say we're out of the box, all the controls are in place, you're 90% ready, there is 10% of maybe some updates you need to

**Matthew Oliver** [12:26:32]: make, documents, whatever it might be.

**Matthew Oliver** [12:26:35]: Once you've done the groundwork for that in terms of the automation for that particular framework, What we then do is we can use AI to then read all the policies that you've got and map across other frameworks.

**Matthew Oliver** [12:26:48]: We've got about 42 across out of the box to see how far off you are from those.

**Matthew Oliver** [12:26:52]: And it's basically a table.

**Matthew Oliver** [12:26:53]: So you can see you're 85% away from SOC.

**Matthew Oliver** [12:26:58]: You may be wanting to go to more GDPR.

**Matthew Oliver** [12:27:01]: So it could be that you're 85% away from GDPR, that kind of thing.

**Matthew Oliver** [12:27:05]: And so it maps it that way.

**Matthew Oliver** [12:27:07]: And

**David Orban** [12:27:08]: do you have APIs for systems to be able to control Vanta itself rather than people clicking around?

**David Orban** [12:27:17]: Do you have MCP AI to AI connectors and things like that?

**David Orban** [12:27:24]: I think

**Matthew Oliver** [12:27:24]: because obviously the nature of what we do, the AI won't replicate or change anything within the platform or do so in your policies as well.

**Matthew Oliver** [12:27:31]: It's more of, I'd need to probably show you.

**Matthew Oliver** [12:27:34]: I'm going to take a note of that question and give you some more of a structured answer for that because I think,

**David Orban** [12:27:41]: because when it comes to AI to AI, we're not, we've had

**Matthew Oliver** [12:27:44]: that a couple of times now.

**Matthew Oliver** [12:27:45]: I think the general rule of thumb is that we don't tend to allow AI to change anything in it, if that makes sense, or communicate.

**Matthew Oliver** [12:27:51]: And the question was specifically asked by

**David Orban** [12:27:53]: agents.

**David Orban** [12:27:53]: Yeah, that's right.

**David Orban** [12:27:55]: So whether they only have read permissions,

**Matthew Oliver** [12:28:00]: it can still be useful

**David Orban** [12:28:04]: be able and interact with your platform rather than directly through the intermediation of an AI agent, right?

**Matthew Oliver** [12:28:14]: Correct.

**Matthew Oliver** [12:28:15]: And it is

**David Orban** [12:28:15]: okay to come back on that as well or say, you know, it's on the roadmap or whatever it is.

**Matthew Oliver** [12:28:23]: Okay, so thank you.

**Matthew Oliver** [12:28:25]: And

**David Orban** [12:28:27]: I will send you a recap email of what we discussed and the outstanding questions.

**David Orban** [12:28:34]: And we will take it from there, as well as the person coming in and taking on the role potentially will be in touch, as I said, after end of March.

**Matthew Oliver** [12:28:51]: Okay, perfect.

**Matthew Oliver** [12:28:52]: Well, I mean, you let me know when you'd like to spend some time having a look at the products, and then we can work around you.

**Matthew Oliver** [12:28:57]: That's no problem.

**Matthew Oliver** [12:28:58]: Yeah.

**Matthew Oliver** [12:28:58]: Of

**David Orban** [12:28:58]: course.

**David Orban** [12:28:59]: All right.

**David Orban** [12:29:00]: Thank you.

**David Orban** [12:29:00]: Thank Nice to meet, David.

**Matthew Oliver** [12:29:01]: Thanks so much for your time.

**Matthew Oliver** [12:29:02]: See you soon.

**Matthew Oliver** [12:29:02]: You too.

**Matthew Oliver** [12:29:03]: Bye-bye.

**Matthew Oliver** [12:29:04]: Bye-bye.

**Matthew Oliver** [12:29:05]: The recording has stopped.

---
*Backed up from MeetGeek on 2026-03-30 08:42*
