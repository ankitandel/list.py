numbers=[50,49,30,60,76,80]
i=0
while i<=len(numbers):
    j=0
    while j<=len(numbers):
        if numbers[i]==numbers[j]:
            print(numbers[j])
            j=j+1
        i=i+1
    