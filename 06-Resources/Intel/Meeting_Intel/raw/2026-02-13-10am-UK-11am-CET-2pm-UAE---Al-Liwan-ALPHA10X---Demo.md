# 10am UK/11am CET/2pm UAE - Al Liwan/ALPHA10X - Demo

**Date:** 2026-02-13
**Duration:** Unknown
**Meeting ID:** 572267e8-e262-405c-8ea9-87177583005e

## Participants
- *Participants not listed*

### Summary

The meeting progressed from a short framing of purpose into a technical deep-dive and commercial discussion: Robert set expectations for a deeper demo and potential pilot; Issam reviewed current production modules (sourcing, company 360, chat) and upcoming features including structured market analysis, prediligence, and probabilistic scoring; Issam also described neuro-symbolic architecture and data provenance to support explainability and auditability. The team addressed data residency and LLM-hosting trade-offs (Azure Dubai, self-hosting, fallbacks) and validation plans targeting end of March. Arushi mapped product capabilities to private-markets workflows while Nate and David articulated cross-border and merchant-bank use cases. The meeting closed with agreement to exchange documentation under a mutual NDA and to consider a pilot after the March release.

## Full Transcript

**Nate’s Phone** [10:01:07]: Hello, Robert.

**Nate’s Phone** [10:01:11]: How are

**Robert Marcus** [10:01:11]: you?

**Robert Marcus** [10:01:12]: Yeah, pretty good, thanks.

**Robert Marcus** [10:01:13]: So I'm in transit

**Nate’s Phone** [10:01:14]: to London at the moment, so I'll be off camera, just got people around.

**Nate’s Phone** [10:01:19]: No

**Robert Marcus** [10:01:21]: problem.

**Robert Marcus** [10:01:23]: Hi, David.

**Robert Marcus** [10:01:23]: Hello,

**David Orban** [10:01:25]: hello, everyone.

**David Orban** [10:01:27]: Hi, David.

**Robert Marcus** [10:01:28]: Hello, hello.

**Robert Marcus** [10:01:30]: So, gentlemen, mate, David.

**Robert Marcus** [10:01:34]: I must be honest.

**Robert Marcus** [10:01:36]: We scheduled a follow up, or I did.

**Robert Marcus** [10:01:39]: And then we talked on our side.

**Robert Marcus** [10:01:42]: We realized we took you through a pretty superficial demo, but you have a basic idea of what we have.

**Robert Marcus** [10:01:47]: We explain what it is we have.

**Robert Marcus** [10:01:49]: So I think the purpose of this,

**Nate’s Phone** [10:01:53]: sorry, Nate.

**Robert Marcus** [10:01:56]: So the purpose of this conversation with the cost of maybe too many on our side is to talk about options thinking.

**Robert Marcus** [10:02:05]: We're highly motivated to pilot with partners who know what they're doing, to get feedback on the next generation of the platform that is being developed, that is in development that is very close to release.

**Robert Marcus** [10:02:19]: And so the timing of what it is that we're needing and what it is usually good.

**Robert Marcus** [10:02:28]: So open canvas here to see if there's a way to explore our way forward into some kind of initial limited pilot to give you a better understanding of what we do.

**David Orban** [10:02:38]: So you are correct.

**David Orban** [10:02:40]: The meeting that we had was very useful and the demo that we had was limited.

**David Orban** [10:02:50]: And in my mind, the objective of today's call is to have a deeper conversation that is both around the product, potentially with a deeper demo.

**David Orban** [10:03:03]: Including that, at least as far as I am concerned, a lot of what was covered last time.

**David Orban** [10:03:13]: I am not sure I clearly understood what is existing and what is forthcoming.

**David Orban** [10:03:18]: And as a consequence, what would a pilot allow us to do, as opposed to having to wait until you deliver on the promise of a feature that is not yet fully implemented.

**David Orban** [10:03:31]: So we can do, as far as I'm concerned, two, three possible things.

**David Orban** [10:03:41]: give you the opportunity to reschedule if what I was expecting today is not possible.

**David Orban** [10:03:55]: Look at the product more in detail with a clear delineation of what is possible today and what will be possible and when.

**David Orban** [10:04:09]: That's the second possibility.

**David Orban** [10:04:11]: And what I am not ready to do on today's call is to talk about the pilot, because not understanding the product well enough, at least to the degree that I expect.

**David Orban** [10:04:22]: It would be, in my opinion, very abstract.

**David Orban** [10:04:26]: And I like talking about a lot of abstract things, but I don't want to invest your time without being able to decide whether we want to go ahead or not.

**David Orban** [10:04:44]: Very

**Robert Marcus** [10:04:44]: clear.

**Robert Marcus** [10:04:45]: Thank you, David.

**Robert Marcus** [10:04:46]: So definitely would suggest we do not postpone.

**Robert Marcus** [10:04:53]: Seize the day.

**Robert Marcus** [10:04:54]: We'll see if we're heading in the right direction.

**Robert Marcus** [10:04:55]: If we're not, we'll definitely come back to you later.

**Robert Marcus** [10:04:58]: But we're pretty good at what we do and pretty good at tap dancing and being dynamic.

**Robert Marcus** [10:05:03]: So let's give it a shot right now.

**Robert Marcus** [10:05:04]: I understand the requirements.

**Robert Marcus** [10:05:05]: I think the best thing to do would be for me to give a very short preamble then pass to Isam, who can give you a... a more tactical description of the difference between what it is we have today and where we're headed.

**Robert Marcus** [10:05:22]: I think it's really important to understand that because we have a fully deployable platform today that has gone into Arushi has deployed over 80 projects to different players out here, mostly in the Middle East, many of the very big names, sovereign wealth funds and that type of things.

