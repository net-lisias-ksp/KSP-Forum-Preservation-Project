# KSP's Forum Preservation Project :: CHANGE LOG

* 2025-0202 : Scrapings for January 2025
	+ Forum got down **again** from 22th to 24th, but it ended up being some infrastructure changes that took more time than expected.
		- No harm done, other than some dirty pants.
	+ I'm scraping Wiki too, but didn't managed to consolidate the data in time for this release.
		- I expect to be able to update this torrent with the Wiki data still this month.
* 2025-0102 : Scrapings for December 2025
	+ Contains scrapings from Dez 19th 2024 to Jan 1st 2025.
	+ Pretty uneventful month.
	+ Happy New Year!
* 2024-1201 : Scrapings for November 2024
	+ Contains scrapings from Oct 28th to Nov 30th.
	+ Pretty intense month:
		- Forum came back to life at Oct 28.
		- [BuzzHeavier was raided](http://ksp.lisias.net/blogs/news/2024-1015_Forum-is-down/2024/11/24_Archive-is-back). I will not use it anymore...
		- But [Internet Archive is fully operational](http://ksp.lisias.net/blogs/news/2024-1015_Forum-is-down/2024/11/24_Archive-is-back)!
		- I grabbed a Raspberry PI 5 to do the archiving.
			- Not as fast as the Steam Deck I was using, but way more versatile because now I have full control over the O.S.
			- And I have my Steam Deck back! :) 
* 2024-1021 : Scrapings for October 2024
	+ Sadly (I'm heart broken), Forum is down since last 16th.
		- I'm keeping an up to date News section about [here](https://ksp.lisias.net/blogs/news/2024-1015_Forum-is-down/).
	+ So, I only managed to scrap from 8th to 16th and, since until this moment nothing appears to improve on Forum, I decided to call it a Month and updated the Torrent.
		- I reserved the 1st week of October for a mini Sabbatical, as I had 4 times the workload on September. **DAMN**, I lost a whole week. :/
	+ In a way or another, I updated what I had. Let's hope for the best.
	+ See [README](./README.md) for the up to date download links
		- Because, yeah... [Web Archive is half down too](https://www.theverge.com/2024/10/14/24269741/internet-archive-online-read-only-data-breach-outage). :/
			- ***KRAP!!!***
* 2024-1002 : Scrapings for September 2024
	+ All partial `warc` files were replaced by the proper ones.
		`ALL_URLS.csv` was updated accordinly.
	+ Forum is "more or less" feature complete.
		- All known topics up to October 1st were scraped at least once.
		- From now on, the efforts will focus on:
			- Scraping missing profiles;
			- Scraping new topics;
			- update previously scraped topics when needed (low priority).
	+ New `warc` "kind" `revisits`, preseving the recorded... well... revisits. :)
		- `revisits` are not needed for playback, but will play a role now that topics and profiles should be updated regularly.
	+ `revisits` and `redirects` from 202407 and 202408 were reworked (and replaced).
		- Better sanitizing processes were applied on them.
* 2024-0924 : Partial Scrapings for the September, 3rd week
	+ *Ditto*
	+ Added `warc` file for `revisits`.
		- Not useful for replaying, but will help on crawling by remembering the last time a page was revisited, even if not changes deteced.
* 2024-0914 : Partial Scrapings for the September, 2nd week
	+ *Ditto*
* 2024-0908 : Partial Scrapings for the September, 1st week
	+ Don't get attached to these files, they will be reworked next month
		+ They are here to prevent losing data if something happens on my end of the cable modem
	+ I didn't bore to update anything else here, neither signed these files.
* 2024-0902 : Scrapings for August 2024
	+ Added scraped content for August 2024
	+ redis dump is back
	+ Added a `ALL_URLS.csv` with all the URLs ever crawled, when and classification.
* 2024-0820 : MOAR Cleaning up
	+ Added `*-legal.warc` file with the Forum's and TTWO's legalese in a single packet
		- These terms are not hosted on Forum, so I cooked a dedicated spider just for them.
			- Ended up helping me out to understand some mistakes on the Forum's spider! :)
		- I don't expect these are going to change anytime soon - but, better safe than sorry.
	+ Some dirty was found left on the 202407 Scrapings. Cleaned them out.
		- The `HTTP 301 Moved Permanently` records were moved into dedicated `WARC` files to facilitate intenal proceedings.
		- Revisits with same digest profile are now cleaned out from the `WARCball`.
			- This is saving a lot of space!
	+ Removed `redis.dump` as it became outdated and regenerating it for an old release is cumbersome.
		- Use `redo-redis` after updating your `WARC` files.
* 2024-0807 : Ubber Sanitizing & Republish
	+ Previous content was further audited, sanitized and cleaned up
		- Removed `HTTP 4xx` responses (and respective requests)
		- removed duplicated records on `files`, `images`, `media` and `styles` archives
		- completely remove anything not user generated from the main `WARC` file
	+ Adds scraped content up to July 30th
* 2024-0806 : Republish
	+ Previous content was audited and cleaned up
		- Removed non html content that leaked from the main `WARC`s
		- Removed `HTTP 5xx` responses (and respective requests)
		- Includes the 202305 content that was added *ipsi literis*
	+ Adds scraped content up to July 28th
* 2024-0729 : Adding signatures
	+ Adds RSA signatures for all artefacts
* 2024-0728 : First public Release
	+ Stuff from [202305](https://archive.org/details/forum.kerbalspaceprogram.com_202305) added for conveniency
	+ My own Scrapings from July 13th to 27th
	+ [Forum Announce](https://forum.kerbalspaceprogram.com/topic/225368-ksp-forums-archival-options/?do=findComment&comment=4411089)
