# Matteo and David Orban

**Date:** 2025-10-30
**Duration:** Unknown
**Meeting ID:** 03f8fb5b-5467-4cf7-a493-6f7204de257e

## Participants
- *Participants not listed*

### Summary

In the meeting between Matteo Fabro and David Orban, they discussed a proposed crypto trading strategy leveraging alternative data and AI models, with Matteo tasked to share detailed strategies and data sources with David. They addressed the performance of AI trading models, noting challenges with underperforming models lacking alternative data, and emphasized the importance of aligning algorithm behavior with investor risk profiles for transparency. David shared insights from his past experiences, highlighting execution issues and the impact of market behaviors on algorithm performance. They explored the pros and cons of engaging with crypto funds, with Matteo expressing interest in both proprietary trading and partnerships, while also planning to assess the viability of his innovative trading model. Lastly, they discussed compute optimization strategies, with Matteo committing to send a one-pager and pitch deck to David shortly.

## Full Transcript

**Spiallo’s iPhone** [07:05:35]: Hello, hi David.

**Spiallo’s iPhone** [07:05:37]: Can you hear me?

**David Orban** [07:05:38]: Yes.

**David Orban** [07:05:40]: Oh, Is there a lot

**Spiallo’s iPhone** [07:05:43]: of background noise?

**Spiallo’s iPhone** [07:05:46]: Zero.

**Spiallo’s iPhone** [07:05:47]: Or can you hear me clear?

**Spiallo’s iPhone** [07:05:48]: Oh, that's all.

**David Orban** [07:05:49]: Zero background noise.

**David Orban** [07:05:51]: Amazing, you know, because I am

**Spiallo’s iPhone** [07:05:55]: at like the beach right now.

**Spiallo’s iPhone** [07:05:57]: So

**David Orban** [07:06:00]: there's a bit of wind.

**David Orban** [07:06:01]: That is wonderful.

**David Orban** [07:06:04]: You

**Spiallo’s iPhone** [07:06:05]: should,

**David Orban** [07:06:06]: you should not move because your phone tries to send me the video.

**David Orban** [07:06:13]: And

**Spiallo’s iPhone** [07:06:13]: as you move, data changes

**David Orban** [07:06:15]: to watch.

**David Orban** [07:06:19]: Okay,

**Spiallo’s iPhone** [07:06:19]: yeah, I'm just waiting for my MacBook to, oh, here it is, it's turning on.

**Spiallo’s iPhone** [07:06:23]: I'll join from my MacBook now, because I have to share my screen, so.

**David Orban** [07:06:27]: Okay.

**David Orban** [07:06:28]: Here it is.

**David Orban** [07:06:30]: Okay.

**Spiallo’s iPhone** [07:06:30]: How have you been in the meantime, all good?

**David Orban** [07:06:34]: All good.

**David Orban** [07:06:35]: Where are you right now?

**David Orban** [07:06:37]: Whenever you see the book sign, where are you?

**David Orban** [07:06:39]: Whenever you see the book

**Spiallo’s iPhone** [07:06:40]: sign in Italy.

**Spiallo’s iPhone** [07:06:44]: I'll join now from my from my backyard.

**David Orban** [07:06:49]: Okay.

**matteo fabro** [07:08:44]: Okay, there you go.

**matteo fabro** [07:08:47]: Can you hear me?

**David Orban** [07:08:47]: Yes.

**David Orban** [07:08:49]: Very nice.

**David Orban** [07:08:52]: All right.

**David Orban** [07:08:53]: So, well, basically, where is the beach?

**David Orban** [07:08:57]: Are you were saying?

**David Orban** [07:08:58]: Sorry?

**matteo fabro** [07:09:00]: Where is the beach?

**matteo fabro** [07:09:02]: I embody.

**matteo fabro** [07:09:04]: All

**David Orban** [07:09:04]: right.

**David Orban** [07:09:05]: In Bali.

**David Orban** [07:09:05]: Yeah, yeah, yeah.

**David Orban** [07:09:07]: Because

**matteo fabro** [07:09:07]: I want to just... good vibes.

**matteo fabro** [07:09:11]: You know, it's very important.

**matteo fabro** [07:09:12]: Like, I think the environment that you work in is very important.

**matteo fabro** [07:09:17]: Anyways.

**matteo fabro** [07:09:19]: Okay, so basically what I wanted to share with him today is kind of more of the detail than what I was saying last time.

**matteo fabro** [07:09:26]: And so here is.

**matteo fabro** [07:09:31]: That's my screen.

