# Sjors / David Sync

**Date:** 2025-10-06
**Duration:** Unknown
**Meeting ID:** 26f2d0e4-be8d-4092-a37c-a53d6a57e74c

## Participants
- *Participants not listed*

### Summary

The meeting focused on several key areas, including event participation insights for Jitex and North Star, with an emphasis on local government interactions. David aims to enhance efficiency by automating Randy's workflow using AI processes from Shores and will follow up on Randy's meeting with Michael. Discussions on integrating Kong with Cloud Code highlighted challenges with Kong's developer-centric approach and the need to revisit tools like GROC for better performance. Sjors expressed difficulties with non-intuitive triggers in flow design, while David will assist him in developing a workflow automation using Python scripts. The conversation also addressed the costs of cloud services like AWS and Azure, leading to a decision to explore local solutions. Additionally, the need for a minimalistic approach to automation was agreed upon, with David tasked to document the automation process at two levels of abstraction and to investigate OpenAI's API for potential automation applications.

## Full Transcript

**Unknown speaker** [09:00:56]: Pizza with friends.

**Sjors Bogers** [09:01:00]: catching up on the last Italy time.

**Sjors Bogers** [09:01:04]: Yes.

**David Orban** [09:01:08]: And on Saturday I'm flying back.

**Sjors Bogers** [09:01:15]: To go to events or?

**David Orban** [09:01:17]: Yeah, just attending Jitex and North Star and then spending a few days in Abu Dhabi and then back.

**David Orban** [09:01:27]: When you do, make sure you look at Luma.

**Sjors Bogers** [09:01:31]: There's a lot of side events that might be interesting.

**Sjors Bogers** [09:01:34]: Oh, Luma.

**David Orban** [09:01:37]: But does Luma list events publicly?

**David Orban** [09:01:40]: It does, if it wants to invite people.

**Sjors Bogers** [09:01:45]: So you can search by date and location.

**David Orban** [09:01:50]: Yeah.

**David Orban** [09:01:50]: I never checked.

**David Orban** [09:01:53]: Okay, very good.

**David Orban** [09:01:54]: And there's a few from Enacta Ventures.

**Sjors Bogers** [09:01:58]: I think they're from Crypto Oasis.

**Sjors Bogers** [09:02:02]: And last year when we were there with Adrian and Brad, we had a couple of them that were quite good, maybe not for the presenters, but there's also something in my throat.

**Sjors Bogers** [09:02:17]: There's also quite a few people from local government that post at their venues, and those might be interesting to meet.

**David Orban** [09:02:27]: Talking about government, Abu Dhabi just announced a project with, I don't know how much money, a lot of money.

**David Orban** [09:02:37]: to make the UAE government AI native by 2027. Okay.

**David Orban** [09:02:47]: That's very interesting.

**Sjors Bogers** [09:02:52]: Yeah.

**David Orban** [09:02:53]: They saw the Albanian minister and they said, no, we have to be better.

**David Orban** [09:03:01]: One minister, all the ministers.

**David Orban** [09:03:06]: I just sent you the link from in Okta.

**Sjors Bogers** [09:03:08]: But they have a lot of events, at least last year they did it.

**Sjors Bogers** [09:03:13]: And this morning I already saw it too.

**David Orban** [09:03:17]: If you still have access to the Beyond Drive, can I ask you to download the event guide that I created how to participate in events?

**David Orban** [09:03:30]: Yeah.

**Sjors Bogers** [09:03:31]: Can you try and locate it right away before we forget?

**David Orban** [09:03:34]: Yeah.

**David Orban** [09:03:39]: We also had a blog post about it, but.

**David Orban** [09:04:26]: What was the title, is participate in events?

**Sjors Bogers** [09:04:31]: Yeah, something like that.

**David Orban** [09:04:38]: David's conference participation experience.

**Sjors Bogers** [09:04:43]: Could be, yeah.

**David Orban** [09:04:45]: Oh, yeah.

**David Orban** [09:04:46]: Yeah, think that's the one.

**David Orban** [09:04:49]: Yeah, if you download it as Microsoft Word, then you can just drop it over somewhere, anywhere.

