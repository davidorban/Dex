# Quantum Key Distribution Demo

**Date:** 2026-02-09
**Duration:** Unknown
**Meeting ID:** c7099f46-ce8c-442a-8d04-1df34e962643

## Participants
- *Participants not listed*

### Summary

The presenter introduced a multi-organization collaboration to deploy quantum key distribution (QKD) for long-term data security, framing the problem of stored encrypted data being vulnerable to future compute advances. He described an entanglement-based three-node QKD prototype, system components (entangled source, receivers, switch), a dashboard showing key provisioning and QBER tripwires, and stressed compatibility with classical encryption layers. Use cases emphasized healthcare, data centers and critical infrastructure; blockchain and digital asset risks were discussed. The talk covered cost drivers (single-photon receivers), planned cost-reduction approaches (last-mile transmitters, photonic chips), regulatory drivers in the UAE, complementarity with post-quantum software approaches, AI’s potential impact on cryptanalysis, and planned upgrades to key management and integrations for broader application access.

## Full Transcript

**Speaker_03** [08:06:09]: So

**Unknown speaker** [08:06:16]: just

**Speaker_03** [08:06:16]: a

**Speaker_03** [08:06:21]: quick introduction to the sort of collaboration initiative we have.

**Speaker_03** [08:06:23]: That's my job, which is, there's five entities involved in EGM, which are an ATM line right in, Pub 71, where we are now.

**Speaker_03** [08:06:27]: And of course, it's fine.

**Speaker_03** [08:06:27]: Well, my one is from part of the EGRC, part of that, but that means technology umbrella.

**Speaker_03** [08:06:29]: Inspire the ones who sort of broke it all and instead of guys and sort of put together technology programs and so on.

**Speaker_03** [08:06:32]: So we had a signing ceremony last year, and I'm sure we have to put 10 words together.

**Speaker_03** [08:06:40]: So it's been in place for a few months now.

**Speaker_03** [08:06:42]: It's been operational in these buildings.

**Speaker_03** [08:06:43]: But I guess the whole point of this was to try and see if there's interesting use cases, maybe

**Unknown speaker** [08:06:48]: for the finance sector may not.

**Speaker_03** [08:06:49]: kind

**Speaker_03** [08:07:03]: of open to any ideas.

**Speaker_03** [08:07:03]: And if anyone during this talk or the end of this talk has any ideas, the things we would like to try and attend.

**Speaker_03** [08:07:05]: There's a QR code and a spelled out of an English link, which you can visit the details in.

**Speaker_03** [08:07:07]: It's kind of a digital version of putting your business card in a handover, right?

**Speaker_03** [08:07:09]: So somebody from our team will get in touch with anybody to hear that.

**Speaker_03** [08:07:10]: The QR code turns up again later on, of course.

**Speaker_03** [08:07:11]: So, I'm going to frame the context a little bit and say this is about security, it's about sort of long-term security.

**Speaker_03** [08:07:17]: And the problem statement, which may or may not affect people in this room, is to do with the challenge of maintaining security of confidential information over a very long period of time.

**Speaker_03** [08:07:29]: Maybe familiar with this picture on the right hand side.

**Speaker_03** [08:07:33]: I was talking this one from the Canadian Center for Cybersecurity, but many, many organizations have used several variations of this.

**Speaker_03** [08:07:45]: And it gives

**Unknown speaker** [08:07:46]: a very general overview

**Speaker_03** [08:07:46]: of how security foundations works.

**Speaker_03** [08:07:48]: Typically, you'll have two authorized send your own receiver.

**Speaker_03** [08:07:49]: And it's called

**Unknown speaker** [08:07:50]: Alice in Vault by

**Speaker_03** [08:07:50]: cryptographers, and you'll see.

**Speaker_03** [08:07:51]: And now this sends some secret material to model.

**Speaker_03** [08:07:52]: So Alice is represented by the

**Unknown speaker** [08:07:53]: kind of green puzzle.

**Unknown speaker** [08:07:55]: is a crypto and as well with the only audience you can really read some information so so far

**Speaker_03** [08:08:09]: But she can make the recording, so she can take a copy of the equipment that doesn't.

**Speaker_03** [08:08:12]: And she can also make a copy of all other information that travels back and forth between us.

**Speaker_03** [08:08:16]: But this might include metadata and session data in which cryptographic keys are generated.

**Speaker_03** [08:08:21]: So she has a record of all of this, basically.

**Speaker_03** [08:08:24]: And she can store this information.

**Speaker_03** [08:08:26]: And you guys may be aware, storage is very cheap.

**Speaker_03** [08:08:29]: You get very durable, very cheap storage.

**Speaker_03** [08:08:30]: It's more or less unlimited.

**Speaker_03** [08:08:31]: So there's not really any practical limits.

**Speaker_03** [08:08:34]: of Eve can store.

**Speaker_03** [08:08:36]: So it's not a very high cost activity for you.

**Speaker_03** [08:08:38]: So we should assume that whenever you send anything over

**Unknown speaker** [08:08:41]: to any public accessible network, or even a private network, it's probably being recorded somewhere.

**Unknown speaker** [08:08:46]: It's something encrypted, so you're fine, right?

**Unknown speaker** [08:08:47]: But that encrypted data is recorded by anybody.

**Speaker_03** [08:09:00]: to this

**Unknown speaker** [08:09:05]: point where it's sufficiently powerful what kind of abuse do they exist.

**Unknown speaker** [08:09:11]: Sounds like no one might happen to say, what might

**Speaker_03** [08:09:13]: be sufficiently powerful to do?

**Speaker_03** [08:09:14]: Well,

**Unknown speaker** [08:09:15]: one of the problems

**Speaker_03** [08:09:15]: we have with pretty much something like 80% of cryptography that we use today or 80%

**Unknown speaker** [08:09:18]: of our abuse cases are making use of at some point either RSA or

**Speaker_03** [08:09:20]: Diffie-HGF.

**Speaker_03** [08:09:20]: And these

**Unknown speaker** [08:09:21]: are vulnerable to chronic pain.

**Unknown speaker** [08:09:22]: There's an algorithm that will run a

**Speaker_03** [08:09:23]: show of sufficient large quantity here, which will be able to decrease these kind of relevant quantity, you know, that's a lot of people use.

**Speaker_03** [08:09:35]: Coming into existence is at what makes two years.

**Speaker_03** [08:09:37]: And then from that point onwards, the adversary, Eve can decrypt all the stuff that she's been stored for many years.

**Speaker_03** [08:09:43]: So this becomes a problem with the stuff that you're transmitting has a secure lifetime that goes past that point.

**Speaker_03** [08:09:47]: So that's this red period, right?

**Speaker_03** [08:09:48]: So they like you to imagine you have some data, it has value after that point, and it's now publicly available after that point, so this should be a problem, right?

**Speaker_03** [08:09:57]: And this makes, you know, thinking about cryptography a present-day concern, because even though we think that the way we're transmitting information today is probably secure against the kind of news we have today, we know that it will be secure at this difficult to predict point in the future.

**Speaker_03** [08:10:10]: We also know that the world is spending like, I think we're up to hundreds of billions of years, and there's some very large, very serious efforts going on to create a business machine.

**Speaker_03** [08:10:26]: So at this point, to ignore that is to kind of bet against people like IBM and Google and Microsoft.

**Speaker_03** [08:10:29]: Companies that have a pretty good track record of not failing to build computers, right?

**Speaker_03** [08:10:32]: if we expect it to fail at this time.

**Speaker_03** [08:10:34]: It feels like a very strange account.

**Speaker_03** [08:10:36]: So this is a motivation for why we're thinking about long-term security.

**Speaker_03** [08:10:42]: And I also want to highlight that quantum computers, when they're scaled up, this is really the best case scenario for conventional cryptosystems.

**Speaker_03** [08:10:48]: It's entirely possible that some other kind of computer technology would come on before that, and the government should say, break RSA.

**Speaker_03** [08:10:54]: We have no evidence, no, sorry, a lot of evidence go, no proof that the mathematical appendix of RSA to the argument are secure against laptops.

**Speaker_03** [08:11:01]: We just believe that their experience not breaking the schemes, or sorry, breaking the underlying mathematics, but that doesn't mean it can be done, so we should worry about this.

**Speaker_03** [08:11:09]: I've highlighted large-scale artificial intelligence platforms, so I think that's actually meaningful here.

**Speaker_03** [08:11:13]: It is possible that somebody can brute force factor or discrete logarithm.

**Speaker_03** [08:11:18]: And if it turns out that there is an efficient algorithm for accomplishing these tasks, then that's an instant collapse of most of our crypto systems and we have a problem of.

**Speaker_03** [08:11:24]: So that's the context.

**Speaker_03** [08:11:26]: Good news is we have ways to fix this, right?

**Speaker_03** [08:11:28]: So you may have heard of post-monum cryptography.

**Speaker_03** [08:11:30]: I'm not going to talk about that.

**Speaker_03** [08:11:31]: That's not my thing, but that is a software upgrade which is the most likely same thing with software computers, and which we should all take very seriously.

**Speaker_03** [08:11:38]: So I don't need to say that's not important.

**Speaker_03** [08:11:40]: My assumption is that's going on, and we take all of that into the purpose of this talk.

**Speaker_03** [08:11:44]: But I want to think about symmetric cryptosystems, right?

**Speaker_03** [08:11:46]: So this is a system where you encrypt and decrypt using the same CPU key.

**Speaker_03** [08:11:50]: And these systems are typically very durable.

**Speaker_03** [08:11:57]: In fact, also thought to be durable against quantum computers.

**Speaker_03** [08:12:01]: But the challenge is that you need to have a copy of the secret key that's kind of only a symbol, but not any third one.

**Speaker_03** [08:12:06]: And so accomplishing that key generation is actually the way more than the challenge in these systems.

**Speaker_03** [08:12:09]: It's what Diffie-Hellman does, right?

**Speaker_03** [08:12:10]: Diffie-Hellman gives you a way to create secure keys into remote locations, just by communicating, right?

**Speaker_03** [08:12:13]: Publicly.

**Speaker_03** [08:12:13]: That's the problem being that that's based on some of that bad assumptions.

**Speaker_03** [08:12:16]: So it turns out you can use quantum physics or you can use the laws of quantum physics to accomplish exactly this key exchange.