**matteo fabro** [07:09:33]: I thought that, you know, maybe obviously you're not like an expert in quantitative finance, I suppose.

**matteo fabro** [07:09:40]: I could be mistaken, but Looks good.

**matteo fabro** [07:09:47]: Like crypto, and I was thinking of like starting as the first thing was exposed with crypto, because it's the market where there's a lot of publicly available alternative data.

**matteo fabro** [07:10:03]: Obviously it's 24 cent, blockchain is public.

**matteo fabro** [07:10:08]: So in general, I thought it would be quite useful to start with that.

**matteo fabro** [07:10:13]: So can you see my screen?

**David Orban** [07:10:15]: Yes.

**David Orban** [07:10:16]: Okay, so

**matteo fabro** [07:10:17]: basically this was the idea, as you can see here.

**matteo fabro** [07:10:21]: The idea was to use the,

**matteo fabro** [07:10:29]: basically the improvement approach to want the finance specifically solution, so having the systems So maybe I was to start with the Shinkai Baba architecture by Sakai AI to generate regime model that basically detects like the current regime.

**matteo fabro** [07:11:05]: This was suggested to me by like not the actual implementation, but like starting with the regime model for context.

**matteo fabro** [07:11:13]: What's suggested to me by like 10x, 93.0C to now, who now does like cryptal trading, have like crypto trading fund.

**matteo fabro** [07:11:25]: He suggested basically using LLMs for generating like LLN agents for generating trading signals directly.

**matteo fabro** [07:11:34]: So basically the idea is to part of the model specifying the current regime details.

**matteo fabro** [07:11:42]: along with the alternative data, which would be initiated as news.

**matteo fabro** [07:11:48]: Then having the agency to pick some up with trading signal.

**matteo fabro** [07:11:52]: So I'm not sure, like, to what extent you're familiar with the alpha arena benchmarks.

**David Orban** [07:12:00]: Yes.

**David Orban** [07:12:01]: That's base one.

**David Orban** [07:12:02]: I'm not sure.

**David Orban** [07:12:04]: Yeah.

**David Orban** [07:12:04]: And he

**matteo fabro** [07:12:05]: was basically like, yeah.

**matteo fabro** [07:12:12]: Your

**David Orban** [07:12:25]: voice is your voice is breaking

**matteo fabro** [07:12:27]: up.

**matteo fabro** [07:12:56]: Oh, sorry, I think I have a problem with the Wi--Fi.

**matteo fabro** [07:12:58]: Can you hear me properly?

**matteo fabro** [07:12:59]: No,

**David Orban** [07:13:02]: now I can, but before I couldn't, after you shared the AI arena, alpha arena.

**matteo fabro** [07:13:12]: The good point is not right now.

**matteo fabro** [07:13:16]: Two models are outperforming with his deep speech and plan.

**matteo fabro** [07:13:20]: Two models are like kind of a baseline with the big points of fullness, and two models are underperforming as well by now.

**matteo fabro** [07:13:29]: And yeah, I mean, to and all, not different, doesn't incorporate any alternative data.

**matteo fabro** [07:13:35]: There's no music don't play.

**matteo fabro** [07:13:37]: It's just like purely anti-signals, like, right, market data.

**matteo fabro** [07:13:41]: So, one thing, but his idea was to incorporate, like, the alternative signals, along with, you know, having the optimization and the self-improvement was so young.

**matteo fabro** [07:13:53]: direct and direct trading signals.

**matteo fabro** [07:13:55]: Now, my idea was to basically transpose this idea and instead of like generating trading signals directly, which is extremely to generate like data directly.

**matteo fabro** [07:14:06]: I was thinking of moving to the agent basically in the way of my experience from the future idea situation, I have to say that I'll initially request it for me.

**matteo fabro** [07:14:17]: And then Basically, just coming up with these kind of models that feature.

**matteo fabro** [07:14:21]: I'm not sure.

**matteo fabro** [07:14:22]: Can you hear me properly?

**David Orban** [07:14:23]: No, like there's some of the black items.

**David Orban** [07:14:25]: No, I cannot.

**David Orban** [07:14:27]: Is it, stop.

**matteo fabro** [07:14:28]: Was it lagging or like what's the issue?

**David Orban** [07:14:30]: Extremely distorted.

**David Orban** [07:14:32]: Extremely distorted,

**matteo fabro** [07:14:34]: okay.

**matteo fabro** [07:14:35]: Yeah, because there's quite a lot of wind.

**matteo fabro** [07:14:41]: Let me put myself at the back, maybe.

**matteo fabro** [07:14:44]: Sorry.

