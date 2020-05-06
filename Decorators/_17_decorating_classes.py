

# from decorators import debug, timer
from _11_timing_functions import timer
from _12_debugging_code import debug

class TimeWaster:
    @debug
    def __init__(self, max_num):
        self.max_num = max_num

    @timer
    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])


# main

tw = TimeWaster(1000)

tw.waste_time(999)
