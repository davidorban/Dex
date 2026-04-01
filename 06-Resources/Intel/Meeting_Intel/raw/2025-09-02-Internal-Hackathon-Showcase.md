# Internal Hackathon Showcase

**Date:** 2025-09-02
**Duration:** Unknown
**Meeting ID:** 5a8a3468-dc04-4410-9e3b-ffb7fc14af72

## Participants
- *Participants not listed*

### Summary

The meeting covered several key topics, including the low attendance at the hackathon and the decision to record presentations for later viewing. Shane will prepare a judging form for the best presentation. The discussion on automating lead outreach highlighted the use of LinkedIn scraping and the introduction of Lemlist for personalized messaging. A multi-channel outreach strategy was proposed, with Slava tasked to share pricing details for the outreach tool. Task management automation was also discussed, with Panagiotis and Mateo assigned to explore integration with linear tasks and web hooks for project tracking. Daniel Nowak presented a new sales prospecting tool utilizing the Apollo database and Sensei API, demonstrating its capabilities and garnering interest from a marketing agency. The meeting concluded with a focus on enhancing tool functionality and client engagement.

## Full Transcript

**Multiple speakers** [10:31:31]: When you see that, well, danger is coming.

**Multiple speakers** [10:31:36]: That's how you perceive us, Daniel.

**Daniel Nowak** [10:31:43]: That's how you

**Martine Haug Olsen** [10:31:55]: us,

**Martine Haug Olsen** [10:32:02]: Why isn't my TLDV added?

**Shane Sibley** [10:32:10]: That is, this is annoying.

**Shane Sibley** [10:32:39]: Thank

**Martine Haug Olsen** [10:32:54]: you.

**Martine Haug Olsen** [10:33:02]: Oh.

**Daniel Nowak** [10:33:09]: Martin, what do you have for lunch?

**Martine Haug Olsen** [10:33:16]: Oathmeal?

**Martine Haug Olsen** [10:33:19]: Very basic.

**Multiple speakers** [10:33:22]: Is that a brunch or a lunch?

**Shane Sibley** [10:33:25]: Brunch.

**Martine Haug Olsen** [10:33:27]: Okay, nice.

**Martine Haug Olsen** [10:33:32]: Yeah.

**Shane Sibley** [10:33:32]: Yeah, we got relatively light attendance today, right?

**Shane Sibley** [10:33:37]: Mm-hmm.

**Shane Sibley** [10:33:37]: Mm-hmm.

**Shane Sibley** [10:33:43]: Thank

**Shane Sibley** [10:33:49]: you.

**Shane Sibley** [10:34:34]: Well, Slava, with with light attendants today, you got a better chance of jet setting out to Mexico to see Dan.

**Shane Sibley** [10:34:50]: Has, who here is present or has put something together for today?

**Shane Sibley** [10:34:56]: One.

**Shane Sibley** [10:35:02]: Two.

**Shane Sibley** [10:35:05]: All right.

**Shane Sibley** [10:35:09]: All right.

**Shane Sibley** [10:35:23]: right.

**Shane Sibley** [10:35:23]: Hey, Alessandro.

**Shane Sibley** [10:35:27]: How is it going?

**Alessandro Huaroto** [10:35:29]: Yeah, good and you.

**Alessandro Huaroto** [10:35:31]: I'll bet everything good, everything good.

**Shane Sibley** [10:35:39]: Yeah, we're pretty light on the attendants today.

**Shane Sibley** [10:35:41]: I wonder if we should just get started and people trickle in, or is there a lot of people off today?

**Shane Sibley** [10:35:47]: I know we've got Marco, Marco Rupert and Dan's not up yet.

**Alessandro Huaroto** [10:35:55]: Yeah, I'm checking.

**Alessandro Huaroto** [10:35:57]: Well, of course, we have a few people off.

**Alessandro Huaroto** [10:35:59]: We have like, a few people from Tech Team off, yeah.

**Alessandro Huaroto** [10:36:03]: Marco is also off.

**Alessandro Huaroto** [10:36:04]: So, I guess, mainly because of this.

**Alessandro Huaroto** [10:36:07]: Rupert is also off, correct, and then is leave, you know.

**Daniel Nowak** [10:36:21]: Okay.

**Multiple speakers** [10:36:25]: Well, I mean, this is all going to be recorded anyway.

**Shane Sibley** [10:36:28]: So if anybody else is going to be jumping on to do their recorded sessions, I don't think we should wait around any longer.

**Shane Sibley** [10:36:35]: People can check it out afterwards.

