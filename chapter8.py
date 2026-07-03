#indexing

#q1
city="Nagpur"
print(city[0])
print(city[2])
print(city[5])

print()

#negative indexing

word="python"
print(word[-1])

print()

#q2
city="Nagpur"
print(city[-1])
print(city[-2])
print(city[-3])

print()

#q3
text="hello"
print(text[-1])
print(text[-5])

print()

#slicing
 
word="python"
print(word[0:3])
print(word[2:5])

print()

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
print(name[::-1])  #reverse string

print()

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

print()

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

print()

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

print()

#q10
text="Missisippi"
print(text.count("s"))
print(text.count("i"))

print()

#string immutability

name="Carry"
name="Harry"
print(name)

print()

#q11
city="NGP"
new_city="Nagpur"
print(city)
print(new_city)

print()

word="bananaS"
print(word.replace("S","s"))
print(word)

print()

print(word.replace("a","o"))

print()

word=word.replace("b","B")
print(word)

print()

word=word.upper()
print(word)

print()

print(word.upper())

print()

#Escape character
print("he said \"hello\"")  #\tells next char has special meaning

print()

print("hello\nworld")

print()

print("name\tage")
print("harry\t5")

print()

print("\\")  #to print backlash

print()

#q12
print("my name is \"Rashi\"\n\nI love Python")

print()
print("Hello\nPython\tWorld")

print()
text = "Python"
print(text.upper().replace("P","J").lower())

print()
#built-in functions

name="Rashi"
a=len(name)
print(name)
print(a)

print()

#q13
city="Nagpur"
print(len(city))

print()

print(min("apple"))
print(max("Harry"))

print()

print(sorted("Harry"))
print(sorted("rashi"))
print(sorted("Rudra"))

print()

text="Python"
print("P"in text)
print("Z"in text)

print()

sentence="I love python"
print("love"not in sentence)

print()

#q14
text="Programming"
print("gram" in text)
print("Gram"in text)

print()
