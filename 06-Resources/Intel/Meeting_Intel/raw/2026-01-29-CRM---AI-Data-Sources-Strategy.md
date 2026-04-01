# CRM & AI Data Sources Strategy

**Date:** 2026-01-29
**Duration:** Unknown
**Meeting ID:** 3b877506-290d-4a8b-8b6a-f5840d6ed24c

## Participants
- *Participants not listed*

### Summary

The meeting focused on consolidating multiple contact data sources into the CRM (Pipedrive) and establishing systems of record (SharePoint, Trezorite). Participants prioritized collecting historic exports (LinkedIn, MailChimp, Alicia and JAD spreadsheets) and discussed practical workflows for business cards using a lightweight MVP: photo + voice note, then OCR and speech-to-text to populate CRM fields. AI was proposed to extract structured information, enrich records, and prompt follow-ups. Compliance (data protection and opt-out handling) and cautious use of cloud vs. in-house storage were addressed. Operational next steps included assigning Asana tasks, installing Outlook/Slack on mobile, and distributing security/onboarding documents.

## Full Transcript

**Speaker_04** [09:32:47]: Did you get your notification

**Speaker_00** [09:32:49]: of what?

**Speaker_04** [09:32:50]: Claude that you notified it once the data.

**Speaker_00** [09:32:53]: Oh, I forgot about it.

**Speaker_00** [09:32:56]: Let's check.

**Speaker_00** [09:32:57]: That's a very good thing, absolutely.

**Speaker_04** [09:33:02]: Are you paying for the subscription?

**Speaker_04** [09:33:04]: Because I think Claude

**Speaker_00** [09:33:04]: is paid.

**Speaker_04** [09:33:05]: I think Claude...

**Speaker_00** [09:33:07]: Yeah, yeah, I'm on a paid subscription.

**Speaker_00** [09:33:10]: Absolutely,

**Speaker_04** [09:33:10]: yes.

**Speaker_00** [09:33:13]: So LinkedIn, new permission required sheets.

**Speaker_00** [09:33:21]: Oh, okay, it's ready to create the spreadsheet.

**Speaker_00** [09:33:24]: Or it was, who knows when.

**Speaker_00** [09:33:25]: Let's hope it remembers what it was doing.

**Speaker_00** [09:33:31]: Okay, that's okay.

**Speaker_01** [09:33:34]: What I would like to do is multiple things, but of course, definitely cover what you wanted to talk about, which is CRM and AI,

**Speaker_05** [09:33:47]: right?

**Speaker_01** [09:33:49]: And we,

**Speaker_01** [09:33:57]: you have to excuse me, but I don't remember if we went through what I I'm going through with everyone, including showing you the acceptable use policy and the security training documents, security briefing documents.

**Speaker_01** [09:34:20]: Did we go through these?

**Speaker_01** [09:34:22]: No.

**Speaker_01** [09:34:22]: Okay, so we will do

**Speaker_05** [09:34:23]: that.

**Speaker_01** [09:34:24]: Okay.

**Speaker_01** [09:34:25]: Did we look at your email signature settings and things like that?

**Speaker_01** [09:34:29]: No.

**Speaker_01** [09:34:29]: Did we in the past?

**Speaker_05** [09:34:31]: No.

**Unknown speaker** [09:34:31]: Okay.

**Speaker_01** [09:34:31]: So we will do that as well.

**Speaker_01** [09:34:33]: But let's start with, actually not only CRM, let's start with data sources and then what you think your high priority objectives are with regards to those data sources.

**Speaker_01** [09:34:58]: You have been here for one week or less?

**Speaker_03** [09:35:01]: Two weeks.

**Speaker_01** [09:35:02]: Two weeks.

**Speaker_01** [09:35:03]: A long time.

**Speaker_01** [09:35:05]: A long time.

**Speaker_03** [09:35:05]: It

**Speaker_01** [09:35:07]: is.

**Speaker_01** [09:35:08]: Have you been able to map the data sources where we have data that you need to consolidate?

**Speaker_04** [09:35:16]: Right.

**Speaker_04** [09:35:18]: I think the data sources that we get currently is the business cards.

**Speaker_04** [09:35:24]: or normal interpersonal relationship and that's it, okay?

**Speaker_04** [09:35:33]: Because it is, you know, it's mostly given to me, when I'm joined so by Lee, by Yvon, that's it.

**Speaker_04** [09:35:42]: So other data sources, I don't have it in hand.

**Speaker_04** [09:35:46]: So I overheard, I said, saying, what about the data that I have in next cell?

**Speaker_04** [09:35:51]: Where do I keep it?

**Unknown speaker** [09:35:52]: And

**Speaker_04** [09:35:53]: I was like, we have a built-in CRM, you have me.

**Speaker_04** [09:35:56]: I can analyze the data if we have some duplicates and Okay, yeah.

**Speaker_01** [09:36:01]: Okay, so let me list a few more that I know, and then of course there will be many that I don't know either,

**Speaker_05** [09:36:08]: right?

**Speaker_01** [09:36:10]: And then either you or Ivan or me, we have to communicate, not once, but over

**Speaker_05** [09:36:20]: and

**Speaker_01** [09:36:20]: over again to everyone.

**Speaker_01** [09:36:24]: what is our objective and that they should support our objective in consolidating the data into the CRM.

**Speaker_01** [09:36:33]: Okay?

**Speaker_01** [09:36:33]: So one important step in order to do that is to declare, which is what I will do, either today or tomorrow, doesn't matter, but very

**Speaker_05** [09:36:44]: shortly.

**Speaker_01** [09:36:45]: what are our systems of record.

**Speaker_02** [09:36:48]: Right, okay.

**Speaker_01** [09:36:49]: So for our policies, the system of record is SharePoint.

**Speaker_05** [09:36:57]: Okay.

**Speaker_01** [09:36:58]: For our client folders, the system of record is treasured.

**Speaker_01** [09:37:06]: for the client contact information, the system of record is the CRM, i.e.

**Speaker_01** [09:37:12]: pipe drive.

**Speaker_01** [09:37:13]: And then if the CRM changes in the future, it doesn't matter.

**Speaker_01** [09:37:18]: The system of record for client contact information is the CRM.

**Speaker_01** [09:37:24]: So today pipe drive.

**Speaker_01** [09:37:27]: Now, that means something very important.

**Speaker_01** [09:37:34]: Everyone is free to keep their friends' lists on Excel, but they are not free to keep their company corporate contact lists on Excel.

**Speaker_01** [09:37:46]: Right.

**Speaker_01** [09:37:46]: It is just not allowed.

**Speaker_03** [09:37:48]: Exactly.

**Speaker_03** [09:37:48]: Right.

**Speaker_01** [09:37:50]: So we will, of course, not be rigid about enforcing

**Speaker_03** [09:37:54]: it.

**Speaker_01** [09:37:56]: until we are, until we are, right?

**Speaker_01** [09:37:58]: So progressively we will increase the pressure.

**Speaker_01** [09:38:01]: Right,

**Speaker_02** [09:38:01]: right,

**Speaker_01** [09:38:02]: yeah.

**Speaker_01** [09:38:02]: Very simply, because it is otherwise non-compliant, and we have to be

**Speaker_02** [09:38:07]: compliant.

**Speaker_01** [09:38:08]: Compliant, exactly, yes.

**Speaker_01** [09:38:09]: So, um,

**Speaker_01** [09:38:19]: I can already pinpoint.

**Speaker_01** [09:38:22]: a few Excel lists that actually I also have and I can send you.

**Speaker_01** [09:38:27]: Okay.

**Speaker_01** [09:38:28]: JAD.

**Speaker_01** [09:38:29]: Have you heard of JAD?

**Speaker_01** [09:38:31]: Yes.

**Speaker_01** [09:38:31]: Okay.

**Speaker_01** [09:38:32]: So JAD organizes our networking meetings and dinners all over the world.

**Speaker_01** [09:38:41]: Australia and Singapore and Dubai and London and New York and etc.

**Speaker_01** [09:38:47]: And he has a spreadsheet that he sent me already in June I think.

**Speaker_01** [09:38:57]: And he is very eager for that list to be in our CRM.

**Speaker_03** [09:39:02]: Oh, okay.

**Speaker_01** [09:39:03]: And so I will send you the list and then you can look at the list and decide how to clean the data, how to enrich the data, and then put it in the

**Speaker_02** [09:39:13]: CRM,

**Speaker_01** [09:39:14]: right?

**Speaker_01** [09:39:17]: Right.

**Speaker_01** [09:39:18]: You mentioned Michael, right?

