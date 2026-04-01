# AI-Driven Knowledge & Document Strategy

**Date:** 2025-12-07
**Duration:** Unknown
**Meeting ID:** 42b06199-04c9-4ba4-9eca-9ef5b2b7358b

## Participants
- *Participants not listed*

### Summary

The meeting focused on establishing AI-driven workflows and tooling (Warp, Windsurf, Claude Flow) and recommended iterative multi-tool comparisons to produce and refine business plans, slide decks, and implementation playbooks. A digital twin of the organization using markdown folder structures and synthetic data was proposed to simulate divisions and optimize outcomes. Document and knowledge capture were emphasized—creating conversational templates, photographing handwritten notes for transcription, and producing three deliverables (implementation doc, executive summary, slide deck). Discussion covered limitations of current integrations (Copilot, Gemini), the need to run LLMs on Azure for better integration, cultural adoption challenges and gatekeeping within the organization, and operational quality issues (broken QR code, misspelled display name) that require attention.

## Full Transcript

**Speaker_03** [16:13:56]: Okay, so first of all, I'm delighted that Toby wants to use AI tools and that he is empowering you to do the thing or to produce first drafts to be reviewed etc.

**Speaker_03** [16:14:22]: fantastic also I like his approach which is not just give me the output but what he wrote is work with David to set

**Speaker_03** [16:14:42]: up

**Speaker_03** [16:14:50]: labeling you the data scientist of the group where you may or may not want to disabuse him of whatever his interpretation is of being a data scientist gives you the opportunity and the excuse of working with user-friendly processes because he's not expecting you to hand over the workflow so that he

**Speaker_03** [16:15:25]: can do that.

**Speaker_03** [16:15:27]: What he wants is you to keep doing that.

**Speaker_03** [16:15:31]: And the advantage of that is that contrary, for example, Randy or... Shahin who want to do things themselves and then are a bit frustrated when everything is not ship shape and as easy to use as a well polished Microsoft Word or PowerPoint, you can be on the edge and look at different things and

**Speaker_03** [16:15:57]: always come up with what works best and integrate and so on.

**Speaker_03** [16:16:01]: So I think that is a great way of taking advantage of his expectation and the way that he, at least as I interpreted, the email is setting up things.

**Speaker_03** [16:16:14]: Now, that is my premise.

**Speaker_03** [16:16:21]: What do you think and how do you want to go about it?

**Speaker_05** [16:16:25]: I

**Speaker_04** [16:16:30]: only have like a high level interpretation of at the moment when he described it to me it was less so much about setting up the workload and it was more just He's going to hand me a business paper, a business plan paper.

**Speaker_04** [16:16:45]: And he wanted to see AI flesh it out, flesh out the ideas, and then spend a bit of time presenting it, making it presentable to the board, that sort of thing.

**Speaker_04** [16:16:59]: Yeah, in terms of setting up a workflow, I would only really have the high level thoughts that you've already documented for this one, which is basically like broad or Chachi-Pati.

**Speaker_04** [16:17:12]: I'd be leaning towards Chachi-Pati.

**Speaker_04** [16:17:16]: But Manus and Jenspark, My experience with GenSpark has been that it's the best and it's good as a starting point.

**Speaker_04** [16:17:27]: But if we already have the text and if we already have some Aliwan branded presentations, then it's going to be more time inefficient to involve GenSpark.

**Speaker_04** [16:17:37]: I don't know about Manus too much.

**Speaker_04** [16:17:39]: I think we had a quick look at it and it wasn't quite as strong as GenSpark in the memory.

**Speaker_04** [16:17:43]: But I think in terms of structuring the information, Tai Chi PT is going to be the

**Speaker_02** [16:17:48]: best for that.

**Speaker_02** [16:17:49]: Okay, okay, wonderful.

**Speaker_02** [16:17:51]: I would like to introduce you to

**Speaker_03** [16:17:55]: three other components of a tool set that is expanding, contracting, diverging, consolidating, as they compete with each other.

**Speaker_03** [16:18:11]: The

**Speaker_03** [16:18:17]: first is warp.

**Speaker_03** [16:18:19]: which is an agentic AI-driven terminal, where you can set up the scaffolding of a project that has many components that you need static dynamic and you just mix them up without worrying.

**Speaker_03** [16:18:49]: And Warp can work both on your local computer as well as on remote repositories.

**Speaker_03** [16:18:57]: I use it with GitHub.

**Speaker_03** [16:19:00]: Are you familiar with GitHub?

**Speaker_03** [16:19:02]: Yeah.

**Speaker_03** [16:19:02]: Okay.

**Speaker_03** [16:19:03]: So that's the first.

**Speaker_03** [16:19:05]: And what is beautiful about it is that you don't have to worry about what developers really invest a lot of time fighting which is the updating, the incompatibilities of different libraries and versions and all that, which you can forget about because it will take care of it.

**Speaker_03** [16:19:31]: And it's fantastic because when there is an error, of something, whatever, it reads the output in the terminal of the error, and then says, do you want me to correct that?

**Speaker_03** [16:19:43]: Yeah.

**Speaker_03** [16:19:43]: You say, yeah, duh, I want you to correct it, and then you go ahead and iterate until it's fine.

**Speaker_03** [16:19:49]: So that's one.

**Speaker_03** [16:19:50]: The second is windsurf.

**Speaker_04** [16:19:55]: I've got windsurf.

**Speaker_03** [16:19:55]: Perfect.

**Speaker_03** [16:19:59]: And it's funny because... Cursor was the first forking VS Code, which is the Microsoft Integrated Development Environment.

**Speaker_04** [16:20:15]: That's what I've historically been using.

**Speaker_03** [16:20:17]: Yes.

**Speaker_04** [16:20:18]: Giving it, I didn't have Linux, so you're going to install the WSL and then run on this everything.

**Speaker_04** [16:20:24]: But historically I've been using VS

**Speaker_03** [16:20:25]: Code.

**Speaker_03** [16:20:27]: And so cursor was the first, but cursor initially only would give you suggestions line by line and windsurf's innovation, not even a year ago maybe, was that they actually went file by file and the windsurf agent would, if you went into Yolo mode, It would just do stuff on an entire file.

**Speaker_03** [16:21:03]: Typically the limit at the beginning was 500 lines of code and then it would start losing its memory.

**Speaker_03** [16:21:11]: And then Google gutted windsurf because they were about to be acquired by OpenAI.

**Speaker_03** [16:21:25]: And Google swooped the founder and CEO leaving the company empty, and then it was picked up and it still lives.

**Speaker_03** [16:21:35]: But the founder went to work for Google, and now Google released, it's called, not Atomic, I don't remember the name, they released an IDE based on Gemini, but it's the same thing, it's a VS Code fork, et cetera.

**Speaker_03** [16:21:59]: And these are becoming... Yes.

**Speaker_03** [16:22:04]: These are becoming really good.

**Speaker_03** [16:22:06]: What is good about windsurf is that you can hook it up with whatever engine you want.

**Speaker_03** [16:22:18]: Yeah.

**Speaker_03** [16:22:18]: And these days the best engine is Claude 4.5. sorry, cloud opus 4.5. Yeah.

**Speaker_03** [16:22:27]: That is seen as really the best until, you know, next time.

**Speaker_03** [16:22:36]: The third tool that I want to mention to you is cloud code.

**Speaker_03** [16:22:44]: Yeah.

**Speaker_03** [16:22:44]: Okay, which you run inside the terminal, so inside the warp.

**Speaker_04** [16:22:49]: Yeah.

**Speaker_03** [16:22:50]: And in particular, with Claude flow with that that creates the swarms of agents that just go for an hour to do what you told them through a plan and they speed out software as a service platform you know like that really amazing so

**Speaker_05** [16:23:18]: Why

**Speaker_03** [16:23:21]: is it worth, in my opinion, to handle multiple tools?

**Speaker_03** [16:23:28]: I wouldn't recommend it to Randy.

**Speaker_03** [16:23:30]: I wouldn't recommend it to Samuel.

**Speaker_03** [16:23:33]: Forget about Tony, right?

**Speaker_03** [16:23:35]: Toby.

**Speaker_03** [16:23:37]: but I think that you could easily

**Speaker_03** [16:23:48]: create a plan for example with chat GPT of what you want to do and then run the same plan on chat GPT on plot flow or whatever and then compare the output and see say review critically and suggest improvements.