**David Orban** [09:05:05]: Yeah.

**David Orban** [09:05:05]: I'll do it right away.

**Sjors Bogers** [09:05:40]: Just send it over to your personal email.

**Sjors Bogers** [09:05:44]: Okay, thank you.

**David Orban** [09:05:55]: So did you have a chance to look at the NADM project I shared with you.

**David Orban** [09:06:00]: Before we talk about that, let's talk about the more important thing, which is that I spoke to Randy yesterday.

**David Orban** [09:06:08]: And he confirmed that he will have a meeting with Michael today, where he will not go and say, let's hire Shores.

**David Orban** [09:06:19]: What he will say is, thanks to these processes, I'm doubling my capacity of handling clients.

**David Orban** [09:06:31]: And then Michael will ask, wow, and what are these processes?

**David Orban** [09:06:35]: Well, they are the AI processes developed by Shores.

**David Orban** [09:06:39]: That's it.

**David Orban** [09:06:41]: So I will ask him later today or tomorrow how the meeting went.

**David Orban** [09:06:48]: And then I will ask him to please do the same with serving.

**David Orban** [09:06:54]: Yeah.

**David Orban** [09:06:57]: Okay.

**David Orban** [09:06:57]: Okay.

**David Orban** [09:06:58]: Okay.

**David Orban** [09:06:58]: Now we can talk about NA10.

**David Orban** [09:07:02]: No, I didn't have the time to look what you did.

**David Orban** [09:07:08]: The fact that you are frustrated is very valuable because you are developing a better understanding of what are the limits of the tools that are purported to be good, but stuck big time.

**David Orban** [09:07:27]: And then you will be better able to appreciate their evolution, whether by an A10 itself or as it is expected, being announced by OpenAI tonight, right?

**David Orban** [09:07:43]: And our aspiration to be able to automate the workflow for Randy is that.

**David Orban** [09:07:59]: It's an aspiration.

**David Orban** [09:08:01]: We have to work towards it, but if we that the tools are not yet where we need them to be, that's okay.

**David Orban** [09:08:13]: I'm sure they are, right?

**David Orban** [09:08:16]: Whatever difficulty you are having with an A10, and I can dislike the tool, it doesn't mean that it cannot do what we want to do.

**David Orban** [09:08:25]: It can, it's sure.

**David Orban** [09:08:27]: Yeah, it's more likely the learning curve, right?

**Sjors Bogers** [09:08:29]: Yes, yeah.

**David Orban** [09:08:32]: The way of thinking.

**Sjors Bogers** [09:08:33]: Yes.

**David Orban** [09:08:37]: And also, you know, these tools are kind of a,

**David Orban** [09:08:50]: like a crutch.

**David Orban** [09:09:08]: as well.

**David Orban** [09:09:10]: The URL is Konghq.com.

**David Orban** [09:09:17]: And that is the real deal.

**David Orban** [09:09:25]: Because NA10 pretends to hide the complexity, but It is not able to and whatever it makes easy, it is not the substance, it's only the surface.

**David Orban** [09:09:46]: Oh, you can draw a line from one box to the next, big deal.

**David Orban** [09:09:51]: It's not the WYSIWYG editor that matters.

**David Orban** [09:09:53]: What matters is what can be done, right?

**David Orban** [09:09:57]: So obviously, and I don't know, maybe NA10 has an API, and I'm just being a snob, but Kong doesn't pretend to make it easy.

**David Orban** [09:10:14]: It is unabashedly geared towards developers, and we are developers using cloud code.

**David Orban** [09:10:25]: and telling Cloud Code, this is what I want to do, using the Kong documentation, work out how I should be going about it, and then set up the scaffolding, installing all the tools, blah, blah, blah, blah.

**David Orban** [09:10:43]: One of the things that I don't remember if we discussed in the past, is that it can be extremely useful to tell the platform cloud code, for example, or warp.

**David Orban** [09:10:57]: If you haven't started using warp yet, you should.

**David Orban** [09:11:03]: install the click, the command line interface.

**David Orban** [09:11:11]: this has been such a historical mistake.

**David Orban** [09:11:15]: We should have started calling it the command line interface tool so that we could say install the clit.

