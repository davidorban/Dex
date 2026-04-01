# AI Agents Experimentation and Oversight

**Date:** 2026-02-25
**Duration:** Unknown
**Meeting ID:** 12904375-c438-4f0f-8379-3c6f80be0164

## Participants
- *Participants not listed*

### Summary

The meeting focused on operationalizing AI agents for team workflows: confirming that briefs and agendas were AI-generated, discussing the participant's positive experience receiving measurable feedback and managerial recognition, and exploring AI use for market research and complex financial modeling. The conversation assessed optimal agent counts versus human attention limits, task decomposition, and levels of human oversight, while raising regulatory and data-residency concerns. Tool capabilities and access issues were noted, including lack of co-work access and plans to pick up compatible hardware. The group contrasted proactive agents (OpenClaw) with Claude, decided to sandbox riskier agents in Alivon Labs, and agreed to document use cases, add repeatable evals, and incorporate executive summaries to manage output volume.

## Full Transcript

**Speaker_04** [07:30:01]: So I just responded to your report.

**Speaker_01** [07:30:07]: Yeah.

**Speaker_04** [07:30:08]: And the original brief, your report, my response, they are very properly AI generated,

**Speaker_01** [07:30:19]: as

**Speaker_04** [07:30:20]: they should be.

**Speaker_04** [07:30:22]: and including the agenda for the meeting, which is super detailed, extending to an hour, even though we only booked a half an hour, by the way.

**Speaker_04** [07:30:33]: I forgot to add that detail to the thing designing the agenda, or generating the agenda.

**Speaker_04** [07:30:41]: And all of this should enable us to concentrate on what matters and then look at what should be the next steps, right?

**Speaker_04** [07:30:58]: Yeah.

**Speaker_04** [07:30:59]: So, first of all, how do you feel about being the experimental subject of this process?

**Speaker_04** [07:31:12]: Is it something that you enjoy or it concerns you because it detracts time from other things you have to do, or it compliments and supports it well.

**Speaker_02** [07:31:24]: I think that's a very interesting question for a number of reasons.

**Speaker_02** [07:31:27]: I think to answer it, I love That's great.

**Speaker_02** [07:31:33]: But there's several layers to that answer.

**Speaker_02** [07:31:36]: And it kind of

**Speaker_02** [07:31:44]: goes back

**Speaker_02** [07:31:50]: to where we are as not only is there the human level of, you know, I can see I'm adding value, but also because we're a new bank, you know, KPIs and all that sort of stuff is a little bit vaguer.

**Speaker_02** [07:32:10]: Now, you have done the roll charter and things, and that's great, but the scope of my role means that, you know, in terms of measurable outcomes that you can easily quantify.

**Speaker_02** [07:32:20]: It's not quite so simple.

**Speaker_02** [07:32:23]: Whereas this has a very clear framework, you know, very clear steps and it's a very measurable process.

**Speaker_02** [07:32:30]: So it's one area, you know, obviously it's within my role charter to be doing this.

**Speaker_02** [07:32:35]: And so it's really actually quite gratifying to have a quantification of my... you know my work efforts and the actual results of them you know so it's yeah on that level it's it's really quite nice and also reassuring because it's something that I'm you know continually seeing you feel your own

**Speaker_02** [07:32:55]: exactly exactly and so it's it's almost like instantaneous feedback that I'm getting to myself on the progress

**Speaker_04** [07:33:01]: Before today's email with the report attached, did you have a chance to brief Toby at all on what you were doing and when you did, if you did, did he show support?

**Speaker_04** [07:33:16]: Was he... Was he, did he ask any follow- up questions?

**Speaker_04** [07:33:23]: Did he show interest about it?

**Speaker_02** [07:33:26]: Yeah, no, he's definitely been quite interested in what I'm doing.

**Speaker_02** [07:33:31]: You know, frequently he walks by my desk and, you know, he's like, oh, what's, yeah, what's going on?

**Speaker_02** [07:33:36]: What are you doing here?

**Speaker_02** [07:33:37]: And, you know, yesterday I was working on a financial model with Claude ad-in there, and he was like, oh, that's, you know, what you're doing there.

