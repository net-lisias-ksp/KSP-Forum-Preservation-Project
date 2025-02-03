# KSP's Forum Preservation Project

Efforts for preserving [KSP's Forum](https://forum.kerbalspaceprogram.com/) for the posteriority if the worst happens.

This is the Internet Archive's torrent entry with the scraped files. See the project's README (link below) for the gory details.

We are hoping for the best, but expecting the worst. The hard part will be to expect the worst [without causing it](https://en.wikipedia.org/wiki/Self-fulfilling_prophecy)...


## News

Forums was down since 2024-1016, but **finally** came back to life at 2024-1028.

Internet Archive was attacked in October 2024, but it's fully operational again as November 2024.

Forum was down again in January 22th and 23th 2025, coming back for good on 24th.

Check the `News` section bellow.


## In a Hurry

* News
	+ [Forum was down... Again!](https://ksp.lisias.net/blogs/news/2024-1015_Forum-is-down/)
	+ [Forum was down](https://ksp.lisias.net/blogs/news/2025-0122_Forum-is-down-AGAIN/)
* Downloads:
	+  [Internet Archive](https://archive.org/details/KSP-Forum-Preservation-Project)
		- [Internet Archive is fully operational](https://ksp.lisias.net/blogs/news/2024-1015_Forum-is-down/2024/11/24_Archive-is-back) for me at least since 2024-1124.
	+ Others?
		- As long doesn't costs me money neither remove the files if nobody downloads them for some time, what ruled out Google Drive, Dropbox and GoFile. 
* Documentation
	+ [Project's README](https://github.com/net-lisias-ksp/KSP-Forum-Preservation-Project/blob/master/README.md)
	+ [Source](https://github.com/net-lisias-ksp/KSP-Forum-Preservation-Project)
		- [Issue Tracker](https://github.com/net-lisias-ksp/KSP-Forum-Preservation-Project/issues)


## Contents

This torrent contains:

* `WARC` files, to be used with a tool like `pywb` or anything else that knows what a `.warc` file is.
	+ unpack the `.lrz` files using [lrzip](https://github.com/ckolivas/lrzip)
		- Package list for Linux: https://pkgs.org/download/lrzip
		- On MacOS: https://ports.macports.org/port/lrzip/
		- On Windows: https://www.youtube.com/watch?v=z47kprta8Ig
			- Good luck!
* `.sig` files, with the digital signature on each artefact so you can sure whatever you have is the data I had published without tampering.
	+ a `verify.sh` `bash` script, that will verify integrity of the signed files.
+ `allowed_signers` contains the public key to be used to verify the files' signatures. It **must** be identical to the one published on the project's repo ([here](https://github.com/net-lisias-ksp/KSP-Forum-Preservation-Project/tree/master/torrent/KSP-Forum-Preservation-Project)).
+ a bunch of `.md` files with minimal documentation (like this text). Refer to the project's repository (see "Source" above) for complete ones.


## DISCLAIMER

We are not cheap work force. We are not doing it for "them".

We are doing it for ourselves in a way that "they" would also be benefited, we are working to achieve a win-win situation.

Yes, they royally screwed the pooch and there's a chance we would be helping to save their sorry arses. But we are doing it to save our own - saving theirs is a compromise to enhance our chances. ;)

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
* Known publicly available efforts
	+ [Internet Archive](https://web.archive.org/web/*/forum.kerbalspaceprogram.com)
	+ [forum.kerbalspaceprogram.com_202305](https://archive.org/details/forum.kerbalspaceprogram.com_202305) - included on this torrent for convenience
	+ [bizzehdee's dataset](https://github.com/bizzehdee/kspforumdata)
