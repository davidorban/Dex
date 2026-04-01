# Sjors / David Sync

**Date:** 2025-09-04
**Duration:** Unknown
**Meeting ID:** a6850ee4-720f-4f66-96ad-d2b8893a429b

## Participants
- *Participants not listed*

### Summary

The meeting focused on several key areas, including the challenges of generating synthetic data with AI tools, where participants identified the need for improved prompts and data retrieval methods. Sjors was tasked with exploring the MCP for scraping capabilities, while David committed to analyzing statistical data and creating 3D visualizations post-URL scanning. Discussions also covered the rising demand for AI tokens, with David projecting a significant increase in consumption, alongside concerns about budget implications due to escalating token costs. The meeting addressed organizational structure changes, office access issues, and tax residency implications for David's potential move to Dubai. Additionally, accommodation arrangements for upcoming visits to Abu Dhabi were discussed, and tasks were assigned to ensure smooth transitions and communication with investors regarding ongoing deals. Meeting logistics were also coordinated, with David confirming his availability and the meeting location.

## Full Transcript

**Unknown speaker** [12:01:00]: It's

**Unknown speaker** [12:01:05]: interesting because the fact that it can be prompted to be in a certain way.

**Unknown speaker** [12:01:15]: So for example, if you say provide a critical review of whatever document, It will behave more skeptical, it will be more cautious in its judgment than not if you just say, hey, analyze this document for me and then it will potentially be more gung-ho, more eager to please, etc.

**Unknown speaker** [12:01:47]: As well as it will attempt things and when doesn't work, It can come up with reasons not to do it rather than do it.

**Sjors Bogers** [12:02:02]: Like in my case, design synthetic data and then say, okay, this is what it would look like if I did it, but since I couldn't, here's the synthetic data and then blah, blah, blah.

**David Orban** [12:02:21]: And then you say, no, that's really not what I wanted, and it apologizes.

**David Orban** [12:02:26]: But in both cases, as of right now, and this is not necessarily gonna be the case in three months, six months, who knows how fast, it is not able to go one level above and say, should I even bother generating synthetic data?

**David Orban** [12:02:47]: Will that be useful?

**David Orban** [12:02:48]: Or is the intent behind this analysis to tell the user that they are incredible or is the intent behind the analysis to alert the user about the weaknesses of the document, right?

**David Orban** [12:03:09]: So until it is able to do that, it is our job to just go that extra step and make sure that the prompts are either providing that priming to start with or do two different, produce two different results and then compare them with another prompt still.

**Sjors Bogers** [12:03:44]: Yeah, I was trying as well.

**Sjors Bogers** [12:03:45]: I did four iterations over two sessions because I constantly get choked, right?

**Sjors Bogers** [12:03:51]: Yeah.

**Sjors Bogers** [12:03:53]: So the first time I had the same issue, it came up with a fake table.

**Sjors Bogers** [12:03:56]: And then I think in the second run, I got it to actually go into the website and Yeah, click one of the businesses and I tried to do only tests with the first three companies because if I would set it up to do 200 at once it would fail straight away.

**Sjors Bogers** [12:04:16]: So, and then on the second attempt, it opened the first drop down because it's automatically opened once you click So I got there and then on the third attempt I got it to copy that section and then I actually got for one of the companies the good data and then it tried for the second and the third

**Sjors Bogers** [12:04:33]: and it got nothing because it asked me early on if I can't find it out should I just say not disclosed or not available so all the sales at NA and ANA and And then I copy that back into it said, oh yeah, of course that's stupid.

**Sjors Bogers** [12:04:49]: Let me try again and then it even forgot the first data it got.

**Sjors Bogers** [12:04:56]: Then I did a little more digging and I found another MCP that's specifically built for scraping.

**Sjors Bogers** [12:05:05]: And I saw it on a YouTube video and was working well and even can do captures and things like that.

**Sjors Bogers** [12:05:12]: But I couldn't test it because it was a paid thing, so you need to set up the API key.

**Sjors Bogers** [12:05:19]: But I have a link, so maybe if you want to give it a shot.

**Sjors Bogers** [12:05:23]: Then I thought, as it was showing me the browser actions.

**Sjors Bogers** [12:05:30]: I saw it go to the website.

**Sjors Bogers** [12:05:31]: I saw it open the first company on the right open data section.

**Sjors Bogers** [12:05:37]: Then it clicked it, it went to the drop down and then it sort of stopped.

**Sjors Bogers** [12:05:40]: So then I trained it by doing it manually myself with Describe.

**Sjors Bogers** [12:05:45]: And then it actually worked because it started opening the drop downs.

**Sjors Bogers** [12:05:50]: So I got it to train to that level.

**Sjors Bogers** [12:05:53]: But it still didn't take the screenshot and put the data in a CSV file, not even once.

**Sjors Bogers** [12:06:01]: But the AI told me there's a cut off after two minutes because it's like a prevention to not have runaway activities that it just goes crazy for hours on something that may or may not work.

**Sjors Bogers** [12:06:13]: I didn't manage to turn off that two minute cut You did or did not manage to do that, but that was mainly because I was choked myself, so I was trying and then I got, I ran into the wall again.

**Sjors Bogers** [12:06:28]: So maybe that's something you can look at, or can look at.

**Sjors Bogers** [12:06:34]: Yeah, I think it was pretty interesting that with a scribe, which are pretty easy to make, you can show them how human would go about it, and then it actually picks up on that.

**Sjors Bogers** [12:06:44]: It's a bit of a weird loop, but It was very good.

**Sjors Bogers** [12:06:50]: good.

**David Orban** [12:06:53]: So, I used to hate infographics.

**David Orban** [12:07:00]: And I still hate them.

**David Orban** [12:07:02]: But at least now I know why they exist.

**David Orban** [12:07:07]: And you would think that infographic exists because they are entertaining or that they illustrate with a better visualization, some topic that otherwise would be possible.

**David Orban** [12:07:26]: And that is true.

**David Orban** [12:07:29]: But the real reason infographics have a role is because at least until yesterday, they demonstrated human effort.

**David Orban** [12:07:41]: That someone took the efforts to not only collect the data, but also to think of how many hamburgers per unit should be stacked one on top of each other or whatever bullshit decision in how the data should be killed.

**David Orban** [12:08:08]: Because one of the main reasons why I don't like infographics is because very pristine dynamic data is just squished and smashed so that nothing can be extracted from it, right?

**David Orban** [12:08:25]: Except what the designer believes should be your impression, hence the hamburgers.

**David Orban** [12:08:33]: And I was thinking that... We are in this absurd situation, which is caused by the fact that we are in the middle of a transformation, where websites are still mostly designed for humans, and then we are forcing AI to behave as humans would, clicking here, clicking there, taking screenshots, running

**David Orban** [12:09:09]: OCR on a screenshot, while the underlying data is already machine readable, and so it should be so easy.

**David Orban** [12:09:21]: And I'm sure it will be because already some people are realizing and acting on the fact that in the big scheme of things, statistically speaking, people visiting websites will be a vanishingly small number.

**David Orban** [12:09:43]: Then a little bit larger percentage, but not too much will be search engines, and 99.9% will be AI agents.

**David Orban** [12:09:53]: And so what already was an important

**David Orban** [12:10:01]: focus search engine optimization is now rapidly turning into AI agent optimization of the websites, both in terms of discovery, but also in terms of

**David Orban** [12:10:32]: Inspired by that, I of course knew what the way to overcome this is.

**David Orban** [12:10:44]: Because the reason why we use the agent to click and OCR and stuff is because we believe we are not able to write a scraper.

**David Orban** [12:10:57]: That's not true.

**David Orban** [12:11:00]: We can write a scraper that will grab the HTML and then traverse and interpret the HTML source of the page.

**David Orban** [12:11:12]: And so that is what I did with the lucky component that the pages of ESCA are all sharing the same URL schema.

**David Orban** [12:11:32]: And even if the progression of the numbers is not exactly sequential, they belong to a range.

