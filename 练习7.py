# 一张纸的厚度大约是0.08mm，对折多少次后能达到珠穆朗玛峰的高度（8848.13m）

height=0.08/1000
count=0
while True:
    height=height*2
    count+=1
    if height >= 8848.13:
        break
print('要对折',count,'次，才能达到珠穆朗玛峰的高度。')