**matteo fabro** [07:14:44]: The first time that I'm coming here.

**matteo fabro** [07:14:48]: So it's better than the morning every time that you social space and figuring out the detail.

**matteo fabro** [07:14:58]: So maybe if I go so then it should work better.

**matteo fabro** [07:15:02]: Okay.

**matteo fabro** [07:15:03]: Is it working better now?

**matteo fabro** [07:15:04]: Can it hear me better?

**matteo fabro** [07:15:05]: Right

**David Orban** [07:15:06]: now, yes.

**David Orban** [07:15:08]: Okay.

**David Orban** [07:15:09]: Yeah,

**matteo fabro** [07:15:10]: it should be fine.

**matteo fabro** [07:15:11]: Is there a reason why wouldn't this work?

**matteo fabro** [07:15:13]: So that's why we lie.

**matteo fabro** [07:15:57]: Leading.

**David Orban** [07:16:46]: If

**matteo fabro** [07:16:48]: there's like anything, any applause is like, oh, thank you so much.

**matteo fabro** [07:16:52]: Okay.

**matteo fabro** [07:16:53]: Oh, honestly.

**matteo fabro** [07:16:54]: Now you should be able to hear me properly.

**matteo fabro** [07:16:57]: It's like, no waste on the wind.

**matteo fabro** [07:17:00]: Is it good now?

**David Orban** [07:17:01]: Yes.

**David Orban** [07:17:02]: Oh, okay.

**David Orban** [07:17:04]: Okay,

**matteo fabro** [07:17:04]: so anyway, yeah, I'm not sure like how much this resonates with you, like in terms of technology and so on.

**matteo fabro** [07:17:14]: Like, base is obviously quite niche, and it's very like quantitative finance oriented, so I'm not sure.

**matteo fabro** [07:17:22]: how much you understand of this, or like if you've done any quantitative finance at all, or like if you've seen any similar projects to this with like hearing any comments whatsoever.

**matteo fabro** [07:17:35]: I mean, today I still did the parallel with the space on your side.

**David Orban** [07:17:40]: Some years ago, I was the CEO of a company called Quantonomy.

**David Orban** [07:17:49]: that aimed to do exactly this.

**David Orban** [07:17:54]: And at the time we were looking forward to raise between $152 million in the fund to trade.

**David Orban** [07:18:13]: And there were many challenges, and I left the project.

**David Orban** [07:18:22]: But I mentioned it just to confirm that I have some experience with something like this.

**matteo fabro** [07:18:35]: Okay, very interesting.

**matteo fabro** [07:18:36]: And when you say like exactly this, like what do you mean?

**matteo fabro** [07:18:40]: Like what approaches were you using or like challenges did you find?

**matteo fabro** [07:18:45]: So

**David Orban** [07:18:45]: this was before LLMs were, um, uh, in the, at the current level of sophistication because it was more than, uh, than, uh, when was it, uh, Yeah, around 17, 18, I would have to check my archive exactly the period of time, but yes, it was definitely more than five, six years ago.

**David Orban** [07:19:21]: But the approach was evolutionary algorithms searching for trading signals, to be executed across multiple exchanges

**David Orban** [07:19:49]: originally Bitcoin and Ethereum focused.

**David Orban** [07:19:57]: And then we try to extend it to other cryptocurrencies as well.

**David Orban** [07:20:07]: And some of the challenges were around the ability of the algorithms to pull the trigger of actually when the trades should be executed.

**David Orban** [07:20:31]: They were, we were cautious and we didn't want to, we were paper trading at the beginning, then we were using live money And at the time Bitcoin was maybe $10,000 or so.

**David Orban** [07:20:59]: And we wanted to build both a paper trading track record and then a live record so that with that not only we could go to investors through having back tested the approach but showing live data as well.

**David Orban** [07:21:23]: So the way that the algorithm was set up in order not to lose money, sometimes it would not act on the signal that was identified.

**David Orban** [07:21:34]: Another challenge at the time, and I don't know if that is still the case, is that some of the markets were very shallow, so we had to be careful how to structure the trades in order to be able to execute them in a timely manner.

**David Orban** [07:21:55]: And we were at the time not working with market makers.

**David Orban** [07:22:00]: So it would depend entirely on the particular exchange.

**David Orban** [07:22:09]: Because obviously the larger Bitcoin and Ethereum Trades had no problem in terms of liquidity, but when we extended it to other cryptocurrencies, not necessarily the liquidity was there all the time.

**David Orban** [07:22:30]: We also did some tests with

**David Orban** [07:22:41]: public stocks using interactive broker.

