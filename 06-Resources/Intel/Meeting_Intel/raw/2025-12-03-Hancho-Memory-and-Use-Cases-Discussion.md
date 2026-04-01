# Hancho Memory and Use Cases Discussion

**Date:** 2025-12-03
**Duration:** Unknown
**Meeting ID:** 01f67927-3862-4dd3-9de1-458b4171411a

## Participants
- *Participants not listed*

### Summary

The call reviewed Hancho usage, examples, and emerging application categories: chat-based memory, education platforms, enterprise/institutional memory, and robotics. David highlighted Bordy as an example of effective multimodal handoffs and praised Hancho demos and X402 integration. Discussion covered strategic vision—memory infrastructure as essential beyond RAG—and potential enterprise/government use for capturing metadata and simulating organizational variants. Product feedback included positive reception of demos and a recommendation to consider broader design for go-to-market. The meeting closed with Abigail offering to follow up on thread and share contact details.

## Full Transcript

**ajspig** [17:30:46]: Hi, David.

**ajspig** [17:30:48]: Hello, hello.

**ajspig** [17:30:49]: How are you doing?

**ajspig** [17:30:50]: Looks like you're on the road.

**David Orban** [17:30:53]: Yeah, but traffic is very slow, so no problem, even if I glance at you.

**ajspig** [17:30:58]: Okay, good.

**ajspig** [17:31:00]: Good, don't want to cause a car accident for sure.

**David Orban** [17:31:04]: Not unless or until I uploaded myself, right?

**ajspig** [17:31:08]: Right.

**David Orban** [17:31:12]: Is anyone else joining today?

**David Orban** [17:31:14]: I think

**ajspig** [17:31:15]: Cortland should be joining.

**ajspig** [17:31:16]: Here's the one that initially you were talking with.

**David Orban** [17:31:20]: Correct.

**David Orban** [17:31:21]: So we'll give him just a minute here, but

**ajspig** [17:31:24]: I'm happy to dig in as well.

**David Orban** [17:31:28]: So what do you do at the company?

**David Orban** [17:31:30]: Yeah, I

**ajspig** [17:31:30]: head up the developer relations.

**ajspig** [17:31:32]: So 50% I'm helping build and then 50% I'm talking about what we're building.

**David Orban** [17:31:37]: All right.

**ajspig** [17:31:40]: It's been really fun to work with a product.

**ajspig** [17:31:42]: It's been a blast.

**ajspig** [17:31:42]: Have you had the chance to work with Honto Chat at all?

**David Orban** [17:31:47]: So I signed up in April.

**ajspig** [17:31:50]: Yeah.

**ajspig** [17:31:51]: When it was very,

**David Orban** [17:31:53]: very raw and rough at the edges still.

**ajspig** [17:32:00]: And at that point, I

**David Orban** [17:32:01]: did have a bit of time, but it just wouldn't work for whatever reason, doesn't matter.

**David Orban** [17:32:09]: And then I got a bit busier.

**David Orban** [17:32:13]: And in preparation for this call, I looked at the various examples, including Honcho Chat, and they are delightful.

**David Orban** [17:32:31]: And yes, I see them as... examples of what can be done using Hancho, even if maybe some of them, or specifically Hancho Chat, is also a useful gateway into building with Hancho itself.

**David Orban** [17:32:53]: Spot

**ajspig** [17:32:53]: on.

**ajspig** [17:32:54]: Yes, exactly.

**ajspig** [17:32:55]: Yeah, that's totally what we've built Hancho Chat to do is to help people see the capabilities of Hancho and how memory that's built in a way that actually works the way LLM's work and works in a reasoning pattern, how that actually makes a difference.

**David Orban** [17:33:12]: Yeah, yeah.

**David Orban** [17:33:14]: So what in the past few weeks, what categories of applications would you highlight that surprise you that are at least somewhat unexpected.

**ajspig** [17:33:35]: Like people using Hancho Chat?

**David Orban** [17:33:37]: No, well, not only Hancho Chat, but the API itself, right?

**David Orban** [17:33:44]: Let me give you an example.