**David Orban** [12:11:45]: So it is in the process of finishing as we speak, after testing a bit the process It is now systematically scanning all the URLs from 0000 to 3,000. Yeah, all right.

**David Orban** [12:12:05]: So, and it takes time, but it is ignoring the error messages that it is getting like we saw yesterday.

**David Orban** [12:12:16]: It's saving the HTML, the full HTML without worrying about interpreting it for each of the pages that exist, and then I already have tested and it's ready, the simple, well, I don't know if it is simple, it was simple for me to say, just do how the HTML has to be parsed so that all the company data

**David Orban** [12:12:46]: is then put in a CSV in a single line.

**David Orban** [12:12:50]: And I already started asking, OK, what are the analyses, statistically, that you can draw from the types of licenses, and then how it could be charted.

**David Orban** [12:13:07]: And I didn't do it yet, so it doesn't know.

**David Orban** [12:13:12]: But I will ask to create 3JS, which is a 3D JavaScript library.

**David Orban** [12:13:21]: visualization where I can see kind of a point cloud and turn it around in different axes and I know how to represent at least four dimensions because three is normal and then the fourth, actually five, the fourth dimension can be the size of the balls.

**David Orban** [12:13:46]: And the fifth dimension can be represented by a spectrum of colors.

**David Orban** [12:13:54]: And then you can do hyper transformations.

**David Orban** [12:13:57]: So if you sort by whatever dimension the colors could be all over the place.

**David Orban** [12:14:05]: But then if you sort by the dimension of the colors, then you have maybe, you know, red in the middle and then yellow and green and blue, whatever the sequence.

**David Orban** [12:14:21]: And then you see different

**David Orban** [12:14:28]: aggregations forming naturally.

**David Orban** [12:14:33]: Yeah.

**David Orban** [12:14:34]: So that is what I'm planning to do a little bit this afternoon after the download of all the attempts, failing and succeeding finishes.

**David Orban** [12:14:46]: So the lesson that we can take advantage of the bridge that the coding ability represents between the agent and our goal, as long as we understand that they can behave differently from how humans would behave and we don't force them to be human if they don't need to.

**Sjors Bogers** [12:15:18]: But I assume you you got this idea because you already knew that this could be done, right?

**Sjors Bogers** [12:15:25]: It's not that the AI suggested another solution that then put you on this track, right?

**Sjors Bogers** [12:15:30]: You came with the input.

**David Orban** [12:15:32]: So I don't remember, but it could have very well have been that way, even if it didn't happen this time around.

**David Orban** [12:15:38]: It could be.

**David Orban** [12:15:40]: So actually the opposite happens to me as well, where have a straightforward solution in mind, and the AI designs an entire framework and thousands of lines of code because it can, and by the time I bring my attention back to it, it is so deep in that hole, and then I can say, sorry, wonderful, but

**David Orban** [12:16:13]: not needed, you can do it like this.

**David Orban** [12:16:18]: So, so coming to that conclusion on my side this time around, whatever it was, is not unique.

**David Orban** [12:16:26]: Other people can realize this is a possibility, as long as they are not living in that condition of learned helplessness that too many people have, and they enjoy the little friction that vibe coding still represents

**David Orban** [12:16:57]: Yeah.

**Sjors Bogers** [12:16:58]: For me was a little bit the other way around because it starts creating a scraper and kept failing and then I told it to use a MCP to control the browser and then it started going down that path.

**Multiple speakers** [12:17:09]: Perfect, perfect.

**David Orban** [12:17:11]: And the plurality of approaches that we can test is itself an advantage.

**David Orban** [12:17:17]: For example, what you learned will be extremely useful when you also discover what is called a puppeteer and playwright that are two libraries where programmatically you can test a website that you designed and run locally or in the remote server too i think only locally where you can tell the ai to

**David Orban** [12:17:52]: design the tests that will hopefully prove that the various pieces of functionality in the website are what you wanted.

**David Orban** [12:18:05]: And that is, I don't think it is done using OCR, but then that is the additional approach.

**Sjors Bogers** [12:18:16]: What does OCR stand for?

**Sjors Bogers** [12:18:19]: What does OCR stand for?

**David Orban** [12:18:21]: optical character recognition, the way that a screenshot can be interpreted, right?

**David Orban** [12:18:27]: You take the screenshot and then you say, okay, I don't know what's on it, you extract the written parts.

**David Orban** [12:18:35]: Yeah.

**David Orban** [12:18:44]: And by the way, I have no idea the You can you can now paste a screenshot in cloud code.

**David Orban** [12:18:55]: And I don't know.

**David Orban** [12:18:58]: Because recognizes the screenshot content in real time, and I don't know how it does And it is certainly not OCR.

**Multiple speakers** [12:19:11]: I use that term that is out of the 80s because that is what I would do but now it is certainly not optical and it is not only characters it's it recognizes everything yeah I noticed that And I don't know if it's because of my plan or part of my prompting style or whatever, but very often it just

**Sjors Bogers** [12:19:43]: stops what it was stops remembering what it was doing before goes down its own rabbit So he comes up with an idea and then he forgets what what he was working on before and then even though I bring that back into the memory like reference with the full starting prompt it still focuses mainly on the

**Sjors Bogers** [12:20:06]: on the second part of the last part of the assignment basically very well.

**David Orban** [12:20:19]: You can overcome that by either

**David Orban** [12:20:30]: building or providing or generating a thorough plan and then literally the plan will have to do that the system will check off and it knows that it has to stick to And the way, so, um, code dev.net or code guy, code guide.dev, you remember is, is one way to do that, but it's overkill.

**David Orban** [12:21:06]: Um, and the simplest way to do that is to use cloud flow, you haven't yet, right?

**Sjors Bogers** [12:21:15]: That's what the agents, you mean, Yes.

**David Orban** [12:21:18]: Well, because author of Claude Flow believes that inspired by him, and we don't know and probably not, but Claude itself now incorporates agents.

**David Orban** [12:21:35]: So it is not enough to say agents because it could be one or the other.

**David Orban** [12:21:42]: But yes, cloud flow is what you install specifically and separately, downloading it or I showed you, I think, the GitHub repository of the guy in Toronto, I think I used a few times, but the main issue for me is that it, it shuts me down really fast.

**David Orban** [12:22:09]: Yeah, because that is hungry for tokens.

**Sjors Bogers** [12:22:13]: Yeah, so whenever I use it within five, 10 minutes, I hit my wall.

**David Orban** [12:22:21]: That's terrible.

**David Orban** [12:22:23]: That is how it might feel to, and apologies for the comparison, to be poor.

**David Orban** [12:22:32]: Right?

**David Orban** [12:22:32]: When you see, I don't know, you are walking on a street and there's beautiful, sweet display of desserts behind a glass and you don't have the money to buy them and you would love a piece of cake.

**David Orban** [12:22:56]: And it's... It is, I think, a very, very good counter- argument to those that say that we are about to see the AI boom deflating, because there is an incredible pent-up demand for more and more tokens.

**David Orban** [12:23:23]: one thing you can do is to run CC usage.

**David Orban** [12:23:28]: in your terminal.

**David Orban** [12:23:30]: And you can see a gift track, And you can see for the past 30 days, how many tokens you used in what way?

**David Orban** [12:23:40]: How many tokens were cached, for example, which costs less and things like And what that?

**Multiple speakers** [12:23:50]: CC usage.

**David Orban** [12:23:54]: You need to download it first, it's not a built--in command, of course.

**David Orban** [12:23:59]: And, um, and, um, I am not, not every month or, or, or, you know, it shows you a 30-day trailing window.

**David Orban** [12:24:13]: So my 30-day trailing window is not always at peak, uh, depending, you know, if I am distracted and I don't have, uh, the model just doing things all the time, then it is not.

**David Orban** [12:24:31]: But when I keep it intensively working, I get up to a billion tokens a month.

**David Orban** [12:24:41]: A billion tokens.

