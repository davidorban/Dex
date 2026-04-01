# AI Tools, Dashboard & Advisory Planning

**Date:** 2025-11-28
**Duration:** Unknown
**Meeting ID:** 8d64b4b4-4fb0-49b1-a511-be0776787fba

## Participants
- *Participants not listed*

### Summary

The meeting focused on standing up AliOne Labs as a sandbox for AI experiments, a rapid demo of a populated advisory dashboard, and operationalizing data and tooling across advisory work. Attendees discussed securing client permissions to use testimonials, integrating real invoicing and pipeline systems into the dashboard, and providing team access for review. The group agreed on using synthetic/redacted data to avoid compliance issues, exploring AI to quantify pipeline progress, and collecting anonymous team input on AI tools. David demonstrated AI-generated visual media tools and shared access instructions; follow-ups include granting dashboard credentials, pitch-book ownership adjustments, and further tool recommendations via the AI channel.

## Full Transcript

**Unknown speaker** [12:29:47]: Well,

**Unknown speaker** [12:30:52]: Hello.

**Samuel Tregeagle** [12:30:53]: Mr. David, how are you?

**Samuel Tregeagle** [12:30:56]: Hello, I am very well and you.

**Samuel Tregeagle** [12:31:00]: I'm good.

**Samuel Tregeagle** [12:31:01]: I'm really looking forward to this weekend.

**Samuel Tregeagle** [12:31:05]: It's just what I needed, honestly.

**Samuel Tregeagle** [12:31:09]: Well, that's great news.

**Unknown Speaker** [12:31:11]: Any week you need the weekend, you will always have it.

**Samuel Tregeagle** [12:31:15]: Oh, this one is special because it's UIA National Day on Monday and Tuesday.

**Samuel Tregeagle** [12:31:21]: Oh, so for the weekend.

**Samuel Tregeagle** [12:31:23]: Yeah, correct.

**Samuel Tregeagle** [12:31:25]: So, very happy.

**Samuel Tregeagle** [12:31:27]: That means I can really sit down and knuckle this out because it's just been a client thing after client thing this week.

**Samuel Tregeagle** [12:31:34]: It's really, really taken up the priorities.

**Samuel Tregeagle** [12:31:36]: But I managed to get the internship plan.

**Samuel Tregeagle** [12:31:39]: Yeah.

**Samuel Tregeagle** [12:31:40]: And I have bad news

**Unknown Speaker** [12:31:42]: for you.

**Unknown Speaker** [12:31:42]: Randy told me.

**Unknown Speaker** [12:31:46]: that in 2026 he plans to have zero clients at no time.

**Unknown Speaker** [12:31:52]: There will be no moment when Randy wants to have zero clients.

**Unknown Speaker** [12:31:57]: So sorry, Samuel, but.

**Unknown Speaker** [12:32:01]: Damn it.

**Unknown Speaker** [12:32:01]: And I was really hoping next year would be

**Samuel Tregeagle** [12:32:02]: the year we finally got rid of all.

**Samuel Tregeagle** [12:32:09]: Yeah, but I mean, it's good.

**Samuel Tregeagle** [12:32:10]: We've had some really good feedback this week.

**Samuel Tregeagle** [12:32:13]: Randy, you missed a bit on poll.

**Samuel Tregeagle** [12:32:15]: I was pretty glowing about us as well to night, which was quite nice.

**Randy Boyer** [12:32:21]: Very nice.

**Randy Boyer** [12:32:22]: Got to tell me a little

**Samuel Tregeagle** [12:32:26]: bit later, yeah.

**Samuel Tregeagle** [12:32:27]: That'd be great.

**Samuel Tregeagle** [12:32:27]: Yeah, yeah.

**Samuel Tregeagle** [12:32:28]: We'll have a little check-in about that afterwards.

**Samuel Tregeagle** [12:32:32]: And it will be

**Unknown Speaker** [12:32:36]: hopefully still possible, and it would be quite important to not only capture that praise, but then immediately ask the client, is it okay if we quote you on that, is it okay if we put you on the website as a testimonial, right?

**Unknown Speaker** [12:32:53]: Now, obviously, depending on the stage and the confidentiality and whatever else, but it is always good to immediately take advantage of those who are happy and maybe would be even pleased that we want to feature them.

**Unknown Speaker** [12:33:12]: Yeah, and

**Randy Boyer** [12:33:13]: as we'll go into more detail with Samuel a little bit later, but this particular client, we've, you know, we've hit the bullseye on virtually everything that we've done for them, including even helping them with their business, not just in packaging them and and helping in figuring out how to pitch,

**Randy Boyer** [12:33:36]: you know, figuring helping them pitch and training them how to do a pitch and everything that we know we actually have some traction in one of the key markets that they've had trouble.

**Randy Boyer** [12:33:47]: We've helped them.

**Randy Boyer** [12:33:48]: So we should in the next couple weeks or so get this, this permission from both Paul and from Andrew about potentially using some of these things for marketing purposes.

**Randy Boyer** [12:34:06]: Yeah, definitely.

**Randy Boyer** [12:34:08]: Very good.

**Randy Boyer** [12:34:09]: Definitely.

**Randy Boyer** [12:34:10]: So

**Unknown Speaker** [12:34:12]: I don't remember last week when we spoke if I mentioned Aldi1 Labs to you guys?

**Unknown Speaker** [12:34:19]: No, I don't think so.

**Unknown Speaker** [12:34:21]: Okay.

