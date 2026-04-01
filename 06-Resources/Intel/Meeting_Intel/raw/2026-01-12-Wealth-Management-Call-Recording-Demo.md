# Wealth Management Call Recording Demo

**Date:** 2026-01-12
**Duration:** Unknown
**Meeting ID:** 30c23606-18fd-4b79-b328-903db80e566c

## Participants
- *Participants not listed*

### Summary

The meeting established AliOne Group's regulatory and technical constraints and refined a narrow wealth-management use case: a small outbound team must record client order conversations with ADGM-compliant storage and auditability. The vendor presented two approaches—integrating a standalone recorder with Cisco PBX or adopting a cloud softphone/contact-center solution—and demonstrated softphone features (masking, manual/automatic recording, transfer/conference). Participants discussed Teams integration, searchable metadata, transcription licensing, data retention/deletion controls, and agreed next steps: David to confirm platform choice internally and the vendor to provide integration effort estimates, licensing and pricing.

## Full Transcript

**Unknown speaker** [08:00:20]: So to them we

**David Orban** [08:00:21]: should wait for Veron?

**David Orban** [08:00:30]: Actually, yes, because I've moved

**Cigdem Kemi** [08:00:32]: the meeting so that she's available.

**Cigdem Kemi** [08:00:34]: I hope she will dial in soon because she will have the questions from a wealth management perspective, how to use the voice recording tool and she knows also like the regulatory requirements in her area.

**Cigdem Kemi** [08:00:48]: But nevertheless, we can kick off the meeting and then let me see if she will join.

**Cigdem Kemi** [08:00:54]: Otherwise we have to, you know, I have to address the questions afterwards.

**Cigdem Kemi** [08:01:00]: Hi, Veron.

**Cigdem Kemi** [08:01:02]: Hey, hi.

**Cigdem Kemi** [08:01:05]: Hello, everyone.

**Cigdem Kemi** [08:01:06]: So we can start.

**Cigdem Kemi** [08:01:08]: My name is

**David Orban** [08:01:11]: David Orban.

**David Orban** [08:01:11]: I'm head of technology and innovation, and I am looking forward to understanding more about your platform, Major, and Shweta.

**David Orban** [08:01:26]: Of course, we will have Baron ask specific questions that concern her area, as Chidam just said.

**David Orban** [08:01:40]: Before we start, is there anyone we are waiting for on your side?

**David Orban** [08:01:47]: No,

**Shweta Bhatia** [08:01:49]: David, so it's just Mayur and I who would be front-ending the conversation here.

**Shweta Bhatia** [08:01:54]: So thank you so much for talking on the time and joining the call today.

**Shweta Bhatia** [08:02:00]: While I still go through the requirement that you guys have, however, I would request if you could help us with a brief, because what I understand is that you're looking for a recording solution.

**Shweta Bhatia** [08:02:11]: But what I don't understand is the back end of the system that you're currently using.

**Shweta Bhatia** [08:02:16]: Is there any existing contacts, though you did mention that the recording solution should be able to integrate with Cisco via.

**Shweta Bhatia** [08:02:24]: and nice for that matter, but wanted to also understand that what's your current solution that you're using.

**Shweta Bhatia** [08:02:30]: I also did try to go through a Levan group just to get some perspective on what the company does.

**Shweta Bhatia** [08:02:40]: research here because one company shows that it's into real estate, which is based on Bahrain, the

**David Orban** [08:02:45]: other one.

**David Orban** [08:02:46]: Sure, don't worry, don't worry, your confusion is, is natural and I will clarify it very quickly, which will also answer your other question.

**David Orban** [08:02:58]: So AliOne Group is in the process of launching a series of non-regulated and regulated financial services headquartered in Abu Dhabi with offices elsewhere.

**David Orban** [08:03:15]: Our main website is AliOne Group.

**David Orban** [08:03:22]: where you will see nothing, only leave your email to get updated exactly because we are in the process of launching.

**David Orban** [08:03:30]: We are regulated both onshore and offshore under the ADGM offshore and under ESCA onshore.

**David Orban** [08:03:41]: And, you know, the technical aspect, we use a Microsoft stack.

**David Orban** [08:03:51]: We have important data residency requirements, and we have, of course, important auditability, record-keeping and cyber security requirements, and so on.

**David Orban** [08:04:14]: The Cisco component is not that we are relying on a Cisco stack.

**David Orban** [08:04:20]: It is simply the phone that we have on the desk.

**David Orban** [08:04:22]: That's it.

