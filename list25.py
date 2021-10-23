list=[1,2,3,4,5,6,10,9,12,15,27,30]
i=0
a=[]
while i<len(list):
    if list[i]%3==0:
        print(3)
        a.append(3)
    else:
        print(list[i])
        a.append(3)
    i=i+1
print(a)