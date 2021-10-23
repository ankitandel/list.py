question_list = ["1).How many continents are there?","2).What is the capital of India?","3).NG mei kaun se course padhaya jaata hai?"]
options_list = [["A.Four", "B.Nine", "C.Seven", "D.Eight"],["A.Chandigarh", "B.Bhopal", "C.Chennai", "D.Delhi"],["A.Software Engineering", "B.Counseling", "C.Tourism", "D.Agriculture"]]
solution_list = [3,4,1]
answer=[["3.seven ","4.Eight"],["3.chennai","4.delhi"],["1.software engineering","2.counseling"]]
i=0
s=0
count=0
while i<len(question_list):
    print(question_list[i])
    b=0
    z=i
    while b<=len(options_list):
        x=(options_list[i][b])
        print(b+1,x)
        b=b+1
    c=input("do you want lifeline")
    if c=="yes":
        print("accept")
        if count<1:
            print(answer[z])
            num=int(input("enter the answer"))
            if num==solution_list[i]:
                print("correct answer")
                s=s+100
                print("win",s)
            else:
                print("incorrect answer")
                print("win",s)
                break
            count=count+1
        else:
            print("you are alredy use lifeline")
            var=int(input("enter the answer"))
            if var==solution_list[i]:
                print("correct your answer")
                s=s+100
                print("win",s)
            else:
                print("wrong answer")
                print("win",s)
                break
    else:
        var2=int(input("enter the answer"))
        if var2==solution_list[i]:
            print("correct your amswer")
            s=s+100
            print("win",s)
        else:
            print("wrong answer")
            print("win",s)
    i=i+1     
          
print("win",s)