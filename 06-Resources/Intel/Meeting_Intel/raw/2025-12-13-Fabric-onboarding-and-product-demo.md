# Fabric onboarding and product demo

**Date:** 2025-12-13
**Duration:** Unknown
**Meeting ID:** 47a87920-d1aa-4e3e-b1c7-3778f59aad66

## Participants
- *Participants not listed*

### Summary

The meeting combined a live onboarding/demo of Fabric with strategic discussion. The team activated David's account and walked through the user portal, memories/threads, and MCP integrations to surface Fabric data into LLMs (Claude, GPT). They covered authentication steps, novelty scoring analytics, and practical use cases (chatbots, FAQs, developer-built experiences) as well as Fabric's FinTech-style aggregation model and pricing approach (developers pay). Funding status and potential future raises were discussed, alongside data integrations, rollout discipline (only enabling processed sources), cross-platform identity/reposting ambitions, and privacy/ethical concerns for sensitive jurisdictional scenarios.

## Full Transcript

**David Orban** [17:00:08]: I am great.

**David Orban** [17:00:10]: It's really,

**Eeshita Pande** [17:00:11]: really nice to meet you.

**Eeshita Pande** [17:00:12]: I've heard a lot about you from Luca, who's here, and Massimo, who should also come by and say hello for a minute.

**Luca Bertelli** [17:00:20]: Oh, yeah.

**David Orban** [17:00:21]: Wonderful to see Massimo.

**David Orban** [17:00:22]: I haven't seen him for some time, and I'm happy that Luca joined you.

**David Orban** [17:00:30]: I'm sure he's a very valuable addition to the

**Eeshita Pande** [17:00:33]: team.

**Eeshita Pande** [17:00:33]: He is, he is, yes.

**Eeshita Pande** [17:00:35]: He's already like started working with us.

**Eeshita Pande** [17:00:38]: We're working together all the time.

**Eeshita Pande** [17:00:39]: He was with us this weekend, or like last weekend as well, and we're just having a really fun time together.

**Eeshita Pande** [17:00:45]: So

**David Orban** [17:00:49]: I haven't read everything you posted on your sub stack yet.

**David Orban** [17:00:55]: Didn't have the time.

**David Orban** [17:00:56]: But I have over the years been a user of things that tried to do what you are now trying to do.

**David Orban** [17:01:08]: And

**Eeshita Pande** [17:01:11]: too

**David Orban** [17:01:11]: many times founders say, oh, I need to hurry up.

**David Orban** [17:01:19]: It may be too late, it's never too late.

**Eeshita Pande** [17:01:22]: Yeah,

**David Orban** [17:01:22]: as proven by the fact that we are not using MySpace, but Facebook, for those of us who do, we are not using AltaVista, but Google to search, and so on.

**David Orban** [17:01:38]: And there may be many more, but off the top of my head, I am able to mention friend feed, for example.

**David Orban** [17:01:52]: which had a very dedicated group of followers able to aggregate the footprint of their various social networks.

**David Orban** [17:02:10]: And another one that comes into my mind is clout with a K.

**Eeshita Pande** [17:02:16]: And

**David Orban** [17:02:17]: cloud aimed to monetize your aggregate social footprint.

**David Orban** [17:02:27]: And I think French feed was acquired.

**David Orban** [17:02:33]: I don't remember by whom we could find out.

**David Orban** [17:02:36]: Facebook.

**David Orban** [17:02:38]: Oh, was it, all right.

**Luca Bertelli** [17:02:40]: Yeah, 2009.

**David Orban** [17:02:43]: So, you

**Eeshita Pande** [17:02:43]: know, I think, like, David, it's an interesting point, right?

**Eeshita Pande** [17:02:45]: I think, like, being early is often, like, more of an indicator of being wrong than is, like, being on time.

**Eeshita Pande** [17:02:53]: And I think, like, one of the big reasons why actually your digital self has not been a successful, like, product until now.

**Eeshita Pande** [17:03:01]: is because there was no other application for your digital self to really go to and to interact with.

**Eeshita Pande** [17:03:08]: And what we found is, actually, LLMs are a great place for your digital self to plug into.

**Eeshita Pande** [17:03:15]: And so you could aggregate the data from Google, from meta, from all these search and social platforms.

**Eeshita Pande** [17:03:20]: But the most you could do is either sell it for like a few dollars, which a lot of people have tried to do, and it's really not a very compelling proposition.

**Eeshita Pande** [17:03:29]: But only now, after LLMs, has it actually become possible to bring this digital self to other applications, and then those applications actually personalize to fit you.

**Eeshita Pande** [17:03:39]: So I think like I would almost say that and then you know like one of the there are like quite a few others who've started like you know in this like day and age there's like Kudos Lab labs which is like shelf there is cross hatch a non-key tool trying to do like some version of integrating your

**Eeshita Pande** [17:03:56]: data but even so like you know even a few years ago was was almost too early and you know we raised a little bit of money toward the end of last year and one of the big pieces of feedback we had from a lot of RVCs was like, is this still too early for this idea?

**Eeshita Pande** [17:04:12]: And, you know, I think we're finding with the conversion rates that we're seeing and the value that we're able to see in the product ourselves, that is actually probably we're right on time this time around.

**David Orban** [17:04:24]: Crossing fingers.

**Eeshita Pande** [17:04:26]: Yes.

**Eeshita Pande** [17:04:27]: Yeah, so it was it was really lovely to see you on board onto Fabric as well.

**Eeshita Pande** [17:04:32]: And I've heard a lot about you from both Luca and Massimo.

**Eeshita Pande** [17:04:36]: And I was looking into like some of the work that you've done as well, like in longevity and in, you know, all these areas that I personally am very invested in as well.

**Eeshita Pande** [17:04:45]: So I was really happy to get a chance to, you know, onboard you onto Fabric.

**David Orban** [17:04:50]: All right, let's do

**Eeshita Pande** [17:04:51]: it.

**Eeshita Pande** [17:04:52]: Do you want to share your screen with us and we can just do it live?

**Eeshita Pande** [17:04:56]: Mm-.

**Eeshita Pande** [17:05:04]: Perfect.

**Eeshita Pande** [17:05:05]: You should I see you're on the user portal already.

**Eeshita Pande** [17:05:07]: Yeah.

**Eeshita Pande** [17:05:11]: Did we approve David Luca?

**Eeshita Pande** [17:05:14]: No, no, let me quickly do it.

**Eeshita Pande** [17:05:17]: Okay.

**Eeshita Pande** [17:05:23]: Perfect.

**Eeshita Pande** [17:05:24]: Yep, I've now activated you, David, so you should get a text from me saying that you can now access fabric.

**Eeshita Pande** [17:05:46]: Maybe.

**Eeshita Pande** [17:05:47]: Yeah, it takes

**Luca Bertelli** [17:05:48]: it takes a couple of a couple of seconds, but if you want, you can already go on up.onfabric.io.

**Luca Bertelli** [17:06:00]: So removing the onboarding, yeah.

**Luca Bertelli** [17:06:04]: Yeah, here we go.