**Speaker_02** [07:33:46]: I was like, I explained to him I was using Claude to test some of the logic in the model, and all of those things and how I'd basically used Claude to actually rework some bits that I'd done so I'd imposed my logic but I wasn't quite managing to get something to link up just because of the

**Speaker_02** [07:34:03]: complexity of the model and I had I then got to a point where I was like I could use Claude for this so I said to Claude oh can you look at this you know this is what I'm trying to do you know this is how I've been taught to do it this is the logic I follow but for some reason the numbers aren't

**Speaker_02** [07:34:16]: looking quite right to me can you have a look and see And it very quickly, you know, did stuff in the background while Star was unable to do other stuff.

**Speaker_02** [07:34:24]: It took even called quite a lot of time.

**Speaker_02** [07:34:27]: Yeah, as it is natural.

**Speaker_02** [07:34:29]: Yeah.

**Speaker_02** [07:34:31]: But coming back to the question then, you know, yes, Toby's been very interested.

**Speaker_02** [07:34:34]: You know, I've definitely been keeping him updated with what I'm doing.

**Speaker_02** [07:34:38]: Randy's very interested as well.

**Speaker_02** [07:34:41]: And, you know, we have our weekly advisory and IB meetings on a Monday.

**Speaker_02** [07:34:46]: So, you know, even this Monday, Toby gave a shout out to me to say, you know, I've been doing... loads of really impressive things with the AI to help the workflows and contribute to the teams.

**Speaker_02** [07:34:58]: And obviously some deliverables, you've seen some things I've just taken the initiative to do as extra because I now have that.

**Speaker_02** [07:35:06]: Including

**Speaker_04** [07:35:07]: the weekly market research,

**Speaker_02** [07:35:09]: right?

**Speaker_02** [07:35:09]: Exactly what I was referring to right

**Speaker_04** [07:35:11]: there.

**Speaker_04** [07:35:12]: Yeah, yeah.

**Speaker_04** [07:35:12]: It's

**Speaker_02** [07:35:12]: fantastic.

**Speaker_02** [07:35:13]: So it's great and it's constantly giving me ideas for how I can improve because the market research, historically I might have spent all that time doing the analysis and stuff to build the report and you'd get so stuck down bogged down in what your focus is on, but you kind of lose track of the

**Speaker_02** [07:35:33]: overall picture and kind of where there might be pitfalls.

**Speaker_02** [07:35:36]: Whereas this way, you're not quite so focused in the box.

**Speaker_02** [07:35:42]: So, for example, off the back of the last one that I did, and off the IB meeting that we had, I actually realized another iteration that I could do on that in order to add even more value for the origination team.

**Speaker_02** [07:35:58]: So, you know, and that's something that, you know, without the use of AI would just be nigh on impossible, because the add-in that I'm going to do next time requires the analysis of something like 42 pages worth of individual names.

**Speaker_02** [07:36:17]: The amount of data just on that alone is just ridiculous.

**Speaker_02** [07:36:20]: Whereas, you know, it's a very simple download and us, Claude, I would just add this extra output.

**Speaker_02** [07:36:27]: And, you know, very quick and easy to then add further actions off of the thing.

**Speaker_02** [07:36:34]: Because at the minute as it stands, it's like... identifying trends, making suggestions for opportunities, suggesting where we should monitor things.

**Speaker_02** [07:36:43]: But then, you know, for origination, for example, it's like, okay, great, here's this company, we should follow, we should try and see what we can do with this opportunity here.

**Speaker_02** [07:36:55]: Who do I reach out to?

**Speaker_02** [07:36:56]: Yeah.

**Speaker_02** [07:36:57]: Right?

**Speaker_02** [07:36:58]: Whereas using this add-on, I can have Claude look through and be like, okay, of these opportunities, who would be the best people to reach out to for us?

**Speaker_02** [07:37:07]: And as we're looking to integrate the intelligence collective thing, I'm seeing the potential for trying to integrate that into the process as well so that we can see, okay, are there any individuals that we're already connected to within any of those companies that might actually be a better place