**Unknown Speaker** [12:34:24]: So I always come up with new shit, right?

**Unknown Speaker** [12:34:27]: And...

**Randy Boyer** [12:34:30]: You're David Orban, we expect these things every time we talk to you.

**Unknown Speaker** [12:34:35]: So, so, Alivan Labs is not a new division, it is not a new entity, it is a sandbox, and it is a place where we experiment with tools that have not yet been adopted as standard with the knowledge that the experiments are not touching regulated entities, client confidential data, and there will be no

**Unknown Speaker** [12:35:06]: compliance issues around it.

**Unknown Speaker** [12:35:09]: And as a consequence, it must necessarily live on a different domain, on a different tenant, so that we use the same architecture that we have under Ali1.com.

**Unknown Speaker** [12:35:25]: But we can, with the knowledge that everything is going to be fine.

**Unknown Speaker** [12:35:33]: And then when we come to certain conclusions, make the recommendation that whatever the tool is that we experimented with, should be adopted company-wide.

**Unknown Speaker** [12:35:46]: So I registered the AliOne Labs.com.

**Unknown Speaker** [12:35:50]: And whoever will want to be part of these experiments, that is where we will do them, rather than under Oli1.com itself.

**Unknown Speaker** [12:36:03]: And so

**Randy Boyer** [12:36:03]: to meet your criteria, it either has to be something that we're doing internally that's not with the client, or it has to be with advisory because we're the only group that actually does unregulated work.

**Randy Boyer** [12:36:19]: Yes, and

**Unknown Speaker** [12:36:25]: when we want to experiment with other divisions, we will just generate synthetic data.

**Unknown Speaker** [12:36:34]: So we will have processes to redact data and to names and any identifiable information and numbers with others, or to start from scratch and imagine a wealthy family and their allocations and then, you know, whatever, depending on or an investment banking deal, whatever it is going to be.

**Unknown Speaker** [12:37:15]: Yes, this is necessary.

**Unknown Speaker** [12:37:20]: Why?

**Unknown Speaker** [12:37:21]: Because she then asked me to provide her the list of tools that we want to use, and then in 2027 she would reconsider how to change them.

**Unknown Speaker** [12:37:37]: And I am a grown-up man, but I cry to the thought.

**Randy Boyer** [12:37:45]: of having to... Wait two years.

**Randy Boyer** [12:37:50]: Having to stop

**Unknown Speaker** [12:37:54]: learning about what is going on in the world for that long.

**Unknown Speaker** [12:37:59]: So we still have to agree on what will be a reasonable revision because she said, well, that is what she's accustomed to in the European banks and entities she worked with.

**Unknown Speaker** [12:38:13]: And I couldn't stop myself telling her European innovation is not a lighting rod that everyone looks to in understanding how to become a financial or technology leader.

**Unknown Speaker** [12:38:34]: And

**Randy Boyer** [12:38:35]: also in AI, things are happening every week.

**Randy Boyer** [12:38:39]: Exactly.

**Randy Boyer** [12:38:41]: Yeah.

**Unknown Speaker** [12:38:42]: Now, one thing that is quite lucky is that the expression, the jagged edges of AI capabilities that is becoming adopted so that it extends in unexpected directions is actually covering an ever expanding area that

**Unknown Speaker** [12:39:13]: implies that if you do leading edge mathematical research, then yes, you need the state of the art engine.

**Unknown Speaker** [12:39:28]: But if you do, I don't know, compliance checking of something that is very well understood, then definitely what used to be state of the art six months ago, And now kind of a run of the mill is enough.

**Unknown Speaker** [12:39:48]: So if we shudder to the thought of having to only use Microsoft co-pilot rather than being able to use open AI or cloud or whatever else.

**Unknown Speaker** [12:40:07]: I believe that Microsoft Copilot will be just fine for 90% of what we need.

**Unknown Speaker** [12:40:15]: Exactly because how fast they are evolving.

**Unknown Speaker** [12:40:19]: Anyway, we will see.

**Unknown Speaker** [12:40:21]: Now, the second line in my notes on Slack is that I suggested and Chidim agreed that we should also hear from all of our team.

**Unknown Speaker** [12:40:36]: What are the tools that everyone is already using, regardless of whether it has been sanctioned and approved and it is just something that they find useful.

**Unknown Speaker** [12:40:51]: Not only what brand and what version and whether it is paid or free, but also what features.

**Unknown Speaker** [12:40:59]: Like Michael said that he finds fixer often useful and then he may not take on the draft that the tool wrote for his emails but still reading that helps right and and any other function including meet geek for for note taking and so on so i will be designing and sending out that that survey it will

**Unknown Speaker** [12:41:29]: be anonymous so everyone can spill their beans and then the dashboard, which last week I said I would create and I did.

**Unknown Speaker** [12:41:44]: Now, just FYI, what I started with is to create a plan for the creation of the dashboard.

**Unknown Speaker** [12:41:58]: And the plan very naturally included time and resources as if they were human coded okay so it is a hundred thousand dollars and twelve weeks all right how long did it take me to do it

**Unknown Speaker** [12:42:26]: come on just say a number of hours or days or weeks It doesn't matter, there's no wrong answer.

**Unknown Speaker** [12:42:35]: That's

**Samuel Tregeagle** [12:42:35]: got to be less than a week, right?

**Samuel Tregeagle** [12:42:37]: Yes, it is less than a week.

**Samuel Tregeagle** [12:42:38]: It