**Speaker_03** [08:12:24]: And so that's the part which we propose to upgrade.

**Speaker_03** [08:12:26]: So from now on, I'm going to talk about secure communication.

**Speaker_03** [08:12:29]: The security and encryption is not normal.

**Speaker_03** [08:12:31]: That's just conventional AES type encryption.

**Speaker_03** [08:12:33]: What's quantum is the key, right?

**Speaker_03** [08:12:35]: How we generate this key and how we distribute this code.

**Speaker_03** [08:12:40]: with one of the key distribution, the aim of the technology that we have to discuss.

**Speaker_03** [08:12:46]: And should be well as consistent, right?

**Speaker_03** [08:12:47]: Depending on how modern the encryption library is, it's its own example, right?

**Speaker_03** [08:12:52]: But yeah, so you're here, sometimes your photo is quantum cryptography.

**Speaker_03** [08:12:54]: A bit of a misnomer, because the cryptography is not quantum, but the key distribution is quantum, and so that's what we should focus on.

**Speaker_03** [08:12:58]: Okay, in Abu Dhabi and in TII, we were founded about five years ago, so my team has spent the last five issues working on this problem, and we've used some solutions that accomplished one of the key distribution.

**Speaker_03** [08:13:12]: In particular, the photograph on the right is our prototype QKE system that's based on quantum entanglement.

**Speaker_03** [08:13:16]: Problem is not to go into too much detail about that, but I'm happy to go afterwards.

**Speaker_03** [08:13:20]: And this is what we deploy here in ADGM, so we have this prototype QKE system.

**Speaker_03** [08:13:22]: We also have upstream solutions that are mastermind, right?

**Speaker_03** [08:13:25]: So one of the common objections you're going to get to keep the heat is that it's quite expensive, it requires quite exotic hardware, but we are working with this.

**Speaker_03** [08:13:31]: So there will be a second half of this year, we should have something at a CAD engineering prototype level, which is a cost-connected version of this.

**Speaker_03** [08:13:38]: So when thinking about possible use cases of very strict communication, the cost figure can change over time or change over time.

**Speaker_03** [08:13:45]: So please don't let that be a huge variant today.

**Speaker_03** [08:13:46]: But yeah, we're able to build sort of large room networks using our entangled base system.

**Speaker_03** [08:13:51]: Now we have to be able to build kind of switch-based solutions that are plausibly accessible to say SMEs or branch networks in the in the near future.

**Speaker_03** [08:13:59]: And that's where we are here today.

**Speaker_03** [08:14:00]: The systems are compatible with many, many, many existing classical encryption layers.

**Speaker_03** [08:14:06]: For example, ABVAC and Jimbo 14-Thundlers in a few hours.

**Speaker_03** [08:14:09]: So most of these guys have implemented a 10 API that was defined by ETSI.

**Speaker_03** [08:14:13]: So there is a standard that's a relevant standard, which we have used to distribute keys to those devices.

**Speaker_03** [08:14:19]: And in terms of the actual solution which we have to deploy in a GKM, it's comprised of two main pieces.

**Speaker_03** [08:14:24]: Therefore, keep getting a receiver.

**Speaker_03** [08:14:26]: That's the device that generates keys.

**Speaker_03** [08:14:28]: And so every user needs to have one of these devices.

**Speaker_03** [08:14:30]: And there's an entanglement circuit which connects pairs of devices using entangled photon pairs.

**Speaker_03** [08:14:41]: Photon and where is technical jar and it's a particle monitor.

**Speaker_03** [08:14:48]: So all of this technology Okay, a very rough cartoon of what we did.

**Speaker_03** [08:14:53]: We built a three-node network.

**Speaker_03** [08:14:55]: So we're currently here on Hub 71. That level is supposed to be the 15th floor.

**Speaker_03** [08:14:59]: And then we have also a node in ADGem County and a node down from the ADGem Authority building.

**Speaker_03** [08:15:03]: So it's a three-node network.

**Speaker_03** [08:15:06]: It looks kind of like this, so feel free of media.

**Unknown speaker** [08:15:12]: and are the ghosts and receivers that meet photons and produce the keys.

**Unknown speaker** [08:15:16]: So we have three receivers, one source, and a

**Speaker_03** [08:15:18]: switch.

**Unknown speaker** [08:15:19]: And

**Speaker_03** [08:15:20]: the switch tracks each pair of receivers, the sequence one after the other.

**Speaker_03** [08:15:24]: And so you can sort of think of the ghosts and the switch.

**Speaker_03** [08:15:27]: Those are kind of shared resources on them.

**Speaker_03** [08:15:30]: to add more nodes to this network, we would just have to add more of this sort of receiving to the background.

**Speaker_03** [08:15:37]: So yeah, we have a start-type switch-based network with the key key layer, and that then provides keys onto a network.

**Speaker_03** [08:15:41]: Some of these things sort of force-net devices.

**Speaker_03** [08:15:42]: Force-net devices produce a logical network thing used in Toronto.

**Speaker_03** [08:15:45]: That's also three nodes, but it's actually The keys are generated between any pair of devices.

**Speaker_03** [08:15:51]: And so this quantum guarantee, which is the representative of the black solid line that can kind of go around it, that quantum guarantee exists between each pair.

**Speaker_03** [08:15:57]: So even though the data physically travels from this building through the authority's building and up to the academy's building, they're linked directly with this quantum key.

**Speaker_03** [08:16:06]: So there is no way, even in principle, for somebody in the middle of the

**Unknown speaker** [08:16:08]: room to grip that definition.

**Speaker_03** [08:16:09]: So this kind of any connectivity is an emotional link you can, and we're quite proud of that slight differentiated networks to accomplish these kinds of technical based approach.

**Speaker_03** [08:16:19]: Again, I'm sorry, I'm telling you these are, I like this work.

**Speaker_03** [08:16:22]: But yeah, that's also potentially very interesting to use case points of view, because it means you can imagine pushing things around such a network where it would seem to be shadowed in the center to the three different locations of storage.

**Speaker_03** [08:16:29]: There's no way even in principle that an unauthorized policy on this network of course is encrypted information.

**Speaker_03** [08:16:36]: That's the center between the end of the two months.

**Speaker_03** [08:16:38]: Again, the locations, of course, they're something like the HTML and the HTML code.

**Speaker_03** [08:16:42]: How does this work?

**Speaker_03** [08:16:43]: From a user point of view, so we provision the keys onto an IPsec network, this query server that's called layer 3. This

**Speaker_03** [08:16:56]: is the OSI network side.

**Speaker_03** [08:16:59]: So you have a sort of physical data network transport session, presentation application line.

**Speaker_03** [08:17:08]: Most of us interact with the application layer on a day-to-day basis.

**Speaker_03** [08:17:09]: But further down, the network theory said, I think 100 years ago, and that provides secure tunnels between different points in the network.

**Speaker_03** [08:17:13]: And that's where the points of keys are being sort of huge.

**Speaker_03** [08:17:14]: So all the data that travels on the network is protected that way.

**Speaker_03** [08:17:15]: And so if you wanted to do some demo on this network and want to be secure, everything traveling within the network, not within the network, it's anything between APIs on their network would be protected at that low lane.

**Speaker_03** [08:17:22]: But that's not very interesting.

**Speaker_03** [08:17:25]: So we also have this option.

**Speaker_03** [08:17:27]: So you can also make applications which directly access the key.

**Speaker_03** [08:17:30]: So this API is used to be very well documented over here by ETSI, allows you to directly use something that's like a REST-like API, apparently it might.

**Speaker_03** [08:17:39]: It's also organized as an actual REST API, it's where it's like, I don't know if you use that API.

**Speaker_03** [08:17:43]: But apparently if you use that API, you can request the keys directly and the devices and they're using

**Speaker_03** [08:17:52]: different place well to make sure if there are any single mx and they do quite a bit of things so they've created a bunch of test applications to try and transaction is there directly in the bottom here and that's supporting this level okay I'm going to skip straight over the slide and let's say if

**Speaker_03** [08:18:10]: you guys are already hard-warned with people I even profess to not understand you about 30 months off but this is the detail of how the things are important I think it's really comes to be able to be, that's the part that you're going to interact with.

**Speaker_03** [08:18:22]: And I wanted to show you a live dashboard with how this thing works, how it works in practice.

**Speaker_03** [08:18:25]: Unfortunately, there appears to be a network latency on the classical network, so it's on the phone.

**Speaker_03** [08:18:28]: This is the regular one, always a problem, right?

**Speaker_03** [08:18:30]: Which prevents me from showing you live dashboard, but if I could, it would look better than this, right?

**Speaker_03** [08:18:33]: So I'll draw attention to the top section, that's the key So you can see each pair of loans is being provisioned

**Unknown speaker** [08:18:40]: sort

**Speaker_03** [08:18:40]: of one

**Unknown speaker** [08:18:41]: at a

**Speaker_03** [08:18:41]: time, one pair at

**Unknown speaker** [08:18:45]: a time.

**Unknown speaker** [08:18:45]: And you see we can play with the schedule so we can change all the metrics are there, let's switch between.

**Unknown speaker** [08:18:48]: In this case, we

**Speaker_03** [08:18:49]: were trying to balance the amount of key that each pair of loans had between it.

**Speaker_03** [08:18:52]: And so you see the worst pair was pair four and five at the bottom.

**Speaker_03** [08:18:56]: That had the lowest key rate, so we spent the lowest time on that one.

**Speaker_03** [08:18:58]: And it looks

**Speaker_03** [08:19:08]: like the middle part

**Unknown speaker** [08:19:08]: of 3 and 5, that was to have the

**Speaker_03** [08:19:14]: highest key rights, so you see that gets provisionally useful.

**Speaker_03** [08:19:15]: But we have total control to play with that strategy.

**Speaker_03** [08:19:16]: So if you, for example, we want to refresh the music, but I'm going to use a very recently for some application.

**Speaker_03** [08:19:19]: We can write that down.

**Speaker_03** [08:19:19]: And then other than that, you see with the keyboard down the bottom here, the bottom key generation works like piecing keys, continuous pieces, constant production of secret key material, which is just random and important to us.

**Speaker_03** [08:19:24]: And we sort of store those in a buffer.