**David Orban** [17:33:48]: I don't know if you heard of or have interacted with Bordy.

**ajspig** [17:33:54]: No, how do you spell

**David Orban** [17:33:55]: B-O-A-R-D-Y, board.

**ajspig** [17:34:01]: Okay.

**ajspig** [17:34:01]: And it

**David Orban** [17:34:02]: is a very recent app for investor introductions.

**ajspig** [17:34:13]: Okay.

**ajspig** [17:34:13]: And the

**David Orban** [17:34:13]: flow really feels like something that is gonna be, if not universal, close to universal.

**David Orban** [17:34:24]: It moves seamlessly between email, WhatsApp, voice calls, it calls you, and then you have a 10-minute conversation with it.

**David Orban** [17:34:38]: And it goes very, very well.

**David Orban** [17:34:41]: And then, you know, whatever.

**David Orban** [17:34:44]: It doesn't matter.

**David Orban** [17:34:45]: But regardless of whether they will be successful or not, and whether the specific application area is interesting or important, and then how big it is, etc.

**David Orban** [17:35:03]: just how well the handoff between the various modalities is really good.

**David Orban** [17:35:14]: Here's another example.

**David Orban** [17:35:19]: On WhatsApp, even before the example, a characteristic of body is that it is very proactive.

**David Orban** [17:35:29]: So chat GPT and all the others are kind of passive.

**David Orban** [17:35:33]: And the only way that they want to do things is by asking you the lame questions that never close the conversation.

**David Orban** [17:35:42]: They always want to keep the conversation open.

**David Orban** [17:35:45]: And I mean, at least I personally don't very much like it.

**David Orban** [17:35:49]: But Bordy is very proactive in getting to the point of what it wants.

**David Orban** [17:35:59]: And here's the example.

**David Orban** [17:36:02]: It wants to talk to you.

**David Orban** [17:36:04]: It wants to set up a call.

**David Orban** [17:36:08]: So it proposes call swaths.

**David Orban** [17:36:12]: And then when you say yes, it sends a calendar invite.

**David Orban** [17:36:16]: and then it calls you at the time agreed.

**David Orban** [17:36:21]: And again, it is well designed, very purposeful and feels very smooth as it moves from WhatsApp chat to phone call to email.

**David Orban** [17:36:36]: It's really good.

**David Orban** [17:36:39]: Okay,

**ajspig** [17:36:40]: regardless of my positive experience

**David Orban** [17:36:42]: with Bordy, The reason I brought it up is because I asked you the question, what kind of applications surprise you that developers are trying to do?

**David Orban** [17:36:55]: And I wrote, and you are welcome to quote specific ones, but the reason I said categories, because that gives you the opportunity also of, you know, exploring rather than specifics to talk about what areas are emerging.

**David Orban** [17:37:13]: Sure.

**ajspig** [17:37:13]: Right?

**ajspig** [17:37:14]: Yeah, so in the case for Bordy, like if we were to integrate with them, we would help with our memory infrastructure.

**ajspig** [17:37:20]: And so that's kind of where we're fitting in right there is memory infrastructure.

**ajspig** [17:37:23]: So pretty much anyone that's building with AI applications or anything, even not even like necessarily connected to AI, but you need some sort of memory infrastructure, that's where we come in.

**ajspig** [17:37:36]: So we've had a lot of people to kind of answer your question, people with chat-based applications who are chatting with other AI products.

**ajspig** [17:37:45]: That's a common use case for them.

**ajspig** [17:37:48]: We also have education platforms that are interacting with students and wanting to have those conversations.

**ajspig** [17:37:57]: They specifically are using it with like a, when they're chatting with like an AI simulation to kind of help them learn historical facts.

**ajspig** [17:38:05]: Like that's a case for it as well with Hancho.

**ajspig** [17:38:08]: But they also use it in other scenarios as well to kind of help students learn and using the memory to help feed that.

**ajspig** [17:38:16]: Those are two that are coming to mind right now.

**ajspig** [17:38:18]: But we're like, we're pretty versatile and can fit in a lot of different scenarios.

