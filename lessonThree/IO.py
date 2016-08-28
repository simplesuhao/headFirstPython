# coding=utf-8
import os

# 切换当前工作目录
os.chdir("C:\\Users\\Administrator\\Desktop\\HeadFirstPython\\chapter03")
try:
# 打开数据文件，读取数据并显示
    data = open('sketch.txt')
# print(data.readline(), end='')
# seek()用于将文件返回至起始位置
# data.seek(0)
    for each_line in data:
        # if not each_line.find(':') == -1:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')
        except ValueError:
            pass

    data.close()
except IOError:
    print('The data file is missing!')