**David Orban** [09:11:23]: And so regardless of that huge mistake, and I'm laughing because the AI transcript will not have the common sense of understanding that I'm joking, it will take it seriously.

**David Orban** [09:11:42]: Anyway.

**David Orban** [09:11:44]: see another problem.

**Sjors Bogers** [09:11:46]: Since most developers are male, they will not be able to find right?

**Sjors Bogers** [09:11:50]: That's right.

**David Orban** [09:11:53]: So the opportunity of installing the common line interface, which supercharges the use of the remote tool because then the cloud code, for example, can just say, okay, what are the help, what is the help available in the common line interface, what are the parameters for invoking it, and then it

**David Orban** [09:12:30]: works on the remote thing using the local tool, very, very fast.

**David Orban** [09:12:34]: Oh, by the way, talking about fast, And, and, you know, revisiting the tools all the time is healthy.

**David Orban** [09:12:45]: So yesterday I revisited, I revisited

**David Orban** [09:12:53]: WindSurf, which I have been using as an interface, but not as an agent.

**David Orban** [09:13:02]: And the default now is GROC.

**David Orban** [09:13:07]: And in particular, GROC, fast one.

**David Orban** [09:13:14]: And the fact that it is fast is so good because it is very fast.

**David Orban** [09:13:23]: You know, just subjectively, four or five times faster than anything else.

**David Orban** [09:13:28]: So I had fun vibe coding this little website that is actually hosted on GitHub just like this one.

**David Orban** [09:13:52]: So both of these are serving a very narrow specific purpose.

**David Orban** [09:14:00]: This is the AI paradox report.

**David Orban** [09:14:04]: This is the jolting paradox.

**David Orban** [09:14:09]: So everything is a paradox.

**David Orban** [09:14:11]: Jolting technologies article.

**David Orban** [09:14:16]: And it was a lot of fun doing it with GROC inside windsurf.

**David Orban** [09:14:28]: Okay.

**David Orban** [09:14:29]: So... Really, really good.

**David Orban** [09:14:31]: Oh, and they are, I don't know if they already or they are about to release a version of GROC with one or two million tokens context window.

**David Orban** [09:14:46]: So very large repositories can be added to it.

**David Orban** [09:14:58]: And I don't know if I mentioned to you, but talking about, you know, the basis, not the basis.

**David Orban** [09:15:06]: I triumphally declared that the jolting technologies hypothesis has been confirmed when Matter said that they measured rather than seven or four months doubling time for agents.

**David Orban** [09:15:24]: And I don't remember what their measurement was at the time but last week with the release of plot sonnet 4.5 there was just a little remark by entropic that they did some development work and Sonnet kept working on it for 30 hours so in the chart where matter talks about what results they have i

**David Orban** [09:16:13]: i don't know

**David Orban** [09:16:19]: where that 30 hours would be because these are minutes Time horizon in minutes.

**David Orban** [09:16:28]: So the top is about 100 minutes, which is less than two hours.

**David Orban** [09:16:33]: And now we are talking about 30 hours.

**David Orban** [09:16:35]: So it's bomb way up.

**David Orban** [09:16:42]: So what we were talking about is closing all the parentheses, revisiting tools because it's worth it.

**David Orban** [09:16:55]: installing command line interfaces because they are easy to use for the tools and checking out Kong if it can be a more dignified and honest tool to use as opposed to an A10.

**David Orban** [09:17:27]: Okay.

**David Orban** [09:17:28]: Yep, that's clear.

**Sjors Bogers** [09:17:30]: Do you want to look at the flows I came up with?

**Sjors Bogers** [09:17:34]: Yes, let's look together.

**David Orban** [09:17:35]: Okay.

**David Orban** [09:17:39]: Should you share the window?

**David Orban** [09:17:41]: Yeah, working

**Sjors Bogers** [09:17:49]: Let me see, let me know if I need to zoom in on something or can you read it already?

**David Orban** [09:17:56]: No, I cannot read it except for the largest.

**David Orban** [09:18:01]: Now I can, yes.

**Multiple speakers** [09:18:04]: So the logic I took here is we need a trigger, right?