**Speaker_01** [09:39:20]: And he's 20 plus thousand contacts.

**Speaker_01** [09:39:24]: Okay?

**Speaker_01** [09:39:25]: And then I showed you my LinkedIn.

**Speaker_01** [09:39:28]: And you didn't ask me because you chose to be shy.

**Speaker_01** [09:39:32]: You should have asked me, can I have your contacts?

**Speaker_01** [09:39:39]: Hi.

**Speaker_03** [09:39:39]: Right?

**Speaker_01** [09:39:40]: Yeah, but it's

**Speaker_03** [09:39:41]: great.

**Speaker_01** [09:39:42]: Well,

**Speaker_03** [09:39:42]: well,

**Speaker_01** [09:39:43]: the answer can be no.

**Speaker_03** [09:39:45]: Okay.

**Speaker_01** [09:39:45]: But if you don't ask, I mean, you are thirsty for data.

**Speaker_01** [09:39:52]: You want to have a million records in Pipe Drive.

**Speaker_01** [09:39:58]: But if you... Oh, and I don't know if you report to Ivan?

**Speaker_05** [09:40:03]: Okay.

**Speaker_01** [09:40:04]: So I don't know if Ivan already came to you with your... the role charter.

**Speaker_04** [09:40:12]: Yeah, like the KPIs.

**Speaker_01** [09:40:14]: Yes.

**Speaker_01** [09:40:15]: So you will have your objectives and you will have the KPIs that support you in measurably.

**Speaker_01** [09:40:24]: trending and hopefully achieving your objectives.

**Speaker_01** [09:40:27]: Right?

**Speaker_01** [09:40:28]: So I don't know, but one of those KPIs is going to be the growth of the CRM month by month.

**Speaker_03** [09:40:37]: Exactly,

**Speaker_01** [09:40:37]: yes.

**Speaker_01** [09:40:37]: So if you don't ask, people like me, with 27,000 contacts, You are not going to get your bonus.

**Speaker_01** [09:40:45]: You're not very simple.

**Speaker_01** [09:40:47]: If you don't reach your objectives and KPS, you are not going to get your bonus.

**Speaker_01** [09:40:52]: So you must overcome your being shy because there's money on the table.

**Speaker_01** [09:40:57]: And if you want the money, you have to

**Speaker_04** [09:41:00]: ask.

**Speaker_04** [09:41:00]: Exactly.

**Speaker_01** [09:41:01]: Okay.

**Speaker_04** [09:41:03]: But questions.

**Speaker_04** [09:41:05]: So I mean, if it's with Michael and you, they would be a lot of people who would be still getting connection requests from their LinkedIn also, right?

**Speaker_04** [09:41:15]: It's one of the sources that they would get, apart from the business card, the event that they go to.

**Speaker_04** [09:41:21]: So should I be managing the LinkedIn account also?

**Speaker_01** [09:41:25]: Well, that is the second question.

**Speaker_01** [09:41:28]: What is the first

**Speaker_04** [09:41:29]: question?

**Speaker_04** [09:41:33]: No, I think that I'm not sure because my first question is, of course.

**Speaker_01** [09:41:38]: If I tell you what the first question is, can you force yourself to speak it back to me?

**Speaker_05** [09:41:44]: Okay, okay.

**Speaker_01** [09:41:46]: The first question is, David, can you please export your LinkedIn data and give it to me?

**Speaker_04** [09:41:52]: Yeah, how do I do it?

**Speaker_04** [09:41:55]: How do I...

**Speaker_01** [09:41:56]: Wait a

**Speaker_04** [09:41:56]: minute.

**Speaker_01** [09:41:57]: you agreed that you repeat the question.

**Speaker_04** [09:42:00]: Yeah, so David, how do I get your LinkedIn?

**Speaker_01** [09:42:04]: No, no, no, no, no, no, okay.

**Speaker_01** [09:42:06]: Look, word by word, I said, David, can you export your LinkedIn contacts for me and give them to me?

**Speaker_04** [09:42:15]: David, could you please extract your LinkedIn contacts and give to me?

**Speaker_01** [09:42:21]: Yes.

**Speaker_01** [09:42:22]: Okay.

**Speaker_01** [09:42:22]: That's it, because obviously, Well, maybe in the case of Michael, he gave you his login, and then you will export the contacts.

**Speaker_05** [09:42:34]: Right.

**Speaker_01** [09:42:35]: But it is probably not necessary, and it increases the probability of getting no as an answer if you ask the login to

**Speaker_02** [09:42:46]: everyone.

**Speaker_02** [09:42:46]: Exactly, yeah.

**Speaker_01** [09:42:47]: So no, you don't need to ask the

**Speaker_02** [09:42:49]: login.

**Speaker_01** [09:42:50]: But you want the data.

**Speaker_02** [09:42:52]: Right, yeah.

**Speaker_01** [09:42:53]: So the question is, to everyone, Can you give me your LinkedIn export?

**Speaker_01** [09:42:58]: That's the question.

**Speaker_05** [09:42:59]: Right.

**Speaker_01** [09:43:00]: And then someone say yes, like me, others say no.

**Speaker_01** [09:43:04]: Okay?

**Speaker_01** [09:43:05]: Now, since you are not asking for login, your second question is not even relevant because obviously you

**Speaker_01** [09:43:18]: to manage the account, you want the

**Speaker_03** [09:43:20]: data.

**Speaker_01** [09:43:21]: Okay?

**Speaker_01** [09:43:22]: So a task for me and here is a task for you.

**Speaker_01** [09:43:27]: Please assign me a task on Asana.

**Speaker_02** [09:43:30]: Asana,

**Speaker_01** [09:43:31]: right.

**Speaker_01** [09:43:31]: Okay?

**Speaker_01** [09:43:31]: So the task from you to me is

**Speaker_02** [09:43:34]: give

**Speaker_01** [09:43:35]: you my LinkedIn data.

**Speaker_02** [09:43:38]: Okay?

**Speaker_02** [09:43:38]: Right, okay.

**Speaker_01** [09:43:39]: Now, So that's another source for you of a lot of data.

**Speaker_01** [09:43:44]: And I don't know how many people have how many followers.

**Speaker_01** [09:43:47]: And by the way, I have a total of about 100,000 followers.

**Speaker_01** [09:43:55]: 30,000 on LinkedIn, 10,000 on X, 10,000 on Facebook.

**Speaker_01** [09:44:04]: I don't know how many on Instagram and so on and so

**Speaker_05** [09:44:06]: forth,

**Speaker_01** [09:44:07]: right?

**Speaker_01** [09:44:08]: But I don't think you are planning to map people across multiple platforms.

**Speaker_01** [09:44:20]: Your main objective is to have email addresses, is that correct?

**Speaker_01** [09:44:26]: And LinkedIn profiles?

**Speaker_04** [09:44:27]: LinkedIn, basically the name, the organization that they work in, email address as of now, I'm not sure, like I don't want the mobile number, region, because I could still get into pitch work or crunch basis to get the organization details.

**Speaker_04** [09:44:43]: That I would want to know the label of the lead, let's say if it's a prospect or if it's an investor or government entity or yeah, etc.

**Speaker_04** [09:44:57]: like that.

**Speaker_04** [09:44:58]: I think that's one thing.

**Speaker_04** [09:45:00]: on this basis I would want to have few more questions aligned to it if it's an investor how much funds that they want to, what to say,

**Speaker_05** [09:45:11]: you

**Speaker_04** [09:45:12]: know, the minimum investment account that they want to raise and in what sectors, in what fields and what, I think for now, basic for them to, you know, until I start, you know, pulling in more data, like, let's say, in the future that how many, like, you know, in past, what was the company that

**Speaker_04** [09:45:33]: they have challenged for, like, you know, how many funds they have raised for other companies what's your growth, revenue and all of that.

**Speaker_04** [09:45:40]: So that's later.

**Speaker_04** [09:45:41]: But for now, I want to keep it very simple so that at least they get attached to that particular thing.

**Speaker_04** [09:45:47]: Okay, I need to put it in.

**Speaker_01** [09:45:48]: Well, you already listed something that is close to impossible.

**Speaker_01** [09:45:53]: Because let's assume that I give you, and it won't be 27,000 because, again, LinkedIn, shows those as contacts and followers, but when I export, it depends on how many of them agreed to provide their emails,

**Speaker_02** [09:46:15]: right?

**Speaker_02** [09:46:15]: Right, yeah.

**Speaker_01** [09:46:17]: So there will be a spreadsheet and you are not going to sit with me and go through 27,000 to check those things, right?

