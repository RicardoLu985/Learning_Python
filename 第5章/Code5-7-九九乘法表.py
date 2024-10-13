
# 方法一：
m = 9
for i in range(m+1):
    if i > 0:
        for j in range(i+1):
            if j > 0:
                print(i,'x',j,'=',i*j,sep='', end='  ')
        print()

# 方法二：
for i in range(9):
    for j in range(i+1):
        print('%dx%d=%d' % (j+1,i+1,(i+1)*(j+1)),end='  ')
    print()
