import os

from chapter05.DataProcessing import sanitize, dp, get_coach_data

os.chdir('E:\python\headFirstPython\data')
james = get_coach_data('james.txt')
julie = get_coach_data('julie.txt')
mikey = get_coach_data('mikey.txt')
sarah = get_coach_data('sarah.txt')
'''
with open('james.txt') as jaf:
    data = jaf.readline()
james = data.strip().split(',')

with open('julie.txt') as juf:
    data = juf.readline()
julie = data.strip().split(',')

with open('mikey.txt') as mif:
    data = mif.readline()
mikey = data.strip().split(',')

with open('sarah.txt') as saf:
    data = saf.readline()
sarah = data.strip().split(',')


clean_james=[]
clean_julie=[]
clean_mikey=[]
clean_sarah=[]
for each_t in james:
    clean_james.append(sanitize(each_t))
for each_t in julie:
    clean_julie.append(sanitize(each_t))
for each_t in mikey:
    clean_mikey.append(sanitize(each_t))
for each_t in sarah:
    clean_sarah.append(sanitize(each_t))

dp是一个函数 用于去除重复类，并返回前三个值
clean_james = dp([sanitize(each_t) for each_t in james])
clean_julie = dp([sanitize(each_t) for each_t in julie])
clean_mikey = dp([sanitize(each_t) for each_t in mikey])
clean_sarah = dp([sanitize(each_t) for each_t in sarah])
'''
# 更简单的解决办法：

clean_james = [sanitize(each_t) for each_t in james]
clean_julie = [sanitize(each_t) for each_t in julie]
clean_mikey = [sanitize(each_t) for each_t in mikey]
clean_sarah = [sanitize(each_t) for each_t in sarah]


print(sorted(set(clean_james))[0:3])
print(sorted(set(clean_julie))[0:3])
print(sorted(set(clean_mikey))[0:3])
print(sorted(set(clean_sarah))[0:3])