**Unknown Speaker** [12:42:38]: took me an hour.

**Unknown Speaker** [12:42:41]: Excellent.

**Unknown Speaker** [12:42:43]: So what you see is what would have been 12 weeks work of a team, not just one person, a designer, a project manager, a front-end developer, a back-end developer, is a typical set of people working on different aspects of something like this.

**Unknown Speaker** [12:43:06]: So it took me an hour.

**Unknown Speaker** [12:43:09]: And it is ready to be interfacing real data sources, because right now the numbers are invented.

**Unknown Speaker** [12:43:19]: They are based on the business plan that you shared Randy.

**Unknown Speaker** [12:43:24]: So they are not out of thin air.

**Unknown Speaker** [12:43:30]: but they are not real time.

**Unknown Speaker** [12:43:32]: So this will then interface zero for invoicing, pipe drive for the pipeline and whatever else.

**Unknown Speaker** [12:43:44]: So this is the dashboard itself and then there are detailed pages for everything.

**Unknown Speaker** [12:43:54]: What is the progress towards finding retainer revenue?

**Unknown Speaker** [12:44:00]: And it is possible to edit it and change the data.

**Unknown Speaker** [12:44:11]: What is orbit startup partnership, blah, blah, blah.

**Unknown Speaker** [12:44:18]: Just to be

**Randy Boyer** [12:44:18]: clear for Anna and Samuel, the real is The business plan information from my business plan, but the actuals are not actuals.

**Randy Boyer** [12:44:30]: Yes.

**Randy Boyer** [12:44:31]: Yes, absolutely.

**Randy Boyer** [12:44:33]: Yeah, yeah.

**Unknown Speaker** [12:44:34]: So, here's another page, pipeline funnel by stage.

**Unknown Speaker** [12:44:42]: Here, the names.

**Unknown Speaker** [12:44:44]: the invented names of the clients and the deals, you can sort them by probability.

**Unknown Speaker** [12:44:51]: This is weighted probability, so whatever is the absolute number is multiplied by the percentage and so on.

**Unknown Speaker** [12:45:01]: How many clients, I don't even know what this is, because I specify up to a point, but it is, more realistic to to say that I'm the orchestrator or whatever other label we want to use.

**Unknown Speaker** [12:45:24]: Conductor, yeah.

**Unknown Speaker** [12:45:25]: Conductor.

**Unknown Speaker** [12:45:26]: And then when it comes up with something, I would have to ask, and I was too lazy to ask.

**Randy Boyer** [12:45:35]: No, totally, you want to make sense, because we actually are collecting equity, and so we, you The common way to express it is assets under management.

**Randy Boyer** [12:45:47]: Perfect.

**Randy Boyer** [12:45:48]: Okay.

**Randy Boyer** [12:45:49]: Now, here is

**Unknown Speaker** [12:45:50]: an

**Samuel Tregeagle** [12:45:50]: interesting... Sorry, are we collecting equity under advisory as well, or just the regulated IB stuff?

**Samuel Tregeagle** [12:45:56]: No, under advisory.

**Randy Boyer** [12:45:58]: I can give you two examples.

**Randy Boyer** [12:46:00]: In FOMO, we already have some, and then with Mirai valves, we're expecting to get it.

**Randy Boyer** [12:46:11]: Okay, cool.

**Samuel Tregeagle** [12:46:12]: Sorry to interrupt.

**Samuel Tregeagle** [12:46:14]: No, no, that's okay.

**Samuel Tregeagle** [12:46:15]: Absolutely.

**Unknown Speaker** [12:46:17]: Now, this is interesting because I myself have absolutely no idea what it even means to be compliant.

**Unknown Speaker** [12:46:28]: And when the auditor comes, how badly we freak out and then what does it even mean?

**Unknown Speaker** [12:46:37]: So all of this is for me a learning opportunity too.

**Unknown Speaker** [12:46:43]: And as you can see, there are things like annual KYC.

**Unknown Speaker** [12:46:51]: All right.

**Unknown Speaker** [12:46:54]: Verify beneficial ownership structure, data protection audit.

**Unknown Speaker** [12:47:00]: So very, very interesting things.

**Unknown Speaker** [12:47:04]: Pending, completed in progress, etc.

**Unknown Speaker** [12:47:09]: Right?

**Ana Capuder** [12:47:11]: Can I ask where this?

**Ana Capuder** [12:47:13]: tasks came from?

**Ana Capuder** [12:47:15]: Like where, what is this related to?

**Samuel Tregeagle** [12:47:18]: This is the new, this is the H1 for 2026 priorities, you just haven't seen them yet.

**Samuel Tregeagle** [12:47:23]: So take note of all these tasks, they're going to be on your desk pretty soon.

**Samuel Tregeagle** [12:47:28]: Uh-huh.

**Samuel Tregeagle** [12:47:29]: Annual data protection audits, it's interesting.

**Samuel Tregeagle** [12:47:35]: Whether they will or

**Unknown Speaker** [12:47:36]: will not, these come, so condescendingly, one, could label these the AI hallucinations.

**Unknown Speaker** [12:47:49]: But in this case, they are not because they are absolutely reasonable, but they have been completely invented by the AI in order to populate the page, right?

**Unknown Speaker** [12:48:03]: So 10 minutes after starting, the dashboard was full and the other pages were empty.

**Unknown Speaker** [12:48:12]: And so I just told the AI filled the page.