**Speaker_01** [09:46:29]: It is a wonderful challenge, but I don't know how you are gonna enrich the data so that those fields can be filled.

**Speaker_01** [09:46:38]: Okay.

**Speaker_01** [09:46:38]: Investor, not investor, ticket size,

**Speaker_04** [09:46:42]: etc.

**Speaker_04** [09:46:43]: But how would I know if what label, you know, is attached to the particular person or organization because eventually you are texting the person, you would be going to an event and having a connection between, you would be knowing whatever the

**Speaker_01** [09:46:58]: organization.

**Speaker_01** [09:46:59]: Yes, but let's distinguish between a historical

**Speaker_04** [09:47:02]: dump,

**Speaker_01** [09:47:03]: you know, I just received a notification from LinkedIn and I was on LinkedIn for the past 20 years or whatever, it's longer than Well, the data

**Speaker_02** [09:47:17]: dump

**Speaker_01** [09:47:19]: is going to include every period of time.

**Speaker_02** [09:47:23]: Right,

**Speaker_01** [09:47:24]: right, yeah.

**Speaker_01** [09:47:26]: And so the same for Michael,

**Speaker_05** [09:47:29]: right.

**Speaker_01** [09:47:30]: So I think it is useful to distinguish between a historical snapshot and then add to that cumulative like week after week the business cards and the events.

**Speaker_01** [09:47:46]: Because if I meet someone yesterday and I have a business card and either I speak to you or I dictate to chat GPT or whatever it is, I will remember.

**Speaker_01** [09:47:59]: If I do it next week, I already not remember.

**Speaker_01** [09:48:02]: Exactly,

**Speaker_05** [09:48:03]: exactly.

**Speaker_01** [09:48:03]: Right?

**Speaker_01** [09:48:04]: So what we are talking about now is not those business cards.

**Speaker_01** [09:48:09]: We are talking about historical

**Speaker_03** [09:48:11]: data

**Speaker_01** [09:48:12]: that, because I asked you, if you mapped the data sources, and the same with JAD.

**Speaker_01** [09:48:23]: I don't know, but whatever his spreadsheet is, I don't know if you can ask him one by one what he knows about.

**Speaker_01** [09:48:30]: Maybe, maybe, but I would be surprised that he knows everything about everyone, because of the length of time.

**Speaker_01** [09:48:37]: Right, okay.

**Speaker_01** [09:48:39]: Okay, so my question was, and you implicitly answered,

**Speaker_05** [09:48:48]: my

**Speaker_01** [09:48:49]: question was, are you planning to keep track and then record in pipe drive social media accounts of contacts that are different from LinkedIn.

**Speaker_01** [09:49:05]: So are you interested in X or are you interested in Instagram or other things?

**Speaker_04** [09:49:11]: Yes, I would want to, I think maybe in the near future because currently I want to focus on one that is for current, like the historical data that we have from LinkedIn accounts from everybody yet at the present that I get the business card from people.

**Speaker_01** [09:49:33]: So I just want to talk about the historical first, because we are talking about data, how you aggregate, how you map and aggregate, and then you process what is here.

**Speaker_01** [09:49:42]: Okay, so the answer is no.

**Speaker_01** [09:49:44]: As of today, you are not asking me to also give you the list of X or list of Instagram, the list of Facebook, the list of everything else, right?

**Unknown speaker** [09:49:56]: Okay.

**Speaker_01** [09:50:01]: Next question.

**Speaker_01** [09:50:03]: Have you thought about the data protection legislation

**Speaker_05** [09:50:10]: in

**Speaker_01** [09:50:12]: force in the UAE

**Speaker_05** [09:50:14]: and

**Speaker_01** [09:50:15]: how what you are planning to do is abiding the law or breaking the

**Speaker_05** [09:50:24]: law,

**Speaker_01** [09:50:25]: and how are you planning to manage that?

**Speaker_04** [09:50:29]: No, I haven't read about that.

**Speaker_01** [09:50:31]: Okay, so you should.

**Speaker_04** [09:50:37]: Yeah, I should,

**Speaker_01** [09:50:37]: yes, I should, yeah.

**Speaker_01** [09:50:38]: And all over the world,

**Speaker_05** [09:50:41]: there

**Speaker_01** [09:50:43]: is different legislation, weaker or stronger, but almost everywhere in the world, there is a fundamental paradox.

**Speaker_01** [09:50:53]: And it is that people have the right to ask you to not to be contacted and erase their data.

**Speaker_01** [09:51:07]: And that means that they have to be in a special database.

**Speaker_04** [09:51:12]: Right.

**Speaker_04** [09:51:13]: Which is secretive and which is not,

**Speaker_01** [09:51:15]: you know.

**Speaker_04** [09:51:15]: Which

**Speaker_01** [09:51:16]: gets checked every time you send a mailing, for example.

**Speaker_01** [09:51:21]: you have to check against that opt- out list so that by mistake you don't contact them.

**Speaker_01** [09:51:29]: And the paradox is that they ask you to delete their data.

**Speaker_04** [09:51:32]: Exactly.

**Speaker_01** [09:51:33]: But no, that's not what you do.

**Speaker_01** [09:51:34]: You keep it in a special list, right?

**Speaker_01** [09:51:37]: So I'm not a lawyer and I don't know how this is not common knowledge that this is how it should

**Speaker_05** [09:51:45]: work.

**Speaker_01** [09:51:47]: I did receive deletion requests with other companies or companies where I invested, received them, and then you communicate to the person who received your request based on the privacy law, blah, blah, blah, and then I don't know, I don't know.

**Speaker_01** [09:52:06]: Because that specialist is very important, right?

**Speaker_01** [09:52:08]: The opt-out list.

**Speaker_03** [09:52:09]: Right, exactly.

**Speaker_01** [09:52:10]: Now, um...

**Speaker_03** [09:52:16]: So...

**Speaker_01** [09:52:18]: The next source, which very logically comes into play is MailChimp.

**Speaker_01** [09:52:25]: Okay?

**Speaker_01** [09:52:26]: We have

**Speaker_03** [09:52:26]: MailChimp.

**Speaker_01** [09:52:28]: We are not using it because not having the license means that we haven't been actively marketing ourselves, but we have MailChimp and we, as a consequence, should give you the list from MailChimp in order to put it into the CRM.

**Speaker_01** [09:52:48]: Okay?

**Speaker_04** [09:52:49]: So a question, what is MailChimp first of all?

**Speaker_04** [09:52:52]: Because yesterday I heard Michael also was saying, but it was not clear to me.

**Speaker_04** [09:52:55]: So what's...

**Speaker_01** [09:52:57]: Okay.

**Speaker_01** [09:52:58]: It is just a platform of email marketing.

**Speaker_03** [09:53:02]: Okay.

**Speaker_01** [09:53:03]: Are you familiar with HubSpot?

**Speaker_01** [09:53:06]: HubSpot has a marketing module.

**Speaker_01** [09:53:08]: dedicated to sending large volumes of

**Speaker_05** [09:53:11]: email,

**Speaker_01** [09:53:12]: right?

**Speaker_01** [09:53:13]: Not the kind of one-on-one emails that a salesperson would send to

**Speaker_04** [09:53:20]: a

**Speaker_01** [09:53:20]: prospect.

**Speaker_01** [09:53:21]: Yeah, so it's

**Speaker_04** [09:53:21]: like a bulk email that it would just generate to other people.

**Speaker_01** [09:53:23]: It still can be personalized based on the fields that you have available, but it is typically sent, do you know what AB testing is?

**Speaker_01** [09:53:36]: Okay.

**Speaker_01** [09:53:38]: AB testing is when you send, you have, let's say, 100,000 emails.

**Speaker_01** [09:53:50]: You send 10,000 with a given subject line, and you see how many of them are opened.

**Speaker_01** [09:53:58]: You send 10,000 with an other subject line, and then you see which one is the better.

**Speaker_01** [09:54:05]: and you send to the remainder 80,000 the winner of this test.

**Speaker_01** [09:54:11]: And if you have millions of addresses rather than a few hundred thousand, then you can do tests cascading.

**Speaker_01** [09:54:20]: So first you establish the subject

**Speaker_05** [09:54:23]: line,

**Speaker_01** [09:54:24]: then you establish the copy.

**Speaker_01** [09:54:26]: then you establish the action item, the call to action button.

**Speaker_01** [09:54:33]: And Amazon, already 20 years ago was doing a dozen steps before they finally sent the email to everyone.

**Speaker_01** [09:54:47]: So optimizing the message over and over again.

**Speaker_01** [09:54:51]: So