**Robert Marcus** [10:05:39]: So it's fully functional today.

**Robert Marcus** [10:05:40]: I do not want you to walk away with the impression that we're waiting for the future.

**Robert Marcus** [10:05:46]: We are, as you know with any AI platform of this complexity.

**Robert Marcus** [10:05:50]: It is never complete.

**Robert Marcus** [10:05:52]: We're innovating all the time.

**Robert Marcus** [10:05:53]: The R&D over here started actually Excuse me, a very long time ago, 2008, 2009. So we have a significant evolution over a period of time.

**Robert Marcus** [10:06:05]: And we're moving further and further into a future that really is on the far frontier of the integration of generative AI, LLMs, together with multi-agent architecture, agent technology in general, together with neurosymbolic AI and the whole emerging concept of the world model, which is really the

**Robert Marcus** [10:06:33]: foundation of what it is we have.

**Robert Marcus** [10:06:35]: And Issam can give you a description of that, but I think the thread that is important to emphasize is we can deploy today at you.

**Robert Marcus** [10:06:43]: I don't know where the noise is coming from, if it's on our side, but we can deploy today, but we're becoming more and more powerful as we move into future in the very near future.

**Robert Marcus** [10:06:56]: with that work.

**Robert Marcus** [10:06:57]: Let

**David Orban** [10:06:58]: me respond to you.

**David Orban** [10:07:00]: So thank you for the clarity.

**David Orban** [10:07:03]: I understand that the product is in production.

**David Orban** [10:07:06]: And so it is even simpler.

**David Orban** [10:07:09]: Maybe you have already a PDF that you can send me that clearly differentiates between existing features and your roadmap and expected release cycles with 80 enterprise clients I am sure that you have SLAs, where they know what is coming when it is ready, and they want to test beforehand so that the

**David Orban** [10:07:38]: new model doesn't regress in a series of evals that they already have ready, for example, right?

**David Orban** [10:07:47]: As well as anything else.

**David Orban** [10:07:49]: Another clear nead is again, not on this call, but you will have certainly a document that illustrates the data residency where the challenge specifically for the UAE is that frontier models are hosted in non-compliant regions.

**David Orban** [10:08:19]: So are we all enthusiastic about cloud 4.6?

**David Orban** [10:08:24]: Yes.

**David Orban** [10:08:25]: Is it available on AWS in the UAE region?

**David Orban** [10:08:33]: No.

**David Orban** [10:08:35]: So if our mutual fascination of bleeding edge technology delivers results that we cannot use, because of regulatory constraints that needs to be taken into consideration where you will be able to tell us because of your relationship with Anthropic or OpenAI or whoever it were, that Microsoft is

**David Orban** [10:09:06]: getting their act together and they will be hosting GPT 5.3 in the local region by Q2 or Q3 or whatever it is, right?

**David Orban** [10:09:19]: And then the third, also relevant set of information that you, you, with 80 clients, I don't know if all of these are clients or pilots, how you want to categorize them.

**David Orban** [10:09:39]: You must have a pretty clear idea of what is your engagement model.

**David Orban** [10:09:48]: You know, we didn't touch the last time we spoke.

**David Orban** [10:09:54]: And

**Issam** [10:09:55]: evidently you

**David Orban** [10:09:59]: will have had the chance of both developing it and debugging it, making it a win-win for you and your existing clients.

**David Orban** [10:10:13]: And for us, obviously, that is also something we must have, because you clearly indicated a flexibility to have a pilot that doesn't require, it

**David Orban** [10:10:34]: is as if I am not misunderstanding you are available for a free pilot rather than paid pilot.

**David Orban** [10:10:43]: However, with the expectation of it being successful, we want to make sure that once we turn it into a paid engagement, it is compatible with what we want.

**David Orban** [10:10:58]: So that will be also necessary.

**David Orban** [10:11:02]: And I stop.

**Robert Marcus** [10:11:03]: These are the remarks about what you said.

**Robert Marcus** [10:11:06]: Thank you, very clear.

**Robert Marcus** [10:11:07]: Thank you, David.

**Robert Marcus** [10:11:10]: Let's go like this.

**Robert Marcus** [10:11:11]: I think let's start up with Issam, doing exactly what I suggested.

**Robert Marcus** [10:11:14]: Issam, you're talking about what it is we do today, what we have today, and where we're headed.

**Robert Marcus** [10:11:19]: Also covering SOC 2 and regional compliance with regard to Azure, where we are very strong.

**Robert Marcus** [10:11:27]: I think we should flip back after that to Arushi and talk more about product.

**Robert Marcus** [10:11:32]: And then I'll take care of the financials, the economics of a potential future.

**Robert Marcus** [10:11:36]: Excuse me, arrangement with you afterwards.

**Robert Marcus** [10:11:39]: So we'll keep it very interactive.

**Robert Marcus** [10:11:42]: So please, I'm actually quite glad we don't have a deck and we're not overly organized over here.

**Robert Marcus** [10:11:46]: This is a conversation.

**Robert Marcus** [10:11:47]: You guys impressed us because you clearly know what you're doing, and there are relatively few people who do in the space.

**Robert Marcus** [10:11:54]: So let's have a conversation this time in your hands.

**Issam** [10:11:57]: Yes, so I'll try to bring as much clarity as possible to what we have exactly and what we plan to have in the near future and by when.

**Issam** [10:12:06]: I don't know if you recall the main components of the platform, but for instance, the sourcing engine which is based on our knowledge graph, which contains millions of companies that were filtered, selected for private market interest.

**Issam** [10:12:19]: This we already have and is available running production.

**Issam** [10:12:23]: The custom attributes layer that we showed, meaning that you can enrich the company's information with whatever data you are interested in to filter further your sourcing universe and select a subset of companies.

