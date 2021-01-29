[김소정] [오전 10:17] a=int(input())
b=int(input())
c=int(input())
d=a*b*c
D=list(str(d))
print(D)
count_0=0
count_1=0
count_2=0
count_3=0
count_4=0
count_5=0
count_6=0
count_7=0
count_8=0
count_9=0
num=0
for i in range(1):
    for j in range(len(D)):
        if D[num]=='0':
            count_0 +=1
            num+=1
        elif D[num]=='1':
            count_1 +=1
            num+=1
        elif D[num]=='2':
            count_2 +=1
            num+=1
        elif D[num]=='3':
            count_3 +=1
            num...