**Eeshita Pande** [17:06:06]: Yeah, so here we have, yeah, like a lot of your memories that we've created from the data that you've shared with us.

**Eeshita Pande** [17:06:13]: And this sort of, you know, is the context that feeds into the LLMs that you might like to connect it with.

**Eeshita Pande** [17:06:20]: So we're supporting Cloud, we're also supporting GPT, Mistral, cursor, like all the standard like MCP clients.

**Eeshita Pande** [17:06:27]: And the idea is you just add our MCP server and then Fabric's memories or like your memories like through Fabric are available to the LLM as context.

**Eeshita Pande** [17:06:36]: sight.

**David Orban** [17:06:38]: Wonderful.

**David Orban** [17:06:45]: Okay, so let me connect

**Eeshita Pande** [17:06:48]: Google.

**Eeshita Pande** [17:06:52]: Are you, is your account, are you based in, I saw your number, like are you based in the US or are you based in Europe?

**David Orban** [17:06:59]: Who

**Eeshita Pande** [17:06:59]: knows?

**Eeshita Pande** [17:07:02]: We'll

**David Orban** [17:07:04]: find out.

**David Orban** [17:07:05]: Even Google doesn't know, because for example, they have a specific... Sorry.

**David Orban** [17:07:16]: They have a specific page that tells you where your account is located as far as they are concerned.

**David Orban** [17:07:28]: And that says Europe, then they have the family account that doesn't allow me to add my wife because they say I'm not in

**Eeshita Pande** [17:07:36]: Europe.

**Eeshita Pande** [17:07:38]: Even

**David Orban** [17:07:39]: Google is confused about

**Eeshita Pande** [17:07:41]: it.

**Eeshita Pande** [17:07:42]: I think this is good feedback.

**Eeshita Pande** [17:07:44]: We've given like some feedback to Google on this.

**Eeshita Pande** [17:07:47]: You have to select the duration as well.

**Eeshita Pande** [17:07:59]: Yep, so now this will also enable us to create these memories from your Google data.

**Eeshita Pande** [17:08:04]: And we're supporting, we have integrations with Pinterest, LinkedIn, TikTok, like a bunch of others.

**Eeshita Pande** [17:08:09]: And we're also scoping out how to get your prompts from your different LLMs that you're using.

**Eeshita Pande** [17:08:15]: And we can try and connect your digital self now in Claude.

**Eeshita Pande** [17:08:21]: And here is Massimo, you will see after.

**Eeshita Pande** [17:08:23]: Ciao, David.

**Eeshita Pande** [17:08:26]: One

**David Orban** [17:08:27]: second, I have to go back, who knows where?

**David Orban** [17:08:34]: Where are you?

**Eeshita Pande** [17:08:39]: Ciao.

**Eeshita Pande** [17:08:43]: Really.

**Eeshita Pande** [17:08:44]: How are you?

**David Orban** [17:08:45]: I am very well in you.

**Eeshita Pande** [17:08:47]: Nice.

**Eeshita Pande** [17:08:48]: Are you in Italy?

**David Orban** [17:08:50]: Right now I am just back from Abu Dhabi and I am flying on Monday to Sydney.

**David Orban** [17:08:55]: Yes.

**David Orban** [17:08:56]: Will you

**Eeshita Pande** [17:08:56]: be in Italy over Christmas?

**Eeshita Pande** [17:08:59]: I will

**David Orban** [17:08:59]: be in Sydney until January 15. Oh, okay,

**Eeshita Pande** [17:09:02]: no, I was saying because otherwise I would have come to Milan with Luca and we could have met up, but I guess we will be for another time.

**David Orban** [17:09:12]: Absolutely, London in September and I will be soon enough again, and it will be wonderful to meet in person both the two of you as well as Isita.

**Eeshita Pande** [17:09:26]: Thank you, David.

**Eeshita Pande** [17:09:27]: Yeah, it would be very nice.

**Eeshita Pande** [17:09:28]: Like, do let us know when you're in London and yeah, it'd be great to get dinner or something together.

**Eeshita Pande** [17:09:33]: All right.

**David Orban** [17:09:35]: So you mentioned the... And...

**Eeshita Pande** [17:09:39]: All right.

**David Orban** [17:09:40]: So you mentioned that there are these other connectors.

**David Orban** [17:09:45]: They are not... accessible from my interface.

**David Orban** [17:09:51]: Is there a URL I need to go

**Eeshita Pande** [17:09:52]: to?

**Eeshita Pande** [17:09:53]: So

**David Orban** [17:09:54]: we are still in the process of being made available to beta testers?

**David Orban** [17:09:58]: Yes,

**Eeshita Pande** [17:09:59]: that's correct.

**Eeshita Pande** [17:09:59]: So we have, while we have the integration, so we've already integrated with TikTok, booking, Pinterest, LinkedIn, and we're getting more and more live, but the actual processing of the data, i.e.

**Eeshita Pande** [17:10:11]: making sense of it, we've only done for Google and Instagram posts and stories.

**Eeshita Pande** [17:10:17]: And so over the coming months, we'll bring along more and more data sources and we'll actually make sense of them.

**Eeshita Pande** [17:10:23]: And so we decided that if we can't make sense of the data, it doesn't make any sense for people to connect it and then not be able to use it.

**Eeshita Pande** [17:10:31]: So we only bring it live after we have a little bit of understanding of it.

**David Orban** [17:10:36]: Very interesting that.

**David Orban** [17:10:37]: So I already saw in the interface that the, I mean, I love chat GPT and all the LLMs,

**Eeshita Pande** [17:10:58]: but

**David Orban** [17:10:59]: isn't it, at least to me, it is a bit, worse than humbling it's it's the meaning that they ruined so many of my favorite words.

**Eeshita Pande** [17:11:16]: I

**David Orban** [17:11:18]: always use m dashes in my prose.

**Eeshita Pande** [17:11:21]: Me too, me too.

**Eeshita Pande** [17:11:23]: Yes, I

**David Orban** [17:11:24]: find myself deleting m dashes so that people uselessly get alerted about them.

**David Orban** [17:11:34]: Tapestry is one of my favorite words.

**Eeshita Pande** [17:11:37]: Yes.

**Eeshita Pande** [17:11:38]: And so many others

**David Orban** [17:11:40]: that are overused or at least were at the beginnings of probably GPT-3 or something like that.

**David Orban** [17:11:49]: Anyway, that's just an aside.

**Eeshita Pande** [17:11:52]: It's so or true like I love the M- dashes and now like I have to delete them from every email, every text.

**Eeshita Pande** [17:11:59]: I just like them so like visually they're so much nicer than the single dash like I hate the single dash and so now I have to reverse to the colon or the semicolon

**David Orban** [17:12:09]: so so next question yes I use colon as well or even just commas but but the next question regarding M dashes Are you making the mistake that GPT does too of leaving spaces before and after, or you are using proper typography, typographical convention, and there is no space

**Eeshita Pande** [17:12:34]: between... You know, Luca will tell you about my attention to detail, as he's been, unfortunately, working for the last few weeks with me.