**Issam** [10:12:36]: This we also have available.

**Issam** [10:12:38]: And as Arushi showed, you can have fact checking and information verification, sorry, verified information on each custom attribute you are generating.

**Issam** [10:12:49]: The conversational interface we have as a chat, that we already have, obviously.

**Issam** [10:12:53]: And you can ask general questions, as Arushi has shown on market analysis aspects, and you will get answers.

**Issam** [10:13:02]: The main revamp on this aspect, because we will ship a completely new version by end of March.

**Issam** [10:13:09]: One of the drawbacks of having a central entry point as a chat is that unknown unknowns.

**Issam** [10:13:16]: People don't know what the platform can do or cannot do right.

**Issam** [10:13:20]: So the sourcing part will stay exactly the same and will probably merge the customer attributes part somewhat with the search, because again, users don't understand necessarily how criteria correspond to exact search, leveraging our search engine versus what is the customer attribute.

**Issam** [10:13:35]: They just ask plain language questions, and it will be our agent's job to manage behind the scenes how the workflow will be decomposed.

**Issam** [10:13:43]: And on the market analysis part, We will have a more structured canvas where you define the market of interest, and then it will automatically trigger all the sub-agents that do information retrieval, reasoning, et cetera, to give you an overall assessment of the market.

**Issam** [10:13:57]: So it will not happen in the chat anymore.

**Issam** [10:14:01]: It will be a structured layout where you just give a definition of a market or a niche, and you will get a set of information.

**Issam** [10:14:08]: Similarly, Rishi showed in the demo what we call the spotlight page, which is a company focus 360 view.

**Issam** [10:14:16]: This we already have.

**Issam** [10:14:18]: It's already structured as a layout and this is what we target also for the market side of things.

**Issam** [10:14:22]: But we will improve that layer about company 360 with even more information and more reasoning on the company data.

**Issam** [10:14:30]: So I would say these three modules sourcing, market analysis and company 360 already exist in production.

**Issam** [10:14:40]: Sourcing is essentially as it will be end of March in the release, except for some improvements on merging customer attributes with the rest.

**Issam** [10:14:47]: Market analysis will not be a conversation, but it will have a specified layout that the product team has defined that will be completely automated behind the scenes, and the company deep dive will be further improved compared to what you have seen.

**Issam** [10:15:01]: So this is on the main existing aspects.

**Issam** [10:15:04]: What we have today, again, through the chat, but we want to build as a full autonomous capability is prediligence.

**Issam** [10:15:12]: So today you can upload a document, a SIM document to the platform.

**Issam** [10:15:15]: You can interact with it through the chat interface, but we think that we can bring more structure to how the SIM data is analyzed, how it is combined with knowledge graph data or web data to produce an opportunity risk and data gap assessment.

**Issam** [10:15:31]: So we will build the layout for this, which is form of prediligence, which will be completely automated.

**Issam** [10:15:36]: And again, you will still have the assistant if you want to deep dive on certain aspects.

**Issam** [10:15:41]: So this is, I would say, the most new feature or module within the platform, structured prediligence as compared to just uploading a sim to the platform and interacting with it.

**Issam** [10:15:53]: So these are the four main modules we have.

**Issam** [10:15:56]: Three exist, two will be improved a lot, and one will be completely new.

**Issam** [10:16:01]: And transversal to all of this is our, I'm hearing some... Transversal to this, we have the predictive capability.

**Issam** [10:16:09]: So again, Arushi has shown the transactionability prediction score.

**Issam** [10:16:14]: It's something we've been building for a year now, and it is in production and running.

**Issam** [10:16:19]: What we will be adding is that any score on the platform moving forward will correspond to, we'll go through our engine of probabilistic modeling.

**Issam** [10:16:30]: So obviously the transactionability prediction was easy because we have a data, we could build a machine learning model, and we just back tested it, and we shipped it as any good data science team would do.

**Issam** [10:16:41]: But there are other scores that we produce, like a mandate fit score, for instance.

**Issam** [10:16:45]: You have a company, you have a mandate that you have defined, how do you assess the fit between the two?

**Issam** [10:16:51]: What we are building now is a Monte Carlo based model.

**Issam** [10:16:57]: So you have your mandate.

**Issam** [10:16:58]: We extract the criteria of the mandate.

**Issam** [10:17:00]: We have data about the company, like location.

**Issam** [10:17:03]: Does it fit the mandate location or not?

**Issam** [10:17:05]: The sector, does it fit the sector or not?

**Issam** [10:17:07]: We might have ESG criteria, but we are missing ESG criteria for the company.

**Issam** [10:17:11]: So it's missing data.

**Issam** [10:17:12]: We combine this mapping between the criteria of the mandate and the criteria of the company through a probabilistic model.

**Issam** [10:17:19]: We assign probability distributions to each variable.

**Issam** [10:17:23]: We assess uncertainty based on the presence or not of the data and based on the reliability of the source.

**Issam** [10:17:29]: And what we spit at the end is a probability distribution of mandate-fit score.

**Issam** [10:17:33]: And then you can have an average, which is the average fit.

**Issam** [10:17:39]: But we can also assess tail risk.

**Issam** [10:17:41]: What's the probability of it being a very good score, given the available information and the uncertainty we have on that?

**Issam** [10:17:47]: Or what's the probability of it being a bad fit?

**Issam** [10:17:50]: Because obviously we are uncertain about certain data points.

**Issam** [10:17:54]: And this method, this engine of taking whatever input, objective, quantitative or qualitative, taking whatever input we have on a certain entity, again, qualitative or quantitative, making assumptions on the quality of the data and then spitting out the probability distribution to give scores and