**ajspig** [17:38:22]: So, you know, there's all sorts of fun, exciting projects that could fit us in.

**David Orban** [17:38:27]: Of course.

**David Orban** [17:38:28]: Do you find that the use cases fit more a B2C, a consumer-facing pattern?

**David Orban** [17:38:37]: The education one is a detour from classical categories.

**David Orban** [17:38:47]: Or do you have also a sizeable enterprise user base or developers that are either developing applications or inside a large organization wanting to take advantage of what Honsho can

**ajspig** [17:39:08]: offer.

**ajspig** [17:39:11]: I'm sure we could, as we talk more, we could give you more details about what our customer base looks like.

**ajspig** [17:39:15]: But we definitely have a mix.

**ajspig** [17:39:17]: Yeah, the education was kind of a divergent.

**ajspig** [17:39:19]: Maybe it was more typical.

**ajspig** [17:39:21]: And we're definitely exploring and talking to a lot of different people, which has been good.

**ajspig** [17:39:26]: But I'm sure we could give more details later.

**ajspig** [17:39:28]: And I guess I would love to learn more about like what's your vision for using Hanto?

**ajspig** [17:39:33]: It seems like you're coming from an investing background and also some building as well.

**David Orban** [17:39:41]: Yeah, many things.

**David Orban** [17:39:44]: So I am, first of all, philosophically attracted to what Honcho promises.

**David Orban** [17:39:54]: Sure.

**David Orban** [17:39:54]: And we will see whether Honcho will deliver.

**David Orban** [17:39:59]: or someone else or many different approaches will succeed or complement each other, but it is obvious to an increasing number of people that pretending that the context window or any rag approaches are enough is ridiculous, they are not, and something much deeper is needed.

**David Orban** [17:40:28]: Now, once you accept

**David Orban** [17:40:45]: First of all, sorry, not first of all, just to give you one data point about my background.

**David Orban** [17:40:55]: I was part of the team that designed Singularity University at the NASA Research Park together with Ray Kurzweil and Peter Diamandis and others.

**David Orban** [17:41:09]: And I was... This was more than 10 years ago.

**David Orban** [17:41:18]: And 15 years ago, was the chair of Humanity Plus, the World Transhumanist Association, where transhumanism is the philosophy that defines humanity through its ability to overcome its challenges and limitations, including redefining what it means to be human.

**David Orban** [17:41:42]: So that is why for me, talking about digital identity, mind uploading and all those kinds of things is very natural.

**ajspig** [17:41:55]: Yeah.

**ajspig** [17:41:55]: Now, back to today, I am

**David Orban** [17:42:03]: pretty sure that representing, emulating, simulating human identity is going to be a vanishingly small proportion of applications that AI agents with memory functions will choose to implement and maintain.

**David Orban** [17:42:35]: And the reason is very simple.

**David Orban** [17:42:38]: Yes, we are cool, but we are not that cool.

**David Orban** [17:42:42]: And the AI agent based layer of the economy is going to extend in areas very rapidly that we hopefully understand, but that are not based on direct connection with our nature and our desires.

**David Orban** [17:43:07]: So let me give you two simple examples of what I mean that connects back to honcho and honcho applications that I'm interested in potentially exploring.

**David Orban** [17:43:18]: One is, robots, humanoid or not, can benefit from a memory function that intersects their ability to map out a physical space and the timestamp of particular experiences or particular events around physical space.

**David Orban** [17:43:53]: And this can be self- driving cars, this can be industrial applications, home applications, or applications that are completely separate from human-centered experiences.

**David Orban** [17:44:09]: The second example and area that I would mention and highlight is institutional memory.

**David Orban** [17:44:21]: What does it mean to capture and preserve finance granularity possible data layer on the workings of an organization, whether this is meeting transcripts, whether this is Slack channels, but even things that again just describe without necessarily containing the data, the interactions themselves.

**David Orban** [17:45:00]: I don't know if you are familiar with Gather.

**David Orban** [17:45:02]: I'm

