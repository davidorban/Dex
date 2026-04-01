# Quant Research Progress & Workflow

**Date:** 2025-11-27
**Duration:** Unknown
**Meeting ID:** 88ca14ef-f1ad-43fc-be90-d0a015d954d6

## Participants
- *Participants not listed*

### Summary

Matteo presented progress on an LLM-driven quantitative-research agent adapted from a Darwin/Gödel scaffold that generates feature and model hypotheses; he reported a promising crypto information coefficient (~0.095) while acknowledging prior poor results and stochastic outputs. They discussed validation rigor, model selection trade-offs, and engineering choices—Matteo runs agents from his phone connected to Databricks/VMs and prefers direct code uploads to avoid interrupting runs. David suggested papers and tools (nested learning, Anthropic/Claude flow) and proposed an introduction to Garrett Lisi; Matteo emphasized focusing on research hypotheses (not full trading strategies), alternating default-mode and focused work to boost creativity, and plans to push strict validation runs and extend to equities later.

## Full Transcript

**Unknown speaker** [19:00:02]: Thank you

**Unknown speaker** [19:00:46]: Good.

**Unknown speaker** [19:01:37]: Hello,

**Matteo Fabro** [19:01:37]: David.

**Matteo Fabro** [19:01:37]: How are you?

**Matteo Fabro** [19:01:39]: I am

**David Orban** [19:01:40]: good.

**David Orban** [19:01:40]: And you, is your Wi-Fi better than Bali?

**Matteo Fabro** [19:01:44]: Yeah, no, I'm not using Wi-Fi.

**Matteo Fabro** [19:01:47]: I'm just using cellular so you don't mind taking off the camera so that I don't burn all my data that would be really useful if you don't mind.

**Matteo Fabro** [19:01:58]: Okay.

**David Orban** [19:02:03]: Before I do that.

**David Orban** [19:02:05]: Let me just show you that we are in a different vibe from Hawaii and I'm in front of the fireplace.

**Matteo Fabro** [19:02:15]: That's nice.

**David Orban** [19:02:17]: With the

**Matteo Fabro** [19:02:17]: dog.

**Matteo Fabro** [19:02:18]: All

**David Orban** [19:02:22]: right.

**David Orban** [19:02:22]: Nice.

**Matteo Fabro** [19:02:25]: No, yeah, I'm in Hawaii.

**Matteo Fabro** [19:02:29]: very nice.

**Matteo Fabro** [19:02:39]: Here we go.

**Matteo Fabro** [19:02:42]: So I was saying, I'm in Hawaii right now.

**Matteo Fabro** [19:02:44]: It's very nice.

**Matteo Fabro** [19:02:46]: Like I came here just, you know, to focus, to work.

**Matteo Fabro** [19:02:52]: How long

**David Orban** [19:02:53]: were you in Bali?

**Matteo Fabro** [19:02:55]: I did like one week in Bali, two weeks in Thailand.

**Matteo Fabro** [19:03:01]: I was hoping that like I could have used that time to work and stuff.

**Matteo Fabro** [19:03:08]: I mean, did work.

**Matteo Fabro** [19:03:09]: quite a bit, but like, not as much as I wanted to, so I

**David Orban** [19:03:14]: can.

**David Orban** [19:03:14]: How long are you planning to stay in Hawaii?

**Matteo Fabro** [19:03:21]: However, no, I mean,

**David Orban** [19:03:24]: the reason I'm asking is because obviously it is up to you, but I could have introduced you to people who I would assume you would have enjoyed to meet in Bali.

**David Orban** [19:03:40]: I can introduce you to people who you may enjoy to meet in

**Matteo Fabro** [19:03:44]: Hawaii.

**Matteo Fabro** [19:03:58]: Absolutely.

**Matteo Fabro** [19:03:59]: I mean, it would be super great to meet, of course, people and stuff like that.

**David Orban** [19:04:04]: So and I am I am referring to people who have similar interests as you, right?

**David Orban** [19:04:13]: So

**Matteo Fabro** [19:04:14]: yeah, yeah, yeah.

**Matteo Fabro** [19:04:16]: Yeah, for sure.

**Matteo Fabro** [19:04:16]: I mean, if you know somebody that's here, that's, you know, cool, but like they don't even if they're not like into AI and stuff like.

**Matteo Fabro** [19:04:25]: I mean, I'm friends with everyone, like, I don't know, yesterday, I hung out with this guy who's like a construction worker here, but, you know, he's like, very, then I realized that, like, he's very spiritual stuff, like, he's super good at playing, like, hand fan, and, and, like, various flutes

**Matteo Fabro** [19:04:47]: and stuff.

**Matteo Fabro** [19:04:48]: So, I mean, like, I'm open to meeting anyone, you know, it doesn't have to be, like, an AI nerd.

**Matteo Fabro** [19:04:54]: like me,

**David Orban** [19:04:56]: so it

**Matteo Fabro** [19:04:57]: depends.

**Matteo Fabro** [19:04:59]: Anyway, no, yeah, like today, oh, did you leave?

**Matteo Fabro** [19:05:05]: Are you here?

**David Orban** [19:05:06]: Yes, yes.

**David Orban** [19:05:07]: Okay, okay,

**Matteo Fabro** [19:05:08]: meet like switched off.

**Matteo Fabro** [19:05:11]: But yeah, like today I just wanted to like very quickly, like just share like the results that I'm but having right now with what I'm doing.

**Matteo Fabro** [19:05:26]: I think they're like very promising, very exciting.

**Matteo Fabro** [19:05:31]: Obviously, I mean, disclaimer is not perfect yet.

