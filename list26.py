list=[1,3,5,7,6,9,23,45,67,89,30]
i=0
a=[]
while i<len(list):
    if list[i]%2==0:
        print(2)
        a.append(2)
    else:
        print(list[i])
        a.append(2)
    i=i+1
print(a)
    