**Speaker_04** [09:54:51]: it's basically like, you know, the number of people who open the mail, the more attractive the mail is, you know, I would send it to the main people, let's say, like, the, you know, high profile and all of that.

**Speaker_04** [09:55:06]: That's what it is.

**Speaker_04** [09:55:07]: I have word about it.

**Speaker_04** [09:55:09]: I think I read about it somewhere during the day this

**Speaker_03** [09:55:12]: week

**Speaker_04** [09:55:12]: itself.

**Speaker_04** [09:55:13]: So I think it's the same that I know about.

**Speaker_04** [09:55:16]: So basically you just generate on which higher scale that the email has been reached out to.

**Speaker_04** [09:55:22]: Let's say that, okay, these many contacts have opened this particular email and then you would send that particular email to the X number of people,

**Speaker_01** [09:55:30]: right?

**Speaker_04** [09:55:30]: Yes.

**Unknown speaker** [09:55:30]: Okay.

**Speaker_01** [09:55:32]: Now, have you met Alicia?

**Speaker_01** [09:55:36]: Okay.

**Speaker_01** [09:55:37]: So I don't know for certain, but I think Alicia has a lot of spreadsheets.

**Speaker_01** [09:55:44]: Not even on Excel, on Google.

**Speaker_01** [09:55:46]: Okay, so you should ask her as well, to give you those lists so that you can't put them on pipe

**Speaker_04** [09:55:55]: drive.

**Speaker_01** [09:55:56]: Right,

**Speaker_04** [09:55:56]: yes, she do, she will provide me, but now it's her one.

**Speaker_04** [09:55:59]: We had a call, I think, a day, two days before, with me, Lee and Alicia.

**Speaker_01** [09:56:05]: Okay, perfect, perfect.

**Speaker_01** [09:56:07]: And you know, you should do just like with me, you can assign her a task on Asana, and then at least, you know, you agreed, you asked, and then whenever it happens.

**Speaker_01** [09:56:20]: You know, maybe it is not urgent, but it will not disappear, it will not be forgotten.

**Speaker_03** [09:56:25]: Exactly,

**Speaker_01** [09:56:26]: yeah.

**Unknown speaker** [09:56:26]: Okay.

**Speaker_01** [09:56:27]: Now, let's talk about a business cards.

**Speaker_01** [09:56:32]: So, yes.

**Speaker_01** [09:56:33]: But again, there is a historical set of business cards because I am 100% sure that either in his office or at home, Michael has stack after stack after stack of business cards.

**Speaker_01** [09:56:47]: So did you agree with him that he would physically give you these

**Speaker_04** [09:56:51]: cards?

**Speaker_04** [09:56:52]: We did talk about business card.

**Speaker_04** [09:56:53]: I think first conversation was about LinkedIn, how we manage And about stacking of business cards, I believe everybody has it and they haven't

**Speaker_01** [09:57:03]: added.

**Speaker_01** [09:57:03]: Okay, but let's start with Michael.

**Speaker_04** [09:57:04]: Yes.

**Speaker_04** [09:57:05]: Okay, so let's say that I receive his business cards as of now to...

**Speaker_01** [09:57:12]: No, sorry.

**Speaker_01** [09:57:14]: I understand that you have to manage them and process them, but did you agree that he would give them to you?

**Speaker_04** [09:57:20]: Yeah, I'm not agreed, we haven't talked about it yet.

**Speaker_04** [09:57:23]: Okay.

**Speaker_04** [09:57:23]: So hopefully he agrees to it, because he would be given

**Speaker_01** [09:57:26]: it.

**Speaker_01** [09:57:26]: Oh, I would be surprised if he didn't, but you must ask.

**Speaker_04** [09:57:29]: Right, right, yeah, because we were focusing on LinkedIn.

**Speaker_01** [09:57:32]: That's okay, I'm not saying that you should have

**Speaker_04** [09:57:34]: asked.

**Speaker_01** [09:57:36]: I'm

**Speaker_04** [09:57:36]: just

**Speaker_01** [09:57:37]: saying that you have to ask.

**Speaker_01** [09:57:39]: And that is an important source of contacts.

**Speaker_02** [09:57:43]: Right.

**Speaker_01** [09:57:44]: Right?

**Speaker_01** [09:57:44]: Not only the new ones, even the old ones.

**Speaker_01** [09:57:47]: Okay?

**Speaker_01** [09:57:48]: And then again, how old?

**Speaker_01** [09:57:51]: Who knows?

**Speaker_01** [09:57:53]: Does it make sense to get a 10 years old business card in this world where things change rapidly, maybe not.

**Speaker_01** [09:58:00]: But a one year old business card, yeah, that

**Speaker_00** [09:58:03]: is

**Speaker_01** [09:58:03]: still

**Speaker_00** [09:58:04]: probably

**Speaker_01** [09:58:04]: valid, right?

**Speaker_01** [09:58:06]: Okay.

**Speaker_01** [09:58:07]: Now, the easiest way today to handle those cards, in my opinion, is with... Cloud or ChatGPT, where you can do them not one by one, but 20 at a time.

**Speaker_01** [09:58:30]: Just put them in three rows, sorry, three columns, six rows, so that's 18 cards.

**Speaker_01** [09:58:41]: You take a photo and then you tell ChatGPT, create a spreadsheet.

**Speaker_01** [09:58:49]: Yeah.

**Speaker_01** [09:58:50]: Okay.

**Speaker_01** [09:58:51]: And so 20 at a time, you can do it.

**Speaker_04** [09:58:54]: Okay.

**Speaker_04** [09:58:55]: Can I pause?

**Speaker_04** [09:58:56]: Can, like, I would want to refine that because, yes, that would be helpful because for me, getting a stack of card, pasting in the information, but it would be just generalized to name.

**Speaker_04** [09:59:07]: maybe the organization name, email, mobile, and the job title, that's it.

**Speaker_04** [09:59:14]: But what about the labels?

**Speaker_04** [09:59:18]: I mean the historical part of data, of course, nobody would be remembering it, but I mean historical part of data, I could just analyze, maybe look into a crunch base, LinkedIn, research about what their particular company is, maybe drop down the particular label, let's say, prospect investor, how

**Speaker_04** [09:59:36]: they are doing well and all of that.

**Speaker_04** [09:59:39]: But on the current pieces, like if I would talk about from the day till the future, I wouldn't be able to manage that, like taking a picture, putting it in.

**Speaker_04** [09:59:55]: So my first step, I was talking to Ivana also about it.

**Speaker_04** [09:59:59]: My first step is to make sure at least, you know, if they get the business card, the day that they get, at least for like 20 minutes, they click the particular snapshot.

**Speaker_04** [10:00:14]: It, like an OCR, it just, what to say, pulls in the information into a form for now, because I'm not talking about a bigger scale that they will be using CRM as of now, but I just wanted to get into, you know, what to say, to, I know it's not, I think I talked about the Google form day before

**Speaker_04** [10:00:34]: yesterday.

**Speaker_04** [10:00:34]: I haven't published it.

**Speaker_04** [10:00:35]: This is just the set of things because I'm very familiar with Google forms that, you know, what the drop downs, the tick marks and everything.

**Speaker_04** [10:00:44]: What I would want your help in this particular

**Speaker_04** [10:00:54]: Yeah.

**Speaker_04** [10:00:55]: So if in Asana or if we can build up an app, I'm not sure where, this is just my views.

**Speaker_04** [10:01:05]: So that, you know, they just click the photo of the business card.

**Speaker_04** [10:01:08]: All the data will be captured to the particular form.

**Speaker_04** [10:01:11]: Let's say if it's an email address, if it is at the rate in the business card, it just captures to that.

**Speaker_04** [10:01:18]: And then you have a drop down of labels.

**Speaker_04** [10:01:21]: Let's say this is a prospect.

**Speaker_04** [10:01:22]: So if it's a prospect, what are the other questions that would be, you know, that they can fill it.

**Speaker_04** [10:01:29]: So

**Speaker_01** [10:01:29]: let's say.

**Speaker_01** [10:01:30]: How would they fill it?

**Speaker_01** [10:01:32]: No, manually?

**Speaker_04** [10:01:33]: Yeah, it's just like, you know.

**Speaker_01** [10:01:35]: Do you think, do you really think it will ever happen?

**Speaker_04** [10:01:39]: No, but not the business card manually.

**Speaker_01** [10:01:41]: No, no, no, these fields, how many are they?

**Speaker_04** [10:01:44]: This is two, five, that's it.

**Speaker_04** [10:01:46]: It's just very small.

