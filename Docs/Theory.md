# KSP's Forum Preservation Project :: Theory of Operation

The way the Internet Archive / Wayback Machine works are not too different (conceptually) from a local CMS repository (like SVN). You store many different versions of a web page in a controlled and recoverable way.

The unit of storage is the [`WARC`](about:blank) file. It's, in essence, an indexable sequence of dumps from http requests and their respective responses (*ipsi literis*, including headers - specially encoded responses, as `Content-Encoding: br`, are stored exactly as received), with a special prefix header describing when, how and what the following [request/response] tuple refers to.

Obviously, sequentially accessing such WARC file (easily reaching many gigabytes in size) would be nuts, so these files are paired with [`CDX`](https://github.com/internetarchive/cdx-summary) summary files where some metadata from the `WARC` file entries are registered on a simple line record format, indexing the `WARC` file.

Due the size WARC files can reach, essentially all the tools support a `WARC.gz` file format, essentially gzipped blobs concatenated. It's usual to "recompress" a `WARC.gz` file once you done feeding it to maximise the compression ratio of the whole thing.

Of course, these are only the file formats. We need tools to filler them up.

There're many but, for our current purposes, `pywb` was chosen. This, and the other tools needed to a full setup will be described below.


## Architecture

It was decided to implement the solution in a somewhat convoluted way, recording concomitantly into 3 distinct collections:

* Content
* Images (and videos)
* Styles (css et all)

`pywb` allows us to dynamically merge the collections and serve them on a single front-end, as they were just one. Pretty convenient, and it was what allowed me to try this stunt at first place.

The rationale for this decision is simple besides not exactly straightforward: images almost never changes, as well styles. Scraping them separately will save a bit of Forum's resources and scraping time while updating the collections, as the media will rarely (if ever) change. Same for styles.

So one can just ignore them while refreshing the archive contents, focusing on what matters most. 

There's an additional benefit on keeping textual info separated from images and styles: whoever owns the Intellectual Property, owns the images and styles, **but not the textual contents**. Posts on Forum _**are** almost unrestrictedly and perpetually **licensed**_ to the Forum's owner, but they still belong to the original poster. So whoever owns the IP, at least theoretically, have no legal grounds to take down these content - assuming the worst scenario, where this Forum goes titties up and a new owner decides to take down the Forum mirrors, they will be able to do so only for the material they own - images and styling. And these we can easily replace later, forging a new WARC file pretending being that, now lost, content.

Ok, ok, on Real Life™ things doesn't work exactly like that. But it costs very little (if any) to take some preventive measures, no?

At least, there's still an another reason to separate these contents: compression.

My initial attempts let videos pass trough the filters and be stored together the textual content, and - boy... - this royally screwed up compression. The [scraps from 2023](../README.md#References) were being compressed at +/- 44/1 ratio, but my owns were being compressed "only" at 20/1.

The videos injected on the textual content were the culprit!


## Tools

### `pywb`

`pywb` have two different operating modes: **recording** and **`**replaying**`**.


#### `pywb` in replaying mode

wip

##### cdx-server

wip


#### `pywb` in recording mode

wip

##### redis

wip

### `scrapy`

wip


## Implementation

wip
