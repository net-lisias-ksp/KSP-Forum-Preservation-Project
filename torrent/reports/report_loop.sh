#!/usr/bin/env bash

while true; do
	sleep $((3600 - $(date +%s) % 3600))
	./connect
	./site_complaints
	python ./report_chart.py
done