**David Orban** [12:24:42]: And you know, there just no limit.

**David Orban** [12:24:46]: I think I told you I I have two big repositories, right?

**David Orban** [12:24:54]: One today.

**David Orban** [12:24:55]: One is tag and the other is my personal stuff.

**David Orban** [12:25:03]: And on both, periodically run a prompt that says, look at all the repository and all the files and create a plan what are the things that I could be doing in order to maximize the value that this repository represents, not monetary value, but what are the things that I should be doing.

**David Orban** [12:25:30]: And since that is kind of a, itself a generative process and a constructive process.

**David Orban** [12:25:43]: There's no end.

**David Orban** [12:25:44]: There's no moment in time that one should say, I can't think of nothing more.

**David Orban** [12:25:52]: That there's always, you can, you can always think of more.

**David Orban** [12:25:54]: So, uh, I, I draw two conclusions from this.

**David Orban** [12:26:02]: One, that.

**David Orban** [12:26:09]: I will be surprised if in a year's time I will not be consuming a trillion tokens per month rather than a billion.

**David Orban** [12:26:21]: And two, and I'm afraid, but I know it's true that when Claude or OpenAI will come out with their next tier, And OpenAI already confirmed.

**David Orban** [12:26:40]: They are gonna release a $2,000 per month tier.

**David Orban** [12:26:46]: I will subscribe it.

**Sjors Bogers** [12:26:49]: Yeah, but of course, if you look at the value you get, it's still on the price, right?

**David Orban** [12:26:53]: Yeah, that's exactly the point.

**David Orban** [12:26:56]: It will be logical, sounds absurd today.

**David Orban** [12:27:03]: You know, just like it would sound absurd a year ago that I would subscribe happily to $200 a Same thing.

**Sjors Bogers** [12:27:12]: I wouldn't be surprised if they make a $200,000 monthly grant.

**David Orban** [12:27:21]: Absolutely, absolutely.

**David Orban** [12:27:23]: And I am really eager to further analyze where the disconnect is on the side of the naysayers, those that almost with giddy expectation are prophesizing the burst of the bubble.

**David Orban** [12:27:49]: Why?

**David Orban** [12:27:50]: What are they happy about when their...

**David Orban** [12:27:58]: doom scenario comes through why why why would that one good and and why don't they see that it's

**Multiple speakers** [12:28:19]: that that so many indicators point in the other direction Yeah, what you said before about feeling poor.

**Sjors Bogers** [12:28:30]: It feels more like you see in the movie Limitless, where they and you do.

**Sjors Bogers** [12:28:35]: Yeah, it feels like you run out of the medicine, right?

**Multiple speakers** [12:28:39]: Very, very, very good, very good.

**Sjors Bogers** [12:28:41]: All the people I can't afford it, they blowing up their... Yeah, yeah, and it is frighteningly on point.

**David Orban** [12:28:54]: because these superpowers create that an absolute degree of dependency.

**David Orban** [12:29:10]: Have you seen the movie Transcendence?

**Sjors Bogers** [12:29:13]: It's a pretty old one, Fuck Well, just to figure out when I saw it.

**Sjors Bogers** [12:29:21]: I heard of it.

**David Orban** [12:29:22]: It's maybe 10 years old or 15 years old.

**David Orban** [12:29:25]: Oh, I thought it was old.

**Sjors Bogers** [12:29:27]: Yeah, pretty sure I saw it.

**David Orban** [12:29:28]: Johnny Depp.

**David Orban** [12:29:31]: And he's the famous one.

**David Orban** [12:29:35]: I mean, I'm sure all the other actors are famous in their own way, but the star is Johnny Depp.

**David Orban** [12:29:43]: and he dies at the beginning of the movie except that he's uploaded and it wasn't very well received and the chemistry between the actors is a bit flaky unfortunately that doesn't help but there are some smart things in that movie and the uploaded Johnny Depp character becomes very ambitious and

**David Orban** [12:30:26]: superhuman, not only in the software but in the hardware as well.

**David Orban** [12:30:34]: He manipulates nanotech and this and that and so And in order for the world to save itself, They do something I didn't remember exactly what, that basically stops the use of electricity all over the world.

**David Orban** [12:30:55]: And they retreat in a pre-industrial society, still remembering how good it was when they could use electricity, And the movie ends with zooming on a droplet of water on a leaf.

**David Orban** [12:31:31]: And I don't know if, I don't remember if there is some other hint and how much I am jumping to that conclusion only.

**David Orban** [12:31:38]: But I believe that zooming represents the... confirmation that the superintelligence is only hiding and biding its time.

**David Orban** [12:31:52]: They didn't really eliminate it.

**David Orban** [12:31:55]: It is still there in the droplet of water.

**David Orban** [12:31:59]: And the feeling that these characters project when they look at some non-functioning piece of equipment longingly, is what we feel when the AI is not there anymore, and we have to make do without that superpower that it gives us.

**Sjors Bogers** [12:32:28]: Yeah, I think it wasn't the news maybe a month or two months ago, but some sort of deal with open AI and Dubai that they would give all Dubai citizens access for free to open AI.

**Multiple speakers** [12:32:41]: Is that actually happening So you heard about it?

**David Orban** [12:32:45]: It was not only Dubai, but all of the UAE.

**David Orban** [12:32:50]: Okay.

**David Orban** [12:32:50]: And when it happened, I wanted to go check.

**David Orban** [12:33:02]: But there is no trace of it having been agreed.

**David Orban** [12:33:11]: Maybe they discussed A journalist picked up on but there is no official trace.

**David Orban** [12:33:20]: There has been a newer which was a little more corroborated and a little more believable because it was an article about a discussion that Sam Altman had with, I don't remember which minister in where the minister said Altman offered to give free access to chat GPT to all the UK residents.

**David Orban** [12:34:00]: Yeah.

**David Orban** [12:34:00]: So evidently this is happening.

**David Orban** [12:34:04]: And

**David Orban** [12:34:12]: It will be impossible to resist, you know.

**David Orban** [12:34:15]: Already in India, they introduced the cheap plus version, $5 rather than And I don't think it's radical enough.

**David Orban** [12:34:32]: Two would have been better, you a 90% discount more attractive.

**David Orban** [12:34:41]: And it is fascinating that they still are also hungry for data.

**David Orban** [12:34:50]: They are hungry for our queries.

**David Orban** [12:34:54]: Very, very interesting.

**Sjors Bogers** [12:34:56]: We all know the next step, right?

**Sjors Bogers** [12:34:57]: They provide a cheap and they hike the prices.

**Sjors Bogers** [12:35:01]: Once everyone's addicted.

**Sjors Bogers** [12:35:04]: They may.

**David Orban** [12:35:08]: The analogy with Microsoft is perfect where Microsoft tolerated the the piracy of Windows and Office for 10 years and then introduced the license keys and ever more stringent ways to get paid.

**David Orban** [12:35:33]: And that can be a given outcome, but No, not necessarily.

**Sjors Bogers** [12:35:47]: Looking at TEG and budget-wise, are they taking it into account already, the token expenditure, that it might rise exponentially?

**David Orban** [12:36:02]: the reason I can afford to spend, sorry, to spend, to use a billion tokens month is because the cost per token has come down exponentially, right?

**David Orban** [12:36:17]: So, yes, I did put in the budget, um, for my resources.

**David Orban** [12:36:26]: Uh, you, you, you remember, I told you $500 per month of AI tools on top of everything else.

**David Orban** [12:36:37]: And I hope.

**David Orban** [12:36:39]: they will understand that it is not only worth it, but it is worth to give the same budget to everyone.

**David Orban** [12:36:52]: And then whether that amount goes up because of the prediction of the irresistibility of the $2,000 per month tier, it's a good question because Yeah, it's real money, multiplying $2,000 by 50, that's $100,000 a month.

**David Orban** [12:37:12]: Yeah, right there.

