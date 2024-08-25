'''
Created on Apr 1, 2023

@author: lisias
'''

import os, sys
import pygal
import datetime
import csv

def cvs_load_connect(name:str) -> dict:
	r = dict()
	path = os.path.join(".", name+".csv")
	with open(path, 'r') as csvf:
		reader = csv.reader(csvf, delimiter='\t', quotechar='"')
		for row in reader:
			date = [int(i) for i in row[0].split("-")]
			time = [int(i) for i in row[1].split(":")]
			timestamp = datetime.datetime(date[0], date[1], date[2], time[0], time[1], tzinfo=datetime.timezone.utc)
			count = int(row[2])
			r[timestamp] = count
	return r

def cvs_load_complaints(name:str) -> dict:
	r = dict()
	path = os.path.join(".", name+".csv")
	with open(path, 'r') as csvf:
		reader = csv.reader(csvf, delimiter='\t', quotechar='"')
		for row in reader:
			date = [int(i) for i in row[0].split("-")]
			hour = int(row[1])
			timestamp = datetime.datetime(date[0], date[1], date[2], hour, tzinfo=datetime.timezone.utc)
			kind = row[2]
			count = int(row[3])
			if kind not in r: r[kind] = dict()
			r[kind][timestamp] = count
	return r

def normalize_dataset(dataset:dict, target:datetime.datetime, fill_hours:bool=False) -> dict:
	for d in dataset:
		dataset[d] = { k:v for k, v in dataset[d].items() if k >= target }

	all_keys = set()
	for i in dataset:
		all_keys.update(dataset[i].keys())
	if fill_hours:
		d = min(all_keys)
		end = max(all_keys)
		while d < end:
			if d not in all_keys:
				all_keys.add(d)
			d = d + datetime.timedelta(hours=1)
	for i in all_keys:
		for j in dataset:
			if i not in dataset[j]: dataset[j][i]=0
	return dataset
				
def plot(data:dict, name:str, kind):
	fn = "report_chart-" + name.replace(' ', '-') + ".png"

	chart = kind(width=2400, x_label_rotation=45, show_minor_x_labels=False)
	chart.title = name

	sd = set()
	for k in data:
		sd.update(data[k].keys())
	sd = sorted(sd)
	chart.x_labels_major = [d for d in sd if 0 == d.minute and 0 == d.second]
	chart.x_labels = sd
	if sd[0] not in chart.x_labels_major:
		chart.x_labels_major.insert(0,sd[0])
	if sd[-1] not in chart.x_labels_major:
		chart.x_labels_major.append(sd[-1])

	for k in sorted(data.keys()):
		chart.add(k, [data[k][d] for d in sd if d in data[k]])
	chart.render_to_png(fn, 120)


def main():
	connect = cvs_load_connect("connect_log.hits-per-minute")
	complaints = cvs_load_complaints("site_complaints_log.hits-per-hour")

	all_keys = set()
	for i in complaints:
		all_keys.update(complaints[i].keys())
	target = max(min(all_keys), min(connect.keys()))

	connections = dict()
	connections['connections'] = connect

	normalize_dataset(connections, target)
	normalize_dataset(complaints, target, True)

	plot(connections, "Connections", pygal.Bar)
	plot(complaints, "Events", pygal.StackedBar)

	return 0

if "__main__" == __name__:
	sys.exit(main())
	print("END OF LINE.")