**Speaker_03** [16:24:13]: Very simply that.

**Speaker_03** [16:24:15]: And do it back and forth two, three times until it becomes really robust.

**Speaker_03** [16:24:21]: Okay?

**Speaker_03** [16:24:25]: Yeah.

**Speaker_03** [16:24:26]: Now,

**Speaker_03** [16:24:32]: I actually created...

**Speaker_03** [16:24:41]: a digital twin.

**Speaker_02** [16:24:42]: Yeah.

**Speaker_02** [16:24:44]: Tell me more about that.

**Speaker_02** [16:24:45]: Okay.

**Speaker_03** [16:24:47]: So, when I arrived, you will see if you go back in the I don't know it all channel, I didn't know what was an investment bank.

**Speaker_03** [16:25:03]: What was a merchant bank?

**Speaker_03** [16:25:05]: Why we would call ourselves one day this, one day the other?

**Speaker_03** [16:25:08]: And I would just ask.

**Speaker_03** [16:25:12]: Or what is the difference between wealth management and asset management, what kind of services we would provide to families as a multifamily office, and so on and so forth.

**Speaker_03** [16:25:25]: And obviously my level of knowledge is now a little bit better, but not necessarily that deep.

**Speaker_03** [16:25:31]: So every time I receive a new org chart, I give it to Claude and I say update your understanding of Ali1 based on the new art chart.

**Speaker_03** [16:25:46]: Or we have a new presentation, you know, the latest partner deck, which was the one that Michael said, okay, with carefully, but this can be circulated, and so on.

**Speaker_03** [16:25:57]: Whatever new information, I just feed it to, to

**Speaker_03** [16:26:06]: very simply you can call it a folder structure and inside the folder are marked down files, and these represent the organization.

**Speaker_03** [16:26:22]: And then, periodically, I say, okay, analyze the whole thing, look at where the gaps are, look at what the activities are, and start enriching it and start modeling it, including what are the skills that are needed, what are the entities, what are the relationships, what are the revenue lines, and

**Speaker_03** [16:26:54]: so on and so forth.

**Speaker_03** [16:26:58]: And relatively recently, I started putting on top more agent-like structures that are trained... Oh, sorry, before we go to the agents.

**Speaker_04** [16:27:14]: Yeah, I think I see this.

**Speaker_03** [16:27:16]: So then having this empty structure, I say, create a set of synthetic data that can represent the full working situation of Ali 1 as if It were already full speed with a pipeline of investment banking mandates, with a fund that is deploying capital, with families where portfolios are being evaluated

**Speaker_03** [16:27:56]: and rebalanced for allocations of wealth and so on.

**Speaker_03** [16:28:04]: Two things I didn't yet feed completely to the system is Haoukouf, which is very particular and I

**Speaker_05** [16:28:17]: am simply...

**Speaker_03** [16:28:23]: Because I don't have... a good description yet of what Alcoff is going to do.

**Speaker_03** [16:28:31]: I mean, I have an understanding, but I didn't want to include it yet.

**Speaker_03** [16:28:36]: And I didn't include the sovereign banking opportunities here.

**Speaker_03** [16:28:43]: But for those that I did, investment banking, asset management, wealth management, family office, services, and not completely yet, but progressively back office as well.

**Speaker_03** [16:28:56]: including innovation division, AI native processes and so on, I said create a set of synthetic data and then train the agents on the synthetic data to execute the processes that the various divisions are supposed to carry out in order to not only simulate what the various outcomes are in terms of

**Speaker_03** [16:29:32]: generating revenue and commissions and whatnot, but with the ability to then instantiate an arbitrarily large number of variants and evolving them,

**Speaker_03** [16:29:54]: and it can be maximizing revenue, minimizing costs, maximizing upside in terms of equity that we earn and that we then monetize in the future, or I don't know, IPO in five years, whatever that you want to maximize.

**Speaker_03** [16:30:15]: So that is the reason for the digital twin to exist in order to not only have a static picture, but the ability to look at any kind of alternatives and to say, oh, that is better than this, and so why don't we move towards that?

**Speaker_03** [16:30:38]: Randy, for example, already gave me his business plan that he not only created in September, but I think October, whenever he was, he actually updated already incorporating his improved ability to serve his clients thanks to some of the AI workflows that in the meantime he acquired and is now using.

**Speaker_03** [16:31:08]: And so that's great.

**Speaker_03** [16:31:11]: And now we have the second division, or I mean advisory is part of IB, but we have IB itself that says, hey, this is my thinking, these are the components Let's put together a full business plan and a presentation based on it.

**Speaker_03** [16:31:35]: So really, really fantastic, because then you can take the first and the second and go to Dania and go to Miray and say, hey, do you want to play?

**Speaker_03** [16:31:47]: And they can say, go away, or they can say, all right,

**Speaker_04** [16:31:54]: let's

**Unknown speaker** [16:31:55]: try.

**Speaker_04** [16:31:55]: Yeah, I see the

**Unknown speaker** [16:32:02]: guidance.

**Unknown speaker** [16:32:21]: Thank you

**Speaker_04** [16:32:27]: In terms of what we're going to task with though, from what I understand, it's, we're experimenting, we're refining the process.

**Speaker_04** [16:32:35]: As you say, we're kind of bouncing between the different tools we have to see what the best outcome is going to be.

**Speaker_03** [16:32:43]: Well, Toby definitely didn't say try as many tools as you can.

**Speaker_03** [16:32:47]: He doesn't even care.

**Speaker_04** [16:32:48]: Yeah.

**Speaker_03** [16:32:49]: That is what I am suggesting, that it is worth.

**Speaker_03** [16:32:52]: Yeah.

**Speaker_03** [16:32:53]: It is worth setting things up.

**Speaker_03** [16:32:57]: iteratively, right?

**Speaker_03** [16:33:01]: You don't have to evaluate which is the best.

**Speaker_03** [16:33:04]: They will evaluate why and how a certain variant can be improved.

**Speaker_03** [16:33:13]: And then you look at their criteria and you say you are right or you are wrong, but The

**Speaker_03** [16:33:28]: output of an AI process has to be given to an AI.

**Speaker_03** [16:33:35]: To give it to a human is backwards.

**Speaker_03** [16:33:43]: Now, at the end, when you are done and after three rounds of evaluations, One and the other will say, I don't know what to do anyway.

**Speaker_03** [16:33:56]: This is good.

**Speaker_03** [16:33:57]: It is as good as it gets.

**Speaker_03** [16:34:00]: At the end, you will have a document and then you read through the document, and maybe you find something that they missed.

**Speaker_03** [16:34:08]: but not at the beginning, not at the middle, just at the end.

**Speaker_03** [16:34:14]: After three, four iterations.

**Speaker_03** [16:34:16]: Okay.

**Speaker_03** [16:34:16]: Right?

**Speaker_03** [16:34:17]: And then very likely what they produce is going to be far too long.

**Speaker_03** [16:34:22]: It will be like 20, 30 pages.

**Speaker_03** [16:34:25]: Yeah.

**Speaker_03** [16:34:25]: That's okay.

**Speaker_03** [16:34:27]: And then they will realize and they will suggest even to create an executive summary And then it is that that you translate into a slide that move.

**Speaker_03** [16:34:41]: And again, it can be done with one, two, or three different tools.

**Speaker_03** [16:34:47]: And you can now, you know, even Cloud itself generates slides, Gemini generates slides.

**Speaker_03** [16:34:56]: All of them now generate slides.

**Speaker_03** [16:34:58]: And you can download these slides in PPT and then compare again.

**Speaker_03** [16:35:03]: the mistakes that Manus made at the beginning of creating slides that were too tall.

**Speaker_03** [16:35:13]: Yeah, those Jens Park does that as well.

**Speaker_03** [16:35:15]: Some of them are now realizing and going back and say, no, no, I have to shrink it.

**Speaker_03** [16:35:20]: It's too tall.

**Speaker_03** [16:35:22]: So they start to understand that they don't have to cram every piece of information, that they have to find the ability to leave things out.

**Speaker_03** [16:35:33]: Yeah, and then in terms of finalizing the slides, I will really recommend, actually, I will just do it, not even recommend.

**Speaker_03** [16:35:46]: I will find a person that for $20 an hour, whatever it is, is a designer, a designer, specialized in designing sliders.