**David Orban** [12:37:18]: And imagine how exciting to be able to say, well, still worth

**David Orban** [12:37:29]: So we had a meeting with Randy and Shaheen.

**David Orban** [12:37:36]: Randy is the head of advisory and Shahin works with him and they have been for the past two three weeks doing AI experiments and they very happy very excited and we agreed on certain next steps Shahin is smart you will enjoy working with very very and

**David Orban** [12:38:05]: they did a fantastic choice to pick a client with whom they just started and say, okay, with this particular client, we will do everything using AI.

**David Orban** [12:38:22]: So, um, starting as simply as, uh, recording the discovery meetings, the initial ones, and then, generating slide decks and analyzing or creating financial models and so on.

**David Orban** [12:38:45]: And my request to them, apart from offering, of course, to help all the way and course correct or, or, you know, do whatever, my request was to make the effort of asking themselves and then documenting

**David Orban** [12:39:08]: what it would have been time and the resources needed they didn't use Because that will be important indicator for us.

**Sjors Bogers** [12:39:22]: And what is so special about these clients?

**Sjors Bogers** [12:39:25]: Is it an AI company or it you don't know?

**David Orban** [12:39:29]: Oh, no, no, no.

**David Orban** [12:39:29]: The reason they picked it is because it's just the last one to sign, the latest one to sign.

**David Orban** [12:39:36]: So if the others already started, and they wouldn't have represented an entire arch with these, they are just starting now.

**David Orban** [12:39:57]: Okay.

**David Orban** [12:39:57]: Yeah.

**David Orban** [12:40:02]: You still have access to Slack, right?

**David Orban** [12:40:04]: Yeah.

**Sjors Bogers** [12:40:07]: I still have full access to everything.

**David Orban** [12:40:12]: Yeah.

**David Orban** [12:40:13]: Could you please make

**David Orban** [12:40:21]: a backup of the learning channel and the tools channel where I posted stuff?

**David Orban** [12:40:34]: Okay.

**David Orban** [12:40:34]: You have to figure out how to make the backup Well, even, you know, just you go at the beginning and then you copy and paste, something as simple as Because in, in, well, maybe in the, no, I don't think I attached files or documents, I just posted text and links, I think.

**David Orban** [12:41:04]: And whatever else you believe is worth safekeeping There's no specific way to export it, If you are an admin, but I don't know if you I don't think am.

**Sjors Bogers** [12:41:20]: Yeah.

**Sjors Bogers** [12:41:24]: Okay, I'll look it.

**David Orban** [12:41:26]: Okay, what else?

**David Orban** [12:41:45]: We had a meeting with a Dutch architectural firm ZJK.

**Sjors Bogers** [12:41:55]: Doesn't ring about, right?

**David Orban** [12:41:58]: That does a lot of work in the UAE, sports stadiums and other stuff.

**David Orban** [12:42:08]: And they spoke about parametricism.

**David Orban** [12:42:12]: which is the Zaha Hadid approach that Patrick Schumacher, the guy we talked to, formalized.

**David Orban** [12:42:24]: And I didn't bring him up in this meeting, but I did ask if they believe that these tools that they are using AI should democratize the aesthetic qualities that now are isolated in these small number of buildings and would be possible to live in houses that as creative and different.

**David Orban** [12:42:58]: And he

**David Orban** [12:43:06]: said that they are concentrating on these because housing is boring, and then as he said he realized that housing is boring because they are not bringing parametricism to housing, but he didn't want to go there, because he said, oh, but housing is such that it is affordable because it is

**David Orban** [12:43:38]: standardized, But then, of course, it's natural that standardization is necessary only if you don't have the AI tools.

**Sjors Bogers** [12:43:50]: Yeah, the, there's this, the biggest real estate platform in the Netherlands is called Finda.

**Sjors Bogers** [12:43:58]: And only enlisted realtors can use it.

**Sjors Bogers** [12:44:02]: So you have to be part of association, which was pretty locked And they've been capturing a lot of data, of course.

**Sjors Bogers** [12:44:10]: it's no surprise that everybody's looking at chateaus and castles and mansions, but they don't have the budget And then they end up buying in a row house in the street.

**Sjors Bogers** [12:44:20]: So then looking at the data, they said, okay, what's the average house people end up with and what do they actually search for before start buying And they combined And I don't think it was very solid done on data, but more like, oh, people like something big and they end up buying something They

**Sjors Bogers** [12:44:40]: put those two together, and in the space of an in-a-row house, they design something really amazing, but for the same budget, as boring in a row house and then they pretty sure it's still online i'm trying to find it but have to look for what it's called and then they have this side by side so you

**Sjors Bogers** [12:44:57]: see the typical three floor in a row building and one that's yeah it looks much more grand because they break out the the ceiling between the first and the second floor so in the living room you have five meter ceiling and you have doors to the garden that are also four meters high so it feels like

**Sjors Bogers** [12:45:20]: a castle door opening even though your background is really small still but it's very spacious and then a lot of it is moved to the sides so all the shelving the kitchen is sort of built into the wall so you create a lot of space And then they still have the same amount of rooms, albeit a little

**Sjors Bogers** [12:45:38]: smaller to make room for the space and the spacious feeling.

**Sjors Bogers** [12:45:42]: But also the bed is built into the wall and the bathroom.

**Sjors Bogers** [12:45:47]: It feels like a spa because it's just the bath is the floor and it can fill 40 centimeters up.

**Sjors Bogers** [12:45:53]: So you just walk into the bathroom and you turn on the bath or the shower, it just fills up.

**Sjors Bogers** [12:45:58]: It's really amazing.

**Sjors Bogers** [12:46:00]: I don't, I think the plan was always to actually build it as a test house, but I don't think they ever got And maybe with all the price increases, it got more expensive now.

**Sjors Bogers** [12:46:10]: Perfect, perfect.

**David Orban** [12:46:11]: That is exactly the approach that I imagine would be possible.

**David Orban** [12:46:18]: Perfect.

**David Orban** [12:46:19]: If you can find it, I will enjoy Yeah.

**Sjors Bogers** [12:46:26]: Well, what was the reason an architectural firm talks to tech?

**David Orban** [12:46:31]: Because they want to expand in the Middle East No, they are already there, but the only one, we have to get accustomed to the new name, right?

**David Orban** [12:46:45]: The only one wealth management clients,

**David Orban** [12:46:57]: either directly or together with the government or because they are the government, finance, huge real estate construction.

**David Orban** [12:47:09]: Okay.

**David Orban** [12:47:09]: You know, last time we were on the beach and we were looking at the skyscraper and we're counting that each of them is like a billion.

**David Orban** [12:47:19]: Yeah.

**David Orban** [12:47:19]: Well, Zayat has 150 of them.

**David Orban** [12:47:21]: Okay.

**David Orban** [12:47:31]: And in particular this firm also is very much around sustainability and a reduction of CO2 footprints.

**David Orban** [12:47:48]: So it is good that Aldi 1 has this sensibility.

**David Orban** [12:47:55]: You know, and then whatever the meeting brings, it wasn't oriented towards particular deal, it was just to get to know each other Yeah.

**Sjors Bogers** [12:48:16]: Yeah.

**David Orban** [12:48:16]: And who is then in a meeting like besides So it was organized by the CMO, Alice, and... There were Luke and Shaheen and Jad, who was also online, and Hayko,

**David Orban** [12:48:46]: who just joined recently, he's head of products, he's one of the people who's activities were described to me two days ago and I understood nothing.

**Sjors Bogers** [12:48:58]: Yeah.

**Sjors Bogers** [12:48:59]: yeah.

**David Orban** [12:49:02]: So yeah, there were maybe 10 people in the meeting room plus three online.

**David Orban** [12:49:13]: For about an hour of meeting.

**David Orban** [12:49:16]: Yeah, no, it was good.

**David Orban** [12:49:21]: Tomorrow is a holiday in the UAE.

**Sjors Bogers** [12:49:24]: Okay, which

