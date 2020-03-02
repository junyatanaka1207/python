      #string.py -ok-
# course = "leanig pyhthon"
# print(course[5])

# name = "junya tanaka"
# print(name)
# print(name[2:3])
# print(name[1:5])
# print(name[:5])
# print(name[:])

# fav_team = "manchester united"
# print(fav_team[2])
# print(fav_team[0:10])
# print(fav_team[:2])

# first = "junya"
# second = "tanaka"
# name = "jr"
# full = first + second +name
# print(full)

# first = "junya"
# second = "tanaka"
# name ="jr"
# full = f'{first} {second} {name}'
# print(full)


    #method. py              -method完了ー
# name = "junior"
# print(name)
# print(name.upper())

# name = "JUNIA"
# print(name)
# print(name.lower())

# name = "   juniya"
# print(name)
# print(name.strip())

# name = "   juniya"
# print(name)
# print(name.replace("j","k"))

# name = "  juniya"
# print(name)
# print(name.find("a"))

# name = "juniyatanaka"
# print(name)
# print(name.capitalize())

                    #hellow py
# junior = 1001
# print(junior)

# name = "junior"
# print(name)

# int = 2
# print(type(int))

# number = 5.5
# print(type(number))

# name = "junior"
# print(type(name))

# boolen = True
# print(type(boolen))

# bloon = False
# print(type(bloon))

# star ="juniya tanaka"
# print(star)

# name = "junya"
# age = 21
# country = "japan"
# is_student = True
# print(name, age, is_student)

        #hnumber.py     
        #ーnumberは完了ー
# print(3+3)
# print(3-3)
# print(10/3)
# print(10//3)
# print(10%3)
# print(10**3)

# print(round(2.5))
# print(abs(-3.33))

#print() とは（）内にあるものを表示しろ！という意味なので
#line84のprint(name,age,is_student)とは、変数name age is_studentの中身を表示しろ　という意味になります
#いいですか　あくまでnameやらageやらis_studentは変数なのです　数学でいうxやyなのです

                                            #2日目

# age = 16 
# if age == 22:
#   print('eligile')
# elif age <=18:
#   print('not child')
# else:
#   print('child')

    #while.py
# guess = 0 
# answer = 25

# while answer != guess:
#   guess = int(input("Guess"))

    # logical.py
# high_income = False
# good_credit = True

# if high_income or good_credit:
#   print('OK')

        #ligical_and.py
# high_income = True
# good_credit = True
# if high_income and good_credit ==True:
#   print('ok')
# age = 10
# if age >= 18 and 65>=age:
#   print('accepted')
# else:
#   print('not accepted')
 
       #list.py
# name = list("junya")
# print(name)

# numbers = list(range(5))
# print(numbers)

# letters = ["a","b","c","d"]
# print(letters[2])

# letters = ["a","b","c","d"]
# print(letters[-4])

# letters = ["j","u","n","y","a"]
# print(letters[2])
# letters[0] = 'a'
# print(letters)
# print(letters[::2])
# print(letters[::3])

# letters = ["a","b","c"]
# for x in letters:
#   print(x)

# letters = ["junya","tanaka","sir"]
# for x in letters:
#   print(x)

          #for.py
# for x in range(5):
#   print(x)

# for a in "python":
#   print(a)

# for abc in ['a','b','c']:
#   print(abc)

# for a in range(2, 5):
#   print(a)

# for name in ["j","u","n","y","a", "t","a","n","a","k","a"]:
#   print(name)

# for name in ["junya tanaka"]:
#   print(name)

# for x in range(0,10,2):
#   print(x)

# name = ["junya","tanaka","atoms"]
# for n in name:
#   print(n)

# club = ["manu","real madrid","yankers"] 
# for y in club:
#   print(y)


                                    #三日目

#list.enumirate

# letters = ["a","b","c","d"]
# for letter in enumerate(letters):
#     print(letters)

           #fifo
# from collections import deque
# quee = deque({})
# quee.append(1)
# quee.append(2)
# quee.append(3)
# print(quee)
# quee.popleft()
# print(quee)
# quee.popleft()
# print(quee)
# quee.append(4)
# print(quee)

#lifo.py
# browsing_Session = []
# browsing_Session.append(1)
# browsing_Session.append(2)
# browsing_Session.append(3)
# print(browsing_Session)
# last = browsing_Session.pop()
# print(last)
# print(browsing_Session)

       #sot.py
