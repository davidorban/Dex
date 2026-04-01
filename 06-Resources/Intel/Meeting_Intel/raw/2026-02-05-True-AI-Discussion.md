# True AI Discussion

**Date:** 2026-02-05
**Duration:** Unknown
**Meeting ID:** 64649ff3-1364-4ea7-a5a9-0daefa543540

## Participants
- *Participants not listed*

### Summary

The call began with technical connectivity issues, then moved to brief introductions and Aliwan's background. Johan explained his conceptual AI design, his motivation and limitations in implementing it, and described his prior technical ideas. He stated the project needs substantial research, technical teams, and likely institutional partners rather than a startup model. David provided strategic feedback recommending open-source/community pathways, active promotion, and using AI for iterative refinement. The meeting concluded with Johan agreeing to send the white paper and David agreeing to review it (with AI) and provide feedback by email.

## Full Transcript

**David's Notetaker** [12:01:32]: Unfortunately, I cannot see you or hear you.

**David's Notetaker** [12:01:41]: Now I can see you but I still can't hear you.

**David's Notetaker** [12:01:58]: Just to be sure I will join from another device.

**David's Notetaker** [12:02:04]: So that we.

**David's Notetaker** [12:02:04]: See if it is on my side.

**David's Notetaker** [12:02:08]: But I was just in a few calls.

**David's Notetaker** [12:02:10]: I would be surprised, but it's always possible.

**David's Notetaker** [12:02:36]: you

**Johan** [12:05:18]: Hello, is this better?

**Johan** [12:05:25]: Hello?

**Johan** [12:05:29]: Yes, I can hear you now.

**Johan** [12:05:31]: Oh, fantastic.

**Johan** [12:05:33]: Yeah, I try to use my phone instead of the laptop.

**Johan** [12:05:37]: So it's working.

**Johan** [12:05:41]: Wonderful.

**Johan** [12:05:42]: Thank

**Unknown User** [12:05:42]: you.

**Unknown User** [12:05:44]: Thank you very much for joining.

**Unknown User** [12:05:47]: And we have been, just as a refresher, introduced by Jan, a colleague of mine.

**Unknown User** [12:05:53]: You sent me a high-level outline of your project.

**Unknown User** [12:06:00]: And I don't know how much you know about us.

**Unknown User** [12:06:05]: Maybe it is worth spending a few minutes, or maybe you have known Jan for a long time, I don't know,

**Johan** [12:06:11]: and know everything about the only one.

**Johan** [12:06:13]: Yeah, it's good if you can tell me who you guys are a little bit.

**Johan** [12:06:17]: I'm not aware for you.

**Johan** [12:06:20]: Okay, okay.

**Unknown User** [12:06:21]: So Aliwan is an Abu Dhabi headquartered investment bank of merchant bank tradition.

**Unknown User** [12:06:31]: We have offices in Abu Dhabi, Riyadh, London, New York and Tel Aviv with activities around asset management, wealth management, family office services, advisory.

**Unknown User** [12:06:48]: And my

**Unknown User** [12:06:57]: background is in AI, so that is why Jan thought that it would be interesting to talk to you.

**Unknown User** [12:07:08]: Yes, yes, okay,

**Johan** [12:07:09]: very good, so let me briefly state what my purpose is here.

**Johan** [12:07:16]: So I obviously got aware of the AI when the LLMs got introduced a couple of years back.

**Johan** [12:07:24]: And after using them, I realized that there are a lot of limitations, but also they seem quite opaque.

**Johan** [12:07:36]: Let me say that.

**Johan** [12:07:37]: And from a user point of view, I got a little bit worried about where this can go.

**Johan** [12:07:44]: Then I listened to a guy called Jan Plovsky.

**Johan** [12:07:50]: He's some kind of AI professor professor in computer science, I think.

**Johan** [12:07:56]: And his concerns regarding how you harness AI, especially if they get more competent than the LLMs are today.

**Johan** [12:08:09]: And obviously I also realize that the LLMs released for public consumption to say are probably a lot less advanced than what is available to institutions and other actors in the field.

**Johan** [12:08:26]: So anyway, this made me think about this and I also understand that a lot of innovations that are done are never done in a, let me say, with the holistic view in mind.

**Johan** [12:08:46]: They are basically coming from some genius level guy inventing something.

**Johan** [12:08:52]: And then that grows and you add on stuff as you find the problems.

**Johan** [12:09:01]: And you end with some kind of patchwork that may not have been the ideal way of pursuing this project, whatever you're trying to develop.

