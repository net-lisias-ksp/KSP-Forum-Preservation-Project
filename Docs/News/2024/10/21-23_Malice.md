# KSP's Forum Preservation Project :: News :: 2024-1021T23:18z

## Malice?

People on Reddit are now talking about intentional attacks on Forum. And I agree.

Until recently, I was blaming AI Companies for scraping the Web to their knees - and in fact, at least some of them were.

Then a bit later, people started to get worried and tried to scrap Forum themselves (like me). Some people believed that they were the ones screwing the Forum, but I can say that someone on PD or TTWO cranked up the CloudFlare protections to a pretty indecent level, to the point that if I restarted my browser the very few pages I had opened would make CloudFlare to strike me by "abuse". Not saying it's impossible, but pretty unlikely that personal or a small group of enthusiasts could overcome CloudFlare in order to keep causing damages.

Interesting enough, Forum kept giving us the `http 5xx` salutes all the time, clearly an evidence that the (intentional or not) DDoS attack was still ongoing.

Check this report for the last week Forum was alive:

![20241016.Events.png](../../../../torrent/reports/report_chart/20241016.Events.png#FullWidth)

The coloured bars are the "normal" `5xx` errors we are getting for months. That solid green bars are Forum going down. Something happened swift as a knife cutting a throat.

This was something new.

My initial thought was someone on PD/TTWO getting fed up of this crap and pulled the plug on Forum to stop the harassment. Not an absurd thought, as some other sites had done it in the recent past.

But... Keeping Forum down for so much time is causing more damages than the harassment, so by now I **really doubt** this was what happened.

So it should be something else.

Like what happened with Internet Archive last Oct 11th (about 5 days before Forum), or last week on some private network that I'm not allowed to disclose, but at least I can casually mention that being a Fortinet customer nowadays is a invite to get some ransomware installed in your servers. Someone "out there" is out for shopping, I can guarantee you.

Now... They hit Forum for ransom? I doubt, because 13 hours later the sinister event I received a Digest mail from Forum, and this email could only be created and sent if a process on the Forum's infrastructure would be alive and accessing an equally alive database where the Topics, Threads, Posts and Profiles (the Forum's "soul") is stored. So we have a concrete confirmation that at least until 13 hours Forum got down, Forum's "soul" was still alive - but with the Front Page unable to connect to the database by some reason.

But this doesn't means that TTWO themselves weren't hit by such plague!!

If I'm right, TTWO's infra guys are buried in really deep shit right now and, frankly, restoring Forum is not on the top of their backlog at this moment. It would be, even, a liability because they need to be absolutely sure they found and fixed all the holes before restoring services.

All we can do, right now, is to wait. And, by fuck's sake, I hate having to wait.

## References

* [Reddit comment](https://www.reddit.com/r/KerbalSpaceProgram/comments/1g8lipp/comment/lt17r5s/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)