# numbers = [3.34,98,67,51]
# numbers.sort()
# print(numbers)

# numbers = [3,34,98,67,51]
# numbers.sort(reverse=True)
# print(numbers)

#map.py

# items = [("product 1", 10),("product 2", 5),("product3,"7)]
# prices = []
# for item in items:
#     prices.append(item[1])
#  print(prices)
 
# items = [("product 1", 10),("prpduct 2", 5),("product 3",7)]
# prices = list(map(lambda item: item[1],items))
# print(prices)   

# items = [("product 1", 10),("product 2 ",5),("product 3", 7)]
# x  = list(filter(lambda item: item[1] > 6,items))
# print(x)

# list1 = [1,2,3]
# list2 = [10,20,30]
# print(list(zip("abc",list1,list2)))

# list1 = [2,3,4,5]
# list2 = [20,100]
# print(list(zip(list1,list2)))

# names1 = ["junya","yamada","tanaka"]
# names2 = ["sakamoto","kataoka","nakajima"]
# print(list(zip(names1,names2)))

#  tapple.py
# name = ("junya","soma","huma","yuto","kaito","jinn")
# for x in name:
#     print(x)

# name = ("junya","kaito","jinn","yuuto","taro","eiji")
# if "junya" in name:
#     print("ok")

# name = ("junya","soma","huma","jin","koya", "ryuu")
# print(len(name))
#  tempCodeR-
# number = (1,2) + (3,4) + (7,61)
# print(number)

# number = (1,3)*3
# print(number)

# tup = ("web","got","fag","fag")
# print(tup[1])

# tup = ("yho","faf","vavsdf","vsg","fsbs","sgb")
# print(tup[3:])

# tup1 = ("japan","canada","uk")
# print(tup1[-1:])

# x = ("junya","tanak","india")
# y = list(x)
# print(y)
# y[1] = "takumi"
# x = tuple(y)
# print(x)

# cont = ("japan","india","canada","america","uk","us")
# if "uk" in cont:
#     print("ok")

# names = ("yuki", "rio","junya")
# print(len(names))

#sets.1py

# name = {"taka","toshi","yuki","kai","ida","tanni"}
# print(name)
# name.add("hukunaga")
# print(name)

# name = {"taka","toshi","yuki","kai","ida","tani"}
# for y in name:
#     print(y)

# neme = {"taka","toshi","eisi","kai","ida","tani"}
# print(len(name))

# name = {"osaka","tokyo","nagoya"}
# x = name.pop()
# print(x)
# print(name)

# names = {"x","y","z"}
# names.clear()
# print(names)

# set1 = {"a,b,c"}
# set2 = {1,2,3}

# sets = set1.union(set2)
# print(sets)

# numbers = [1,2,3,4,5]
# con = set(numbers)
# print(con)

# first = {1,2,3,4,5}
# second = {6,4,7}
# print(first | second)
# print(first & second)
# print(first - second)
# print(first ^ second)

# name = {"junya","yuki","rio"}
# print(name)

# name = {"shizuoka","kanagawa","tokyo","osaka"}
# for junya in name:
#     print(junya)

# name = {"nakamura","watabe","ymada"}
# print("junya" in name)

# name = {"nakamura","watabe", "yamada"}
# print("nakamura" in name)

# name = {"nakamura", "watabe","yamada"}
# name.add("koki")
# print(name)

# name = {"osaka", "kyoto", "hiroshima","toyama"}
# name.update(["a","b","c"])
# print(name)

# name = ("osaka","nagsaki","hiroshima",)
# print(len(name))

# letters = ["a","b","c","d"]
# letters.append("e")
# print(letters)

# names = ["junya","tanaka","yamada","abe"]
# names.append("tino")
# names.append("nishiyama")
# print(names)
# names.insert(0,"tiger")
# print(names)
# names.insert(1,"kobe")
# print(names)
# names.insert(7,"koike")
# print(names)
# names.remove("koike")
# print(names)
# names.remove("tanaka")
# print(names)
# names.pop()
# print(names)
# del names[2]
# print(names)
# names.clear()
# print(names)

# items = [("priduct 1",10),("prodict 2",5),("prouct3",15)]
# items.sort(key=lambda items: items[1])
# print(items)

# items =[("product 1",100),("product 2", 80),("product 3",50)]
# items.sort(key=lambda items: items[1])
# print(items)