**Speaker_03** [16:36:06]: And we are missing that and we cannot accept neither to invest 10 times as much time as would be needed in order to make a slide deck decent, nor can we afford to give decks to clients or even internally that are ugly or uninformative and so on.

**Speaker_03** [16:36:33]: So it will take maybe a bit of time to find the right person.

**Speaker_03** [16:36:42]: I will experiment with one or two, but we don't need to hire them.

**Speaker_03** [16:36:49]: They just have to sign an NDA and then work on our decks.

**Speaker_03** [16:36:53]: That's very normal.

**Speaker_03** [16:36:57]: because we don't have the skill

**Speaker_04** [16:37:22]: In terms of, as you said, the output tends to be quite long, they're quite large with these are in the iterative process, right?

**Speaker_04** [16:37:33]: So if I understand correctly, we're prompting GPT or for example, or Claude, to review the business plan information that Toby gave us, come up with something.

**Speaker_04** [16:37:47]: And then equally we're prompting, we're taking that output, giving it to Claude, saying, giving Claude a prompt saying, criticize this, find where there's gaps, find the ways we can improve it, and bring this process back and forth three to four times, right?

**Speaker_03** [16:38:01]: Yes.

**Speaker_03** [16:38:02]: Yes, and you tell them to create a markdown file so that you move easily without worrying about formatting.

**Speaker_04** [16:38:09]: Yeah,

**Speaker_03** [16:38:10]: but generally

**Speaker_04** [16:38:11]: we're going to look at it for three or four iterations

**Speaker_03** [16:38:13]: anyway.

**Speaker_03** [16:38:14]: Yeah, yeah, yeah.

**Speaker_03** [16:38:15]: You look at what they say and it will be reasonable.

**Speaker_03** [16:38:19]: It will be really good stuff.

**Speaker_03** [16:38:21]: Yeah.

**Speaker_03** [16:38:22]: And then when you are happy with the final, there are different ways of changing the markdown into... a Microsoft Word document.

**Speaker_03** [16:38:37]: One is using the Pandoc libraries, but they produce something that I wasn't very happy with, ever.

**Speaker_03** [16:38:44]: I

**Speaker_04** [16:38:45]: have some

**Speaker_03** [16:38:46]: experience.

**Speaker_03** [16:38:47]: Yeah, the other is actually a workaround that I found today is the best.

**Speaker_03** [16:38:57]: Google Docs.

**Speaker_03** [16:38:59]: has a hidden feature that you have

**Speaker_03** [16:39:25]: And so the three work products are, or the three deliverables are the slide deck, the executive summary, and the third one, which is the long one, is the implementation document.

**Speaker_03** [16:39:44]: And maybe Toby will find the time to read it, maybe not, but that serves as a playbook to resort to as specific deals come

**Speaker_03** [16:40:16]: additional steps can be creating SOPs, creating standard operating procedures and processes and policies that tie together of how systematically, reproducibly, reliably do things.

**Speaker_03** [16:40:38]: Yeah.

**Speaker_03** [16:40:40]: I

**Speaker_05** [16:40:40]: mean, that

**Speaker_04** [16:40:44]: sounds like a good plan.

**Speaker_04** [16:40:44]: One thing that I've been encountering is particularly with the Islamic things, like for example, like this is in part, in our generation of fighting.

**Speaker_04** [16:40:57]: Actually, a billion-note stuff.

**Speaker_04** [16:40:58]: At a certain point, I don't know if it's the way I'm doing things, but it's starting to hallucinate a fair bit, it's starting to misinterpret distractions, giving me multiple sections of the same thing.

**Speaker_04** [16:41:09]: Have you encountered this, and if you have, how are you managing it?

**Speaker_00** [16:41:14]: Yeah,

**Speaker_04** [16:41:15]: so... One thing to be clear though, I haven't been using, since I got this new computer, I haven't been using... It's small or anything like that.

**Speaker_04** [16:41:25]: I haven't been using like multi-agents.

**Speaker_04** [16:41:26]: It's all been just GPT or quarter and trying to like, similar to what you were saying, except instead of iterating, I'm just more manually taking the best of both, which is less efficient, but so that's something

**Speaker_02** [16:41:39]: I can learn

**Unknown speaker** [16:41:40]: from.

**Speaker_03** [16:41:48]: the context window not only is limited but it keeps an increasing number of things together.

**Speaker_03** [16:42:09]: Each time like you talk about, it's feeding this whole conversation.

**Speaker_03** [16:42:12]: It keeps the conversation, it keeps the product, the output.

**Speaker_03** [16:42:18]: But today, things are made worse by the fact that it is also keeping instructions for the agents, it's keeping instructions for MCPs and other tools that it may end up deciding to use.

**Speaker_03** [16:42:33]: So the context window tends to fill up.

**Speaker_03** [16:42:40]: That is why, very recently, starting, I don't know, maybe two months ago, rather than talking about prompt engineering, people started to talk about context engineering.

**Speaker_03** [16:42:52]: or you don't worry about a prompt, the individual prompt, because the thinking models are very happy and eager to enrich your instructions with a broader scope, breaking it apart, and then telling themselves, oh, in order to get to the point which very succinctly the bus described, I need these

**Speaker_03** [16:43:26]: three, four, ten steps.

**Speaker_03** [16:43:28]: And then each step will be itself a prompt, etc.

**Speaker_03** [16:43:32]: So, prompt engineering is less necessary at this point.

**Speaker_03** [16:43:37]: What instead is very useful is what I also call scaffolding.

**Speaker_03** [16:43:45]: and it can also be called context engineering.

**Speaker_03** [16:43:49]: So what I do often, and that is why I look at the approach as if it were a code base, that is why I don't talk about single files but folders or folder structures of multiple folders, is I tell the engine, go through it and write documentation about it.

**Speaker_03** [16:44:12]: Write, read me.

**Speaker_03** [16:44:14]: And when there is some complex activity, I don't say do it, I say write a plan to do it.

**Speaker_03** [16:44:23]: And then, if it says, sorry, I'm too confused, I can say, don't worry, just refer to the plan, refer to the readme, check if it is up to date, if not updated.

**Speaker_03** [16:44:38]: even writing stuff like restart.md or wake up.md.

**Speaker_03** [16:44:46]: And then when I restart the session, completely fresh.

**Speaker_03** [16:44:51]: I say, the first thing I say is, read me, read the wake up, and start working on a plan again where you left off.

**Speaker_03** [16:45:02]: And that is a good way to clean the context.

**Speaker_03** [16:45:08]: Now, Claude started deciding on its own when it is the time to, it calls it compacting the context.

**Speaker_04** [16:45:19]: Yeah, I've

**Speaker_03** [16:45:19]: noticed.

**Speaker_03** [16:45:21]: And that's okay, I didn't take time to evaluate whether That's a really recent thing, though.

**Speaker_03** [16:45:28]: I've only seen it in the last

**Speaker_04** [16:45:29]: few days,

**Speaker_03** [16:45:30]: maybe

**Speaker_04** [16:45:30]: even a couple weeks.

**Speaker_03** [16:45:31]: That's right, something like that.

**Speaker_04** [16:45:32]: I kind of

**Speaker_03** [16:45:33]: moved off Claude for a bit.

**Speaker_03** [16:45:35]: So very, very recent, and I haven't yet had the chance of deciding whether I want to second guess it.

**Speaker_03** [16:45:42]: for the moment I, because actually when it does it, it asks, was this compacting good or not, and then you can tell it good, bad, or I don't know.

**Speaker_03** [16:45:52]: At the very

**Speaker_04** [16:45:53]: least, I've noticed it's... Its operationality is significantly better than GPT, you still doesn't have that context of

**Speaker_03** [16:46:01]: compression.

**Speaker_03** [16:46:02]: Yeah.

**Speaker_03** [16:46:03]: So, People expect OpenAI to release a new model this week, we'll see.

**Speaker_03** [16:46:11]: I started looking at co-pilot and it is unfortunately close to unusable.

**Speaker_03** [16:46:17]: Close to unusable?

**Speaker_03** [16:46:18]: For what kind of... Well, it knows nothing of its own place in the broader world of Microsoft Tools, it is completely unable to interact with them.

**Speaker_03** [16:46:37]: And even what they describe as agent studio is nothing what we understand agents to be, it's painful.

**Speaker_03** [16:46:50]: So for example, when when you are on a PowerPoint, copilot pops up and says, let me do something.