**Unknown Speaker** [12:48:17]: Now, it knew what it was talking about because it had a huge amount of context due to the fact that I think last week I told you that I am creating or I have created a digital twin of Ali 1 group.

**Unknown Speaker** [12:48:39]: So I have a model for every division, every role, every type of engagement, and that is why I can instruct the AI to do things that have hopefully resemblance to reality.

**Unknown Speaker** [12:49:01]: And the advantage is also that with a model that is improving, again, hopefully with additional data, we can then stress tested we can see what we want to maximize for example rather than maximizing short-term profit we want to maximize long-term upside in our partnership value model and and if we

**Unknown Speaker** [12:49:32]: have a rich understanding of how the different pieces fit together then we can easily do that Okay, and the last one is the team.

**Unknown Speaker** [12:49:46]: According to the data, Hela is part of advisory, but... Yes, she is.

**Randy Boyer** [12:49:52]: Oh, she is.

**Randy Boyer** [12:49:53]: That is true.

**Randy Boyer** [12:49:54]: That is true.

**Randy Boyer** [12:49:55]: Perfect.

**Randy Boyer** [12:49:56]: What?

**Randy Boyer** [12:49:56]: He's just been seconded to working on things related to Saudi, but she is technically advisory.

**Randy Boyer** [12:50:06]: Okay, perfect.

**Randy Boyer** [12:50:08]: And of course

**Unknown Speaker** [12:50:09]: anything that is incorrect here we can and will correct and I will be creating with the huge investment of other virtual hundreds of thousands of hours and months and months of effort in reality an hour of fun, the dashboards for the other divisions as well.

**Unknown Speaker** [12:50:36]: Okay, now each of you have your own access and the URL will be advisory.alibonlabs.com.

**Unknown Speaker** [12:50:49]: You have your username and password.

**Unknown Speaker** [12:50:53]: And some things are not functional yet, so you click here and nothing happens.

**Unknown Speaker** [12:51:01]: or here, don't worry.

**Unknown Speaker** [12:51:03]: That's fine.

**Unknown Speaker** [12:51:04]: We will just

**Randy Boyer** [12:51:04]: decide what we want to do.

**Randy Boyer** [12:51:06]: On the advisory side, we're very close to actually having it all done because you have the goals, you have the objectives, the OKRs.

**Randy Boyer** [12:51:24]: You just need the actuals and the actual actuals actually exist.

**Randy Boyer** [12:51:29]: So the question is, Getting the actuals.

**Randy Boyer** [12:51:32]: Perfect.

**Randy Boyer** [12:51:35]: Perfect.

**Randy Boyer** [12:51:35]: So when when I when I when I ask,

**Unknown Speaker** [12:51:38]: hey, what do you guys want to discuss?

**Unknown Speaker** [12:51:43]: It would be great if you actually gave access to work in progress because then I could I could tell the AI.

**Unknown Speaker** [12:51:55]: What do you think this corresponds if the complete result was 100%.

**Unknown Speaker** [12:52:02]: This work in progress, according to your judgment, is it 50% or 60%?

**Unknown Speaker** [12:52:09]: And then we can compare it with your self-valuation.

**Unknown Speaker** [12:52:16]: And you can say, that bastard things I'm only halfway through.

**Unknown Speaker** [12:52:24]: I thought I was 80% through or the opposite, right?

**Unknown Speaker** [12:52:28]: Whatever it is, doesn't matter.

**Unknown Speaker** [12:52:31]: Now,

**Ana Capuder** [12:52:34]: but how, for example, I just, okay, I'm trying to understand how, for example, would I evaluate how much I've progressed with the discussion together with beta waves, for example, right, on potential partnership.

**Ana Capuder** [12:52:46]: Where would we get this information?

**Ana Capuder** [12:52:49]: There's no metrics in terms of like, okay, it was just like discussion of how we would approach partnership in this case for the accelerator, right?

**Ana Capuder** [12:52:56]: But there's nothing that you can measure it was just discussion.

**Ana Capuder** [12:52:59]: Their feedback, like how do you capture that data?

**Ana Capuder** [12:53:04]: Yes, that is a that is a

**Unknown Speaker** [12:53:06]: fundamental question.

**Unknown Speaker** [12:53:07]: And there are always things that are harder to quantify.

**Unknown Speaker** [12:53:14]: that doesn't mean that we shouldn't try right so let me let me challenge you will be wrong but through experience we will we will diminish how wrong we are right

**Randy Boyer** [12:53:27]: so let me give you let me give you a let me let me challenge you with the following if we add the ability to, which I hope we will, depending on how things work with Cheatham and what tools we use and whatever.

**Randy Boyer** [12:53:45]: Let's say we recorded all of our conversations with all of our partners.

**Randy Boyer** [12:53:52]: What could have happened is the AI would have seen your conversation with Asama and did you talk to, what's her name?

**Randy Boyer** [12:54:07]: I'm having trouble with my names today.

**Randy Boyer** [12:54:09]: Anyway, the two people at BetaWaves, it could have looked at those two conversations and then made a guess and say you're 11% of the way towards a deal with, based upon what I saw, based upon what I read in the two and fro between Anna and the two people at BetaWaves, I'm estimating that you're 11%

**Randy Boyer** [12:54:38]: of the way towards having a partnership deal.

**Randy Boyer** [12:54:43]: And then Anna,

**Unknown Speaker** [12:54:45]: you are absolutely justified to question its conclusions and ask, why do you think that?

