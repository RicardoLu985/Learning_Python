# with open('data.csv',mode='r', encoding='utf-8') as f:
#     context = f.read()
#     print(context)

import csv

with open('data.csv', mode='r', encoding='utf-8') as file:
    context = csv.reader(file)
    header = next(context)  # 获取并消除表头
    scores = []
    for i in context:
        scores.append(int(i[2]))
    print(sum(scores)/len(scores))