**Sjors Bogers** [09:18:09]: But the triggers that they offer are not super intuitive for me.

**Sjors Bogers** [09:18:14]: So I took the simple one to just click and execute the flow that I designed.

**Sjors Bogers** [09:18:21]: Then it needs to find the client data in wherever we're going to store it.

**Sjors Bogers** [09:18:28]: So for now I chose Google Drive, right?

**Sjors Bogers** [09:18:30]: So I have access to But that's already where the first thing that's unusual to me starts, because me thinking about it humanly, you would say you go into the folder and you download everything that's in the folder, select all, and then drag it into the AI agent, right?

**Sjors Bogers** [09:18:50]: But that's already separated into two nodes.

**Sjors Bogers** [09:18:52]: So one needs to list and find the folder, and then search what is in the folder, and then another note needs to download what has been listed.

**Sjors Bogers** [09:19:02]: So these type of translation things I have to make for every little step.

**Sjors Bogers** [09:19:09]: And that cause a lot of frustration and learning curve already.

**Sjors Bogers** [09:19:14]: Maybe I can show you how granular it is, so you have an idea.

**Sjors Bogers** [09:19:23]: You go for Google Drive.

**Sjors Bogers** [09:19:26]: And then you see all these actions already, right?

**Sjors Bogers** [09:19:31]: Yes.

**Sjors Bogers** [09:19:32]: And it's not always clear which one you should take.

**Sjors Bogers** [09:19:37]: And then once you pick one, you need to set all the parameters.

**Sjors Bogers** [09:19:44]: And again, that is also not very intuitive most of the times, especially when things are split up a certain way.

**Sjors Bogers** [09:19:51]: And even if you ask clause, for example, It gives very confusing information.

**Sjors Bogers** [09:19:58]: I did it first with just text, completely different interfaces talking about listing things that don't even exist.

**Sjors Bogers** [09:20:04]: So then I give it the screenshots and it's still rather confusing.

**David Orban** [09:20:09]: Okay, so this is important because I was about to stop you and tell you the way I would have gone about the objective is to search if there is an API for an A10, and it is, and there is, And it says, using NA10's public API, you can programmatically perform the same tasks as you can in the graphical

**David Orban** [09:20:38]: user interface.

**David Orban** [09:20:40]: And then there is a documentation.

**Multiple speakers** [09:20:43]: So is that what you tried to use with Claude?

**David Orban** [09:20:47]: Yeah, that's the first thing I So first I installed the NA10 MCP.

**Sjors Bogers** [09:20:53]: So I can use the cloud desk code to create whatever I just did manually, what I just showed you, right?

**Sjors Bogers** [09:21:01]: So then it goes through all my prompting and then gives a design and that's JSON code, and I just paste it in and then the flow appears in any time.

**Sjors Bogers** [09:21:14]: Okay, and it didn't work.

**David Orban** [09:21:16]: Now, using the MCP is not the same as using the API.

**David Orban** [09:21:24]: Okay.

**David Orban** [09:21:26]: I mean, ideally it should be But the flexibility of the MCP comes at the cost of subtle misunderstandings between the two translations, one from your natural language into what the LLM understands, and then from the MCP to the calls that it makes remotely to the MCP server on the other side.

**David Orban** [09:21:51]: The API has the cost of being harder to learn But once you debug the API calls, it is deterministic.

**David Orban** [09:22:06]: Now, given that you don't need to learn the API because you tell the LLM what you want to do using the API.

**David Orban** [09:22:22]: But we can go back to your workflow as long as you, unless you feel necessary, move beyond sharing your frustration just concentrate what you accomplished.

**David Orban** [09:22:39]: Yeah, and that's the problem.

**Multiple speakers** [09:22:40]: I didn't accomplish much.

**Sjors Bogers** [09:22:42]: I've been looking at over the weekend in chunks of several hours until I got so frustrated that I didn't want to do it anymore?

**Sjors Bogers** [09:22:50]: Okay.

**Multiple speakers** [09:22:51]: That's something else I went Do you believe that the lack of results is due to this learning curve?

**David Orban** [09:23:05]: Would you agree that it cannot be due to the limitation