**Matteo Fabro** [19:05:37]: So, like, just to give you an overview, basically, since we spoke last time, had a bit of a change in the sense that, like, last time we spoke, I was more in the realm of like the arena bench approach where they do, you know, you remember like basically just the agents, they have them like trade

**Matteo Fabro** [19:06:03]: cryptos directly and stuff.

**Matteo Fabro** [19:06:06]: So that approach I think could potentially work, but I don't think at this stage, I mean, I don't know if you saw the arena bench results, so they were pretty poor.

**Matteo Fabro** [19:06:23]: then like i mean they didn't give the agent like alternative data they just gave them like market data which i think they'll change now in the second run but still i think i think it's kind of a stupid approach in general the the guy that did it obviously I mean, I don't mean to be a scientist or

**Matteo Fabro** [19:06:48]: anything like he doesn't look super smart.

**Matteo Fabro** [19:06:51]: So I basically took the hint and stuck with my initial plan, which was basically what, you know, Cetadel had asked me what I'm working on with also this other quant researcher who's like pretty big, he's like ex vice president at two Sigma.

**Matteo Fabro** [19:07:15]: His partner is X, head of LLM, 2 Sigma, which is like, you know, one of the best quantitative firms.

**Matteo Fabro** [19:07:24]: They, like, were co-contributors on the SPI paper and so on.

**Matteo Fabro** [19:07:28]: So, they're pretty good.

**Matteo Fabro** [19:07:30]: And basically, you know, the approach is that of having the LLMs, like the agents come up with like quantitative model hypotheses, like features and model hypotheses, which are then basically, you know, tested and, you know, the goal is that of basically finding, you know, good models that have

**Matteo Fabro** [19:07:53]: strong predictive power, you know.

**Matteo Fabro** [19:07:57]: And so for the initial run, I did like crypto that I'm gonna do equity afterwards, like what?

**Matteo Fabro** [19:08:05]: I'm gonna do like both, but yeah, like right now I'm just working on finishing up the crypt, so I wanna get that to work like decently.

**Matteo Fabro** [19:08:15]: So after one month, I basically finally managed to get the system to actually work in the sense that basically what it does, I just adapted the Darwin Godel machine by Sakana.

**Matteo Fabro** [19:08:33]: to this pretty much.

**Matteo Fabro** [19:08:37]: So like, yeah, I basically just adopted the system.

**Matteo Fabro** [19:08:43]: You know, I adopted the scaffolding so that basically the base coding agent becomes a quantitative coding agent.

**Matteo Fabro** [19:08:53]: And yeah, basically the whole evaluation frameworks like revolves around just quantitative developments, quantitative testing, identifying, you know, metrics like IC, like, you know, all of these like stability and stuff.

**Matteo Fabro** [19:09:15]: I was also including Sharp before, like risk-adjusted returns, etc.

**Matteo Fabro** [19:09:21]: But I like now I've thought about it a bit, and like since the task, the original task was coming up with feature and model hypotheses and not developing trading strategies.

**Matteo Fabro** [19:09:36]: I basically removed Sharp from the fitness function because I mean that's more like implementation and stuff and I don't think makes sense to focus on too many things.

**Matteo Fabro** [19:09:51]: So at the current stage, I'm just considering information quotation, stability, hit rate, that sort of thing.

**Matteo Fabro** [19:09:59]: And then, like, obviously, it's going to be the quantitative firm's role to actually implement the models and the hypothesis to get, you know, go to risk-contrastor returns.

**Matteo Fabro** [19:10:12]: And yeah, I sent you, like, the document, which basically demonstrates that the agent managed to improve itself.

**Matteo Fabro** [19:10:23]: So we started off with like an agent that was producing like very skewed results, you know, very stochastic information coefficients and stuff.

**Matteo Fabro** [19:10:44]: So obviously I'm not an expert at once myself, so I have to like discuss the details with other people.

**Matteo Fabro** [19:10:52]: I have quite a few points that I'm working with, but like, I mean, I have like a decent understanding and I would say that, yeah, I mean, did the agent basically manage to find kind of a bug in its implementation and fix it?

**Matteo Fabro** [19:11:10]: And we got a very high information coefficient, so we got 0.095, which is basically as good as you can get.

**Matteo Fabro** [19:11:20]: Like in practice, it's extremely good.

**Matteo Fabro** [19:11:23]: It's indicative of like actual production readiness, because if it was like, I don't know, 0.5, that would be like way too high in these.

**Matteo Fabro** [19:11:34]: There's definitely overfitting.

**Matteo Fabro** [19:11:35]: It means there is something wrong with the system, but like 0.095 is like really the, because I mean, usually like 0.05 is the cutoff where funds start using a strategy.

**Matteo Fabro** [19:11:52]: And, you know, 0.1 is usually the highest call off after, like, above 0.1 you know you start to have to like scrutinize it a lot and see you know if there's overfitting and stuff and you start having you know some serious doubts about seriousness so we go like 0.05 sorry sorry 0.095 which is like

**Matteo Fabro** [19:12:19]: basically you know as high as you can get without like going above the overfitting threshold So, you know, it's very, very promising.

**Matteo Fabro** [19:12:29]: Obviously in crypto, it's easier to get the results because, you know, markets are way less efficient.

**Matteo Fabro** [19:12:38]: So, you know, obviously, in equity is going to be way more difficult to get something like this.

**Matteo Fabro** [19:12:43]: Crypto markets are much smaller, much, you know, less liquid, less tradeable in many ways, I think.

**Matteo Fabro** [19:12:53]: I mean, you're not saying it's perfect or anything, but you know, I think it's a good, very good start to the thing.

**Matteo Fabro** [19:13:00]: And, you know, it allows me to keep tweaking the thing and just like keep working on it and then potentially like, you know, in the, in the future apply it to two things that go beyond on finance as well.

