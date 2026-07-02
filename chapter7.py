def welcome():
    print("*"*20)
    print("welcome to my app")
    print("*"*20)
welcome()
welcome()
welcome()

print(" ")

#q1
def greet():
    print("hello Rashi")
    print("Have a great day")
for i in range(5):
    greet()

print(" ")

#q2
def welcome():
    print("hello welcome")

def greet():
    print("Hello")

def print_line():
    print("-------------------")

welcome()
greet()
print_line()

#parameters

def greet(name):
    print(f"hello {name}")
greet("Harry")

print(" ")

def country (name):
    print(f"i live in {name}")
country("India")
country("Japan")
country("South Korea")

print()

def square(num):
    print(f"the square is {num*num}")
square(5)
square(8)
square(10)

print()

#multiple parameters
def student(name,age):
    print(f"Name : {name}")
    print(f"Age: {age}")
student("Harry",5)

print()

def movie(name,year):
    print(f"Movie:{name}")
    print(f"Released: {year}")
movie("Interstellar", 2014)
movie("3 Idiots", 2009)
movie("Your Name", 2016)