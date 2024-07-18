#!/usr/bin/env bash
for f in forum.kerbalspaceprogram.com-00000.warc.gz forum.kerbalspaceprogram.com-00000.warc.os.cdx.gz forum.kerbalspaceprogram.com-00001.warc.gz forum.kerbalspaceprogram.com-00001.warc.os.cdx.gz forum.kerbalspaceprogram.com-meta.warc.gz forum.kerbalspaceprogram.com-meta.warc.os.cdx.gz forum.kerbalspaceprogram.com_202305.cdx.gz forum.kerbalspaceprogram.com_202305.cdx.idx forum.kerbalspaceprogram.com_202305_files.xml forum.kerbalspaceprogram.com_202305_meta.sqlite forum.kerbalspaceprogram.com_202305_meta.xml ; do
	wget --continue https://archive.org/download/forum.kerbalspaceprogram.com_202305/$f
done