**Matteo Fabro** [19:13:14]: So

**David Orban** [19:13:15]: a few, you know, pieces of feedback and

**Matteo Fabro** [19:13:20]: questions.

**David Orban** [19:13:22]: Are you planning to do a stronger adversarial testing where you improve the or evolve even the validation?

**Matteo Fabro** [19:13:38]: Yeah, exactly.

**Matteo Fabro** [19:13:40]: Jackson.

**Matteo Fabro** [19:13:42]: Yeah, I mean, evolve the validation.

**Matteo Fabro** [19:13:45]: That's an interesting question.

**Matteo Fabro** [19:13:49]: that I didn't think about, but I don't know honestly to what extent that would be useful, but I'm gonna write it down because it's

**David Orban** [19:13:59]: interesting.

**David Orban** [19:14:02]: And to what extent do you store an archive of the strategy genomes?

**David Orban** [19:14:11]: as you iterate across generations so that you can you can enable a

**Matteo Fabro** [19:14:19]: kind

**David Orban** [19:14:19]: of a recursive advance in features or models

**Matteo Fabro** [19:14:24]: or

**David Orban** [19:14:24]: even research strategy

**Matteo Fabro** [19:14:27]: no yeah so it's super interesting because basically we don't evolve the so I mean there are a few questions there so let me start with the validation.

**Matteo Fabro** [19:14:39]: I definitely have like the validation that I used on that approach of like a walk forward analysis with six months, six months trained, one month test, one month validate.

**Matteo Fabro** [19:14:54]: So we're basically, yeah, I mean, just very basic.

**Matteo Fabro** [19:15:03]: And I've now implemented like way more advanced validation, so like production level.

**Matteo Fabro** [19:15:13]: And I've tried to run like a 30 generation run, unfortunately.

**Matteo Fabro** [19:15:21]: think either the validation is too strict or there is some other issue, but like we haven't been able push IC above zero.

**Matteo Fabro** [19:15:31]: in this run.

**Matteo Fabro** [19:15:32]: I mean, I'm on like the ninth generation.

**Matteo Fabro** [19:15:34]: I stopped it.

**Matteo Fabro** [19:15:35]: I'm like on the ninth generation, but I was able to push IC higher than zero with this validation.

**Matteo Fabro** [19:15:44]: It could also be the like Like, and my outputs are very stochastic, so it's possible that like the improvements that were previously identified were missed this time, even if last time was just one generation, it's possible that it was particularly lucky.

**Matteo Fabro** [19:16:02]: So, I don't know, there are many reasons for why it didn't work.

**David Orban** [19:16:06]: Another point.

**David Orban** [19:16:09]: is that you should introduce real world constraints sooner rather than later

**Matteo Fabro** [19:16:16]: so that solution

**David Orban** [19:16:18]: doesn't lead to reward hacking.

**David Orban** [19:16:21]: but that it is aligned with robust PNL, whether it

**Matteo Fabro** [19:16:28]: is... Yeah, yes and no.

**David Orban** [19:16:31]: Or go

**Matteo Fabro** [19:16:32]: down and

**David Orban** [19:16:34]: other variables that will influence real world trading

**Matteo Fabro** [19:16:40]: behavior.

**Matteo Fabro** [19:16:41]: Yeah, so I mean, I'm gonna push back on that a bit because like, as I was saying, this implementation is more like about generating quantitative model and feature hypothesis.

**Matteo Fabro** [19:16:55]: So the keyword there is hypothesis, you know, we're not generating quantitative model and feature strategy.

**David Orban** [19:17:05]: So, so, so what is, what is, what is the signal?

**David Orban** [19:17:10]: What is that you are, uh, it is the, the trading strategy that you are generating.

**David Orban** [19:17:17]: Is that correct?

**Matteo Fabro** [19:17:19]: No, so we're not generating strategies.

**Matteo Fabro** [19:17:22]: We're generating, so strategies is basically taking an idea and then actually implementing it, uh, and working around the real world constraints.

**Matteo Fabro** [19:17:35]: So basically optimizing for transaction costs, for slippage, for all of these things, for like capacity, using a hypothesis that you already have.

**Matteo Fabro** [19:17:49]: So that's like more on the quantitative development side, quantitative implementation, quantitative training, et cetera.

**Matteo Fabro** [19:17:57]: Me, I'm doing more on the quantitative research side where I'm basically providing the hypotheses.

**Matteo Fabro** [19:18:06]: And then that's where I stop because I mean, that's already very difficult.

**Matteo Fabro** [19:18:15]: And I feel like it's better to do like one thing well, especially at this stage than trying to do everything.

**Matteo Fabro** [19:18:23]: And then, you know, it comes out pretty poor because like even on the previous run, I had an information coefficient of like 0.1 basically.

**Matteo Fabro** [19:18:34]: But like I had like all of the real work constraints, so sad.

**Matteo Fabro** [19:18:37]: So I had like, you know, slippage, transaction costs, capacity calculation, etc.

**Matteo Fabro** [19:18:45]: And sharp was negative, you know, and I see was like very high.

**Matteo Fabro** [19:18:50]: So, you know, I'm sure that a good quant could have taken that and probably it work.

**Matteo Fabro** [19:18:58]: But I mean, I never quote myself and you know my I that's not part of the value proposition at this stage, like at this stage more just getting a good signal.

**Matteo Fabro** [19:19:10]: You know, and then, and then, like, maybe at a future date, potentially, but probably, you know, maybe not even.

**Matteo Fabro** [19:19:20]: Because I'm not interested in, like, trading markets directly.

**Matteo Fabro** [19:19:24]: I'm not particularly interested in, like, opening up fund myself.