**ajspig** [17:45:03]: not, but what you're describing is definitely something that we're, but second point, I would say that that is definitely something we're really closely working with right now.

**David Orban** [17:45:11]: Wonderful, wonderful.

**David Orban** [17:45:13]: Gather is a, 2D or exonometric place for remote teams where you set up a little

**ajspig** [17:45:24]: avatars.

**ajspig** [17:45:25]: Yeah.

**ajspig** [17:45:26]: Okay, that move

**David Orban** [17:45:27]: around that they meet in meeting rooms.

**ajspig** [17:45:29]: Yeah, and it's kind of a retro style.

**ajspig** [17:45:32]: Yeah,

**David Orban** [17:45:32]: absolutely, like a video game out of the 80s.

**ajspig** [17:45:36]: Right.

**ajspig** [17:45:36]: And so there, even

**David Orban** [17:45:39]: if people just talk like you and I, but they are in the same meeting room.

**David Orban** [17:45:46]: That is information worth capturing without capturing what they said.

**David Orban** [17:45:52]: Who are the people that are meeting when?

**David Orban** [17:45:55]: And so there is a lot of rich information that is worth capturing, representing and understanding.

**David Orban** [17:46:07]: And then we should obviously be talking not only about enterprises but also governments and how centralized or decentralized governance can be made much more efficient if we understand the kinds of interactions they lead to decision-making and so

**ajspig** [17:46:34]: And then with this model,

**David Orban** [17:46:37]: what I'm interested in understanding how we can simulate alternative variants and then apply evolutionary algorithms to come up with new ways of working together in an enterprise or in government that is the result of picking the best or the fittest of a certain set of simulations.

**David Orban** [17:47:12]: So these are two examples that have almost nothing to do or very little to do with chatting with honcho chat and finding out why your therapy sessions don't work.

**ajspig** [17:47:32]: Yeah, it's the second one where you're talking about interactions between users like in a Slack chat or like in the gather rooms or those kind of environments where you have a lot of conversation and it's who's in the conversation, it's where the conversation is happening.

**ajspig** [17:47:50]: There's a lot of metadata that can be gathered.

**ajspig** [17:47:52]: I'd say that's where a lot of our focus is in right now, and that's where we're set up really nicely to help augment those situations.

**ajspig** [17:47:59]: Hancho chat is an extension of that, but it's pretty limited in its capabilities.

**ajspig** [17:48:06]: And you pointed out spot on there at the beginning of how it's just trying to highlight some of the basic capabilities of Hancho.

**ajspig** [17:48:13]: But what you're talking about there with that second point of those chat rooms.

**ajspig** [17:48:16]: That's where we're seeing a lot of our customers right now also coming from scenarios like that.

**ajspig** [17:48:20]: And the first one of the robotics, I personally am really interested in robotics.

**ajspig** [17:48:24]: And really, that definitely feels like the next frontier.

**ajspig** [17:48:27]: But we don't currently have a lot

**David Orban** [17:48:34]: of

**David Orban** [17:48:43]: resources command you for doing It not only enables you to collect data, but also rekindles the attention of someone like me who has been interested few months ago, but then was distracted.

**David Orban** [17:49:08]: by the next shiny object and bring back the attention and say, hey, David, do you remember this honcho play with the API?

**David Orban** [17:49:20]: Look at the latest stuff and so on and so forth.

**David Orban** [17:49:25]: and I was so happy to see pretty penny or what is the other demo?

**ajspig** [17:49:33]: Oh, well, why am I forgetting the name?

**ajspig** [17:49:36]: The one that we came

**David Orban** [17:49:41]: out with in October.

**David Orban** [17:49:43]: It is the one where you dump your expertise and you are supposed to be paid.

**David Orban** [17:49:49]: Yeah, pending

**ajspig** [17:49:49]: for your thoughts.

**ajspig** [17:49:50]: Okay, perfect.

**David Orban** [17:49:52]: So I was just delighted to see that you are using X402 because I hope it is going to be very, very successful.

