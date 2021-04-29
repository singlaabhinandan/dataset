import csv
import numpy

def calculate_scan_latencies(filename):
    scan_latencies = []

    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            nth_lat_str = row[-1]
            nth_lat_val = nth_lat_str.split(":")[-1]
            val = nth_lat_val.strip()
            scan_latencies.append(float(val))

    print( filename,':',numpy.percentile(scan_latencies, 95))

calculate_scan_latencies("stats1")
calculate_scan_latencies("stats2")
calculate_scan_latencies("stats3")