**Matteo Fabro** [19:19:28]: I mean, the whole point of this is just to, like, optimize, you know, work with quant funds, develop and so on.

**Matteo Fabro** [19:19:37]: And then like, you know, move on to something else, like, I don't want to, you know, play in finance forever, because I mean, I don't, I don't particularly like the game, you know, it's fine, like, it's not like I dislike it, but it's also not my passion, you know,

**David Orban** [19:19:54]: not something

**Matteo Fabro** [19:19:55]: that I would say I... Did

**David Orban** [19:19:58]: you see the nested learning paper from Google Research?

**Matteo Fabro** [19:20:05]: No, I didn't see.

**Matteo Fabro** [19:20:06]: I saw yesterday a paper came out from sample which pretty interesting.

**Matteo Fabro** [19:20:10]: It's called MetaTaxgrad.

**Matteo Fabro** [19:20:13]: Nestle Learning, I didn't see.

**David Orban** [19:20:15]: Yeah, I will send you the link on WhatsApp right now.

**David Orban** [19:20:21]: And I

**Matteo Fabro** [19:20:22]: think it would

**David Orban** [19:20:23]: be interesting for you to look at it.

**Matteo Fabro** [19:20:28]: Yeah, so I think this is more on the foundation model side, though.

**David Orban** [19:20:34]: Well, how long can you avoid to go that level deep?

**David Orban** [19:20:43]: Do you think that?

**Matteo Fabro** [19:20:44]: Yeah, forever, forever.

**Matteo Fabro** [19:20:46]: I mean, it's like asking a Python developer how long he needs to wait before going to the compiler level.

**Matteo Fabro** [19:20:53]: It's like it's just different, different languages, you know, I feel like Everybody has their own specialization doesn't make sense for me to work on in the same way that like I'm not gonna work on quantitative strategies probably, at least like not full strategies are not gonna work on like

**Matteo Fabro** [19:21:14]: foundation model development because like foundation model development is just a different beast.

**Matteo Fabro** [19:21:20]: It's like you need crazy, crazy amount of compute and it's just not doable.

**Matteo Fabro** [19:21:27]: It's like the difference between like drilling oil, refining oil and like opening a gas station, you I like, I've opened a gas station and you're asking me like, when am I going to start drilling oil?

**Matteo Fabro** [19:21:39]: You know, it's like bit different in terms of scope.

**Matteo Fabro** [19:21:45]: So I don't

**David Orban** [19:21:46]: think that I'm going to paste on WhatsApp for you now is from Anthropic, who shared some useful approaches to increase the effectiveness of long-running agents.

**David Orban** [19:22:09]: And this may be more on the level

**Matteo Fabro** [19:22:13]: that

**David Orban** [19:22:14]: we feel comfortable with.

**Matteo Fabro** [19:22:17]: Yeah, yeah, I mean, I feel like, uh, yeah.

**Matteo Fabro** [19:22:22]: I don't know, I don't know.

**Matteo Fabro** [19:22:23]: I feel like what, like the scaffold I have is pretty good.

**Matteo Fabro** [19:22:28]: Um, yeah, this, this, I feel like it's all very basic, very, very basic.

**Matteo Fabro** [19:22:32]: It's all, yeah, too basic for Have you, I mean,

**David Orban** [19:22:35]: that, uh, Gemini, uh, three pro?

**Matteo Fabro** [19:22:40]: Haven't tried it.

**Matteo Fabro** [19:22:41]: Uh, I know it's good.

**Matteo Fabro** [19:22:43]: Um, I mean, It's good in like non- coding tasks for coding like anthropic is still better.

**Matteo Fabro** [19:22:51]: Since I'm working on something that's like mostly coding.

**Matteo Fabro** [19:22:57]: haven't really implemented Gemini, but definitely interesting.

**Matteo Fabro** [19:23:01]: And really, I mean, at this point, like the difference between LLMs is like getting to a point where I mean, even kind of use, whichever is like, pretty much the same, you know, unless, I mean, depends, like, there are definitely use cases where you want to optimize a lot, but I feel like for what

**Matteo Fabro** [19:23:23]: I'm doing, like, foundation models are less relevant.

**Matteo Fabro** [19:23:26]: Like, I could even be using cloud 3.5 or, you know, an older model, I mean, doesn't really change the nature of my

**David Orban** [19:23:33]: research.

**David Orban** [19:23:38]: You did or didn't look at Opus 4.5?

**Matteo Fabro** [19:23:43]: Yeah, no, I did.

**Matteo Fabro** [19:23:44]: use it, I mean, I use it for like coding.

**Matteo Fabro** [19:23:49]: I haven't switched the foundation model in my architecture from Sonic to Opus, just because I mean, the cost is way higher it's probably worth for that cost.

**Matteo Fabro** [19:24:04]: I mean, maybe yes, I don't know.

**Matteo Fabro** [19:24:06]: I have to think about like I'm already spending like a lot of money on this, not money, but like a lot Microsoft's credit.

**Matteo Fabro** [19:24:16]: So I don't want to, I don't want to burn all of them yet.

**Matteo Fabro** [19:24:21]: So I don't know, I'll see, I'll see, I'll see, I'll Definitely.

**Matteo Fabro** [19:24:25]: I mean, the whole foundation model part is very interesting, but like,

**David Orban** [19:24:33]: in general.

**David Orban** [19:24:34]: Another tool that I enjoy a lot, and I don't remember if we discussed it at all, is Claude

**Matteo Fabro** [19:24:43]: flow,

**David Orban** [19:24:45]: which preceded the agentic approaches that anthropic itself adopted in Claude code.

**David Orban** [19:24:57]: And on GitHub, it has, I don't know, 10,000 stars, probably in downloads, you know, whatever it is.