**Speaker_04** [10:01:47]: I just want to start with something small, very compact, very centralized data that they can just start filling it.

**Speaker_04** [10:01:55]: Very less.

**Speaker_01** [10:01:56]: It will never

**Speaker_04** [10:01:56]: happen.

**Speaker_04** [10:01:58]: But then...

**Speaker_01** [10:02:01]: Okay.

**Speaker_01** [10:02:02]: It will never happen.

**Speaker_01** [10:02:06]: And I hope to be wrong.

**Speaker_01** [10:02:09]: I'm not saying that you shouldn't try and I will help you trying it.

**Speaker_01** [10:02:15]: But Ivan sent out an email of how the CRM should be used.

**Speaker_01** [10:02:22]: Shervin sent out an email of how the CRM should be used.

**Speaker_02** [10:02:26]: Nobody

**Speaker_01** [10:02:27]: is

**Speaker_02** [10:02:27]: using it.

**Speaker_02** [10:02:28]: Right,

**Speaker_01** [10:02:28]: right.

**Speaker_02** [10:02:28]: Exactly.

**Speaker_02** [10:02:29]: Exactly.

**Speaker_01** [10:02:30]: However, the meeting today, and we are halfway through and we haven't touched the heart of the meeting.

**Speaker_01** [10:02:39]: The meeting today is about AI.

**Speaker_01** [10:02:42]: Creating an app with forms is not AI.

**Speaker_01** [10:02:45]: Okay?

**Speaker_01** [10:02:46]: You know what is AI?

**Speaker_01** [10:02:48]: Is allowing them, when they are in a cab, leaving the event, and they have 10 business cards that they collected to, yes, take a photo of the card and then record their thoughts about that particular person And of course, they can have a reference card.

**Speaker_01** [10:03:13]: Please, please, but it is a printed or, you know, it's on the phone, doesn't matter.

**Speaker_01** [10:03:18]: It is a very simple reminder.

**Speaker_01** [10:03:20]: Please, as you think about the meeting you just had, where you were there with a glass of wine, you had a nice chat, as you are recording your thoughts about this particular contact where you just took a photo, if possible, mention also 1, 2, 3, 4, 5. because when they are in a car, they are half

**Speaker_01** [10:03:47]: drunk, they are very tired, they're not gonna fill in the form.

**Speaker_01** [10:03:51]: And if they do it the next day, they will not remember.

**Speaker_02** [10:03:54]: Exactly.

**Speaker_01** [10:03:55]: So it has to be then.

**Speaker_01** [10:03:56]: But the advantage of AI is that unstructured text can be then extracted and transformed, then math don't on the

**Speaker_04** [10:04:07]: fields.

**Speaker_04** [10:04:07]: That also would help, I think, actually, because let's say that if Though, I mean, I'm just giving an assumption if this could read out loud, what is the funding state?

**Speaker_04** [10:04:18]: And then he could just be like, okay, it is in the seed structure and all of that.

**Speaker_04** [10:04:23]: It just triggers that button.

**Speaker_04** [10:04:24]: Like, if he says it in an unstructured manner, and then with those keywords, if AI can just pull in that information in there, that would be easy.

**Speaker_01** [10:04:34]: Yes.

**Speaker_01** [10:04:36]: And...

**Speaker_01** [10:04:44]: that the AI actually ask follow- up questions.

**Speaker_02** [10:04:49]: Hmm, right, yeah.

**Speaker_01** [10:04:51]: So it says, okay, that's wonderful, but what about this that you didn't mention?

**Speaker_02** [10:04:56]: Right, yeah.

**Speaker_01** [10:04:56]: Okay, one step at a time, okay.

**Speaker_01** [10:04:59]: Now, what is very important is that you have to find one or two people who are not only available but are excited to experiment about this with you.

**Speaker_01** [10:05:22]: And after all the effort realizing that no one uses it.

**Speaker_04** [10:05:26]: Exactly.

**Speaker_04** [10:05:26]: I

**Speaker_01** [10:05:26]: would want to do

**Speaker_04** [10:05:27]: a UAT testing understanding.

**Speaker_01** [10:05:29]: You want to test it with someone and you have to find volunteers, champions who are happy to test it with

**Speaker_04** [10:05:38]: you.

**Speaker_04** [10:05:38]: Exactly.

**Speaker_01** [10:05:39]: Exactly.

**Speaker_04** [10:05:39]: Yes, of course I would want to do that before rolling it out.

**Speaker_04** [10:05:42]: Yeah, life purpose.

**Speaker_04** [10:05:44]: So how would this work?

**Speaker_04** [10:05:47]: My question is that because You told it can't be in form of an app, but what is your vision on this to at least start working?

**Speaker_04** [10:05:58]: Because they wouldn't be able to fill it.

**Speaker_04** [10:06:02]: I don't know how voluntarily like they would be telling me what happened in an event I have you know again it's like unstructured data that I need to record and all of that but what is the what they say the next step that I can you know go into it and then

**Speaker_01** [10:06:18]: so you you mentioned things that are very ambitious and rather than trying and failing to do something very ambitious Have you ever heard about the expression MVP

**Speaker_03** [10:06:34]: you have?

**Speaker_01** [10:06:35]: Yeah, yeah, yeah.

**Speaker_01** [10:06:36]: Okay, it stands for minimum viable product, right?

**Speaker_01** [10:06:40]: So something that is not beautiful, not very functional, but it is one step in the right direction.

**Speaker_01** [10:06:52]: And it produces usable, measurable, feedback that you then use in order to take the next step and the next step and the next step until actually you have something

**Speaker_02** [10:07:07]: great.

**Speaker_02** [10:07:08]: Correct,

**Speaker_01** [10:07:08]: yeah.

**Speaker_01** [10:07:09]: And in the startup world the next stage is product market fit when not only people are available to suffer through the tests but when people are so excited that they are talking to their friends about it and they say

**Speaker_05** [10:07:29]: Oh,

**Speaker_01** [10:07:30]: look at that you are still giving your assistant the business cards.

**Speaker_01** [10:07:34]: That is so ancient.

**Speaker_01** [10:07:36]: Look at what I'm doing.

**Speaker_01** [10:07:38]: This is so cool.

**Speaker_01** [10:07:39]: Exactly.

**Speaker_01** [10:07:40]: And the other person is saying, oh wow, I want to do that.

**Speaker_01** [10:07:44]: Exactly.

**Speaker_01** [10:07:45]: So that will come in three months or six months, who knows, that stage.

**Speaker_01** [10:07:50]: We are not there yet.

**Speaker_01** [10:07:54]: But you ask me, what could be the next step?

**Speaker_01** [10:07:58]: So I can tell you what the next step is.

**Speaker_01** [10:08:00]: It's very, very simple.

**Speaker_01** [10:08:03]: A photo of the business card and the voice recording of the notes.

**Speaker_01** [10:08:11]: And they have to do nothing else, just send you the photo and literally the MP3 of the recording, the audio.

**Speaker_01** [10:08:20]: And then it is our job to build the workflow

**Speaker_05** [10:08:24]: that

**Speaker_01** [10:08:25]: transforms the recording into text.

**Speaker_01** [10:08:29]: that transforms the image into

**Speaker_05** [10:08:32]: fields,

**Speaker_01** [10:08:33]: and then matches the two, and then maybe goes out to LinkedIn, and there are data sources for enriching the data.

**Speaker_01** [10:08:41]: We mentioned Peach Boot, but there are others as well that we can use.

**Speaker_01** [10:08:47]: Okay?

**Speaker_01** [10:08:48]: And so, if I were in you, what I would do is to write a very simple two paragraph request to send as instructions to your testers.

**Speaker_01** [10:09:13]: And these two paragraphs are Thank you very much for volunteering to test this process.

**Speaker_01** [10:09:19]: We are at the very beginning, but I am sure we will improve.

**Speaker_01** [10:09:24]: In the meantime, what I am asking you is the following.

**Speaker_01** [10:09:27]: Please take a photo of the business cards that you collect at events or whatever the contact is.

**Speaker_01** [10:09:34]: Maybe it was a WhatsApp QR code.

**Speaker_01** [10:09:38]: It was a LinkedIn connection.

**Speaker_01** [10:09:39]: It doesn't have to be just business card,

**Speaker_05** [10:09:41]: right?

**Speaker_05** [10:09:42]: and

**Speaker_01** [10:09:42]: record a voice note with whatever you remember, whatever the context is, if possible covering these four or five

**Speaker_04** [10:09:57]: points.

**Speaker_04** [10:09:57]: Right.

