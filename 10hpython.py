# print("hello world")

# #i am a manu haraj

# """
# so this is my program
# """

# #pratic set 1 
# print("""Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.
# Twinkle, twinkle, little star,
# How I wonder what you are!""")

# print("""5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50""")


#chapter 2

'''a= 45
b= 35
c=7
name="manu"
print(a+b+c, name)

# folatung numeber are dacmil ex.5.4 etc...
#integer are they number ex.1,2,3 etc...
#any names and anything is in "" code is called string
#true false are the buline data type
#none is the ome data type varible

a=1 #a is a integer
b=5.333 #b is dacmil
c= "manu" #this is string
d= "false" #buline data type,
e= "none" #none data varible

#oprator property
#artmatic oprator

a=8
b=6
c=a+b
print(c)

#assigent oprator
# all here this oprator is working like -,+,
a=4-2
print(a)
b=3
b+=2
print(b)

#comparison oprator
#always comparison value is buline
d=5<4
print(d)
a=5!=7
print(a)

a=5==5 #== is the comparison 
print(a)

#logical oprator

e = "hauman" or "goat"
e = 5 or 3

print(not(True))

a="32.1"
b=float(a)
t= type(b)
print(t)

#input fuction

a= int(input("enter your number"))
b= int(input("enter your second number"))

print("number a is", a)
print("number to is", b)
print("your ans", a+b)'''

'''#chapter 2 practic set
#1 question and solution
a=int(input("write your number"))
b=int(input("enter your second number"))
print(a + b)

#2 question and solution

a=37
b=5
print("your divide ans is this", a%b)

#3 question and ans

a= input("what is this number")
print(type(a))

#4 question and ans

a=48
b=35
print(a>b)

#5 question and ans

a=int(input("write the numer what you fine the avrage"))
b=int(input("write the numer what you fine the avrage"))
c=int(input("write the numer what you fine the avrage"))
d=int(input("write the numer what you fine the avrage"))'''
'''a= int(input("enter your first number 1:"))
b= int(input("enter your second number 2:"))
print("the avrage of two number", (a+b)/2)'''
#question 6 and answer
#a = int(input("enter your square number"))
#print("your square", a*a)

# what i lern practic

 #i am making the unkie calculator
'''a =  input("choose oprator(+, -, /, *,):")
b= int(input("add your number to do any think like"))
c= int(input("add your number to do any think like"))

print("your add answer", (b+c))
print("your multiply ans", (b*c))
print("your divide answer", (b/c))
print("your subtract answer", (b-c))'''

#my second practic
'''a= 34
print(type(a))
a="manu"
print(type(a))'''

#capter 3 satarted so i have to lern
'''for i in range(3):
  print("manu")'''

'''a = 12
b = 6
print("you ans", (a+b))'''

#chapter 3 __ STRINGS


'''#any move to write string
#we also write string in 3 way
name = 'manu' #this is string
name = "manu" #this double ling string
name = man #this is triple line string

#lenth in string
  
name="deepanjali"  

nameshort= name[0:5]#0 is nothing but that is the first letter 
print(nameshort)

chatcher1=name[1]
print(chatcher1)

#negatuve scliching

name="harry"
print(name[0:3])
print(name[-4:-1])#hard method 
print(name[1:4])#easy method

print(name[:4])#here : dot is back nothing means 0 and the :lenth of the word this do having nothing means -1.

#scliching with skip value

b = "abcdefghijklmnopq"
print(b[1 : 9]

name ="harty"
print(name[ 2 : 0])

#lenth in python

a= "deepanjali"
#print(len(a))
print(a.endswith("jali")) # this is ends with
print(a.startswith("deep"))#starts 
print(a.capitalize())#frist letter capitalize

b="abcdefghijklmnopq"
print(len(b))

s ="manu is a good boy"
print(s.replace("good","bad"))

#escape sequence chatcher
#here all escape sequence chatcher
#\n,\,
a = "manu is a good boy\
but not he is\n \"funny\""
print(a)'''

#CHAPTER 3 PRATIC SET ONLY ANSWER

# 1  QUECTION IS THIS 