**Matteo Fabro** [19:25:07]: And

**David Orban** [19:25:08]: it's very, very nice.

**David Orban** [19:25:10]: Yeah, I mean,

**Matteo Fabro** [19:25:11]: in general, I'm doing, is it the one that has like the little ships that come down as it's working?

**Matteo Fabro** [19:25:22]: No.

**Matteo Fabro** [19:25:24]: No, Okay, maybe that's adapted on the, I don't know.

**Matteo Fabro** [19:25:29]: But, um, no, I mean, in general, like, um, it's, yeah, I don't want to, like, I feel like the less you're, like, the less you have on your radar, the better, you know, it's like, because I already have, like, a lot of things on my plate.

**Matteo Fabro** [19:25:49]: I just need to, like, reduce things, you know.

**Matteo Fabro** [19:25:52]: Well, yeah.

**David Orban** [19:25:55]: I think that is a healthy approach as long as your heuristic your your evaluation of what to ignore and when when to break your own rule of

**Matteo Fabro** [19:26:16]: ignoring obviously yeah no no i agree i agree i agree i mean obviously it doesn't have to be taken like to the stupid extreme but like uh i feel like yeah i just need to like focus on what i'm doing at this point like at the start it was good you know to explore when like foundation models were

**Matteo Fabro** [19:26:33]: still coming out like everything was kind of a bit bad and stuff but like now that product like i'm dropping as a production level agent you know it runs on my phone why do i need to like look at other things i mean unless it's like really materially better to where you say okay i i know that it's

**Matteo Fabro** [19:26:53]: what's really better because everybody's saying it then okay but if it's just like these you know not this in particular because this obviously came before so it's interesting but like in general like one of these frameworks all these things like new foundation models i feel like it's very

**Matteo Fabro** [19:27:08]: distracting it's a full-time job you know just like keeping up with AI now is like literally a full- time job.

**Matteo Fabro** [19:27:15]: Like there are people that are literally paid just to do that and make content on that.

**Matteo Fabro** [19:27:20]: So I mean, I feel like at this point I kind of have to a bit like turn around, you know, focus on what I'm doing and then like a later date.

**Matteo Fabro** [19:27:30]: I mean, unless obviously I don't know Sakana releases Darwin Golden Machine 2, then obviously that's

**David Orban** [19:27:36]: different.

**David Orban** [19:27:37]: Exactly.

**Matteo Fabro** [19:27:39]: in general, I want to just focus on what I'm doing right now.

**David Orban** [19:27:43]: And running cloud code in the browser is such a joy.

**David Orban** [19:27:51]: Yeah.

**David Orban** [19:27:52]: I have, you know, Chrome on the phone has tab

**Matteo Fabro** [19:28:01]: collections.

**David Orban** [19:28:02]: So I have an entire tab collection.

**David Orban** [19:28:06]: with four or five instances applaud.

**Matteo Fabro** [19:28:10]: So good.

**David Orban** [19:28:12]: Each working on a different repo.

**Matteo Fabro** [19:28:15]: Yeah, I mean, I found that like for me at least like one instance is enough.

**Matteo Fabro** [19:28:23]: Like other things better to do like few things properly than like many things poorly.

**Matteo Fabro** [19:28:29]: So like I do a maximum, maybe two agents, just so like, because I have like my project in defense, which interesting.

**Matteo Fabro** [19:28:38]: And so like let it run on that, like then I let it run on the quanting, like an ever less, for example.

**Matteo Fabro** [19:28:45]: Like

**David Orban** [19:28:45]: what do you do while the agent is working?

**Matteo Fabro** [19:28:50]: Exactly.

**Matteo Fabro** [19:28:50]: So I was going to tell you about like my work setup because it's so good.

**Matteo Fabro** [19:28:55]: Basically, now I've got it to work on my phone properly, finally.

**Matteo Fabro** [19:29:01]: It works, especially with Opus 4.5, but like works so well.

**Matteo Fabro** [19:29:07]: have it connect to Databricks on Azure.

**Matteo Fabro** [19:29:14]: Like I get it to write a script to connect to data bricks.

**Matteo Fabro** [19:29:19]: Then from data bricks, SSHs into the VM, and that's where all of the code runs.

**Matteo Fabro** [19:29:27]: So it's so beautiful because I don't have to do anything locally.

**Matteo Fabro** [19:29:31]: So I literally

**David Orban** [19:29:32]: don't have to... Don't use a GitHub workflow triggers, web

**Matteo Fabro** [19:29:38]: hooks.

**Matteo Fabro** [19:29:41]: I honestly, I don't even know if it's... I mean, right now I'm just telling it to upload the code.

**Matteo Fabro** [19:29:46]: Because the annoying thing is that you have to pull request the progress.

**Matteo Fabro** [19:29:51]: So if I would have done it with web hook.

**Matteo Fabro** [19:29:54]: I don't know if it's configured with web hooks.

**Matteo Fabro** [19:29:56]: I don't think But if it is... uh even if it is like it's still annoying because like i have it means that i basically have to interrupt it while it's working have to merge the pull request i have to wait for it to upload and then i can tell it to run whereas where i was like now i'm just telling it

**Matteo Fabro** [19:30:16]: to upload the code directly so i don't have to wait for anything because

**David Orban** [19:30:20]: everything itself and and you don't use uh regardless of uh CICD

**David Orban** [19:30:31]: process and whether that is worth the effort or not.

**David Orban** [19:30:38]: Do you rely on any version control?

**David Orban** [19:30:44]: How do you roll back?

**David Orban** [19:30:47]: Of course, of course.

**Matteo Fabro** [19:30:48]: I mean, with cloud code, you have, it basically creates new branches every time it works on the browser.

