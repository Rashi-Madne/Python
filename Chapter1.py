# Exercise 1
name="Rashi"
age=20
city='Nagpur'
print(f"my name is {name}")
print(f"My age is {age}")
print(f"I live in {city}")

print()

#Exercise 2
a=10
b=5
print(f"addition of {a} and {b} is {a+b}")
print(f"subtraction of {a} and {b} is {a-b}")
print(f"multiplication of {a} and {b} is {a*b}")
print(f"division of {a} and {b} is {a/b}")

print()

#exercise 3
a=input("Your name: ")
b=int(input("your age :"))
print(f"hello {a}, you are {b} years old")

print()

#print and return
def square(number):
    return (number*number)
answer=square(5)
print(answer)

print()

def add(a,b):
    return a+b

addition=add(4,2)
print(addition)

print()

def sub(a,b):
    return a-b

print(sub(4,2))

print()

#exercise 4

def cube(num):
    print(num*num*num)
cube(2)

print()

def cube(num):
    return(num*num*num)

result=cube(2)
print(result)

print(cube(3))

print()

#exercise5

def full_name(first,last):
    return f"{first}{last}"

print(full_name("Rashi", "Madne"))

print()

def name(first,middle,last):
    return first+" "+middle+" "+last

print(name("Rashi", "Sarika", "Madne"))

print()

def multiply(a, b):
    return a * b

x = multiply(5, 6)

print(x + 10)

#default values
def greet(name=" Guest"):
    print(f"Hello{name}")

greet(" Rashi")
greet(name=" Harry")
greet()

print()

def power(base,exponent=2):
    return base**exponent
print(power(5))
print(5,3)

print()
#exercise6

def country(name="India"):
    print(f"I live in {name}")

(country)
country("Japan")

print()

#named arguments

def student(name,age):
    print(name)
    print(age)

student("Harry",5)
student(name="Rudra",age=6)

#exercise 7
def book(title,author):
    print(f"title: {title}")
    print(f"author: {author}")

book("ABC","abc")
book(title="XYZ",author="xyz")