**Unknown Speaker** [12:54:56]: And then ask, okay, what can I do in order to get to 80% in a week or whatever else, right?

**Unknown Speaker** [12:55:06]: the numbers and the dashboard are not to say, okay, now the dashboard is done, the numbers are filled, I can wash my hand, this was useless.

**Unknown Speaker** [12:55:22]: But I was told I have to do it, so I did it, and I don't care, I did it.

**Unknown Speaker** [12:55:28]: No, all of this is only useful if they are the starting point to be able to ask ourselves how to work more efficiently and more effectively.

**Unknown Speaker** [12:55:42]: Okay.

**Unknown Speaker** [12:55:43]: And one

**Randy Boyer** [12:55:44]: of the things that the AI tools can do, and David taught me this is a lot of us use tools and we use a tool and we get some kind of result and we say, okay, we got the result.

**Randy Boyer** [12:55:57]: What David teaches us is that's only the starting point.

**Randy Boyer** [12:56:02]: Why don't you ask a couple of the other tools to critique the first tool about whether it really did the right job and how could it have improved.

**Randy Boyer** [12:56:13]: And so by getting in, by engaging in all of this critical evaluation of the tools and what it's doing, whether it did it right, whether the other tools can see where it made mistakes and whatnot, it just unbelievably helps you helps clarify and helps you to analyze things.

**Randy Boyer** [12:56:34]: I've never been able to analyze things at the granular level now that I can now because there are, I've got like all of these critical tools that can help me and I can have them fight it out between them.

**Ana Capuder** [12:56:52]: But does that mean then that we have to first trust our OKRs and KPIs to Let's say one AI tool so that they have something to compare it to like where we want to be and then we have to upload all the input right from the discussion then the then we would get results where we are like what is the

**Ana Capuder** [12:57:12]: metrics like or the progress and then we have to do the same process with other tools or like what what is the verdict like how how do we do that I'm just trying to understand so there are many ways

**Unknown Speaker** [12:57:22]: obviously and it will be up to the division has in collaboration with the executive management team to decide for each of the divisions as far as I am concerned I updated on my own my position on the art chart now that I have the new title of head of innovation I updated who am I report to to Amy

**Unknown Speaker** [12:57:59]: rather than Jerry and I already created in June for myself monthly milestones.

**Unknown Speaker** [12:58:14]: And I'm generating weekly and monthly reports.

**Unknown Speaker** [12:58:19]: And so with the change of the title, I just told the AI.

**Unknown Speaker** [12:58:24]: Take all of this in consideration and update everything accordingly.

**Unknown Speaker** [12:58:33]: And I literally say accordingly.

**Unknown Speaker** [12:58:36]: I'm not saying in this way, in that way, that other way.

**Unknown Speaker** [12:58:40]: I am not micromanaging it.

**Unknown Speaker** [12:58:47]: And then another thing I do is very often I don't even look at the output, but I feed it as input to the next stage.

**Unknown Speaker** [12:58:58]: So what I will do without even looking at the output is create my innovation division dashboard based on those OKRs and KPIs that you have decided I should have.

**Unknown Speaker** [12:59:15]: And then sooner or later I will need, and in my case, this is a big issue, touch reality.

**Unknown Speaker** [12:59:24]: Because in a lot of things that I am doing, I haven't been able for some reasons that don't matter get in touch with reality for too

**Randy Boyer** [12:59:36]: long.

**Randy Boyer** [12:59:37]: Unfortunately, David, I have to leave.

**Randy Boyer** [12:59:39]: The day from hell every minute of my day is, is, I'm going to call it scheduled, so I've got to go.

**Randy Boyer** [12:59:45]: But this is really, really interesting, and I'll follow up with Samuel and Anna on this and with you this weekend.

**Randy Boyer** [12:59:52]: Okay, very good.

**Randy Boyer** [12:59:53]: And I

**Unknown Speaker** [12:59:54]: will distribute you access credentials to be able to look at it directly to you.

**Unknown Speaker** [13:00:00]: Okay, thanks, David.

**Unknown Speaker** [13:00:02]: All right, bye.

**Unknown Speaker** [13:00:03]: Anna, Samuel, you can stay a few more minutes.

**Ana Capuder** [13:00:07]: Actually, Shaheen and Hela are waiting for me because we are supposed to move to Dubai, but I can stay on a call.

**Ana Capuder** [13:00:12]: I will just turn off the camera.

**Ana Capuder** [13:00:15]: Let me see.

**Unknown Speaker** [13:00:17]: So, just like last week, the conclusion is simple.

**Unknown Speaker** [13:00:24]: You don't report to me.

**Unknown Speaker** [13:00:26]: My offer to help is available.

**Unknown Speaker** [13:00:29]: And I can help.

**Unknown Speaker** [13:00:31]: in proportion to how much of what you are doing you share.

**Unknown Speaker** [13:00:35]: I'm not gonna force myself on you, nor I am gonna second guess what you are doing if you don't share spontaneously, right?

**Unknown Speaker** [13:00:46]: So I am happy that you wrote those four lines, and next week, actually I'm gonna be in Abu Dhabi, So next Friday, if you have a bit of time we may meet.

**Unknown Speaker** [13:01:05]: The offer and the invitation remains to share working progress so that I can show you how you can benefit from using AI in order to work faster and work better.

**Unknown Speaker** [13:01:21]: And also experience directly what it means to try to quantify things that intuitively you feel are hard or impossible to quantify.

