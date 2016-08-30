import os

import pickle

from chapter04.nester import print_lol
os.chdir('C:\\Users\\Administrator\\Desktop\\HeadFirstPython\\chapter03')
man = []
other = []
try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    # 一定不能忘
    data.close()
except IOError:
    print('File not find')
try:
    with open('man_data.txt', 'wb') as man_file:
        pickle.dump(man, man_file)
    with open('other_data.txt', 'wb') as other_file:
        pickle.dump(other, other_file)
except IOError as err:
    print('File error:'+str(err))
except pickle.PickleError as perr:
    print('pickling error:' + str(perr))

new_man=[]
try:
    with open('man_data.txt', 'rb') as man_file:
        new_man = pickle.load(man_file)
except IOError as err:
    print('File error:' + str(err))
except pickle.PickleError as perr:
    print('Pickling error:' + str(perr))
print_lol(new_man)