**Matteo Fabro** [19:30:56]: Then you basically once you like the progress you merge to main so

**David Orban** [19:31:03]: so you are still relying on

**Matteo Fabro** [19:31:04]: github yeah, which is okay of course I mean and every time I I tell it to look its past commits like I always I tell I always tell it to look at past changes because you know context isn't that long so usually Doesn't remember what it did.

**David Orban** [19:31:22]: Well, did you see a couple of days ago or so it started compacting during a period when it wasn't running a risk of saturating the context

**Matteo Fabro** [19:31:36]: yet?

**Matteo Fabro** [19:31:37]: Yeah, I

**David Orban** [19:31:38]: mean,

**Matteo Fabro** [19:31:39]: the compact thing is decent.

**Matteo Fabro** [19:31:41]: It's not like exceptional.

**Matteo Fabro** [19:31:43]: I feel like it's obviously it's better than nothing, but like you still have to reveal the context every time, almost every time.

**Matteo Fabro** [19:31:50]: So

**David Orban** [19:31:51]: it's

**Matteo Fabro** [19:31:52]: a bit annoying.

**Matteo Fabro** [19:31:53]: But that's like the only thing.

**Matteo Fabro** [19:31:54]: Otherwise, like aside from that, you know, Iran's basically, I'm basically embracing the post-labor economy.

**Matteo Fabro** [19:32:03]: So like I just let it work and it's nice because it's slow, you know, if it was like instant, it would be annoying because then I would have to, you know, work, keep working, but

**David Orban** [19:32:14]: like, no good, because it takes

**Matteo Fabro** [19:32:18]: like 20,

**David Orban** [19:32:19]: 30 minutes.

**David Orban** [19:32:20]: Tell me about how you feel about your need modulate your level of concentration and to increase it when you need to focus, decrease it when you can turn your attention to something else.

**David Orban** [19:32:43]: Because that is the point that you just said, excessively fast AI engine would require you to pay attention at the highest level

**Matteo Fabro** [19:33:02]: to

**David Orban** [19:33:03]: an extended period of time running the risk of not being able to keep up anyway.

**David Orban** [19:33:10]: So, no,

**Matteo Fabro** [19:33:11]: I mean, I don't think I would be like not be able to keep up.

**Matteo Fabro** [19:33:14]: I mean, obviously I would prefer, I'm just joking.

**Matteo Fabro** [19:33:16]: Obviously I would prefer to be fast.

**Matteo Fabro** [19:33:19]: I mean, that's obvious, you but you know, I take advantage of the fact that it's low because, you know, attention is like, So the human mind is basically designed in such a way it has two networks.

**Matteo Fabro** [19:33:36]: It has the salience network, which is like the attention method, like where basically the mind is concentrated, like the brain is running.

**Matteo Fabro** [19:33:48]: like specific instance, you know, it's as if you're running, you know, the cloud code specific instance.

**Matteo Fabro** [19:33:55]: And, you know, it's just only that in the brain pretty much, you know.

**Matteo Fabro** [19:33:59]: So that's one warning part and obviously it's useful because it gets you to complete tasks.

**Matteo Fabro** [19:34:07]: Okay, but basically when you're doing that, like creativity is very low, divergent thinking is very low.

**Matteo Fabro** [19:34:17]: So it basically becomes very difficult to come up with ideas and so Whereas

**David Orban** [19:34:23]: like then we have maybe referring to Phanaman's Nobel Prize

**Matteo Fabro** [19:34:28]: winning.

**Matteo Fabro** [19:34:28]: No, no,

**David Orban** [19:34:29]: no, no, no,

**Matteo Fabro** [19:34:30]: no.

**Matteo Fabro** [19:34:30]: That's different, that's different.

**Matteo Fabro** [19:34:32]: So what are

**David Orban** [19:34:33]: you referring

**Matteo Fabro** [19:34:34]: I'm just referring to the two modes of the brain.

**Matteo Fabro** [19:34:39]: according to like the scientific literature there's the task mode which is like actively engaged in a task okay so you're hunting something and you're you know just looking at that super focus so that's convergent thinking that's very uh direct then obviously within these there's you know type one

**Matteo Fabro** [19:35:01]: and type two you know all sort of thing but like i'm talking more about like the broader networks in the brain.

**Matteo Fabro** [19:35:08]: I mean, you can look this up.

**Matteo Fabro** [19:35:09]: So there's like the salience network, which is which like the task specific network.

**Matteo Fabro** [19:35:15]: And then this is very interesting.

**Matteo Fabro** [19:35:16]: I think this is much more interesting than type one and type two thinking.

**Matteo Fabro** [19:35:21]: Like, I feel like this is much, much more interesting and much, much better to take advantage like, it's much more powerful because all of the great thinkers of the past really took advantage of this other network, which is the default mode network.

**Matteo Fabro** [19:35:36]: So the reason why it's called the default mode is because humans are, mean, like this by default, you know, unless they're doing something very, like that requires concentration.

**Matteo Fabro** [19:35:50]: Humans are naturally like this.

**Matteo Fabro** [19:35:52]: And so it's interesting because like basically the default mode network is like something that encourages divergent thinking, Creativity.

**Matteo Fabro** [19:36:05]: So the reason for why, I don't know, like Einstein took walks, you know, works very little and like why philosophers like work very little and did basically almost nothing.

**Matteo Fabro** [19:36:18]: And like why like all of your best ideas come in the shower is basically because like the default mode activates when you're not doing anything, you know.

**Matteo Fabro** [19:36:27]: And it just like processes all of the information that you have, and it comes up like with new insights, new ideas.

**Matteo Fabro** [19:36:34]: And this is probably

**David Orban** [19:36:35]: why the

