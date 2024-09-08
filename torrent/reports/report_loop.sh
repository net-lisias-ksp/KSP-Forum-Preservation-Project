#!/usr/bin/env bash

while true; do
	./connect
	./site_complaints
	./report_http5
	python ./report_chart.py
	sleep $((3600 - $(date +%s) % 3600))
done
