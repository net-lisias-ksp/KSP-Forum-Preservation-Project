#!/usr/bin/env bash
for f in `find .. -name "*.cdxj"` ; do
	./upload-redis "redis://macmini62:6379/0/pywb:forum.kerbalspaceprogram.com:cdxj" < $f
done
