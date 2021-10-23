#Ek code likho jo kissi bhi list ke liye uss list ke do sum ka output karta hai, ki uss list mei 
#odd numbers ka sum aur even numbers ka sum kitna hai.
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
sum=0
sum1=0
while i<=len(elements):
    if elements[i]%2==0:
        print(elements[i],"even number")
        sum=sum+elements[i]
    else:
        print(elements[i],"odd number")
        sum1=sum1+elements[i]
    i=i+1
print(sum,"even number")
print(sum1,"odd number")
