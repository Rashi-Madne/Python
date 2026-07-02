#q1
age=int(input("age: "))
if(age>=18):
    print("Eligible ")
else:
    print("Minor")

#q2
marks=int(input("marks: "))
if (marks>=90):
    print("A+")
elif(marks>=75 and marks<=89):
    print("B")
if(marks>=60 and marks<=74):
    print("C")
if(marks>=40 and marks<=59):
    print("D")
else:
    print("Fail")

#q3
password=input("password: ")
if password=="python123":
    print("login successful")
else:
    print("wrong password")

#q4
num=int(input("enter a num : "))
if num>0:
    print("positive")
elif num<0:
    print("negative")
else:
    print("zero")

#q5
num=int(input("enter a num : "))
if num%2==0:
    print("even")
else:
    print("odd")