**David Orban** [09:23:28]: NA10 workflow repositories in GitHub, where you may find something that is 80% what you need and then adapt Yeah, I look for those, but I couldn't find something that could understandably make work for us.

**Sjors Bogers** [09:23:48]: So that's why after all the work I did, I tried to start, how would I design it, and then compare it with the tutorials and see if that makes sense.

**Sjors Bogers** [09:23:58]: That's how I came up with these things, whatever I did with Claude, it didn't even remotely look at these things and these are the way that also within n8n they suggest certain setups and the ones i designed look far more similar to the ones that cloud created that was just one big line no agent in

**Sjors Bogers** [09:24:20]: it for example and was much more code based it seemed and of course with with code triggers you can also code the whole thing together but yeah absolutely and And we shouldn't shy away from using quotation marks primitive tools, because I'm already suspicious of N8N's rebranding itself to ride a

**David Orban** [09:24:50]: wave of AI agents.

**David Orban** [09:24:52]: It's a workflow automation tool.

**David Orban** [09:24:55]: So having Python scripts automating what we want to do, is more honest, perfectly fine.

**Sjors Bogers** [09:25:08]: The last Okay.

**Sjors Bogers** [09:25:09]: That's great.

**Sjors Bogers** [09:25:09]: I couldn't hear you.

**Multiple speakers** [09:25:12]: Yeah, I don't know why screen is very slow.

**David Orban** [09:25:18]: Probably the computer is having a hard time.

**David Orban** [09:25:24]: Let me join from the other one.

**David Orban** [09:25:27]: Okay.

**David Orban** [09:25:27]: I leave here and join there.

**David Orban** [09:25:47]: Um,

**David Orban** [09:26:07]: you can see me right, even though I cannot see myself, doesn't matter, but just ask.

**David Orban** [09:26:12]: No, there's no video.

**Sjors Bogers** [09:26:16]: Okay.

**David Orban** [09:26:18]: Let's see.

**David Orban** [09:26:19]: All right.

**David Orban** [09:26:20]: There should be.

**David Orban** [09:26:21]: It doesn't matter.

**David Orban** [09:26:22]: Oh, now there is.

**Multiple speakers** [09:26:26]: So the one you see now.

**David Orban** [09:26:30]: Sorry, just to finish, because you said you couldn't hear what I was saying is that doing with Python scripts, honestly, what NA10 dishonestly labels AI agents while it is a simple workflow automation is perfectly fine.

**Sjors Bogers** [09:26:59]: Okay.

**Sjors Bogers** [09:27:00]: The one you're looking at right now is one that cloud created based on my prompts.

**Sjors Bogers** [09:27:07]: But yeah, some of the things I don't really understand what these notes do.

**Sjors Bogers** [09:27:11]: let alone that I can come up with design similar like that, right?

**Sjors Bogers** [09:27:17]: Okay.

**David Orban** [09:27:18]: So let's do two things, if you agree.

**David Orban** [09:27:24]: I don't mind having you to invest your time to touch any 10 and get first-hand experience and develop the level of understanding that you have, including your frustration.

**David Orban** [09:27:43]: Let's leave it now on the side.

**David Orban** [09:27:46]: Wait until we see what Open AI announces tonight, but also use Claude to develop a workflow automation that is exclusively based, as I said, on Python scripts.

**David Orban** [09:28:18]: Okay?

**David Orban** [09:28:19]: So you just describe what you want to do and then progressively go on implementing it in small scripts.

**David Orban** [09:28:31]: So one of the script will be monitoring a folder.

**David Orban** [09:28:35]: And when the folder is And don't hesitate using a local folder because using the Google API to monitor a remote folder is just too much of a headache.

**David Orban** [09:28:51]: Just a local folder.

**David Orban** [09:28:54]: And the script says, look for files in the folder.

**David Orban** [09:29:00]: And then when the files appear, do something with That's Right?

**David Orban** [09:29:10]: And then create the resulting file and then again, sending that file via email with Google would require using the Google API.

**David Orban** [09:29:23]: And if you have the time and the willingness, then you can also look at how Kong could help or not.

**David Orban** [09:29:35]: One of the things that you will realize is that it's heavily AWS oriented.