**Issam** [10:18:12]: tell risk is something that will be generalized to all types of scores we have on the platform.

**Issam** [10:18:18]: So we ship, transactionality is already in production, mandate-fit score will be shipped for end of March, and duplication of this engine for any score reasoning will be an available capability.

**Issam** [10:18:31]: So I hope this brings some clarity.

**Issam** [10:18:33]: Do you

**Robert Marcus** [10:18:33]: want to just cover the SOC2 narrative and the regional compliance?

**David Orban** [10:18:39]: Before we go there, and thank you for that reminder, Robert.

**David Orban** [10:18:45]: Before we go there, a couple of questions.

**Issam** [10:18:51]: I

**David Orban** [10:18:53]: want to explore three layers

**Issam** [10:18:57]: in the product as it exists today or as it

**David Orban** [10:19:00]: is going forward.

**David Orban** [10:19:04]: One is the chat interface and the product's ability to form ever-improving contextual understanding of the user or the number of users through the conversations.

**Issam** [10:19:27]: Yeah.

**Issam** [10:19:27]: And how this

**David Orban** [10:19:30]: is not only retained, but then turns into potentially a more agentic behavior the product where out of the universe of targets maybe things get pre-selected or in more proactive manner the product goes out and in a predictive manner starts collecting things that it believes will be useful.

**Issam** [10:20:04]: So that's the first.

**Issam** [10:20:06]: What can you say

**David Orban** [10:20:07]: about that?

**David Orban** [10:20:08]: So this ties

**Issam** [10:20:09]: to what Robert was mentioning on the notion of world model and institutional memory.

**Issam** [10:20:16]: Our target, why are we building the system the way we are doing it?

**Issam** [10:20:19]: Meaning we are collecting information always with metadata about its provenance.

**Issam** [10:20:23]: And it's not just external world information about companies.

**Issam** [10:20:27]: It's also user behavior, user preferences.

**Issam** [10:20:30]: So for instance, if we have, and that's why we are putting in a specified canvas for prediligence, If the user sees three conflicting data points coming from internet, web search, and from our knowledge graph.

**Issam** [10:20:41]: And he has a third information from the CIM and selects, for instance, one value.

**Issam** [10:20:46]: He will give a rational.

**Issam** [10:20:48]: All of these events happening will be stored within our platform.

**Issam** [10:20:53]: So you could imagine that is that we structure all world and context interactions.

**Issam** [10:21:03]: And the neural part is that we do it either through understanding of language, through the chat, or because we build in the uncertainty management through machine learning or qualitative models.

**Issam** [10:21:12]: But at the end, we just have a sort neurosymbolic sensor system.

**Issam** [10:21:17]: that captures everything that is happening from in the world, outside world, of private markets, and in the user interactions.

**Issam** [10:21:25]: And our target once we, and this is why we are also very interested in building pilots, is that once you have acquired context within an institution, You can start training a world model of the decision making dynamics within the institution.

**Issam** [10:21:39]: You need also to collect outcomes.

**Issam** [10:21:41]: What's the, and why?

**Issam** [10:21:43]: What were the positive investments?

**Issam** [10:21:45]: What were the negative investments so that you can train final layer of models, the world model of the institution decision making process.

**Issam** [10:21:53]: of what are the patterns of decisions that led to positive outcomes.

**Issam** [10:21:59]: And then the system can become more proactive, as you said, suggesting, for instance, when you have taken an underwriting phase and you made certain rational selections, etc., flag to you, okay, this pattern of data selection or this pattern of uncertainty flagging, etc., is not consistent.

**Issam** [10:22:18]: with the best practices we have seen in the past that led to positive outcomes.

**Issam** [10:22:23]: Obviously, it can also starting just from a mandate and based on how the analysts have done the sourcing, the screening, the selection, immediately suggest potentially a shortlist based on the mandate.

**Issam** [10:22:35]: So to sum it up.

**Issam** [10:22:36]: We are building the sensor system that obviously acquires private markets data.

**Issam** [10:22:40]: This is already done.

**Issam** [10:22:42]: Is able to acquire institutional context.

**Issam** [10:22:44]: And then we can train a model to automate and identify the decision-making process as a hope.

**David Orban** [10:22:52]: So thank you.

**David Orban** [10:22:55]: Very useful.

**David Orban** [10:22:57]: You actually preempted my questions because I was about to ask, these were the three layers of the question, right?

**David Orban** [10:23:07]: And I saw them in a certain progression, was about the neuro-symbolic approach and the world model,

**Issam** [10:23:19]: or still like

**David Orban** [10:23:21]: to call it a digital twin, because... when you talk about the world model, robots come into my mind instead.

**David Orban** [10:23:28]: But yes.

**David Orban** [10:23:32]: And we don't need necessarily to insist on the part that I was leading to, which is more how it can be proactive, agentic.

**David Orban** [10:23:42]: more collaborative rather than passive.

**David Orban** [10:23:48]: It is okay if it is not like that.

**David Orban** [10:23:52]: But just before we move on to the regulatory parts, when you talk about the neuro-symbolic aspects, one of the best Well, potentially the most important promise of a neurosymbolic approach is a superior explainability

**Issam** [10:24:16]: of

**David Orban** [10:24:17]: the results, the conclusions, the, you know, whatever the model speaks out.

**David Orban** [10:24:26]: How do you take advantage of that if you can deliver on that promise?

**David Orban** [10:24:31]: And as a segue into the regulatory compliance part, Do you use that explainability to make the decisions better supported, more traceable and auditable when human acts on them?

**Issam** [10:24:50]: Yeah, absolutely.

**Issam** [10:24:50]: Exactly, exactly that

**Robert Marcus** [10:24:52]: refer to some.

**Robert Marcus** [10:24:54]: So just again