**Speaker_03** [08:19:29]: So we can also make larger clues.

**Speaker_03** [08:19:33]: The applications will need larger keys or whatever, right?

**Speaker_03** [08:19:35]: So the keys are continuously accumulated at that point.

**Speaker_03** [08:19:37]: There's also this bit of jargon you're going to hear thrown around by the way.

**Speaker_03** [08:19:40]: If you're a lookout QK, it's called the quantum bit error ratio or QK.

**Speaker_03** [08:19:42]: And you can think of this as a kind of tripwire.

**Speaker_03** [08:19:45]: So anyone who tries to tackle this network, anybody who tries to intercept the photons or break the scheme in any way, will drive an increase in this error ratio.

**Speaker_03** [08:19:55]: So it's a sort of tripwire, or if it goes above the orange line in the graph, the system will assume there's a problem and try and bring it below that line.

**Speaker_03** [08:20:04]: And if it goes above the gray line, it will just stop producing keys.

**Speaker_03** [08:20:07]: So it's completely fail-safe and that's the same one that tries to.

**Speaker_03** [08:20:11]: Again, very very technical detail, which I could go into, but essentially there's no way proven by constant physics.

**Speaker_03** [08:20:15]: Also you can interact with the network in a way that would compromise

**Speaker_00** [08:20:17]: the

**Speaker_03** [08:20:17]: spirit key and not try to help this region.

**Speaker_03** [08:20:18]: So this is our triple R we want to discuss to make sure it's below the necessary threshold.

**Speaker_03** [08:20:25]: question that we have to go to one.

**Speaker_03** [08:20:27]: Just to say, we think it's provided, can I say ultimate protection for data data?

**Speaker_03** [08:20:31]: I mean, an ultimate in a sense that we don't know of a better way or a harder way

**Unknown speaker** [08:20:35]: to secure us, I

**Speaker_03** [08:20:35]: think.

**Unknown speaker** [08:20:36]: So the ultimate protection you give today's data is a chance of learning

**Unknown speaker** [08:20:45]: we'll be upgrading our algorithms themselves to something that's

**Speaker_03** [08:20:48]: one or six.

**Speaker_03** [08:20:49]: But this goes back to the first of all, security into a physical basis, and it just gives you a kind of backstop where let's say one of these new algorithms that's being pushed, it turns out not to be resilient against quantum computers.

**Speaker_03** [08:21:01]: This will definitely be resilient against quantum computers, and also any other kind of computer that will ever be created, which is a ridiculous statement, but I mean very seriously.

**Speaker_03** [08:21:09]: So it's a really different approach.

**Unknown speaker** [08:21:11]: And like

**Speaker_03** [08:21:12]: I said, the QR code is still there.

**Unknown speaker** [08:21:13]: Thank you.

**Speaker_00** [08:21:28]: and the threat is far in the future and or however far we don't know and as such it is hard for organizations busy with their day- today to plan ahead, unless compelled by regulations that will tell them you are only compliant if you implement something like this.

**Speaker_00** [08:21:52]: Is it your expectation that this is going to be the driver for adoption?

**Speaker_00** [08:21:57]: It's a very good point, so compliance

**Speaker_03** [08:21:59]: and regulations are required in this way.

**Speaker_03** [08:22:06]: it's difficult to make predictions, especially about the future.

**Speaker_03** [08:22:09]: But in this case, I have seen, as of last year, some of the main quantum computing companies have roadmaps that scale to something that would threaten encryption, I say, 2030. I personally don't believe they will do this by 2030, but I think by 2035, it's not the best.

**Speaker_03** [08:22:24]: I can think of loads of information as a secure lifetime that goes past 2030. So it's a present problem, right?

**Speaker_03** [08:22:30]: And so in terms of regulations for some people to operate, It's definitely true, this will be part of that, and as a conversation going on with the security, sorry, with the insurance companies to see how they kind of manage this thing.

**Speaker_03** [08:22:40]: I would say that most large issue-scale enterprises could afford to devote a little bit of force to this, have some kind of plan in place for when these regulations come in.

**Speaker_03** [08:22:50]: In the UAE, there is a recommendation already, mandating cryptographic migration for government entities, which will probably be extended because it's for the UAE, to very large private sector entities at some point.

**Speaker_03** [08:23:02]: So there is a mandate to transition to quantum safe solutions.

**Speaker_03** [08:23:04]: In regulations, they don't actually say what quantum safe solutions are.

**Speaker_03** [08:23:07]: They leave that as a sort of financial office, which I'll get worked on.

**Speaker_03** [08:23:09]: But this would count as one of those quantum safe prices.

**Speaker_03** [08:23:13]: So I think anyone who's dealing with particularly valuable data should probably have some activity on this.

**Speaker_03** [08:23:20]: And we see this as an issue as well.

**Speaker_03** [08:23:21]: There are test beds in London and Singapore and Madrid in particular.

**Speaker_03** [08:23:25]: I think those are the three most serious ones I think of in which banks like HSBC in Santander.

**Speaker_03** [08:23:29]: are very seriously engaging with this technology, doing POCs.

**Speaker_03** [08:23:36]: They're all very careful to tell you they're not using customer data, they're using simulated data.

**Speaker_03** [08:23:39]: But I've also spoken privately to the CEOs with EQV and e-companies, and they're sure they're not legal action using it.

**Speaker_03** [08:23:43]: So it's in that phase now where maybe it's not, it doesn't necessarily connect with regulations and compliance, but it doesn't compromise existing compliance.

**Speaker_03** [08:23:52]: So people are putting it in as a sort of fallback.

**Speaker_03** [08:23:58]: than just

**Unknown speaker** [08:24:09]: being compliant with whatever regulations are.

**Unknown speaker** [08:24:10]: And so I think this is the time for planning to do that.

**Speaker_05** [08:24:21]: on such a nice presentation.

**Speaker_05** [08:24:24]: One question is regarding the expansion in other sectors like healthcare and how you see a capability of such networks and how we are far away from setting the network that also communication users at home in specific association

**Speaker_03** [08:24:42]: and cases like hospitals for example.

**Speaker_03** [08:24:43]: So a great question of that dimension healthcare because from my point of view the healthcare sector has worked a lot with this secure lifetime to live.

**Speaker_03** [08:24:48]: If you imagine a very large hospital like the one next to us and I've lost track over there somewhere.

**Speaker_03** [08:24:53]: So there's a very large hospital and you have thousands of patients that you've got a lot of very personal things on the data on these patients.

**Speaker_03** [08:25:00]: And I think there's a duty of protection to protect them, but this will be expected by your clients.

**Speaker_03** [08:25:05]: And you should probably keep this stuff confidential as long as the patient is alive, and the patient has children.

**Speaker_03** [08:25:10]: like a very reason you make the argument that there's almost unbounded with secure lifetime information and also that could be like tangible financial like values for statement right so you could also argue in court with someone who's disabled who's disappointed to actually have material losses

**Speaker_03** [08:25:26]: right so I think that's a really important error entity like a large hospital, for example, that's doing backup to a remote data center or who is being compelled to back up their data to a government-run central repository as in the UAE.

**Speaker_03** [08:25:39]: I think those links, we could definitely protect it.

**Speaker_03** [08:25:42]: It's a situation where you've aggregated a lot of data together, so you don't have to worry about the value of each individual patient report.

**Speaker_03** [08:25:48]: You worry about the aggregate value of all the records, the probability that's something that there is very high one place and push it down, single flight.

**Speaker_03** [08:25:55]: So if somebody wants to do this store-in-air and per plate, it has to fly together with earth, so that's where you're going to protect, right?

**Speaker_03** [08:26:01]: And I think we have to give us a really nice lens to look at the general problem of how do we scale what's happening to society.

**Speaker_03** [08:26:09]: So if you start imagining where is data brought together in angry, and the places where the largest volume of valuable information, traveling down one link, that's where you would start all of this now.

**Speaker_03** [08:26:17]: So I think healthcare, absolutely, that's good.

**Speaker_03** [08:26:18]: Like data centers, definitely, right?

**Speaker_03** [08:26:20]: But then you start thinking, okay, once I've protected all those very high value targets, you just move to the next point and then you go down and down and down the chain, out into the branches of the tree, if you like.

**Speaker_03** [08:26:28]: And so then I start thinking about QGate to the user.

**Speaker_03** [08:26:31]: So for example, I live here in Raffa Beach somewhere.

**Speaker_03** [08:26:33]: And my Wi-Fi network is protected with, honestly, I don't know where it's probably not very secure.

**Speaker_03** [08:26:38]: But my kids' Netflix habits are probably not very valuable data.

**Speaker_03** [08:26:41]: So I don't think it's an especially valuable data traveling around my network.

**Speaker_03** [08:26:45]: But I also live in a building with probably a few thousand other people.

**Speaker_03** [08:26:48]: And I can say for sure that they don't have valuable stuff happening with their networks.

**Speaker_03** [08:26:51]: And again, it all gets aggregated somewhere in the basement, goes across the road to a baseline of a facility and then heads off to the city.

**Speaker_03** [08:26:57]: I don't know why it's not necessary.

**Speaker_03** [08:26:58]: So probably it is plausible to roll this out to these aggregation ones.

**Speaker_03** [08:27:03]: But again, maybe not on the way to the individual use of apartments.

**Speaker_03** [08:27:06]: So we have a technology that's in development, I think I mentioned at the start of the talk, there's a cost-optimized solution.

**Speaker_03** [08:27:11]: I think this brings the cost of QKD down to similar to the cost of networking cryptos.

**Speaker_03** [08:27:16]: And I know people can afford to use those to secure buildings.

**Speaker_03** [08:27:18]: So I hope we have a solution that's going to at least reach like offices and stuff.

**Speaker_03** [08:27:24]: So I think it's plausible.

**Speaker_03** [08:27:25]: I think anyone that has fiber connections, anyone that has fiber internet, for example, can probably benefit from this in the next few years.

**Speaker_03** [08:27:30]: But they should be tackled after we tackle things like healthcare data around today.

**Speaker_03** [08:27:35]: So that's kind of the highest priority, I think.

**Speaker_03** [08:27:38]: Also government communications as well.

**Speaker_03** [08:27:43]: And the protection starts to look reasonable