**David Orban** [07:22:49]: And that is of course an entirely different ball game.

**David Orban** [07:23:00]: And yeah, that was around the time that I left the project.

**David Orban** [07:23:05]: And one of the reasons I left because I lost faith in our CTO and his ability to pull the project together in a proper manner.

**David Orban** [07:23:20]: from an engineering point of view as well.

**David Orban** [07:23:24]: And since he was the one that recruited me as CEO, I said, okay, this is not working.

**David Orban** [07:23:33]: Thank you, bye-bye.

**matteo fabro** [07:23:42]: Okay, very interesting.

**matteo fabro** [07:23:44]: Thank you for that.

**matteo fabro** [07:23:45]: So obviously you have experience with this to some extent.

**matteo fabro** [07:23:51]: And okay, so I understand the challenges and like if I can ask you also, I mean, what went well, like in terms of like things you found to be like to have potential, but that like you didn't fully manage to exploit, but that in an alternative scenario you think would have been like valuable to

**matteo fabro** [07:24:13]: explore further.

**matteo fabro** [07:24:15]: I think that would also be very used.

**matteo fabro** [07:24:16]: So

**David Orban** [07:24:17]: what was very clear that there is an extreme appetite for something like this.

**David Orban** [07:24:22]: We had people with active deployed capital in the three, four hundred million dollar range ready to start working with us, you know, starting to put in a little bit of money and then progressively increase the amount.

**David Orban** [07:24:44]: And that was very positive because it clearly shows that if you have the ability to show a good return, then you can find the capital to trade with.

**David Orban** [07:25:08]: What was, I think, not sufficiently modeled is the various indicators that the trading would

**David Orban** [07:25:28]: be able to match the risk appetite for the right kind of investor rather than going too broad.

**David Orban** [07:25:36]: It is better to

**matteo fabro** [07:25:37]: characterize the type trade and

**David Orban** [07:25:40]: then match it with the right kind of investor rather

**matteo fabro** [07:25:45]: than... Do you mind rephrasing that?

**David Orban** [07:25:49]: Okay, so the algorithm will... embody over time a certain type of behavior where whatever gains you have in a quarterly or a yearly period between you will have bad days or bad weeks when the fund gives up the gains or even dips into losing money at least temporarily.

**David Orban** [07:26:37]: And since this is possible and especially initially very important to be transparent with your investors, you will show the investors how everything is going.

**David Orban** [07:26:52]: And if you find people who are not compatible with the behavior that the trading algorithm embodies, then there is a mismatch, either because they will believe that you are not aggressive enough, if their risk appetite is higher than what you are showing, or because they will freak out because you

**David Orban** [07:27:18]: have a 10% drawdown, even though just temporarily, And they want to pull the capital, right, depending on your agreements.

**David Orban** [07:27:31]: So that is what I mean that the algorithm embodies a behavior that must match the risk profile of the right kind of investor.

**David Orban** [07:27:45]: And the better you are able to defined those characteristics, the more likely you are able to target the right people.

**David Orban** [07:27:57]: So, so that is one.

**David Orban** [07:28:03]: I had another thing in mind.

**David Orban** [07:28:04]: Yes,

**David Orban** [07:28:10]: so depending on so many factors, of course, one one question for me and we at the time with quantum economy didn't get to that point at all but one question is what meta level must be implemented so that the algorithm realizes when the market has internalized its approach and it must upgrade itself

**David Orban** [07:28:51]: because whatever works for a given period of time will stop working after a while.

**David Orban** [07:28:57]: And that is why there are entire teams of researchers and quants working on the algorithms all the time at the large funds, because they do this manually.

**David Orban** [07:29:13]: So for me, the interesting question is not only Can an algorithm work because absolutely it can?

**David Orban** [07:29:21]: But how can the algorithm understand its own need to evolve and when to trigger a switch in a new version, which of course has its own risks and how do you disclose that with the investors?

**David Orban** [07:29:39]: that the algorithm itself is changing because with a traditional mind, with a traditional mindset, they will say, okay, show me back testing for one year of the new algorithm.

**David Orban** [07:29:54]: And you will tell them, well, no, I cannot back test the new algorithm because it is now fit for the new market.

**David Orban** [07:30:02]: And then they will say, okay, then why don't we wait a year so that we can prove that the new algorithm works on the new market, and then I will put in the money, and then you say, well, no, because if you need to wait another year, then maybe I will need to change the algorithm again.

**David Orban** [07:30:24]: So explaining the changing nature of the game is also an important communication challenge, in my opinion.

