import re

text ="my name is junay"
x = re.search("^my,^junya$",text)
print(x)


text ="My name is junya"
x = re.search("my.*junya$",text)
print(x)

# for small letters
x = re.findall("[a-m]" ,text)
print(x)

# # for capital letters

x  = re.findall("[A-M]",text)
print(x)

# for numbers

test = "my age is 20"
x = re.findall("\d",test)
print(x)

name = "junya"
x = re.findall("^j",name)
print(x)

name = "junuya"
x = re.findall("a$",name)
print(x)

sent = "I am from japan"
x = re.findall("am{1}",sent)
print(x)

names = "David roger junya karthik"
x = re.findall("junya|karthik",names)
print(x)

sentence = "i am singer sings well"
x = re.findall("\Ai",sentence)
print(x)

y = "The rain is good i am 30"
x = re.findall("\w",y)
print(x)

xy = "i love lakers"
x = re.findall("lakers\Z",xy)
print(x)

# # only letters

yy = "i am junya and i love basball i am 40"
x = re.findall("\D",yy)
print(x)


txt = "i live in japan for 10 years and i want to live in uk for 8 years"
x = re.findall("[0-9]",txt)
print(x)

time = "This is india and time is 18:10 pm"
x = re.findall("[0-5][0-9]",time)
print(x)