**Unknown speaker** [08:27:48]: in that content.

**Unknown speaker** [08:27:51]: Thank you.

**Unknown speaker** [08:27:53]: Thank you for your technical

**Speaker_03** [08:28:03]: pitch as

**Speaker_03** [08:28:13]: well for us you can sort of rank by priority where you would expect to find the most exposure.

**Speaker_03** [08:28:23]: So obviously government is where you find people who claim that the data has no bounds in your lifetime or so.

**Speaker_03** [08:28:29]: Also that's an area that's not super sensitive to profit.

**Speaker_03** [08:28:32]: No, sorry, government's done.

**Speaker_03** [08:28:33]: You should try and make profits.

**Speaker_03** [08:28:35]: They have an operating budget and that's concerned about what it costs to you.

**Speaker_03** [08:28:37]: and achieve security.

**Speaker_03** [08:28:38]: So that's a great place to start with a stamping.

**Speaker_03** [08:28:43]: And then if you move out into kind of, I guess, like society at large, I think healthcare data finance data, maybe on transaction records, stuff like this.

**Speaker_03** [08:28:49]: Very sensitive corporate IP.

**Speaker_03** [08:28:51]: There's definitely trade secrets that are transitioned to offices that could have a very high value.

**Speaker_03** [08:28:57]: So these would be kind of areas where you'd expect to find this.

**Speaker_03** [08:28:59]: I also think there's probably quite a strong use case in personal infrastructure.

**Speaker_03** [08:29:02]: So critical infrastructure, this is less about long- duration security, although it's definitely also important.

**Speaker_03** [08:29:06]: For example, if you've built a nuclear reactor, then the plans and the exact layout are inside that facility, that should stay secret as long as the reactor is commissioned, because if you were going to try and compromise or exploit the damage listing, you would start by trying to get hands-on

**Speaker_03** [08:29:20]: schematics.

**Speaker_03** [08:29:21]: So there's definitely very long-term secure information on critical infrastructure section.

**Speaker_03** [08:29:24]: But there's also like live data and travel around the center.

**Speaker_03** [08:29:29]: So for example, there is a QKD trial happening in the board of Rob's down today.

**Speaker_03** [08:29:34]: And they're securing two types of data.

**Speaker_03** [08:29:36]: One is customer's data.

**Speaker_03** [08:29:37]: You should find customer's data has a very long secure lifetime.

**Speaker_03** [08:29:39]: You know, you have a container.

**Speaker_03** [08:29:41]: The stuff inside the container should be confidential.

**Speaker_03** [08:29:44]: You have to disclose that to the customers of people.

**Speaker_03** [08:29:45]: They should also keep this information confidential, but they want to transfer it in ground reports so you have a long secure lifetime.

**Speaker_03** [08:29:51]: But they're also securing sensor data.

**Speaker_03** [08:29:53]: So the port of Rob's down, sorry, port of Rob down.

**Speaker_03** [08:29:55]: many, I think it's water level sensors, and they're really keen on making sure that the integrity of that network is undeniable.

**Speaker_03** [08:30:02]: Because if one of the sensors goes out of range, they have to shut down the wall and move all the assets out of them.

**Speaker_03** [08:30:08]: And this can easily result in disruptions that take several days to recover from, that's through tens of millions of years.

**Speaker_03** [08:30:13]: And I said to them, why would you just send the guy on a bicycle to check?

**Speaker_03** [08:30:16]: And they said, no, no, that's not how operating for cells like this works, because this is what's happening.

**Speaker_03** [08:30:21]: So I think there's an argument that the key PD could be used to not just secure the network, but using this key material you can prove that only authorized participants in the network had sent these to this data around.

**Speaker_03** [08:30:34]: So I think that's a strong argument in critical structure.

**Speaker_03** [08:30:36]: So that's a slightly different application of it.

**Speaker_03** [08:30:39]: It's also important.

**Speaker_03** [08:30:41]: But I think those are the main areas where that privilege will take place.

**Speaker_03** [08:30:43]: You also asked about, and that being general.

**Speaker_03** [08:30:46]: And so I think, again, I think the narrative is pretty strong on what's called post-1 cryptography.

**Speaker_03** [08:30:52]: bit of awareness that's come and go to the last maybe three years that we do need to address some kind of migration or something that's quantum safe but again most companies, most users interact with the application and you're going to open your laptop and you say what am I using on here?

**Speaker_03** [08:31:11]: There's probably hundreds of cryptographic algorithms going on my laptop.

**Speaker_03** [08:31:13]: Every single bit of software has something and they all need to be upgraded so it's quite daunting and so if you are using like a cloud service provider probably you should be asking your cloud service provider what they're doing about corresponding cryptography whether it's getting when they're

**Speaker_03** [08:31:26]: getting implemented, and so on and so on.

**Speaker_03** [08:31:29]: And I think people are doing this.

**Speaker_03** [08:31:31]: If you have your own private infrastructure, then it's probably a time to do a cryptographic audit.

**Speaker_03** [08:31:33]: So there are companies that's actually spin-out front-tailing quantum data.

**Speaker_03** [08:31:35]: No affiliation to the quantum research center.

**Speaker_03** [08:31:36]: They're doing what was called cryptography.

**Speaker_03** [08:31:37]: So the terminology can be quite confusing.

**Speaker_03** [08:31:39]: But one of their main activities is this cryptographic image, which is called Scorge, instead of go through organization, make a list of what cryptography is in use where, and then prioritize bits of it from migration.

**Speaker_03** [08:31:48]: So that's quite an important strategy.

**Speaker_03** [08:31:51]: But I think the peak you see migration can look quite overwhelming, because like I said, so many things have to be replaced, and it is going to take a long time to be very disruptive, that if you have private infrastructure and private networks that support this kind of thing, then you can use a, in

**Speaker_03** [08:32:05]: some sense, it's way easier, right?

**Speaker_03** [08:32:07]: You just deploy it on critical things, and now you know that whatever's traveling you've done, however it's individually protected, it's benefiting from its lower level of protection.

**Speaker_03** [08:32:14]: The technical terms, that is defense and death, and it's, I think it's relevant to anyone that has a private number of attention.

**Speaker_03** [08:32:20]: And in some sense, it's a few risks, a bit of the rest of the migration, so that's where I'd say it is, but I think levels of awareness are definitely improved over the last few years.

**Speaker_03** [08:32:29]: And then UAE Cybersecurity Council is pushing quite hard on this transition.

**Speaker_03** [08:32:35]: We have this big event in Abu Dhabi that's become an annual event called CyberCube, which is commonly sponsored by the Cybersecurity Council, and it's all about its migration.

**Speaker_03** [08:32:41]: So you see a lot of activity, a lot of interest, and that's encouraging.

**Speaker_03** [08:32:44]: It means I don't have to walk around,

**Unknown speaker** [08:32:47]: I have to get into that and

**Speaker_03** [08:32:47]: throw you somewhere.

**Speaker_03** [08:32:48]: Thank you.

**Speaker_01** [08:32:52]: When

**Speaker_03** [08:33:06]: you explain this quantum of security to lay people, do you have a aha moment of ways on which the lay person understands the quantum body with the observability changes the culture.

**Speaker_03** [08:33:09]: Okay, so I think that's a good question.

**Speaker_03** [08:33:13]: I have a scientific education.

**Speaker_03** [08:33:14]: So I, an old guy called Arta Anger, who invented entanglement base QV in 1991. And he has an entire hour-long budget lecture just talking about superposition.

**Speaker_03** [08:33:23]: So I was like superposition, and I'm two months of being simultaneously being two contradictory states at the same time.

**Speaker_03** [08:33:29]: Why does that take now?

**Speaker_03** [08:33:31]: No, he turns this into an entire hour of trying to really get people to understand this point.

**Speaker_03** [08:33:35]: So I think it could go for a team.

**Speaker_03** [08:33:37]: For me, I think I have some slides that are not in this deck, but talk about, you know, someone says physics back to security or physics derived security, security based on common physics, and you should say that sounds weird, what does that mean?

**Speaker_03** [08:33:47]: And so I would say there's a couple of points.

**Speaker_03** [08:33:49]: One is to think of light traveling in terms of single particles, single particles of light.

**Speaker_03** [08:33:53]: That's a core principle of what's called discrete variable QQE, which is the kind of weird.

**Speaker_03** [08:33:59]: If you think about classical information, which is also often optical and photonic in nature, so in my apartment I have a device that focuses on fiber.

**Speaker_03** [08:34:06]: And that device sends bits on the information that's not enough of a deep photon to base 1 to 0s, and those bits travel over the fiber to form with pulse supply.

**Speaker_03** [08:34:14]: The pulse supply contains trillions of photons, a huge number of photons, 10 to the 24 photons, lots of photons make up out of pulse, and the entire pulse is a 1 or a 0. And so if you take a tiny fraction of those photons out of the pulse, you can tell if they come from a 1 or a 0 pulse.

**Speaker_03** [08:34:30]: So the information is redundantly encoded across a very large number of photons.

**Speaker_03** [08:34:33]: But when you move to quantum communications, it's a single photon and it's carrying information.

**Speaker_03** [08:34:37]: And so obviously the rules are different now.

**Speaker_03** [08:34:40]: I can't take some of them, because there's only one per bit, per bit, per bit.

**Speaker_03** [08:34:45]: So that's one of the intrinsic transactions that I think people connect 2.1. You say, look, I can't take fractions of the lights out of its particles, single particles.

**Speaker_03** [08:34:53]: And the other one is this idea of like the particles in a single position.

**Speaker_03** [08:34:57]: So you can code a one and a zero simultaneously with different phases.

**Speaker_03** [08:35:00]: This is maybe hard for people to wrap their heads around.

**Speaker_03** [08:35:02]: But you can definitely say if I take one of these problems out and measure it, I destroy it in the process, and I project the state.

**Speaker_03** [08:35:08]: And there's no way for me to then take what I can't believe and put it back in.

**Speaker_03** [08:35:12]: You can't copy these things without disturbing.

**Speaker_03** [08:35:15]: You can't measure them without destroying the state.

**Speaker_03** [08:35:17]: And so it's natural to imagine it's impossible to come up with a scheme where such a measurement inevitably disrupts the communication quality.

**Speaker_03** [08:35:25]: And that's where the security is coming from.