**Johan** [12:09:11]: So thinking about that, I designed this structure, let me call that, or blueprint for how I think an AI should be designed try to address these issues that Jan Plowski and others have brought forward when it comes to AI.

**Johan** [12:09:30]: So that's my You know, that's why I've done this kind of design.

**David Orban** [12:09:39]: That's absolutely admirable.

**David Orban** [12:09:43]: And when you say, let me tell you what is my objective here, I thought you were referring to our call.

**David Orban** [12:09:49]: So what is your objective in this call?

**David Orban** [12:09:53]: What will mean for you that you will end the call and you will say, I'm glad that we had this call.

**Johan** [12:10:03]: It is obviously this design is a complex, right?

**Johan** [12:10:07]: So it's like a 70, 75 page PDF describing how this should look.

**Johan** [12:10:13]: But I obviously cannot verify that I'm correct or not.

**Johan** [12:10:21]: I use obviously models to verify way I think.

**Johan** [12:10:26]: And I understand that's a bit of a or could be a bit of a trap.

**Johan** [12:10:31]: And

**David Orban** [12:10:32]: that's what could we maybe take a take a step back, you can tell me about your background, whether you come from an entrepreneurial path or or you have had technical or technology related activities in the past that could be useful.

**Johan** [12:10:56]: originally an Air Force pilot and then an airline captain for my whole career.

**Johan** [12:11:03]: But I worked on the sidelines with other projects and particularly I got involved in a small Swedish startup company that is involved in managing air traffic and providing weather and solutions for managing the traffic.

**Johan** [12:11:28]: And there I invented a structure how to properly manage air traffic, which it has never been implemented because there's too many stakeholders, but it's still something that the big governmental entities like Cesar strives to do.

**Johan** [12:11:52]: Even though I've been fiddling with this for 10 years, it moves in snail pace.

**Johan** [12:11:59]: Let me say that.

**Johan** [12:12:01]: So in that sense, I've always been a conceptual thinker.

**Johan** [12:12:06]: So I have some technical understanding of things, but not on the detail level, but conceptually I have.

**Johan** [12:12:13]: And once the LLM showed I could use them as knowledge base to see if my concepts actually were working.

**Johan** [12:12:25]: And the first thing I did was to design a Bitcoin level two payment system.

**Johan** [12:12:33]: And I have designed a consciousness first world view that I probably will try to publish in some kind of scientific publication.

**Johan** [12:12:52]: And now

**David Orban** [12:12:52]: I design this AI.

**David Orban** [12:12:55]: Wonderful.

**David Orban** [12:12:56]: So thank you for that background information.

**David Orban** [12:12:59]: Now, you stated and you said, obviously, and for someone who is on the first call with you, maybe that is less obvious.

**David Orban** [12:13:09]: You said, obviously I cannot implement this 77 page or even verify that it is correct.

**David Orban** [12:13:18]: So what is your ideal outcome if you want your idea flourish?

**David Orban** [12:13:28]: Are you seeking other team members that you want to add to project?

**David Orban** [12:13:33]: Do you want to find a university that sponsors the research that can establish, whether it makes sense, you want to found a startup where you are the CEO and seeks venture capital funding for it.

**David Orban** [12:13:52]: So how do you want to go about turning it into reality?

**Johan** [12:13:58]: So my viewpoint, considering that I'm a conceptual thinker, I cannot implement this.

**Johan** [12:14:07]: I'm not the right person for implementing, but I understand the complexity is such that it would require a team or a, you know, somebody with significant financial and competence resources to develop this is, I don't believe it's a startup because I think you need much more finance capability than a

**Johan** [12:14:32]: startup.

**Johan** [12:14:33]: I would think AI lab or governmental entity that involved in developing and especially so because this is designed to be a self- evolving system, not not just a prompt steered system.

**Johan** [12:14:54]: So it could potentially be a

**David Orban** [12:14:59]: very, very clear.

**David Orban** [12:15:00]: So what do you think that an entity like you described is a good target for this kind of next phase in your project.

**David Orban** [12:15:15]: What do you think they would need in order to be convinced that rather than being a lunatic, you have real ideas that they should devote time and energy and understanding and then carrying forward.

**David Orban** [12:15:36]: Yes, so

**Johan** [12:15:38]: it's basically two things I think is needed.

**Johan** [12:15:41]: One is that that such entity actually reads this white paper.