**David Orban** [08:04:24]: And with regards to the office environment where we are, and I don't know, Chidim, if you had a different experience, there is a relatively low level of technology preparedness and integration ability.

**David Orban** [08:04:45]: Just as a simple example, we said, hey, we need a voicemail to be forwarded to the email and so on and so forth.

**David Orban** [08:04:55]: And it has met significant challenges just to implement a simple thing like that, right?

**David Orban** [08:05:02]: So we don't have access, and I don't expect we would have access to a Cisco backend.

**David Orban** [08:05:10]: It is much easier, if compliant, to have VoIP numbers that ring on a computer or that using the computer to dial out than not integrating into our physical phones.

**David Orban** [08:05:33]: But this is all preliminary.

**David Orban** [08:05:35]: I would also like to return with an opening question.

**David Orban** [08:05:40]: I did send an email.

**David Orban** [08:05:43]: Sorry, please, Chidempo.

**David Orban** [08:05:46]: I would

**Cigdem Kemi** [08:05:46]: prefer that we start the demo session and we can clarify technical details after.

**Cigdem Kemi** [08:05:54]: This would be a better approach also to see if we're wrong.

**Cigdem Kemi** [08:06:00]: can use the tool like and I think you're one of the main regulatory requirements from your side, Veron is that the worst recording of every client order must happen and also must happen in ADGM physically in this physical location that means we need like a solution that we can use like everywhere

**Cigdem Kemi** [08:06:20]: you know and and also the recording is somewhere and we can have access to the recording also after two years and you know for some historical assessments etc.

**Cigdem Kemi** [08:06:35]: And I don't know if you have already clients who are in the UAE and maybe also licensed with the IFC or ADGM and our financial institutions and are using this tool.

**Cigdem Kemi** [08:06:48]: If you have market experience also in the asset management or wealth management area, it would be good when you just showcase your tool with your main features and the benefits and your service offerings.

**Cigdem Kemi** [08:07:00]: And then, yeah, we can take it from there because I think David will have, and I will have also many technical questions afterwards, but first we would like to see if it really fits the purpose and what does it look like.

**Cigdem Kemi** [08:07:15]: Sure, absolutely.

**Shweta Bhatia** [08:07:16]: So the reason of understanding your requirement other than what you have put on an email said Gumb was to so that we align and show you the customized demo rather than bringing you what we have because we do offer a lot of solutions and what nice basically does we are a cloud native contact center

**Shweta Bhatia** [08:07:35]: solution where we offer your agents to be handling customer queries on different channels could be voice as well as digital so could be voice and text channels now what you're asking for is primarily around recording that's another solution that we offer but as I said that we in this particular

**Shweta Bhatia** [08:07:56]: region especially in UAE The offering is our complete contact center solution, which comes with a recording feature by default.

**Shweta Bhatia** [08:08:04]: So currently, as I understand from David, that you guys have a PBX system on Cisco, which I'm assuming is a hard phone.

**Shweta Bhatia** [08:08:12]: But tomorrow, if at all, since you are still in pre-launch, but tomorrow post-launch, if at all you want to have your agents to be using a cloud native contact center solution where along with recording we do also help with other workforce engagement modules right so from a future ready perspective

**David Orban** [08:08:31]: just just to just to correctly shape your expectation yeah uh we don't offer retail solutions we don't we are not gonna have uh tens or hundreds of people working the phone uh so uh that guides you as well in understanding which of your solutions is a good fit.

**David Orban** [08:08:54]: So,

**Mayur Patil** [08:08:54]: okay.

**Mayur Patil** [08:08:55]: So first of all, my question from my side.

**Mayur Patil** [08:08:58]: So is it just you need a voice recording solution or you need a whole contact center solution?

**Mayur Patil** [08:09:06]: Because if we say we are going to use just Cisco, so we just need to tap the lines of the Cisco and record the calls, or is it just like, You need a new ACD where the agents would be logged into that particular soft phone to that particular cloud ACD.

**Mayur Patil** [08:09:24]: Take the calls whenever any call comes on an IVR, press one for this particular support, press two for this and the call lands to the IVR and agent picks up the call.

**Mayur Patil** [08:09:35]: Once that is done, the call is automatic recording.

**Mayur Patil** [08:09:37]: So what is like the exact year, right?

**Mayur Patil** [08:09:40]: Is it just you need the recording of the calls which is happening on the current existing system or is it like you will be taking off the Cisco phones and the agents would be logging into the cloud solution.

**Mayur Patil** [08:09:54]: My expectation

