from chapter06.DataProcessing import sanitize


class Athlete:
	def __int__(self, a_name, a_dob=None, a_times=[]):
		self.name = a_name
		self.dob = a_dob
		self.times = a_times

	def top3(self):
		return sorted(set([sanitize(t) for t in self.times]))[0:3]