**David Orban** [07:30:35]: Okay,

**matteo fabro** [07:30:35]: thanks for that.

**matteo fabro** [07:30:36]: I wrote everything down very clearly.

**matteo fabro** [07:30:38]: I can send it to you after you want, just so you can review your thoughts.

**matteo fabro** [07:30:43]: Also, I wanted to ask to like one last point.

**matteo fabro** [07:30:48]: I understood like challenges, potential reflections and so on.

**matteo fabro** [07:30:54]: If you had to outline, like before we go back to my work, if you had to outline like the major learning or learnings like from this experience, like what would it be in terms of like both technical and also like non-technical.

**matteo fabro** [07:31:12]: Like I see that thing.

**David Orban** [07:31:15]: No, sorry, ask the question again.

**matteo fabro** [07:31:18]: Like if you had to like outline what you really like brought home with you in terms of like, not necessarily specific to this, but like really the key lesson that you learned.

**matteo fabro** [07:31:32]: Um, just so I can avoid making anything earlier this and like you can just reflect on it as well.

**matteo fabro** [07:31:38]: Like any, like, you know, really what you brought back where you think like this is what really I got out from, from the experience.

**David Orban** [07:31:48]: There are many of course, and some can apply to you, others not.

**David Orban** [07:31:56]: We didn't have a sufficient degree of communication in the team.

**David Orban** [07:32:03]: We didn't have enough skin in the game, which investors definitely want.

**David Orban** [07:32:09]: We were not always able to differentiate between when the algorithms would not perform correctly and when instead we were just observing behaviors in the market, like front running our trades or, you know, whatever could have impacted negatively the performance of the algorithm.

**David Orban** [07:32:44]: Some lessons are really important things that work on paper, not necessarily work in real life.

**David Orban** [07:32:55]: There were some relatively complicated but quite beautiful round trips across three, four exchanges that appeared to work very well on paper, but once you tried to execute them, they just couldn't.

**David Orban** [07:33:15]: either because of execution time or the cost of execution eating into the profits.

**David Orban** [07:33:28]: The infrastructure at the time, and of course today it could be much better, was a bit wobbly, and sometimes we could not collect the right amount of data because our backend infrastructure wasn't robust enough.

**David Orban** [07:33:51]: Yeah, so these were some of the things that I remember learning

**matteo fabro** [07:34:07]: Okay, just took a second there.

**matteo fabro** [07:34:09]: My typing speed is good, but still need a bit

**David Orban** [07:34:13]: course you type permanent.

**David Orban** [07:34:14]: I have my note taker in the call, so I will be able to send you the

**matteo fabro** [07:34:18]: meeting.

**matteo fabro** [07:34:18]: Okay, okay.

**matteo fabro** [07:34:19]: Thank you, yeah.

**matteo fabro** [07:34:20]: But I like to type because it just like helps me remember, help me think and stuff.

**David Orban** [07:34:25]: Okay, so well,

**matteo fabro** [07:34:27]: thanks for that, first of all.

**matteo fabro** [07:34:29]: Always good to learn from others' experiences, I would say.

**matteo fabro** [07:34:33]: Okay, so in terms of what I'm doing, Let me share my screen again.

**matteo fabro** [07:34:39]: Can you hear me clearly, so slightly more or less?

**David Orban** [07:34:43]: Yes.

**David Orban** [07:34:44]: Might be some, okay, thank you.

**David Orban** [07:34:46]: Might

**matteo fabro** [07:34:46]: be some distortion of stuff, but... Wait, I will share my screen here.

**matteo fabro** [07:34:53]: It seems...

**matteo fabro** [07:34:59]: Let me share my screen, but let me try.

**matteo fabro** [07:35:02]: Oh, no, So, okay, so in terms of like what I'm doing, basically I have like a couple of options in terms of what I can do.

**matteo fabro** [07:35:12]: Obviously I can do them both, but they're fundamentally different, so I think it's good to like just define them clearly.

**matteo fabro** [07:35:22]: And just to give you like background on what I'm going to do my best practice.

**matteo fabro** [07:35:27]: So basically like the two main things that I could do.

**David Orban** [07:35:30]: This is obsidian, right?

**David Orban** [07:35:32]: Yes, sir.

**matteo fabro** [07:35:33]: Okay.

**matteo fabro** [07:35:35]: is my life.

**matteo fabro** [07:35:38]: I spend more time in Obsidian that I think I've spent with my family over the last two years.

**matteo fabro** [07:35:45]: But, um, it's not like this.

**matteo fabro** [07:35:48]: Okay, so basically the two things that I can optimize for and that, like, I will be working on, like, either, um, generating like direct trading signals.