**Shane Sibley** [10:36:37]: But I think the same thing applies for as the same thing as before applies.

**Shane Sibley** [10:36:43]: So five, try to do under five minutes, so that we can segment it off.

**Shane Sibley** [10:36:49]: Then we'll put together a form afterwards, so everyone you know, be the judge of the best presentation.

**Shane Sibley** [10:36:57]: And if you could name it for me as well, then I can go back and put the, add the name in there.

**Shane Sibley** [10:37:03]: Who wants to, who wants to dive into it and demonstrate first?

**Shane Sibley** [10:37:07]: Mateo, Peresiodas?

**Shane Sibley** [10:37:14]: Ah, Slava, you want to jump in there first?

**Shane Sibley** [10:37:16]: Yeah, yeah, absolutely.

**Slava Sazonov** [10:37:17]: I want to Mexico, so for sure.

**Slava Sazonov** [10:37:22]: Let's do it then.

**Slava Sazonov** [10:37:23]: So I'm gonna share the screen just shortly.

**Slava Sazonov** [10:37:30]: Here we go.

**Slava Sazonov** [10:37:31]: All

**Slava Sazonov** [10:37:37]: righty.

**Slava Sazonov** [10:37:38]: Pinky, please, when you can see the screen.

**Slava Sazonov** [10:37:43]: Perfecto.

**Slava Sazonov** [10:37:44]: So I'm not able to see actually, well, so if something is stuck or something, just ping me.

**Slava Sazonov** [10:37:51]: So let's begin from the beginning.

**Slava Sazonov** [10:37:53]: My hack will call Let's call it LinkedIn prospecting and automation of LinkedIn something like that.

**Slava Sazonov** [10:38:07]: So I spent basically three days or two days of trying to code something and to build something.

**Slava Sazonov** [10:38:14]: And then one day of research and deep dive of the tools.

**Slava Sazonov** [10:38:19]: So it's three steps back.

**Slava Sazonov** [10:38:22]: So my intention was I wish to create a LinkedIn prospecting tool, which will allow us from the video team, so that we will contact potential clients through the LinkedIn, so that the outreach is automatic, so that prompt for each of the lead is unique, So means the prompt will be adjusted based on

**Slava Sazonov** [10:38:45]: the lead information which he has in the LinkedIn.

**Slava Sazonov** [10:38:49]: So means profile, profile information, name, sure name, where he studied, where he worked and so on and so forth.

**Slava Sazonov** [10:38:57]: So actually, the idea was.

**Slava Sazonov** [10:39:00]: that I will provide to the agent.

**Slava Sazonov** [10:39:05]: Let's, I will show it how I build it in an 18th on 80% and then I was out of the time.

**Slava Sazonov** [10:39:13]: So my wish was, so that I start the process.

**Slava Sazonov** [10:39:15]: I provided the Google sheet with the contacts from the LinkedIn, which I would like my agent one to scrap.

**Slava Sazonov** [10:39:24]: Then all the contacts are scrapped.

**Slava Sazonov** [10:39:27]: This workflow is actually working.

**Slava Sazonov** [10:39:29]: So all the contacts are prepared.

**Slava Sazonov** [10:39:31]: And then my phantom buster, so my agent one is taking the URLs.

**Slava Sazonov** [10:39:39]: from the Google sheet and then it's scrapping the information from each of the URL, from each of the leads which I provided.

**Slava Sazonov** [10:39:49]: Then it's proceeding the information and preparing that for the second agent.

**Slava Sazonov** [10:39:55]: So it's preparing the JSON format for the agent number two, which will fetch the output to the main agent.

**Slava Sazonov** [10:40:05]: which is over here, but before that, what fetching does, it's provide the information to the open AI.

**Slava Sazonov** [10:40:13]: So I connected the chat GPT API, plus I connected the phantom booster API also to an ATM.

**Slava Sazonov** [10:40:22]: So actually in this step, the information is taking, it's sent it to open AI, where prompt, which I created is, unique based on the profiles of the leads which are over here.

**Slava Sazonov** [10:40:42]: So then the prompt is generated, the data are collected, and last, the main agent is active then, so he's taking the prompts, he's taking the contacts from here, and then it does the outreach to the leads.

**Slava Sazonov** [10:40:59]: So overall, my wish was, I'm providing the contacts from LinkedIn.

**Slava Sazonov** [10:41:04]: So here is the 10 leads, which I would like to follow up with.

**Slava Sazonov** [10:41:07]: Please create me the unique prompts.