# names = {"junya":"123456789","yuki":"9856371"}
# print(names)

# cars = {"brand":"honda","model":"lexas","year":2000}
# print(cars)
# print(cars["model"])
# print(cars["brand"])

# cars = {"brand":"honda","model":"lexas","year":"2000"}
# print(cars)
# cars["year"] = 2020
# print(cars)
# for x in cars:
#     print(x)
# for x in cars:
#     print(cars[x])

# for x in cars.values():
#     print(x)

# cars = {"balsnd":"vents","model":"hi","yesr":"2000"}
# print(cars)
# for x in cars.values():
#     print(x)

# cars = {"land":"honda","model":"jiyu","year":"134"}
# for x,y in cars.items():
#     print(x,y)

# if "years" in cars:
#     print("yes")
# print(len(cars))

# cars["cplor"] ="red"
# print(cars)



#----------5日目---------------------

#dict.py

# names = {"firstname":"junya","lasname":"tanaka"}
# print(names)
# names["country"] = "japan"
# print(names)
# for x,y in names.items():
#     print(x,y)

#tempCodeRunnerFile.py

# numbers = [1,2,3,4,5,]
# con = set(numbers)
# print(con)

# first = {1,2,3,4,5}
# second = {6,4,7}
# print(first | second)
# print(first & second)
# print(first - second)
# print(first ^ second)

#calss.py

# class MyName:
#     pass

# print(MyName)

# class YourName:
#     a = 10

# print(YourName.a)

# class Hisname:
#     a = 10
#     name = "junya"

# print(Hisname.name)
# print(Hisname.a)

#classinit.py

# class Person:
#     def __init__(self,name,age,country):
#         self.name = name
#         self.age = age
#         self.country = country
    
# p1 = Person("junya","20","japan")
# p2 = Person("karthic","24","india")
# print(p1.name)
# print(p1.age)
# print(p1.country)
# print(p2.name)
# print(p2.age)
# print(p2.country)

# class Person:
#     def __init__(self,name,age,number,adress):
#         self.name = name
#         self.age = age
#         self.number = number
#         self.adress = adress

# p1 = Person("junya","10","14125","fwg@dfg")

# print(p1.name)
# print(p1.age)
# print(p1.number)
# print(p1.adress)

#classobject.py

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def myfunc(self):
#         print("Hellow my name is:" + self.name)

# p1 = Person("junya",20)
# p1.myfunc()

# class Person:
#     def __init__(self,age):
#         self.age = age

#     def myfunc(self):
#         print("Hellow my age is:" + self.age)


# p1 = Person("20")
# p1.myfunc()


# class Person:
#     def __init__(self,fname,lname):
#         self.firstname = fname
#         self.lastname = lname

#     def fullname(self):
#         print(self.lastname,self.firstname)

# x = Person("junya","tanaka")
# x.fullname()

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def myfunc(self):
#         print("Hellow my name is:" +self.name)


# p1 = Person("junya",10)
# print(p1.name)
# p1.name = "tanaka"
# print(p1.name)
# print(p1.age)

#reg.py


# import re

# text = "my name is junya"
# x = re.search("^my,^junya$",text)
# print(x)

# text = "My name is junya"
# x = re.search("my.*junya$",text)
# print(x)

# x = re.findall("[a-m]",text)
# print(x)

# x = re.findall("[A-M]",text)
# print(x)

# test = "my age is 20"
# x = re.findall("\d",test)
# print(x)

# name = "junya"
# x = re.findall("^j",name)
# print(x)

# name = "junya"
# x = re.findall("a$",name)
# print(x)

# sent = "I am from japan"
# x = re.findall("am{1}",sent)
# print(x)

# names = "David ronger junya karthic"
# x = re.findall("junya | karthic",names)
# print(x)

# sentence = "i am singer sings well"
# x = re.findall("\Ai",sentence)
# print(x)

# y = "The rain is good i am 30"
# x = re.findall("\w",y)
# print(x)

# xy ="i love lakers"
# x = re.findall("lakers\",xy)
# print(x)

# yy = "i am junay and i love baseball i am 40 "
# x = re.findall("\D",yy)
# print(x)

# txt = "i love in japan for 10 years and want to live in uk for 8 years"
# x = re.findall("[0-9]",txt)
# print(x)

# time = "This is india and time is 18:10 pm"
# x = re.findall("[0-5][0-9]",time)
# print(x)

