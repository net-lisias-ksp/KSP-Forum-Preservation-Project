# KSP's Forum Preservation Project :: Tools

This document aims to be a "cheat-sheet" with quick hints for many different tasks needed to carry on the project.

See [Theory](./Theory.md) for a thoughtfully description.


## Downloading IA's forum.kerbalspaceprogram.com_202305

To anyone willing to download the Internet Archive data, this dataset doesn't have a torrent, unfortunately.

So I made this little script to download that huge basket of bytes using wget with the option to recover the downloads if things goes south in the process. Worst case scenario, you run the script again, no data loss. 

Here: [download-forum.kerbalspaceprogram.com_202305](../Source/bash/download-forum.kerbalspaceprogram.com_202305.sh)


## Dumping a URL from IA's into a local WARC

Source: https://github.com/openzim/warc2zim/issues/95#issuecomment-1166366024

Here: [wayback_dl.sh](../Source/bash/wayback_dl.sh)


## Extracting all URLs archived from the WARC files

```
cat *.warc | grep -a "WARC-Target-URI" | sed 's/WARC-Target-URI: //' | dos2unix | sort | uniq > uri.txt

```

## Listing all images from the `<img src="">` tags from the html archived on the WARC files.

```
cat *.warc | grep -Poa '<img[^>]*src="\K[^"]*(?=")' | dos2unix | sort | uniq > imgs.txt
```

## Listing all `Content-Type`s from the WARC files.

```
cat *.warc | grep -ae "^Content-Type: " | sed '/msgtype/d' | dos2unix | sort | uniq
```

## Internet Archive

The following commandline will dump the CDX for the pages archived by `archive.org` from the Forum. It's a good benchmark to compare with our own results.

> ATTENTION: This tool is currently untested!

```
curl http://web.archive.org/cdx/search/cdx?url=forum.kerbalspaceprogram.com/* > ia.forum-kerbalspaceprogram-com.cdx
```

And the following will extract the URLs (removing duplicates) from the CDX above:

```
cat ia.forum-kerbalspaceprogram-com.cdx | cut -d' ' -f 3 | sort | uniq > ia.uri.txt

```


## `pywb` a Python Web Archiving Toolkit for replay and recording of web archives

wip


## `lrzip` the best compression tool available today.

To compress all WARC files with maximum compression, preserving the original:

	lrz -z --best --keep *.warc

To decompress

	lrz --decompress --keep *.lrz

**ATTENTION**: this thing is **ssslloooowwwww**, but it gives us the best compression ratio available nowadays.

We are dealing with huge data files that will be shared between many, many people. This is going to save a lot of money for AWS users.