**Slava Sazonov** [10:41:09]: Please reach out to them in this sequence and have unique prompt for each of them based on the information from the LinkedIn profile.

**Slava Sazonov** [10:41:17]: This was the wish.

**Slava Sazonov** [10:41:18]: I spent two days with anything to understand how to connect APIs, how to set up phantom booster, blah, blah, blah.

**Slava Sazonov** [10:41:25]: And then suddenly it was Sunday, and my wife was screaming to me, and I said to me, okay, I will try to see if there's solutions in the market, which can provide exactly the same what I would like to build.

**Slava Sazonov** [10:41:38]: Suddenly I checked around 10, 15 tools.

**Slava Sazonov** [10:41:42]: Some of them were nice, but too expensive.

**Slava Sazonov** [10:41:44]: Some of them were, yeah, skeptic.

**Slava Sazonov** [10:41:48]: And then I found the golden middle tool called Lem list.

**Slava Sazonov** [10:41:56]: I'm not sure if someone already used that.

**Slava Sazonov** [10:41:59]: If yes, then please share the feedbacks.

**Slava Sazonov** [10:42:01]: However, what it does, let's jump over here.

**Slava Sazonov** [10:42:06]: um so it does exactly what i would like to do actually it's it can do it can connect with the contact which i'm sharing in the google sheet so let's say i shared 20 contacts first of all what it does it sends the um request with a unique way.

**Slava Sazonov** [10:42:28]: So it can detect and scrap the name.

**Slava Sazonov** [10:42:32]: It can detect and scrap the company information, where you work, where you study it.

**Slava Sazonov** [10:42:36]: So you can adjust the text and based on your text and empty fields, it will fill in the information exactly from your contact.

**Slava Sazonov** [10:42:45]: Then it can either, when you send the connection, so after the connection, what it can do?

**Slava Sazonov** [10:42:54]: I'm scrolling down, scrolling down.

**Slava Sazonov** [10:42:57]: Sorry, not here, but over here.

**Slava Sazonov** [10:43:01]: Actually, here.

**Slava Sazonov** [10:43:03]: So, invite is accepted.

**Slava Sazonov** [10:43:05]: After that, you can decide whether you would like to send a voice message, a LinkedIn message or something else.

**Slava Sazonov** [10:43:14]: So how does voice message, for example, there is 10 or 15 predefined voices.

**Slava Sazonov** [10:43:21]: And also, you write a script and script will be unique based on his information, which this tool will scrap from his LinkedIn profile.

**Slava Sazonov** [10:43:30]: You're selecting the voice, it's sending the audio message.

**Slava Sazonov** [10:43:34]: Or it can send the LinkedIn message, not the voice message, also based on his information.

**Slava Sazonov** [10:43:40]: And you can set up the sequence how often.

**Slava Sazonov** [10:43:43]: And as well as that, it can even call if there is a number provided.

**Slava Sazonov** [10:43:47]: So actually... It does pretty much everything what I wish to do in N8N.

**Slava Sazonov** [10:43:54]: Or it can scrap.

**Slava Sazonov** [10:43:56]: It do the sequence.

**Slava Sazonov** [10:43:57]: It can send the audio message.

**Slava Sazonov** [10:43:59]: It can write the message.

**Slava Sazonov** [10:44:01]: Everything personalized because it's scrapping the information by itself from the LinkedIn.

**Slava Sazonov** [10:44:07]: And the setup, how to set up it's very easy.

**Slava Sazonov** [10:44:11]: You just say, I would like to set up a new company.

**Slava Sazonov** [10:44:15]: And then you're defining the company name.

**Slava Sazonov** [10:44:17]: So I need to define the sensei information.

**Slava Sazonov** [10:44:20]: Then it was a draft.

**Slava Sazonov** [10:44:22]: So all the information here, it just draft.

**Slava Sazonov** [10:44:25]: Then you're defining the ICPs.

**Slava Sazonov** [10:44:27]: You're defining the personas.

**Slava Sazonov** [10:44:29]: Then you're saying what is pain points, which you would like to address.

**Slava Sazonov** [10:44:33]: So here, e-commerce, SaaS providers, healthcare providers.

**Slava Sazonov** [10:44:37]: So let's continue.

**Slava Sazonov** [10:44:38]: Then we can copy paste our persona, which we would like to tackle.

**Slava Sazonov** [10:44:44]: Then we can check the leads in the next step.

**Slava Sazonov** [10:44:47]: So either we provide the Google sheet or I'm going to show you.

**Slava Sazonov** [10:44:52]: So here is a persona.

