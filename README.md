# KSP's Forum/WIKI Preservation Project

Efforts for preserving [KSP's Forum](https://forum.kerbalspaceprogram.com/) **and also** [KSP's WIKI](https://wiki.kerbalspaceprogram.com/) for the posteriority if the worst happens.

We are hoping for the best, but expecting the worst. The hard part will be to expect the worst [without causing it](https://en.wikipedia.org/wiki/Self-fulfilling_prophecy)...

## News

Forum's was down since 2024-1016, but **finally** came back to life at 2024-1028.

Forum was down again in January 22th and 23th 2025, coming back for good on 24th.

In 2025-0222, a mishap on handling the default theme's CSS rendered the site screwed. ~~Switching to any other theme works around the issue.~~ The issue is fixed since Feb 23th 8:00z.

Check the `News` section bellow.


## In a Hurry

* [News](./Docs/News)
* Downloads:
	+ Forum
		- [Internet Archive](https://archive.org/details/KSP-Forum-Preservation-Project)
			- Internet Archive's Collections as from 2024-1124], is fully operational.
			- It's updated to the latest release.
		- ~~[buzzheavier.com](https://buzzheavier.com/fl/GaCLgPsR4AA?orderby=createdAt&orderdir=desc&page=1)~~
			- I just detected (2024-1124) that the buzzheavier downloads were removed. (sigh)
			- ~~I was reticent to upload the current archived material on some fishy fire sharing site, but things are what things are.~~
			- ~~Monitor this site's reputation [here](https://www.urlvoid.com/scan/buzzheavier.com/). If anything fishy is reported, consider avoiding downloading from this one.~~
			- And remember, all the files on the dataset are **signed**. Check that signatures!
		- Others?
			- As long doesn't costs me money neither remove the files if nobody downloads them for some time, what ruled out Google Drive, Dropbox and GoFile. 
	+ WIKI
		- [Internet Archive](https://archive.org/details/KSP-WIKI-Preservation-Project)
		- Yeah! I finally gathered my... thingies... 🤪 together and published the WIKI material.
* [Source](https://github.com/net-lisias-ksp/KSP-Forum-Preservation-Project)
	+ [Issue Tracker](https://github.com/net-lisias-ksp/KSP-Forum-Preservation-Project/issues)
* Documentation	
	+ [Project's README](https://github.com/net-lisias-ksp/KSP-Forum-Preservation-Project/blob/mestre/README.md)
	+ [Theory of Operation](./Docs/Theory.md)
	+ [Install](./Docs/Install.md) instructions for the whole stack
	+ [Tools](./Docs/Tools.md)


## Description

With the (at the moment of this writing) recent news about the Private Division's staff being sacked and the Intercept Games (Studio that was carrying on the KSP2 development) shutdown, the whole franchise entered into a limbo - causing fears that, perhaps, support for the Forum could cease.

Losing more than 10 years of historical content, as well know-how on how mod the game would be, well, terribly unfortunate to say the least!

We already have the [Internet Archive](https://web.archive.org/web/*/forum.kerbalspaceprogram.com) but, as a matter of fact, it's unwise to have all your eggs on the same basket (most of us have only two, to be honest!) and the bigger the guy, the worst is the fall. Internet Archive had already suffered a (unjust) [big loss on a lawsuit](https://www.techdirt.com/2024/06/20/500000-books-have-been-deleted-from-the-internet-archives-lending-library/) that ended up with the lost of 500.000 ebooks that were being (legally, to be clear) available.

Concerning Kerbonauts are, so, gathering together on efforts to preserve that wonderful content if the worst happens.

However, doing that indiscriminately will hurt Forum, prompting someone to take down the initiative - being the reason I decided to go WARC on the thing, so we can share between us the archives saving Forum's some bucks in bandwidth. Additionally, since anyone can do their own archive and compare the results, this will keep people (including me) honest. There're legally abiding terms published on this Forum, and any change on some of them would be considered fraud - having more people with the same data is a safety measure for everybody involved, as we can support each other in the case of a dispute.

Plain mirroring the site is a bad idea. In order to have a chance to survive, the Archives must try their best to be plausibly considered fair use on a Court, not to mention gathering people to support on our case, prompting TTWO (or anyone that ends up buying the ~~lemon~~ IP) to consider any earnings on taking the thing down versus the drawbacks on P/R and deciding it's their best interest not to intervene in a destructive way.

However, we need to help them to help us (willingly or not). So we need to address some elephants in the room:

* Impersonation
	+ Dude, this is absolutely a no-go. Under no circumstances one can republish Forum's data in a way that may lead people to believe that you are them. So you just can't publish a mirror of the thing *ipsi litteris* using a different URL.
* Plagiarism
	+ *Ditto*! If you change the content in an attempt to prevent the Impersonation, you are... well... changing the IP and publishing a derivative!!! This is piracy, simple like that.
* Copyright
	+ Our best hope of success is to rely on the Copyright loopholes that **may** allow us to legally do this stunt.

Given the above considerations, I concluded that going Internet Archive is the most viable solution. The Look and Feel makes absolutely sure you are not impersonating Forum or TTWO, the content is preserved (preventing plagiarism) and since the Internet Archive managed to legally publish their archives, this is a precedent that we may use to do the same.

TTWO (or whoever ends up buying the ~~lemon~~ IP) will always have the right to file a DMCA on anyone publishing such Archive, however. To tell you the true, they can do it even on our personal sites about the franchise (see [Nintendo](https://news.ycombinator.com/item?id=35597493). So let's discourse about what would prompt them to do that:

1. Risk of losing control of the IP
2. Devaluation of the IP
3. Lost of revenue (direct or indirect)
4. Someone on TTWO waking up in a bad mood in the morning

Going Internet Archive style mitigates the Risk 1 and Risk 2 - as a matter of fact, having this content preserved in case of the worst may even salvage some of the IP's value, as invaluable content to reboot the Community will be still available to anyone owning the Franchise in the future - it's notorious that even Nintendo had to rely on "backup sites" to be able to publish themselves some of the ROMs they sold in cartridges in the past!

The Risk 3 is something we don't have to worry about, as Forum doesn't generate direct revenue - and the indirect ones we had covered by mitigating Risks 1 e 2.

About the Risk 4, the only defence we have is P/R. They had a **huge** backslash on the KSP2 drama, and that hurts - right now I'm pretty sure there's someone there overviewing everything to prevent another one. Bad P/R costs them money, huge amounts of money. And they are on the game (pun not intended) for the money.

So, as long we manage to help them to help us (willingly or not), we have a reasonable chance to score this stunt.

(Ab)using a bit the Game Theory, these are the possible outcomes (as long we stick to the rules I'm trying to delineate):

1. We do the Archiving, the Forum survives: Content preserved.
2. We do the Archiving, the Forum dies: Content preserved.
3. We do not do the Archiving, the Forum survives: Content preserved.
4. We do not do the Archiving, the Forum dies: Content is lost.

Since our main (and only) goal is the survival of the Content (as nobody here is going to make any money, directly or indirectly, with it), where are the better chances of saving the Content? Well, doing the Archive ourselves. So the logical decision is **doing the Archive**.

But, by then, we risk being taken down on a DMCA, right? What are the possible outcomes?

1. Forum survives, TTWO issues a take down on the Archives: Content preserved.
2. Forum survives, TTWO ignore the Archives: Content preserved.
3. Forum dies, TTWO ignore the Archives: Content preserved.
4. Forum dies, TTWO issues a take down on the Archives: Content is lost.

Again, since our goal is the preservation of the Content, it's our best move to do the Archiving the same. What matters if TTWO takes them down in the future, as long Forum is alive? And if Forum ever dies, it's still their best interest to preserve the content as any future reboot of the franchise would benefit from it. Heck, I would not be surprised if someone on TTWO ends up making a copy of our Archives for them.

### Notes about WIKI

The WIKI is licensed under [CC-BY-SA 3.0](https://wiki.kerbalspaceprogram.com/wiki/Kerbal_Space_Program_Wiki:Text_of_Creative_Commons_Attribution-ShareAlike_3.0_Unported_License) and so no special care is needed - but keep in mind that KSP's trademarks [still apply](https://wiki.kerbalspaceprogram.com/wiki/Kerbal_Space_Program_Wiki:General_disclaimer)!


## DISCLAIMER

We are not cheap work force. We are not doing it for "them".

We are doing it for ourselves in a way that "they" would also be benefited, we are working to achieve a win-win situation.

Yes, they royally screwed the pooch and there's a chance we would be helping to save their sorry arses. But we are doing it to save our own - saving theirs is a compromise to enhance our chances. 😉

[Stone Soup](https://en.wikipedia.org/wiki/Stone_Soup).


## References

* Forum
	+ [KSP Forums Archival Options.](https://forum.kerbalspaceprogram.com/topic/225368-ksp-forums-archival-options/)
	+ [Wiki migration plan?](https://forum.kerbalspaceprogram.com/topic/225405-wiki-migration-plan/)
	+ Historical Context 
		- [IGN reports: T2 wants to get rid of the IP, they want to offload PD completely.](https://forum.kerbalspaceprogram.com/topic/224984-ign-reports-t2-wants-to-get-rid-of-the-ip-they-want-to-offload-pd-completely/)
		- [Take Two Interactive (Rockstar, 2K, Private Division) canceling games, ending projects and laying off 5% of its workforce](https://forum.kerbalspaceprogram.com/topic/224485-take-two-interactive-rockstar-2k-private-division-canceling-games-ending-projects-and-laying-off-5-of-its-workforce/)
		- [Bad Gateway,Possible End,Theories,Solutions.](https://forum.kerbalspaceprogram.com/topic/225145-bad-gatewaypossible-endtheoriessolutions/#comment-4404679)
		- [An update of sorts from your forum moderation team.](https://forum.kerbalspaceprogram.com/topic/225365-an-update-of-sorts-from-your-forum-moderation-team/)
		- [500,000 Books Have Been Deleted From The Internet Archive’s Lending Library](https://www.techdirt.com/2024/06/20/500000-books-have-been-deleted-from-the-internet-archives-lending-library/)
* Toolset
	+ [`pywb`](https://github.com/webrecorder/pywb) Core Python Web Archiving Toolkit for replay and recording of web archives 
		- [Manual](https://pywb.readthedocs.io/en/latest/manual/)
		- [`wombat`](https://github.com/webrecorder/wombat) Wombat.js client-side rewriting library 
		- [`outbackcdx`](https://github.com/nla/outbackcdx) Web archive index server based on RocksDB 
		- [`cdxj-indexer`](https://github.com/webrecorder/cdxj-indexer) CDXJ Indexing of WARC/ARCs 
	+ [`waybackpack`](https://github.com/jsvine/waybackpack) Download the entire Wayback Machine archive for a given URL. 
	+ [`waybackpy`](https://github.com/akamhy/waybackpy) Wayback Machine API interface & a command-line tool
	+ [`scrapy`](https://scrapy.org/) An open source and collaborative
	+ [replayweb.page ](https://github.com/webrecorder/replayweb.page) A WARC player in your own browser, without relying on (yours or 3rd parties) servers.
* Known publicly available efforts
	+ [Internet Archive](https://web.archive.org/web/*/forum.kerbalspaceprogram.com)
	+ [forum.kerbalspaceprogram.com_202305](https://archive.org/details/forum.kerbalspaceprogram.com_202305)
	+ [bizzehdee's dataset](https://github.com/bizzehdee/kspforumdata)
* Relevant Material
	+ [Welcome to the Internet Archive Developer Portal](https://archive.org/developers/index.html)
		- [Internet Archive Tasks API](https://archive.org/developers/tasks.html)
	+ [Internetarchive on github](https://github.com/orgs/internetarchive/repositories)
	+ [Wayback Archiver](https://github.com/wabarc)
	+ [iipc's Awesome Web Archiving document](https://github.com/iipc/awesome-web-archiving)
	+ [Warchaelogy](https://nlnwa.github.io/warchaeology/) - in go
		- [warcrefs](https://github.com/arcalex/warcrefs) for Java lovers
* Outage
	+ Internet Archive was down from 2024-10-11 to 22.
		- Then gone down again at [2024-10-22](https://www.reddit.com/r/DataHoarder/comments/1g9wg5z/i_didnt_realize_how_much_i_used_it_until_this/#lightbox).
		- Apparently is back as from [2024-10-23](https://www.reddit.com/r/DataHoarder/comments/1gaqg0r/were_so_back/)
	+ Forum was down between [2024-10-16 and 2025-10-28](https://github.com/net-lisias-ksp/KSP-Forum-Preservation-Project/tree/master/Docs/News).