**Eeshita Pande** [17:12:44]: But I use Oxford commas properly, and I use M-Dashes properly.

**Eeshita Pande** [17:12:50]: Yeah, and so, you know, I'm a big believer in good typography.

**David Orban** [17:12:54]: So I need your help because I joined a team recently in Abu Dhabi.

**David Orban** [17:13:01]: And I'm accustomed to US spelling and I follow the Chicago Book of Style.

**David Orban** [17:13:12]: And in the UAE, they follow British spelling.

**David Orban** [17:13:17]: And I was trying to find what is the right reference replace the Chicago Book of Style to be used.

**David Orban** [17:13:29]: And do you have any recommendation?

**Eeshita Pande** [17:13:32]: I have like no idea actually.

**Eeshita Pande** [17:13:34]: I just like, you know, I have no idea.

**Eeshita Pande** [17:13:37]: I don't know.

**Eeshita Pande** [17:13:38]: Like that is an interesting, yeah, like no idea.

**Eeshita Pande** [17:13:43]: I mean, I learned to speak and write English, but I never actually, I grew up in India, but I never actually like, referred to like a reference

**David Orban** [17:13:55]: sure no problem and if I if I find something and I think it could be useful I will tell

**Eeshita Pande** [17:14:02]: you that would be amazing yeah yeah like would love that

**David Orban** [17:14:05]: okay let's go back to the fabric tapestry

**Eeshita Pande** [17:14:09]: yes so

**David Orban** [17:14:10]: I noticed that you are interpreting the posts Are these interpretations coming from the image being analyzed as well?

**Eeshita Pande** [17:14:24]: Yes, that's correct.

**Eeshita Pande** [17:14:26]: So if you go on the little info button on the far right of the memory, you'll see, yeah.

**Eeshita Pande** [17:14:34]: There's an associated, sorry, this is the associated thread.

**Eeshita Pande** [17:14:38]: So this is the associated post.

**Eeshita Pande** [17:14:39]: So it's a photo of a promotional poster for the Terrace and Colloquium.

**Eeshita Pande** [17:14:45]: And if you go back, and if you go on threads, you will see the actual images as well that we're using.

**Eeshita Pande** [17:14:50]: So if you change the resource on the right, where it says memories to threads.

**Eeshita Pande** [17:15:00]: Yeah, and if you now click again on the, on the, So you'll see that this is the asset that we're we're using.

**Eeshita Pande** [17:15:12]: Yeah, and then this becomes a really useful context for the LLM, which is then able to search over these memories.

**Eeshita Pande** [17:15:20]: So would love for you to connect like one of your LLMs and see how fabric actually works with your LLMs.

**Eeshita Pande** [17:15:27]: Sure, let's do that.

**Eeshita Pande** [17:15:28]: Yeah, so do you use Clode Pro?

**Eeshita Pande** [17:15:31]: Yeah, okay.

**David Orban** [17:15:34]: I'm on Max.

**Eeshita Pande** [17:15:36]: Yeah, perfect, even better.

**Eeshita Pande** [17:15:38]: You know, yes, yes, you open this in Clode.

**Eeshita Pande** [17:15:46]: Perfect.

**Eeshita Pande** [17:15:48]: Yeah, and if you just add yeah, step three.

**Eeshita Pande** [17:16:03]: Yeah, step three.

**Eeshita Pande** [17:16:07]: Yeah.

**Luca Bertelli** [17:16:16]: Yep.

**Eeshita Pande** [17:16:28]: Yep, I think it's ready.

**Eeshita Pande** [17:16:31]: Yeah, I think if you configure it and select the tools.

**Eeshita Pande** [17:16:35]: So ask fabric is the main tool that you should turn on and the rest are, you know, just for some GPT syntax.

**Eeshita Pande** [17:16:42]: But yeah, now fabric is ready.

**Eeshita Pande** [17:16:43]: So now in any chat that you would like to, Claude can ask fabric about anything to do with your digital self.

**Eeshita Pande** [17:16:58]: Thanks.

**David Orban** [17:17:27]: So what is the right way to trigger the tool because this actually went to look at the history rather than the competition

**Eeshita Pande** [17:17:36]: history.

**Eeshita Pande** [17:17:37]: Yeah, so like, you know, essentially there are a few ways.

**Eeshita Pande** [17:17:40]: One is the tool descriptions are good enough that if Claude cannot actually understand in its memory what to answer, it will fall back to the tool.

**Eeshita Pande** [17:17:49]: The other way of doing it is you can just say, what did I talk about in September?

**Eeshita Pande** [17:17:54]: Ask Fabric.

**Eeshita Pande** [17:17:55]: and that will just default directly to asking Fabric.

**Eeshita Pande** [17:18:12]: I'm interested to see if the MCP server turns up in desktop immediately or it needs some, ah, did.

**Luca Bertelli** [17:18:20]: And if you expand, you can see what actually Claude asked and what is the response from fabric.

**Luca Bertelli** [17:18:33]: Well, the response is still coming probably, that's why.

**Luca Bertelli** [17:18:41]: Oh,

**Eeshita Pande** [17:18:41]: yeah, there.

**Eeshita Pande** [17:18:58]: I like this flag.

**Eeshita Pande** [17:19:00]: Dangerously skip permission.

**David Orban** [17:19:02]: Yolo all the way.

**Eeshita Pande** [17:19:06]: Let me, yeah, find the... One sec.

**David Orban** [17:19:24]: I don't think I remember where it was.

**Eeshita Pande** [17:19:35]: So get out here.

**Eeshita Pande** [17:20:23]: I think you'll need to add the MCP directly here like it's not going to work with cloud desktop.

**Eeshita Pande** [17:20:29]: So I'm just sending you the the command line like you know command that you can add which is I've added it in the chat.

**Eeshita Pande** [17:20:37]: Thank you.

**Eeshita Pande** [17:20:38]: Of course.

**Eeshita Pande** [17:20:58]: Yeah, I think now if you do forward slash MCP, it should give you the authentication.

**David Orban** [17:21:04]: Inside the inside

**Eeshita Pande** [17:21:06]: cloud though.

**Eeshita Pande** [17:21:07]: Cloud, yeah, so cloud and then forward slash MCP.

**Eeshita Pande** [17:21:24]: Yeah, and I think if you just enter, yeah, to authenticate.

**David Orban** [17:21:32]: This is another browser.

**David Orban** [17:21:45]: could be used, it could be due to the fact that the token

**Eeshita Pande** [17:21:51]: was

**David Orban** [17:21:51]: used, right?

**Eeshita Pande** [17:21:53]: Yeah,

**David Orban** [17:21:54]: yeah, yeah.

**David Orban** [17:21:54]: So, so let me, let me do it again.

**Luca Bertelli** [17:21:59]: Are you, are

**Eeshita Pande** [17:22:05]: Yeah, I think you'll also have to use the same number, which was, I think, the US number that you authenticated.

**Eeshita Pande** [17:22:11]: course.

**David Orban** [17:22:12]: Yeah.

**Luca Bertelli** [17:22:28]: By the way, you got the fabric message, the second one, I guess.