**Slava Sazonov** [10:44:54]: Let's just tick some.

**Slava Sazonov** [10:44:59]: Then in the leads, we are selecting the leads, which we'd like to tackle.

**Slava Sazonov** [10:45:04]: If it go a lot quickly.

**Slava Sazonov** [10:45:08]: Yes, so here are, for example, the contacts, which I would like to scrap the information from, and then to contact either in chat communication or in the audio communication.

**Slava Sazonov** [10:45:20]: Then in which form?

**Slava Sazonov** [10:45:22]: So in reach lead email, enrich lead phone.

**Slava Sazonov** [10:45:25]: Also, I didn't switch on here, and we can enrich through the audio message, and reach through the message.

**Slava Sazonov** [10:45:31]: So multi-channel outreach from one platform.

**Slava Sazonov** [10:45:35]: what we actually need.

**Slava Sazonov** [10:45:36]: Then pain points.

**Slava Sazonov** [10:45:38]: So we can describe our pain or client pain points, which we'd like to address.

**Slava Sazonov** [10:45:43]: So as an example, sales automation, right?

**Slava Sazonov** [10:45:47]: Then, I don't know, 24-7 support and so on and so forth.

**Slava Sazonov** [10:45:53]: Then value proposition, what we are offering, if comparing, for example, us and competitors.

**Slava Sazonov** [10:46:01]: And then at the end, you have a sequence sequence review, so how to contact those clients.

**Slava Sazonov** [10:46:09]: So email, LinkedIn form, for example, or something different.

**Slava Sazonov** [10:46:14]: This is actually my hack.

**Slava Sazonov** [10:46:18]: So I started the development and I ended up with the already developed tool.

**Slava Sazonov** [10:46:23]: As for the prices, the prices are very decent.

**Slava Sazonov** [10:46:26]: We can then, I can share it and we can discuss with the team internally.

**Slava Sazonov** [10:46:30]: There is also 14, so two weeks of trial.

**Slava Sazonov** [10:46:36]: So we can actually try, see, we can we have 500 contacts for account, and then we can decide whether we need it or not.

**Slava Sazonov** [10:46:48]: So this was pretty much.

**Slava Sazonov** [10:46:50]: I didn't at the end develop nothing.

**Slava Sazonov** [10:46:52]: I then at the end spent my time of investigating.

**Slava Sazonov** [10:46:55]: I tested around 10 tools.

**Slava Sazonov** [10:46:58]: My email now is pumped because of the notifies.

**Slava Sazonov** [10:47:01]: But anyway, I liked a lot this LLM missed tool.

**Slava Sazonov** [10:47:07]: Right on.

**Multiple speakers** [10:47:07]: So that's pretty much.

**Shane Sibley** [10:47:09]: I think this is something that we can experiment with when it comes to the knowledge transfer and list that we have generated there.

**Shane Sibley** [10:47:18]: Yeah.

**Shane Sibley** [10:47:19]: Thanks, Lava.

**Shane Sibley** [10:47:20]: Anybody have any questions on that?

**Shane Sibley** [10:47:29]: All right, who's up?

**Shane Sibley** [10:47:37]: Don't everybody jump in at once?

**Panagiotis Apostolidis** [10:47:40]: Yeah, we can go next.

**Daniel Nowak** [10:47:43]: So this is a hack.

**Panagiotis Apostolidis** [10:47:47]: related to knowledge transfer mostly.

**Panagiotis Apostolidis** [10:47:50]: This is something that me and Matteo will be working on.

**Panagiotis Apostolidis** [10:47:53]: Let me share my screen.

**Panagiotis Apostolidis** [10:48:02]: So we managed to pull two connections right directly in the knowledge base.

**Panagiotis Apostolidis** [10:48:10]: So it's pretty simple.

**Panagiotis Apostolidis** [10:48:12]: You can, I will actually show you what it's doing and then pretty much understand.

**Panagiotis Apostolidis** [10:48:19]: So let's say you want to pull your Slack messages directly to your replica, to your agent.

**Panagiotis Apostolidis** [10:48:25]: All you have to do is like, create a demo app on Slack API and grab the user of Token, load channels.

**Panagiotis Apostolidis** [10:48:40]: Then you can select the channels that you want to load messages from.

**Panagiotis Apostolidis** [10:48:43]: Let's say I want to select all these four channels, continue, select my user, select date, and then hit extract messages.

**Panagiotis Apostolidis** [10:48:59]: So right now there is a little preview on how messages and from which channels I am extracting these messages from.

