# a=[1,2,8,7,6,3,4,5]
# i=0
# b=[]
# while i<len(a):
#     if i%2==0:
#         pass
#     else:
#         b.append(a[i])
#     i=i+1
# i=0
# while i <len(b):
#     j=i
#     var=0
#     while j<len(b):
#         if b[j]>b[i]:
#             var=b[i]
#             b[j]=b[i]
#             b[j]=var
#         i=i+1
# x=0
# while x<len(a):
#     if a[x]%2==0:
#         c=a.index (a[x])
#         b.insert(c,a[x])
# print(b)


s=[2,9,1,8,5,11,3,4,7]
i=0
b=[]
for i in range(len(s)):
    if s[i]%2==0:
        pass
    else:
        b.append(s[i])
i=0
for i in range(len(b)):
    j=i
    temp=0
    for j in range(len(b)):
        if b[j]>b[i]:
            temp=b[i]
            b[i]=b[j]
            b[j]=temp
i=0
for i in range(len(s)):
    if s[i]%2==0:
        a=s.index(s[i])
        b.insert(a,s[i])
print(b)    






    