**Ana Capuder** [13:01:35]: Yeah, that's great.

**Ana Capuder** [13:01:36]: Thank you.

**Ana Capuder** [13:01:36]: I mean, this task are only for the advisory part, because I think we're only testing this with advisory, right?

**Ana Capuder** [13:01:42]: But I work on the investment banking right now.

**Ana Capuder** [13:01:46]: And I feel like this is a great space to just experiment to begin with.

**Ana Capuder** [13:01:50]: For example, last time you restructured like the way, or like you created a list of tasks for the orbit.

**Ana Capuder** [13:01:56]: which was actually a great start because it gives you an orientation of like, okay, these are the phases, this is what we're gonna do, then like subtask, the deliverables, who the person is, like, who is the responsible person and so on, which is, I think, like, a great approach.

**Ana Capuder** [13:02:13]: What I've done, though, is that I feel like sometimes the AI didn't capture everything correctly, but I think it's just because the material that was uploaded to AI was not the newest one, right?

**Ana Capuder** [13:02:24]: So what I've done is... I updated the newest proposal that we shared with Orbit and I asked it again, okay, so now create like new list of tasks.

**Ana Capuder** [13:02:34]: And then I got like a better version of like all the things that we should tackle.

**Ana Capuder** [13:02:39]: And then I revised what you already put in Asana.

**Ana Capuder** [13:02:42]: I mean, there's still some stuff I need to change because I keep having conversation with people and they bring new ideas and I'm like, okay, we can do it differently.

**Ana Capuder** [13:02:48]: But it was a great starting point, you know, like just to give people an idea of where they are.

**Ana Capuder** [13:02:55]: Wonderful.

**Unknown Speaker** [13:02:55]: Okay, thank you.

**Unknown Speaker** [13:02:58]: So please say hello to your traveling companions and I will keep conversing with Samuel.

**Unknown Speaker** [13:03:11]: Okay,

**Ana Capuder** [13:03:11]: thank you, David.

**Ana Capuder** [13:03:13]: See you, see you next week.

**Ana Capuder** [13:03:14]: Bye, bye-bye.

**Ana Capuder** [13:03:16]: So

**Unknown Speaker** [13:03:17]: just a couple of questions and then one recommendation.

**Unknown Speaker** [13:03:25]: Were you able to ask Chidem to change the URL of the SharePoint server?

**Unknown Speaker** [13:03:32]: No,

**Samuel Tregeagle** [13:03:34]: I honestly, that one completely slipped my mind.

**Samuel Tregeagle** [13:03:37]: Okay, no problem.

**Samuel Tregeagle** [13:03:39]: Yeah.

**Samuel Tregeagle** [13:03:40]: Did you see Michael

**Unknown Speaker** [13:03:41]: tagging you to get access to pitch book because he doesn't know who has that and he wanted you to have ownership of that task?

**Samuel Tregeagle** [13:03:52]: Michael tagged me to have ownership of pitch book?

**Samuel Tregeagle** [13:03:55]: Yeah, here.

**Samuel Tregeagle** [13:03:56]: Where is in an email or?

**Samuel Tregeagle** [13:03:58]: No, on Slack here,

**Unknown Speaker** [13:04:00]: right here.

**Unknown Speaker** [13:04:01]: Samuel, this is you.

**Samuel Tregeagle** [13:04:07]: Ah.

**Samuel Tregeagle** [13:04:07]: On Tuesday.

**Samuel Tregeagle** [13:04:08]: Yeah, I did not say that at all.

**Samuel Tregeagle** [13:04:10]: Where is this?

**Samuel Tregeagle** [13:04:11]: This is the pitch book channel.

**Samuel Tregeagle** [13:04:14]: The pitch book channel.

**Samuel Tregeagle** [13:04:17]: So you could,

**Unknown Speaker** [13:04:18]: you could.

**Unknown Speaker** [13:04:19]: I'm

**Samuel Tregeagle** [13:04:21]: not in that channel.

**Samuel Tregeagle** [13:04:24]: Oh, that's...

**Unknown Speaker** [13:04:26]: I was going to say,

**Samuel Tregeagle** [13:04:27]: I was like, I'm concerned.

**Samuel Tregeagle** [13:04:29]: I'm missing a lot.

**Samuel Tregeagle** [13:04:31]: No, no, I'm not in that channel.

**Samuel Tregeagle** [13:04:34]: Samuel was moved in this

**Unknown Speaker** [13:04:38]: channel, so he could not see.

**Samuel Tregeagle** [13:04:44]: Thank you.

**Samuel Tregeagle** [13:04:45]: Thanks for bringing that to my attention.

**Samuel Tregeagle** [13:04:50]: Okay.

**Samuel Tregeagle** [13:04:52]: Adam.

**Samuel Tregeagle** [13:04:54]: Thanks to that.

**Unknown Speaker** [13:04:59]: All

**Samuel Tregeagle** [13:04:59]: right.

**Samuel Tregeagle** [13:05:05]: Okay.

**Samuel Tregeagle** [13:05:06]: This mania

**Unknown Speaker** [13:05:07]: of having secret channels is killing me.

**Unknown Speaker** [13:05:14]: All right.

**Unknown Speaker** [13:05:14]: Yeah,

**Samuel Tregeagle** [13:05:15]: I mean, this pitchfork one, I don't know of it.

**Samuel Tregeagle** [13:05:18]: I get it in that they're trying to reduce the noise of that that people get on their feed.