**David Orban** [09:29:44]: So adopting it comes at the cost of embracing AWS.

**David Orban** [09:29:49]: And I don't know if it is also available on Azure, which almost by definition will be our preferred system, but we'll Yeah.

**Sjors Bogers** [09:30:05]: As I noticed yesterday, almost everything that you drag into it comes with a price.

**Sjors Bogers** [09:30:10]: Sometimes they have free version, but then very often they don't allow you to connect the API keys, right?

**Sjors Bogers** [09:30:16]: Because it's free version.

**Sjors Bogers** [09:30:17]: So you are talking about an 8.10 And then I got the plan, the basic plan.

**Sjors Bogers** [09:30:25]: But if you want to use the Google thing, you have to set up Google Cloud, which could be done for free.

**Sjors Bogers** [09:30:33]: But it comes with free credit.

**Sjors Bogers** [09:30:35]: So that will probably run out at a certain moment.

**Sjors Bogers** [09:30:38]: That's 250 euros, I think, to start with.

**Sjors Bogers** [09:30:40]: So it should be more than enough for now.

**Sjors Bogers** [09:30:43]: if we're actually going to use it, then that's another thing we need to start using.

**Sjors Bogers** [09:30:50]: And then there's fine where you can make a vector database.

**Sjors Bogers** [09:30:54]: So basically you can store all your files there, and then it can fetch the relevant files that it needs by doing a quick search and then pulling only that into the context window.

**Sjors Bogers** [09:31:05]: I don't know if describe it correctly, but that's how I understood And they have free plan, but it's, again, fairly limited.

**Sjors Bogers** [09:31:13]: So that is, again, another service that we might have to look And I think Kong is also only paid.

**Multiple speakers** [09:31:23]: So that's another service, and if we're going to use So, yeah, I can keep adding these things, but No, no, no, obviously not on my dime, because I want to pay you back on NA10, but not on all of these other things.

**David Orban** [09:31:46]: Especially credit-based systems are dangerous, because if you exceed, then they invoice you for $1,000 or $10,000.

**David Orban** [09:31:57]: And then you have to beg to forgive you.

**David Orban** [09:32:00]: And sometimes they do, sometimes they don't.

**David Orban** [09:32:03]: It's a hassle.

**David Orban** [09:32:06]: So,

**David Orban** [09:32:12]: okay.

**David Orban** [09:32:13]: That obviously puts an agreed limit what we can reasonably experiment with.

**David Orban** [09:32:24]: And The conclusion that we should try to find solutions that we can run locally not something I mind.

**David Orban** [09:32:43]: Already the Python based example that I gave you as a possible task goes in that direction.

**David Orban** [09:32:54]: degrees of confidentiality on some of the things we need to handle.

**David Orban** [09:33:02]: Do the same.

**David Orban** [09:33:05]: We may build local server farm of some kind.

**David Orban** [09:33:19]: Then what that implies is that we should have a way evaluate when frontier performance is needed and have router.

**David Orban** [09:33:38]: So some tasks can be routed local LLM that is just intelligent enough to do what we need.

**David Orban** [09:33:51]: And GPT- 6 is not needed.

**David Orban** [09:33:55]: And clode 5 is not needed, right?

**David Orban** [09:34:00]: Yeah.

**Sjors Bogers** [09:34:03]: I think what is also harming it a little bit is that There's not really framework for me right now to work with, right?

**Sjors Bogers** [09:34:10]: I don't all the set tools.

**Sjors Bogers** [09:34:12]: I don't have the logic of the processes yet because I'm trying to figure out what is the best way to approach Once we have those things in place, it's going to be a lot easier, right?

**Sjors Bogers** [09:34:22]: We can even document it throw that into the cloud context window when we're building it as Yes, two remarks about that.

**David Orban** [09:34:39]: The only way to break the chicken and egg is by making some decisions about what tools you want to use and then discarding them if they don't work.

**David Orban** [09:34:58]: That shouldn't stop you from being able to document what you are doing the right level of detail so that The documentation can be applied to a different tool when you change.

**David Orban** [09:35:13]: The lower level of documentation should be already delegated to the LLM itself.