**Speaker_01** [10:09:59]: And then send me the photo and the voice recording

**Speaker_05** [10:10:06]: through

**Speaker_01** [10:10:07]: your preferred

**Speaker_05** [10:10:09]: channel.

**Speaker_01** [10:10:10]: rather than already imposing how to send it to you, you leave them free to use Slack or use email or whatever, and then you collect, and then you and I work to make the next step.

**Speaker_03** [10:10:24]: Exactly,

**Speaker_01** [10:10:25]: yes, yes,

**Speaker_03** [10:10:26]: yes, yes.

**Speaker_01** [10:10:27]: Okay?

**Speaker_03** [10:10:27]: Okay, yes,

**Speaker_01** [10:10:28]: good.

**Speaker_04** [10:10:34]: So, okay, that's why I think a basic step that I could to what to say, put in the data into pipe drive and everything.

**Speaker_04** [10:10:44]: But once, like, I think, if I feel that particular, you know, what is the voice recording with these, these things, and the business card snapshot, if they send it to me, what would, like, of course, I would put it into a pipe drive, but I want to stand, like, once it's successful, I want to stand

**Speaker_04** [10:11:03]: one more step on top so that, You know, it is filled, like, you know, of course, maybe with voice recognition, maybe with the, what is a picture, but maybe just one more step on top that they start using some tool to send me in one particular place rather than the other channel.

**Speaker_01** [10:11:27]: Of course.

**Speaker_01** [10:11:29]: Yeah.

**Speaker_01** [10:11:30]: Yeah.

**Speaker_01** [10:11:30]: That is the next step.

**Speaker_01** [10:11:31]: Of course, absolutely.

**Speaker_01** [10:11:33]: Absolutely.

**Speaker_04** [10:11:33]: So what would it be the preferred, you know, preferred app or the channel, or what can you suggest?

**Speaker_01** [10:11:42]: When is the right time to start thinking about it?

**Speaker_01** [10:11:46]: Is now the right time?

**Speaker_01** [10:11:47]: No, I don't think.

**Speaker_01** [10:11:49]: So that's clear.

**Speaker_01** [10:11:51]: The freedom that we enjoy

**Speaker_05** [10:11:55]: is

**Speaker_01** [10:11:56]: because it is necessary because if we thought we already knew, then it wouldn't be an experiment.

**Speaker_01** [10:12:05]: It is an experiment because we don't know.

**Speaker_01** [10:12:07]: We don't know what the best channel would be.

**Speaker_03** [10:12:09]: Exactly.

**Speaker_01** [10:12:10]: We don't know, even if it works, maybe it doesn't work.

**Speaker_01** [10:12:13]: And then why would we invest the effort of thinking about what is the best channel if it doesn't even work,

**Speaker_05** [10:12:19]: right?

**Speaker_01** [10:12:20]: So yes, there will be next steps and we will think about them and we will implement them.

**Speaker_01** [10:12:27]: But today is a waste of time to talk, to think about that.

**Speaker_04** [10:12:31]: Right.

**Speaker_04** [10:12:32]: So in my previous work, just like a suggestion, I don't know if that would work here.

**Speaker_04** [10:12:38]: We had an in-house tech team that they would build the app there.

**Speaker_04** [10:12:42]: you know they would do it so so we in okay this is confidential but I would just want to tell you in VUV like it's it's like a CRM system for banks okay where you have the personal data the business data and the investment side so in the CRM system we had full external side and then the traditional

**Speaker_04** [10:13:08]: what to say, account, like basically current account, personal account, business account, or savings account, it would be managed within the organization.

**Speaker_04** [10:13:19]: It wouldn't be given to anybody else.

**Speaker_04** [10:13:21]: And we can, you know, with... I'm not sure about the very technical IT terms, but that would be our security base rather than we giving it to external parties, because pipe drive, I'm not sure how many data that would be leaking from us.

**Speaker_04** [10:13:37]: So it's just one thought.

**Speaker_04** [10:13:39]: So if ever we have our in-house technical team that can help us and guide us, and if I can, like of course, with your help and Yvonne's help, if I can beat the barrier of creating workflows, managing and giving it a detailed suggestion of what we need in the app or website or that can, you know,

**Speaker_04** [10:14:01]: built from their part.

**Speaker_01** [10:14:02]: So, so I don't remember the name of the bank where you worked.

**Speaker_01** [10:14:06]: Do you know how many people they were in total?

**Speaker_01** [10:14:09]: Yeah,

**Speaker_04** [10:14:09]: this back end, this front end.

**Speaker_01** [10:14:10]: No, no, no, in total between employees and tellers.

**Speaker_01** [10:14:15]: It was a retail bank, right?

**Speaker_04** [10:14:16]: Yeah, it's a retail bank.

**Speaker_04** [10:14:17]: It was like, you know, it's two to three years.

**Speaker_04** [10:14:20]: It's a digital bank, okay, so it was around, I think.

**Speaker_04** [10:14:25]: 20, 25, it was a

**Speaker_01** [10:14:27]: little... 25 people?

**Speaker_01** [10:14:28]: Yes.

**Speaker_01** [10:14:29]: Mm-, okay.

**Speaker_01** [10:14:30]: And how many people were in the IT department?

**Speaker_04** [10:14:36]: No, sorry, 25 people were in the IT department.

**Speaker_01** [10:14:39]: Okay, my question was how many people were in total in the bank?

**Speaker_04** [10:14:42]: In total in the bank.

**Speaker_04** [10:14:44]: It was around, when I joined, it was around touching the 500 ways, but it was very less.

**Speaker_04** [10:14:50]: It... When I left the bank, it targeted to 700 people in

**Speaker_05** [10:14:56]: total.

**Speaker_04** [10:14:57]: Yes,

**Speaker_01** [10:14:57]: because

**Speaker_04** [10:14:57]: I had the access of admin, so I would

**Speaker_01** [10:15:03]: know how many people are in Ali 1?

**Speaker_03** [10:15:05]: Yeah, it's

**Speaker_01** [10:15:06]: 50.

**Speaker_03** [10:15:07]: 50.

**Speaker_01** [10:15:07]: Okay.

**Speaker_01** [10:15:08]: So when you're asking, if we have an IT department, how many people you expect are the IT department out of the 50?

**Speaker_04** [10:15:19]: I'm not sure upon what the particular, you know.

**Speaker_01** [10:15:23]: Sure.

**Speaker_01** [10:15:23]: You are speaking to the IT department.

**Speaker_04** [10:15:25]: Yes, yes.

**Speaker_01** [10:15:26]: No, that's what I say.

**Speaker_01** [10:15:28]: I am the IT

**Speaker_04** [10:15:29]: department.

**Speaker_04** [10:15:29]: Yeah, you are the IT department.

**Speaker_01** [10:15:31]: That's it.

**Speaker_01** [10:15:32]: No one else.

**Speaker_04** [10:15:33]: Okay.

**Speaker_04** [10:15:34]: Could you be able to manage the front-end, back-end?

**Speaker_04** [10:15:41]: No, it's just a question.

**Speaker_02** [10:15:43]: Like,

**Speaker_04** [10:15:43]: because of your help, I would want to get into the structure built in there.

**Speaker_04** [10:15:48]: Because you said, see, you know, you don't want to be in the ancient of like, I just give my card to the assistant.

**Speaker_04** [10:15:54]: She clicks and she puts it in.

**Speaker_04** [10:15:56]: You want to be more futureized and get things well sorted, clean.

**Speaker_04** [10:16:02]: And then it's easier for us to track all the data.

**Speaker_04** [10:16:05]: Let's say that I just put in the data now, Who will follow up on that?

**Speaker_04** [10:16:10]: What is the activity done?

**Speaker_04** [10:16:12]: Let's see if there is a mandate letter.

**Speaker_04** [10:16:14]: Nobody is putting those files from Trezorite.

**Speaker_04** [10:16:16]: It is not even linked.

**Speaker_04** [10:16:17]: Nothing.

**Speaker_04** [10:16:17]: There's no follow-up.

**Speaker_04** [10:16:18]: It's just there.

**Speaker_04** [10:16:20]: But what is the purpose of that data to move in?

**Speaker_04** [10:16:22]: Perfect.

**Speaker_04** [10:16:23]: Okay.

**Speaker_01** [10:16:24]: So there are three different things here.

**Speaker_01** [10:16:27]: One, to actually execute the experiment.

**Speaker_01** [10:16:33]: to understand how long the experiment should last, what we expect, and then be able to measure whether we succeeded or not succeeded.

**Speaker_01** [10:16:46]: Now, not succeeding doesn't mean that, oh my God, we failed.

