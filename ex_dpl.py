# -*- coding:utf-8 -*-

# 该程序使用python 2，因此，一般用以下4,5，6三行代码解决中文编码错误问题，一劳永逸
# 但貌似因为Python2选择了 ASCII，而python 3默认Unicode，所以，有声音不建议这种用法。

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import re
from collections import Counter
from zhon.hanzi import punctuation

initial_input=open("happiness_seg.txt", "r").read().decode("utf-8")    # 读取文件，将str转换为unicode
string = re.sub(ur"[%s]+" %punctuation, "", initial_input.decode("utf-8"))    # 调用zhon包去除中文标点
initial_list=string.split(" ")    # 将文章生成初始列表，空格划分各个元素
# print (string)
# print (initial_list)

standard_list=[]    # 初始化最终的列表

for i in range(0, len(initial_list)-1):
	if(len(initial_list[i])>=2 and len(initial_list[i+1])>=2):    # 判断相邻两元素长度均不小于2
		doublewords=initial_list[i]+initial_list[i+1]
		standard_list.append(doublewords)

counter=Counter(standard_list).most_common(10)    # Counter的内置函数挑选出频次最高的10个
for element in counter:    # 打印
	for word_count in element:
		print (word_count)