**matteo fabro** [07:36:02]: So this would be like more relevant to what you did.

**matteo fabro** [07:36:06]: I think it definitely has potential if done properly.

**matteo fabro** [07:36:10]: However, as I'm sure you know, from your experience, challenging to generate alpha, very challenging, directly, very challenging to... You know, just build a fund in general, because like, once you have like a good strategy, then at that point, you're not like selling the solution to funds anymore.

**matteo fabro** [07:36:33]: You're like more in the realm of like, actually, uh, I think it's possible, uh, but at the same time, extremely challenging, It's a big question mark to what extent it will work.

**matteo fabro** [07:36:50]: Then this is the other one, which is more in line with providing solutions to funds, providing my expertise and stuff with regards to AI development, but not necessarily running a strategy myself.

**matteo fabro** [07:37:06]: I'm running like the complexity of, you know, raising a fund and so on, which is just like doing more like on the Kwan's research side, so having the agent instead of directly providing signals, so like Faisal and so on, and so forth, and so forth.

**matteo fabro** [07:37:23]: It's more like just defining the relevant models and features that can be explored.

**matteo fabro** [07:37:28]: And then providing these two bonds, which would bend to like the philosophy of analysis themselves, burning the models themselves, and so on.

**matteo fabro** [07:37:37]: So I basically have to like decide between the two, which approaches makes more sense, which is like you would like you would like to listen to positive outcomes.

**matteo fabro** [07:37:47]: Of course, I can do both because once you have the... So I think that generating this scaffold is pretty easy for me.

**matteo fabro** [07:37:56]: I don't think I would find it particularly challenging.

**matteo fabro** [07:38:00]: The problem is in running and optimizing And so, yeah, I'm kind of very undecided in terms of what I want to do between these two.

**matteo fabro** [07:38:12]: This obviously is easier... to at least, yeah, I think it's easier to find something just yeah it's like easier because here you're doing like more traditional like quantitative research you're you're providing solution to fund which then like run the strategies themselves or like they tweak the

**matteo fabro** [07:38:35]: strategies according to their needs whereas with this like obviously you're you're running a strategy yourself and it becomes like much more complex you have to also like figure out everything that goes along with you know, running font, raising for font and so on, which I think would be very

**matteo fabro** [07:38:53]: challenging.

**matteo fabro** [07:38:54]: So, yeah, I don't know.

**David Orban** [07:38:57]: Yes.

**David Orban** [07:38:57]: So, um,

**David Orban** [07:39:04]: the, the question that you can ask yourself is, is, um, what, Where do your skills lie and what are the things that you enjoy doing and that you can do well?

**David Orban** [07:39:23]: Also, as importantly, what are the skills that not only you don't have, but you do not want to develop, because you don't have the time or you know that you wouldn't be good and the investment in developing that skill would be wasted, would be negative, or the return on that investment would be

**David Orban** [07:39:54]: negative.

**David Orban** [07:39:55]: So definitely implementing an algorithm for fund and then raising the money and then running the fund requires a 360 degree dedication where the person, the founder has to steal themselves.

**David Orban** [07:40:25]: And at the beginning, which could very well be three, four years, do a lot of things that they are not good at and they don't like doing, but they have to be done.

**David Orban** [07:40:39]: and the resources are not yet there to delegate those to others.

**David Orban** [07:40:47]: One of the mistakes at Quantonomy was actually that I joined too soon.

**David Orban** [07:40:57]: It wasn't yet time, and what I could help with often wasn't needed, and what was needed I couldn't necessarily provide.

**David Orban** [07:41:10]: What you have to look out for in the scenario where you are selling the algorithm rather than selling the fund is that it allows you to get more easily distracted.

**David Orban** [07:41:32]: finding the clients and and persuading them that it is worth paying attention to you requires continuity of effort over, again, probably not just a few months, but longer, because they will want to know what they are paying for, they get support or they get additional needs or development if that is

**David Orban** [07:42:07]: necessary, or as the market changes, you will be able to provide them with updates to the strategy, and in turn, that means that you need to keep your focus there too, following that line of action and following the clients.

**David Orban** [07:42:27]: even if this is a more narrow focus than the one of building the entirety of the fund.

**David Orban** [07:42:40]: So these are some of the questions that you should ask yourself as you decide between these two options.

**David Orban** [07:42:50]: A third option that you did not mention is to join a fund rather than providing as a vendor algorithms and strategies to a fund.

**David Orban** [07:43:03]: You could become part of the team.

