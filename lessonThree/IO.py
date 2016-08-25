# coding=utf-8
import os

# 切换当前工作目录
os.chdir("C:\\Users\\Administrator\\Desktop\\HeadFirstPython\\chapter03")

# 打开数据文件，读取数据并显示
data = open('sketch.txt')
print(data.readline(), end='')
print(data.readline(), end='')