**David Orban** [17:22:38]: Yes, this is the authentication

**Eeshita Pande** [17:22:41]: one.

**Luca Bertelli** [17:23:09]: Are you doing it from inside cloud or is like a CLI common, this cloud flow?

**David Orban** [17:23:20]: Actually, it works both ways, but you know, right, I wanted to do it inside cloud.

**David Orban** [17:23:25]: Okay, okay.

**David Orban** [17:23:30]: But, aren't we?

**Luca Bertelli** [17:23:31]: Yeah, we are.

**Luca Bertelli** [17:23:32]: Yeah, yeah, yeah, yeah.

**Eeshita Pande** [17:24:28]: Cool.

**Eeshita Pande** [17:24:30]: What is the novelty scoring approach?

**Eeshita Pande** [17:24:32]: Is it something that just tells you how like, you know, new and like novel your posts are?

**David Orban** [17:24:38]: Correct.

**Eeshita Pande** [17:24:39]: Yes.

**David Orban** [17:24:43]: And it should be somewhere.

**David Orban** [17:24:44]: So the way I work is that.

**David Orban** [17:24:51]: Let's open a new window.

**David Orban** [17:24:58]: So this is my local plane.

**David Orban** [17:25:05]: And

**David Orban** [17:25:13]: it's not even novelty.

**David Orban** [17:25:20]: It should be a prompt measuring the value of new

**Eeshita Pande** [17:25:26]: ideas.

**David Orban** [17:25:31]: Yeah, it doesn't matter.

**David Orban** [17:25:32]: Not my problem, close

**Eeshita Pande** [17:25:33]: problem.

**Eeshita Pande** [17:25:34]: Yeah, close problem.

**Eeshita Pande** [17:25:37]: Did it find it?

**Eeshita Pande** [17:25:38]: Let's see, it's still on the fabric steps, but I think it found novelty scoring.

**David Orban** [17:25:42]: Yeah.

**David Orban** [17:25:42]: Yeah, I did see it found something.

**David Orban** [17:25:45]: There you go.

**David Orban** [17:25:46]: Yeah.

**David Orban** [17:25:47]: July 24. There you AI-based system using LLMs to evaluate ideas from transcripts.

**David Orban** [17:25:52]: Yeah.

**Eeshita Pande** [17:25:53]: So it essentially takes your past posts, the LLM evaluates them, gains an understanding of them, and then takes the latest posts to see how different they Yes.

**Eeshita Pande** [17:26:03]: Got it, yeah,

**David Orban** [17:26:05]: yeah.

**David Orban** [17:26:05]: And one thing that could be useful for you, I actually have a chatbot website.

**David Orban** [17:26:13]: It's based on Sensei.

**David Orban** [17:26:15]: Yeah.

**David Orban** [17:26:16]: And I don't hesitate showing you the back end.

**David Orban** [17:26:22]: because it's fine.

**David Orban** [17:26:25]: You would have the same access if you used it.

**David Orban** [17:26:29]: But the second reason because

**Eeshita Pande** [17:26:35]: They

**David Orban** [17:26:35]: are pivoting.

**David Orban** [17:26:36]: Yes.

**David Orban** [17:26:37]: So rather than now offering generic chatbots with personalization, they are targeting enterprises to have a conversation with people leaving the company that their knowledge stays with the company, right?

**David Orban** [17:26:56]: And

**Eeshita Pande** [17:26:56]: what were some of the reasons for their pivot, David?

**Eeshita Pande** [17:27:00]: Like, I would be really curious to understand.

**David Orban** [17:27:02]: They couldn't sell

**Eeshita Pande** [17:27:05]: Yeah, it just

**David Orban** [17:27:06]: like... They couldn't sell the chatbot, right?

**David Orban** [17:27:10]: And I enjoyed looking at the conversations my website visitors would have.

**David Orban** [17:27:18]: And some of them were pretty extensive.

**David Orban** [17:27:24]: And let me try to remember, because I have to remember the URL studio, there you go.

**David Orban** [17:27:36]: So this is my my

**David Orban** [17:27:43]: chatbot.

**David Orban** [17:27:47]: And I am definitely not on a free trial.

**David Orban** [17:28:05]: Maybe I cannot show it to you.

**David Orban** [17:28:11]: Yeah,

**Eeshita Pande** [17:28:11]: you see?

**Eeshita Pande** [17:28:12]: Yeah, it's actually not enough, yeah, it's

**David Orban** [17:28:15]: like March 2026.

**David Orban** [17:28:30]: All right, then I'm just showing it to

**Eeshita Pande** [17:28:32]: you.

**David Orban** [17:28:33]: Another time, another time.

**David Orban** [17:28:35]: Anyway, what I would have shown you is that I, at the time when this was created, exported all my blog posts for, don't know, like 20 years, all my tweets I don't think I gave it my Facebook data

**Eeshita Pande** [17:29:05]: and

**David Orban** [17:29:06]: then I, or actually not me directly, but they ingested and curated in some way my YouTube

**Eeshita Pande** [17:29:17]: channel

**David Orban** [17:29:20]: with all the videos and then transcribed the videos, etc.

**David Orban** [17:29:24]: So in total there were like 50 different sources of data.

**David Orban** [17:29:31]: and yeah it was pretty good in in answering in my name and

**Eeshita Pande** [17:29:39]: like yeah the in terms of like the utility to you like you you had like sensei on your website and and there weren't enough people like you that wanted to pay for like a chatbot on the website like it was that no

**David Orban** [17:29:51]: no no it so it it wasn't my problem not being able to monetize because as an advisor to sensei i got this for free right and i wonder oh okay so they killed it

**Eeshita Pande** [17:30:11]: and people

**David Orban** [17:30:13]: use it now all right so The utility to me was coming from understanding what kind of questions the people visiting would be asking because then I would progress in extracting them based on frequency and the frequency of course would be itself semantic similarity and then I would generate a human

**David Orban** [17:30:50]: curated and a human sourced answer to those questions rather than relying on the chat bot to answer only.

**Eeshita Pande** [17:31:05]: Interesting.

**Eeshita Pande** [17:31:06]: So you weren't, okay, that's quite interesting.

**Eeshita Pande** [17:31:08]: So like, yeah, for the most common, like, you know, FAQ-like topics, you would actually write a response.

**David Orban** [17:31:14]: Yes, yes, because for the moment,

**Eeshita Pande** [17:31:19]: yeah,

**David Orban** [17:31:19]: we still trust knowing myself better than ChatGPT or Claude or Fabric.

**David Orban** [17:31:30]: So it could very well be that I would refer to the answers to those questions,

**Eeshita Pande** [17:31:37]: or I

**David Orban** [17:31:37]: would look what the auto-generated answer to that particular FAQ would be.

**David Orban** [17:31:47]: However, exactly because of how important they are, because they happen frequently, is worth my time.

**David Orban** [17:31:59]: reviewing and possibly augmenting or correcting what the AI believes the right answer is.

**Eeshita Pande** [17:32:11]: Yeah, that makes a lot of sense,

**David Orban** [17:32:14]: So for example, yeah,