**Speaker_04** [10:16:50]: No,

**Speaker_01** [10:16:51]: we learned something.

**Speaker_04** [10:16:52]: We learned something,

**Speaker_01** [10:16:52]: right, okay?

**Speaker_01** [10:16:53]: So the experiment succeeds regardless.

**Speaker_01** [10:16:57]: It is either we learn one thing or we learn the other

**Speaker_02** [10:17:00]: thing.

**Speaker_01** [10:17:00]: Perfect, in any case.

**Speaker_01** [10:17:04]: And then you asked something that again is, it's fine.

**Speaker_01** [10:17:14]: I invite you to keep asking every question you

**Speaker_03** [10:17:17]: want.

**Speaker_01** [10:17:19]: as long as you are ready to hear the answer.

**Speaker_01** [10:17:22]: And the answer is, again, it is not a question for now.

**Speaker_02** [10:17:26]: Yes,

**Speaker_01** [10:17:26]: it's... Of course you will not be coding the app.

**Speaker_01** [10:17:29]: Of course you will not be managing back end.

**Speaker_01** [10:17:32]: Of course you will not be designing front end.

**Speaker_01** [10:17:35]: Perfectly fine.

**Speaker_01** [10:17:37]: Don't worry about it right now.

**Speaker_01** [10:17:38]: Don't

**Speaker_02** [10:17:39]: worry.

**Speaker_01** [10:17:40]: We will discuss it and then, you know, we will have, we will find a way.

**Speaker_01** [10:17:46]: Okay, either I will do it because by magic, I don't know.

**Speaker_01** [10:17:50]: Or we will hire someone or whatever it is

**Speaker_05** [10:17:53]: going

**Speaker_01** [10:17:56]: Okay.

**Speaker_01** [10:17:56]: Now, you mentioned something, you just hinted at it.

**Speaker_01** [10:18:00]: that you believe we should have everything in- house rather than using cloud-based services.

**Speaker_01** [10:18:09]: Ideally, that is possible.

**Speaker_01** [10:18:11]: And I think that is a very important point.

**Speaker_01** [10:18:20]: As of right now, we are using cloud-based services.

**Speaker_01** [10:18:24]: But yes, that is a very, very important point.

**Speaker_01** [10:18:31]: We'll see.

**Speaker_01** [10:18:33]: Yes, in the

**Unknown speaker** [10:18:37]: future.

**Speaker_01** [10:18:37]: Okay.

**Speaker_01** [10:18:38]: Now, the third point

**Speaker_05** [10:18:43]: goes

**Speaker_01** [10:18:44]: back a bit to the beginning because I suggested that you should find the champions, you should write to them, And then as they start selling, sending you the photos and the

**Speaker_02** [10:19:01]: recordings.

**Speaker_01** [10:19:02]: Then you and I can agree, and you don't need to worry about I will take care of OCR and speech to text and all those kinds of things.

**Speaker_01** [10:19:14]: So don't worry about that.

**Speaker_01** [10:19:15]: You

**Speaker_04** [10:19:15]: will take

**Speaker_01** [10:19:16]: care.

**Speaker_01** [10:19:16]: Yes.

**Speaker_01** [10:19:17]: Okay, because

**Speaker_04** [10:19:17]: I tried experimenting.

**Speaker_04** [10:19:19]: I wrote the data in GitHub, like the code and everything.

**Speaker_04** [10:19:23]: All of I failed in the, I think I tried twice.

**Speaker_04** [10:19:26]: One is Flutter and one is GitHub.

**Speaker_04** [10:19:32]: Yeah, so I think it was from the API, I think it was, I forgot it was one of the app that I took, but I totally failed.

**Speaker_04** [10:19:43]: was like, okay, this is not my thing, so I said.

**Speaker_04** [10:19:45]: Well,

**Speaker_01** [10:19:46]: when was that?

**Speaker_04** [10:19:47]: Just the first week.

**Speaker_01** [10:19:52]: But were you using AI or you were, which one?

**Speaker_01** [10:19:56]: How?

**Speaker_01** [10:19:58]: Because GitHub is a platform for storing the source code of projects.

**Speaker_03** [10:20:04]: Right, yeah.

**Speaker_01** [10:20:04]: Flutter is a programming language for mobile

**Speaker_03** [10:20:08]: development.

**Speaker_01** [10:20:10]: Right, right.

**Speaker_01** [10:20:11]: And if you attempted to handle them directly, then of course the learning curve is very, very steep.

**Speaker_01** [10:20:18]: But if you addressed whatever you wanted to address with AI, then tell me what AI you use.

**Speaker_01** [10:20:26]: Don't tell me GitHub or Flutter.

**Speaker_04** [10:20:28]: No, so I did use ChatGPT to run me through.

**Speaker_04** [10:20:34]: If I was not sure about it, like, I think the whole day I was in ChatGPT.

**Speaker_04** [10:20:41]: Okay, that's the one thing.

**Speaker_04** [10:20:43]: But yes, I did use Copilot also to help me.

**Speaker_04** [10:20:49]: Yeah, those two.

**Speaker_04** [10:20:50]: I

**Speaker_01** [10:20:51]: was just

**Speaker_04** [10:20:51]: trying to, you

**Speaker_01** [10:20:52]: know,

**Speaker_04** [10:20:52]: like it's like

**Speaker_01** [10:20:53]: a prompt engineer.

**Speaker_01** [10:20:54]: So your experience is very important.

**Speaker_01** [10:21:02]: And the words that you are using are self-defeating because you said, are you failed?

**Speaker_01** [10:21:10]: You didn't fail.

**Speaker_01** [10:21:11]: You didn't fail.

**Speaker_01** [10:21:13]: You learned something.

**Speaker_01** [10:21:15]: I

**Speaker_04** [10:21:15]: learned something, yes, I did.

**Speaker_01** [10:21:16]: But maybe you don't even know what you learned, because I can tell you what you

**Speaker_04** [10:21:21]: learned.

**Speaker_01** [10:21:22]: What you learned is that the tools that you picked are not fit for the purpose.

**Speaker_03** [10:21:29]: yes

**Speaker_01** [10:21:29]: okay in particular co- pilot is a useless piece of shit it's just horrible it's horrible and Microsoft should be ashamed of itself so what I what I I command you for the initiative.

**Speaker_01** [10:21:49]: It is wonderful that you tried.

**Speaker_01** [10:21:51]: You didn't fail.

**Speaker_01** [10:21:52]: And I invite you to ask for advice.

**Speaker_04** [10:21:59]: Yes, I do ask for advice.

**Speaker_01** [10:22:02]: Well, you didn't.

**Speaker_04** [10:22:03]: No, I do ask now,

**Speaker_01** [10:22:04]: yeah, because in a conversation.

**Speaker_01** [10:22:07]: So, so... What

**Speaker_03** [10:22:09]: do I use

**Speaker_01** [10:22:10]: and... So, yes, yes, that's great.

**Speaker_01** [10:22:13]: But probably what would be useful is maybe next week to have another session after you collected a few of these cards, and rather than showing you something in the abstract, to show you specifically how I would approach it doing and then and then you will see how I work and then either we will

**Speaker_01** [10:22:36]: succeed or not succeed because I always learn failing,

**Speaker_05** [10:22:43]: right?

**Speaker_01** [10:22:44]: Okay, so I will have to be going soon and we have another couple of things to go through.

**Speaker_01** [10:22:52]: Did you find this useful in the meantime, this conversation?

**Speaker_04** [10:22:55]: Yes, I did,

**Speaker_01** [10:22:56]: I

**Speaker_04** [10:22:56]: did, yeah.

**Speaker_04** [10:22:57]: And of course, I would want your advice always what particular tools that I can use in AI and what can enrich my skills in your data platform, you know, whatever the resource that I can use very effectively, I would want to ask your advice on that,

**Speaker_05** [10:23:14]: yes.

**Speaker_05** [10:23:14]: Okay.

**Speaker_01** [10:23:23]: It was again asking for permission.

**Speaker_03** [10:23:25]: That's okay, it's

**Speaker_01** [10:23:28]: okay.

**Speaker_01** [10:23:29]: I will show you when it is

**Speaker_03** [10:23:30]: done.

**Speaker_01** [10:23:32]: It is working on this tab creating the

**Speaker_00** [10:23:34]: spreadsheet.

**Speaker_04** [10:23:55]: So one question I want to ask you that you have subscribed for Claude, right?

**Speaker_04** [10:23:59]: Is it useful for you?

**Speaker_04** [10:24:01]: Is it?