'''name = input("👉 Please enter your name: ")
print("🌞 Good Afternoon,", name.capitalize() + "!")

#2 QUECTION>
letter= dear <|name|>,
           you are seleceted!
           <|date|>
           
print(letter.replace("<|name|>" , "manu").replace("<|date|>" , "12 july"))    

#QUECTION 3
 
a="hai  i  am  a  manu" 
print(a.find("  "))

#QUECTION 4

a="hai  i  am  a  manu" 
print(a.replace("  ", "  "))

#QUECTION 5

letter="dear manu,\n\t this is python course.\n thanks"
print(letter)

#what i lern all projects is in down'''

#projects
#यूजर को एक रैंडम नंबर गेस करने को बोलो, और बताओ सही है या नहीं।

'''import random

# Step 1: Random number generate karo (1 se 10 ke beech)
secret_number = random.randint(1, 10)
attempts = 0

print("Welcome to Number Guessing Game!")
print("Guess a number between 1 and 10")

# Step 2: Loop chalayenge jab tak guess correct na ho
while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret_number:
        print("🎉 Congratulations! You guessed it right.")
        print("You took", attempts, "attempts.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")'''

# 2 projects

#odd and even cheaker

# User se number input lo
'''num = int(input("Enter a number: "))

# Check karo even hai ya odd
if num % 2 == 0:
    print(num, "is an Even number.")
else:
    print(num, "is an Odd number.")'''



#       CHAPTER 4- lists and tuple 

# lists method all 
'''friends = ["apple", "orange",5 ,345.06, False, "akash", "rohan"] # this is list

print(friends[6])
friends[6]="grapes"
print(friends[6])
print(friends[0:4])

friends = ["apple", "orange",5 ,345.06, False, "akash", "rohan"]
print(friends)

friends.append("manu")#in end change value

print(friends)

l1 = [1, 34, 56, 48, 58, 89]
l1.sort()#accorfing order
print(l1)
l1.reverse()#deccionfing ordrr
print(l1)

l1.insert(3, 5000)
print(l1)#changing any ware value 

l1.pop(4)
print(l1)#remove anyware value

l1 = [34, 56, 89]
l1.remove(34)
print(l1)

#tupls in python
#tuples are the like lists but some differce

a = (1, 2, 5, 6)
print(type(a))#why this is tuples because this is here the bracket

a =()#this is mt tuple

a=(1,)
print(type(a))#this is integer
#when you want to a integer to tuple so put there ,

a = (1,45,342,3424,False,"rohan", "shivam") #you cant change  value in tuple 
print(type(a))

#tuple meathods
a = (1,45,342,3424,False,"rohan", "shivam")
print(a)

no=a.count(45)
print(no)

i=a.index(3424)
print(i)

print(len(a))'''

#CHAPTER 4 practic SET
# 1 QUECTION

'''fruit=[]
f1= input("enter fruit name:")
fruit.append(f1)
f2= input("enter fruit name:")
fruit.append(f2)
f3= input("enter fruit name:")
fruit.append(f3)
f4= input("enter fruit name:")
fruit.append(f4)
f5= input("enter fruit name:")
fruit.append(f5)
f6= input("enter fruit name:")
(fruit.append(f6)
f7= input("enter fruit name:")
fruit.append(f7)

print(fruit)'''

# second QUECTION 2

'''marks=[]
f1= int(input("enter marks :"))
marks.append(f1)
f2= int(input("enter marks :"))
marks.append(f2)
f3= int(input("enter marks :"))
marks.append(f3)
f4= int(input("enter marks :"))
marks.append(f4)
f5= int(input("enter marks :"))
marks.append(f5)
f6= int(input("enter marks :"))
marks.append(f6)
f7= int(input("enter marks :"))
marks.append(f7)

print(marks)'''

#QUECTION 3

'''l = [12,32,45,78]

print(sum(l))'''

#QUECTION 4

'''a = (7, 0, 8, 0, 0, 9)
m = a.count(0)
print(m)'''

#chapter 5 -dictionary and sets

