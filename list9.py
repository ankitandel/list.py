marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]]

i=0
count=0
while i<len(marks):
    j=0
    sum=0
    a=0
    while j<len(marks[i]):
        a=a+(marks[i][j])
        j=j+1
    sum=sum+a
    avarage=sum//len(marks[i])
    i=i+1
    count=count+1
    print(count,"year avg=",avarage)