**Cigdem Kemi** [08:09:55]: is, please, should that?

**Cigdem Kemi** [08:09:57]: Okay.

**Cigdem Kemi** [08:09:58]: Maybe Varon can describe the business case and maybe it's not for a call center.

**Cigdem Kemi** [08:10:02]: We are not talking about call centers.

**Cigdem Kemi** [08:10:04]: It's really wealth management specific.

**Cigdem Kemi** [08:10:06]: Varon, please.

**Cigdem Kemi** [08:10:07]: Actually,

**Veron Shim** [08:10:09]: if you have probably worked with any private banks before, it's just about It's just recording.

**Veron Shim** [08:10:16]: It's just like, you know, assistant in the office.

**Veron Shim** [08:10:20]: Place order for the client.

**Veron Shim** [08:10:22]: And that conversation has to be recorded for future probably dispute management or any possible scenario

**Mayur Patil** [08:10:30]: that we need with that.

**Mayur Patil** [08:10:32]: So that's all we need.

**Mayur Patil** [08:10:34]: Okay, fine.

**Mayur Patil** [08:10:35]: Totally fine.

**Mayur Patil** [08:10:36]: So now it is just the voice recording which we need to focus So in order to have that voice recording.

**Mayur Patil** [08:10:42]: So right now, what I understand you are using Cisco phones.

**Mayur Patil** [08:10:45]: Am I right for doing the calls, answering the calls?

**David Orban** [08:10:50]: Is it just Cisco phones?

**David Orban** [08:10:52]: We haven't launched yet, but as of right

**Mayur Patil** [08:10:54]: now, that would be the case.

**Mayur Patil** [08:10:56]: Yes.

**Mayur Patil** [08:10:56]: That would be that the case.

**Mayur Patil** [08:10:57]: Okay, so maybe like it is not yet launched, but those will be phones which will be used would be a Cisco phones.

**Mayur Patil** [08:11:03]: So like

**David Orban** [08:11:03]: how many, no, sorry, sorry.

**David Orban** [08:11:06]: I my expectation, as I said before, that if we go to our, because we are now in a shared space, right?

**David Orban** [08:11:17]: We are in a co-working space with a given number of positions, and if we went to the IT of the co-working space and said, by the way, we need to integrate with nice, They wouldn't be able to complete the integration.

**David Orban** [08:11:36]: I don't think that is why I said even something as simple forwarding the voicemail recording to an email is representing a challenge, let alone integrating an external system right.

**David Orban** [08:11:53]: So that is why I was saying that I believe it is more likely that if we go with your solution, it will not be based on the physical phones, it will be based on the soft

**Mayur Patil** [08:12:04]: phones.

**Mayur Patil** [08:12:05]: Yes, yes, yes, yes.

**Mayur Patil** [08:12:07]: So totally yes, so but we come from more from the contact center background, like the contact center as a service, where you are talking about back office site, maybe a wealth management who are the back office users.

**Mayur Patil** [08:12:22]: who are normally taking the calls, handling the whatever the transactions are, and if there is any dispute or any compliance comes up.

**Mayur Patil** [08:12:31]: So you just go to the recording, pull out that recording, verify that, and then maybe like try to solve the dispute, right?

**Mayur Patil** [08:12:39]: So when it comes to the, that is where, like, how the voice recording solution works.

**Mayur Patil** [08:12:45]: I'm like, from my side, I've been implementing this solution, so come from an implementation side before coming into the pre-sales.

**Mayur Patil** [08:12:53]: But yeah, so that is where how the voice recording will work.

**Mayur Patil** [08:12:56]: But from the cloud solution part, it will be a totally contact center solution where you would be having an IVR in ACD or cloud ACD, where agents would be logging in with their agent's ID.

**Mayur Patil** [08:13:09]: And whenever when the call comes in, maybe to your DID number, or maybe your toll-free number, and it gets routed from your IVR to the system.

**Mayur Patil** [08:13:18]: But can we

**Cigdem Kemi** [08:13:18]: have a demo, please?

**Cigdem Kemi** [08:13:20]: Can you showcase this product?

**Cigdem Kemi** [08:13:23]: because we are talking already about the technical solution but I worry this is not the right problem we should see it also we should see the features and assess that's a good fit for us or not yes

**Mayur Patil** [08:13:37]: not a problem in showing the demo right but but first of all we also need to understand what problem we are solving if we are if you're not getting to know the what what is your problem and we are just focusing a product where you would not get like what is the problem it is getting solved then you

