# 使用计数法求质数

for i in range(2,101):
    count=0
    for j in range(2,i):
        if i % j == 0:
            count += 1
    if count == 0:
        print(i,'是一个质数。')
    else:
        print(i,'是一个合数','它能被',count,'个数字整除。')