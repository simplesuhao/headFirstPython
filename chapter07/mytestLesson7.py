import os

from chapter07.athletemodel import put_to_store


os.chdir('E:\python\headFirstPython\data')


the_file=['sarah2.txt', 'james2.txt', 'julie2.txt', 'mikey2.txt']
data = put_to_store(the_file)
print(data)