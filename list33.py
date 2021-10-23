z=input("enter the name")
i=0
a=[]
while i <len(z):
    a.append(z[i])
    i=i+1
print(a)
j=0
c=[]
while j<len(a):
    if a[j]=="a" or a[j]=="e" or a[j]=="i" or a[j]=="o" or a[j]=="u":
        c.append(a[j])
    j=j+1
print(c)
