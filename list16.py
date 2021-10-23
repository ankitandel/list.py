paisa= [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
i=0
count=0
count2=0
count3=0
while i<len(paisa):
    b=paisa[i]
    if b>=10000000:
        count=count+1
    elif b>=100000:
        count2=count2+1
    elif b<=100000:
        count3=count3+1
    i=i+1
print("crorepati",count)
print("lakhpati",count2)
print("dilwale",count3)