**Matteo Fabro** [19:36:36]: reason why humans are we are, because all animals have like the salience network, you know, but only humans have the default mode network.

**Matteo Fabro** [19:36:47]: It's

**David Orban** [19:36:47]: like a... Yeah, it is a bit too ambitious to call it default because it assumes that the majority of our time is spent in the default mode.

**Matteo Fabro** [19:37:00]: Yeah, that's the problem with modern society.

**Matteo Fabro** [19:37:03]: So that's exactly the point in making.

**Matteo Fabro** [19:37:05]: So that's the problem with modern society and why so many people.

**David Orban** [19:37:08]: One of the things that I'm articulating in the various conferences and write-ups in a manner that is not too aggressive, not too on the nose in order not to offend too many people is that the mirror that AI puts in front of us will make a lot of people realize that we are zombies.

**David Orban** [19:37:34]: Most of us, most of

**Matteo Fabro** [19:37:35]: the time.

**Matteo Fabro** [19:37:36]: Yeah, most of us, most of us,

**David Orban** [19:37:37]: most of us.

**David Orban** [19:37:38]: Yeah,

**Matteo Fabro** [19:37:39]: that's the problem.

**Matteo Fabro** [19:37:40]: So basically I used to not be aware of this.

**Matteo Fabro** [19:37:43]: So like when I was not aware of this, I was like, All day, every day, I was in like task specific network.

**Matteo Fabro** [19:37:51]: I was always doing something.

**Matteo Fabro** [19:37:53]: The default network takes usually like approximately 15 minutes to activate.

**Matteo Fabro** [19:37:59]: So you need to be bored for like 15 minutes for the default network to activate.

**Matteo Fabro** [19:38:04]: So if you take a walk, like a long walk, or like if you take a long shower, or like if you can't sleep in bed, that's like when the default network activates.

**Matteo Fabro** [19:38:14]: For me, like it used to never activate because I was always doing tasks.

**Matteo Fabro** [19:38:20]: I was always doing things because, you know, AI was much worse and I wasn't even aware of this.

**Matteo Fabro** [19:38:26]: So like I never had time, you know, to be creative.

**Matteo Fabro** [19:38:30]: And that's why probably my results were so poor.

**Matteo Fabro** [19:38:33]: It's because, I mean, the task specific network is like very much an animal slash like computer network.

**Matteo Fabro** [19:38:41]: You're basically computer, you know?

**Matteo Fabro** [19:38:44]: Whereas like with the default mode network, as I was saying, is something that like only humans have.

**Matteo Fabro** [19:38:51]: And not only do they have it, but their supposed default state.

**Matteo Fabro** [19:38:57]: So where you want to pretty much, to be as human as possible.

**Matteo Fabro** [19:39:03]: And that's basically where creativity is located.

**Matteo Fabro** [19:39:06]: So now I basically switch to the other side and I try increase default mode network activity, as much as possible almost.

**Matteo Fabro** [19:39:18]: So obviously, I mean, task specific is still important.

**Matteo Fabro** [19:39:22]: If you're doing something and stuff, it's not like I completely disregard tasks.

**Matteo Fabro** [19:39:26]: But in general, since AI takes care of pretty much every task pretty well.

**Matteo Fabro** [19:39:34]: I basically now have switched to trying to come up with tasks to give it, because if you don't have the tasks, then obviously, what tasks are you going So basically what I do now optimize for this is, I come like all the way full circle because you start lazy, then you work like crazy and then you

**Matteo Fabro** [19:39:59]: come back to being lazy, you know, to optimize for this.

**Matteo Fabro** [19:40:03]: And so now like what I do is basically just, you know, as I said, I run it the phone to have like less immersion in the thing.

**Matteo Fabro** [19:40:14]: like I so just imagine like I run close my phone after like I'm sure the task is properly running and stuff I put it away usually like I'm at the beach I go like on the beach or like in the water stay there like 20-30 minutes and I really the default mode really activate really I start thinking

**Matteo Fabro** [19:40:38]: about what can I do better what can I do different Or even nothing, like even even if you don't have like any specific insight, it still helps the brain to like process and just, you know, like process for, you know, any future insight or also like the default mode network lets you recover from task

**Matteo Fabro** [19:41:00]: specific activity so that when you engage in the next task, you're way more focused do it way better.

**Matteo Fabro** [19:41:06]: So I don't know, basically I just like let this network work.

**Matteo Fabro** [19:41:11]: for like 20, 30, 40 minutes, then like I go back to my phone, I go back into like task specific activity, maybe 10 minutes, and then I go back into the thought mode for like 20, 30 minutes.

**Matteo Fabro** [19:41:22]: And this is basically how I spend my day now.

**Matteo Fabro** [19:41:25]: So, and I'm seeing I have way better results.

**Matteo Fabro** [19:41:27]: I

**David Orban** [19:41:29]: my

**Matteo Fabro** [19:41:29]: terminology

**David Orban** [19:41:32]: for the people who realize that they can avoid being zombies all the time to be luminaries.

**David Orban** [19:41:43]: Exactly.

**David Orban** [19:41:44]: To be enlightened, to be curious, to be exploring.

**David Orban** [19:41:50]: And so the hope is that interaction with AI that allows delegating more mechanical

**Matteo Fabro** [19:42:01]: thought-class

**David Orban** [19:42:03]: will free up

**Matteo Fabro** [19:42:05]: people to

**David Orban** [19:42:06]: immerse themselves and to realize that they have the opportunity and they enjoy that enlightened of being ordinary.

**Matteo Fabro** [19:42:17]: Yes.

**Matteo Fabro** [19:42:18]: I mean, and right now, like, this is like the only thing that AI doesn't really have.