**David Orban** [17:32:22]: this page is not yet updated my latest role.

**David Orban** [17:32:29]: I don't know what weight this would have, but it is fair to assume that a page like this would have an outsized weight in defining what the answer of what does David do or who is David in professional life.

**David Orban** [17:32:47]: And if it is not updated, then the AI's answer is not...

**Eeshita Pande** [17:32:54]: Yeah.

**Eeshita Pande** [17:32:54]: Yeah, yeah, yeah, yeah.

**David Orban** [17:32:56]: Sorry.

**David Orban** [17:32:57]: Go ahead.

**Eeshita Pande** [17:32:57]: Go ahead.

**Eeshita Pande** [17:32:58]: I guess like, you know, what's been interesting to us is like we focused on a slightly like, you know, different and more of like a fintech-like approach here for now to begin with, because precisely, because as you're saying, right, that it's quite difficult for your digital self at this point to

**Eeshita Pande** [17:33:15]: really like understand you in a huge amount of detail at every step of the way.

**Eeshita Pande** [17:33:20]: But the reason why we wanted to like still bring together like behavioral data sources of the kind where sure you can download your data for the last X years, but you can't set up like recurring transfers like every day.

**Eeshita Pande** [17:33:33]: So you could be able to like take all the, unless you're doing the work of manually curating your digital self, it's quite difficult to like, you know, every day or every week upload this data.

**Eeshita Pande** [17:33:43]: I'm

**David Orban** [17:33:44]: listening and then we'll be talking as well, but I will brew a coffee.

**Eeshita Pande** [17:33:47]: So please.

**Eeshita Pande** [17:33:48]: Of course, of course.

**Eeshita Pande** [17:33:49]: And then I guess like the other thing that we found is that you want to like provide some utility from the very beginning.

**Eeshita Pande** [17:33:57]: So like instead of you know, just having like our own like interface.

**Eeshita Pande** [17:34:04]: Right now, we decided that actually using like, yeah, different MCP clients and injecting the understanding into the understanding that cloth or GPT or others might have a few is probably going to improve the user experience quite a lot, and especially for people who might not have quite as

**Eeshita Pande** [17:34:22]: extensive, you know, like documentation about themselves, like you know, like, who've not written many blog posts, who've not, like, made a lot of videos, and a lot of their behavior is around the big, like, tech platforms.

**David Orban** [17:34:36]: Okay, so, one

**David Orban** [17:34:42]: question from the beginning of what you said, then I will have another one, and you can tell me how long you want this to

**Eeshita Pande** [17:34:53]: last.

**David Orban** [17:34:54]: I have a pizza coming on the hour, so I will have to pick it Yeah, yeah, yeah.

**David Orban** [17:35:04]: So you said at the beginning of your remark, we take it from a FinTech point of view, and the rest of what you said had nothing to do with FinTech.

**David Orban** [17:35:16]: So one, define what that means.

**Eeshita Pande** [17:35:20]: Yes, yes, yes.

**David Orban** [17:35:21]: And connect it to me to the fact that other people have less stuff written about

**Eeshita Pande** [17:35:26]: Yes, so like the FinTech point of view here, David, is like the point of view of aggregating like data sources.

**Eeshita Pande** [17:35:32]: So, you know, you know, have companies like Plaid, Trulair, the FinTech aggregators, who essentially bring together your different bank accounts.

**Eeshita Pande** [17:35:41]: and they enable other companies to actually be able to use that data.

**Eeshita Pande** [17:35:45]: And so that's what I mean by the FinTech point of view that we collect and clean up and enrich all your data from Instagram and Google and TikTok and all these platforms.

**Eeshita Pande** [17:35:55]: So in like this universe, other companies can then use your digital self to build better products for you.

**Eeshita Pande** [17:36:02]: So does that make sense?

**David Orban** [17:36:05]: It does and it doesn't in the sense that Let me let me see or ask you first.

**David Orban** [17:36:17]: Staying on that, give me two, three examples of use cases of my data being used by third

**Eeshita Pande** [17:36:28]: parties from

**David Orban** [17:36:29]: a fintech point

**Eeshita Pande** [17:36:30]: of view.

**Eeshita Pande** [17:36:31]: Yes, so the FinTech analogy is like what I'm not saying is that your data should be used to make like better lending decisions on you.

**Eeshita Pande** [17:36:41]: Like that's not what I'm saying because also that's illegal under the Fair Lending Act.

**Eeshita Pande** [17:36:45]: What I mean by FinTech is this model of aggregating data creating an intermediary, and then having other companies build products on top of that, is fintech is the only industry where that model has actually done very well.

**Eeshita Pande** [17:36:59]: So I used to be head of monetization for a fintech company where we used PLAD to actually build a personalized chatbot on your financial data.

**Eeshita Pande** [17:37:08]: So you could ask our chatbot, like Leo, is what the chatbot was called.

**Eeshita Pande** [17:37:12]: Hey, how much can I spend while I'm going out tonight?

**Eeshita Pande** [17:37:17]: And because we had your bank transaction data through Plaid, we could give you a really good answer.

**Eeshita Pande** [17:37:22]: And same for personalized credit decisions.

**Eeshita Pande** [17:37:25]: How that approach applies to Fabric is there's tons of use cases in consumer dating, consumer social, consumer shopping, where when you first log in, the application on the other side knows nothing about you.

**Eeshita Pande** [17:37:37]: So you'll get shown like, for instance, a carousel of people to date who might not have anything in common with you.

**Eeshita Pande** [17:37:44]: But if we're able to match you based on who you are and who they are, because we've got this rich understanding of you from day one, then that's a really valuable product.

**Eeshita Pande** [17:37:53]: So the FinTech analogy applies on the aggregation and having developers building on top of that understanding and not, we're going to use this data and make better lending decisions because of

**David Orban** [17:38:05]: Okay, good, goodish.

**David Orban** [17:38:11]: Unconvinced, but let's move

**Eeshita Pande** [17:38:14]: Tell me why are you unconvinced?

**David Orban** [17:38:18]: It is a very subtle difference between being served with good products and services and being exploited and extorted.

**David Orban** [17:38:31]: Let me give you the example that I stumbled upon just today.

**David Orban** [17:38:38]: Everyone started to love Substack, after realizing that social networks didn't represent reliable and reputable relationship with their contacts.

**David Orban** [17:38:53]: And as of a couple of days ago, Substack started to send out the newsletters that they were supposed to deliver via email your paid subscribers crankated

**Eeshita Pande** [17:39:10]: so

**David Orban** [17:39:12]: that they would have to install the Substack app and read the entire newsletter on the Substack

**Eeshita Pande** [17:39:18]: app.

**David Orban** [17:39:19]: And that is the perfect example of what Corey Doctor of my friend calls and certification of the plant forms.

**Eeshita Pande** [17:39:26]: Yeah,

**David Orban** [17:39:27]: yeah.

**David Orban** [17:39:27]: So that is why I'm saying that the way you try to balance your narrative is necessary and to me unconvincing, but I am very happy to suspend my judgment.