**Speaker_02** [07:37:29]: to reach out to, to build a relationship?

**Speaker_04** [07:37:36]: There are both in the initial brief and in your report some arbitary values like 10 agents, well we have 10 fingers, so why not a round number, right?

**Speaker_04** [07:37:53]: Sure.

**Speaker_04** [07:37:53]: Makes no difference whether they are 5 or 15. I think it is good to have the kind of self-assessment that you have applied to understand at each time what is the right number of type of use cases.

**Speaker_04** [07:38:12]: And the reason why we call these agents is because you give them a task and then you concentrate your attention on something else.

**Speaker_04** [07:38:20]: And then you go back to it when it is done, enabling the notification so that you know it's done and it is waiting for you, right?

**Speaker_04** [07:38:33]: And the question is, Is it good to fragment our attention partially overlapping?

**Speaker_04** [07:38:44]: Half a dozen of these tasks that we can go back to when they finish.

**Speaker_04** [07:38:50]: If their duration is, let's say, half an hour, that maybe is feasible.

**Speaker_04** [07:38:59]: Maybe it is borderline too much because that kind of continuous partial attention introduces a cognitive deficit, a cognitive debt, where you need to switch context, you know.

**Speaker_04** [07:39:18]: Just like the AI, we also have this context limit.

**Speaker_04** [07:39:23]: And by the time we are ready to give our attention to something, already another thing is calling us, right?

**Speaker_04** [07:39:31]: And maybe that means that today it is better to keep it at a relatively lower number, five rather than 10 of these simultaneous opportunities, possibilities, application areas in the knowledge that very naturally, as the complexity of the tasks increases and the ability of cloth following a complex

**Speaker_04** [07:40:02]: task not for half an hour but for three hours or three days that will give you a way to delegate

**Speaker_04** [07:40:16]: then go delegate another one then go delegate another one increasing their total number or even introduce hierarchy where there is a middle management layer in the agents themselves so that you have, I don't know, five of them reporting to one and you are controlling

**Speaker_02** [07:40:40]: that well I mean I'm not necessarily to go into now but that's yes yes

**Speaker_04** [07:40:45]: so so the scaffolding of a genetic infrastructure is being built as we speak okay already Claude is able to spawn parallel tasks so you don't realize but It inside, it already is doing a bit of that.

**Speaker_02** [07:41:13]: Yeah, so when you give it one task, it's creating, but then it's also reviewing at the same time.

**Speaker_04** [07:41:17]: Something like that.

**Speaker_04** [07:41:18]: Or it does web search and web scraping while it is writing the word document with the styles that you requested and things like that, right?

**Speaker_04** [07:41:30]: Whatever it is, it decides how to break the task down.

**Speaker_04** [07:41:34]: what needs to be executed in sequence, what can be executed in parallel, okay?

**Speaker_04** [07:41:41]: So not only the question is at any given time what is the right complexity, duration, partial overlap, oversight of these tasks, but also interacting with the tool, what is the level of technical detail that is useful to gain what is the right investment on your side in understanding the inner

**Speaker_04** [07:42:08]: workings rather than just using the tool, right?

**Speaker_04** [07:42:12]: And I leave you to evaluate both.

**Speaker_04** [07:42:16]: So I invite you to address

**Speaker_04** [07:42:24]: as you look at what you are doing on top of what you already raised in terms of the fitness for purpose, where it may write too long or too short, how to prompt it well, how to write skills that give it the right constraints so that the output corresponds to what we want.

**Speaker_04** [07:42:57]: And on top of the other thing that you raised, and we will go back to it of the threshold of human oversight when it comes into the picture as opposed to complete delegation, right?

**Speaker_02** [07:43:11]: We

**Speaker_04** [07:43:12]: will come back to that.

**Speaker_04** [07:43:13]: So on top of these that you already raised and must continue in your experiment and self-evaluation, the other two that I would add are looking dynamically, what is the right number of tasks that you can launch and then review and manage properly in relation to their complexity and as the tool

**Speaker_04** [07:43:45]: allows more and more complex things to launch.