#dictionary
'''marks= {
   "manu":100,
   "rohan":56,
   "priyakant":23
}

print(marks, type(marks))

#dictionary meathods'''

'''marks= {
   "manu":100,
   "rohan":56,
   "priyakant":23,
   0: "harry" #here string and number are allowed
}
#methods
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"manu": 90})
print(marks)

print(marks.get("manu"))
print(marks["manu"])#this is alomodt sames get and marks but when we try manu2 in get you have none and in marks error because in deccionary not allowed this []

#sets in python

#sets is a collection of objects

trom = {}# this is empty dictionary
ssb = {3, 4, 5}# this is mt dictionary

a = set() # dont use {} this this will be vreat empty dictionary

s = {1, 54, 5, 5}# sets cant repet any word
print(s)

#sets methods

s = {1, 54, 5, 5, "harry"}
print(s, type(s))

s.add(534)#this is methods
print(s)

#sets are unoderd
#sets are unindexed
#there is no way to change sets in values
#sets cannot take duplicates values

s = {1, 54, 5, 5, "harry"}
len(s)
print(s)
s.remove(54)
print(s)'''

'''s1 = {3, 5, 6}
s2 = {4, 7, 9, 5}
print(s1.union(s2))
print(s1.intersection(s2))'''

#chapter 5 practic set

#1st QUECTION

'''a = set()
b = input("enter your number")
a.add(int(b))
k = input("enter your number")
a.add(int(k))
c = input("enter your number")
a.add(int(c))
t = input("enter your number")
a.add(int(t))
u = input("enter your number")
a.add(int(u))
i = input("enter your number")
a.add(int(i))
p = input("enter your number")
a.add(int(p))
z = input("enter your number")
a.add(int(z))
print(a)'''

# 2 QUECTION
#this is the most important QUECTION

'''s = set()
a.add(20)
a.add(20.0)
s.add("20")

print(s)'''

# 3 QUECTION

'''s = {}
print(type(s))'''

#QUECTION 4

'''name = {
     "manu":"english",
     "sohan":"hindi",
     "raushan":"tamil",
     "shivam":"telgu"
}

print(name)'''#you can the input also 

# 5 QUECTION

'''d ={}
name = input("enter friend name")
lamg = input("enter laungagr name")
d.update({name: lamg})
name = input("enter friend name")
lamg = input("enter laungagr name")
d.update({name: lamg})
name = input("enter friend name")
lamg = input("enter laungagr name")
d.update({name: lamg})
name = input("enter friend name")
lamg = input("enter laungagr name")
d.update({name: lamg})

print(d)'''

#6 QUECTION and the fifth quection are smae and the quection is write 2 friends name to same what is print.

#7 quection are als9 same because the quection is when language is change is so what

# 8 quection - problem

'''s = {8, 7, 12 "harry", [1,2]}#cahnge now you cant chage this value'''

# CHAPTER 6 - conditional expression

#conditional

'''a = int(input("enter your age:"))

if (a>18):
 print("you are a young")
else:
 print("you are a child")'''
 
 #if means aur and else means wrong when you type a if like your age is 18 you are a young 
 
 #else means you cant do 
'''a = int(input("enter your age here:"))
if (a>18):
 print("you are a young")
 print("you can voted")
 
else:
 print("you are a child")

print("end of the program")
 '''
'''a = int(input("enter your age here:"))
if (a>=18):
 print("you are a young")
 print("you can voted")

elif(a<0):
 print("invalid age")
elif(a==0):
 print("invlif")
 
else:
 print("you are a child")'''

#if and elif and else are always connected

#quiz

'''a = int(input("Enter your age here:"))

if(a>=18):
 print("yes")

elif(a<0):
 print("invaid age")

elif(a==0):
 print("this is not a age invalid")
 
else:
 print("no")'''
 
