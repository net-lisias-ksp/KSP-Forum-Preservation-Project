#!/usr/bin/env bash

while true; do
	echo "Started ad `date`"
	./connect
	./site_complaints
	./report_http
	python ./report_chart.py
	echo "Finished at `date`"
	echo "------"
	sleep $((3600 - $(date +%s) % 3600))
done