**Samuel Tregeagle** [13:05:25]: Slack, slack

**Unknown Speaker** [13:05:27]: is... a chamber of zombies and of deathly silence.

**Unknown Speaker** [13:05:35]: The only channel where there are people who are alive is water cooler, everything else is frighteningly absent.

**Unknown Speaker** [13:05:48]: Oh, I do agree.

**Unknown Speaker** [13:05:49]: And I see the stats, because everyone can see the stats and 90% of the conversations are indirect messages.

**Unknown Speaker** [13:06:00]: We are paying for Slack for nothing.

**Unknown Speaker** [13:06:04]: And if Michael believes that we would be distracted by the conversations, then we should rename ourselves only one kindergarten.

**Samuel Tregeagle** [13:06:22]: Because it means we are not professionals.

**Unknown Speaker** [13:06:25]: We are incapable of being disciplined and pursue our goals, and we need such a strict oversight because otherwise we are distracted.

**Unknown Speaker** [13:06:38]: It's really, really bad.

**Unknown Speaker** [13:06:40]: I hope I will remember to tell him.

**Unknown Speaker** [13:06:45]: Okay, so the question then was, not the question these were the questions the recommendation was that yes you can organize your notes but what i would recommend you start with is to just copy paste everything in a single text file

**Samuel Tregeagle** [13:07:14]: yeah and tell the ai please organize my notes that's what i'll do david but you're gonna you might I write a lot of my notes in here.

**Samuel Tregeagle** [13:07:24]: Yeah, yeah, you know what you

**Unknown Speaker** [13:07:25]: can do.

**Unknown Speaker** [13:07:26]: You take a photo of your notebook and you say, here is what I wrote, and here is my notebook, and it will understand your handwriting.

**Unknown Speaker** [13:07:38]: It will understand your notebook.

**Unknown Speaker** [13:07:40]: It will even design the, if you created charts, it will recreate the charts.

**Unknown Speaker** [13:07:49]: I'm going to have to...

**Samuel Tregeagle** [13:07:51]: Okay, so in terms of that, the best tool for... Yeah, okay, cool.

**Samuel Tregeagle** [13:07:57]: All right, that's a good start.

**Samuel Tregeagle** [13:08:03]: One thing that I just want to... This is not necessarily entirely related, but I just want to flag, because I literally just had a meeting with these guys, and they mentioned using AI to generate a video which can be used as a sort of... explainer for some of the technology, which might not be

**Samuel Tregeagle** [13:08:22]: obvious to people outside their industry.

**Samuel Tregeagle** [13:08:24]: And I know that you used AI to generate some semi-static, but moving from memory, like you used to use the AI to generate some video sitting in the background as like an ambient thing for your slides, right?

**Samuel Tregeagle** [13:08:38]: I was wondering if I haven't had a chance to check the AI channel yet, but I was wondering if you have any recommendations for that.

**Samuel Tregeagle** [13:08:44]: Okay, so why don't you

**Unknown Speaker** [13:08:45]: please ask the question there?

**Unknown Speaker** [13:08:47]: and then I will answer.

**Unknown Speaker** [13:08:49]: And the reason we want that is for it to accumulate the knowledge and share knowledge with everyone else, right?

**Unknown Speaker** [13:08:57]: So in the leapfrogging, every week a new tool is better.

**Unknown Speaker** [13:09:06]: So I started my slides with mid-journey.

**Unknown Speaker** [13:09:11]: Then if you asked me two weeks ago, I would have said Sora.

**Unknown Speaker** [13:09:18]: And and this week I am telling you the best is to use Nano Banana Pro.

**Samuel Tregeagle** [13:09:28]: Nano Banana Pro?

**Samuel Tregeagle** [13:09:30]: Nice.

**Samuel Tregeagle** [13:09:31]: Nano Banana Pro

**Unknown Speaker** [13:09:33]: by Google is part of Gemini or Gemini.

**Unknown Speaker** [13:09:41]: Right.

**Unknown Speaker** [13:09:42]: For creating an image and then using VEO, VEO 3.1 to animate it or to do whatever you want, right?

**Unknown Speaker** [13:09:56]: So, for example, creating, let me show you, I will share it here

**Samuel Tregeagle** [13:10:04]: on this other computer.

**Samuel Tregeagle** [13:10:06]: While you're doing that, I'm going to put the message in the channel as well.

**Unknown Speaker** [13:11:11]: Hmm.

**Unknown Speaker** [13:11:40]: Okay, so let

**Unknown Speaker** [13:11:54]: me let me open it here.

**Unknown Speaker** [13:12:23]: So, okay, well.

**Unknown Speaker** [13:12:30]: What I said to the AI is, actually, I started from, let me show you that one as well.

**Unknown Speaker** [13:12:45]: So, Gemini.Google.com.

**Unknown Speaker** [13:12:50]: You see, NanoBanana Pro.

**Unknown Speaker** [13:12:53]: And I went to this.

**Unknown Speaker** [13:12:58]: Maybe.

**Unknown Speaker** [13:13:00]: No, this one.

**Unknown Speaker** [13:13:01]: Infographic, yes.

**Unknown Speaker** [13:13:04]: Animate AR Future.

**Unknown Speaker** [13:13:12]: Transcript AI Stack Distance, sorry.

**Unknown Speaker** [13:13:16]: So this is the prompt.