**Panagiotis Apostolidis** [10:49:08]: And then by clicking, adding to knowledge base, you can see that this text entry is created.

**Panagiotis Apostolidis** [10:49:16]: So this is something that I did a few minutes ago, just so we don't have to wait for the process to finish.

**Panagiotis Apostolidis** [10:49:23]: You can see that these messages are from me, and this is pretty much what I've been sharing in these channels.

**Panagiotis Apostolidis** [10:49:29]: So you can quickly create a demo app for specific employee.

**Panagiotis Apostolidis** [10:49:36]: give the specific permissions.

**Panagiotis Apostolidis** [10:49:38]: All these permissions are mentioned here.

**Panagiotis Apostolidis** [10:49:43]: And you need to install the app on the census slack, grab the auth token, and then give the auth token to the interface, and then you can pretty much load the messages.

**Panagiotis Apostolidis** [10:49:57]: So this is for slack, pretty simple.

**Panagiotis Apostolidis** [10:50:01]: And then we have the same thing for Lina.

**Panagiotis Apostolidis** [10:50:04]: So for linear, you need to create like the specific user needs to go to linear create an API key directly from the dashboard and then grab that API key, paste it.

**Panagiotis Apostolidis** [10:50:18]: And then by doing that, you can load pretty much every user and every task inside linear.

**Panagiotis Apostolidis** [10:50:25]: So let's say I select, let's say I select Vadim.

**Panagiotis Apostolidis** [10:50:29]: You can select teams, projects, define like be more specific if you want.

**Panagiotis Apostolidis** [10:50:35]: Select dates, I'll go back one month.

**Panagiotis Apostolidis** [10:50:40]: You can select an end date as well, but if you don't, it will pretty much select the current date as an end date.

**Panagiotis Apostolidis** [10:50:51]: Let's wait for the task to load.

**Panagiotis Apostolidis** [10:50:58]: So we can see all of Vadim's tasks over the past, like pretty much one month.

**Panagiotis Apostolidis** [10:51:04]: 19 tasks in total, you can browse through them.

**Panagiotis Apostolidis** [10:51:06]: And then if you click upload tasks to knowledge base, you can see that one by one the tasks are being added as text entries.

**Panagiotis Apostolidis** [10:51:17]: So you can see an example here.

**Panagiotis Apostolidis** [10:51:24]: It takes some time to load because it's on development.

**Panagiotis Apostolidis** [10:51:34]: Yeah, so development is a bit slow.

**Panagiotis Apostolidis** [10:51:36]: Ideally, it should open to a new tab when I click it, but it's compiling.

**Panagiotis Apostolidis** [10:51:44]: I will start the page.

**Panagiotis Apostolidis** [10:51:45]: Oh, there you go.

**Panagiotis Apostolidis** [10:51:49]: Okay.

**Panagiotis Apostolidis** [10:51:50]: Let's go back.

**Panagiotis Apostolidis** [10:51:55]: So yeah, you can see like project details.

**Panagiotis Apostolidis** [10:52:00]: like statuses, states and stuff, title and everything.

**Panagiotis Apostolidis** [10:52:03]: It should all of the information relate to the task pre-filled here in the text entry.

**Panagiotis Apostolidis** [10:52:11]: So, yeah.

**Mateo Kapllani** [10:52:14]: To one thing, Sorry, one thing that I would like to add is that the last time I also tested this out.

**Mateo Kapllani** [10:52:21]: So there is a really nice connection with linear and slack.

**Mateo Kapllani** [10:52:27]: So for example, there was a linear task that we created through slack and we had the conversation of linear of slack on the linear on the description.

**Mateo Kapllani** [10:52:36]: so because we have this knowledge base at the moment it took the conversation and it also creates a summary if you go on the knowledge base and you go to a specific task with a specific description which might be much more it also creates a really nice summary for the AI to grab basically so if it

**Mateo Kapllani** [10:52:56]: creates a really nice summary it can have a basic like easier rag to hit and respond to the user.

**Mateo Kapllani** [10:53:04]: So that is also one reason that we separated the task on linear one by one.

**Mateo Kapllani** [10:53:09]: So we can have better data given to the replica and they will create a symbolization and then we can have like a better rag system to support this functionality.

**Mateo Kapllani** [10:53:22]: Yeah.

**Mateo Kapllani** [10:53:25]: Yes, Martin.

**Martine Haug Olsen** [10:53:26]: one question can you because you said that the end date if you didn't set it it would just be set to the day that you like put it in would be possible to add like an automation process probably on top of this so that once you have added project on linear for example could the replica just