**David Orban** [17:39:48]: The second thing that you said is obviously super important is that you need first target developers so that they can provide compelling applications that use fabric, which knowledge of people fabric provides.

**David Orban** [17:40:12]: That in turn means and you need to confirm whether this is true, that you are planning to allow users to create their tapestry for free.

**Eeshita Pande** [17:40:26]: Exactly, yeah, like we don't have any plans to charge users for their tapestry because we think ultimately if a developer is able to increase retention on their products by using fabric, then the developer should be the one who paying and not the end

**David Orban** [17:40:42]: user.

**David Orban** [17:40:43]: Perfect.

**David Orban** [17:40:47]: How much did you raise?

**Eeshita Pande** [17:40:50]: 3 million.

**David Orban** [17:40:52]: What is your current runway?

**David Orban** [17:40:53]: Oh,

**Eeshita Pande** [17:40:54]: like we barely spend anything, so like over three years at this rate.

**David Orban** [17:40:58]: Luca, come on.

**Luca Bertelli** [17:41:02]: You've

**David Orban** [17:41:02]: got to pay for those pizza or for those ramens.

**David Orban** [17:41:08]: Or... You are very well paid in equity, which is fine

**Eeshita Pande** [17:41:12]: too.

**Eeshita Pande** [17:41:12]: Yes,

**Luca Bertelli** [17:41:13]: that's

**David Orban** [17:41:14]: the case.

**David Orban** [17:41:16]: And when do you plan your next

**Eeshita Pande** [17:41:18]: race?

**Eeshita Pande** [17:41:19]: So we're thinking about it.

**Eeshita Pande** [17:41:22]: We don't have any eventual pressure right now to raise.

**Eeshita Pande** [17:41:25]: Our investors have reached out wanting to double down.

**Eeshita Pande** [17:41:28]: There's a few things that we would like to prove.

**Eeshita Pande** [17:41:31]: So we recently launched this Prozuma product and quite important to prove is how well we actually understand the user and what use cases are users finding utility.

**Eeshita Pande** [17:41:42]: So a lot of the beta experiments that we're running are around, okay, like use fabric inside Claude or GPT to come up with like a gift list for yourself, or use fabric to generate this wrap of yourself.

**Eeshita Pande** [17:41:55]: And the idea there if we actually create this amazing understanding of you from four or five data sources, and by the way, that's the other point that I wanted to like also touch on, you said that social data doesn't reflect your relationships in as much detail, that's correct, but when you combine

**Eeshita Pande** [17:42:12]: social

**David Orban** [17:42:12]: data No, I didn't say no, no, I said it is not dependable.

**David Orban** [17:42:17]: Yeah.

**David Orban** [17:42:18]: Meaning that social networks can change their mind and you lose the connection you have with your network.

**Eeshita Pande** [17:42:29]: Okay, okay, got it, got it.

**Eeshita Pande** [17:42:31]: I

**David Orban** [17:42:31]: thought, I thought, I thought... No, no.

**David Orban** [17:42:33]: I believe that, you know, the... paranoid conviction of people that their phone listens to them from exactly the fact that Facebook knows you much better than you know yourself,

**Eeshita Pande** [17:42:48]: absolutely.

**Eeshita Pande** [17:42:49]: Yeah, and you know, so if you see the kind of data, so the posts and stories is one Facebook like integration we have, the other one is interactions which we also get on a recurring basis.

**Eeshita Pande** [17:42:58]: So there we get everything that like, you know, all the pixels that Facebook drops all over the internet, we get all that data about you.

**Eeshita Pande** [17:43:07]: So we can see your purchases.

**Eeshita Pande** [17:43:08]: Like, you know, for instance, if I buy something from a website that has a Facebook pixel, we can see that purchase in the interactions data, the likes, the comments, the follows, your social graph, like all of that.

**Eeshita Pande** [17:43:19]: In fact, even your messages, even though we're not getting a lot of that data, because we don't know how to process it yet.

**Eeshita Pande** [17:43:24]: But the idea there on the milestones to show that with four or five data sources, we can create such a rich understanding of you that when you plug this into applications like GPT and Claude, the responses that you get are incredibly rich and just on a level that's just not comparable with the

**Eeshita Pande** [17:43:42]: single platform understanding.

**Eeshita Pande** [17:43:44]: And that would enable us to raise more.

**Eeshita Pande** [17:43:48]: So we're considering raising this coming year, even though we don't need to.

**Eeshita Pande** [17:43:53]: But depending on how that understanding piece goes, we're doing a hackathon along with one of our partners like Google in March to like get some developers to build cool products on top of us.

**Eeshita Pande** [17:44:04]: So based on those two like, you know, almost like areas which are really all using the user understanding, I'll make a decision on whether to raise in 2026 or a little later.

**David Orban** [17:44:15]: Whatever it is going to be, VCs are going to be spooked either by the circular deals between Nvidia and LLM's hyperscalers and

**Eeshita Pande** [17:44:33]: data

**David Orban** [17:44:35]: center building being stuck.

**David Orban** [17:44:40]: And the likely reason for that is that there will be substantial delays due to labor shortages And the market will misinterpret that saying, oh, data centers are not in demand anymore or whatever.

**David Orban** [17:44:57]: Or there will be technological breakthroughs that allow frontier LLMs to be trained a tenth or a hundredth of the energy than before, and VCs don't understand Jensen's paradox or Jensen's laws, I prefer to call it, that demand will expand much more than the efficiency reduction would reduce the

**David Orban** [17:45:34]: supply need a given level of demand, or some geopolitical effect because the US onshore in chip production actually makes a Chinese invasion of Taiwan more likely.

**Eeshita Pande** [17:45:56]: you think like US will not be as incentivized

**David Orban** [17:46:01]: to defend Taiwan?

**David Orban** [17:46:03]: The US will wash their hands of Taiwan and say are, defend deescalation and we defend the world against World War III and there's a consequence we don't intervene.

**David Orban** [17:46:20]: Why, while in reality the reason they don't intervene because TSMC has a production plant in Texas or whatever.

**Eeshita Pande** [17:46:31]: But like, I mean, I don't know if that's, you know, I guess, like some of the estimates on when China will make a move on Taiwan are like 2027. That's not fast enough for enough like onshore US like chip production.

**David Orban** [17:46:48]: Correct.

**David Orban** [17:46:49]: And China can push it back a year, right?

**David Orban** [17:46:52]: It matter.

**Eeshita Pande** [17:46:55]: We both one way

**David Orban** [17:46:57]: or another.

**David Orban** [17:46:58]: Because China wants the US not to intervene

**Eeshita Pande** [17:47:01]: too.

**Eeshita Pande** [17:47:02]: Yes.

**David Orban** [17:47:03]: The proud refusal of accepting HB200s shows that they believe Huawei will be on parity with with NVIDIA next

**Eeshita Pande** [17:47:20]: year.

**David Orban** [17:47:21]: And I believe that too.

**David Orban** [17:47:24]: As a matter of fact, I spoke to Alibaba just last week with regards to their presence in the

**Eeshita Pande** [17:47:35]: UAE,

