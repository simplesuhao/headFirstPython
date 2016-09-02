from chapter06.AthleteClass import Athlete


def sanitize(time_string):
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return time_string
	(mins, secs) = time_string.split(splitter)
	return mins + '.' + secs


def get_coach_data(filename):
	try:
		with open(filename) as f:
			data = f.readline()
		templ = data.strip().split(',')
		return Athlete(templ.pop(0), templ.pop(0), templ)
	except IOError as ioerr:
		print('File error:' + str(ioerr))
		return None