**Multiple speakers** [10:53:47]: continuously follow that project with me tickets on that person so basically you wouldn't need to manually always go and yeah Yeah, you see this is a lot of manual work that you have to do, like create the bots, take the API keys and paste them all together.

**Panagiotis Apostolidis** [10:54:01]: So, for example, on the Slack side, I will talk about Slack.

**Mateo Kapllani** [10:54:11]: here can i answer about linear so it's on point yeah so you can continue with slack afterwards but with with with with this with linear as you said yeah we have to go out with the basic functionality we have with knowledge base but it's not a hard implementation because if you think about linear

**Mateo Kapllani** [10:54:29]: also has web hooks so you just need to set up a web hook which will grab the information like for say let's say for your tasks and every time you do you add some logic like check if it's Martin task and if it's that just add it on the knowledge entry since we have the API it's like super easy to do

**Mateo Kapllani** [10:54:49]: yeah Panagot, you can continue if you want to add something.

**Panagiotis Apostolidis** [10:54:53]: Yeah, yeah, I was going to add about the Slack site.

**Panagiotis Apostolidis** [10:54:58]: Pretty much, if you remember, when we were working on connecting LinkedIn and X to like the replica creation, you can do the same thing for Slack.

**Panagiotis Apostolidis** [10:55:08]: and pretty much like automatically get the users messages so that the replica can have the context, but I didn't want to to tackle this because it would mess up with the current authentication that we have.

**Panagiotis Apostolidis** [10:55:26]: That's why you need to create the bot and paste the auth token.

**Panagiotis Apostolidis** [10:55:32]: But yeah, I guess with Cronjobs and stuff, you can automatically get the data inside that knowledge base.

**Panagiotis Apostolidis** [10:55:39]: Let you authenticate.

**Mateo Kapllani** [10:55:40]: Also, Spain, part of this idea was mostly cause of the knowledge transfer idea that Dan had provided.

**Mateo Kapllani** [10:55:49]: So the way we thought it is like, since we want to create a dynamic way to extract information from the guy that is leaving the company, It would be, well, most companies have like a task manager application, linear, general, asana, or whatever is that.

**Mateo Kapllani** [10:56:07]: So having all that context, I think is like actually important for the knowledge transfer.

**Mateo Kapllani** [10:56:15]: Definitely.

**Shane Sibley** [10:56:15]: And I mean, we're starting with the off boarding, right?

**Shane Sibley** [10:56:18]: But if it can actually be a bit more, a bit more of a sticky tool where people use it internally before some and it's continuously up to date as to like as for what Martin was asking.

**Shane Sibley** [10:56:31]: Then it becomes much more valuable internally used as well.

**Shane Sibley** [10:56:34]: So if the outputs of that replica can then be used within Slack, then, you know, Dan or myself or somebody would be able to say, where are we out with this project?

**Shane Sibley** [10:56:44]: And then we could actually talk to a bot, and up to date with the project itself.

**Shane Sibley** [10:56:51]: So, yeah.

**Mateo Kapllani** [10:56:53]: Yeah, that's Yeah.

**Mateo Kapllani** [10:56:55]: Yeah.

**Mateo Kapllani** [10:56:55]: Well, with the environment you have created with API, it's really easy to do.

**Mateo Kapllani** [10:56:59]: Like literally, you can have that in one day.

**Mateo Kapllani** [10:57:04]: Very cool.

**Multiple speakers** [10:57:05]: Not that I'm giving promises one day.

**Panagiotis Apostolidis** [10:57:13]: Okay, yeah, that's about it.

**Panagiotis Apostolidis** [10:57:17]: Well done.

**Shane Sibley** [10:57:20]: Has anybody else put something together for today?

**Daniel Nowak** [10:57:30]: Well, in that case, if there is some time left, I can show my stuff.

**Daniel Nowak** [10:57:36]: Yeah, always some feedback valuable.

**Daniel Nowak** [10:57:39]: So guys, sorry if that will sound like a pitch, but do you know what is usually the biggest pain in the ass for the sales people once they're starting to do their work?

**Daniel Nowak** [10:57:51]: Well, I guess you might not know necessarily, but trying to find the right prospects.

**Daniel Nowak** [10:57:57]: And with multiple tools like even Slava showed, well, it's sometimes to really find your way around.

**Daniel Nowak** [10:58:04]: And let me actually pull up the screen.

**Daniel Nowak** [10:58:07]: The entire screen is the best.