**Issam** [10:24:55]: to give more concretely what we have built in terms of NSAI.

**Issam** [10:25:00]: So we have basically at the data layer what we call ledgers.

**Issam** [10:25:05]: We have a core ledger that contains information about stable entities like companies, some people information, transactions, etc.

**Issam** [10:25:14]: And then we have what we call the decision ledger, which is where we store the context of interactions with the user.

**Issam** [10:25:20]: And some entities are user defined.

**Issam** [10:25:22]: So for instance, when the user defines a market, there is no absolute definition of a market that exists like an existing entity like a company.

**Issam** [10:25:30]: The company is out there in the real world.

**Issam** [10:25:32]: The market is a user defined concept.

**Issam** [10:25:34]: But still, we can collect claims and build reasoning based on that specific definition.

**Issam** [10:25:41]: So we have two levels that store the two types of context.

**Issam** [10:25:45]: Currently we have the core ledger and part of the decision ledger and both of them will be completely finalized by end of March.

**Issam** [10:25:53]: We are now in testing phase.

**Issam** [10:25:56]: So once you have these two layers, then the working memory of an LLM, which is the context window becomes just the layer where you have a pipeline that collects all the relevant information and put it in the context window of the LLM.

**Issam** [10:26:11]: And the agent has clear instructions of not inventing things and answering based only on what is present in his context window.

**Issam** [10:26:21]: So we do not give the LLM the ability to answer directly or just go retrieve information on the web and use that information to answer us.

**Issam** [10:26:31]: We completely separate information retrieval either in batch as we do for the core entities which are very stable.

**Issam** [10:26:39]: So we have data engineering pipelines that collect informational stories or more dynamically based on the specific user context.

**Issam** [10:26:46]: This is the data layer, the facts layer.

**Issam** [10:26:49]: And then the LLM, the neural part, is just there to leverage its context window.

**Issam** [10:26:53]: to take in the structured inputs coming from the facts layer.

**Issam** [10:26:58]: Potentially there might be some qualitative aspects, including the system prompt that gives him instruction.

**Issam** [10:27:03]: Some of the data or the claims might be qualitative too.

**Issam** [10:27:06]: And whatever output the LLM is producing is fully based verified information we have put in his context window.

**Issam** [10:27:15]: And I can speak to how do we make sure that the facts layer, how it is governed.

**Issam** [10:27:21]: Again, there we have a tiering of confidence and trustworthiness of data.

**Issam** [10:27:26]: So for instance, data we retrieve from cap IQ or other trustworthy sources is tier one data.

**Issam** [10:27:33]: And the tier 4 is proxy information.

**Issam** [10:27:36]: So for instance, you want revenue about a company.

**Issam** [10:27:38]: The company is a SaaS company.

**Issam** [10:27:40]: We don't have revenue, but we have employee range.

**Issam** [10:27:42]: We can infer more or less what is the revenue from the employee range.

**Issam** [10:27:46]: This is tier 4. It can be leveraged, but it's tagged as tier 4 in the LLM reasoning.

**Issam** [10:27:52]: And obviously, since everything is stored, both the data layer, the facts layer, and also whatever is happening in thread of the LLM interactions with the facts layer or tools, All of this is stored and hence auditable.

**Issam** [10:28:05]: So we can always trace back how a decision was I hope this answers your question.

**David Orban** [10:28:11]: Yes, it does.

**David Orban** [10:28:11]: Thank you.

**David Orban** [10:28:13]: So let's move to the compliance part and data, residency and those kinds of things.

**Issam** [10:28:25]: So on the data residency, obviously, we are Azure based, so we can leverage the servers of Microsoft that are based in Dubai.

**Issam** [10:28:35]: So data itself is not a problem.

**Issam** [10:28:38]: We are fully cloud-based, so we are able to leverage that.

**Issam** [10:28:42]: on the aspect of LLMs.

**Issam** [10:28:45]: Here it's a trade--off.

**Issam** [10:28:47]: Currently, for the system that we are running, notably for demos and for first pilots, where there is no super critical data.

**Issam** [10:28:56]: Many things are happening through the OpenAI API.

**Issam** [10:28:58]: So they provide us with an LLM.

**Issam** [10:29:00]: It's not an agent.

**Issam** [10:29:01]: So it's a stateless system.

**Issam** [10:29:02]: We just send it our query and we get an answer.

**Issam** [10:29:07]: Currently, based on the content of each layout, there is no ultra-sensitive information.

**Issam** [10:29:12]: The only user provided information is obviously the context, what he is asking, and potentially the sim he is uploading.

**Issam** [10:29:20]: So currently for the sim, we have built a system that leverages external APIs.

**Issam** [10:29:26]: If needed for confidentiality reasons, we can completely turn it into a self-hosted RAG system.

**Issam** [10:29:32]: that sends nothing to external APIs.

**Issam** [10:29:35]: And for the LLM calls, What we want to build and it's not here completely on all services, but already present on some of them is a fallback option in terms of LLMs, because you could call open AI, but you can also self-host a mistral or whatever open source LLM on your own GPU infrastructure and

**Issam** [10:29:56]: use just that to exactly deploy the same workflows.

**Issam** [10:30:00]: This is where the evaluations become important.

**Issam** [10:30:02]: And again, we are building them.

**Issam** [10:30:04]: We have already built our evaluations for the sourcing engine.

**Issam** [10:30:07]: We are building our evaluations for the market analysis.

**Issam** [10:30:10]: And we are starting to build it.

**Issam** [10:30:12]: No, we plan to do it by end of March, more less, for the pre-led indigenous part.

**Issam** [10:30:15]: So that evaluations make sure that the behavior stays stable, even when you do swap LLMs based on a set of tasks.

