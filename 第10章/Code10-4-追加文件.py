# 打开文件
from fileinput import close

file1 = open('test.txt','a',encoding='utf-8')
# 追加文件
file1.write('\n为什么没有诺奖！')
# 关闭文件
file1.close()