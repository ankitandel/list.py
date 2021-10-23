m = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]

]
v=15
b=0
while b<len(m):
    column=0
    sum=0
    s=len(m[b])
    while column<s:
        sum=sum+m[b][column]
        column=column+1
    print(sum,"column")
    a=sum+sum+sum
    b=b+1
print(a)
j=0
while j<len(m):
    row=0
    sum1=0
    while row<len(m[j]):
        sum1=sum1+m[row][row]
        row=row+1
    print(sum1,"row")
    h=sum1+sum1+sum1
    j=j+1  
print(h)
x=m[0][0]+m[1][1]+m[2][2]
z=m[0][2]+m[1][1]+m[2][0]
if x==v:
    if z==v:
        c=x+z
        print("diagonal:",c)
        if sum==sum1==v:
            print("it is magic square")
        else:
            print("it is not magic square")
    else:
        print("it is not magic square")
else:
    print("it is not magic square")