**Matteo Fabro** [19:42:24]: like AI doesn't really have a default mode network obviously like doesn't it's just like all I mean it says you it's like the transformer is literally based on attention you so it's literally based on salience so it's like it doesn't have this type of divergent thinking right now and that's why like

**Matteo Fabro** [19:42:46]: the combination of human brain plus AI brain so good because you're basically If you do it properly, you're basically like combining the strengths of the two approaches, because like our task or like task specific network obviously is way less developed than like the AI attention mechanism,

**Matteo Fabro** [19:43:08]: obviously like AI approaches way more information, you know, way faster and so on.

**Matteo Fabro** [19:43:14]: it's like we're never going to be able to compete on like on creativity, divergence, etc.

**Matteo Fabro** [19:43:21]: I mean, as of right now, AI systems don't really have that.

**Matteo Fabro** [19:43:27]: And so, I mean, they have it like a bit, but it's not really divergent thinking, you know, it's still convergent, but like on divergent topics.

**Matteo Fabro** [19:43:37]: whereas like we have like really divergent.

**Matteo Fabro** [19:43:40]: I mean, you can be working, you can be thinking about like AI and then like something like super random does nothing to do with pops into your mind, you know.

**Matteo Fabro** [19:43:52]: I think it's very interesting to mix these two aspects together and kind of, you know, optimize the convergent divergent balance to basically, you know, get something, something really big, you know.

**David Orban** [19:44:07]: Are you on Maui?

**Matteo Fabro** [19:44:11]: No, unfortunately I'm on Oahu because it's the only place where you can reasonably live, especially without a car.

**Matteo Fabro** [19:44:21]: I mean the

**David Orban** [19:44:21]: safety.

**David Orban** [19:44:22]: The person that I want to introduce you to is Garrett Lisi.

**David Orban** [19:44:28]: He's a physicist and he founded the Pacific Science Institute.

**Matteo Fabro** [19:44:35]: Oh, that's

**David Orban** [19:44:35]: cool.

**David Orban** [19:44:36]: He also

**Matteo Fabro** [19:44:37]: runs.

**David Orban** [19:44:38]: And it is a community of researchers that allows people to work independently outside academic conventions.

**David Orban** [19:44:53]: He himself is known for his quantum gravity model that is very interesting mathematically but hasn't been obviously yet experimentally proven as none of them and the Institute is also able to host people So I will make the intro and then if you want to.

**Matteo Fabro** [19:45:30]: OK, thank

**David Orban** [19:45:30]: you.

**David Orban** [19:45:31]: For

**Matteo Fabro** [19:45:31]: sure.

**Matteo Fabro** [19:45:31]: Yeah, I mean, I'm going to I'm going to go to to Maui, of course.

**Matteo Fabro** [19:45:36]: You know, one of the one of these days either now or like maybe I know.

**Matteo Fabro** [19:45:42]: But for sure I'm going go.

**Matteo Fabro** [19:45:43]: So that's me.

**Matteo Fabro** [19:45:45]: Thank OK, so anyway, basically that's kind of my workflow right now.

**Matteo Fabro** [19:45:54]: Now I have to, like, as I was saying, get a, you know, good generational run going.

**Matteo Fabro** [19:46:02]: want to see, you know, especially with, like, strict validation, like, what results we can So, if we can get, like, similar results to what I previously had, but, like, with strict validation, that would really be really good, because at that point, like, production level.

**Matteo Fabro** [19:46:20]: So, we're going to do that.

**Matteo Fabro** [19:46:23]: What else?

**Matteo Fabro** [19:46:26]: Yeah, no, I just wanted to kind of share bit the progress.

**Matteo Fabro** [19:46:30]: Obviously at this point it's still not production level, so it doesn't really make sense to speak about any next steps or anything, I just wanted to share my progress and hear your thoughts if you have any insights or ideas or if fine.

**David Orban** [19:46:54]: that's it.

**David Orban** [19:46:55]: All right.

**David Orban** [19:46:55]: So I will send Garrett an email intro and copy you and hopefully you two can hook up and yep.

**David Orban** [19:47:05]: What's his name?

**Matteo Fabro** [19:47:08]: What's his name?

**Matteo Fabro** [19:47:09]: Garrett?

**David Orban** [19:47:10]: Lisi, L-I-S-I.

**Matteo Fabro** [19:47:14]: Okay.

**Matteo Fabro** [19:47:16]: Okay, thank you.

**Matteo Fabro** [19:47:16]: Yeah, when I go to Maui, I'll definitely go.

**Matteo Fabro** [19:47:22]: I definitely go visit him.

**Matteo Fabro** [19:47:25]: That's cool that he's doing quantum gravity.

**David Orban** [19:47:31]: Okay.

**David Orban** [19:47:32]: Nice chatting.

**David Orban** [19:47:33]: Have fun at the beach and we'll

**Matteo Fabro** [19:47:36]: be in time.

**Matteo Fabro** [19:47:36]: Thank you.

**Matteo Fabro** [19:47:37]: Thank you.

**Matteo Fabro** [19:47:38]: I'll keep you updated.

**Matteo Fabro** [19:47:39]: Hopefully I'll have something cool soon.

**Matteo Fabro** [19:47:43]: So

**David Orban** [19:47:44]: send me some photos.

**Matteo Fabro** [19:47:46]: Oh, yeah, yeah, I will.

**Matteo Fabro** [19:47:48]: Okay.

**Matteo Fabro** [19:47:49]: Bye-bye.

**Matteo Fabro** [19:47:49]: Okay.

**Matteo Fabro** [19:47:50]: Bye-bye.

**Matteo Fabro** [19:48:05]: Thank

**Unknown speaker** [19:48:05]: you

---
*Backed up from MeetGeek on 2026-03-30 08:51*