**Speaker_03** [08:35:28]: So I don't know about the Alhambra.

**Speaker_03** [08:35:29]: I mean, I like this idea of like a simple particle versus non-standard.

**Speaker_03** [08:35:31]: People seem to

**Unknown speaker** [08:35:32]: connect with that.

**Unknown speaker** [08:35:33]: And then

**Speaker_03** [08:35:34]: if

**Unknown speaker** [08:35:35]: you go to Whiteboard and start

**Speaker_03** [08:35:37]: thinking about it, you can just sort of come

**Unknown speaker** [08:35:38]: up

**Speaker_03** [08:35:38]: with how many of you can make a course of a secure schema.

**Speaker_03** [08:35:41]: But yeah, it's up.

**Speaker_03** [08:35:42]: It's fine.

**Speaker_03** [08:35:42]: The entire one part, I just want to

**Unknown speaker** [08:35:43]: talk to you.

**Unknown speaker** [08:35:43]: That's a good trick.

**Speaker_02** [08:35:45]: Thank you for the presentation.

**Speaker_02** [08:35:47]: I work in the digital assets space, and I was curious, probably, you might get this question, but specifically regarding Bitcoin, I'm just wondering if you have any thoughts on potential quantum waste that could

**Speaker_03** [08:35:58]: potentially play out?

**Speaker_03** [08:36:00]: Sure, I think digital assets are super relevant to this.

**Speaker_03** [08:36:03]: Again, it's a situation where digital data hasn't like a real family group so should be very concerned about this.

**Speaker_03** [08:36:11]: I think specifically when it comes to blockchain technologies, that's a public legend.

**Speaker_03** [08:36:15]: So you can't get away from the fact that you need a public infrastructure, It's very difficult to run at least a global blockchain that doesn't rely on public key infrastructure.

**Speaker_03** [08:36:31]: So it's very difficult to acquire this like a fully symmetric key blockchain.

**Speaker_03** [08:36:36]: You can do it, people have done it, and it's done for, I guess, sort of air gaps, you know, corporate blockchain.

**Speaker_03** [08:36:40]: So think about things like the MRO space where someone's using blockchain to keep track of components of aircraft or something.

**Speaker_03** [08:36:43]: Then it can be fully symmetric.

**Speaker_03** [08:36:44]: You don't have to distribute a public key very clearly.

**Speaker_03** [08:36:45]: Everyone's in the organization.

**Speaker_03** [08:36:48]: But I think digital assets have to be on these like world news through the public- blockchain.

**Speaker_03** [08:36:54]: So you need this public-private community structure.

**Speaker_03** [08:36:56]: And so I'm aware that are upgrades.

**Speaker_03** [08:36:58]: There are blockchains that are entirely based around the idea of being quantum safe.

**Speaker_03** [08:37:02]: And that should show you the seriousness of this.

**Speaker_03** [08:37:04]: When it comes to Bitcoin in particular, so again, I'm not an expert on this, but my understanding is the original transactions on the chain.

**Speaker_03** [08:37:11]: were signed using the RSA crypto system, right?

**Speaker_03** [08:37:17]: And so the situation now, I think the term is the private key is exposed, is that right?

**Speaker_03** [08:37:21]: So this means that it's, sorry, the public key is exposed, right?

**Speaker_03** [08:37:24]: So it's possible for somebody who would like to step on a computer to take that public key.

**Speaker_03** [08:37:31]: transactions as if they're in the wallet.

**Speaker_03** [08:37:33]: That's inevitable, that will definitely happen.

**Speaker_03** [08:37:35]: So for example, those early wallets that haven't moved for a very long time.

**Speaker_03** [08:37:38]: At some point, somebody will start transacting on those and then we'll know that this machine.

**Speaker_03** [08:37:44]: Likewise, if I made that machine, I wouldn't do that.

**Speaker_03** [08:37:46]: I was going to be too often, so I'd go and do more stuff with that in a very specific machine.

**Speaker_03** [08:37:50]: But yes, I think it's too late for some of you guys.

**Speaker_03** [08:37:56]: That's really interesting to see how the network reacts to that when it happens.

**Speaker_03** [08:38:00]: But I understand that modern blockchain operates differently, right?

**Speaker_03** [08:38:02]: So from now forward, everyone transfers everything to a new office to a residual value goes to a new office, which doesn't help exploit its public.

**Speaker_03** [08:38:07]: That makes it much harder for everyone coming out to attack this.

**Speaker_03** [08:38:09]: I'm not saying it's possible.

**Speaker_03** [08:38:10]: So there

**Speaker_03** [08:38:17]: probably is an important upgrade to some EQC-based complicated structure in the future.

**Speaker_03** [08:38:28]: But yeah, it would be a fascinating network effect when that happens in the ordinary, like, I guess, track down that way.

**Speaker_03** [08:38:31]: And this, there's a lot of, I'm really asking about just how much of this thought to be just stuck.

**Speaker_03** [08:38:33]: So, I think that'll be a quick, I think a price crunch, thanks very much, but probably not possible.

**Speaker_03** [08:38:35]: I wouldn't expect that.

**Speaker_03** [08:38:36]: except to say that it's definitely too late for a lot of us left to not be in front of the system.

**Speaker_03** [08:38:45]: So whatever that means,

**Speaker_01** [08:38:46]: it was planning a little bit.

**Speaker_01** [08:38:46]: Yeah, you mentioned that the price will come down eventually, hopefully, whatever.

**Speaker_01** [08:38:52]: I'm curious about what are the cost drivers, right?

**Speaker_01** [08:39:04]: so

**Speaker_03** [08:39:05]: I can talk about answering.

**Speaker_03** [08:39:06]: So it turns out the skill we built here involves one entangled server in the middle and then many receivers.

**Speaker_03** [08:39:11]: And so you can share that one entangled resource between, I think, depends on the range of the fiber, because the range limits the key rate.

**Speaker_03** [08:39:18]: But yeah, you can map one entangled source to 3,000 users, no problem, right?

**Speaker_03** [08:39:23]: So the cost of entangled source is not super important.

**Speaker_03** [08:39:26]: Also, it's a lot lower than the receivers, so the network is kind of built back on the digital network, right?

**Speaker_03** [08:39:30]: The receivers are the expensive part.

**Speaker_03** [08:39:31]: They're expensive because they contain single-folded detectors.

**Speaker_03** [08:39:34]: And so the technique that you can click on a single part of the light goes into this.

**Speaker_03** [08:39:39]: It's quite an extreme thing.

**Speaker_03** [08:39:39]: It's basically, it's anti-particle, etc.

**Speaker_03** [08:39:41]: And so those are, the supply chain is terrible.

**Speaker_03** [08:39:43]: There's very few places going to make them.

**Speaker_03** [08:39:45]: They're very expensive because the R&D that goes into making them work reliably is difficult.

**Speaker_03** [08:39:52]: to the street, variable key period, but I can circle back to the audience, tries to make their own in-house attentions.

**Speaker_03** [08:40:00]: We've also been working on this, it takes years and costs them a bit of time.

**Speaker_03** [08:40:03]: So that's a very hard technology to master.

**Speaker_03** [08:40:08]: And so for the moment, that's really a massive price point.

**Speaker_03** [08:40:10]: So what we do with our last mile system is we flip it around.

**Speaker_03** [08:40:12]: We put one receiver in the middle, which we don't try and customize.

**Speaker_03** [08:40:14]: In fact, we make it more expensive and make it higher performance.

**Speaker_03** [08:40:17]: And then we give the users transmitters.

**Speaker_03** [08:40:18]: In the last mile scheme, we don't use entanglement anymore.

**Speaker_03** [08:40:20]: We just worked on an older technology that was invented in 1984. So the protocol is called BBS1.

**Speaker_03** [08:40:23]: And we try to really seriously post- optimize the transfer to the summit.

**Speaker_03** [08:40:29]: target like a translated price, I don't like to give exact amounts, but we're looking at about $20,000 maybe for $100,000, which sounds like a lot, but it's not network-enriched as cost, right?

**Speaker_03** [08:40:40]: You go to June for a while, we're in advance, and that's what it comes to say.

**Speaker_03** [08:40:42]: I know there's a budget for those in IT, so the chip is under it.

**Speaker_03** [08:40:44]: You contrast that with today, like the only company I'm aware of selling QKB with all of your sales prices is at the content.

**Speaker_03** [08:40:50]: And I believe they charge about $250,000 to scale two months.

**Speaker_03** [08:40:54]: of managing production but in particular if you scale this to a large network so our last and our solution imagine to these stars are going to be our one receiver connects to maybe 100 transfitters and then the cost of the receiver is down to not very well done any more and those transfitters can be

**Speaker_03** [08:41:14]: nice to come back to produce them i think the cost can come down another factor of two or three so we can probably start to make qkd transfitters that cost less semantics at which point i think we can start to make a fairly good list i also And a lot of the cost that goes into the transmitter is on

**Speaker_03** [08:41:22]: optoelectronics, sort of lasers, detectors, things like that, not single photo detectors, but just high enough photo diamonds.

**Speaker_03** [08:41:28]: And all of that can be compressed into a chip.

**Speaker_03** [08:41:31]: So one activity having a team here about four guys work on this is to really to explore photonic chip solutions to all of that.

**Speaker_03** [08:41:38]: And I think there's a good chance that sometime this year we're going to get one of those working.

**Speaker_03** [08:41:46]: You know, getting them working this year and getting into a product is a very different thing.

**Speaker_03** [08:41:48]: So two or three years, I think we can replace most of us in that with one of these products.

**Speaker_03** [08:41:51]: And I would imagine, like, at least my workman says that the next sort of a little hard drive for a let's say a bell mic and an amp-on and probably put them inside the amount of disc.

**Speaker_03** [08:42:07]: Because again, you're buying a primitive from a 14-hour MCM or GMO or something.

**Speaker_03** [08:42:13]: So it's like a network device instead of the size of a normal VCR player or something.

**Speaker_03** [08:42:16]: And so once QKU becomes a deployment inside there, that should really let us really push out the infrastructure.

**Speaker_03** [08:42:19]: So today it's a 19-inch rank 4U device plus a little bit of 100,000 dollars per note.