**David Orban** [09:35:21]: I mean, even the higher level should be developed with the LLM, but there should be a distinction between what is the goal and then how it is implemented.

**David Orban** [09:35:32]: The second point that I want to give you as a feedback based on what you said,

**David Orban** [09:35:45]: that for the next couple of years, there will be a very delicate interplay between deciding that it is worth standardizing on a given set of features, throwing away what we did because the next new thing is worth And this is not only going to be dictated by own curiosity or being addicted to the

**David Orban** [09:36:24]: novelty, but also by compliance and processes and procedures.

**David Orban** [09:36:37]: And we will have a very lively dialogue, not only internal to our team, but with other colleagues on what are the right decisions each time.

**David Orban** [09:36:51]: Just this morning, posted about this on Slack

**David Orban** [09:37:11]: in AI first where Robert asked how can LLMs be trusted I on one hand referred to him to post I made a month ago where there specific settings so that the LLMs are not allowed to crane on your data, so they don't retain The next step being that enterprise level use is needed so that there are more

**David Orban** [09:37:55]: centralized controls.

**David Orban** [09:37:58]: Then the fact that there are good guides, for example, this was published by you.com, and it has security review checklist, right?

**David Orban** [09:38:11]: Or data, sorry, is that the same?

**David Orban** [09:38:16]: No, here you Internal AI use policy template.

**David Orban** [09:38:21]: And these are good starting points.

**David Orban** [09:38:24]: But the third thing that I then posted is exactly this, that governance and experimentation have to go hand in hand.

**David Orban** [09:38:34]: this is the ideal quadrant that we have to aim achieving high governance and high experimentation, where we maintain the ability to innovate while knowing that we are compliant.

**Sjors Bogers** [09:38:56]: And I was looking at the things that frustrate me and see if affects other users in the same way.

**Sjors Bogers** [09:39:04]: So that makes sense.

**Sjors Bogers** [09:39:06]: It's not me.

**Sjors Bogers** [09:39:07]: That's the problem.

**Sjors Bogers** [09:39:09]: People are bumping into the same difficulties.

**Sjors Bogers** [09:39:13]: And one of the analogies was, and that's something I would see coming also looking at this.

**Sjors Bogers** [09:39:18]: If you a lot of these processes, things start to break as well, right?

**Sjors Bogers** [09:39:23]: Because the tools you drag into it are going to change a little bit and then It's a constant maintenance loop.

**Sjors Bogers** [09:39:29]: The analogy they use is like you create an animal and then trying to cure the wounded animal time after time.

**Sjors Bogers** [09:39:38]: So where we are right now, just looking at how simple it was to just take the files and take the prompts and then execute whatever output is, is already what you're using, right?

**Sjors Bogers** [09:39:50]: So for now, it is still fairly simple to do it manually.

**Sjors Bogers** [09:39:54]: And I'm not sure if we should also consider doing just that, making a database of prompts that the advisor can easily go into, and then they manually take the folder and the data they want because that is a simple way to go around as for now.

**Sjors Bogers** [09:40:11]: I'm not saying we should do that, but if that's much simpler than building this whole Christmas tree of tools, that might be more pragmatic.

**David Orban** [09:40:30]: I agree about a minimalistic approach rather than a Baroque approach.

**David Orban** [09:40:39]: Again, that is why I said, let's use Python scripts.

**David Orban** [09:40:46]: 20- year old technology.

**David Orban** [09:40:54]: We should not

**David Orban** [09:41:01]: lower our ambitions.

**David Orban** [09:41:10]: I think that the perception of value would be radically decreased if we said it couldn't be automated.

**David Orban** [09:41:20]: Yeah, I understand.

**Sjors Bogers** [09:41:22]: Right?

**Multiple speakers** [09:41:23]: Even if you are right and it is simple and it takes really just a little bit of time.

**David Orban** [09:41:28]: And maybe it is even healthy because while you are doing it, you can more easily review what the AI produces rather than going back after the fact and then being angry about some mistakes.

**David Orban** [09:41:47]: Even if that is the case, our users, i.e.

**David Orban** [09:41:52]: Randy, would correct their expectation of the benefit downwards radically if we told him that it cannot be automated.

