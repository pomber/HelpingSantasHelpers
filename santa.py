import os
import csv
import math
import heapq
import time
import datetime

from hours import Hours
from toy import Toy
from elf import Elf

import evaluator

def get_toys(toy_file):
    with open(toy_file, 'rb') as f:
        toysfile = csv.reader(f)
        toysfile.next()
        for row in toysfile:
            yield Toy(row[0], row[1], row[2])

def evaluate(num_elves, input, solution):
    output = 'subm.csv'

    toy_file = os.path.join(os.getcwd(), input)
    soln_file = os.path.join(os.getcwd(), output)

    toys = get_toys(toy_file)

    result = solution.solve(toys)

    with open(soln_file, 'wb') as w:
        wcsv = csv.writer(w)
        wcsv.writerow(['ToyId', 'ElfId', 'StartTime', 'Duration'])
        for line in result:
            toy_id, elf_id, start_seconds, work_duration, rating = line
            ref_time = datetime.datetime(2014, 1, 1, 0, 0)
            #TODO pasar a hours.py:
            tt = ref_time + datetime.timedelta(seconds=60*start_seconds)
            time_string = " ".join([str(tt.year), str(tt.month), str(tt.day), str(tt.hour), str(tt.minute)])
            wcsv.writerow([toy_id, elf_id, time_string, work_duration, rating])

    evaluator.evaluate(num_elves, input, output)

        