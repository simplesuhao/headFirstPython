import os

from chapter06.AthleteExtendList import Athlete
from chapter06.GetData import get_coach_data

os.chdir('E:\python\headFirstPython\data')
sarah = get_coach_data('sarah2.txt')
james = get_coach_data('james2.txt')
mikey = get_coach_data('mikey2.txt')
julie = get_coach_data('julie2.txt')
# (sarah_name, sarah_dob) = sarah.pop(0), sarah.pop(0)
# print(sarah_name + "'sfastest time are: " + str(sorted(set([sanitize(t) for t in sarah]))[0:3]))
print(sarah.name + "'s fastest times are:" + str(sarah.top3()))
print(james.name + "'s fastest times are:" + str(james.top3()))
print(mikey.name + "'s fastest times are:" + str(mikey.top3()))
print(julie.name + "'s fastest times are:" + str(julie.top3()))

vera = Athlete('vera vi')
vera.append('1.31')
print(vera.top3())
vera.extend(['2.22', '1-21', '2:22'])
print(vera.name)
print(vera.top3())