**Mayur Patil** [08:13:56]: will also not it is just not like just jumping in a demo show the product and it's like okay fine this is how it is right so that is

**Veron Shim** [08:14:03]: where we are very intrigued into ask more questions yeah sorry to interrupt actually it was very simple so just like what you have mentioned is the wealth management solutions we don't need toll free we don't need a call center we don't need agent to picked up so someone from the office calling the

**Veron Shim** [08:14:19]: client and the recording, that's all we need.

**Veron Shim** [08:14:23]: That's

**Mayur Patil** [08:14:24]: Okay.

**Mayur Patil** [08:14:25]: Okay, fine.

**Mayur Patil** [08:14:26]: And how many years?

**Mayur Patil** [08:14:27]: So outbound, outbound rather than inbound.

**Mayur Patil** [08:14:30]: Yeah, so whether we should call

**Veron Shim** [08:14:32]: from a hard phone or a soft phone.

**Veron Shim** [08:14:36]: So it's something that we need to figure out.

**Veron Shim** [08:14:39]: So because in the co-working space, we can't be using their phone because there's a phone given to us in the office, but we don't, we probably can't use that.

**Veron Shim** [08:14:49]: But if it's a soft phone feature, then how are we going to dial in, know, how are we going to record that using the soft phone feature?

**Veron Shim** [08:14:57]: That's probably what we need.

**Veron Shim** [08:14:58]: Okay,

**Mayur Patil** [08:14:59]: no problem.

**Mayur Patil** [08:15:02]: So I

**Shweta Bhatia** [08:15:02]: think, Veron, if I understand, so please correct me if whatever I understood from this conversation that we haven't procured the hard phones yet, but we are also open at exploring the soft phone option.

**Shweta Bhatia** [08:15:15]: Because if let's say you have your employees making calls or for example receiving internal calls as well that can be happened that can happen on soft phones as well now with soft phone solution we really don't have to think it as a contact center solution only is just a software a cloud software

**Shweta Bhatia** [08:15:33]: that we offer on which your employees could make calls it could be inbound and outbound both And apart from calls if at all they want to connect on a digital channel as well internally that's also an option available and all these calls will be recorded so basically here we're talking about two

**Shweta Bhatia** [08:15:51]: separate solutions let's say if you plan to continue with a hard work hard hard phone which is a Cisco PBX or any other then.

**Shweta Bhatia** [08:16:01]: Our recording solution comes separately and that that's when we have to integrate with your PBX asthma you'd mentioned that whatever calls are happening we have to move those calls to a recording system that's option number one though I understand the requirement for now it is 25 to 30 you know such

**Shweta Bhatia** [08:16:19]: PBX phones right now the second option if you are open at exploring looking at one complete solution which enables you to make those incoming outgoing calls internally also can be connected, as well as the calls are getting recorded by default.

**Shweta Bhatia** [08:16:36]: So that's something option two is something that we can help you with.

**Shweta Bhatia** [08:16:40]: So that's how we were just trying to ask these questions to understand what the requirement is and accordingly we make, you know, move forward in terms of what solution kind of fits with your requirement.

**Shweta Bhatia** [08:16:52]: So if you're open at exploring the soft phone option, We are more than happy to let's say set up another follow-up call, show you the demo how the recording and everything would work.

**Shweta Bhatia** [08:17:02]: But if let's say we say that okay, no, we are looking at a PBX and a separate recording solution, then yes, it might be a little challenge for this particular region.

**Shweta Bhatia** [08:17:12]: So just wanted to voice it out there.

**Shweta Bhatia** [08:17:16]: And

**David Orban** [08:17:16]: Veron, do you confirm what Shretta said that you would need people calling our clients?

**David Orban** [08:17:26]: I think that's

**Veron Shim** [08:17:27]: what I on the email, right?

**Veron Shim** [08:17:29]: But not at the moment.

**Veron Shim** [08:17:31]: I mean, of course, like what David had shared that the company still starting.

**Veron Shim** [08:17:36]: So we are looking at, I mean, a small team that will handle these calls with the client for now.

**Veron Shim** [08:17:44]: So it wouldn't be anything that 1020, probably to be just going to be like, you know, three to five for start.

**Veron Shim** [08:17:52]: Not not that numbers yet Okay, fair

**Shweta Bhatia** [08:17:58]: enough.

**Shweta Bhatia** [08:17:59]: So once we have a clarity in terms of which option we are comfortable with if it's a software.

**Shweta Bhatia** [08:18:04]: So

