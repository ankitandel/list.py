#Ek code likho jo kisi bhi list ke liye yeh output karta hai, ki uss list mei kitne odd numbers hai aur 
#kitne even numbers hai.
e= [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=1
count=0
count1=0
while i<=len(e):
    if e[i]%2==0:
        print(e[i],"even number")
        count=count+1
    else:
        print(e[i],"odd number")
        count1=count1+1
    i=i+1
print(count,"even number")
print(count1,"odd number")