**David Orban** [10:30:25]: And definitely LLMs start to become so... good that even using the previous version is

**Issam** [10:30:37]: fine.

**Issam** [10:30:39]: And it is more and more so.

**Issam** [10:30:41]: And

**David Orban** [10:30:41]: quantization allows better hosting opportunities.

**Issam** [10:30:48]: Yeah, absolutely.

**Issam** [10:30:50]: So it is

**David Orban** [10:30:51]: going in the great direction.

**David Orban** [10:30:54]: Okay.

**David Orban** [10:30:56]: I'm sure there are other aspects around regulatory and compliance issues that we will need to explore, but in the meantime,

**Issam** [10:31:07]: this is okay.

**David Orban** [10:31:10]: Thank you.

**David Orban** [10:31:11]: And Robert, I think you said that Arushi should

**Robert Marcus** [10:31:17]: show something too.

**Robert Marcus** [10:31:19]: Yes, if Arushi, if you could concentrate on the decision intelligence focus and the primary workflows, less technical, more workflows.

**Aarushi Agarwal** [10:31:30]: Absolutely.

**Aarushi Agarwal** [10:31:33]: Yeah.

**Aarushi Agarwal** [10:31:35]: Okay.

**Aarushi Agarwal** [10:31:35]: So this is more converting what Assam said and putting it in terms of the workflows and linking that to what happens in a private market investment workflow today and how, which parts of it is it that we're trying to solve for.

**Aarushi Agarwal** [10:31:48]: So as we mentioned the last time, the one liner, the two, three word phase of the product is that we are a decision intelligence platform.

**Aarushi Agarwal** [10:31:57]: and we are built for private markets and investment space within that.

**Aarushi Agarwal** [10:32:01]: So that is the goal.

**Aarushi Agarwal** [10:32:02]: That remains unchanged.

**Aarushi Agarwal** [10:32:03]: The way we transpire this in terms of what happens on the platform is we envisage five main workflows.

**Aarushi Agarwal** [10:32:11]: First is targeting.

**Aarushi Agarwal** [10:32:12]: So targeting has everything to do with sourcing and screening and everything that is some said in between that we have a data layer of our own.

**Aarushi Agarwal** [10:32:21]: We are able to capture so much information which is currently sitting in silos fragmented.

**Aarushi Agarwal** [10:32:26]: about companies, we have an engine on top on which you can search through companies, you can screen.

**Aarushi Agarwal** [10:32:33]: And the end goal, the end outcome over there is a short list of targets that match the thesis, whatever that you began with.

**Aarushi Agarwal** [10:32:43]: And it is ranked and you have an explanation of why everything exists over there.

**Aarushi Agarwal** [10:32:48]: Over there, we have all the flexibility to include some attributes about a company profile that are well known, but even on the fly information, something that's not stored in the data set.

**Aarushi Agarwal** [10:32:58]: So everything you need to to get to a short rank list of targets is workflow number one, which is targeting.

**Aarushi Agarwal** [10:33:05]: This is live on the platform.

**Aarushi Agarwal** [10:33:07]: We have been doing this for our current clients.

**Aarushi Agarwal** [10:33:09]: in multiple different ways.

**Aarushi Agarwal** [10:33:11]: So a lot of use cases around corporate MNA, where they just want to expand into a new geography or vertical or horizontal expansion.

**Aarushi Agarwal** [10:33:20]: In some cases, just looking for alternate suppliers, something looking for, okay, I have this portfolio and I want to just enhance it for an adjacent product or a substitute product, all of those kind of use cases.

**Aarushi Agarwal** [10:33:33]: We have already tested and implemented this with multiple clients to start with the problem statement.

**David Orban** [10:33:39]: They're very interesting.

**David Orban** [10:33:41]: And sorry, Arush, if I interrupt you, because I would like to invite Nate if he can to maybe comment, because we had a chance of sitting down and meet about some of the ways that we envision potentially using the product in the future.

**David Orban** [10:33:59]: I don't remember how much we told you about the way Alivan works.

**David Orban** [10:34:06]: We call ourselves an investment bank of a merchant bank tradition where not only design a given transaction, but we also actively participate in the long-term success and in investing the principal led.

**David Orban** [10:34:33]: actively participate in the process and benefit from upside.

**David Orban** [10:34:41]: And a particular focus we have is to bring companies to the GCC region, in particular to the UAE.

**David Orban** [10:34:52]: where they may not be aware of the facets that this entails and what are the opportunities So, Nate, sorry, I saw you unmuting yourself.

**David Orban** [10:35:06]: Why don't you take

**Nate’s Phone** [10:35:07]: Yeah, certainly.

**Nate’s Phone** [10:35:08]: Sorry if it's a bit noisy in the background.

**Nate’s Phone** [10:35:10]: I'm just, I'm in a London train delay situation, so I do apologize.

**Nate’s Phone** [10:35:16]: Yeah, certainly, where I am vision.

**Nate’s Phone** [10:35:19]: Now, I don't believe this being the only use case, because I believe the nature of the platform.

**Nate’s Phone** [10:35:25]: There is a lot of use cases that we can look at.

**Nate’s Phone** [10:35:27]: But certainly the use case that I'm looking at is David just described, if I was to focus on one, the cross-border aspect.

**Nate’s Phone** [10:35:35]: So what we really need to look at an understanding of where companies, what companies are really about.

**Nate’s Phone** [10:35:42]: You know, we get a lot of information that is public.

**Nate’s Phone** [10:35:46]: You know, you get information from companies' house.

**Nate’s Phone** [10:35:48]: You get different things, aspects of our companies.

**Nate’s Phone** [10:35:51]: We can look at pitch book.

**Nate’s Phone** [10:35:52]: We can look at everywhere.

