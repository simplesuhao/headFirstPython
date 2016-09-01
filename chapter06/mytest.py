from chapter06.DataProcessing import get_coach_data, sanitize
import os
os.chdir('E:\python\headFirstPython\data')
sarah = get_coach_data('sarah2.txt')
# (sarah_name, sarah_dob) = sarah.pop(0), sarah.pop(0)
# print(sarah_name + "'sfastest time are: " + str(sorted(set([sanitize(t) for t in sarah]))[0:3]))
print(sarah['name'] + "'s fastest times are:" + sarah['Times'])
