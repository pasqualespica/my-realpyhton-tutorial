# from decorators import timer
from _11_timing_functions import timer

@timer
class TimeWaster:
    def __init__(self, max_num):
        self.max_num = max_num

    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])


# Decorating a class does not decorate its methods. 
# Recall that @timer is just shorthand for TimeWaster = timer(TimeWaster).

# Here, @timer only measures the time it takes to instantiate the class:


tw = TimeWaster(1000)


tw.waste_time(999)