**David Orban** [17:50:06]: is a protocol that definitely nudges the universe in the right direction after it bifurcated and we are sitting on the wrong branch 30 years ago when incumbent financial institutions successfully convinced everyone that credit cards were the right way to transact on the internet.

**David Orban** [17:50:31]: And man, were they so wrong.

**ajspig** [17:50:35]: Yeah, we actually use X402 also in Hancho Chat.

**ajspig** [17:50:39]: The agents,

**David Orban** [17:50:40]: when you're working with it, you can give your agent an access

**ajspig** [17:50:43]: to a wall, and then it can spend on the marketplace and buy and sell artifacts.

**David Orban** [17:50:47]: Wonderful, wonderful.

**David Orban** [17:50:50]: All right.

**David Orban** [17:50:51]: So anything that you want to tell me or I should tell you as we are close to the end of our call today?

**ajspig** [17:50:59]: Well, I'm certainly excited.

**ajspig** [17:51:01]: So see you back and excited about Hancho and Hancho Chat in particular.

**ajspig** [17:51:05]: Yeah, if you are building with it or come across anyone that's building with it, we'd love to.

**ajspig** [17:51:10]: hear from them as well.

**ajspig** [17:51:12]: You're spot on with us wanting to learn more about how people are using it in reaching out to the community.

**ajspig** [17:51:19]: Definitely a big part right

**David Orban** [17:51:20]: now.

**David Orban** [17:51:20]: Here is a piece of feedback.

**David Orban** [17:51:22]: Sure.

**David Orban** [17:51:28]: I love your super geeky design both the website and the But whomever implemented that, as well as me, we are in minority, and you have to ask yourself, as I'm sure you benefit of sticking to because it attracts some people, and repels

**David Orban** [17:52:11]: a point where you or someone else analyzing your data will say, hey, here's this segment, it's very interesting.

**David Orban** [17:52:21]: It is a small portion of our users, but it is a huge market.

**David Orban** [17:52:28]: Isn't it the case that we are getting people using high quality because they just hate our design?

**ajspig** [17:52:38]: You're a little bit sloppy right now.

**ajspig** [17:52:40]: And it may sound

**David Orban** [17:52:42]: superficial.

**David Orban** [17:52:43]: Okay.

**David Orban** [17:52:44]: I don't know what is the last one that you heard.

**ajspig** [17:52:48]: think I'm getting your point.

**ajspig** [17:52:49]: Just the design of how it's a very strong design and not wanting repel people.

**David Orban** [17:53:00]: And yeah, there are pros and cons, and it could be... could be something that you want to weigh as you evolve the way your go- to market, right?

**ajspig** [17:53:15]: Yeah, thank you for the advice.

**ajspig** [17:53:17]: It certainly is a balance with design and I appreciate your feedback.

**David Orban** [17:53:22]: Okay, well, thank you.

**David Orban** [17:53:25]: And I will, I don't think I have, do I have your email?

**ajspig** [17:53:32]: No, but I'll respond to the thread.

**David Orban** [17:53:35]: So you can get it.

**David Orban** [17:53:36]: Because you look like AJ, AJ, SP, IG on

**ajspig** [17:53:43]: Zoom.

**ajspig** [17:53:44]: But I don't

**David Orban** [17:53:46]: know if that is how I should address it.

**David Orban** [17:53:48]: No, my

**ajspig** [17:53:49]: first name is Abigail.

**ajspig** [17:53:50]: Sorry, I should have started with that.

**ajspig** [17:53:51]: I'm not sure why it says that, but I'll... No

**David Orban** [17:53:54]: problem.

**David Orban** [17:53:55]: But I'll respond to the threats.

**David Orban** [17:53:56]: You'll have

**ajspig** [17:53:56]: my email.

**ajspig** [17:53:58]: Okay, thank you.

**ajspig** [17:53:59]: Okay,

**David Orban** [17:53:59]: well, enjoy the rest of your drive, David.

**David Orban** [17:54:00]: Stay safe.

**David Orban** [17:54:01]: Bye-bye.

**David Orban** [17:54:07]: Thank

---
*Backed up from MeetGeek on 2026-03-30 08:51*