**David Orban** [17:47:36]: which used to be a Huawei stronghold, and the US came and said, sorry, do you mind kicking them out and taking NVIDIA instead?

**David Orban** [17:47:46]: But when customers will clamor for Huawei, because it is now better tokens per jowl than Nvidia next year, G42, which is the leading data center or Equinix even, that is hosting hyperscalers, we'll have to ask themselves, okay, can we afford not to serve our

**Eeshita Pande** [17:48:13]: customers?

**Eeshita Pande** [17:48:15]: Anyway,

**David Orban** [17:48:16]: Back the point.

**David Orban** [17:48:17]: Back to the point.

**Eeshita Pande** [17:48:18]: We spoke one way or another.

**David Orban** [17:48:20]: He should raise when money is plentiful.

**David Orban** [17:48:24]: Yes.

**David Orban** [17:48:25]: And then have a stronger war chest being able to cross the trough of disillusionment where startups that don't get to run, they die.

**Eeshita Pande** [17:48:40]: It's a good, it's a very good point.

**Eeshita Pande** [17:48:43]: Some of our, like, yeah, we season advisors are making this point as well, that probably middle of next year is the most we should push in terms of raising, at the very least, another few million.

**Eeshita Pande** [17:48:55]: But if things go well, probably a much larger round.

**Eeshita Pande** [17:48:59]: And the idea is that, you know, you actually, there will be, it's not like whether there will be a recession, it's like when there will be a recession.

**Eeshita Pande** [17:49:07]: It

**David Orban** [17:49:07]: is natural, it cannot not be, but it is just the question of timing it well and playing the cards the best possible.

**David Orban** [17:49:14]: And

**Eeshita Pande** [17:49:14]: you want to be, you know, you want to be, I guess it's like good because then it's a buyer's market for hiring, and so you want to be well capitalized, you want to have a war chest, and you want to hire lots and lots of amazing engineers, and keep building while the rest of the world is going

**Eeshita Pande** [17:49:32]: through the recession.

**David Orban** [17:49:34]: Yes, absolutely.

**David Orban** [17:49:35]: Okay, so do you have an API available yet?

**Eeshita Pande** [17:49:40]: Luca.

**Luca Bertelli** [17:49:41]: Yeah, so we have, let's say, a proto version of an API in the sense that you cannot ask Fabric like you do via MCP, but you can read the memories and the threads that you saw on the dashboard.

**Luca Bertelli** [17:50:00]: So basically the same endpoints that you uh query that you the user portal queries when you load them and you see

**David Orban** [17:50:09]: so obviously i didn't see the mcp manifest and the tool set that the mcp has and i am not able to judge how much of of an effort the developer has to do now in order to have feature parity with the MCP.

**Eeshita Pande** [17:50:26]: It's a good question.

**Eeshita Pande** [17:50:28]: And I guess like what we found is, especially with like most larger companies that we worked with in the past, that actually the raw data, they're not able to make sense of it.

**Eeshita Pande** [17:50:40]: There's a lot of work to be done in going from like raw data to this digital self, which is the work that we're doing.

**Eeshita Pande** [17:50:46]: And over time, the goal is to expose the digital self through the API as well.

**Eeshita Pande** [17:50:51]: But for now, because we're working directly with end users and taking a lot of feedback on how good the digital self should be, if we give a version to developers and then change it completely, that really messes up their applications as well.

**Eeshita Pande** [17:51:04]: So we've got a bunch of early developers who are happy to start working with like threads, which is the raw data.

**Eeshita Pande** [17:51:11]: And our thinking is we work together and we learn on what they do with threads and we use

**David Orban** [17:51:17]: that.

**David Orban** [17:51:17]: But let me stop you and in a few minutes I have to Do you believe that you are talking to end users rather than an extremely narrow set people who are able to go through the onboarding the way I did faster or slower, doesn't matter, but they are still absolutely geeky and nerdy rather than normal

**David Orban** [17:51:46]: people.

**Eeshita Pande** [17:51:47]: So it's a very good question.

**Eeshita Pande** [17:51:49]: So, you know, like the prosumers for sure are like you, but like we've like actually on board at thousands of people who are not prosumers, who are end users, and they're able to navigate.

**Eeshita Pande** [17:51:59]: And I've been on like a lot of user interviews where people have navigated this journey.

**Eeshita Pande** [17:52:04]: And it's not been difficult for them.

**Eeshita Pande** [17:52:07]: I was like

**David Orban** [17:52:07]: really... instead of what I did.

**Eeshita Pande** [17:52:12]: Yes, not the, so the MCP side is different.

**Eeshita Pande** [17:52:17]: So actually, and adding the MCP encode, for instance, and GPT is pretty straightforward for most people.

**Eeshita Pande** [17:52:25]: So they click from the user portal in the open encode.

**Eeshita Pande** [17:52:29]: the URL is there.

**Eeshita Pande** [17:52:31]: I was also very surprised, actually.

**Eeshita Pande** [17:52:33]: Because most of them don't even know what MCPs are.

**Eeshita Pande** [17:52:37]: And then they just click and they're like, oh, here's a link.

**Eeshita Pande** [17:52:39]: I'll put the link.

**Eeshita Pande** [17:52:40]: Sometimes they call fabric like something weird, but most of the time they don't.

**Eeshita Pande** [17:52:45]: It consistently

**David Orban** [17:52:48]: surprised me.

**David Orban** [17:52:49]: I'm very happy to hear that, but I would still caution you to believe that you are talking to a representative sample of human behavior don't know, Facebook experiences it through their 3

**Eeshita Pande** [17:53:10]: billion users.

**Eeshita Pande** [17:53:11]: Yes, for sure, for sure.

**Eeshita Pande** [17:53:12]: And I think like, you know, the early set of adopters can be prosumers, they don't need to be developers, they just need be like some people who understand like some version of technology.

**Eeshita Pande** [17:53:23]: that they're using like GPT, they're using maybe clothes.

**Eeshita Pande** [17:53:28]: And so I think that like usually ends being enough for them to understand what it means doing a consent flow and bringing that understanding to cloud.

**Eeshita Pande** [17:53:37]: But I was like you, I was also surprised.

**Eeshita Pande** [17:53:40]: We even did last year, we were working with a bunch of fashion brands in bringing the data to fashion brands.

**Eeshita Pande** [17:53:46]: And so there I did a lot of user interviews and there were also older people who like had no idea of, you know, like they didn't, they were not technical at all.

**Eeshita Pande** [17:53:56]: And they just like clicked, they just kept clicking through and to the point where got quite worried and I was like, oh, hey, like what do you think is actually going on here?

**Eeshita Pande** [17:54:03]: Like, what are you doing?

**Eeshita Pande** [17:54:05]: And they're like, oh, like, you know, Google has all my data and now Fabric will have all my data and I'm getting 10 pounds for it.

**Eeshita Pande** [17:54:11]: So I'm like really happy because Google doesn't give me anything.

**Eeshita Pande** [17:54:14]: So it's, It's really not that big a hurdle.