**Speaker_03** [16:47:01]: And you tell copilot to do something and very, very rapidly it says, oh sorry I cannot operate directly on the file, you have to do it manually.

**Speaker_03** [16:47:11]: And then why are you there if I have to do it manually?

**Speaker_04** [16:47:16]: This is the M365 version, right?

**Speaker_03** [16:47:17]: Yes.

**Speaker_04** [16:47:19]: That's discouraging.

**Speaker_00** [16:47:22]: Yes,

**Speaker_04** [16:47:23]: yes, definitely.

**Speaker_04** [16:47:25]: But it has reading capabilities, right?

**Speaker_04** [16:47:28]: Like, you can at the very least read your file, which is, well, it doesn't have... Yeah, I think so.

**Speaker_04** [16:47:36]: Yeah, because the flag narrated concern for me, because I suggest that we use Copilot for the research plan, not because we need to use it to... change anything, you know, documents.

**Speaker_04** [16:47:50]: That's not at all what I want, but just for, it's already integrated into SharePoint.

**Speaker_04** [16:47:57]: SharePoint means we can have a much better metadata structure than we can have in my pleasure it.

**Speaker_04** [16:48:03]: And for RAG, right?

**Speaker_04** [16:48:05]: Yeah, for RAG.

**Speaker_04** [16:48:07]: Yeah, for

**Unknown speaker** [16:48:08]: RAG.

**Speaker_04** [16:48:09]: I'm worried now, I feel like, is it even useful for that?

**Speaker_04** [16:48:13]: I mean, I haven't dug around and experimented.

**Speaker_04** [16:48:17]: You don't

**Speaker_03** [16:48:18]: think so?

**Speaker_03** [16:48:19]: Co-pilot, no.

**Speaker_03** [16:48:20]: Now, what we can and will use is the Azure cloud, and then we will just run our LLMs in the Azure cloud as a service.

**Speaker_03** [16:48:36]: and then interface that with Copilot or do whatever.

**Speaker_03** [16:48:41]: We'll see.

**Speaker_03** [16:48:41]: I'm not saying that it is going to be unusable forever, but it is close to unusable now at our level.

**Speaker_03** [16:48:52]: If someone says, hey, help me write an email and then they copy and paste the email in Outlook,

**Speaker_05** [16:49:00]: Yeah.

**Speaker_03** [16:49:01]: Sure, it will do it.

**Speaker_03** [16:49:03]: Yeah.

**Speaker_03** [16:49:03]: And why not?

**Speaker_03** [16:49:04]: It's okay.

**Speaker_03** [16:49:07]: Yeah.

**Speaker_03** [16:49:07]: But we need much more sophisticated integration than what it can now provide.

**Speaker_03** [16:49:14]: And the reason why that is so much of a letdown is because who can do this integration if not Microsoft?

**Speaker_03** [16:49:21]: Yeah.

**Speaker_03** [16:49:24]: And by the way, Gemini is the same.

**Speaker_03** [16:49:26]: So you have Gmail.

**Speaker_03** [16:49:29]: And you say, Gemini, find me the pitch decks that I was sent the last month.

**Speaker_03** [16:49:39]: Yeah.

**Speaker_03** [16:49:40]: And it would say, oh, sorry, I cannot see your messages.

**Speaker_00** [16:49:43]: Why do you even exist if you cannot do that?

**Speaker_00** [16:49:46]: Yeah.

**Speaker_03** [16:49:47]: Right?

**Speaker_03** [16:49:47]: Yeah.

**Speaker_03** [16:49:48]: And there are other tools that can.

**Speaker_03** [16:49:50]: So it is not that it is technically not possible.

**Speaker_03** [16:49:53]: It's that Google is stupid.

**Speaker_04** [16:49:58]: Okay.

**Unknown speaker** [16:49:58]: Okay.

**Speaker_03** [16:49:59]: Now, let's finish talking about the IB part, and then let's move to the document management part, okay?

**Speaker_03** [16:50:09]: So, given the transcription that we are doing, I will send you the notes that are structured, and then you can decide, yes, I want to follow them or I don't want to follow them, but it should be possible to move fast.

**Speaker_03** [16:50:30]: And a lot of us are so happy to move slow.

**Speaker_03** [16:50:37]: And, you know, maybe sometimes it's good.

**Speaker_03** [16:50:39]: You know, Michael took 10 years to get where we are now, and maybe we should take 10 years to make the next step.

**Speaker_03** [16:50:48]: But I will be dead in 10 years, so...

**Speaker_00** [16:50:58]: I will be on Mars.

**Speaker_00** [16:50:59]: So if it

**Speaker_04** [16:51:01]: is

**Speaker_00** [16:51:02]: hard to work remotely with everyone saying, oh, we will talk about it next time you are here.

**Speaker_00** [16:51:08]: It will be even harder when I'm on Mars.

**Speaker_00** [16:51:12]: But

**Speaker_03** [16:51:13]: Toby,

**Speaker_03** [16:51:21]: He's not gonna benefit from this if we give it to him two months from now.

**Speaker_04** [16:51:25]: No, of course

**Speaker_03** [16:51:26]: not.

**Speaker_03** [16:51:27]: So, up to you.

**Speaker_04** [16:51:29]: My intention was to get started running right away basically.

**Speaker_04** [16:51:34]: I have two urgent priorities tomorrow morning, but they weren't tackled then, and tomorrow I was expecting to have at least the first route done.

**Speaker_04** [16:51:40]: Perfect.

**Speaker_04** [16:51:41]: Yeah.

**Speaker_04** [16:51:41]: Perfect.

**Speaker_04** [16:51:42]: You know, when the head of investment banking comes down, you've got a head of the door, right?

**Speaker_04** [16:51:48]: Yep.

**Speaker_04** [16:51:50]: Yeah.

**Speaker_04** [16:51:51]: Also, I don't think it's going to be an entirely demanding task.

**Speaker_04** [16:51:55]: I think it's... I think it's quite possible to do a lot of it is going to be background processors and it's just going to be stepping into to basically act as a steward of it, right?

**Speaker_04** [16:52:09]: This is my understanding.

**Speaker_04** [16:52:10]: So,

**Speaker_03** [16:52:16]: I spoke with Nancy, Nancy

**Speaker_05** [16:52:19]: Gao,

**Speaker_03** [16:52:22]: and she delighted me with her remark that so many of the knowledge that resides with people in investment banking is not captured and then when they leave that knowledge leaves with them of relationships, of practices, of how you do deals and why certain things work and others not.

**Speaker_03** [16:52:53]: And she's very eager to be able to capture that.

**Speaker_03** [16:52:56]: So we agreed that I will create for her a very lean conversational template that first she can use and then she can see if in her group should also be adopted that basically allows anyone to just talk until relative to a given deal, their brain is empty.

**Speaker_03** [16:53:30]: And they don't know what else to say.

**Speaker_03** [16:53:33]: With the questions that are not from a preset list, but they are being born, they are being formulated by the AI conversational partner ad hoc, corresponding to what is specifically appropriate in that particular situation and I would hope that we will be able to use that experience and then extend

**Speaker_03** [16:54:12]: it to others as well.

**Speaker_03** [16:54:14]: Because, yes, a lot of it is back-end stuff, a lot of it is, I don't know, using Peach book well, a lot of it is finding the right investors or M&A or whatever it is.

**Speaker_03** [16:54:27]: But the reason why we know a lot of that is is because we don't know what we don't know.

**Speaker_03** [16:54:33]: We don't know what else is there.

**Speaker_03** [16:54:35]: And this approach potentially is able to offer a broader and deeper picture of what makes a banker successful, of what makes a deal move well and fast, a client excited and happy with the outcome and so on.

**Speaker_04** [16:54:58]: So this conversational, this conversation, this is going to range from deal specific to just general knowledge of the industry, of relationships.

**Speaker_04** [16:55:13]: What's the scope of these conversations?

**Speaker_03** [16:55:16]: So we did not decide on that with Nancy for the moment, but yes, it can be

**Speaker_04** [16:55:23]: both.

**Speaker_04** [16:55:25]: Yeah, I think it's very easy to see the immediate value of these conversations just the kind of reporting internal communications thing that people could at least have documented like if someone leaves a company but we still have a find then it's like instead of having to offer more that's very

**Speaker_04** [16:55:45]: useful.

