marks=[46,43,76,64]
print(marks)

print()

list=["rashi",7,None,True,5.3,-3,0]
print(list)

print()

fruits=["apple","banana","watermelon"]
print(fruits[0])
print(fruits[-1])
print(len(fruits))

print()

#q1
languages = ["Python", "Java", "C++", "JavaScript"]
print(languages)
print(languages[0])
print(languages[3])
print(len(languages))

print()

fruits = ["Apple", "Banana", "Mango"]
fruits[0]="orange"
print(fruits)


#list slicing
name="python"
print(name[0:3])

print ()

fruits = ["Apple", "Banana", "Mango", "Orange", "Kiwi"]
print(fruits[0:3])
print(fruits[2:5])
print(fruits[:2])
print(fruits[2:])
print(fruits[:])
print(fruits[-2])
print(fruits[-3:])
print(fruits[:-2])

print()
numbers=[32,54,65,23,12,45,78,76]
print(numbers[::2])
print(numbers[1::2])

print(numbers[::-1])

print()

colors=["Red",'Yellow','Blue',"White","Black"]
print(colors[:2])
print(colors[2:])
print(colors[:])
print(colors[::-1])
print(colors[::2])

print()

print(colors.append("Grey"))       #append modifies list ....this will return None because it doesnt give updated list
print(colors)

colors.append("Golden")
print(colors)

print()

#q2
languages=["python","java"]
languages.append("c++")
print(languages)

print()
languages.insert(2,"c")
print(languages)

print()

#q3
colors=["Red","Black"]
colors.insert(1,"blue")
print(colors)

list1=[1,2,3]
list2=[4,5,6]
list1.extend(list2)
print(list1)
print(list2)

print()

list1.append([7,8])   #append takes only 1 argument
print(list1)
list1.extend([7,8])   #extend also takes 1 argument
print(list1)

print()

#q4
first=["A","B"]
second=["C","D"]
first.extend(second)
print(first)

print()

fruits=["Apple","banana","guava","fig"]
print(fruits)
fruits.remove("fig")
print(fruits)

print()

num=[2,4,5,2]        #only first value gets removed
num.remove(2)
print(num)

#q5
animals = ["Dog", "Cat", "Rabbit"]
animals.remove("Cat")
print(animals)

print()

numbers = [10,20,30]
numbers.pop(1)
print(numbers)
x=numbers.pop(1)  #will give what is deleted also
print(x)
print(numbers)
      
print()

#q6
cities = ["Nagpur","Mumbai","Delhi"]
cities.pop()
print(cities)

print()

numbers = [10,20,30]
numbers.clear()
print(numbers)

#q7
letters=["R","A","S"]
letters.clear()
print(letters)

print()

numbers=[54,232,2,65,75,7,43]
numbers.sort()          #ascending order
print(numbers)
numbers.sort(reverse=True)  #DESCENDING ORDER
print(numbers)

print()

fruits=["Mango","Apple","Watermelon"]
fruits.sort()
print(fruits)
fruits.sort(reverse=False)
print(fruits)
fruits.sort(reverse=True)
print(fruits)

print()

#q8
marks = [85,62,97,75]
marks.sort()
print(marks)

print()

numbers = [10,20,30]
numbers.reverse()
print(numbers)

#q9
colors = ["Red","Green","Blue"]
colors.reverse()
print(colors)

print()

fruits = ["Apple","Banana","Mango"]
fruits.index("Apple")  #wont work because it deoesnt modify list
print(fruits)
print(fruits.index("Apple"))  
#returns value error find reurns -1 if not in list

print()

numbers = [1,2,2,3,2]
print(numbers.count(2))

print()

letters = ["A","B","A","C","A"]
print(letters.count("A"))

print()

a = [10, 20, 30]
b=a
print(a)
print(b)

print()

a[1]=100
print(b)
print(a)

print()

a = [190,270,350]
b=a.copy()
print(a)
print(b)

print()

a = [1,2,3]
b=a[:]
b[1]=99
print(a)
print(b)

print()

#q10
numbers = [5,10,15]
copy_numbers=numbers.copy()
print(numbers)
print(copy_numbers)

print()

copy_numbers[2]=45
print(copy_numbers)

print()

#q11
a = [5,10,15]
b=a
print(b)
b.append(3)
print(b)

print()

#q12
a = [10,20]
b=a[:]
b.append(43)
print(b)

print()

fruits = ["Apple", "Banana", "Mango"]
for fruit in fruits:
    print(fruit)

print()

#q13
colors = ["Red", "Green", "Blue"]
for color in colors:
    print(color)

print()

fruits = ["Apple", "Banana", "Mango"]
for i in range(len(fruits)):                  #to get index also
    print(i,fruits[i])             

print()

#q14
languages = ["Python", "Java", "C++"]
for i in range(len(languages)):
    print(i,languages[i])

print()

fruits = ["Apple", "Banana", "Mango"]
for index, fruit in enumerate(fruits):
    print(index,fruit)

print()

#q15
games = ["Chess", "Football", "Cricket"]
for index, game in enumerate(games):
    print(index,game)

print()

matrix=[
    [1,2],
    [3,4]
]
print(matrix)
print(matrix[0])
print(matrix[1])
print(matrix[0][1])
print(matrix[1][1])

print()

#q16
marks=[[3,2],[4,5]]
print(marks)