**Eeshita Pande** [17:54:18]: And when we were raising, a lot of our investors were also questioning this assumption that what percent of people will actually convert into sharing their data.

**Eeshita Pande** [17:54:27]: And I'd worked a lot in open banking in increasing the conversion rates of our funnel.

**Eeshita Pande** [17:54:31]: So I was like, we started in open banking with 3 to 5%, which is a difficult flow.

**Eeshita Pande** [17:54:37]: And then we got it to like over 90%.

**Eeshita Pande** [17:54:40]: So we'll probably see single digits conversion rates at the beginning, and that's fine.

**Eeshita Pande** [17:54:44]: But in some experiments, we saw like 40% conversion rates.

**Eeshita Pande** [17:54:48]: And these were all statistically significant results, like done with samples of 15,000 people.

**Eeshita Pande** [17:54:54]: So it's kind of, it was very surprising to me.

**Eeshita Pande** [17:54:57]: But I'm going to take that as a win.

**Eeshita Pande** [17:55:00]: And it just worked.

**David Orban** [17:55:04]: OK. So, yeah, just to show this is what Claude came up with, interplanetary AI, law and legal personhood, jolting technologies, all right, whatever it good.

**David Orban** [17:55:25]: And then, given my realization quite a few years ago that platforms broke the promise of the internet to allow interoperability.

**Eeshita Pande** [17:55:41]: Yes.

**David Orban** [17:55:42]: The worst in this is Instagram where even text is not selectable,

**Eeshita Pande** [17:55:49]: where you

**David Orban** [17:55:50]: cannot write, click on images to

**Eeshita Pande** [17:55:52]: save.

**Eeshita Pande** [17:55:52]: They

**David Orban** [17:55:53]: are just the

**Eeshita Pande** [17:55:54]: worst.

**Eeshita Pande** [17:55:55]: Yeah.

**David Orban** [17:55:55]: But but even the quotation marks better ones

**Eeshita Pande** [17:56:00]: with

**David Orban** [17:56:02]: X that truncates the URLs with three dots at the end so you cannot copy the whole tweet knowing that what you get is usable.

**David Orban** [17:56:14]: I ended post posting 100% of what create.

**David Orban** [17:56:23]: Okay, okay.

**David Orban** [17:56:26]: So just to show you today, I posted this newsletter on Substack and,

**David Orban** [17:56:45]: you know, short with a couple of of of images and the same on LinkedIn as an article and the same is on X again as an article and so on and so forth in about 15 different platforms yeah yeah and you know from more visible to to more exotic So weird

**Eeshita Pande** [17:57:23]: threads.

**David Orban** [17:57:26]: Yeah.

**Eeshita Pande** [17:57:27]: So I guess like, so where it gets interesting actually is you could, so the integrations that we have, right, we get the data from threads.

**Eeshita Pande** [17:57:37]: I mean, we're not processing it yet, but we have threads, we have LinkedIn, we have Instagram.

**Eeshita Pande** [17:57:43]: And the idea is actually, in principle, you could post on one, we pull that data, and then you have an agent that reposts for

**David Orban** [17:57:54]: you.

**David Orban** [17:57:54]: Well, that would be that would be amazing and extremely valuable if you had a map of the at tags

**Eeshita Pande** [17:58:05]: of

**David Orban** [17:58:07]: one person to the other to the same person on the other

**Eeshita Pande** [17:58:11]: platform.

**Eeshita Pande** [17:58:12]: Yes,

**David Orban** [17:58:13]: I am at David Orban

**Eeshita Pande** [17:58:14]: everywhere because

**David Orban** [17:58:17]: I'm an early adopter and everyone else called David Orban most of the time cannot grab the same handle, but even I sometimes come late.

**David Orban** [17:58:31]: So TikTok, I am what is the queue?

**David Orban** [17:58:35]: What is the question?

**David Orban** [17:58:36]: What is the

**Eeshita Pande** [17:58:37]: queue?

**Eeshita Pande** [17:58:37]: Yeah,

**David Orban** [17:58:38]: yeah.

**David Orban** [17:58:38]: So if I use your agent, it would have to understand what is my tech here or

**Eeshita Pande** [17:58:44]: right?

**Eeshita Pande** [17:58:44]: Because you opt in with us, anything that you connect is your account.

**Eeshita Pande** [17:58:50]: So it wouldn't be like if it's what is the queue, but you've

**David Orban** [17:58:53]: actually... Yeah, yeah, yeah, but I'm not talking about myself.

**David Orban** [17:58:56]: Let's say that I'll post something that we had a conversation and I'm tagging you.

**David Orban** [17:59:01]: Yes, yeah.

**David Orban** [17:59:02]: So then you would have to breach the Chinese wall.

**David Orban** [17:59:05]: Yes.

**David Orban** [17:59:06]: Between my tapestry and your tapestry in order for that understanding to translate in the

**Eeshita Pande** [17:59:12]: post.

**Eeshita Pande** [17:59:12]: 100%, 100%, 100%.

**Eeshita Pande** [17:59:14]: Like that's without a question.

**Eeshita Pande** [17:59:16]: And over time, like, you know, we will on board like a billion people and then like we will have all of their accounts and that will be a solvable problem.

**David Orban** [17:59:25]: But for now.

**David Orban** [17:59:26]: And then I will finish with this.

**David Orban** [17:59:29]: All of us must have at least probably more.

**David Orban** [17:59:34]: alteregos because there are secret behaviors that are by definition illegal until they become majority that all of us experiment with and that is the reason privacy matters because that is the way society evolves and only if our digital projections are allowed to refine our understanding of those

**David Orban** [18:00:03]: illegal behaviors that we can transfer this evolution in the digital realm as well, oh, realm, that's another word that chat GPT ruined for me, in the digital realm.

**David Orban** [18:00:18]: And so your platform can only be embraced wholeheartedly if you can ride this and manage this very, very, very delicate situation.

**David Orban** [18:00:39]: Yeah, yeah.

**David Orban** [18:00:39]: And I being of course provocative, but how can you exist in Nigeria if this behavior that you

**Eeshita Pande** [18:00:54]: support

**David Orban** [18:00:57]: is homosexuality which is prohibited in Nigeria.

**Eeshita Pande** [18:01:02]: Yeah,

**David Orban** [18:01:03]: yeah, yeah, yeah.

**David Orban** [18:01:04]: Or posting on social media in the UK things that are jailable

**Eeshita Pande** [18:01:09]: offence because that's someone.

**Eeshita Pande** [18:01:11]: I mean that

**David Orban** [18:01:12]: is very worth.

**David Orban** [18:01:13]: So anyway, gotta go get a pizza and thank you for the chat and for helping me on board and I'm looking forward to following how the platform evolves and giving you more feedback as that was done.

**Luca Bertelli** [18:01:29]: Thank you so much, David.

**Luca Bertelli** [18:01:30]: Amazing.

**David Orban** [18:01:31]: Thank you.

**Eeshita Pande** [18:01:32]: Bye.

**Eeshita Pande** [18:01:32]: Thanks.

---
*Backed up from MeetGeek on 2026-03-30 08:50*
