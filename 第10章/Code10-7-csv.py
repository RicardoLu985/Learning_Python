# with open('data.csv',mode='r', encoding='utf-8') as f:
#     context = f.read()
#     print(context)

import csv

# with open('data.csv', mode='r', encoding='utf-8') as file:
#     context = csv.reader(file)
#     header = next(context)  # 获取并消除表头
#     scores = []
#     for i in context:
#         scores.append(int(i[2]))
#     print(sum(scores)/len(scores))

with open('data.csv', 'a', newline='', encoding='utf-8') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    # spamwriter.writerow(['阿山','js','60'])
    # spamwriter.writerow(['tom', 'java', '45'])
    # spamwriter.writerow(['mia', 'python', '100'])
    lista = [['阿山','js','60'],['tom','java','45'],['mia','python','100']]
    spamwriter.writerows(lista)