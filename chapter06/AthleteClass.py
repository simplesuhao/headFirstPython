from chapter06.DataProcessing import *


class Athlete:
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

    def top3(self):
        return sorted(set([sanitize(t) for t in self.times]))[0:3]

    def add_time(self, time_value):
        return self.times.append(time_value)

    def add_times(self, list_of_times):
        return self.times.extend(list_of_times)