#relational oprator
'''1	==	equal to	दोनों मान बराबर हैं तो True देगा
2	!=	not equal to	दोनों मान अलग-अलग हैं तो True देगा
3	>	greater than	बाईं ओर का मान दाईं ओर से बड़ा है तो True देगा
4	<	less than	बाईं ओर का मान दाईं ओर से छोटा है तो True देगा
5	>=	greater than or equal to	बाईं ओर का मान बड़ा या बराबर है तो True देगा
6	<=	less than or equal to	बाईं ओर का मान छोटा या बराबर है तो Tre देगा'''
#logical oprator
''' 1	and	and	सिर्फ तभी True देगा जब दोनों शर्तें True हों।
2	or	or	अगर कोई भी एक शर्त True हो जाए, तो True देगा।
3	not	not	दिए गए condition का उल्टा (Reverse) कर देता है — True को False और vice-versa
'''

#elif is always using unlimated

#multiple if setement


'''a = int(input("Enter your age here:"))
#if setement no 1
if(a%2==0):
 print("a is even")
#if setement no 2
if(a>=18):
 print("yes")

elif(a<0):
 print("invaid age")

elif(a==0):
 print("this is not a age invalid")
 
else:
 print("no")'''


# CHAPTER 6 practic sets

#1 QUECTION

'''num1 = int(input("व्यक्ति 1 का नंबर दर्ज करें: "))
num2 = int(input("व्यक्ति 2 का नंबर दर्ज करें: "))
num3 = int(input("व्यक्ति 3 का नंबर दर्ज करें: "))
num4 = int(input("व्यक्ति 4 का नंबर दर्ज करें: "))

# सबसे बड़ा नंबर ढूंढना using conditional expressions
if (num1 >= num2) and (num1 >= num3) and (num1 >= num4):
    print("सबसे बड़ा नंबर है:", num1)
elif (num2 >= num1) and (num2 >= num3) and (num2 >= num4):
    print("सबसे बड़ा नंबर है:", num2)
elif (num3 >= num1) and (num3 >= num2) and (num3 >= num4):
    print("सबसे बड़ा नंबर है:", num3)
else:
    print("सबसे बड़ा नंबर है:" )    '''

# 2 QUECTION

'''a1 = int(input("enter marrk 1:"))
a2 = int(input("enter marrk 2:"))
a3 = int(input("enter marrk 3:"))

#cheak for total percantage

total_percentage = (100*(a1 + a2 + a3))/300

if(total_percentage>=40 and a1>=33 and a2>=33 and a3>=33):
 print("you are pass", total_percentage, "%")
 
else:
 print("you are fail try next year", total_percentage, )
'''


# 3 QUECTION

#spam comments dectaced

'''p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

ma = input("enter your comment:")

if((p1 in ma) or (p2 in ma) or (p3 in ma) or (p4 in ma)):
 print("this is spam")

else:
 print("this comment is not spam")'''
 
# 4 QUECTION

'''a = input("enter your name:")
print(len(a))

if len(a)<10:
 print("your name is less than 10 words")

else:
   print("your name is more than greater 10 words")'''
 
# 5 QUECTION 

'''name = ["manu", "vivek", "rohan", "shyam" ]

a = input("enter your name:")

if (a in name):
 print("that name avalible")

else:
 print("name not avalible")'''


# 6 QUECTION

'''a = int(input("enter your marks"))

if(a<=100 and a>=90):
       grade = "ex"
elif(a<90 and a>=80):
       grade = "a"        
elif(a<80 and a>=70):
       grade = "b"        
elif(a<70 and a>=60):
       grade = "c"        
elif(a<60 and a>=50):
       grade = "d"        
elif(a<50):
        grade = "f"


print("your grade is:", grade) '''    
   
# 7 QUECTION

'''post = input("enter the post")

if("manu" in post.lower()):
  print ("this is talking about manu")
else: 
  print ("this post is not")'''
  
  
#CHAPTER 7 - loops in python

#this is repting for anything

#loops

#write one to 100
#this is for loop
'''for i in range(1, 100):
  print(i)'''

#types of loop 
#1.while
#2.for

#while loop

'''i = 1

while(i<6):
  print(i)
  i +=0'''
  
'''
output:
1
2
3
4 
5
'''

#QUIZ - write 1 to 50 using while loop

'''a = 1
while(a<51):
  print(a)
  a += 1'''

#2 QUIZ
  
