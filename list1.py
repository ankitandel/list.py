#ode likho jo di gayi list mein jo number 20 se bade hai aur 40 se chote hai unhe count kare.
# Aur firr unka count print kare.

numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
lenth=len(numbers)
index=0
counter=0
while index<len(numbers):
    b=(numbers[index])
    if b>20 and b<40:
        counter=counter+1
        print(b)
    index=index+1
print(counter)

#Code likho jo iss list mein se maximum dhund kar ke print kare.