**Sjors Bogers** [12:49:32]: I actually created the holiday calendar.

**David Orban** [12:49:36]: So I can look up.

**Sjors Bogers** [12:49:41]: But they don't stick to that holiday calendar, I assume, right?

**Sjors Bogers** [12:49:45]: With everybody being distributed?

**David Orban** [12:49:48]: I don't know.

**David Orban** [12:49:54]: I'm sure the emirates like what's her amira stick to so here is the here is the calendar and I did a version that lists all the offices, right?

**David Orban** [12:50:19]: So what is the holiday in the various places?

**David Orban** [12:50:25]: And so here we are, September, not listed.

**David Orban** [12:50:35]: Interesting, okay, this is already a mistake.

**David Orban** [12:50:40]: As a consequence, I also because all of the Islamic holidays are fluctuating because they are not only linked to the moon but they are linked to the moon sighting so they are expected to be in a given place or around a given set of days but exactly when it is gonna is established by the Islamic

**David Orban** [12:51:19]: Council and then communicated so funny that this is not that it is the Prophet's birthday just googled oh it is so rather than then here yeah it should be on the fifth not the 15th Perfect.

**David Orban** [12:51:38]: So this is the mistake.

**David Orban** [12:51:40]: Okay.

**David Orban** [12:51:40]: And it's not Monday, but Friday.

**David Orban** [12:51:44]: Yep.

**Sjors Bogers** [12:51:45]: All So it's Islam at Christmas basically.

**David Orban** [12:51:51]: Yeah, that's correct.

**David Orban** [12:51:54]: Exactly.

**David Orban** [12:52:05]: And then I also updated received from Amira a spreadsheet with with the people, but I didn't like It's very, very, well, it doesn't matter.

**David Orban** [12:52:27]: So I did my own version.

**David Orban** [12:52:31]: And I calculated via AI automatically what country from the city.

**David Orban** [12:52:36]: And I standardized the phone with dashes, again with AI, you know, just with the equals AI function.

**David Orban** [12:52:46]: You know that, Yeah, very And, and now trying to understand comparing old org chart that is also in the repository and it's old because it has this key person, chief of staff, that resigned slash was fired within two months.

**David Orban** [12:53:23]: Okay.

**David Orban** [12:53:23]: Maybe And a lot This happened, I don't know, in March or whenever.

**David Orban** [12:53:31]: So, unfortunately, a lot of things depended on him, and we were counting on him being able to do And he hasn't been replaced yet with a new hire.

**David Orban** [12:53:43]: So, I am trying to adapt whatever that Orchard says to what is the reality today.

**David Orban** [12:54:00]: So, for example, head of operations should be reporting to the head count

**David Orban** [12:54:11]: now

**David Orban** [12:54:16]: is 42, 41.

**Sjors Bogers** [12:54:24]: had a question that I would like to ask when we It's a bit of a silly question, I'm not sure if it's appropriate.

**Sjors Bogers** [12:54:35]: But I would like to know if the office is available to end for Oh, so answer

**David Orban** [12:54:48]: certainly seven.

**David Orban** [12:54:52]: And... I did arrive when reception and the bar and everything was empty early enough, you know, quarter to eight and there is security.

**David Orban** [12:55:11]: So I am pretty sure that the security gate is, there's people there all the time.

**David Orban** [12:55:20]: And then the the The tag LD1 office has its own card.

**David Orban** [12:55:30]: So maybe even if the glass door closed until 6 o'clock in the morning, with your card, you can click it open, tap it Yeah, good question.

**David Orban** [12:55:50]: Because of your habit of working 2 a.m. or something.

**Sjors Bogers** [12:55:54]: Yeah, and if I feel on the Sunday that I want to get some work done and especially in the beginning, I don't know what the living situation would look like.

**Sjors Bogers** [12:56:02]: If it's shared, I can imagine more peaceful to just walk in on a Sunday, right?

**Sjors Bogers** [12:56:10]: Or at night after going to the gym or whatever when I feel working.

**David Orban** [12:56:13]: Yeah, I think it's not inappropriate you should Okay.

**Sjors Bogers** [12:56:27]: Would you say gate outside, but you can enter from the bottom, right?

**David Orban** [12:56:35]: The escalator coming up from the underground.

**David Orban** [12:56:41]: arrives to a corridor.

**David Orban** [12:56:45]: The security is along that corridor.

**David Orban** [12:56:50]: And they they have their marble desk.

**David Orban** [12:56:58]: and they are looking at the elevator shaft and and before you get to the elevators there is you know there is an electronic entrance so I don't have a badge yet they told me that if I want it they can give it to me but I said I don't care because I just stop at the security they register me and You

**David Orban** [12:57:27]: don't need to be a list.

**David Orban** [12:57:33]: You just say where you go, they give you your But without a badge, you cannot enter the elevator.

**Sjors Bogers** [12:57:44]: Do you know what the workspaces itself look like?

**Multiple speakers** [12:57:47]: I saw few pictures somewhere in the... I sent you a few pictures, Yeah, yeah.

**Sjors Bogers** [12:57:55]: So I think it was a few offices and meeting rooms, and in the middle, they had these cubicles, right?

**David Orban** [12:58:01]: Open spaces, yes.

**David Orban** [12:58:05]: And you you can be anywhere.

**David Orban** [12:58:10]: Now, We are in the process of securing new offices.

**David Orban** [12:58:19]: So the one that you saw is on the 25th floor.

**David Orban** [12:58:25]: And we rented new ones in the fourth.

**David Orban** [12:58:33]: And then we are talking about other buildings And whenever that comes I immediately tell listen, as soon as we are on different floors and in different buildings, it's as if we were remote.

**David Orban** [12:58:51]: So please get into the mindset remote work.

**Sjors Bogers** [12:58:57]: Yeah.

**Multiple speakers** [12:58:58]: Do they choose to do this due to space limitations Yeah, because the current one co-working space And so there are multiple, black rock is there, for example.

**David Orban** [12:59:14]: Nice.

**David Orban** [12:59:14]: Not bad neighbor.

**David Orban** [12:59:15]: Yeah.

**David Orban** [12:59:18]: Can we have that?

**David Orban** [12:59:21]: Together not?

**David Orban** [12:59:22]: You're Aliwan has its own...

**David Orban** [12:59:32]: let's say the main office of Aliwan is secured with its door that the badge opens.

**David Orban** [12:59:43]: And the fact that the badge also allows you to come when the main glass door of the whole floor is closed.

**David Orban** [12:59:54]: I'm not sure that is true.

**David Orban** [12:59:55]: I would think logical, but I don't So the badge opens the main door of the Aliwan offices, and as you get there let's say, six desks, All of the desks the ones that you can also, like mine, you go up and down, standing desk style and things like Is it six, one, two, three, four, five, six, seven,

**David Orban** [13:00:29]: eight, maybe more eight like six, not six.

**David Orban** [13:00:32]: And then there is another glass office that is Michael's.

**David Orban** [13:00:39]: So in that area, nine people can work at the same time.

**David Orban** [13:00:47]: But then everyone is always in meetings, and as soon as you have a meeting, you take one of the meeting rooms.

**David Orban** [13:00:55]: There there's a board room level meeting room with up to, I don't know, 15 people.

**David Orban** [13:01:04]: There's a smaller one for six people, more than And then there are those where two people can be very comfortable meeting.

**David Orban** [13:01:13]: And four a bit, know, stuffed in as sardines, but, uh, they are very good because full ventilation AC and a nice desk.

**David Orban** [13:01:27]: Um, when people have a call with someone on the outside, they go in one of those small Do you have an office space dedicated If you do a... mean, I've only been there once, And when went, I was there for a a bit and just picked the desk and no one kicked me off.

**David Orban** [13:02:08]: So every day I arrive, I would typically be the first, I put backpack, computer and everyone else arriving would pick another it.

**David Orban** [13:02:23]: It, some of the desks were evidently inhabited, you know, by little trinkets or whatever that people would leave there.

