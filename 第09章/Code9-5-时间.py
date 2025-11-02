import time
from time import localtime

t = time.time()  # 时间戳：1970年开始
print(t)

t = time.localtime()  # 结构化的时间
print(t)
print(t.tm_year, type(t.tm_year))
print(time.strftime('%Y-%m-%d %H:%M:%S', t))

from my_package import my_tools
print(my_tools.get_time())