**David Orban** [07:43:07]: And whether you want to do that or not, depends on the answer on another set of questions.

**David Orban** [07:43:16]: Because in crypto especially, many funds are remote.

**David Orban** [07:43:23]: So you could work and live wherever you want, but also they are extremely volatile.

**David Orban** [07:43:32]: When the market is good, they get formed, they do their thing, in a bull market, they can show results.

**David Orban** [07:43:54]: And then when the bear market comes, 80% just close shop because they cannot perform in a bear market.

**David Orban** [07:44:03]: That was actually one of our open questions because your benchmark in the public markets is the S&P 500. You have to outperform the S&P 500, otherwise, why run the risk?

**David Orban** [07:44:26]: In the crypto markets, your benchmark is Bitcoin.

**David Orban** [07:44:31]: You have to outperform Bitcoin, otherwise why bother?

**David Orban** [07:44:35]: Just keep the money in Bitcoin, right?

**David Orban** [07:44:38]: So the pro of a crypto fund is flexibility, the con of a crypto fund is volatility.

**David Orban** [07:44:51]: existential volatility, you know, live or die.

**David Orban** [07:44:55]: If you were to consider joining a traditional team, a hedge fund, they would say, okay, come and work with us in New York, and then that would be good or bad.

**David Orban** [07:45:09]: Also, I'm sure you would learn a lot, but also you would have to be very disciplined about what you do, what you don't do, And in a corporate environment you may have a hard time abiding by that discipline.

**David Orban** [07:45:29]: So again, those are the things that you could consider.

**David Orban** [07:45:35]: Pay would be very good, but for example, New York expenses would be very high.

**David Orban** [07:45:41]: So you wouldn't necessarily put away a lot of money.

**David Orban** [07:45:47]: So yeah, that is a third question that you can ask yourself, building a fund, selling strategies and algorithms, or joining a team.

**David Orban** [07:46:01]: Yeah,

**matteo fabro** [07:46:02]: I mean, like, obviously, like, as I was saying, we were saying, like last time, I mean, I subscribe to pretty fast tape-off hypothesis, so obviously the idea of getting like a normal

**David Orban** [07:46:16]: job and so on.

**David Orban** [07:46:16]: We have a date, September 2028. Yeah.

**David Orban** [07:46:22]: Open AI announced the data of the singularity.

**matteo fabro** [07:46:27]: Yeah, so I mean, obviously like getting a job and so on is kind of ridiculous at this point.

**matteo fabro** [07:46:36]: So that's definitely off the table.

**matteo fabro** [07:46:38]: aside from the fact that I'm not a job type of person in general, but even more so now.

**matteo fabro** [07:46:45]: With regards to the various other points you mentioned, in terms of like, I think it would be probably easier for me to go like directly through the model hypothesis and so on because like I already have like pretty strong relationship with like a lot of funds like satanel for example I've been

**matteo fabro** [07:47:08]: speaking to like one of the key decision makers with this type of sourcing you know with like basically all of the quantons you know I'm like very very close to them like I know them like personally like I know you so It's I mean, I feel like that would probably be the easier thing in the shorter

**matteo fabro** [07:47:28]: term.

**matteo fabro** [07:47:29]: But in the longer term, I mean, obviously, if I could like find some pretty strong signals and stuff, that would also be like extremely valuable in the long term.

**matteo fabro** [07:47:41]: I feel like this approach that I have is extremely innovative, like very much state of the art.

**matteo fabro** [07:47:47]: Like I don't think anybody else is doing like this sort of thing at quant puns.

**matteo fabro** [07:47:52]: So probably there's a lot of potential there.

**matteo fabro** [07:47:55]: At the same time, yeah, I mean, I don't know, like I could do both, but the problem with doing both, obviously, is that you don't optimize for one.

**matteo fabro** [07:48:06]: And then at that point, like the risk goes like not doing anything properly.

**David Orban** [07:48:11]: What stops you from just trading a little bit of your own money?

**matteo fabro** [07:48:19]: Yeah, so at that point, so at that point, yeah, exactly, I would be doing more on this side, so like trading execution and so on.

**matteo fabro** [07:48:28]: And that's like more... more, yeah, on this side of the spectrum.

**matteo fabro** [07:48:35]: I can do both, yeah, so I can do like this for funds and this, like on the proprietary side, and then see if it goes well, potentially working with like this crypto fund, because like this crypto guy that I'm speaking with, as I said, he's like an ex-high-requency trader at Citadel, he did like,

**matteo fabro** [07:48:54]: Taltech, either like masters at Berkeley, postdoc at MIT.