**David Orban** [08:18:05]: let's assume since you said that that with the hard phones, you would have a hard time delivering a solution in the region.

**David Orban** [08:18:13]: That is what I understand.

**David Orban** [08:18:14]: There is no choice to be made.

**David Orban** [08:18:17]: there is no need to reschedule the call.

**David Orban** [08:18:19]: Please show us your software solution because I think we answered all your questions.

**David Orban** [08:18:24]: Okay, okay, fair enough.

**Veron Shim** [08:18:26]: We are still the company is building up so it's very fluid.

**Veron Shim** [08:18:30]: So we could be moving from office to another office and do not know.

**Veron Shim** [08:18:35]: So I think having the soft phone features probably works better when it comes such situation, because we might be right not might not be using this co-working space, we might be moving, you know, we do not know when.

**Veron Shim** [08:18:48]: So we don't want and all these features being interrupted when sight happens.

**Veron Shim** [08:18:55]: So I think software might be a better idea.

**Veron Shim** [08:18:57]: Fair enough,

**Shweta Bhatia** [08:18:58]: fair enough.

**Shweta Bhatia** [08:18:59]: Mayu, would we be able to show something on the platform just to put things into perspective?

**Shweta Bhatia** [08:19:05]: Yeah,

**Mayur Patil** [08:19:05]: just let me see if I can pull up something.

**Mayur Patil** [08:19:15]: Maybe

**Veron Shim** [08:19:15]: you can share also how does it work when we actually make call or receive call, how does it work?

**Veron Shim** [08:19:23]: Yeah, sure.

**Veron Shim** [08:19:25]: You can give them your phone number and they should call and they should call you call.

**Veron Shim** [08:19:32]: Yeah, sure.

**Veron Shim** [08:19:34]: You can give

**David Orban** [08:19:34]: them your phone number and they should call

**Mayur Patil** [08:19:39]: No, so that's all right.

**Mayur Patil** [08:19:41]: So right now it will be just a demo environment.

**Mayur Patil** [08:19:45]: yeah so can i can try out where just let me see so this is the nice cx1 nice cx1 agent which i'm trying i'm right now logging so basically

**Veron Shim** [08:19:59]: this is the software that we are mostly talking about international call because yeah

**Mayur Patil** [08:20:05]: yeah so so this is the options first of all we need to select which it integrated software and we need once you launch so are logged in to the CX1 agent once you are logged in you have different status where you can put yourself on maybe different codes on available break lunch right so once you put

**Mayur Patil** [08:20:36]: on available so i'll just try to dial out any call Maybe you can give your number.

**Mayur Patil** [08:20:42]: I can just dial it out your number.

**Mayur Patil** [08:20:44]: Actually,

**Veron Shim** [08:20:45]: I'm not using my phone now for the video call, so it might not be convenient.

**Veron Shim** [08:20:49]: Okay.

**Veron Shim** [08:20:50]: You

**Shweta Bhatia** [08:20:50]: can dial my number.

**Shweta Bhatia** [08:20:51]: I'll put down my number here.

**Shweta Bhatia** [08:20:53]: One second.

**Shweta Bhatia** [08:20:56]: If not, then I can just dial out my number.

**Mayur Patil** [08:21:01]: So this is my.

**Mayur Patil** [08:21:04]: I'm just dialing it out.

**Mayur Patil** [08:21:14]: Thank you,

**Cigdem Kemi** [08:21:30]: Do I understand correctly the client will have also access to use this tool or to dial the number of veron, for instance, to place orders or how does it work?

**Veron Shim** [08:21:41]: The client is just receiving calls on their normal mobile They wouldn't be.

**Veron Shim** [08:21:47]: Yeah.

**Mayur Patil** [08:21:50]: We hit a second just let me see some issue.

**Mayur Patil** [08:22:02]: So

**Shweta Bhatia** [08:22:03]: we generally on our first call kind of do a discovery call where we understand what the requirement is because as I said there are a lot of solutions that we offer and then post which as a second call is when we show you the demo I think Mayur is trying to kind of fix his demo environment right now

**Shweta Bhatia** [08:22:20]: to make that call for you so bear with us for another 60 seconds.

**Shweta Bhatia** [08:22:24]: Yeah.

**Shweta Bhatia** [08:22:25]: Are you guys all based out of Dubai or Abu Dhabi?

**Shweta Bhatia** [08:22:28]: Abu Dhabi.

**Shweta Bhatia** [08:22:30]: Abu Dhabi.