**David Orban** [13:02:31]: So I didn't pick one of those signs that is why I had no, I didn't even ask, I just that.

**Multiple speakers** [13:02:41]: Yeah, it was the same when I worked for Phillips.

**Sjors Bogers** [13:02:44]: Everybody had open seating, but people still ended up sitting at same spot most of time.

**Sjors Bogers** [13:02:49]: Uh-huh.

**David Orban** [13:02:51]: Uh-huh.

**Multiple speakers** [13:02:52]: But they also probably 40% more seats than people.

**Sjors Bogers** [13:02:57]: So it's easy to sit with other people if you want to work them for week.

**Sjors Bogers** [13:03:02]: Yeah.

**Sjors Bogers** [13:03:04]: But do you don't have the screen set up you want as well, or you just do everything on your

**David Orban** [13:03:15]: I didn't see anyone with an extra screen, And I also only use the laptop.

**David Orban** [13:03:31]: Tag and the team is really not technologically advanced.

**David Orban** [13:03:42]: And they, I am sure, associate multiple screens with Bloomberg.

**David Orban** [13:03:51]: Why do you want multiple screens?

**David Orban** [13:03:53]: Oh, because I am a trader on Bloomberg terminals.

**David Orban** [13:03:58]: And, but yeah, we can definitely popularize the benefit of having multiple screens for knowledge workers in That is Because for me, it's a productivity benefit.

**Sjors Bogers** [13:04:15]: Sometimes I work in my bedroom and I have a it, 32 or 42 old TV that use.

**Sjors Bogers** [13:04:26]: So much easier, okay, just put four screens on that thing and so much easier to to find the stuff you're working on, because right now I'm working 50 different tabs in different browser profiles.

**Sjors Bogers** [13:04:39]: Just alone finding where I had the tap It's, uh, yeah, probably cost me an hour week.

**Sjors Bogers** [13:04:47]: Yep.

**David Orban** [13:04:48]: Yeah.

**David Orban** [13:04:55]: Hmm.

**David Orban** [13:04:55]: So much so much of what I do is now beckoning the terminal.

**David Orban** [13:05:02]: You know, just character based and I maybe will, go over to jot down idea that will become a prompt.

**David Orban** [13:05:17]: And as I work on it and refine it, go over to Claude and then back.

**David Orban** [13:05:24]: But yeah, I like multiple monitors nonetheless.

**Sjors Bogers** [13:05:31]: I forgot the name of the brand and I'm sure others do it too.

**Sjors Bogers** [13:05:35]: And maybe there's a digital version it.

**Sjors Bogers** [13:05:37]: And they make this really cool mechanical keyboards.

**Sjors Bogers** [13:05:39]: And I think more expensive ones are almost 800 or 900 dollars.

**Sjors Bogers** [13:05:44]: But they have these quick key setups that you can use.

**Sjors Bogers** [13:05:49]: So you tap it basically like control C, but then you make a list of things you often use.

**Sjors Bogers** [13:05:57]: Right.

**Sjors Bogers** [13:05:58]: With haptic feedback basically.

**Sjors Bogers** [13:06:02]: And I can imagine if you start using prompts very often, that's very helpful, right, to have these quick setups.

**Multiple speakers** [13:06:08]: And they also have the mini version, and that's, you can take out the buttons for different programs you I actually have one of those, because with Emil, when we were doing we would use it for controlling OBS for streaming.

**David Orban** [13:06:32]: So same absolutely same When Apple came out with the light I knew it wouldn't work because they mistook the advantage of programmability without realizing that... it came with the cost of giving up muscle So you would always have to glance at the light bar and then position your finger somewhere,

**David Orban** [13:07:16]: and each application would have a different place you put your and that cognitive overhead took away any positive of the experience.

**Sjors Bogers** [13:07:31]: Yeah, that's actually the same with car design, right?

**Sjors Bogers** [13:07:33]: the four or five years, there's a lot of screens in cars now and people hate it, and now they're bringing back all the physical buttons.

**Sjors Bogers** [13:07:53]: How often do you think you will be in Abu Every quarter.

**David Orban** [13:08:01]: About a week, 10 days per month.

**Sjors Bogers** [13:08:04]: Okay, quite lot.

**Sjors Bogers** [13:08:09]: But so far you have been only once, It was August.

**Multiple speakers** [13:08:14]: Oh, yeah, I thought it was long, Yeah, I was, I was 10 days in August, now I'm going 10 days in September.

**David Orban** [13:08:21]: I already have the dates in October, at least I know I need to be there October 23. There's an event where we will soft launch the new brand, only And then I will go November and then December and January, I may go, but it will be timed let me be in Sydney from December 15 to January 15. That is,

**David Orban** [13:09:03]: that is the current plan.

**David Orban** [13:09:04]: And, um,

**David Orban** [13:09:13]: The next challenge is that I want to talk to Michael about the new agreement and how we should structure it and the bonuses and equity and whatever else I think I mentioned you.

**David Orban** [13:09:28]: But if they insist and it's okay, that it has to be with me as a natural person, Then it looks like the only way I can avoid paying taxes in Italy is to be Dubai tax resident.

**David Orban** [13:09:53]: Which for Dubai is not a big deal and it doesn't require too much being But you have to be outside of Italy for 100 and basically 200 days Yeah, it's the same with Dutch rules.

**Sjors Bogers** [13:10:09]: It's half year plus day.

**David Orban** [13:10:11]: And neither I nor probably my wife would have a problem being elsewhere.

**David Orban** [13:10:22]: The problem, it's a good problem to have is my because she needs me, so... I would have to see how to do that and and I know it's just it's just too high tax, come on, it's so high.

**David Orban** [13:10:50]: 40, 50% it's crazy.

**David Orban** [13:10:54]: Crazy.

**Sjors Bogers** [13:10:56]: I don't know how it works if you would fly to fly into Switzerland, for And then take the car to Italy, because with your passport, you enter Europe, and they think you're in Switzerland, and you can still spend a little bit more days in Italy, Oh, Oh, that's interesting.

**Sjors Bogers** [13:11:20]: You can cheat a little, but you have to make sure you, yeah, in the Netherlands at least, even if you're past that half a year plus you also look at your relationships.

**Sjors Bogers** [13:11:30]: If they look at your bank account, your mobile And if there's enough reasons to indicate that you still have your social life in the Netherlands, you can still be liable for taxes Yeah.

**David Orban** [13:11:43]: And share it for So the way it works in Italy is that if you you are suspected of flaunting the rules, practically there's no way that you can prove they are wrong exactly because of the same mechanisms, right?

**David Orban** [13:12:18]: then your lawyer goes to them and they make and and typically those are very good deals.

**David Orban** [13:12:31]: Just to confirm, when COVID even before joining

**David Orban** [13:12:48]: beyond, was earning whatever amount of money, declaring then planning to pay taxes.

**David Orban** [13:12:57]: And when COVID came, I froze everything.

**Sjors Bogers** [13:13:00]: Yeah, you told me at the time.

**Sjors Bogers** [13:13:02]: Including the taxes.

**David Orban** [13:13:04]: And so the taxman came and said, what the And I said, So they gave me a plan, a payment And it is amazing.

**David Orban** [13:13:14]: like... I seven years or ten years at one, two percent of interest per So I told myself, I took the and turns out, wasn't able to buy Bitcoin instead, because of not getting paid by beyond, but that was the thinking, delaying the payment of... of the taxes while benefiting from the appreciation of

**David Orban** [13:13:48]: Bitcoin is perfect.

**Sjors Bogers** [13:13:52]: Oh, yeah.

**Sjors Bogers** [13:13:53]: I'm joking, of course, but if it doesn't work out with the taxes, maybe I should get a place in Bergamo that and you fly to Switzerland to it.

**Sjors Bogers** [13:14:01]: You get a place for me in Amsterdam, I fly to Belgium and then up, and then we can fix like that.

