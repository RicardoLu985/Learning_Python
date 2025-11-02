# re
"""
    正则表达式处理
    可以用于文本搜索、替换、分隔等
"""

# ids = input('请输入你的身份证号：')
# # 18位数
# # 前17位是数字+ x，或者纯18位数字
# if len(ids) == 18 :
#     if ids[:-1].isdigit() and ids[-1].isdigit() or ids[-1] == 'x':
#         print('输入正确！')
#     else:
#         print('输入错误！')
# else:
#     print('输入错误！')

import re
# \d：数字     \D：非数字
result = re.match(r'\d+','01546354687463')
print(result)
# \w：数字字母下划线
result = re.match(r'\w+','hgfgh4455')
print(result)
# \s：空白字符   \S：非空
result = re.match(r'\s+','   ')
print(result)
# ^、$分别限制开头结尾

# . 任意字符
result = re.match(r'^code\d-\d-.+$','code5-4-shagfj')
print(result)
# [] 区间，可选列表
result = re.match(r'^[abcd]+$','abbbbcd')
print(result)
# | 或者
result = re.match(r'^a|b$','a')
print(result)

# 验证身份证号
result = re.match(r'^\d{6}(20[01]\d|202[0-4]|(19\d\d))(0[1-9]|1[0-2])([012]\d|3[01])\d{3}(\d|X)$','452023200810068032')
print(result)


from my_package import my_tools
id_card = '452023199811328032'
result = my_tools.validate_id_card(id_card)
print(result)