**Shweta Bhatia** [08:22:32]: Yeah.

**Shweta Bhatia** [08:22:33]: Yeah, because we are

**Veron Shim** [08:22:34]: ADGM license entity, so all calls and activities, license activities that we done from ADGM itself.

**Veron Shim** [08:22:43]: okay, understood.

**Veron Shim** [08:23:09]: Okay.

**Shweta Bhatia** [08:23:36]: Why don't you want to walk them through the features that we have on the soft phone from where, yeah.

**Mayur Patil** [08:23:42]: Yeah, just second.

**Mayur Patil** [08:23:43]: I haven't yet to receive a call.

**Mayur Patil** [08:23:51]: Okay.

**Mayur Patil** [08:23:55]: Okay.

**Mayur Patil** [08:24:04]: So, This is the call initiative, right?

**Mayur Patil** [08:24:07]: So I have received the call on my mobile.

**Mayur Patil** [08:24:11]: So this is how like the soft phone would look like right.

**Mayur Patil** [08:24:13]: These are the soft phone controls which are available where you can put yourself on hold, mute.

**Mayur Patil** [08:24:21]: If any point of a time you want to mask, right?

**Mayur Patil** [08:24:23]: So basically mask is a feature where you want to mask any sensitive information, right, in the call when the customer is speaking, right?

**Mayur Patil** [08:24:33]: maybe some sharing some credit card details or something like that right any sensitive information which needs to be shared so agent can do it themselves right they can have the control to mask so what will happen in the voice recording that particular words or that particular numbers would be

**Mayur Patil** [08:24:53]: masked it will be a white noise kind of a white noise inside the recording so that will not captured so Other than that, there is option for you can do manual record or you can have an automated recording, right?

**Mayur Patil** [08:25:09]: So like a recording on demand kind of a feature, right?

**Mayur Patil** [08:25:11]: So if an agent wants to do a recording on demand, he can just do it by clicking this record or otherwise you can, it is like a 100% recording, a rule has to be created in the back end and that particular rule can be configured for that particular agents in the team and the call will be recorded

**Mayur Patil** [08:25:29]: automatically.

**Mayur Patil** [08:25:30]: other feature like the transfer or the consult right or the conference part where you would you can either transfer the call or bring in by dialing out the number and you can conference if any third party if it is needed right you can do so you can have conference have transfer inside the system So

**Mayur Patil** [08:25:51]: yeah, so basic, these are all the kind of basic features which I would say from a software perspective, nothing much when it comes to since your requirement is just for the voice recording.

**Mayur Patil** [08:26:03]: But yes, as a platform from CX1 side, here in this, we are more into the contact center platform where agents not only just handle the voice call, but in the same environment, they can also handle the chat, right?

**Mayur Patil** [08:26:19]: if any chat related query if any inquiry if any comes in right from your website And if it needs to be routed to the agent or maybe to the user to handle it, and maybe it might be some business lead or which needs to be act upon where an opportunity is there for and sell, right?

**Mayur Patil** [08:26:35]: So you can handle that omni-channel, you can get that omni-channel agent-wise

**David Orban** [08:26:39]: experience as well.

**David Orban** [08:26:40]: Yeah.

**David Orban** [08:26:41]: Major, I came into this call a bit late and I only asked some questions on email very late too.

**David Orban** [08:26:52]: So, so forgive me, based on your experience, and from what you understand, Varon described, of a small number of people making outbound calls in a Microsoft-based environment where software phones are fine.

**David Orban** [08:27:10]: What stops us from using Teams and Teams recording to generate a compliant tenant-based ACS

**Mayur Patil** [08:27:20]: stored Right, you can use you can use teams, we can record teams

**David Orban** [08:27:26]: Okay, but that's my point.

**Mayur Patil** [08:27:29]: We can go ahead and record it ourselves, right?

**Mayur Patil** [08:27:32]: No, okay, so so okay, so when you are recording, right, so that is basically getting stored you will not be able to search.

**Mayur Patil** [08:27:40]: It is getting stored on OneDrive for that particular interaction.

**Mayur Patil** [08:27:43]: You

**David Orban** [08:27:44]: will not get the metadata.

**David Orban** [08:27:46]: That's that's another question.

**David Orban** [08:27:48]: Yeah, so that is where that is where the

**Mayur Patil** [08:27:49]: platform voice recording platforms comes into picture where you will see the start time stop time.

**Mayur Patil** [08:27:54]: The metadata, the calling number, call party number, right?