**matteo fabro** [07:49:00]: So he's obviously very good.

**matteo fabro** [07:49:01]: He suggested the same infrastructure.

**matteo fabro** [07:49:03]: So think he has a lot of potential.

**matteo fabro** [07:49:07]: He already said that he wants to work with me and so on.

**matteo fabro** [07:49:09]: So potentially I can do something with him on this side.

**matteo fabro** [07:49:13]: And then I have other potential partners on this side.

**matteo fabro** [07:49:17]: And yeah, I mean, if I can find something here, like, of course, I'm very happy to speak with you as well.

**matteo fabro** [07:49:25]: Obviously, like, this, I suppose, is not super relevant to what you do at the moment.

**matteo fabro** [07:49:31]: But yeah, I think, yeah, potentially, I could explore both.

**matteo fabro** [07:49:35]: It kind of makes sense also because like this scaffold is like singular.

**matteo fabro** [07:49:39]: And then once I have that, the problem is like running the compute because it's like super expensive.

**matteo fabro** [07:49:44]: I am sponsored by like Microsoft and Google.

**matteo fabro** [07:49:46]: So I do have like 50K in credits that I can more or less, but I can spend like for compute optimization.

**matteo fabro** [07:49:53]: I just have to make sure that I like play them well, you know, that I don't waste them.

**matteo fabro** [07:49:59]: Running like this scaffold property, I think it's gonna be like 10K plus.

**matteo fabro** [07:50:04]: even 20k.

**matteo fabro** [07:50:06]: So basically, if I do both, I'm probably gonna spend all of my compute.

**matteo fabro** [07:50:12]: But I do think that this really has a lot of potential like, I mean, this like self-improvement strategy like this, you know, using the evolutionary algorithm for, know, defining the regime model, and then like using this, I think is extremely valuable, like target golden machine for like agent

**matteo fabro** [07:50:32]: optimization.

**David Orban** [07:50:34]: what I also recommend, even for your own benefit is to prepare two documents, one pager and pitch deck, even if you don't raise a fund, because it forces you to articulate in a crisp, concise manner the approach, the problem that you are solving, why you believe you will be successful, what are your

**David Orban** [07:51:14]: financial needs and so on, right?

**David Orban** [07:51:17]: And then you know two things.

**David Orban** [07:51:23]: One, that you clearly understand the points because you were able to put them on paper, two, if you need to explain to someone or show to someone, you have a base point where to start.

**David Orban** [07:51:47]: And if you believe that is useful and you want to send me the first version of those two documents, I will be happy to give you feedback.

**David Orban** [07:51:59]: And I think that can be a good exercise regardless of what you decide to do.

**matteo fabro** [07:52:08]: Okay, yes, thank you so much.

**matteo fabro** [07:52:11]: I have a phone in like five minutes, but I will send you this material.

**matteo fabro** [07:52:16]: I will continue like on the technical side for sure.

**matteo fabro** [07:52:23]: then we can act like in one or two weeks, like electional, like what I'm doing.

**matteo fabro** [07:52:31]: I will probably, sure continue the conversation with like the crystal guy, I'm now speaking with like some really good font like today I set a meeting with one who's like an ex-VP of two sigma and his partner achieved like the ex-head of an alliance at two sigma and two sigma is probably the

**matteo fabro** [07:52:50]: strongest one they were one of the co-alters on DSPy paper, which is like one of the self-improvement architecture before Satana came along.

**matteo fabro** [07:53:02]: So I think definitely there's a lot of potential here on both sides.

**matteo fabro** [07:53:08]: I will see what I can do on the technical side.

**matteo fabro** [07:53:11]: Hopefully I can demonstrate like something material within a couple of weeks on at least one of the two points.

**matteo fabro** [07:53:19]: And then we can reconnect and see your thoughts on things.

**matteo fabro** [07:53:24]: And if there's like any way we can forward on anything together, like do something in any sort of way, shape or form.

**David Orban** [07:53:31]: Okay.

**David Orban** [07:53:32]: Thank you so much, David.

**David Orban** [07:53:33]: I will send

**matteo fabro** [07:53:34]: the material, you know, by tomorrow, like one of these days.

**David Orban** [07:53:38]: Take your time.

**David Orban** [07:53:39]: Take your time, no worries.

**David Orban** [07:53:40]: Okay.

**David Orban** [07:53:41]: Thanks again,

**matteo fabro** [07:53:42]: really.

**matteo fabro** [07:53:43]: Thanks for your time, really.

---
*Backed up from MeetGeek on 2026-03-30 08:55*