**Speaker_04** [16:55:45]: And I could see that supporting Tony and Yvonne in these like weekly IB meetings too.

**Speaker_04** [16:55:53]: But I'm curious how you'd capture the industry knowledge.

**Speaker_04** [16:56:01]: I mean, not necessarily capturing it, but transferring it as

**Speaker_03** [16:56:08]: well.

**Speaker_03** [16:56:09]: There will be things that still remain outside of the coverage of these conversations for sure.

**Speaker_03** [16:56:17]: Yeah.

**Speaker_03** [16:56:18]: It doesn't have to be 100%.

**Speaker_03** [16:56:19]: Yeah.

**Speaker_03** [16:56:22]: And the second thing that we discussed with Nancy is that she said, I love the opportunity of using note takers.

**Speaker_03** [16:56:32]: And very simply, most of my meetings are such that we cannot use them because they are in person.

**Speaker_03** [16:56:38]: I cannot put my phone recording.

**Speaker_03** [16:56:40]: It would be very badly received.

**Speaker_03** [16:56:44]: And I have thick notebooks, because that is seen as normal of me just taking notes and I take a lot of notes.

**Speaker_03** [16:56:53]: So what I told her, which I think I told you as well a few times, is to take a photo and feed the photo to chat GPT.

**Speaker_03** [16:57:01]: And it is amazing, maybe not just one page, but three, four pages of how much it understands.

**Speaker_04** [16:57:13]: Yeah.

**Speaker_04** [16:57:15]: It did understand a favorite.

**Speaker_04** [16:57:19]: I admit that my handwriting might not be the best because there were big chunks that were struggle with,

**Unknown speaker** [16:57:25]: but...

**Speaker_04** [16:57:25]: Such as life.

**Speaker_03** [16:57:27]: And I don't know.

**Speaker_03** [16:57:28]: Nancy is probably writing in Chinese.

**Speaker_03** [16:57:30]: You know, it's not our problem.

**Speaker_03** [16:57:34]: And it doesn't have to be perfect, but if today 0% is transferred or close to 0% is kept from your notebooks, right?

**Speaker_03** [16:57:45]: Or it goes through your brain and then it goes into the computer back and forth in a separate loop.

**Speaker_03** [16:57:53]: then again being able to capture that is better.

**Speaker_03** [16:57:58]: A third point that is linked to this and it is giving us a segue to talk about knowledge management and as a subset of that about document management, if we don't have documents, what do you manage?

**Speaker_03** [16:58:18]: Because today we have a huge number of research PDFs that no one looks at.

**Speaker_03** [16:58:25]: We have a relatively small number of internally created documents that are mostly client facing.

**Speaker_03** [16:58:34]: And we have very, very, very few pieces of documentation about our own processes and our own ways of doing things.

**Speaker_03** [16:58:45]: And certainly we capture zero today of everyone's experience and everyone's relationships and everyone's networks and ways of doing things on an individual basis.

**Speaker_03** [16:58:59]: So what I want is for knowledge management to be the catalyst and these experiments to be the catalyst to make Aliwan a learning organization.

**Speaker_03** [16:59:18]: An organization that as such, as a corporate entity, as such is capable of learning, not only at the individual level.

**Speaker_03** [16:59:31]: And one that requires with or without AI is data.

**Speaker_03** [16:59:36]: You know, you cannot learn the water cooler, not the channel, but the physical water cooler is a great place to exchange gossip, but the organization learns zero just because people chit chat around the water cooler, right?

**Speaker_03** [16:59:55]: And we had a perfect example of how dangerous it is to close silos because they completely block opportunities not only to learn, even to communicate.

**Speaker_03** [17:00:15]: And I don't know if you are in the Abu Dhabi Finance Week channel?

**Speaker_04** [17:00:21]: Yeah, I saw

**Speaker_03** [17:00:23]: the whole thing.

**Speaker_03** [17:00:24]: That was the second example.

**Speaker_03** [17:00:27]: And I think I remarked Aliche today where she said, oh, I'm very interested about this, but let's take it private.

**Speaker_03** [17:00:42]: And I told her, no, let's not take it private.

**Speaker_03** [17:00:45]: Why do you want to deprive others to learn?

**Speaker_03** [17:00:50]: Why do you believe that you are interested and they should not be interested?

**Speaker_03** [17:00:56]: What is the advantage of not letting them have the opportunity to understand what the whole thing is about?

**Speaker_04** [17:01:06]: Yeah, I don't think it's necessarily like they're trying to deprive people, but I think it's a vulnerability.

**Speaker_04** [17:01:10]: Learning is a vulnerable thing for many people.

**Speaker_04** [17:01:12]: And I don't think they're particularly comfortable being vulnerable in public channels is my guess.

**Speaker_03** [17:01:19]: So they were told that they should be perfect and they should know everything right away, out of the

**Speaker_04** [17:01:25]: bed.

**Speaker_04** [17:01:27]: on that mindset irrespectively, whether it's rational.

**Speaker_04** [17:01:33]: So, so... But I mean, yeah, it's useful to have these learnings shared publicly.

**Speaker_04** [17:01:41]: I'm not trying to just to...

**Speaker_03** [17:01:42]: No, no, I understand that you are not saying that I am wrong.

**Speaker_03** [17:01:45]: You are trying to let me understand her point of view and her where she's coming from.

**Speaker_04** [17:01:51]: This is my guess as well.

**Speaker_04** [17:01:52]: I could be entirely mistaken.

**Speaker_03** [17:01:54]: Yeah.

**Speaker_03** [17:01:54]: Michael, for example, when I insistently and repeatedly tell him that we should not have this paranoid attitude, says that certain things are secret and that is fine, but then we should have an explicit classification of what is confidential and what is secret.

**Speaker_03** [17:02:16]: Otherwise people are confused.

**Speaker_03** [17:02:19]: Then the second thing that he says is that the noise impacts productivity because people are distracted and I vehemently disagree with that because one, we are not in a kindergarten, we are professionals, and two, you can mute a channel, or you can leave a channel.

**Speaker_03** [17:02:46]: as long as then you don't complain that you didn't know what was posted in the channel because you decided to leave it.

**Speaker_04** [17:02:52]: Yeah, but I think that's where the trouble is, right, is that there's a lot of information coming in and people need to be consuming all of it to make sure that they understand what's relevant to

**Unknown speaker** [17:03:02]: that.

**Speaker_03** [17:03:02]: No, no, for many reasons.

**Speaker_03** [17:03:05]: One, because the channels have a goal, and it is true that things should be posted where they belong.

**Speaker_03** [17:03:13]: That is where the context is relevant.

**Speaker_03** [17:03:16]: So when I am asked the question, I often say, okay, let's move the conversation to another channel, because it doesn't belong here, it belongs there.

**Speaker_03** [17:03:26]: And so that's one.

**Speaker_03** [17:03:29]: The second is, very recent, Slack introduced AI summaries of chance.

**Speaker_03** [17:03:36]: So you don't think you have time

**Speaker_05** [17:03:38]: to... Yeah.

**Speaker_03** [17:03:40]: You don't have you have time to follow every conversation?

**Speaker_03** [17:03:43]: Great.

**Speaker_03** [17:03:45]: Read the AI recap.

**Speaker_03** [17:03:47]: You don't trust the AI?

**Speaker_03** [17:03:49]: All right, then you invest the time to read every conversation.

**Speaker_03** [17:03:53]: You don't have the time, then you have to decide where you want to focus.

**Speaker_03** [17:03:58]: And that is not going to get better.

**Speaker_03** [17:04:00]: You know, pretending that short conversations shouldn't happen is not going to improve that.

**Speaker_03** [17:04:10]: There is an analytics dashboard on Slack.

**Speaker_04** [17:04:16]: Where is that, by the way?

**Speaker_04** [17:04:17]: I haven't,

**Speaker_03** [17:04:19]: is that

**Speaker_04** [17:04:20]: in the tools?

**Speaker_03** [17:04:20]: No, no, no, it's on the web interface.

**Speaker_03** [17:04:24]: and 90% of our conversations are in direct messages.

**Speaker_03** [17:04:30]: That's horrible.

**Speaker_03** [17:04:32]: That is exactly how not to use Slack.

**Speaker_03** [17:04:36]: We are paying thousands of dollars.

**Speaker_03** [17:04:39]: You know, we are paying a lot of money

**Speaker_05** [17:04:41]: to