**Speaker_03** [08:42:24]: But I think very soon that's going to come down.

**Speaker_03** [08:42:25]: And I think, since we're talking about the cost of this, I should mention that the point of the ADGN network we've built here is to get rid of a school, so provide this as like infrastructure, and that anyone in this room, and you have a friend in Abu Dhabi, can approach us and try and start from

**Speaker_03** [08:42:44]: it.

**Speaker_03** [08:42:44]: So it's an opportunity to experiment with use cases without having to find a few hundred thousand dollars to fund experiments as hardware.

**Speaker_03** [08:42:48]: And there'd be the better place for the next solutions that came along with you.

**Unknown speaker** [08:42:50]: Thank you.

**Unknown speaker** [08:42:58]: You said this

**Speaker_02** [08:43:01]: technology is more complementary to the governance

**Speaker_06** [08:43:09]: system we have,

**Speaker_03** [08:43:10]: as we integrate this more and more.

**Speaker_03** [08:43:12]: Do you think it'll have an impact on art systems about communication?

**Speaker_03** [08:43:15]: Sure, so complementary to EQC approaches and to other kinds of encryption as well.

**Speaker_03** [08:43:18]: So this is a way of doing hardware security.

**Speaker_03** [08:43:19]: So it's obviously, it's a slightly different paradigm from algorithms here.

**Speaker_03** [08:43:24]: I've written a

**Unknown speaker** [08:43:27]: series

**Speaker_03** [08:43:29]: that's

**Unknown speaker** [08:43:31]: very important.

**Unknown speaker** [08:43:33]: For example, in

**Speaker_03** [08:43:34]: blockchain, you want to sign something.

**Speaker_03** [08:43:35]: So you need to have a public-private key infrastructure that allows you to sign the transactions.

**Speaker_03** [08:43:37]: We could do that here, but only one other person will be able to verify your signature on the other symmetric keyboard.

**Speaker_03** [08:43:41]: So it's complementary to software and computer.

**Speaker_03** [08:43:42]: But also, if you think about how the internet, I'd love him recently with a cryptographer and from our cryptography research center.

**Speaker_03** [08:43:46]: And the sort of, once we drove into it, the core of his objection was, it'd be very difficult to replace the entire incident with us.

**Speaker_03** [08:43:53]: And I said, Definitely not the platform, how on earth would you even approach this.

**Speaker_03** [08:43:57]: And so we end up going back to this point of is this technology valuable if it can replace all the encryption?

**Speaker_03** [08:44:02]: I think yes, right.

**Speaker_03** [08:44:03]: It's like arguing, so arguing the reverse would be arguing the trains are doing this, because you can't use trains to get extra design.

**Speaker_03** [08:44:08]: So there are different measures for different types of things.

**Speaker_03** [08:44:16]: So I think I might use transport as a counter, you know, sort of analogy, right?

**Speaker_03** [08:44:19]: But in transport, we see different kinds of transport for different, like different use of transport.

**Speaker_03** [08:44:24]: If I'm

**Unknown speaker** [08:44:24]: trying to get

**Speaker_03** [08:44:24]: from here to New York, I'm going to drunk, I'll take a plane.

**Speaker_03** [08:44:26]: I'm going to get it from here to my house, and I'm going to drive.

**Speaker_03** [08:44:27]: So I think the software approach is kind of like you're driving, that's your personal transport.

**Speaker_03** [08:44:30]: So they're needed every, but they're even needed on my laptop, between other bits of software.

**Speaker_03** [08:44:35]: So if your brain system wants to communicate with power, then they'll also communicate with And so it's important to have software encryption that can handle that.

**Speaker_03** [08:44:43]: That's the QKD wouldn't help there.

**Speaker_03** [08:44:45]: But then if we're connecting two data centers together, why not use this high level of security?

**Speaker_03** [08:44:49]: So that's what I meant by comprehension.

**Speaker_03** [08:44:50]: And I think also it's a sort of diversification of risk.

**Speaker_03** [08:44:54]: So as long as you're only using software encryption, you're vulnerable to compute advances.

**Speaker_03** [08:44:59]: So I think that in the PQC community, they're very clear about this, that these algorithms are not forever.

**Speaker_03** [08:45:04]: They'll need to be replaced eventually once somebody breaks them, whether it's possibly in the breaks them or some other company in the breaks.

**Speaker_03** [08:45:11]: But with QKD, that's not clear.

**Speaker_03** [08:45:12]: and we can tolerate any kind of computer being developed, like really unbounded work.

**Speaker_03** [08:45:16]: And we rely only on people not being able to come down to the quantum physics of the system, which we think we're fairly sure about.

**Speaker_03** [08:45:21]: But again, I'm a physicist, so hey, there could be some really exciting new physics that makes these things more secure.

**Speaker_03** [08:45:26]: So again, you want to try and balance these different risk factors.

**Speaker_03** [08:45:29]: So this is a way of diversifying how your information security is obtained.

**Speaker_03** [08:45:39]: and also

**Speaker_01** [08:45:46]: compromise

**Speaker_01** [08:45:59]: with UK, you would certainly as yet not fall through business, right?

**Speaker_01** [08:46:00]: And that gets much, much harder to say.

**Speaker_01** [08:46:02]: That's kind of why not a question.

**Speaker_01** [08:46:02]: My question is, What does

**Speaker_03** [08:46:05]: AI present in the context of quantum security?

**Speaker_03** [08:46:10]: So what was the risks with respect to AI, in that was.

**Speaker_03** [08:46:13]: And I may,

**Speaker_01** [08:46:14]: I know you went through with the ADGM as an ecosystem.

**Speaker_01** [08:46:23]: What about applications of quantum security into a critical infrastructure?

**Speaker_01** [08:46:27]: I'm sorry, energy

**Speaker_03** [08:46:27]: sector over better than the UK, and critical infrastructure for it to get out of the future.

**Speaker_03** [08:46:31]: Okay, so the first one, AI.

**Speaker_03** [08:46:32]: So I think.

**Speaker_03** [08:46:33]: When I think about AI damaging our cyber security, there are people in our research center who specialize on this, but not sorry on my research center, but an adjacent research center in San Antonio.

**Speaker_03** [08:46:43]: And so of course you can use AI to probe complex networks and look for things that are implemented incorrectly on the top of sleep stuff, that's that's sort of not interesting, that's not interesting to me, I'm sorry, that's your kind of general secure system in this area, right?

**Speaker_03** [08:46:58]: And of course you can also use AI to point out the same problem and try and find out what's in your system.

**Speaker_03** [08:47:03]: That's one area where AI just replace a lot of very key keywords to people.

**Speaker_03** [08:47:08]: But I think it's also possible for AI to fundamentally challenge the way you're doing encryption.

**Speaker_03** [08:47:13]: So I'm not suggesting somebody will produce an LEM or some kind of neural net that can decrypt RSA communications.

**Speaker_03** [08:47:19]: But I think it's very interesting what Google's deep-minded company have been doing on this.

**Speaker_03** [08:47:24]: So if you look at how they solve things like Go, they were operating this generalized episode on hardware approach.

**Speaker_03** [08:47:28]: where they would gamify a problem, and they get the AI to play into the stuff that they're going to attack.

**Speaker_03** [08:47:35]: And they also, much, much less likely reported, but they did something on matrix multiplication.

**Speaker_03** [08:47:38]: So they trained AI to predict algorithms for matrix multiplication, not quantum algorithms, just algorithms.

**Speaker_03** [08:47:45]: And it's very, very cheap and easy to test the performance of these algorithms actually on the grid.

**Speaker_03** [08:47:49]: So they kind of use the AI to generate millions and millions and millions of possible matrix multiplication algorithms, and then they test them.

**Speaker_03** [08:47:56]: And so up until that point, I think the history was 50 or 60 years.

**Speaker_03** [08:48:00]: There have been a single matrix multiplication program, which was the de facto correct way to multiply two matrices together.

**Speaker_03** [08:48:06]: Had it very well on its scale and it was very well understood.

**Speaker_03** [08:48:08]: And they did this thing over a couple of days, after which they were able to reduce the cost, meaning performance, cost, energy cost of learning, of matrix multiplication by about 30%.

**Speaker_03** [08:48:17]: Of course, the catch was that in an ongoing single best album that made a bunch of outcomes, depending on the major sites.

**Speaker_03** [08:48:23]: What over the next few weeks, they found a single album, which was about 30% more efficient than previous best album?

**Speaker_03** [08:48:29]: And that happened over the course of the week or so.

**Speaker_03** [08:48:33]: It wasn't very widely thought this sounds like it was very important to AI people, because they did a lot of much of our major cities, right?

**Speaker_03** [08:48:38]: And AI is of course consuming about an hour, so I'm glad they did it, but I'm encouraged.

**Speaker_03** [08:48:41]: And the problem is, I need it for what if they try a factory?

**Speaker_03** [08:48:45]: I don't know if they try factor.

**Speaker_03** [08:48:58]: Then this is So I don't think AI will directly de

**Speaker_03** [08:49:25]: And this is what I mentioned, the kind of port of Rotterdam environment, where the type of sensor network.

**Speaker_03** [08:49:29]: So now imagine you get nuclear reactors.

**Speaker_03** [08:49:31]: So the way these things are usually operated is you have to have an information coordinate around you, and no information you're out of you.

**Speaker_03** [08:49:38]: This means if you want to see data from the reactor, you have to go to the reactor, you have to go to the reactor.

**Speaker_03** [08:49:41]: And if you want to send a command to the reactor, you definitely have to be inside the reactor with it.

**Speaker_03** [08:49:46]: So I think QKD gives the opportunity to do some networking here.

**Speaker_03** [08:49:48]: I don't want to... I don't know, sort of, I don't know, projecting the tubers there, but it is a kind of encryption that is so strong that you could imagine extending, like, linking together to use secure science and allowing secure remote command of things like that.

**Speaker_03** [08:50:01]: Maybe not to move your laptop, but something of a similar level.

**Speaker_03** [08:50:04]: You can also think about, like, energy grits, so, you know, you have this kind of, connected devices that are scaled on supply to different regions of the city.

**Speaker_03** [08:50:12]: So these are transformers and low balancing algorithms.

**Speaker_03** [08:50:15]: And all of that is vulnerable to attack.