**Sjors Bogers** [13:14:10]: Very complicated,

**David Orban** [13:14:16]: Let's earn it earn enough to make it worth exactly.

**Sjors Bogers** [13:14:21]: Right?

**David Orban** [13:14:22]: it is complicated enough that to spare 50 or 100K in taxes is not really it.

**David Orban** [13:14:30]: But if we spare a million, then it's Yeah.

**Sjors Bogers** [13:14:35]: if you go to Abu Dhabi, do you stay in hotels again, not enough experience.

**David Orban** [13:14:45]: First time And now the second time, is not in the is another but still a hotel.

**David Orban** [13:14:56]: And Randy told me very attached to a residence.

**David Orban** [13:15:05]: And so next time in October, will still tell Michael, this is when I'm coming, please pay for the flight and the hotel.

**David Orban** [13:15:17]: And I expect sooner or later he will say, let's find a different arrangement.

**David Orban** [13:15:23]: And how soon?

**David Orban** [13:15:30]: How depends on a lot of factors.

**David Orban** [13:15:34]: Because in my agreement, actually it spells out that they have to pay for everything.

**David Orban** [13:15:40]: But, Randy you can stay with me, I'm fine Because Randy already told me, I sent you the photos of his apartment as it is, yeah.

**David Orban** [13:15:54]: And right now, Luke and Ivan are sharing that with him, each their zone.

**David Orban** [13:16:05]: But both Luke and Ivan are planning to get their so that will be available.

**David Orban** [13:16:12]: Randy is going to keep it.

**David Orban** [13:16:14]: And he said that if I want to stay have my zone, then that is fine Okay.

**Sjors Bogers** [13:16:24]: Yeah, I was looking around a bit at real estate.

**Sjors Bogers** [13:16:26]: I have been in Dubai for quite time, but yeah, I'm not that familiar with Abu Dhabi, course.

**Sjors Bogers** [13:16:33]: But think that you have the W hotel, but then the W residences, and they have some really nice places that building.

**Sjors Bogers** [13:16:43]: And that comes with extra benefits if you want to have guests They get discounts on the additional hotel and I think even the guests, the normal residents have breakfast things there well.

**Sjors Bogers** [13:16:58]: And I think it's 950 meters from the ceiling tower, where the office is, Or even less, like 500 meters.

**Multiple speakers** [13:17:09]: So maybe that's a good option And how much was rent?

**Sjors Bogers** [13:17:16]: I don't remember if I saw one or two bedroom and it was to but then I for 600,000 and then the mortgage would around 2.5, 3,000

**Sjors Bogers** [13:17:34]: I'm not sure if it was a one two, but if it's a two, it's very easy to split, right?

**Sjors Bogers** [13:17:40]: And it's much cheaper than having hotel

**David Orban** [13:17:52]: So Randy's apartment is in the World Trade Center.

**David Orban** [13:17:57]: Okay.

**David Orban** [13:17:57]: Abu Dhabi World Trade Center.

**David Orban** [13:17:59]: You can up.

**Sjors Bogers** [13:18:02]: Do you know what they pay roughly?

**Sjors Bogers** [13:18:04]: Those guys that sharing?

**Sjors Bogers** [13:18:08]: Okay.

**Multiple speakers** [13:18:09]: Maybe 800 a month Oh, that's

**David Orban** [13:18:21]: All right.

**David Orban** [13:18:22]: So there's going to be something to look at and maybe we could share something don't you know whether me or someone I already discussed this with Randy and he's sure that there will be opportunity for that.

**Sjors Bogers** [13:18:42]: Yeah, I'm not worried about the beginning.

**Sjors Bogers** [13:18:44]: It's more like when the budget to settle down in my How to optimize that as well, right, but that's something for later okay.

**David Orban** [13:18:59]: So, don't worry about, you know, whatever you do between Friday and the weekend, of but if you want to do something, Look at the NA10 that we have been talking about for a long time and I said I would pay for it if you need use the paid version and then just come an example workflow that you believe

**David Orban** [13:19:27]: can be Okay.

**Sjors Bogers** [13:19:31]: I don't know if I have time for this because I really want to focus on closing egg fry beyond stuff.

**Sjors Bogers** [13:19:37]: Okay, no I spoke to Brad about yesterday and again confirmed that I really want to start handing it off So I'm to make it.

**David Orban** [13:19:48]: But you were, oh no, today would be the weekly, and you are not planning to go to the I am going to are?

**Sjors Bogers** [13:19:56]: Yeah, but that's probably the And I discussed with Brad that I would make an overview of all the tasks that I have been involved with and then assign names it.

**Sjors Bogers** [13:20:07]: potential people who could take it over now we're gonna discuss it and make sure and Brad still tries to keep me around and keep the door open but I keep pushing back and saying no really leaving and oddly enough you came up well because he worried that since now you're litigating Um, he wanted me

**Sjors Bogers** [13:20:34]: to ask with Georgey if she was still posting on, because then she wants to be technically be working for action here, and then if something went wrong, then turn that into a problem, I didn't yeah, react to it, I just said, sure, I can check and I checked and on Instagram at the last post is from

**Sjors Bogers** [13:20:58]: May last year, I think, So I probably won't even ask George.

**Sjors Bogers** [13:21:05]: yeah, Yeah, there's no activity.

**Sjors Bogers** [13:21:09]: I was thinking of saying, well, it's his daughter.

**Sjors Bogers** [13:21:11]: I don't think he wants to get his daughter in trouble, Yeah.

**David Orban** [13:21:18]: And Brad didn't Not, at least not yet.

**David Orban** [13:21:23]: August hasn't been paid.

**David Orban** [13:21:24]: Okay.

**Multiple speakers** [13:21:27]: has that happened that Yeah, quite Yeah, it happens with Isaac.

**David Orban** [13:21:34]: So I told Jordan, don't worry, because she sends the invoice, and then if in two, three days, money doesn't she writes back.

**David Orban** [13:21:46]: So she did, and answered, Monday was a bank holiday, which means nothing, It's Thursday.

**David Orban** [13:21:55]: Because it's now Thursday.

**Sjors Bogers** [13:21:57]: But, but yeah, it's just that doing other It's him doing all the stuff he puts a lot of stuff on his credit cards, right, on his personal credit cards, and every now and then that switches, maybe it get maxed out or I don't know But all our services right now refusing to be auto-renewed, so

**Sjors Bogers** [13:22:21]: everybody gets the update on top of their inbox that G-suite will cancel by the end the month.

**Sjors Bogers** [13:22:30]: And there was another one.

**Sjors Bogers** [13:22:31]: I didn't remember it right now.

**Sjors Bogers** [13:22:33]: With a lot of service use that, I think, Canva Slack, not sure.

**Sjors Bogers** [13:22:42]: So he probably has to renew his card again, uh, and that's he also said that again, I asked about payment and how we saw that and that there were a few outstanding things from, uh, from and he said, Yeah, of course, like I said before, I'm willing to make you whole.

**Sjors Bogers** [13:23:05]: That's also always my intention.

**Sjors Bogers** [13:23:06]: Again, it's not going to put it writing.

**Sjors Bogers** [13:23:10]: But he said, with the math of the months, you're actually owed 165, if we round it up to 180 or something, I'm sure we capture everything.

**Sjors Bogers** [13:23:22]: So he wasn't being generous like that.

**David Orban** [13:23:26]: With virtual money.

**David Orban** [13:23:28]: Yeah, monopoly Yeah.

**Sjors Bogers** [13:23:32]: But yeah, It's probably going to take a few months, if not years, to But yeah, the only thing that worries me a little bit now if I'm going to work with you, then his mood turns all together, it is what Yeah.

**Sjors Bogers** [13:23:50]: I'll just work a little harder to make up for the last.

**Sjors Bogers** [13:23:52]: That's right.

**David Orban** [13:23:53]: right.

**David Orban** [13:23:54]: Exactly.

**Sjors Bogers** [13:23:58]: yeah, I always had this feeling and it's not that I discuss it with Brad.

