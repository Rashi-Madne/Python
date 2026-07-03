#indexing

#q1
city="Nagpur"
print(city[0])
print(city[2])
print(city[5])

#negative indexing

word="python"
print(word[-1])

#q2
city="Nagpur"
print(city[-1])
print(city[-2])
print(city[-3])

#q3
text="hello"
print(text[-1])
print(text[-5])

#slicing

word="python"
print(word[0:3])
print(word[2:5])

#q4
fruit="Watermelon"
print(fruit[0:5])
print(fruit[5:])
print(fruit[5:10])

print( )

word = "Programming"
print(word[3:8])

print()

name="Rashi"
print(name[:])

print()

name="Rashi"
print(name[::-1])

#q5
city="Nagpur"
print(city[:3])
print(city[:])
print(city[3:])

print()

#methods

name="rashi"
print(name.upper()) #upper doesnt change original string
name="HARRY"
print(name.lower())

#q6
movie = "INTERSTELLAR"
print(movie.lower())

print()

book="atomic habits"
print(book.title())

print()

#q7
country="south korea"
print(country.title())

print()

name="Rashi Madne                   "
print(name.strip())

print()

#q8
text="           python           "
print(text.strip())

print()

sentence="I like java"
print(sentence.replace("java","python"))

#q9
sen="I like cats"
print(sen.replace("cats","dogs"))

print()

word="programming"
print(word.find("g"))
print(word.find("z"))
print(word.rfind("g"))
#-1 if char is not found

print()

#count
word="banana"
print(word.count("a"))
print(word.count("n"))

#q10
text="Missisippi"
print(text.count("s"))
print(text.count("i"))