**Speaker_04** [07:43:48]: That's one.

**Speaker_04** [07:43:50]: And the second is I forgot, but it will come up because it was recorded.

**Speaker_04** [07:44:02]: So, let's go back to the issue of delegation versus human in the loop and the finalization of the product, let's say, okay?

**Speaker_04** [07:44:17]: That will be more and more crucial.

**Speaker_04** [07:44:20]: So your ability to understand what can be delegated and what

**Speaker_04** [07:44:32]: needs

**Speaker_04** [07:44:40]: so that there is phase one and then review in the middle, and then comes phase two and then review at the end.

**Speaker_04** [07:44:48]: These are extremely important components for two reasons.

**Speaker_04** [07:44:55]: One is that we are still at the beginning of exploring the capabilities of the tools, and while we are exploring them, the capabilities evolve as well, right?

**Speaker_04** [07:45:10]: our own ability to use them well, as well as their own ability to understand what we want and to accomplish it based on what we ask for.

**Speaker_04** [07:45:20]: But the second reason is as important, maybe even more important, that we are doing it relatively freely today,

**Speaker_01** [07:45:31]: but

**Speaker_04** [07:45:32]: we have to be cognizant about an increasing regulatory scrutiny that will come And so we have to be able to design workflows that are compliant.

**Speaker_04** [07:45:44]: Okay?

**Speaker_04** [07:45:45]: Yeah.

**Speaker_04** [07:45:45]: And today this will stop at at making sure that we review the work product, for example, but tomorrow it will include architecture as well, meaning that rather than using cloth as it is, we will use cloth in G42 that is the data location in the UAE rather than using cloud and we don't even know

**Speaker_04** [07:46:22]: where the data is, right?

**Speaker_04** [07:46:25]: Just a couple of examples.

**Speaker_04** [07:46:27]: Yeah.

**Speaker_02** [07:46:29]: There's a couple of points you made that I'd like to address, sir.

**Speaker_02** [07:46:32]: Yes.

**Speaker_02** [07:46:32]: Yeah.

**Speaker_02** [07:46:33]: So, firstly, coming back to what you were saying about the efficacy of how many agents and the fragmentation of human attention.

**Speaker_02** [07:46:47]: I think... There's definitely a point to be made about that.

**Speaker_02** [07:46:51]: I have been finding it's difficult to move to something else for a long period of time and like whilst doing that because of that jumping back and forth.

**Speaker_02** [07:47:03]: Now I think there is value in having a notification.

**Speaker_02** [07:47:07]: such that once it's done, you're aware that it's done, but you can still finish what you're doing uninterrupted.

**Speaker_02** [07:47:14]: So I think it can be quite good if used correctly.

**Speaker_02** [07:47:21]: There's no reason why you have to jump straight back to the thing.

**Speaker_02** [07:47:25]: You can do what you're doing, focus on what you're doing, and then jump back to what you're doing once you're good and ready, right?

**Speaker_02** [07:47:32]: The second thing which you brushed on earlier was escalations.

**Speaker_02** [07:47:40]: So in this whole kind of, excuse me, if you'd planned to get there later.

**Speaker_02** [07:47:47]: But I'm kind of curious to understand a bit more about the escalatory process, what it entails, how it works.

**Speaker_02** [07:47:56]: Yeah, how it looks from a practical perspective, from our side, and how I can start using that better.

**Speaker_04** [07:48:06]: Rephrase that because I'm not sure to which scaling you are referring to.

**Speaker_04** [07:48:14]: Scaling for your own use, a larger number of AI tools and agents, or scaling across the organization, or scaling hierarchically so that others in the team are

**Speaker_02** [07:48:26]: involved.

**Speaker_02** [07:48:26]: No, sorry, not scaling escalating.

**Speaker_04** [07:48:29]: Okay, escalating towards what?

**Speaker_02** [07:48:31]: Well, this is why I'm asking, because there was the point about escalations within the AI use process, and I wasn't too clear on what that

**Speaker_04** [07:48:42]: meant.

**Speaker_04** [07:48:43]: No, I either misspoke or you misunderstood.