**Speaker_04** [10:24:02]: Okay.

**Speaker_04** [10:24:04]: I'm thinking, should

**Speaker_01** [10:24:05]: I... Why would I subscribe you it were not useful to waste money?

**Speaker_04** [10:24:08]: That's true.

**Speaker_04** [10:24:09]: Like,

**Speaker_01** [10:24:09]: I mean, I'm

**Speaker_04** [10:24:10]: just asking.

**Speaker_04** [10:24:12]: Yeah,

**Speaker_01** [10:24:12]: but I told you to be ready for the answer.

**Speaker_04** [10:24:15]: Right.

**Speaker_04** [10:24:19]: Okay, I'm not, because I would want to, because I love researching things, new things.

**Speaker_04** [10:24:26]: And in my feed, it's all AI, this you should use this app and all of that.

**Speaker_04** [10:24:33]: You can build without coding.

**Speaker_04** [10:24:35]: So if you see this read also, I think I'm not sure where I have saved.

**Speaker_04** [10:24:47]: So I keep on saving this to myself.

**Speaker_05** [10:24:51]: Okay.

**Speaker_04** [10:24:52]: So I was like one day I want to do something, maybe build an app and all of that.

**Speaker_01** [10:24:58]: So are you a fan of Star Wars?

**Speaker_01** [10:25:02]: No.

**Speaker_01** [10:25:02]: Have you seen the movies?

**Speaker_05** [10:25:04]: Yeah,

**Speaker_01** [10:25:04]: yeah.

**Speaker_01** [10:25:04]: Okay, you know Yoda, the little green

**Speaker_05** [10:25:07]: character.

**Speaker_01** [10:25:08]: Yoda says, and that is not what you said, but Yoda says, I don't sorry i don't even remember he talks about that that there is no trying there is just doing

**Speaker_02** [10:25:24]: right

**Speaker_01** [10:25:25]: right

**Speaker_02** [10:25:25]: yes

**Speaker_01** [10:25:25]: so so yes of course you can save things forever and say okay when i will have the time i will do something you will never have the time you will never have the time so so it is worth uh doing right away not think about things just start doing right away um And yes, there can be better tools or worse

**Speaker_01** [10:25:51]: tools.

**Speaker_01** [10:25:52]: So developing intuition of what are the right tools for the right things is also good and comes with a little bit of experience as well.

**Speaker_01** [10:26:04]: Okay.

**Speaker_01** [10:26:06]: Now, show me your outlook signature settings.

**Speaker_03** [10:26:17]: Okay, can I compose some meat?

**Speaker_01** [10:26:19]: Yes.

**Speaker_01** [10:26:23]: Okay, and show me how you, sorry, the settings itself.

**Speaker_00** [10:26:34]: Sorry, I'm not familiar with Outlook and where the things are.

**Speaker_04** [10:26:38]: I think I'll just type it out because I know it is in

**Speaker_00** [10:26:41]: the

**Speaker_04** [10:26:42]: home.

**Speaker_00** [10:26:44]: There

**Speaker_03** [10:26:44]: is,

**Speaker_00** [10:26:45]: yes.

**Speaker_03** [10:26:46]: Okay.

**Speaker_03** [10:26:48]: Yes.

**Speaker_00** [10:26:49]: Okay.

**Speaker_01** [10:26:50]: So, okay.

**Speaker_01** [10:26:52]: This is the setting that I wanted to make sure you have, which is you don't have a signature on replies.

**Speaker_01** [10:27:00]: Perfect.

**Speaker_01** [10:27:01]: Do you have Outlook on your phone?

**Speaker_04** [10:27:03]: No, I would want to install it.

**Speaker_04** [10:27:05]: Just, I'm not sure.

**Speaker_04** [10:27:06]: I tried starting at Slack, but I'm not able to, you know, get the work credentials here.

**Speaker_04** [10:27:12]: I'm not sure why.

**Speaker_01** [10:27:14]: Why didn't you ask?

**Speaker_04** [10:27:16]: I

**Speaker_01** [10:27:17]: did.

**Speaker_01** [10:27:17]: No,

**Speaker_04** [10:27:17]: I didn't.

**Speaker_04** [10:27:18]: Why?

**Speaker_04** [10:27:19]: I was, I'm not sure.

**Speaker_04** [10:27:20]: I was like, okay, I can't do it.

**Speaker_04** [10:27:22]: I'll just wait for it and then I'll carry on with my work.

**Speaker_01** [10:27:25]: But that is your work.

**Speaker_04** [10:27:27]: Yeah, that is, I know, but I just, I'm kind of a person that, you know, once I, like, you know, try something, I don't succeed, I keep it aside, I'm like, go to another task.

**Speaker_04** [10:27:39]: I'm not sure, like, I'm trying to improve on that.

**Speaker_01** [10:27:42]: Okay, well, I, if you don't mind, I will keep bothering you I will keep disturbing you asking you are you hiding a problem are you are you sitting on a problem that you are not talking anywhere

**Speaker_04** [10:27:58]: about

**Speaker_01** [10:27:59]: so okay um

**Speaker_04** [10:28:02]: because I think there's an option of I can go to the

**Speaker_01** [10:28:09]: Well, the simplest is to add, no, is to add your email.

**Speaker_05** [10:28:14]: I

**Speaker_01** [10:28:15]: did that.

**Speaker_01** [10:28:15]: Oh, I understand.

**Speaker_01** [10:28:16]: Let's do it again.

**Speaker_01** [10:28:18]: Okay.

**Speaker_01** [10:28:19]: So, sorry, but the first is Outlook.

**Speaker_01** [10:28:20]: Do you have Outlook on the phone?

**Speaker_03** [10:28:23]: No, I think...

**Speaker_01** [10:28:25]: So install Outlook on the phone.

**Speaker_01** [10:28:27]: Okay.

**Speaker_01** [10:28:27]: Then install, sorry, not install, but... enter your email in Slack and then the link that comes to your email when you click the workspace will open on your phone so you cannot click on the computer you have to click on the

**Speaker_03** [10:28:47]: phone yeah I thought okay okay I was right then okay

**Speaker_01** [10:28:52]: so while you are doing that let me ask you a few more questions

**Speaker_03** [10:29:04]: I've worked in it's called view personal.

**Speaker_00** [10:29:22]: Sorry, what are you showing me?

**Speaker_04** [10:29:24]: No, this was the bank that I worked

**Speaker_01** [10:29:26]: in.

**Speaker_01** [10:29:26]: Oh, okay, okay,

**Speaker_04** [10:29:27]: wonderful.

**Speaker_01** [10:29:28]: Okay, very good, thank you.

**Speaker_01** [10:29:33]: So,

**Speaker_01** [10:29:43]: So we looked at the signature and mobile.

**Speaker_01** [10:29:47]: Okay, so when you set up Outlook on your mobile, make sure that you don't advertise Microsoft by putting in the signature automatically this message was composed with

**Speaker_05** [10:30:00]: Outlook.

**Speaker_01** [10:30:02]: Microsoft inserts it, you have to

**Speaker_05** [10:30:05]: delete

**Unknown speaker** [10:30:06]: it.

**Speaker_05** [10:30:08]: accounts.

**Speaker_01** [10:30:09]: Are you set up in the Treasury to?

**Speaker_05** [10:30:12]: Yes.

**Speaker_01** [10:30:12]: Okay, perfect.

**Speaker_01** [10:30:18]: Slack, you need help.

**Speaker_01** [10:30:21]: Azana, do you have Azana?

**Speaker_02** [10:30:23]: Yes, I do have Azana.

**Speaker_02** [10:30:24]: Okay, perfect.

**Speaker_01** [10:30:26]: You have pipe drive, obviously.

**Speaker_01** [10:30:29]: Nitro.

**Speaker_03** [10:30:30]: Yes, nitro, I have no PDF.

**Speaker_01** [10:30:31]: And docu-sign you don't need.

**Speaker_03** [10:30:33]: No, I don't need docu-sign as

**Unknown speaker** [10:30:35]: of

**Speaker_01** [10:30:36]: Okay.

**Speaker_01** [10:30:42]: All right, so the last thing is that you will receive a couple of documents.

**Speaker_01** [10:30:51]: Okay.

**Speaker_01** [10:30:51]: The, and having worked in a bank, you are familiar with them, acceptable use policy, security briefing, how you can use personal devices, etc., etc.

**Speaker_01** [10:31:05]: Okay.

**Speaker_01** [10:31:05]: Okay.

**Speaker_01** [10:31:06]: All right.

---
*Backed up from MeetGeek on 2026-03-30 08:46*