**Mayur Patil** [08:27:57]: So that is where the voice recording platform comes into which which records your team call.

**Mayur Patil** [08:28:02]: Yeah, I know that teams have a default feature of recording itself, but you will not be able to find the exact recording when it was there.

**Mayur Patil** [08:28:11]: who what it was where like maybe the calling number what was it right so you will not be having those details it is just like when it is getting stored in the one drive it is some segment id and thank

**Veron Shim** [08:28:24]: yeah thank you see them i think we require the client to also using teams right for to receive the no

**David Orban** [08:28:32]: no teams teams can make calls to normal phones phone oh okay

**Mayur Patil** [08:28:37]: yeah yeah so teams teams do have that feature when it comes to call the any maybe any number right you can directly basically it is just just assume it as a simple soft phone that should just instead of also it is a collaboration like calling in between the users internally otherwise you can also

**Mayur Patil** [08:28:58]: call it externally also when you have a team's which gives you the flexibility

**Cigdem Kemi** [08:29:03]: yes my questions actually do you offer also an app for instance i assume now that Veron will make the calls from her mobile phone, from her iPhone, and then she would simply just open the app on iPhone and dial in the client's number, and then it will be per default recorded.

**Cigdem Kemi** [08:29:23]: This is like kind of solution that we are looking for, and Veron, please correct me if I'm and then she can maintain the recorded in a specific section or in a workspace, all the recorded calls and maintain them added or moved to another storage, etc.

**Cigdem Kemi** [08:29:43]: You know, like some usability that is provided would be also better and different than what we can do in Microsoft Teams, because when it comes to just simple calls, as already mentioned, we know the Microsoft Teams features, but we are looking something specific for wealth management and something

**Cigdem Kemi** [08:30:04]: that can also be used by David, for instance, when he has important calls that he wants to transcribe

**Veron Shim** [08:30:10]: okay so I mean if that's available it's fine but however mean we can use that for other purposes but for can order placing I think in order to fulfill the compliance requirement it has to be shown that is done in ADGM itself then I mean, having an app when you make call from anywhere, everywhere

**Veron Shim** [08:30:35]: part of everywhere in different part of world to the client may not need that requirement that I mean, as in the call is placed out of ADGM.

**Veron Shim** [08:30:47]: So yeah, so I'm not sure whether that will be something that is that for this purpose itself for the client

**David Orban** [08:30:57]: and and and and with regards to the second remark that she then made the mayor I assume that We have meet geek transcribing the call that we are having right now.

**David Orban** [08:31:14]: You are not offering similar features where meeting would be recorded on teams or zoom or or or in other platforms and then transcribed.

**David Orban** [08:31:28]: Am I correct?

**Mayur Patil** [08:31:31]: Right, so it will not it is so basically if it is integrated with the team so that is the only channel it will not be integrated to any other zoom or something else

**David Orban** [08:31:40]: but but even even on teams you do not offer voice to text do no

**Mayur Patil** [08:31:47]: no so so it it it I I need to check that but what I know that we don't do the week we can do that but right now see basically it is part right for us doing transcription also you need license.

**Mayur Patil** [08:32:01]: It is just not getting enabled by default.

**Mayur Patil** [08:32:05]: In order to run some analytics on the call.

**Mayur Patil** [08:32:07]: So if you do need to do some transcription on the maybe the speech to text, it is just not by default.

**Mayur Patil** [08:32:14]: You have to enable that particular license.

**Mayur Patil** [08:32:16]: If it is needed, then

**Cigdem Kemi** [08:32:17]: only it will be done.

**Cigdem Kemi** [08:32:18]: That's fine.

**Cigdem Kemi** [08:32:18]: The license acquiring the license is fine.

**Cigdem Kemi** [08:32:20]: We just won't understand.

**Cigdem Kemi** [08:32:21]: Is it possible with this tool to get these features?

**Cigdem Kemi** [08:32:25]: Do you offer these services?

**Cigdem Kemi** [08:32:29]: Okay, and also another question is from a security perspective.

**Cigdem Kemi** [08:32:33]: Is it possible that we're on after recording her calls, can delete it, remove it from your particular cloud service and move it to her device or to her storage, because we highly regulated and we cannot leave the client conversation in your

**Mayur Patil** [08:32:52]: Yes, we can we can do that.

**Mayur Patil** [08:32:54]: So deletion of the call and maybe the maintaining the retention, right?

**Mayur Patil** [08:32:59]: So if you need that particular retention, we can configure that retention on that particular environment by using the rules and the calls will be deleted.