**Speaker_03** [08:50:16]: So someone can get into one of these networks, send a few out of commands.

**Speaker_03** [08:50:20]: I've also been told that these millions of us arrive into the UAE, but in a lot of countries, these facilities, these low balancing sites and transformers, are comprised of a big mixture of hardware

**Speaker_03** [08:50:46]: account and it doesn't know what the school is plugged into.

**Speaker_03** [08:50:50]: These devices were made many, many years ago.

**Speaker_03** [08:50:51]: So in that context, they rely very, very heavily on the commands coming from an authorized control center, which has got a complete control center.

**Speaker_03** [08:50:58]: And that's why it's so easy to load a bug by sending a malformed command.

**Speaker_03** [08:51:02]: So I think the way these guys work is in most of these facilities, they have a They have a security policy where if there's any unauthorized access to the network, they shut it down.

**Speaker_03** [08:51:11]: So this means the attacker doesn't actually have to break anything, they just have to go on there and create a file.

**Speaker_03** [08:51:14]: That would be enough to shut the whole place down until they fix the problem.

**Speaker_03** [08:51:17]: So that sounds like quite a vulnerable place to be.

**Speaker_03** [08:51:20]: And again, I feel like if all commands have to be signed with a key gate key that came from the authorized location, that would raise the difficulty of these attacks also.

**Speaker_03** [08:51:30]: And so anyone operating a large network with outside could be interesting.

**Speaker_03** [08:51:37]: So I think you can imagine now water and you can imagine, you know, you can imagine basically anything good with the structure, like traffic lights or something.

**Speaker_03** [08:51:44]: Should we see movies where they make all the traffic lights go around?

**Speaker_03** [08:51:45]: These are places where you could cause a lot of harm quite easily.

**Speaker_03** [08:51:47]: And so adding this layer of protection might

**Unknown speaker** [08:51:50]: be quite a reason for you.

**Speaker_05** [08:51:52]: Thank you so much for this conversation.

**Speaker_05** [08:51:57]: I would like to go like what are the limitations or

**Unknown speaker** [08:52:02]: the challenges currently considering you already

**Speaker_01** [08:52:05]: present

**Speaker_06** [08:52:07]: in ADGM Academy?

**Speaker_06** [08:52:11]: Yes, I am.

**Speaker_06** [08:52:11]: Can you repeat the question?

**Speaker_06** [08:52:12]: What are the limitations

**Unknown speaker** [08:52:19]: and what are the challenges concerning the feedback so far, and what is the facility plan

**Speaker_03** [08:52:29]: in the coming years of what is possible to add on features, to the counter or end of the search concerns.

**Speaker_03** [08:52:34]: Good question.

**Speaker_03** [08:52:34]: I think we should go into the step more into the talk.

**Speaker_03** [08:52:35]: So in terms of challenges, we've been deploying this technology.

**Speaker_03** [08:52:38]: I can tell you what wasn't a challenge in Asia, which would be a challenge in West Bay.

**Speaker_03** [08:52:40]: So this is access

**Unknown speaker** [08:52:40]: to flight.

**Speaker_03** [08:52:40]: So because the technology is a single part of the line, we really need to dedicate fire.

**Speaker_03** [08:52:45]: So the good news is it does work with normal telecommunication staff, but we don't have to use exotic fire, but we do need to have private fire.

**Speaker_03** [08:52:51]: And so the wider setting, that's challenging.

**Speaker_03** [08:52:53]: It's very usual that some entity has a darn fire array between two of its facilities, essentially just government and large scale administrators.

**Speaker_03** [08:53:01]: So within ADGM, we have private fiber right between the buildings.

**Speaker_03** [08:53:07]: So there is a network that's actually a number of who owns an ADGM in this group, right?

**Speaker_03** [08:53:12]: So we were able to use that network and there was a spare capacity, spare fiber, so we didn't have to pull new fibers between buildings.

**Speaker_03** [08:53:16]: But that's usual challenge, so securing this connectivity.

**Speaker_03** [08:53:18]: We are working to coexist with other data in the same fiber.

**Speaker_03** [08:53:23]: That's possible.

**Speaker_03** [08:53:23]: Using different wavelengths, you can shift to a slightly different color of light.

**Speaker_03** [08:53:26]: That's already done.

**Speaker_03** [08:53:26]: So the reason why you can have fiber to the house in order to pay for a dark fiber.

**Speaker_03** [08:53:30]: is that your traffic is happening on a very slightly different color of light to your neighbors traffic and they can be separated efficiently.

**Speaker_03** [08:53:38]: What we have is that even one photon can cause problems.

**Speaker_03** [08:53:40]: So we struggle with scattering losses in these systems.

**Speaker_03** [08:53:42]: But it's something we're working on and we should be able to bring this capability to our existing system in the next few months.

**Speaker_03** [08:53:47]: So that's one thing.

**Speaker_03** [08:53:48]: But that's really the main challenge, right?

**Speaker_03** [08:53:50]: So scaling it out, physical key distribution requires these physical connections.

**Speaker_03** [08:53:54]: And it's in general, it's very unusual to find a use case where you have these kind of pre-existing point-to-point connections.

**Speaker_03** [08:54:00]: So it's also arranged a little.

**Speaker_03** [08:54:03]: So QKD requires that single part of the client to actually get to the final destination, right?

**Speaker_03** [08:54:07]: And say if that's 100-1, there's a fiber required, the chance of that photon actually reaching there is about 100%.

**Speaker_03** [08:54:13]: This

**Speaker_03** [08:54:22]: means that you have to send 100 photons to get one receive.

**Speaker_03** [08:54:25]: Remember, I can't send, I can't end the time, I can't send more thoughts, because that's when my security comes from, so you'll open a challenge.

**Speaker_03** [08:54:28]: In practice and record, this is about the range for this.

**Speaker_03** [08:54:29]: If you're looking to academic officials, this is a fantastic work from the earth to my own.

**Speaker_03** [08:54:31]: Twin fields, QKU schools, and they're now pushing up the fire range at something like a thousand words.

**Speaker_03** [08:54:33]: But those technologies are much higher to do.

**Speaker_03** [08:54:36]: And in practice, in fact, in China, about 50, this is what they're using for their internal business.

**Speaker_03** [08:54:40]: And this then means that if you want to connect, say, an office building Dubai with a data center somewhere in Abu Dhabi, you're going to have to go through what we call trusted knowledge.

**Speaker_03** [08:54:51]: And there's a point where this quantum guarantee is going to be supported, right?

**Speaker_03** [08:54:54]: So let's say I take QFD between here and somewhere in Yassan, and I have a know of them.

**Speaker_03** [08:54:58]: And then I have another know of, let's say, Jabal Ali or something.

**Speaker_03** [08:55:01]: And then another know of the Dubai International Financial Center.

**Speaker_03** [08:55:02]: So what happens you have QKD between each pair of those points, but at least you have the data of a key to store in classical form one of the zeros in a database, not the people.

**Speaker_03** [08:55:15]: So you rely on that data being properly protected so that should be like acquisition of a code between other people, etc, etc.

**Speaker_03** [08:55:21]: You can do this, of course, but that's what we call a trusted node.

**Speaker_03** [08:55:23]: And then you relay the key down the loop.

**Speaker_03** [08:55:25]: So essentially each node encrypts the upstream key with the downstream key that falls on.

**Speaker_03** [08:55:30]: challenge.

**Speaker_03** [08:55:32]: I also think it's an opportunity.

**Speaker_03** [08:55:35]: So like really challenges with us, actually.

**Speaker_03** [08:55:36]: So if you build a sophisticated image of such parents across the country, then you should have a lot of resilience.

**Speaker_03** [08:55:41]: You should build a round queue through this network in lots of interesting ways.

**Speaker_03** [08:55:43]: And the thing that's happening in which you will have to do the sufficient results that people would think and it's more social because you have to trust the integrity of all these trusted networks.

**Speaker_03** [08:55:52]: So again, if you're like a large organization, like any of the banks that have branch networks, you know, you might be able to trust your own network, but you might not want to trust the network if you're a rival bank, because you're using the same fibers, right?

**Speaker_03** [08:56:07]: So finding a way to coexist on a trusted network might be a social challenge or so, but it's not exactly the same.

**Speaker_03** [08:56:10]: So we have to see a bunch of networks and there are routing strategies through such networks that minimize the amount of trust you have.

**Speaker_03** [08:56:22]: I'm just how do I connect from Abu Dhabi to say New York.

**Speaker_03** [08:56:30]: This is way too far.

**Speaker_03** [08:56:32]: So think about how many 54.5 seconds are we need to get there.

**Speaker_03** [08:56:36]: I'm not even sure how you would get lost to the analytics, right?

**Speaker_03** [08:56:39]: But this really is not possible, especially in the words you would need to call something like a dozen countries.

**Speaker_03** [08:56:43]: And that means trusting facilities in a dozen different jurisdictions, I think, that's right.

**Speaker_03** [08:56:47]: They were built by different countries, I'm calling different laws to use.

**Speaker_03** [08:56:48]: So it gets a bit far-fetched, I think.

**Speaker_03** [08:56:49]: So the solution there is to go to free space in South Carolina.

**Speaker_03** [08:56:51]: With satellites, you can effectively have one satellite that does a key statement to the ground.

**Speaker_03** [08:56:58]: And now you have a key player between the ground site and satellite.

**Speaker_03** [08:57:01]: But the satellites are lower forward, like the space station, so it flies around the world every 90 minutes.

**Speaker_03** [08:57:06]: And as it passes over these points, it does that key exchange with points all over the place.

**Speaker_03** [08:57:10]: And then the satellite maintains a key database between many different ground solutions.

**Speaker_03** [08:57:13]: And it can do the exact same key following here I just described as we only see once.

**Speaker_03** [08:57:16]: So effectively with a single satellite, you can build a trusted low network that goes the entire want to trust today.

**Speaker_03** [08:57:25]: And so we are working on this, we have a ground station now off, which is ready to go.

**Speaker_03** [08:57:29]: Fortunately, only people that are working on a constant sight line, which you need, and for geophysical reasons, they're still have to work with them.

**Speaker_03** [08:57:35]: But we, we know a few of these, there's a UK-Singapore satellite, which last year, so this is going to remind you.