**Nate’s Phone** [10:35:53]: But to actually understand where our company functions and where, what makes them tick.

**Nate’s Phone** [10:35:58]: And then looking at from an aspect that many of the companies that we will look at from merchant bank perspective, isn't a one-off transaction.

**Nate’s Phone** [10:36:07]: We're looking at a long-term potential engagement where we need to build a strategy around how we are going to engage a company, build it, you know, enhance a company, look various pieces that are going enhance that company in the long-term.

**Nate’s Phone** [10:36:21]: and then looking at the potential synergies for M&A and the such.

**Nate’s Phone** [10:36:25]: So in a very simple use case, that is an example of where I believed being able to fully dig into it and looking at the substantial amount of information that you're able to generate onto a company, how that would simplify and de-risk a transaction for That's probably a high

**Aarushi Agarwal** [10:36:47]: That's that's very helpful.

**Aarushi Agarwal** [10:36:50]: Thank you for sharing.

**Aarushi Agarwal** [10:36:51]: And this is exactly what we have been doing for a few of our clients.

**Aarushi Agarwal** [10:36:55]: So this actually, the additional things that you said covered the other two use cases.

**Aarushi Agarwal** [10:36:59]: And all three of them are live on the platform right now.

**Aarushi Agarwal** [10:37:02]: That the crux of most of the work that we have done for our clients taking a problem such as this.

**Aarushi Agarwal** [10:37:08]: So you have... either you already have a portfolio of companies in your case or in other cases.

**Aarushi Agarwal** [10:37:14]: You already have just one company and there's a market that you operate in.

**Aarushi Agarwal** [10:37:18]: So one more module is this discover where you go on and you look at that market in a wholesome manner.

**Aarushi Agarwal** [10:37:25]: You look at what it comprises of right now what are the segments what are the main trends what are the growth drivers who is investing where are they investing who are the key players why do they differentiate themselves from one another and the outcome of all of that is where should I invest more

**Aarushi Agarwal** [10:37:42]: which is a niche that is attractive and your parameters of what counts as attractive can be very different in such cases if you have a portfolio You're mainly looking for synergies of where all you do not have to start from scratch.

**Aarushi Agarwal** [10:37:55]: In some other places, it's just a trend that you're trying to piggyback on.

**Aarushi Agarwal** [10:37:59]: Or sometimes it's about where most of the money is flowing.

**Aarushi Agarwal** [10:38:02]: So whatever defines attractiveness for is customizable.

**Aarushi Agarwal** [10:38:07]: Using that, there is a module that is able to analyze and look at markets as a whole, identify these pockets.

**Aarushi Agarwal** [10:38:15]: Then take it onto this targeting module where you're able to do sourcing and screen.

**Aarushi Agarwal** [10:38:20]: And what you said, Nate, is very, very real problem.

**Aarushi Agarwal** [10:38:24]: So we have connections to cap IQ, for instance.

**Aarushi Agarwal** [10:38:28]: We have connections to crunch base.

**Aarushi Agarwal** [10:38:30]: But the problem with these databases is they're good in one thing only.

**Aarushi Agarwal** [10:38:35]: Someone will give you financials.

**Aarushi Agarwal** [10:38:36]: Someone is going to give you previous deals.

**Aarushi Agarwal** [10:38:39]: what one perfect database does not have is everything which is the metrics related to these companies but also a very detailed description of what they do so i am able to go and look in cap iq i can get if i know the company i will get the financials but if i am starting with a thesis i am starting

**Aarushi Agarwal** [10:38:57]: with some hypothesis on synergies that i want the company the medtech space respiratory monitoring devices within that using precision technology, having operations here, being able to transport here, being compliant to so and so.

**Aarushi Agarwal** [10:39:15]: All of

**David Orban** [10:39:16]: that.

**David Orban** [10:39:18]: I stop you only because I want to be respectful with everyone's time.

**David Orban** [10:39:25]: We have five minutes before the end of what we schedule.

**David Orban** [10:39:28]: I'm sure there is a lot more to talk about and what we are saying is interesting and valuable.

**David Orban** [10:39:35]: So, Robert, why don't we finish talking about what comes after a successful pilot, and then we can decide what are the next steps.

**David Orban** [10:39:48]: You are muted.

**Robert Marcus** [10:39:52]: At the risk of seeming evasive, David, I'm going to be evasive.

**Robert Marcus** [10:39:58]: And the reason for that is that we are launching this new version of the platform We're actively looking for launch partners to help us with the refinement of the platform and its application become showcases, the particular focus on the region over here.

**Robert Marcus** [10:40:18]: So we're very flexible.

**Robert Marcus** [10:40:20]: What we is an enterprise solution.

**Robert Marcus** [10:40:25]: What we are not is some kind of 10 bucks per month per user LLM application.

**Robert Marcus** [10:40:32]: So we're not

**David Orban** [10:40:33]: Okay.

**David Orban** [10:40:35]: I didn't expect that you would be, and I'm not surprised that you are not.

**David Orban** [10:40:41]: I understand that you feel the need of not being more explicit.

**David Orban** [10:40:50]: And the way I interpret if you wish, is that you want us to invest our time, our attention, the opportunity cost of dedicating those to both setting up and using the product.

**David Orban** [10:41:12]: And that investment will be considerable.

**David Orban** [10:41:15]: And if we decide to do that is because you regardless of what you are or able or not able to now share.

**David Orban** [10:41:33]: You convince us that we will be able to So what you want is that confidence on both sides that... your investment your investment in evaluating it in the current and future state post- march is going to generate a positive ROI.

**David Orban** [10:42:01]: So even if the details are not in place yet, we will be able to agree and it will be able to be able to be sustainable.

**David Orban** [10:42:13]: That's fine.

