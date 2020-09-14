# 用假设成立法求2—100的质数

for i in range(2,101):
    flag=True
    for j in range(2,int(i**0.5)+1):
        if i%j == 0:
            flag=False
            break
    if flag:
        print(i,'是质数。')