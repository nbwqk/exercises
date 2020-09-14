# 打印乘法表
# 外循环表示行数，内循环表示列数
i=0
while i<9:
    i += 1
    j=0
    while j < i:
        j += 1
        print(j,'*',i,'=',j*i,sep='',end='\t')  # \t 是制表符
    print()