**Robert Marcus** [10:42:15]: That's fine.

**Robert Marcus** [10:42:16]: Exactly.

**David Orban** [10:42:18]: And so in terms of next steps, what I would like is to please provide us with... more than a video, than you have already, or you are in a process of developing around the product documentation, how it is deployed, how it is customized, how ingest data building its sort of model, how is used, are

**David Orban** [10:42:57]: admin interfaces and functions with multi-layer role-based access models and separation of duties and whatever fun stuff we are subject And the more complete our understanding is gonna be.

**David Orban** [10:43:22]: And then I also leave it to you to tell us whether you believe.

**David Orban** [10:43:28]: I mean, I have my own opinion.

**David Orban** [10:43:30]: We are very busy right And if you were to say, why don't you wait until the next version is ready in March?

**David Orban** [10:43:37]: I think that would be better than trying to start right away then having to upgrade or update.

**David Orban** [10:43:44]: And so that would definitely be my preference.

**David Orban** [10:43:51]: Nate, I don't know if you have any closing remarks and requests besides these for Robert and his colleagues.

**Nate’s Phone** [10:44:01]: Yes, thanks, David.

**Nate’s Phone** [10:44:04]: Yes, so just in regards to that, I'm in a grant.

**Nate’s Phone** [10:44:08]: Obviously, we weren't any sort of trial or anything that we do is to be productive and we want to make sure that we're utilizing, you know, the full features so we understand, you know, as that sits.

**Nate’s Phone** [10:44:21]: And I do appreciate it.

**Nate’s Phone** [10:44:24]: I know going into this, but this wasn't a $10 a month per seat type of operation.

**Nate’s Phone** [10:44:31]: Because I do recall our conversation a few years ago, Robert.

**Nate’s Phone** [10:44:34]: But I think most important for us is the ROI on using the software.

**Nate’s Phone** [10:44:40]: And I think that's the most important feature that we need to understand internally is how can we turn this... Oh, apologies.

**Nate’s Phone** [10:44:49]: How we can turn this around... in the future to make a good collaboration between our parties

**David Orban** [10:45:15]: That's right.

**David Orban** [10:45:16]: That's right.

**David Orban** [10:45:17]: So thank you, Nate.

**David Orban** [10:45:19]: Thank you, thank you, Isam.

**David Orban** [10:45:21]: Thank you, Arushi.

**David Orban** [10:45:23]: And Robert, I think it is clear there's mutual interest.

**David Orban** [10:45:31]: We need much more in depth of what ways to proceed with the evaluation.

**David Orban** [10:45:42]: And yeah, just send us a follow-up email and we will take it under advisement.

**Robert Marcus** [10:45:53]: Thank you very much, David.

**Robert Marcus** [10:45:54]: Yes, to just quickly wrap up.

**Robert Marcus** [10:45:56]: Your articulation of the commercials is spot The objective is to like And based on that we find a gentlemanly agreement that respects the value of what we have and where you're at in your evolution.

**Robert Marcus** [10:46:11]: So I don't have a particular concern about that.

**Robert Marcus** [10:46:14]: We are well-financed and we're offering very significant discounts on this launch partner activity that you articulated very By the way, where are you from?

**Robert Marcus** [10:46:25]: What is your accent?

**David Orban** [10:46:28]: I was born in Hungary and my wife is Italian and half German, so

**Robert Marcus** [10:46:36]: pick.

**Robert Marcus** [10:46:38]: You're highly articulate, which is a delight for someone who likes words.

**Robert Marcus** [10:46:45]: So very clear.

**Robert Marcus** [10:46:48]: Excuse me, just clear on our side.

**Robert Marcus** [10:46:52]: We are in R&D shop.

**Robert Marcus** [10:46:54]: We're very much a skunk work, so I've been to some degree in stealth mode and just emerging out of that.

**Robert Marcus** [10:46:59]: So we're not big on marketing documentation.

**Robert Marcus** [10:47:03]: We will need to sign an NDA.

**Robert Marcus** [10:47:05]: Based on that NDA, we can share with you certain of our R&D documentation to do a better understanding of where you are, of where we are.

**Robert Marcus** [10:47:12]: If there's alignment, let's move But we definitely, the value add.

**Robert Marcus** [10:47:17]: Bad for us.

**David Orban** [10:47:19]: That is fine.

**David Orban** [10:47:23]: You know, when someone comes and says, Before we have a call let's sign an NDA.

**David Orban** [10:47:29]: I very much don't like that, but investing your time, our time, having already done that, and wanting to go ahead and NDA is perfectly appropriate.

**David Orban** [10:47:41]: If we sign ours, it will be faster.

**David Orban** [10:47:45]: So if that is okay with you, will... take that route.

**David Orban** [10:47:55]: It is a mutual NDA and it is compatible with our needs without any quirks, except that it is, of course, specific to our jurisdiction.

**David Orban** [10:48:09]: And it will be okay too.

**David Orban** [10:48:13]: It will just take more time for legal review, etc.

**David Orban** [10:48:17]: And then yes, after the NDA is signed, you will send us documentation, we will study it, have more questions, and proceed that

**Robert Marcus** [10:48:28]: Very good, yes, as long as your NDA is mutual, I'm fine signing it, so if you can send that to me, preferably I have a docu-sign, we can get that done,

**David Orban** [10:48:35]: and then revert to the documentation early next Okay, perfect, thank you very

**Robert Marcus** [10:48:41]: Thank you so much, both you.

**Robert Marcus** [10:48:42]: Great conversation.

**Robert Marcus** [10:48:43]: Thanks, everyone.

**David Orban** [10:48:44]: Appreciate

---
*Backed up from MeetGeek on 2026-03-30 08:44*
