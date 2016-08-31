def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return mins + '.' + secs


def dp(data_list):
    unique = []
    if isinstance(data_list, list):
        for each_data in data_list:
            if each_data not in unique:
                unique.append(each_data)
        return unique[0:3]


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        return data.strip().split(',')
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return (None)