**Speaker_04** [07:48:46]: Yeah.

**Speaker_04** [07:48:47]: So, but it is worth going through in spirals those concepts regardless.

**Speaker_04** [07:49:01]: both what I said and maybe finding out what I could have said.

**Speaker_04** [07:49:15]: Let's start with redefining or not redefining, restating, stating again, why the experiment started and what it wants to achieve.

**Speaker_04** [07:49:36]: The experiment started with understanding that the skill of managing and, sorry, defining, delegating and managing the execution of complex tasks that previously someone could only do with a human report today can be done with an AI report.

**Speaker_04** [07:50:04]: And so, even though one would hope that a junior employee possesses that ability to analyze implement, self- supervise, and then communicate the execution of complex tasks by themselves.

**Speaker_04** [07:50:35]: It is something that shouldn't be taken as a given, and definitely doing that with others, human, or in our case, AI, is a skill that we want to let our junior team members acquire early rather than in a few years' time in their professional development.

**Speaker_04** [07:51:06]: So this is the birth of the experiment and of the process.

**Speaker_04** [07:51:15]: The way that it is implemented today through Claude is

**Speaker_04** [07:51:28]: partially insufficient and it is fine for it to be so because Claude is very good at certain things and it is as of today not designed in other things in particular it is not very proactive it doesn't know what it doesn't know oftentimes it barges ahead.

**Speaker_04** [07:52:01]: And based on the information it has been given, it feels that it is the universe of assumptions it has to work from.

**Speaker_04** [07:52:22]: And the fact that this is changing both inside Claude as it is.

**Speaker_04** [07:52:28]: and there are new tools that are more capable of doing that makes it so that the experiment itself is not fixed.

**Speaker_04** [07:52:41]: It is a changing, the nature of the experiment will naturally change.

**Speaker_04** [07:52:47]: So we have to decide, you and I can do that.

**Speaker_04** [07:52:53]: Do we want to introduce new components to the experiment that make it harder to evaluate because it changes the premise to some degree, or we are happy to keep it fixed for the next, let's say, month and only introduce changes later on.

**Speaker_04** [07:53:13]: Let me give you two examples concretely of what I'm talking about.

**Speaker_04** [07:53:21]: The first of how Claude itself changes, you may have already noticed.

**Speaker_04** [07:53:25]: When you give a task to Claude co-work, it actually now has an interface to ask questions.

**Speaker_04** [07:53:34]: And I don't know if you noticed that

**Speaker_02** [07:53:36]: it... Unfortunately, I've not got access to co-work, yeah.

**Speaker_02** [07:53:39]: Because I'm on the ARM64.

**Speaker_04** [07:53:42]: That's intolerable.

**Speaker_03** [07:53:44]: Yeah.

**Speaker_03** [07:53:45]: Why didn't you complain louder?

**Speaker_03** [07:53:47]: I mean, there's not much we can

**Speaker_02** [07:53:50]: do now, is there?

**Speaker_03** [07:53:52]: Yes, you can't have a new computer.

**Speaker_03** [07:53:54]: Like today.

**Speaker_02** [07:53:55]: Really?

**Speaker_03** [07:53:56]: Yes.

**Speaker_03** [07:53:57]: Wow.

**Speaker_02** [07:53:59]: You

**Speaker_03** [07:53:59]: are talking to the head of IT.

**Speaker_03** [07:54:02]: Yeah, fair point.

**Speaker_02** [07:54:06]: But still a Windows computer.

**Speaker_03** [07:54:07]: Yeah.

**Speaker_02** [07:54:08]: Okay.

**Speaker_04** [07:54:13]: So you have been running with one leg chopped off for this whole time.

**Speaker_01** [07:54:20]: Yeah.

**Speaker_04** [07:54:24]: Okay.

**Speaker_04** [07:54:25]: Anyway,

**Speaker_04** [07:54:31]: do you mind coming to Adax to pick it up?

**Speaker_04** [07:54:36]: Whether today or tomorrow, it doesn't

**Speaker_02** [07:54:37]: matter.

**Speaker_02** [07:54:38]: At some point,

