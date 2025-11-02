# 打开文件
from fileinput import close

file1 = open('test.txt','w',encoding='utf-8')
# 写入文件
file1.write('余华，你是最棒的！')
# 关闭文件
file1.close()