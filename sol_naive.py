from hours import Hours
from toy import Toy
from elf import Elf

import heapq
import santa

class Solution:

    def __init__(self, num_elves):
        self.elves = []
        for i in xrange(1, num_elves+1):
            elf = Elf(i)
            heapq.heappush(self.elves, (elf.next_available_time, elf))

    def solve(self, toys):
        hrs = Hours()
        for toy in toys:
            elf_available_time, elf = heapq.heappop(self.elves)
            work_start_time = max(elf_available_time, toy.arrival_minute)

            work_duration = elf.asign_toy(work_start_time, toy, hrs)
            heapq.heappush(self.elves, (elf.next_available_time, elf))

            yield toy.id, elf.id, work_start_time, work_duration, elf.rating


if __name__ == '__main__':
    #10 5000 Score = 33654.4601537
    #10 50000 Score = 205974.408143
    NUM_ELVES = 10
    input_file = 'toys5000.csv'
    solution = Solution(NUM_ELVES)

    santa.evaluate(NUM_ELVES, input_file, solution)