**Speaker_04** [07:54:38]: yeah, of course.

**Speaker_04** [07:54:39]: Okay?

**Speaker_02** [07:54:39]: Yeah.

**Speaker_04** [07:54:42]: So,

**Speaker_04** [07:54:49]: if you are using Claude Cobra, you may, it is possible that you could have noticed that it asks questions.

**Speaker_04** [07:55:01]: And that is fantastically important because it shows that it is starting to interpret your request in a broader context and in that context it has the ability to realize that it doesn't know certain things and rather than, as I said, barging ahead on the limited data it already has It realizes that

**Speaker_04** [07:55:30]: it could make better choices if you gave the additional information it needs.

**Speaker_04** [07:55:36]: And it will typically ask three or four follow-up questions and then adjust its plan based on your answers of what you want to achieve.

**Speaker_04** [07:55:46]: And it is of tremendous importance and value.

**Speaker_04** [07:55:49]: Yeah, that sounds really good, actually.

**Speaker_04** [07:55:50]: So that's one.

**Speaker_04** [07:55:52]: The second example that I want to give about how the experiment can evolve if we choose to do so, is open claw.

**Speaker_04** [07:56:04]: I don't

**Speaker_02** [07:56:04]: know if

**Speaker_04** [07:56:04]: you heard of it.

**Speaker_04** [07:56:07]: I'm already running a swarm of five instances and doing my own, of course, experiments with them.

**Speaker_04** [07:56:16]: and I already designed the naming convention based on Arabic constellations to be able to name I think total of 4,000 agents so with 50 people we can have 80 each of us or whatever number and the team of AI coworkers that we employ.

**Speaker_04** [07:56:53]: So whenever you feel that you want to extend your experimentation, we can introduce that as well.

**Speaker_02** [07:57:06]: I'd be keen to get right on that.

**Speaker_02** [07:57:08]: I think that'd be... Okay.

**Speaker_02** [07:57:11]: Yeah.

**Speaker_02** [07:57:11]: Why wait, right?

**Speaker_04** [07:57:12]: Yeah, well, the difference, the very important difference between Claude today and open claw, And by the way, I don't know if you heard that the creator of OpenClaw has been hired by OpenAI.

**Speaker_04** [07:57:29]: So we will see the leapfrogging that

**Speaker_01** [07:57:33]: I

**Speaker_04** [07:57:33]: described.

**Speaker_01** [07:57:34]: And

**Speaker_04** [07:57:35]: I'm not saying we will go back to OpenAI, but we will have a nice challenge when OpenAI introduces it, and then Claude will or will not, we'll see what we will decide.

**Speaker_04** [07:57:46]: Manus already introduced it.

**Speaker_04** [07:57:47]: Manus integrates now.

**Speaker_04** [07:57:49]: an open claw agent.

**Speaker_04** [07:57:53]: And the fundamental difference between Claude and open claw is the degree of proactivity that open claw exhibits.

**Speaker_04** [07:58:06]: So if Claude decides to ask questions, open claw goes further, not only it imagines what are the answers that you would give, but since it works 24- 7, it keeps asking itself what could I do to be more useful constantly.

**Speaker_04** [07:58:36]: And you can decide what is the frequency once a day or twice a day that it updates you about its thinking and actions based on what it decides to do.

**Speaker_04** [07:58:51]: And this makes it extremely powerful, also extremely dangerous.

**Speaker_04** [07:58:58]: when we start using it, rather than using it in your existing environment, we will use it under Alivon Labs.

**Speaker_04** [07:59:07]: I don't know if I mentioned to you Alivon Labs.

**Speaker_04** [07:59:11]: So you will have an account on Alivon Labs so that we isolate the behavior of this alien agent and whatever mistakes it makes it makes it in isolation rather than impacting our existing infrastructure.

**Speaker_04** [07:59:34]: Yeah, that makes sense.

**Speaker_04** [07:59:38]: All right, so the

**Speaker_04** [07:59:46]: Two things that your report highlights are good and assuming you had the time to read the report.

**Speaker_04** [07:59:53]: Yeah.

