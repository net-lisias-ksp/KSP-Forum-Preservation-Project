'''
Created on Apr 1, 2023

@author: lisias
'''

import os, sys
import datetime
import csv
import pygal

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

def cvs_load_responsetime(name:str) -> dict:
	r = dict()
	path = os.path.join(".", name+".csv")
	with open(path, 'r') as csvf:
		reader = csv.reader(csvf, delimiter='\t', quotechar='"')
		for row in reader:
			date = [int(i) for i in row[0].split("-")]
			time = [int(i) for i in row[1].split(":")]
			timestamp = datetime.datetime(date[0], date[1], date[2], time[0], time[1], tzinfo=datetime.timezone.utc)
			dt = float(row[2])
			r[timestamp] = dt
	return r

def __cvs_load_connect_with_bkp(name:str) -> dict:
	r1 = cvs_load_connect(name)
	r2 = cvs_load_connect(name+"_bkp")
	return __merge_connect(r1, r2)

def __cvs_load_complaints_with_bkp(name:str) -> dict:
	r1 = cvs_load_complaints(name)
	r2 = cvs_load_complaints(name+"_bkp")
	return __merge_complaints(r1, r2)

def __merge_connect(d1:dict, d2:dict) -> dict:
	r = dict()
	def merge(r:dict, d:dict):
		for k,v in d.items():
			if k not in r: r[k] = dict()
			for kk,vv in v.items():
				if kk in r[k]:
					r[k][kk] += vv
				else:
					r[k][kk] = vv
	merge(r,d1)
	merge(r,d2)
	return r

def __merge_complaints(d1:dict, d2:dict) -> dict:
	r = dict()
	def merge(r:dict, d:dict):
		for k,v in d.items():
			if k not in r: r[k] = dict()
			for kk,vv in v.items():
				if kk in r[k]:
					r[k][kk] += vv
				else:
					r[k][kk] = vv
	merge(r,d1)
	merge(r,d2)
	return r

def __normalize_dataset(dataset:dict, target:tuple, increment:callable) -> dict:
	for d in dataset:
		dataset[d] = { k:v for k, v in dataset[d].items() if k >= target[0] and k <= target[1] }

	all_keys = set()
	for i in dataset:
		all_keys.update(dataset[i].keys())

	target_min = increment(target[0])
	target_max = increment(target[1])
	d = target_min
	while d <= target_max:
		if d not in all_keys:
			all_keys.add(d)
		d = increment(d)

	for i in all_keys:
		for j in dataset:
			if i not in dataset[j]: dataset[j][i]=0
	return dataset

def normalize_dataset_hourly(dataset:dict, target:tuple) -> dict:
	return __normalize_dataset(dataset, target, lambda d: d + datetime.timedelta(hours=1) )

def normalize_dataset_minutely(dataset:dict, target:datetime.datetime) -> dict:
	return __normalize_dataset(dataset, target, lambda d: d + datetime.timedelta(minutes=1) )

def plot(now:datetime.datetime, data:dict, name:str, kind, labels_filter:callable):
	timestamp = "{:04d}{:02d}{:02d}".format(now.year, now.month, now.day)
	fn = "report_chart/" + timestamp + "." + name.replace(' ', '-') + ".png"

	chart = kind(width=2400, legend_at_bottom=True, x_label_rotation=45, truncate_label=30, fill=True)
	chart.title = name

	sd = set()
	for k in data:
		sd.update(data[k].keys())
	sd = sorted(labels_filter(sd))
	chart.x_labels = [(str(d.date()) if 0 == d.hour and 0 == d.minute and 0 == d.second else "{:s}T{:s}".format("\u00A0"*20, str(d.time()))) for d in sd]
	chart.x_labels[0] = str(sd[0])

	for k in sorted(data.keys()):
		chart.add(k, [data[k][d] for d in sd if d in data[k]])
	chart.render_to_png(fn, 120)


def do_connections_graph(now:datetime.datetime):
	connect = cvs_load_connect("connect_log.hits-per-minute")
	connections = dict()
	connections['connections'] = connect

	target_min = min(connect.keys())
	target_max = min(now, max(connect.keys()))
	target_min = max(target_min, target_max - datetime.timedelta(days=8))

	normalize_dataset_minutely(connections, (target_min, target_max))
	plot(now, connections, "Connections", pygal.StackedLine, lambda sd: [d for d in sd if 0 == d.minute and 0 == d.second])
	return now, target_min, target_max


def do_complaints_graph(now, target_min, target_max):
	some_complaints = cvs_load_complaints("site_complaints_log.hits-per-hour")
	more_complaints = cvs_load_complaints("report_http.hits-per-hour")
	complaints = __merge_complaints(some_complaints, more_complaints)

	all_complaints_keys = set()
	for i in complaints:
		all_complaints_keys.update(complaints[i].keys())
	target_min = max(min(all_complaints_keys), target_min)
	target_max = min(max(all_complaints_keys), target_max)

	normalize_dataset_hourly(complaints, (target_min, target_max))
	plot(now, complaints, "Events", pygal.StackedBar, lambda sd: [d for d in sd if 0 == d.minute and 0 == d.second])


def do_responsetime_graph(now, target_min, target_max):
	connect = cvs_load_responsetime("connect_log.time-per-connect")
	responsetime = dict()
	responsetime['responsetime'] = connect

	target_min = max(min(connect.keys()), target_min)
	target_max = min(max(connect.keys()), target_max)

	normalize_dataset_minutely(responsetime, (target_min, target_max))
	plot(now, responsetime, "Worst Response Time", pygal.StackedLine, lambda sd: [d for d in sd if 0 == d.minute and 0 == d.second])


def main(args:list):
	now = datetime.datetime.now(tz=datetime.timezone.utc)
	if len(args) > 1:
		raise ValueError("Invalid command line")
	elif len(args) == 1:
		try:
			now = datetime.datetime.strptime(args[0].lower().replace("z", "+0000"), "%Y-%m-%d %H:%M:%S%z")
		except:
			now = datetime.datetime.strptime(args[0].lower(), "%Y-%m-%d")
			now = datetime.datetime(now.year, now.month, now.day, 23, 59, 59, tzinfo=datetime.timezone.utc)
	print("Using now = {0}".format(str(now)))
	now, target_min, target_max = do_connections_graph(now)
	do_complaints_graph(now, target_min, target_max)
	do_responsetime_graph(now, target_min, target_max)
	return 0

if "__main__" == __name__:
	r = main(sys.argv[1:])
	print("END OF LINE.")
	sys.exit(r)