**Sjors Bogers** [13:24:02]: Your name doesn't even come up if he mentioned it, like I told you before, I will never But I still think it's worth you try and reach out because I got the impression for him, he will never reach out to unless the lawyer is taken out Yes, and And I know how you want to play it, I still think might

**Multiple speakers** [13:24:28]: worth trying to have a one-on-one, but that might harm the legal process Thank you for making the recommendation, and I have no problem doing so see.

**Sjors Bogers** [13:24:48]: And maybe if you travel more often, then it's even better to do it in person like Well, as a matter of fact, I will be in Dubai.

**Sjors Bogers** [13:24:56]: exactly.

**David Orban** [13:24:57]: In 10 days or so two And I have free tickets to the event if he wants to come.

**Sjors Bogers** [13:25:08]: And Brad is not in Dubai yet.

**Sjors Bogers** [13:25:10]: He's still LA.

**Sjors Bogers** [13:25:11]: Nadine and the kids went back last

**Sjors Bogers** [13:25:18]: The way I understood it is that it's still indefinite because he really wants to take care of things and make sure one of the things finalized.

**Sjors Bogers** [13:25:27]: So I wouldn't be surprised if he's still there for another four weeks or something like that.

**Multiple speakers** [13:25:34]: But didn't you say that he wants to the solar slash Equify investor guy in That's what he said last week on but that guy is constantly on the move.

**Sjors Bogers** [13:25:48]: So he's in South America, then he's in the Middle East, now he's in Asia I don't know, maybe the plan is to meet them in Vegas and to get a flight to Dubai, I

**David Orban** [13:26:05]: Yeah, the calculation weird

**David Orban** [13:26:14]: Now thinks that he hold the hand of the guy while he's pushing the buttons to send the and that doing that will be effective and if he's right that should happen anywhere in could not only should could happen anywhere in but the guy is ready to and wherever that is the flight is back to LA to meet

**David Orban** [13:26:50]: So being in LA while he's not meeting the investor is not actually I think there is other, there is some other factor involved Yeah, but that's not the only thing why he's in right?

**Sjors Bogers** [13:27:06]: He's also trying to set up that OTC deal.

**Sjors Bogers** [13:27:10]: Yeah, but that is also not happening No, and he explained it a little bit yesterday, if you're interested, otherwise we was very weird what he brought up and he also realized that it's very odd, but normally everybody has to pay for an OTC service, Now we met with a party that is willing to pay to

**Sjors Bogers** [13:27:34]: get access to a lot of cash money that Apparently can leverage in a certain and they pay Brad a small so then you have a double game because you don't have to pay somebody actually get paid but he's trying to figure out why they can even offer this because super weird right they're doing the service

**Sjors Bogers** [13:27:54]: for you so they get access to the money they can do something with and yeah little interest on but I have no clue how you can do that with money And why would you not charge service that everybody else in the world is charging The reason you can do that with cash is because you bought it a 70%

**David Orban** [13:28:16]: discount because you are laundering Yeah, yeah, I think that is the explanation.

**Sjors Bogers** [13:28:24]: Yeah, but that's, that's not something you want to do business with, right?

**David Orban** [13:28:31]: No.

**Sjors Bogers** [13:28:33]: So he's.

**Sjors Bogers** [13:28:34]: He's trying to figure that out because the whole deal, as he had it in mind, is already off the table.

**Sjors Bogers** [13:28:40]: they wanted to do a test run, which they did for 100k and was always the promise to do But because it took long, some of the middleman involved increased their and therefore the original deal is off the and the party is not that interested anymore because even a slight interest increase is huge

**Sjors Bogers** [13:29:01]: impact And maybe they didn't even have millions, and they just wanted to do 100K quickly, right?

**Sjors Bogers** [13:29:09]: We know.

**Sjors Bogers** [13:29:10]: Yeah, yeah.

**Sjors Bogers** [13:29:13]: So, yeah.

**David Orban** [13:29:14]: So, so, I mean, it's not our business anymore.

**David Orban** [13:29:21]: But hope it is not what I Because what I think is that Nadine went back with the kids because they need to go to school.

**David Orban** [13:29:37]: But the problem is between the two of them.

**David Orban** [13:29:40]: That is is staying back.

**David Orban** [13:29:46]: Why do you have Because there is no reason for Brad not to fly Not the investor, not the OTC.

**David Orban** [13:29:57]: That is just Yeah, right.

**Sjors Bogers** [13:30:08]: I hope not for him personally, but I never got that impression that there's any friction and then between I'm not that whole time, of course, But I do have an impression that he leaves Nadine, only gives Nadine the necessary information.

**David Orban** [13:30:27]: I'm pretty sure they don't discuss everything Yes, until he can't anymore, If there's a real financial tension, you know, everything that you have, like, you know, I didn't tell Diana that I wasn't getting paid for three No, didn't.

**David Orban** [13:30:52]: No.

**David Orban** [13:30:54]: Okay.

**David Orban** [13:30:54]: when are she knows?

**Multiple speakers** [13:30:59]: How long has Mm-hmm.

**David Orban** [13:31:03]: For five Okay.

**Sjors Bogers** [13:31:05]: And why did you choose not to Or distress?

**Sjors Bogers** [13:31:09]: Yeah.

**David Orban** [13:31:09]: Yeah, because I didn't care and I it wouldn't have

**David Orban** [13:31:18]: I didn't want her to bust my ball so you need to find something that pays you, right?

**Multiple speakers** [13:31:24]: Because so it's okay, but I did it on my own Right, yeah, I would probably never do I would probably say it as soon wife.

**David Orban** [13:31:40]: I understand, and it is really the Yes and no.

**Sjors Bogers** [13:31:50]: It also caused me a relationship or two, I think, to go to the situation.

**Sjors Bogers** [13:31:56]: It had already, Yeah, with the girl in Amsterdam was definitely And also with dating with other people Yeah, sometimes they, they The story move forward long enough.

**Sjors Bogers** [13:32:12]: think you're a loser whatever, right?

**Sjors Bogers** [13:32:14]: They don't say it with so many but I'd rather be honest and be a loser than lead them on.

**David Orban** [13:32:20]: So.

**David Orban** [13:32:27]: Yeah, we have some... that's, let's see.

**David Orban** [13:32:34]: We have hedgehogs in the garden and the dog smelling it and wants to go and eat the hedgehog.

**Sjors Bogers** [13:32:44]: Yes, you them.

**David Orban** [13:32:47]: This hasn't had the chance yet, but the other one would come home with all the muddled full with pieces of hedgehog, you know.

**David Orban** [13:33:01]: That's funny.

**David Orban** [13:33:02]: Terrible, terrible.

**David Orban** [13:33:04]: All So have a good weekend and I will not speak to you on Monday, and I will see you on Tuesday, but of course we can text and do And I assume you're going to be busy between, is it, 10 1, As I arrive little sooner.

**David Orban** [13:33:34]: So right now, as a matter of fact, I don't have anything So what I think I will be doing is to have nice breakfast with Diana and then maybe just work Because what I normally would be doing you know, set up a meetup of my own, reach out to people.

**David Orban** [13:34:02]: And here instead I wanted to make myself available to anyone in the team if they come up with something that we could be doing So for the moment I didn't organize which means that as you arrive, We could meet earlier and if anything changes, I will Okay, yeah, sounds like a plan.

**David Orban** [13:34:31]: And did Amira clarify which Hilton, because they're like a dozen Hilton's Yeah, and the meeting invites at canopy.

**Sjors Bogers** [13:34:41]: Okay, perfect.

**Sjors Bogers** [13:34:43]: That's also the one you're right?

**Sjors Bogers** [13:34:44]: Yes.

**David Orban** [13:34:47]: Okay.

**David Orban** [13:34:48]: right.

**Sjors Bogers** [13:34:49]: All right.

---
*Backed up from MeetGeek on 2026-03-30 09:01*