**Speaker_02** [07:59:54]: I wouldn't have passed it on to you had I not.

**Speaker_02** [07:59:56]: I did make a few minutes of education as well.

**Speaker_02** [07:59:58]: I'm half

**Speaker_04** [07:59:58]: joking.

**Speaker_04** [07:59:59]: However, I'm pretty serious.

**Speaker_04** [08:00:01]: I mean, I do always read what I produce.

**Speaker_04** [08:00:07]: But I want to be explicit about the fact that it is okay to realize that the volume of output often exceeds our ability to absorb it.

**Speaker_04** [08:00:18]: That is why executive summaries are a perfectly good tool to make it explicit.

**Speaker_04** [08:00:24]: If you read that, it's okay.

**Speaker_04** [08:00:27]: Right?

**Speaker_04** [08:00:27]: I produced it, I'm responsible for it, but I understand you may not have the time to read all that, all that I produced,

**Speaker_01** [08:00:36]: right?

**Speaker_04** [08:00:37]: it is still useful because then you can feed it to another AI, like I did when I composed the email response to you two minutes before coming to the meeting, right?

**Speaker_04** [08:00:50]: So going back to the report, at the end of the report, there are two things that you highlight.

**Speaker_04** [08:00:57]: Go ahead, chewing on them.

**Speaker_04** [08:00:59]: One of them was the escalation.

**Speaker_04** [08:01:04]: Yeah, that's where I use the word escalation.

**Speaker_04** [08:01:06]: You're right.

**Speaker_04** [08:01:08]: The fact that human oversight needs to be incorporated.

**Speaker_04** [08:01:20]: And then I explained it can be incorporated.

**Speaker_04** [08:01:22]: Well, it is naturally incorporated at the beginning through the prompt.

**Speaker_04** [08:01:28]: and then it must happen at the end before the work output is shared

**Speaker_04** [08:01:43]: so that you can confirm to the agent that it is going in the right direction, right?

**Speaker_04** [08:01:48]: It's exactly what we are doing now.

**Speaker_04** [08:01:51]: A review process where you assure the agent that it is doing the right thing, right?

**Speaker_04** [08:01:59]: Or nudge it in a different direction, right?

**Speaker_04** [08:02:01]: That is what I want you to think about in the escalation, how you manage

**Speaker_01** [08:02:07]: them.

**Speaker_04** [08:02:08]: Do you trust them just to say, okay, go and do your thing and you review at the end?

**Speaker_04** [08:02:13]: or you need to, quotation marks, micro- manage it a little bit more, right?

**Speaker_04** [08:02:18]: And it can depend on the task itself.

**Speaker_04** [08:02:21]: The last thing I want to mention is, well, two things, complementary.

**Speaker_04** [08:02:29]: One, the evals, which I know you built at least in one instance, but you didn't include in your report, or I missed it, in the sense that we have to be able to run repeated tests against a known set of examples in order to measure improvements.

**Speaker_04** [08:02:58]: And the second thing is exactly that about all of what you do in terms of quality and speed of what you are able to do.

**Speaker_04** [08:03:12]: So we have to document that in the use cases that you have already addressed in a very human-friendly manner, maybe one page per use case to say, this is how I did financial modeling, it would have taken me two days since that it took two hours knowing me it would have contained five mistakes since

**Speaker_04** [08:03:42]: that it contains to the best of my knowledge zero given the assumptions and the same for the other use cases as well yeah and and I leave it to you how you how you measure and how you compare the agent supported execution versus the manual execution, right?

**Speaker_04** [08:04:11]: Because I don't want you to waste your time and do it manually just so that you can prove the difference, right?

**Speaker_04** [08:04:18]: But yeah, these are the two things that I want you to concentrate on as well on top of the two that you already highlighted in the report.

**Speaker_04** [08:04:26]: Cool.

**Speaker_04** [08:04:27]: Okay?

**Speaker_04** [08:04:29]: All right, so computer, open clone, and all the rest.

**Speaker_04** [08:04:33]: Very

**Unknown speaker** [08:04:33]: good.

---
*Backed up from MeetGeek on 2026-03-30 08:42*