'''s = 1  

while(s<6):
  print("manu")
  s += 1
 '''
#3 QUIZ


'''m = [4, "manu", "sohan", "rahul"]

i = 0
while(i<len(m)):
  print(m[i])
  i += 1'''

#QUIZ finsish

#for loop  

'''for i in range(4):
  print(i)'''

#step size

'''for i in range(0, 100, 4):
  print(i)'''
#using lists  
'''l = [1, 4, 6, 234, 6, 764]

for i in l:
  print(i)'''
  
#using tuple

'''t = (6, 231, 75, 34)

for i in t:
  print(i)'''
  
#using string

'''s = "manuweedsdeepanjali"

for i in s:
  print(i)'''


#vvi(very important) lucky -for loop with else

'''l = [1, 7, 8]

for item in l:
  print(item)
  
else:
  print("done")'''
  
#the breaker statment

'''for i in range(100):
  if(i == 34):
    break #exit the loop right now
  print(i)'''

#continue statment
'''for i in range(100):
  if(i == 34):
    continue #foe skip the intersection
  print(i)
  '''
#pass statment

'''for i in range(645):
  pass
  
  
i = 0  
while(i<45):
  print(i)
  i += 1'''
  
#CHAPTER 7 practic set

#1 QUECTION


'''n = int(input("enter a numer"))

for i in range(1, 11):
  print(f"{n} X {i} = {n * i}")'''
  
# 2 QUECTION

'''l = ["Manu", "Sohan", "Meena", "Raj", "Mona"]

for name in l:
  if name.startswith("M"):
    print(f"hello {name}")
    
#3 QUECTION

n = int(input("enter a numer"))

i = 1
while(i<11):
  print(f"{n} X {i} = {n * i}")
  i += 1
  '''
#4 QUECTION

'''n = int(input("Enter the number: "))

if n <= 1:
    print("Number is not prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Number is not prime")
            break
    else:
        print("Number is prime")'''

#5 QUECTION

'''n = int(input("enter the number:"))
i = 1
sum = 0
while(i<=n):
  sum  += i
  i+=1
print(sum)'''
  
# 6 QUECTION

#5! = 1 X 2 X 3 X 4 X 5 this is factorial


'''n = int(input("enter the number"))
product = 1
for i in range(1, n+1):
  product = product + i
  
print(f"the factorial 9f{n} is{product}")

'''

# 7 QUECTION

#star pattern
'''
for n = 3 
  *
 ***
******'''

'''n = int(input("enter the number"))

for i in range(1, 1+n):
  print(" "* (n-i), end="")
  print("*"* (2*i-1), end="")
  print("")'''
  
# 8 QUECTION

'''n = int(input("enter the number"))

for i in range(1, 1+n):

  print("*"* i, end="")
  print("")
'''
# 9 QUECTION

'''n = int(input("Enter the number: "))

for i in range(1, n + 1):
    if i == 1 or i == n:
        print("*" * n)
    else:
        print("*" + " " * (n - 2) + "*")'''
        
#10 QUECTION

'''n = int(input("enter your number"))

for i in range(1, 11):
  print(f"{n} X {11 - i} = {n*(11-i)}")'''
  
  
# 8 CHAPTER - functions & recursiuons

'''a = int(input("enter your number"))
b = int(input("enter your number"))
c = int(input("enter your number"))

avrage = (a + b + c)/3
print(avrage)'''#here are losts of lines are code

# use functions
#functions defnition
'''def maa():
  a = int(input("enter your number"))
  b = int(input("enter your number"))
  c = int(input("enter your number"))

  avrage = (a + b + c)/3
  print(avrage)
  
  
maa()
maa()'''

# i want to any avrage found so we call

'''def maa():
  a = int(input("enter your number"))
  b = int(input("enter your number"))
  c = int(input("enter your number"))

  avrage = (a + b + c)/3
  print(avrage)
  
  
maa()#functions call
print("thanks")
maa()'''

#QUIZ


'''def a():
   b = input("enter your name:")

a()
print("good day")'''

#types of functions
#there are two types of functions

#1.bulit functions(already present in python) 
#2.user define functions(define by the user)

