from chapter06.AthleteExtendList import Athlete


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return Athlete(templ.pop(0), templ.pop(0), templ)
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return None