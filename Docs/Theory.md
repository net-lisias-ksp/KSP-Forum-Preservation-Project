# KSP's Forum Preservation Project :: Theory of Operation

The way the Internet Archive / Wayback Machine works are not too different (conceptually) from a local CMS repository (like SVN). You store many different versions of a web page in a controlled and recoverable way.

The unit of storage is the [`WARC`](about:blank) file. It's, in essence, an indexable sequence of dumps from http requests and their respective responses (*ipsi literis*, including headers - specially encoded responses, as `Content-Encoding: br`, are stored exactly as received), with a special prefix header describing when, how and what the following [request/response] tuple refers to.

Obviously, sequentially accessing such WARC file (easily reaching many gigabytes in size) would be nuts, so these files are paired with [`CDX`](https://github.com/internetarchive/cdx-summary) summary files where some metadata from the `WARC` file entries are registered on a simple line record format, indexing the `WARC` file.

Due the size WARC files can reach, essentially all the tools support a `WARC.gz` file format, essentially gzipped blobs concatenated. It's usual to "recompress" a `WARC.gz` file once you done feeding it to maximise the compression ratio of the whole thing.

Of course, these are only the file formats. We need tools to filler them up.

There're many but, for our current purposes, `pywb` was chosen. This, and the other tools needed to a full setup will be described below.


## `pywb`

`pywb` have two different operating modes: **recording** and **`**replaying**`**.


### `pywb` in recording mode

wip

#### redis

wip

### `pywb` in replaying mode

wip

#### cdx-server

wip


## `scrapy`

wip
