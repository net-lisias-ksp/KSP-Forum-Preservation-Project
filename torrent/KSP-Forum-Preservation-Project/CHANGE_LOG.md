# KSP's Forum Preservation Project :: CHANGE LOG

* 2024-0908 : Partial Scrappings for the September, 1st week
	+ Don't get attached to these files, they will be reworked next month
		+ They are here to prevent losing data if something happens on my end of the cable modem
	+ I didn't bore to update anything else here, neither signed these files.
* 2024-0902 : Scrappings for August 2024
	+ Added scrapped content for August 2024
	+ redis dump is back
	+ Added a `ALL_URLS.csv` with all the URLs ever crawled, when and classification.
* 2024-0820 : MOAR Cleaning up
	+ Added `*-legal.warc` file with the Forum's and TTWO's legalese in a single packet
		- These terms are not hosted on Forum, so I cooked a dedicated spider just for them.
			- Ended up helping me out to understand some mistakes on the Forum's spider! :)
		- I don't expect these are going to change anytime soon - but, better safe than sorry.
	+ Some dirty was found left on the 202407 scrappings. Cleaned them out.
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
	+ Adds scrapped content up to July 30th
* 2024-0806 : Republish
	+ Previous content was audited and cleaned up
		- Removed non html content that leaked from the main `WARC`s
		- Removed `HTTP 5xx` responses (and respective requests)
		- Includes the 202305 content that was added *ipsi literis*
	+ Adds scrapped content up to July 28th
* 2024-0729 : Adding signatures
	+ Adds RSA signatures for all artefacts
* 2024-0728 : First public Release
	+ Stuff from [202305](https://archive.org/details/forum.kerbalspaceprogram.com_202305) added for conveniency
	+ My own scrappings from July 13th to 27th
	+ [Forum Announce](https://forum.kerbalspaceprogram.com/topic/225368-ksp-forums-archival-options/?do=findComment&comment=4411089)