**Cigdem Kemi** [08:33:10]: So we will have to full power over data.

**Cigdem Kemi** [08:33:13]: Yeah,

**Mayur Patil** [08:33:13]: yeah, 100%, 100%, 100%.

**Mayur Patil** [08:33:15]: So the main now the main thing is that, right?

**Mayur Patil** [08:33:19]: So we just need to first.

**Mayur Patil** [08:33:22]: very much be clear what we will be is it teams is it hard phones or is it soft phones like we because if it is a teams it is like very similar solution right we just don't need to complicate things right teams is there already it is just our voice recording solution coming plug-in integration no

**Mayur Patil** [08:33:48]: nothing much complex right we just need to be very much clear at what agents has to it a team's phone is it a because teams is also a soft one so or is it us yeah if it is a Cisco hard phones or what so basically we'll have to first finalize and accordingly the next part right we because see that

**Mayur Patil** [08:34:10]: there are now multiple iterations have happened right softphone teams then there is Cisco was mentioned so we have to be very clear now so because in order to for me to finalize the solution also right it has to be very clear how many agents we are talking about

**David Orban** [08:34:26]: we will of course discuss it internally and then send you an email yeah but I think it is pretty clear we are not going to use Cisco It in my opinion, most likely that we will use teams to make the calls.

**David Orban** [08:34:40]: Yeah.

**David Orban** [08:34:41]: Yeah.

**David Orban** [08:34:42]: And that we will start with three to five licenses, as Vero said.

**Mayur Patil** [08:34:53]: it.

**Mayur Patil** [08:34:54]: Okay.

**Mayur Patil** [08:34:54]: So because the teams is, I see that you have already made your investment.

**Mayur Patil** [08:34:57]: It might be there, right?

**Mayur Patil** [08:34:58]: The team's roles are already there.

**Mayur Patil** [08:35:00]: So you don't have to.

**Cigdem Kemi** [08:35:01]: So I have a question.

**Cigdem Kemi** [08:35:03]: Can we have a trial version at least five days so that we're on and David can test and see the usability and the benefits.

**Cigdem Kemi** [08:35:13]: And then we can have another follow-up discussion with more details.

**Cigdem Kemi** [08:35:17]: We could try, you know, they could have it maybe enabled in a team, Microsoft Teams, and we could have like a couple of these testing versions.

**Cigdem Kemi** [08:35:28]: I think

**Shweta Bhatia** [08:35:28]: for recording on Microsoft Teams, we would require integration as well.

**Shweta Bhatia** [08:35:32]: Without integration, obviously the trial would not work.

**Shweta Bhatia** [08:35:36]: And I'm not too sure how invested your team or our team would be doing those integration at a primary stage where the requirement is just for five agents, right?

**Shweta Bhatia** [08:35:45]: So because it requires effort.

**Shweta Bhatia** [08:35:47]: So I'm not sure of

**Cigdem Kemi** [08:35:48]: that very.

**Cigdem Kemi** [08:35:50]: Do you have any browser version that we can No, no, we don't have

**Cigdem Kemi** [08:36:00]: So

**David Orban** [08:36:01]: let us know.

**David Orban** [08:36:01]: So I have to go.

**David Orban** [08:36:03]: We scheduled the call for half an hour.

**David Orban** [08:36:05]: Yeah, we are.

**David Orban** [08:36:09]: And I don't have this time additional questions.

**David Orban** [08:36:13]: So we will confirm what I listed or with some changes eventually on an email.

**David Orban** [08:36:21]: And then you can send us an estimate of the engineering required for the integration and the licenses and on.

**Shweta Bhatia** [08:36:29]: Sure.

**Shweta Bhatia** [08:36:30]: Yeah, we'll be.

**Shweta Bhatia** [08:36:31]: And the

**Cigdem Kemi** [08:36:31]: pricing, please.

**Cigdem Kemi** [08:36:32]: Yeah.

**Cigdem Kemi** [08:36:33]: If you can share our service offering with the price tag, it would good.

**Veron Shim** [08:36:37]: Yeah.

**Veron Shim** [08:36:38]: Sure.

**Veron Shim** [08:36:39]: Thank you very much.

**Veron Shim** [08:36:39]: Bye-bye.

**Veron Shim** [08:36:40]: Thank you.

**Veron Shim** [08:36:40]: Thank you.

**Veron Shim** [08:36:42]: Thanks.

**Veron Shim** [08:36:42]: Bye.

---
*Backed up from MeetGeek on 2026-03-30 08:49*