'''def goodday(name, ending):
  print("good day" + name)
  print(ending)
  
goodday(input("enter your name"), "thanks you")'''

'''def goodday(name, ending):
  print("good day" + name)
  print(ending)
  return "done"

a = goodday("harry", "thanks you")
print(a)'''

#deaufut perameter

'''def goodday(name, ending="thank you"):
  print(f"good day", {name})
  print(ending)
  
goodday("harry", "tahnk")
print("rohan")'''

#recursiuons

#recursiuons is a functions thats called recursiuons

'''factorial(1) =  1
factorial(2) =  2 X 1
factorial(3) =  3 X 2 X 1
factorial(4) =  4 X 3 X 2 X 1
factorial(5) = 5 X 4 X 3 X 2 X 1

factorial(n) = n X  n-1 X......3 X 2 X 1

factorial(n) = n * factorial(n-1)

'''

'''def factorial(n):
  if(n==1 or n==0):
    return(1)
  return n * factorial(n-1)
  

n = int(input("enter a number"))
print(f"the factorial of this number is:{factorial(n)}")'''

#CHAPTER 8 practic set

# 1 QUECTION

'''a = 1

b = 2

c = 3

def manu(a, b, c):
  if(a>b and a>c):
    return
  elif(b>a and b>c):
    return b
  elif(c>b and c>a):
    return c
    
a = 1

b = 23

c = 3

print(manu(a, b, c))
  '''
  
# 2 QUECTION
'''def f_to_c(f):
    return 5 * (f - 32) / 9

f = int(input("Enter your temperature in Fahrenheit: "))
c = f_to_c(f)
print("Temperature in Celsius is:", round(f_to_c(f)))'''

# 3 QUECTION

'''print("a")
print("b")
print("c", end="")
print("d", end="")'''

#4 QUECTION

'''def sum(n):
  if(n==1):
    return 1
  return sum(n-1) + n
  
print(sum(3))'''

# 5 QUECTION

'''def pattern(n):
  if(n==0):
    return
  print("*" * n)
  pattern(n-1)
  
pattern(3)
'''

# 6 QUECTION

'''def inch_to_cms(inch):
  return inch * 2.54
  
n = int(input("enter value in inches"))

print("the correcponding value in cm is ", inch_to_cms(n))'''

# 7 QUECTION
'''def rem(l, word):
  while word in l:
    l.remove(word)
  return l

l = ["harry", "rohan", "subham", "an"]
print(rem(l, "an"))
'''
#8 QUECTION

'''def multiple(n):
  for i in range(1, 11):
    print(f"{n} X {i} = {n*i}")
    
multiple(5)'''


# big project mega project 1- Game

'''
1 for snake
-1 for water
0 for gun
'''

'''import random

# Randomly select computer choice
computer_choice = random.choice(["s", "w", "g"])
youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()

youdict = {"s": 1, "w": -1, "g": 0}

# Check for valid input
if youstr not in youdict:
    print("Invalid input!")
else:
    computer = youdict[computer_choice]
    you = youdict[youstr]

    print(f"Computer chose: {computer_choice}")

    if computer == you:
        print("It's a draw")
    elif computer == -1 and you == 1:
        print("You win!")
    elif computer == -1 and you == 0:
        print("You lose!")
    elif computer == 1 and you == -1:
        print("You lose!")
    elif computer == 1 and you == 0:
        print("You win!")
    elif computer == 0 and you == -1:
        print("You win!")
    elif computer == 0 and you == 1:
        print("You lose!")
    else:
        print("Something went wrong!")'''
        


# CHAPTER 9 - file i/o


'''
a = "a very long string with eamil"

email = []
3 second
'''

'''f = open("Pp.txt")#pp.txt is the file name
data = f.read()
print(data)
f.close()'''

'''st = "hey harry you are amazing"

f = open("myfile.txt", "w")
f.write(st)
f.close()'''

'''f = open("Manu.txt")

lines = f.readlines()

print(lines, type(lines))

f.close()'''


#you can you also while loop and so many th8ng see in book

