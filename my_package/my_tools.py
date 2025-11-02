import random
import re
import time

a = []
n = 5

def random_char(upper=True):
    if upper:
        t = random.randint(ord('A'), ord('Z'))
        return chr(t)
    else:
        t = random.randint(ord('a'), ord('z'))
        return chr(t)

def random_string(length):
    s = ''
    for i in range(length):
        s += random_char(random.choice([True, False]))  # 大小写的开关
    return s

def yan_zheng_ma(length):
    return random_string(length)

def main():
    for i in range(20):
        a.append(random_string(random.randint(1,20)))
    print(a)

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def validate_id_card(id_card):
    pattern = r'^[1-9]\d{5}(19\d\d|20[01]\d|202[0-4])(0[1-9]|1[0-2])([012]\d|3[01])\d{3}(\d|X)$'
    match = re.match(pattern, id_card)
    if not match:
        return "无效身份证号码"

    year = int(id_card[6:10])
    month = int(id_card[10:12])
    day = int(id_card[12:14])

    if month == 2:
        if is_leap_year(year):
            if day > 29:
                return "无效身份证号码"
        else:
            if day > 28:
                return "无效身份证号码"
    elif month in {4, 6, 9, 11} and day > 30:
        return "无效身份证号码"
    elif day > 31:
        return "无效身份证号码"

    return "有效身份证号码"

def get_time():
    t = time.localtime()
    s = time.strftime('%Y-%m-%d %H:%M:%S', t)
    return s