**Unknown Speaker** [13:13:19]: describe the integrated AI stack, energy, tube design and manufacturing, data center design and deployment, batteries, solar power, closed loop cooling, LLM training, inference, and the various applications possible from scientific discoveries to materials, blah, blah, blah.

**Unknown Speaker** [13:13:40]: That's it.

**Unknown Speaker** [13:13:41]: So you went to describe this, right?

**Unknown Speaker** [13:13:47]: And then I said, create a widescreen infographic based on the description above.

**Unknown Speaker** [13:13:56]: And it created this infographic, right?

**Unknown Speaker** [13:13:59]: It's nice, nicely structured.

**Unknown Speaker** [13:14:01]: And you could, you could, in the style of a blueprint, in the style of wood carving, in the style of space age aliens, whatever you want.

**Unknown Speaker** [13:14:14]: And then I said, animate the infographic with small movements of the various parts.

**Unknown Speaker** [13:14:26]: And I don't know if you can hear it, but it even added the...

**Samuel Tregeagle** [13:14:29]: Yeah, I could hear it before, yeah.

**Samuel Tregeagle** [13:14:31]: Yeah, yeah, it even

**Unknown Speaker** [13:14:32]: added the music.

**Unknown Speaker** [13:14:35]: And how do I do it full screen like this?

**Unknown Speaker** [13:14:41]: Yeah, okay.

**Unknown Speaker** [13:14:43]: Video full screen.

**Unknown Speaker** [13:14:47]: Yeah.

**Unknown Speaker** [13:14:50]: So, so it is, it is really cool.

**Unknown Speaker** [13:14:55]: Very impressive.

**Unknown Speaker** [13:14:57]: This is not an explainer video, right?

**Unknown Speaker** [13:14:59]: So what they either doing or what they should be doing is to create a script.

**Unknown Speaker** [13:15:05]: Yeah.

**Unknown Speaker** [13:15:07]: Storyboard.

**Unknown Speaker** [13:15:08]: And yes, they understand what are the information content.

**Unknown Speaker** [13:15:15]: And then if they don't feel that they are very good at narrating it to themselves, they would use hey gen.

**Samuel Tregeagle** [13:15:26]: They'll use talking heads.

**Unknown Speaker** [13:15:30]: Yeah.

**Unknown Speaker** [13:15:32]: Yeah.

**Unknown Speaker** [13:15:35]: And hey gen is the best for creating talking heads.

**Samuel Tregeagle** [13:15:42]: Yeah.

**Samuel Tregeagle** [13:15:43]: Yeah.

**Samuel Tregeagle** [13:15:49]: Excellent.

**Samuel Tregeagle** [13:15:51]: And then they can

**Unknown Speaker** [13:15:52]: have a narrator, they can have the illustrations, and they can have all the story arc and so on.

**Unknown Speaker** [13:16:03]: Yeah.

**Unknown Speaker** [13:16:05]: Yeah, very nice.

**Unknown Speaker** [13:16:05]: Thank you.

**Unknown Speaker** [13:16:11]: Okay.

**Unknown Speaker** [13:16:15]: All right, so have a great four-day weekend.

**Samuel Tregeagle** [13:16:20]: It's, yeah, I've really changed because the thing that's most exciting to me is that I can just sit down and like focus just on these one project.

**Samuel Tregeagle** [13:16:29]: So times have changed, but I'm looking forward to it.

**Samuel Tregeagle** [13:16:33]: As well as

**Unknown Speaker** [13:16:34]: hopefully some R&R.

**Unknown Speaker** [13:16:37]: R&R.

**Samuel Tregeagle** [13:16:40]: The work is R&R, isn't it?

**Samuel Tregeagle** [13:16:42]: If you like it, it is.

**Unknown Speaker** [13:16:44]: Yeah, that's true.

**Unknown Speaker** [13:16:45]: That's true.

**Samuel Tregeagle** [13:16:47]: But you're going to be in the office next week.

**Samuel Tregeagle** [13:16:50]: Yes, I fly on

**Unknown Speaker** [13:16:51]: Thursday, in the office on Friday, and then, of course, finance week.

**Samuel Tregeagle** [13:16:59]: Yeah, yeah, true.

**Samuel Tregeagle** [13:17:01]: It's a week after.

**Samuel Tregeagle** [13:17:02]: True.

**Samuel Tregeagle** [13:17:03]: Well, we should schedule some time, have a little catch-up, just chat about stuff outside of work as well.

**Samuel Tregeagle** [13:17:09]: Oh, yeah, well, absolutely.

**Unknown Speaker** [13:17:11]: Yeah, Saturday.

**Samuel Tregeagle** [13:17:13]: I hear that you're a fan of a bit of philosophical debate, and... And I don't know if I'm up to your standard, but I'm interested to have a chat to you about it anyways.

**Samuel Tregeagle** [13:17:24]: Just to hear your thoughts.

**Samuel Tregeagle** [13:17:25]: I think that could be something fun for us to chat about.

**Samuel Tregeagle** [13:17:28]: I am looking forward to

**Unknown Speaker** [13:17:29]: it, and I will definitely take you up on it.

**Samuel Tregeagle** [13:17:32]: Excellent.

**Samuel Tregeagle** [13:17:33]: All right.

**Samuel Tregeagle** [13:17:34]: Have a good one, David.

**Samuel Tregeagle** [13:17:34]: I'll talk to you soon.

**Samuel Tregeagle** [13:17:36]: Bye-bye.

---
*Backed up from MeetGeek on 2026-03-30 08:51*