'''lines = f.readlines()
while (line != ""):
  print(lines)
  line = f.readlines()

f.close()'''

# with statment


'''f = open("Manu.txt")
print(r.read())
f.close()'''

#you can use with statment

'''with open("manu.txt") as f:
  f.read()'''
  
# CHAPTER 9 practic set

# 1 QUECTION
'''
f = open("poem.txt")
content = f.read()
if("twinkle" in content):
  print("the words twinkle in python")
f.close()'''


# 2 QUECTION

'''import random

def Game():
  print("you are playing the game..")
  score = random.randint(1, 62)
  with open("hack.txt") as f:
    hiscore = f.read()
    if (hiscore==""):
      hiscore = int(hiscore)
    else:
      hiscore = 0
  print(f"your score: {score}")
  if(score>hiscore or hiscore==""):
    with open("hack.txt", "w") as f:
    hiscore = f.read()
    #enter the file name
    
  return score
  
game()'''

# 3 QUECTION
'''def generatetable(n):
  table = ""
  for i in range(1, 11):
    table += f"{n} X {i} = {n*i}\n"
    
  with open(f"table/table_{n}.txt", "w") as f:
    f.write(table)

for i in range(2, 21):
  generatetable(i)'''
  
# 4 QUECTION

'''import os
word = "donkey"

with open("r", "File.txt") as f:
  content = f.read()
  
contentnew = content.replace("donkey", "######")

with open("file.txt" "w") as f:
  content = f.write(contentnew)'''
  
# 5 QUECTION

'''words = ["donkey", "bad", "boy"]  # List of bad words to be censored

# Read the original file
with open("Chapter_9_5question.txt", "r") as f:
    content = f.read()

# Replace each bad word with ###
for word in words:
    content = content.replace(word, "#" * len(word))

# Write the cleaned content to a new file
with open("file.txt", "w") as f:
    f.write(content)'''
    
# 6 QUECTION

'''with open("Chapter_9_6quectio.txt")as f:
  content = f.read()
  
if ("python" in content):
  print("yes python is present")
else:
  print("python is not here")'''
  
# chater 10 _ object ortined programming

#class

'''class employee:
  name = "harry"#this is attribute
  laungauge = "py"#this is attribute
  salary = "1200000"# ""
  
harry = employee()
print(harry.name, harry.laungauge)'''

#class attribute

'''class employee:
  laungauge = "py"
  salary = "1200000"
  
harry = employee()
harry.name = "harry code"
print(harry.laungauge, harry.salary)

manu = employee()
manu.name = "manu maharaj"
print(manu.name, manu.salary, manu.laungauge)'''

'''class employee:
  laungauge = "py"
  salary = "1200000"
  
harry = employee()
harry.laungauge = "java acript"
print(harry.laungauge, harry.salary)'''

# self parameter
# static method

'''class employee:
  laungauge = "py"
  salary = "1200000"
  
  def getinfo(self):
    print(f"the laungauge is {self.laungauge}, the salary is {self.salary}")
  
harry = employee()
harry.laungauge = "java acript"

harry.getinfo()
#employee.getinfo(harry)'''


#_int constrcktor

'''class employee:
  laungauge = "py"
  salary = "1200000"
  
  def __int__(self):
    print("i am making greater object")
  
  def getinfo(self):
    print(f"the laungauge is {self.laungauge}, the salary is {self.salary}")
  
harry = employee()
harry.laungauge = "java acript"

harry = employee()
harry.name = "harry"

print(harry.name,harry.salary)
#employee.getinfo(harry)'''

#CHAPTER 10 practic set


# 1 QUECTION


'''class programmer:
  comapny = "microsoft"
  def __init__(self, name, salary, pin):
    self.name = name 
    self.salary = salary
    self.pin = pin
    
p = programmer("harry", 1200000, 802213) 

print(p.name, p.salary, p.pin, p.comapny)'''

# 2 QUECTION

'''class calculator:
  def __init__(self, n):
    self.n = n
  
  def square(self):
    print(f"the square is {self.n*self.n}")
a = calculator(4)
a.square()'''

# 3 QUECTION