**Daniel Nowak** [10:58:10]: So, for instance, this is the Apollo, which is a huge tool and try to find really relevant information you're looking for within this, well, dozens, hundreds, hundreds of different filters, whatever.

**Daniel Nowak** [10:58:26]: So definitely pain in the ass, a lot of clicking, a lot of filtering and not necessarily the value added each and every time unless you're looking for for maybe a big group of people and then upload them wherever.

**Daniel Nowak** [10:58:40]: So, it is usable, but not necessarily each and every time.

**Daniel Nowak** [10:58:45]: But what if we could actually utilize our own API, which is actually very flexible and very, let's say, wonderful in terms of the use, of use as well.

**Daniel Nowak** [10:58:57]: So here is a tool which I have put together throughout the last few days.

**Daniel Nowak** [10:59:04]: So what it does, actually, it uses the database from Apollo.

**Daniel Nowak** [10:59:09]: So it's calling its API.

**Daniel Nowak** [10:59:11]: Apparently, there's a few different APIs.

**Daniel Nowak** [10:59:13]: They didn't make the life easier, including that they don't allow their direct calls from the web.

**Daniel Nowak** [10:59:19]: It has to go to reverse proxy.

**Daniel Nowak** [10:59:21]: So Daniel had to learn how to deal with the super base on the go.

**Daniel Nowak** [10:59:24]: But that's a completely different story.

**Daniel Nowak** [10:59:27]: And yes, definitely not a very funny story.

**Daniel Nowak** [10:59:31]: But how it works.

**Daniel Nowak** [10:59:33]: So here you have prospects.

**Daniel Nowak** [10:59:35]: But actually, let me show you how it can be used on the live example.

**Daniel Nowak** [10:59:41]: So let me just go to a... Buyer intent signals, for instance.

**Daniel Nowak** [10:59:46]: Over here, I've got the companies that are looking on our own website, or we're looking at.

**Daniel Nowak** [10:59:52]: For instance, I have Aspire lifestyles.

**Daniel Nowak** [10:59:55]: So I allowed myself actually to already search for that Aspire lifestyles, previously, but let's just search for prospects.

**Daniel Nowak** [11:00:05]: And here we are.

**Daniel Nowak** [11:00:06]: We have prospects for Aspire lifestyles.

**Daniel Nowak** [11:00:09]: But having a prospect is that's not it.

**Daniel Nowak** [11:00:12]: Well, we definitely need way more information to be gathered, not just the name of the company and name of the CEO.

**Daniel Nowak** [11:00:19]: And this is where the tool comes further.

**Daniel Nowak** [11:00:22]: So obviously, I can jump over to LinkedIn profiles or LinkedIn profile of a company, but I have already some information like number of employees.

**Daniel Nowak** [11:00:31]: I can check the company descriptions.

**Daniel Nowak** [11:00:33]: I've got the verticals over here, and I can even explore the latest news related to that particular company.

**Daniel Nowak** [11:00:41]: Obviously, it's not about reading all of this and well scratching my head what to do with it next.

**Daniel Nowak** [11:00:47]: So what happens next?

**Daniel Nowak** [11:00:48]: Let's say I've got Matthew over here, CEO of Aspire lifestyles.

**Daniel Nowak** [11:00:53]: So I can jump over to this message generator and over here what happens.

**Daniel Nowak** [11:00:59]: So let's say again, I would like to have a look what kind of news they have over Maybe not all of them are relevant, maybe some of them, only some of them are relevant.

**Daniel Nowak** [11:01:07]: So let's say this is the relevant message.

**Daniel Nowak** [11:01:10]: So what I do with all of those information, with the name of the prospect, with a company name, with the company description, with the news related to the company, with all of the research gathered throughout the over here.

**Daniel Nowak** [11:01:26]: Well, I can have a look and Well, go for email, LinkedIn, maybe cold call script, all based on actually Sensei API connection to my replica somewhere out there, which is trained with our own tonality, with our brand, brand voice, with everything that replica needs to Well, Apparently, I didn't go

**Daniel Nowak** [11:01:48]: through all the hassle of training the replica through the API.

**Daniel Nowak** [11:01:51]: I just set the test API replica, which is connected, but there is no information.

**Daniel Nowak** [11:01:57]: So, guys, looking forward to ability to actually connect my replica created in the studio.

**Daniel Nowak** [11:02:02]: But anyway, once I click generate message, it generates message based on all the information, which is related to the prospect company, and also news information found somewhere out there.

**Daniel Nowak** [11:02:15]: Here is a prospecting email.