**Speaker_03** [17:04:42]: use the tool as if it were WhatsApp.

**Speaker_04** [17:04:49]: Yeah.

**Speaker_04** [17:04:49]: Yeah.

**Speaker_04** [17:04:50]: I want to... I'll do this later.

**Speaker_04** [17:04:52]: I just wanted to, I'm going to close this because my computer and my device.

**Speaker_03** [17:04:55]: All right.

**Speaker_03** [17:04:56]: Okay.

**Speaker_03** [17:04:57]: So, knowledge management is only useful if we accept the necessity of becoming a learning organization.

**Speaker_03** [17:05:08]: If not, Knowledge is passive, is useless.

**Speaker_03** [17:05:16]: Knowledge is useful only if it is active, it is put at work.

**Speaker_03** [17:05:22]: And it can only be put at work, not by individuals, but by teams.

**Speaker_03** [17:05:28]: And teams that interface other teams, and that analyze are also self-aware and self-reflective, meaning that they are able to look at what they are doing and then ask themselves, can we do it better, and how, and why?

**Speaker_03** [17:05:53]: And that is only possible if data is

**Speaker_05** [17:05:58]: captured.

**Speaker_03** [17:06:01]: So that is the basis of knowledge management.

**Speaker_03** [17:06:05]: Now inside that document management, I am looking forward to seeing what you propose or what you think it should be or become.

**Speaker_03** [17:06:24]: But again, the question is being able to analyze

**Speaker_03** [17:06:34]: and to surface documents in the right context.

**Speaker_03** [17:06:45]: And that is not only making them searchable much better than Treasury it allows.

**Speaker_03** [17:06:55]: It is not only deciding whether they are obsolete and actively pulling them out so that you don't refer to 2024 report on US blockchain policies if in January 2025 it changed 180 degrees, right?

**Speaker_03** [17:07:20]: But it is also looking at our own documents and see them in evolution.

**Speaker_04** [17:07:33]: Can you elaborate on that?

**Speaker_03** [17:07:34]: Yes.

**Speaker_03** [17:07:43]: Whatever we are doing today is guaranteed not to be world class.

**Speaker_03** [17:07:50]: Okay?

**Speaker_03** [17:07:53]: But we want to fulfill our ambition to be playing in the Premier League, to be a world- class Abu Dhabi headquartered GCC focused full-service investment bank of the Merchant Bank tradition.

**Speaker_03** [17:08:19]: and I am proud of myself because I almost understand what that sentence means.

**Speaker_03** [17:08:29]: So in order to fulfill that ambition, it doesn't matter where we start.

**Speaker_03** [17:08:39]: whatever is the baseline where we are today, we can only improve if we document our processes, we look at the outcomes, we measure them, and we improve the processes, and those are through document management, knowledge management, people management, obviously.

**Speaker_03** [17:09:00]: And iteratively,

**Speaker_03** [17:09:07]: do better now how fast is the iteration so for example chidem told me that she has been accustomed to picking the tools and then a year later and a year later ask herself should we change or should we keep and that iteration to me means that in 10 years you have 10 opportunities to improve, as

**Speaker_03** [17:09:40]: opposed to doing it, I don't know, monthly, and in 10 years to have 120 opportunities to improve.

**Speaker_03** [17:09:52]: Well, the second may cost more, but the speed of improvement is much higher

**Speaker_05** [17:09:58]: too.

**Speaker_03** [17:10:01]: Also, too many of us may be feeling vulnerable, stop releasing drafts.

**Speaker_03** [17:10:12]: They feel like they cannot afford but to release a perfect output.

**Speaker_03** [17:10:18]: All right, with a client, sure.

**Speaker_03** [17:10:20]: You want to be proud of what you created.

**Speaker_03** [17:10:22]: But among us, being fast, And imperfect is much better than being slow and supposedly perfect.

**Speaker_03** [17:10:32]: It's not gonna be perfect anyway.

**Speaker_03** [17:10:34]: So let's at least be fast.

**Speaker_05** [17:10:37]: Yeah.

**Speaker_04** [17:10:46]: Yeah.

**Speaker_04** [17:10:46]: Yeah, I mean, the thing that I'm hearing from all of this, though, is it seems like moving forward,

**Speaker_03** [17:10:52]: there's a

**Speaker_04** [17:10:52]: pretty

**Speaker_00** [17:10:53]: strong idea of what needs to

**Speaker_04** [17:10:54]: happen,

**Speaker_00** [17:10:54]: which

**Speaker_04** [17:10:54]: is documenting the processes, which is observing the outcomes, which is iterating the process.

**Speaker_04** [17:11:00]: Well, it is just my idea, right?

**Speaker_04** [17:11:02]: Yeah, I cannot do it alone.

**Speaker_04** [17:11:03]: Yeah, well, which is what I was leading.

**Speaker_04** [17:11:07]: I mean, really the obstacle then is how are we getting people to do these things, right?

**Speaker_04** [17:11:12]: It seems like we're coming into a people management problem over a systems

**Speaker_03** [17:11:17]: problem.

**Speaker_03** [17:11:17]: Yes, so I wrote to Tracy saying, hey, I would like to learn from your experience in setting up some basic training in tools and how to use them for our team.

**Speaker_03** [17:11:35]: Amina chimed in saying it's not a priority.

**Speaker_03** [17:11:39]: Q2.

**Speaker_03** [17:11:43]: And that is in my opinion a horribly wrong answer.

**Speaker_03** [17:11:50]: Because even things that we have already decided are worth doing, like new team members announcing themselves in the water cooler channel and say who they are and what they do.

**Speaker_03** [17:12:04]: even those things were forgotten, like in a month.

**Speaker_03** [17:12:09]: And no one went and reinforced the message saying, hey, maybe if someone knew joins the team, they should say, I knew, this is what I do.

**Speaker_03** [17:12:25]: And so not only we are not learning, but we are regressing.

**Unknown speaker** [17:12:34]: So

**Speaker_03** [17:12:35]: yeah, I have my things cut out, which is good because, you know, otherwise I would be bored.

**Speaker_05** [17:12:49]: Yeah.

**Speaker_04** [17:13:13]: I was just thinking it's

**Unknown speaker** [17:13:15]: tricky.

**Speaker_03** [17:13:15]: Yeah, yeah, very tricky.

**Speaker_03** [17:13:17]: And a lot of organizations fail to embrace change, fail to benefit from new technologies, let alone AI.

**Speaker_03** [17:13:26]: You know, the reason why studies come out saying, oh, enterprises don't gain from AI.

**Speaker_03** [17:13:33]: Yeah, because they don't want to.

**Speaker_03** [17:13:35]: They actively close off themselves from the benefit they could gain if they opened up a bit more.

**Speaker_03** [17:13:46]: And then we do the survey.

**Speaker_03** [17:13:49]: Everyone uses AI.

**Speaker_03** [17:13:51]: Everyone.

**Speaker_03** [17:13:52]: I didn't show you the results.

**Speaker_03** [17:13:56]: I will, you know, 20 out of 50 field of survey, so that's okay, whatever, half of the people.

**Speaker_03** [17:14:08]: Yeah, let me say, pull it up on the phone, let me show it to you here.

**Speaker_03** [17:14:18]: Is it okay by the way if I go ahead and send Amina the knowledge management pod telling her that the document management pod will come a bit

**Speaker_05** [17:14:28]: later?

**Speaker_03** [17:14:44]: Here

**Speaker_03** [17:14:53]: if you want to scroll just from the top to the bottom.

**Speaker_03** [17:15:04]: And you know nothing earth shattering but still interesting.

**Speaker_03** [17:15:09]: of who responded, who didn't, because if you look at the divisions, it's not that I want to de-anonymize the form, which is anonymous, but still the distribution of responses is clear of what tools... Unsurprisingly, zero

**Speaker_04** [17:15:27]: from asset

**Speaker_03** [17:15:27]: management.

**Speaker_03** [17:15:29]: of what tools are being used and the last one is very interesting, which is what, it is the open answers, what stops people or what challenges they see in being productive.

**Speaker_03** [17:15:44]: Amazing.

**Speaker_03** [17:15:47]: One of us answered, oh, I'm not using transcriptions because I don't know if the company will reimburse it.

**Speaker_03** [17:15:55]: Did you ask the question?

**Speaker_03** [17:15:58]: probably they didn't dare asking the

**Speaker_04** [17:16:00]: question.