**David Orban** [09:42:07]: I understand.

**David Orban** [09:42:11]: All right.

**Multiple speakers** [09:42:15]: I do have a question about the very first trigger, which quite a question mark for me right now.

**Sjors Bogers** [09:42:22]: Because what would be the starting point, right?

**Sjors Bogers** [09:42:26]: If you, let's say we have five different advisors or at the moment we have, how many?

**Sjors Bogers** [09:42:35]: Clients, you or people?

**David Orban** [09:42:37]: People serving the clients as advisors.

**Sjors Bogers** [09:42:39]: So it's Samuel, Randy.

**Sjors Bogers** [09:42:44]: Doesn't, I don't know.

**David Orban** [09:42:45]: Okay, let's say five.

**David Orban** [09:42:50]: Okay.

**Multiple speakers** [09:42:50]: What is their starting point to interact with automation?

**Sjors Bogers** [09:42:55]: And how do I know that Randy is doing this, and he wants the output and not the other five advisors getting an email every time somebody uses something for their client and not for client they're not working Maybe I'm overthinking it, these the type practical things I don't get at the Yes, fair

**David Orban** [09:43:20]: question, I don't know the answer.

**David Orban** [09:43:23]: There can be many different ways to solve And the worst that can happen if the way is to monitor an empty folder where documents are added that the AI needs to be working and then the AI empties the putting the documents in the output folder together with the additional document that the AI created.

**David Orban** [09:44:01]: The worst that can happen is that we are wasting tokens with more people doing the same thing, right?

**David Orban** [09:44:15]: And is not our responsibility to avoid that.

**David Orban** [09:44:23]: Or if we want that to be our responsibility, I would say that it belongs to Asana.

**David Orban** [09:44:31]: So the workflow of how you work the client documents is, is, is based on Asana.

**David Orban** [09:44:43]: And, and there is a stage of understanding and analyzing the client need.

**David Orban** [09:44:51]: then understanding and analyzing client pitch deck, and then understanding and analyzing the client data room and so Oh, an important need is going to be to find good investor matches.

**David Orban** [09:45:19]: we can look at the page deck API, which will be the one that Ali one is going to subscribe to at close to $5,000 a month.

**David Orban** [09:45:38]: But on top of that, there could be also other tools that we want to use that that could be free or just less expensive.

**David Orban** [09:45:54]: And that will be another very, very valuable enhanced activity that we should help

**David Orban** [09:46:10]: Yeah.

**Sjors Bogers** [09:46:10]: Do you think it's worth for you to try and give a shot set this and make it work?

**David Orban** [09:46:20]: I will take my own advice, wait for tomorrow, see what OpenAI announces, try to use the API and see if I can have Claude work on it rather than me personally, directly, rather.

**David Orban** [09:46:48]: And then maybe even use the Python approach that I described you.

**David Orban** [09:46:56]: But no, I don't want to share your frustration and repeat your approach just directly because I know would get angry

**Sjors Bogers** [09:47:13]: Yeah.

**Sjors Bogers** [09:47:13]: Okay.

**David Orban** [09:47:13]: All Anything else?

**David Orban** [09:47:18]: No, I don't think Okay, so based on what you said, feel free not to explore Kong too deeply because it would lead towards the multiplication of the tools.

**David Orban** [09:47:33]: If you want to ask Claude how should go about together with in creating the Python scripts for monitoring folders and creating files blah, blah.

**David Orban** [09:47:46]: I think that could be good clarification.

**David Orban** [09:47:48]: Also maybe you could think of how to document the process at two degrees of abstraction.

**David Orban** [09:47:57]: One at a high level that is independent from the tools then one or two lower levels of which one is an A10, another is the Python script.

**David Orban** [09:48:11]: And then let's see what tomorrow brings.

**David Orban** [09:48:16]: Okay.

**David Orban** [09:48:18]: And tomorrow, same I have a meeting, but I can do something like 1 p.m. If that good for Yeah, that Okay, I will send the invite.

**David Orban** [09:48:35]: Okay, Thank you.

**Sjors Bogers** [09:48:36]: Bye-bye.

---
*Backed up from MeetGeek on 2026-03-30 08:59*