**Speaker_03** [08:57:38]: So we should have a few opportunities to start working.

**Speaker_03** [08:57:39]: Basically, that's kind of the next level of this architecture.

**Speaker_03** [08:57:42]: And again, it's, as soon as we've built the So it's an architecture

**Unknown speaker** [08:58:14]: that's required, it seems to go to

**Speaker_03** [08:58:15]: ground up.

**Speaker_03** [08:58:15]: That's very difficult

**Unknown speaker** [08:58:16]: to

**Speaker_03** [08:58:16]: get

**Speaker_04** [08:58:16]: them

**Speaker_01** [08:58:16]: to

**Speaker_04** [08:58:16]: fund

**Speaker_01** [08:58:16]: that architecture

**Unknown speaker** [08:58:16]: until you fund it.

**Unknown speaker** [08:58:17]: That's what it says.

**Unknown speaker** [08:58:17]: But we are now working.

**Unknown speaker** [08:58:18]: And the textbook.

**Speaker_04** [08:58:18]: I have a question when it comes to the blockchain digital asset space.

**Speaker_04** [08:58:23]: How do you compare QKD to post-quantum photography?

**Speaker_04** [08:58:27]: Like, do they compliment each other, do they compete with each other?

**Speaker_04** [08:58:31]: And I'd love to hear your personal take on what is your timeline when the quantum can.

**Speaker_04** [08:58:36]: Because when you've read

**Unknown speaker** [08:58:38]: for, yeah, cracking smart contracts, are safe.

**Speaker_03** [08:58:44]: in that they achieve a similar thing, not exactly the same thing, but they achieve something similar and they're doing very different ways.

**Speaker_03** [08:58:50]: So specifically when it comes to blockchain, I don't think it's possible to do a widely distributed global blockchain that doesn't use some public key infrastructure.

**Speaker_03** [08:58:59]: And QKD, you can't do public key infrastructure.

**Speaker_03** [08:59:03]: So you can do a symmetric infrastructure watching, but the use case are now really restricted to private single use of watching.

**Speaker_03** [08:59:14]: So again, I think I mentioned MRO earlier.

**Speaker_03** [08:59:15]: It's the only place I know where they're definitely going so great.

**Speaker_03** [08:59:18]: You know, like you have each screw is lent to the watch and watch.

**Speaker_03** [08:59:20]: Sounds extremely tedious, but I believe that's what keeps it safe from the final point.

**Speaker_03** [08:59:23]: So apart from that, that's kind of why they're a country.

**Speaker_03** [08:59:27]: So we obviously need some way of doing public infrastructure if we want to continue to have options.

**Speaker_03** [08:59:32]: And that's where PQC is definitely important.

**Speaker_03** [08:59:35]: And I'm encouraged to see that it's finally getting away and pushing out.

**Speaker_03** [08:59:39]: So that's super important.

**Speaker_03** [08:59:42]: I think there are specific blockchains that are got greatness.

**Speaker_03** [08:59:44]: planned up very similar to that.

**Speaker_03** [08:59:51]: In terms of when, when quantum computers will be able to be able to reach smart contractors.

**Speaker_03** [08:59:59]: It's kind of a lot of the underlying cryptographic primitives that are used to those smart computers are.

**Speaker_03** [09:00:04]: But if they're factoring, or if they're screwed up on them, then we know that as soon as a quantum computer reaches, I think the current estimate is there's an order of like 60 to 10,000 logical computers that would be able to run short programming and divide the private key from the computer, which

**Speaker_03** [09:00:12]: is a problem, right?

**Speaker_03** [09:00:12]: That's what we're learning

**Unknown speaker** [09:00:13]: about.

**Speaker_03** [09:00:13]: So that's a projected announcement.

**Speaker_03** [09:00:19]: of these.

**Speaker_03** [09:00:22]: You can have a financial incentive to see if you'll be optimistic about those timelines.

**Speaker_03** [09:00:34]: If we'll tell you that will happen in 2030. I don't think so personally that could happen, definitely could happen.

**Speaker_03** [09:00:37]: We should act as if that's going to happen.

**Speaker_03** [09:00:39]: But I think it's more likely to happen, like, five years later.

**Speaker_03** [09:00:42]: So in terms of the technology development, we need to have the last field is fantastic, but we're going to do it.

**Speaker_03** [09:00:45]: So we saw error correction, that's already happened.

**Speaker_03** [09:00:46]: So now there are no remaining like physics or infrastructure challenges that tell you the capital.

**Speaker_03** [09:00:48]: and pretty much all the major modalities, so for example, I always have super empty keywords, they've all demonstrated the space power.

**Speaker_03** [09:00:56]: So they don't have any existential barriers to building such a large computer.

**Speaker_03** [09:00:59]: It's now just an engineer.

**Speaker_03** [09:01:03]: Well, I have a lot of engineering problems, maybe I'm an engineer.

**Speaker_03** [09:01:05]: Just like engineering excuse, that's quite close to the cost of paying.

**Speaker_03** [09:01:12]: But I think it was here.

**Speaker_03** [09:01:13]: I don't see any particular reason why any of these guys can't build a lot of stuff or maybe, you know, paid by the end of this, like, maybe 10 years time.

**Speaker_03** [09:01:19]: There are lots of other things that could slow it down.

**Speaker_03** [09:01:20]: For example, there's a ton of hype around the massive hype around it.

**Speaker_03** [09:01:23]: So all of these companies have very, very large valuations, which are probably not supported by the next five year or above.

**Speaker_03** [09:01:27]: So investors could get a bit of a dissolution, I could call the money out and I could slow down the head on.

**Speaker_03** [09:01:35]: So there are things that could happen and slow down.

**Speaker_03** [09:01:39]: But I told you if there's any chance we're not going to see a cryptographed real long appeal in the next, say, 15, 20 years, that will take me up.

**Speaker_03** [09:01:44]: It could happen in five years.

**Speaker_03** [09:01:46]: And there's actually a company called Evolution Cube, out of Canada.

**Speaker_03** [09:01:48]: They have a guy called Michela Mosca, who's already famous in this QKD advocacy space.

**Speaker_03** [09:01:56]: where they were surveying and cryptography specialists and key gauge and public community specialists.

**Speaker_03** [09:02:02]: Basically the question that goes with something like what's the date push and the balance of probabilities that there will be a conflict versus not.

**Speaker_03** [09:02:10]: And they sort of played the statistics of people's answers and a couple of percent.

**Speaker_03** [09:02:13]: They showed that these experts who are very well informed on the topic, When they first start obtaining this, they were saying that it was like a 2% or 3% chance in five years.

**Speaker_03** [09:02:23]: And again, McKellar was telling me, in what industry would a 2% or 3% chance of a complete catastrophe get up?

**Speaker_03** [09:02:30]: So he thought that the very first result said, we should act right now.

**Speaker_03** [09:02:33]: And since then, we're now up to like double digit percentage chance that will happen in the next five years.

**Speaker_03** [09:02:37]: So again, it's unclear why he thinks it's insane.

**Speaker_03** [09:02:39]: that insurance companies aren't forcing people to migrate, pushing and it's right and right away.

**Speaker_03** [09:02:46]: So I think it is a fairly management problem.

**Speaker_03** [09:02:49]: Most of us are going to stay in the genre.

**Speaker_03** [09:02:50]: So it's also a disaster.

**Speaker_03** [09:02:52]: I'm glad to see the amazing of the society in all the ways that just unfortunately get a regular existing practices.

**Speaker_03** [09:02:58]: That's a sort of unfortunate side effect.

**Speaker_03** [09:03:00]: But definitely not.

**Speaker_03** [09:03:01]: I'm sorry.

**Speaker_03** [09:03:03]: Amber and Bob also asked me to mention something so I didn't mention this talk because it's kind of new.

**Speaker_03** [09:03:07]: We are planning to upgrade the QK network.

**Speaker_03** [09:03:10]: We have the side agent.

**Speaker_03** [09:03:11]: We're going to add a bit more of the structure.

**Speaker_03** [09:03:13]: So at this point I mentioned there's like an ID sec tunnel running between the three different sites.

**Speaker_03** [09:03:18]: So you can connect a computer to the one node in the corner of the room actually over there.

**Speaker_03** [09:03:21]: So you can connect a machine to this node and then communicate secure machine on one of the other nodes.

**Speaker_03** [09:03:25]: But we're going to add a couple layers above that.

**Speaker_03** [09:03:28]: So we're going to upgrade our key management layer to be able to support direct application access to the ultimate keys.

**Speaker_03** [09:03:33]: And we're also talking to a couple of international partners who have a key-key awareness software.

**Speaker_03** [09:03:38]: So some of these are more sophisticated KMS layers, e-fusion programs that should have some image.

**Speaker_03** [09:03:43]: We haven't understood them, but it's the kind of thing we're thinking about.

**Speaker_03** [09:03:46]: So more sophisticated key managers, they can do more sophisticated things.

**Speaker_03** [09:03:48]: They're just handing over the key on their own.

**Speaker_03** [09:03:51]: And then there are also a couple of companies that make QQKD aware, secure storage and backup solutions.

**Speaker_03** [09:03:58]: So in particular, one of these companies has a kind of, it's like a platform for using keys to shard and distribute information.

**Speaker_03** [09:04:07]: So that could be interesting to leave on this room, and that's something you're trying to bring into the network and thanks to your master.

**Speaker_03** [09:04:15]: So there'll be some, I guess, further handle on how

**Unknown speaker** [09:04:16]: to actually use this if people are thinking about this.

**Speaker_06** [09:04:17]: Andrew,

**Speaker_06** [09:04:27]: we were out of time.

**Speaker_06** [09:04:33]: That was a lot of questions for us.

**Speaker_06** [09:04:34]: No, I figured it out.

**Speaker_06** [09:04:35]: Thank you.

**Speaker_06** [09:04:35]: Thank you, everyone, for such an engaging session.

**Speaker_06** [09:04:36]: Thank you for your questions and thank you very much.

**Speaker_06** [09:04:38]: So we've reached the end to the session for now, but please, if you have any other thoughts or idea that you want to pass off, please stay a bit longer.

**Speaker_06** [09:04:44]: And thank you very much, James, for the second session.

---
*Backed up from MeetGeek on 2026-03-30 08:45*