**Johan** [12:15:49]: I think it would stand on its own, so to say.

**Johan** [12:15:52]: But the best way is that it's somebody, maybe like yourself, if I understand your background, can, if not endorse it, but at least say that I've looked through this and it's a viable thing to look

**David Orban** [12:16:10]: Do you understand?

**David Orban** [12:16:11]: Oh, yeah, I do, I do.

**David Orban** [12:16:16]: And whether I am or not that kind of person and whether my eventual endorsing it carries weight or not is a different question.

**David Orban** [12:16:25]: But sure, that reasoning is sound.

**David Orban** [12:16:29]: Now, once you achieve that What do you believe your role would be in the project?

**David Orban** [12:16:42]: Once you convince an entity to say, wow, this is worth our money, our resources, our team dedicated to developing this.

**David Orban** [12:16:51]: What role would you play?

**David Orban** [12:16:54]: I would say

**Johan** [12:16:55]: an advisory role to steer the concept.

**Johan** [12:17:04]: The way I see the white paper is that it's a blueprint or a roadmap for how this should be developed how to have the end goal in sight when we when you start rather than then do this add-on way that is the normal way of developing stuff you you have something and or we need this or we need this and

**Johan** [12:17:29]: you you keep adding and then it becomes a patchwork rather than design structure in end.

**Johan** [12:17:37]: Sure.

**Johan** [12:17:37]: The main effort to bring this to reality is technical and implementation knowledge and research.

**David Orban** [12:17:48]: There's some research required as well, of course.

**David Orban** [12:17:51]: Sure.

**David Orban** [12:17:52]: So we have a little more than 10 minutes left in our call.

**David Orban** [12:17:58]: Let me give you some some feedback.

**David Orban** [12:18:01]: And then after that we can we can agree in next steps.

**David Orban** [12:18:05]: So your premise is correct.

**David Orban** [12:18:09]: There is a lot of effort by a lot of people to move forward innovation and progress.

**David Orban** [12:18:22]: It is necessary to have some fresh kind of thinking, fertilizing the effort so that there can be breakthroughs that otherwise wouldn't happen.

**David Orban** [12:18:32]: And whether we call this genius or something else, doesn't matter.

**David Orban** [12:18:37]: What matters is that, yeah, indeed, it is possible to bet on thinkers that don't come necessarily from the field.

**David Orban** [12:18:50]: And contrary to what happened hundreds of years ago, where the number of very valuable thinking that has been forgotten is much larger than those that have been recognized or maybe sometimes rediscovered one or two hundred years after the person giving birth to those ideas died.

**David Orban** [12:19:25]: The advantage of today's world that we are global communications.

**David Orban** [12:19:30]: We have frantic thirst for all kinds of ideas to fight it out in the open.

**David Orban** [12:19:42]: Yes.

**David Orban** [12:19:42]: In particular, in the world of information technology, We have developed a very sophisticated approach in making sure that good ideas have a way of blossoming.

**David Orban** [12:19:58]: And it is called open source.

**David Orban** [12:20:01]: Open source that applies not only to code, but it applies to also how you promote your ideas, how you develop a following of people

**David Orban** [12:20:24]: bet on it not necessarily with money because they may not even have money, but they bet on it with their skills and time because they dedicate it to that project in this very, very large open source community, to the point that Microsoft paid four plus billion dollars to acquire GitHub, which is the

**David Orban** [12:20:43]: main repository of open source in the world.

**David Orban** [12:20:51]: Definitely your ability to recognize the limits of what you are or not able to accomplish is the perfect starting point, because then you can welcome contributions by others.

**David Orban** [12:21:06]: The approach that you had, in my opinion, in trying to achieve this is wrong because you put the onus on the person or the organization.

**David Orban** [12:21:21]: in stepping up and invest in what you should be investing analyzing, understanding the idea in its form, which is a black box.

**David Orban** [12:21:40]: Because you say, well, if you want to learn more, we need an If you really want, then you need to dedicate a team.

**David Orban** [12:21:51]: I haven't invested my time to find a second person who believes in it because I'm alone, but you should dedicate a team, maybe of 10 people.

**David Orban** [12:22:01]: So my recommendation you is to change strategy, to decide whether you expect to become a billionaire out of or whether you believe that it is worth testing it.

**David Orban** [12:22:15]: to find that it is valuable, to become recognized as the person who gave birth to this idea or set of ideas and the project that follows and then receive the financial benefit that naturally follows.