**Speaker_04** [17:16:24]: My kick is not working with calendar.

**Speaker_03** [17:16:28]: Sorry.

**Unknown speaker** [17:16:32]: I don't let

**Speaker_03** [17:16:32]: anyone laugh.

**Speaker_03** [17:16:32]: It did, but now it doesn't.

**Speaker_04** [17:16:45]: Three people said they use it for coding assistance.

**Speaker_04** [17:16:48]: Yeah, amazing, right?

**Speaker_01** [17:16:55]: I have my suspicions.

**Speaker_01** [17:16:58]: No,

**Speaker_04** [17:17:00]: she doesn't code.

**Speaker_04** [17:17:00]: So I think she codes.

**Speaker_01** [17:17:02]: Well, I don't know.

**Speaker_01** [17:17:05]: She's not coding here.

**Speaker_01** [17:17:06]: She's busy resetting people's classrooms.

**Speaker_04** [17:17:13]: Who do you suspect?

**Speaker_04** [17:17:15]: Who are the secret coders among us?

**Speaker_04** [17:17:16]: Hella.

**Speaker_04** [17:17:17]: Hella?

**Speaker_04** [17:17:18]: Coding?

**Speaker_04** [17:17:19]: No way.

**Speaker_04** [17:17:20]: You reckon?

**Speaker_04** [17:17:21]: I think so.

**Speaker_04** [17:17:25]: Maybe.

**Speaker_04** [17:17:26]: She's got layers that hello.

**Speaker_04** [17:17:31]: Interesting.

**Speaker_04** [17:17:32]: Everyone is this chatty

**Unknown speaker** [17:17:36]: good

**Speaker_00** [17:17:36]: to you.

**Speaker_00** [17:17:37]: And I think I answered the survey twice, so the other two is more.

**Speaker_00** [17:17:42]: Okay.

**Speaker_03** [17:17:42]: That makes sense.

**Unknown speaker** [17:17:44]: That makes

**Speaker_03** [17:17:44]: sense.

**Speaker_03** [17:17:45]: But did you, by the way, did you fill the form?

**Speaker_03** [17:17:47]: I did, yeah.

**Speaker_04** [17:17:48]: I thought you'd, I thought I accidentally de-anonymized myself with my answer.

**Speaker_04** [17:17:53]: Let me see if I...

**Speaker_00** [17:17:54]: The New York team said, hey, the New York team.

**Speaker_03** [17:17:57]: So that's easy.

**Speaker_03** [17:17:59]: Even though it's not correlated to the rest, oh, maybe it is.

**Speaker_03** [17:18:03]: I don't know, doesn't matter.

**Speaker_03** [17:18:04]: The point is not finding who said what.

**Speaker_03** [17:18:07]: Yeah.

**Speaker_03** [17:18:29]: What is that?

**Speaker_03** [17:18:30]: It looks good.

**Speaker_03** [17:18:31]: It's sweet, not too sweet.

**Speaker_03** [17:18:34]: It's like a macho touch.

**Speaker_03** [17:18:35]: Yes, correct.

**Speaker_04** [17:18:42]: I have no recollection of what productivity challenges I face.

**Speaker_04** [17:18:47]: Well, what I wrote.

**Speaker_04** [17:18:51]: Well, it was optional,

**Speaker_02** [17:18:52]: so

**Speaker_03** [17:18:52]: not

**Speaker_04** [17:18:52]: everyone filled it.

**Speaker_04** [17:18:53]: I'm pretty sure I did fill it in, because I remember thinking I might have given myself away with my answer, but clearly

**Unknown speaker** [17:18:59]: not.

**Speaker_04** [17:19:00]: Just

**Speaker_03** [17:19:03]: go

**Speaker_03** [17:19:09]: in the survey is to also let everyone understand.

**Speaker_03** [17:19:15]: Also to let everyone understand that we have the same challenges, we have the same desire to find solutions that we are adopting them, even if we don't tell each other about it.

**Speaker_03** [17:19:30]: Like seven people use Kamba.

**Speaker_03** [17:19:33]: It's great, Kamba is great, let's use it more, right?

**Speaker_03** [17:19:37]: Et cetera.

**Speaker_04** [17:19:48]: Okay.

**Speaker_04** [17:19:50]: What do you have any thing you've got to

**Speaker_03** [17:19:54]: turn out?

**Speaker_03** [17:19:54]: No, depending on what we want to do.

**Speaker_03** [17:19:56]: I'm hungry too.

**Speaker_04** [17:19:57]: Yeah.

**Speaker_04** [17:19:58]: I was going to ask you what your thoughts are on how... I mean, like, I know you had your secret.

**Speaker_00** [17:20:09]: Oh, I have more, more secret plans.

**Speaker_00** [17:20:12]: Oh, yeah, yeah.

**Speaker_00** [17:20:13]: I have, I, as soon as... You're not so secret, secret

**Speaker_03** [17:20:16]: plans, as soon as... You know about labs, right?

**Speaker_03** [17:20:21]: Labs?

**Speaker_03** [17:20:22]: Only one labs.

**Speaker_04** [17:20:24]: Oh, yeah.

**Speaker_03** [17:20:25]: The dashboard and the sandbox.

**Speaker_03** [17:20:28]: So that was the last one.

**Speaker_03** [17:20:30]: And my next secret plan... But I will tell you about it, but what was your question?

**Speaker_04** [17:20:36]: I was just going to

**Unknown speaker** [17:20:42]: think.

**Speaker_04** [17:20:44]: I'm trying to work out how best of crazy.

**Speaker_04** [17:20:47]: In terms of getting the uptake, in terms of shifting this mentality to, because what's the learning organization thing?

**Speaker_03** [17:20:55]: That's

**Speaker_04** [17:20:55]: right.

**Speaker_04** [17:20:55]: What, like, are you like just banging your head against the wall?

**Speaker_04** [17:21:00]: Do you have, like, ideas?

**Speaker_04** [17:21:02]: Do you see it as, like, outside your responsibility or...

**Speaker_03** [17:21:05]: So, what are you... I'm lazy.

**Speaker_03** [17:21:07]: So I don't fight wars that I cannot win.

**Speaker_03** [17:21:12]: I always find or always search for easy ways to achieve what I want.

**Speaker_00** [17:21:21]: Now.

**Speaker_00** [17:21:22]: 20 years

**Speaker_03** [17:21:22]: ago, right?

**Speaker_03** [17:21:26]: I have my own thoughts about that, but and just to make the remark, whenever you say 2080, adding up to 100, where the 20 and the 80 are uncorrelated dimensions in reality, it means that it's bullshit.

**Speaker_03** [17:21:53]: It should be 70, 40, or it should be 90, 30, or whatever it is.

**Speaker_03** [17:21:59]: There's absolutely no reason for it to add up to 100. If it adds up to 100, it means the person who is still talking about it does not understand what is the underlying principle.

**Speaker_03** [17:22:14]: But

**Speaker_01** [17:22:14]: it doesn't

**Speaker_03** [17:22:14]: matter.

**Speaker_00** [17:22:15]: It's an aside.

**Speaker_03** [17:22:16]: It's an aside.

**Speaker_03** [17:22:21]: So looking for... easier wins than not banging your head against the wall.

**Speaker_03** [17:22:29]: I am lucky that Michael and Amy are supporting, you know, everything what I do in the sense that they know that I will, by definition, make trouble.

**Speaker_03** [17:22:47]: And the question is also only, it is good trouble or bad trouble.

**Speaker_03** [17:22:52]: That's the only question.

**Speaker_03** [17:22:54]: That there will be some degree of discomfort in others seeing me challenging them, that's a given.

**Speaker_03** [17:23:04]: That is unavoidable, and that's fine.

**Speaker_03** [17:23:07]: But is it gonna be constructive?

**Speaker_03** [17:23:10]: Are they gonna feel pushed to improve, or are they gonna feel that I should go and die in a ditch.

**Speaker_04** [17:23:21]: Sometimes

**Speaker_03** [17:23:22]: both,

**Speaker_04** [17:23:23]: same

**Speaker_03** [17:23:24]: problem.

**Speaker_03** [17:23:26]: So, so,

**Speaker_03** [17:23:33]: that is why these various AI champions are so wonderful, because they self-select to be experimenters.

**Speaker_03** [17:23:45]: However, there are some that by their role are gatekeepers.

