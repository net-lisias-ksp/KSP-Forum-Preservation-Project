# KSP's Wiki Preservation Project

Efforts for preserving [KSP's Wiki](https://wiki.kerbalspaceprogram.com/) for the posteriority if the worst happens.

This is the Internet Archive's torrent entry with the scraped files. See the project's README (link below) for the gory details - I'm reusing the Forum Preservation repository to simplyfy my life.

We are hoping for the best, but expecting the worst. The hard part will be to expect the worst [without causing it](https://en.wikipedia.org/wiki/Self-fulfilling_prophecy)...


## In a Hurry

* Downloads:
	+ [Internet Archive](https://archive.org/details/KSP-WIKI-Preservation-Project)
		- Internet Archive is currently mostly down, so the download page is temporarily unavailable.
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

None at this moment.