**David Orban** [12:22:37]: It is from an entrepreneurial point of view, a very common fallacy to believe that ideas are stolen and yes it happens, but execution is really what matters.

**David Orban** [12:22:50]: Execution not necessarily or only from a technical point of view, execution also from the point of view of creating enthusiasm and recognition around something that is novel and original.

**David Orban** [12:23:05]: And yeah, you know, it is a fairly common way saying that extraordinary claims require extraordinary proofs.

**David Orban** [12:23:24]: including the courage to promote your idea openly because you want to be tested, you want it to become part of the global conversation that enthusiastically follows ideas and their implementation.

**David Orban** [12:23:46]: Now, including the fact that there are projects and teams that aggregate around it.

**David Orban** [12:23:52]: I was involved since the beginning with a project called Singularity Net that has a specific fund giving money, $100, $200,000 worth to early ideas, really, because someone describes them and they apply to receive the grant.

**David Orban** [12:24:12]: And these are grants, no strings attached.

**David Orban** [12:24:16]: And that is just one example.

**David Orban** [12:24:17]: There are many So these are the two things that I would recommend.

**David Orban** [12:24:22]: One, realize that that you cannot deflect the responsibility of creating enthusiasm around your idea, because you feel it and you must share and then ignite that enthusiasm.

**David Orban** [12:24:39]: be smart about how you find the people who, people and resources who would embrace it.

**David Orban** [12:24:50]: And there are so many avenues.

**David Orban** [12:24:52]: And you said that you use the AI to refine it and to write the white paper, perfect.

**David Orban** [12:25:00]: Use the AI for everything else as well.

**David Orban** [12:25:02]: Obviously, my advice should be also tested through AI, ask your AI whether I am saying something that you should follow or not.

**David Orban** [12:25:16]: And I'm sure that is not the only way to do go about it.

**David Orban** [12:25:23]: What I am describing, it is just what I think you should do.

**David Orban** [12:25:25]: There will be many other ways.

**David Orban** [12:25:28]: And your idea is really good, I'm sure you will succeed.

**Johan** [12:25:36]: Would you be interested to read that paper or is it too much time consuming, you think?

**David Orban** [12:25:45]: So I would use AI to read it, as well as myself.

**David Orban** [12:25:49]: So we would do it together.

**David Orban** [12:25:51]: would not sign an NDA, as we already mentioned, very simply because I cannot be tied in hundreds of NDAs apologies, random people asking me to sign something.

**David Orban** [12:26:04]: But if you want to send it to me, I will be happy to provide you feedback, yes.

**David Orban** [12:26:10]: Okay, so

**Johan** [12:26:11]: let me do that then, because if I you I don't have really a social following.

**Johan** [12:26:19]: I'm a bit hermit, right?

**Johan** [12:26:22]: I have very hard to push these ideas out myself.

**Johan** [12:26:26]: It's these kind of encounters, like I realize that John was involved in these kind of things and he suggested that we should try to get in contact.

**Johan** [12:26:38]: And that is like an avenue that would suit me because I am not in a position do that promotion, even if I will, because I cannot get it You know, I tried with point and I can't even get eyes it, you know, because I don't have that reach.

**Johan** [12:26:56]: And when you go in a total sphere, it doesn't matter how many DMs or X posts you try

**David Orban** [12:27:04]: to make, nobody sees it.

**David Orban** [12:27:08]: Well, that's a separate conversation.

**David Orban** [12:27:11]: And of course, you have to be what you are, you have to recognize your nature, you cannot become something else.

**David Orban** [12:27:17]: But thank you for showing flexibility and I'm glad that we had this conversation.

**David Orban** [12:27:22]: You have my email.

**David Orban** [12:27:24]: I'm looking forward to receiving the document.

**David Orban** [12:27:26]: And then in a few days' time, I will give you some feedback.

**David Orban** [12:27:29]: That's fantastic.

**Johan** [12:27:30]: I appreciate that.

**Johan** [12:27:32]: So let's see if you like it or not.

**Johan** [12:27:36]: thank you very taking the time.

**Johan** [12:27:38]: I appreciate it.

**Johan** [12:27:39]: Okay, thank Thank you.

**Johan** [12:27:40]: Have a nice day.

**Johan** [12:27:41]: Thanks.

**Johan** [12:27:42]: Thank you, Johan.

**Johan** [12:27:42]: Bye-bye.

**David Orban** [12:27:43]: Bye-bye.

---
*Backed up from MeetGeek on 2026-03-30 08:45*