**Speaker_03** [17:23:55]: And Tracy is by her role a gatekeeper, some of it perfectly reasonable.

**Speaker_03** [17:24:03]: Like, I don't know, HR complaints shouldn't be in the team's old channel.

**Speaker_03** [17:24:11]: or salary data in some organizations is openly shared and it's unavoidably leading to political bullshit because people are jealous or they feel they should earn more or less or whatever.

**Speaker_03** [17:24:28]: So in that sense, her role as a gatekeeper is absolutely a given.

**Speaker_03** [17:24:35]: In other ways, it shouldn't be like the example I gave, when someone comes on board as new, they should receive a list of things that can be easily complemented by things that Tracy didn't think of.

**Speaker_03** [17:24:54]: And when I dared to suggest some of them, she got very upset.

**Speaker_03** [17:24:59]: And I am sad for having made her upset, But I will just try and achieve the same goal in some other way, because yeah, people should be using Slack, and we have been using Slack less and less.

**Speaker_03** [17:25:21]: What's her name?

**Speaker_03** [17:25:23]: Stephanie, for example, sends emails to not even using Ali 1-0, the the the but but but but she puts the name of everyone on the on the two no that was what that is what you did in you know 30 years ago or or we have now a form with with dashes to ask for leave for vacation that you are supposed to

**Speaker_03** [17:25:56]: print, filled with a pen and then have two people sign, you sign it, and then your manager signs it.

**Speaker_03** [17:26:04]: That is from the 60s.

**Speaker_03** [17:26:07]: And I can already see carbon copies, you know, physical carbon copies.

**Speaker_03** [17:26:12]: No.

**Speaker_03** [17:26:14]: And another gatekeeper, by definition, because that is her role, is Amina.

**Speaker_03** [17:26:24]: but that shouldn't mean when I say I want to do X that she says no you shouldn't do it because I don't report to her she should channel and she should you know find what works not what is not She should find ways to make things work, not find ways to make things stop.

**Speaker_03** [17:27:01]: And I don't know her, so I don't know her challenges.

**Speaker_03** [17:27:04]: I don't know.

**Speaker_03** [17:27:05]: We had a conversation and unfortunately, half of the time, what she said was, and all that good stuff.

**Speaker_03** [17:27:20]: Like I would ask her, okay, tell me, this is what I do, tell me a bit what you do.

**Speaker_03** [17:27:25]: And she'll say, oh yeah, and all that good stuff.

**Speaker_03** [17:27:31]: That means nothing.

**Speaker_03** [17:27:33]: So I don't know what she does.

**Speaker_04** [17:27:42]: Sounds like you're having a lot of

**Unknown speaker** [17:27:44]: fun.

**Speaker_00** [17:27:46]: under

**Speaker_03** [17:27:47]: under many definitions of fun, yes.

**Speaker_03** [17:27:50]: Yeah,

**Speaker_04** [17:27:50]: yes.

**Speaker_03** [17:27:51]: And absolutely, it's a beautiful challenge.

**Speaker_03** [17:27:58]: And, you know, I'm not planning not to keep trying my best.

**Speaker_03** [17:28:10]: You know, that is the thing, small or large.

**Speaker_03** [17:28:16]: I am not able to not to give a fuck.

**Speaker_03** [17:28:25]: I give a fuck.

**Speaker_03** [17:28:27]: I care about it.

**Speaker_03** [17:28:29]: And if someone says, oh, but that's not your, it's not in your job description.

**Speaker_03** [17:28:40]: that makes me care twice as much?

**Speaker_03** [17:28:42]: No, no it doesn't, but that is not an answer that works for me, right?

**Speaker_03** [17:28:52]: Just a stupid episode yesterday.

**Speaker_03** [17:29:00]: The flyer that we printed

**Speaker_04** [17:29:06]: The flyer reprinted

**Speaker_03** [17:29:08]: for the... Self- launch?

**Speaker_03** [17:29:10]: No.

**Speaker_03** [17:29:12]: For this coming week.

**Speaker_03** [17:29:14]: Did you see that?

**Speaker_04** [17:29:15]: No, I haven't seen it.

**Speaker_04** [17:29:16]: Was this in a channel or

**Speaker_03** [17:29:17]: something?

**Speaker_03** [17:29:17]: In one or the other of the channels or both.

**Speaker_03** [17:29:19]: Doesn't matter.

**Speaker_04** [17:29:20]: This was yesterday.

**Speaker_03** [17:29:22]: Yesterday or the day before yesterday.

**Speaker_03** [17:29:25]: Yeah, no, it wasn't on Saturday.

**Speaker_03** [17:29:26]: It was on Friday.

**Speaker_03** [17:29:27]: Okay.

**Speaker_03** [17:29:29]: The flyer says... Interestingly enough, it mentions for the first time investment bank.

**Speaker_03** [17:29:36]: So I was surprised and pleasantly surprised.

**Speaker_03** [17:29:39]: Not sure it's perfect, and it's really because... Anyway, great, it says investment bank, and it says book a meeting and it has two QR codes.

**Speaker_03** [17:29:53]: One of the two doesn't work.

**Speaker_01** [17:29:58]: It just doesn't work.

**Speaker_01** [17:29:59]: Why two QR codes?

**Speaker_00** [17:30:01]: the two meeting rooms.

**Speaker_00** [17:30:05]: So you, as our potential client, have to decide, do I want to have the 25th floor meeting or the 12th floor

**Speaker_05** [17:30:14]: meeting?

**Speaker_05** [17:30:16]: No,

**Speaker_03** [17:30:18]: no, you should laugh, absolutely.

**Speaker_03** [17:30:22]: Or another silly episode.

**Speaker_03** [17:30:26]: Did you notice that our only one all email is misspelled?

**Speaker_03** [17:30:35]: No.

**Speaker_03** [17:30:35]: The email address is correct, but the display name says only one with one L.

**Unknown speaker** [17:30:47]: Really?

**Unknown speaker** [17:30:53]: Yeah.

**Speaker_03** [17:30:54]: So I told Chidem that it should be changed and she said, oh, I have other priorities.

**Speaker_03** [17:30:58]: And I told her, well, I'm not saying you should do it right away, but we should change it.

**Speaker_03** [17:31:05]: And I set up a task in a sauna and she closed the task without changing the display name.

**Speaker_03** [17:31:11]: So I reopened the task.

**Speaker_03** [17:31:16]: And

**Speaker_05** [17:31:16]: I said,

**Speaker_03** [17:31:18]: and I

**Speaker_00** [17:31:18]: said, well,

**Speaker_03** [17:31:20]: you know, yes, it's not a priority, but it's still, you know, can't, at what level of sloppiness can we afford to operate?

**Speaker_03** [17:31:27]: Is losing client funds the level that we can afford?

**Speaker_03** [17:31:31]: Probably not, all right, so we are not going to lose client funds, but evidently we can afford not to spell our own fucking name right, So we will be sloppier than that.

**Speaker_03** [17:31:43]: Evidently we can afford not to check the QR code of something that we go to print with.

**Speaker_04** [17:31:49]: It was already printed?

**Speaker_04** [17:31:50]: Yeah.

**Speaker_03** [17:31:52]: Yeah.

**Speaker_03** [17:31:56]: So attention to detail and professional care is something that as a learning organization we should be happy that there's a fucking jerk like David that is not giving up and just relentless about it.

**Speaker_03** [17:32:21]: And I want the same about me.

**Speaker_03** [17:32:23]: You know, I want people to come and push me against the wall and say, hey David, you are such a little fucking perfectionist.

**Speaker_03** [17:32:33]: Did you see blah blah blah blah blah that you produced?

**Speaker_03** [17:32:40]: Yeah.

**Speaker_03** [17:32:40]: And no one even comes to me because either they don't even look at what I produce or they look at it and then they forget about it and they or they look at it and there is something that is not okay and then they don't tell me about it and none of those three things is fine

**Speaker_03** [17:33:16]: but yes I am having a lot of fun with all of that because it's it's grungy yeah it's it's it's part of being human

**Speaker_04** [17:33:28]: yeah

**Speaker_03** [17:33:29]: oh yeah it's it's we are we are smelly we are imperfect we are political and then is this a good segue for our philosophy that's right let's do that

**Speaker_04** [17:33:46]: we ask

**Unknown speaker** [17:33:47]: what

---
*Backed up from MeetGeek on 2026-03-30 08:51*
