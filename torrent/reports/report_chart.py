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

def __normalize_dataset(dataset:dict, target:tuple, increment:callable) -> dict:
	for d in dataset:
		dataset[d] = { k:v for k, v in dataset[d].items() if k >= target[0] and k <= target[1] }

	all_keys = set()
	for i in dataset:
		all_keys.update(dataset[i].keys())

	d = min(all_keys)
	end = max(all_keys)
	while d < end:
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
    
def plot(data:dict, name:str, kind, labels_filter:callable):
	now = datetime.datetime.now()
	timestamp = "{:04d}{:02d}{:02d}".format(now.year, now.month, now.day)
	fn = "report_chart." + timestamp + "." + name.replace(' ', '-') + ".png"

	chart = kind(width=2400, legend_at_bottom=True, x_label_rotation=45, truncate_label=30)
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


def main():
	connect = cvs_load_connect("connect_log.hits-per-minute")
	complaints = cvs_load_complaints("site_complaints_log.hits-per-hour")

	all_complaints_keys = set()
	for i in complaints:
		all_complaints_keys.update(complaints[i].keys())
	target_min = max(min(all_complaints_keys), min(connect.keys()))
	target_max = min(max(all_complaints_keys), max(connect.keys()))
	target_min = max(target_min, target_max - datetime.timedelta(days=8))

	connections = dict()
	connections['connections'] = connect

	normalize_dataset_minutely(connections, (target_min, target_max))
	normalize_dataset_hourly(complaints, (target_min, target_max))

	plot(connections, "Connections", pygal.Bar, lambda sd: [d for d in sd if 0 == d.minute and 0 == d.second])
	plot(complaints, "Events", pygal.StackedBar, lambda sd: [d for d in sd if 0 == d.minute and 0 == d.second])

	return 0

if "__main__" == __name__:
	r = main()
	print("END OF LINE.")
	sys.exit(r)