**Daniel Nowak** [11:02:19]: Obviously, as said, it's based on a test replica, so it doesn't have all the branding out there, but it's all about the company which we're looking at, which is Aspire Lifestyles.

**Daniel Nowak** [11:02:30]: It's all about the news, which are related to that company as well.

**Daniel Nowak** [11:02:34]: So we have full prospecting email, message, whatever we're looking at, ready to go, without running around looking for a different, filters within the Apollo or any other prospecting tool, everything is simply ready to go.

**Daniel Nowak** [11:02:53]: All stored within here, so as you know, there are a few things.

**Daniel Nowak** [11:02:56]: I needed.

**Daniel Nowak** [11:02:57]: Apollo only needs their one API key.

**Daniel Nowak** [11:03:01]: We need, well, API key, user ID and the replica UID.

**Daniel Nowak** [11:03:04]: But anyway, well, that was way, way easier with our own API than the Apollo.

**Daniel Nowak** [11:03:11]: So just... So that's the tool, not only to make my life easier, which can make my life easier, but actually also to showcase the power of a sensei API.

**Daniel Nowak** [11:03:23]: So let's imagine right now I'm going to delete the Apollo key.

**Daniel Nowak** [11:03:26]: Let's just save all of this.

**Daniel Nowak** [11:03:29]: And let's go to the prospects.

**Daniel Nowak** [11:03:34]: Whatever.

**Daniel Nowak** [11:03:38]: And we're going actually to a mock data, which I can use now to showcase the power of a sensei API on a mock data which I have prepared as well.

**Daniel Nowak** [11:03:49]: So it can be used both for our own prospecting needs and it can be used as a use case or a demo for a sensei API.

**Daniel Nowak** [11:04:00]: What could go further, maybe HubSpot connection, so I won't have to click twice to find the research intense signals and copy and paste the company name.

**Daniel Nowak** [11:04:11]: Maybe a Gmail connection, so I'll be able to send over the emails automatically.

**Daniel Nowak** [11:04:16]: So MVP is already So I guess that would be Thank you.

**Daniel Nowak** [11:04:29]: Nicely done, looking forward to testing it Actually, I've used it already for a demo to a marketing agency this morning because they were looking for some kind of a knowledge management system.

**Daniel Nowak** [11:04:41]: And I showcase how easy is to put a solution together with a sensei API.

**Shane Sibley** [11:04:47]: And now are they interested in the sensei API or your solution?

**Multiple speakers** [11:04:51]: Sensei API.

**Daniel Nowak** [11:04:54]: Sensei Pops and managing knowledge within the marketing agency.

**Shane Sibley** [11:05:00]: Yeah, nicely done, looks good.

**Shane Sibley** [11:05:02]: Now, what's your hackathon called?

**Shane Sibley** [11:05:05]: Your submission called?

**Shane Sibley** [11:05:06]: I called it Prospect AI.

**Daniel Nowak** [11:05:08]: Prospect AI.

**Shane Sibley** [11:05:11]: Perfect.

**Shane Sibley** [11:05:19]: You just said knowledge transfer, Matteo.

**Shane Sibley** [11:05:22]: Would you like to adjust that?

**Shane Sibley** [11:05:37]: AI knowledge transfer, okay.

**Shane Sibley** [11:05:49]: forgot actually to add.

**Daniel Nowak** [11:05:49]: I forgot actually to add, have you noticed the floating banner on the bottom, powered by Sensei API and the AI engine just to be sure that people see that.

**Shane Sibley** [11:06:05]: Yeah, I mean, it was, that one was difficult to miss.

**Shane Sibley** [11:06:11]: But good branding.

**Shane Sibley** [11:06:14]: Is there anybody left to go today, or is that it for today?

**Daniel Nowak** [11:06:21]: So, this is what I was talking about, and actually thanks to Nika this morning, so beautiful one provided.

**Shane Sibley** [11:06:40]: All right, guys, well, yeah, nice and light.

**Shane Sibley** [11:06:43]: Makes it easy to slice it out.

**Shane Sibley** [11:06:47]: So we'll be able to put that into a Slack channel and then put it up for a vote.

**Shane Sibley** [11:06:56]: Thanks a lot for your submissions and it was, enjoy the rest of your day.

**Shane Sibley** [11:07:04]: goodbye everyone, guys.

**Martine Haug Olsen** [11:07:05]: Bye-bye.

**Martine Haug Olsen** [11:07:06]: Bye-bye.

---
*Backed up from MeetGeek on 2026-03-30 09:01*