'''class demo:
  a = 4
  
o = demo()
print(o.a)
o.a = 0

print(o.a)#no class attribute not chage why beacuse 

class demo:
  a = 4
  
o = demo()
print(o.a)
o.a = 0

print(demo.a)'''

# 4 QUECTION

'''from random import randint

class Train:
  
    def __init__(self, trainNo):
        self.trainNo = trainNo
  
    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")
  
    def getstatus(self):
        print(f"Train no: {self.trainNo} is running on time")
  
    def getfare(self, fro, to):
        print(f"Fare for train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")
  

# Object
t = Train(12399) 
t.book("Patna", "Delhi")
t.getstatus()
t.getfare("Patna", "Delhi")
  
'''

# 11 chater
#inheritance & more on oops 

'''class employee:
  comapny = "itc"
  def show(self):
    print(f"the name is {self.name} and the salary is {self.salary}")
    
    
#class programmer:
#  comapny = "itc infotech"
#   def show(self):
#     print(f"the name is {self.name} and the salary is {self.salary}")
    
#   def showlaungauge(self):
#     print(f"the name is {self.name} and he is good {self.laungauge} laungauge")

class programmer(employee):
  comapny = "itc infotech"
  def showlaungauge(self):
    print(f"the name is {self.name} and he is good with {self.laungauge} laungauge ")

a = employee()
b = programmer()

print(a.comapny, b.comapny)'''

# multipal inheritance

'''class employee:
  comapny = "itc"
  name = "defulat"
  def show(self):
    print(f"the name is {self.name} and the salary is {self.comapny}")
    
class coder:
  laungauge = "python"
  def printlaungagus(self):
    print(f"here is your laungauge : {self.laungauge} ")

class programmer(employee, coder):
  comapny = "itc infotech"
  def showlaungauge(self):
    print(f"the name is {self.comapny} and he is good with {self.laungauge} laungauge ")

a = employee()
b = programmer()

b.show()
b.printlaungagus()
b.showlaungauge()'''


#multi level inheritance

'''class employee:
  a = 1

class programmer(employee):
  b = 2

class maneger(programmer):
  c = 3
  
o = employee() 
print(o.a)
#print(o.b)

o = programmer()
print(o.a, o.b)

o = maneger()
print(o.a, o.b, o.c)'''


#super meathods

'''class employee:
  def __init__(self):
    print("constrcktor of employee")
  a = 1

class programmer(employee):
  def __init__(self):
    print("constrcktor of programmer")
  b = 2

class maneger(programmer):
  def __init__(self):
    super().__init__()
    print("constrcktor of maneger")
  c = 3
  
o = employee() 
print(o.a)
#print(o.b)

o = programmer()
print(o.a, o.b)

o = maneger()
print(o.a, o.b, o.c)'''

# class meathods

'''class employee:
  a = 1
  @classmethod
  def show(cls):
    print(f"the value is of a {cls.a}")
    
e = employee()
e.a = 45

e.show()'''

# property dectaced

'''class employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"the value of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self, value):
        parts = value.split(" ")
        self.fname = parts[0]
        self.lname = parts[1] if len(parts) > 1 else ""
e = employee()
e.a = 45               # instance variable
e.name = "harry khan"  # setter call hoga

print(e.fname, e.lname)  # harry khan
e.show()                # the value of a is 1'''

# oprator overloading

'''class number:
  def __init__(self, n):
    self.n = n
    
  def __add__(self, num):
    return self.n + num.n 
    
n = number(1)
m = number(2)


print(n+m)'''


# chater 11 practic set 

# first QUECTION

'''class twodvector:
  def __init__(self, i, j):
    self.i = i
    self.j = j 
    
    
  def show(self):
    print(f"the vector is {self.i}i + {self.j}j")
    
    
class threedvector(twodvector):
  def __init__(self, i, j, k):
    super().__init__(i, j)
    self.k = k
    
    
  def show(self):
    print(f"the vector is {self.i}i + {self.j}j + {self.k}k ")
    
a = twodvector(1, 2)
a.show()
b = threedvector(1, 2, 3)
b.show'''


     