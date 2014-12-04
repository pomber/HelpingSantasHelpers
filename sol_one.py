from hours import Hours
from toy import Toy
from elf import Elf
from operator import itemgetter
from sortedcollection import SortedCollection

import sys
import heapq
import santa

class Solution:

    def __init__(self, num_elves):
        self.elves = []
        for i in xrange(1, num_elves+1):
            elf = Elf(i)
            heapq.heappush(self.elves, (elf.next_available_time, elf))

        self.pending_toys = SortedCollection(key=itemgetter(1))

    def solve(self, toys):
        hrs = Hours()
        next_toy = None
        current_time = 540  # Santa's Workshop opens Jan 1, 2014 9:00 (= 540 minutes)

        while True:
            next_elf_time, elf = heapq.heappop(self.elves)
            current_time = max(current_time, next_elf_time)

            if (next_toy != None):
                self.pending_toys.insert((next_toy, next_toy.duration))
                next_toy = None

            for toy in toys:
                if (toy.arrival_minute <= current_time):
                    self.pending_toys.insert((toy, toy.duration))
                else:
                    next_toy = toy
                    break

            if (len(self.pending_toys) == 0 and next_toy == None):
                raise StopIteration()

            if (len(self.pending_toys) == 0):
                current_time = next_toy.arrival_minute
                break

            remaining_time = hrs.get_remaining_sanctioned_time(current_time)
            
            try:
                toy, duration = self.pending_toys.pop_le(remaining_time)
            except ValueError:
                toy, duration = self.pending_toys.pop_le(sys.maxint)
            
            work_duration = elf.asign_toy(current_time, toy, hrs)
            heapq.heappush(self.elves, (elf.next_available_time, elf))

            yield toy.id, elf.id, current_time, work_duration


if __name__ == '__main__':
    #10 5000 Score = 32179.754561
    #10 50000 Score = 200735.006972
    NUM_ELVES = 1
    input_file = 'toys5000.csv'
    solution = Solution(NUM_ELVES)

    santa.evaluate(NUM_ELVES, input_file, solution)



