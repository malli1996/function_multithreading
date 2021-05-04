# functions executs some set of code repeatedly when we want by calling that function
# we can call the function any number of times

'''def name(name):
    print('hi how are you',name)
name('mallikarjuna')
name('mahesh')
name('rjesh')


def square(number):
    print(number,'number square is ',2**number)
square(2)
square(4)
square(6)

#function can take input values as parameters and executes business logic ,and returns output to the caller  with return statement

def add(x,y):
    return x+y
result=add(10,29)
print(result)
print('sum is ',add(10,33))


def second(number):
    if number%2 == 0:
        print('number is even')
    else:
        print('numjber  is odd')

second(2)
second(3)
second(5)
second(6)
# returning multiple values from a function

def operator(x,y):
    sum = x+y
    sub = x-y
    return sub,sum
t=operator(10,30)
for i in  t:
    print(i)
# they are four types  of actual arguments
# positional arguments-----sub(10,20)
# keyword arguments---sub(name = 'malli,age = 40)
# default arguments------sub(name = 'malli')
# variable length arguments-----sub(s,*n),sub(s,**n)

# positional arguments
def solo(name,age):
    print('his name is ',name,'and age is ',age)
solo('mahesh',22)
solo('malli',33)

#keyword arguments
def solo(name,age):
    print('his name is ',name,'and age is ',age)
solo(name='mahesh',age=20)
solo(name='ram',age=22)
solo('mahesh',age=30)

# default arguments
def solo(name = 'mahesh'):
    print('his name is ',name)
solo()
solo()
solo()

# variable length arguments
def solo(s,*n):
    print('his name is ',s)
    t = 0
    for i in n:
        t = t+i
        print(t)

solo('prakesh',10,20,30)

# another way variable length argumentss
def solo(*p):
    for s in p:
        print(s)
solo(10,20,30,40,60)

# variable length arguments to key value pair

def solo(**kwargs):
    for k,v in kwargs.items():
        print(k,"------",v)

solo(name = 'malli',age =33, district= 'kurnol')


# functions case study

def f1(arg1,arg2,arg3=4,arg4=8):
    print(arg1,arg2,arg3,arg4)
f1(3,2)
f1(10,20,30,40)
f1(10,20,arg4=100)
f1(arg4=33,arg1=44,arg2=88)

#f1(arg3=99,arg4=88,30,40) # after keyword arguments we should not take positional arguments


# a group of lines with some name is called function
# a group of functions saved to file is called module
# a group of modules nothing but libray


# global variables --the variables which are declared outside of the function is called global variable
#we can acces this global variable to all functions of the module

# two types of variables available function one is global variable,local variable
#global variable----
s = 100
def m1():
    print(s)
def m2():
    print(s)
def m3():
    print(s)

m1()
m2()
m3()

#local variable
def m1():
    a = 100
    print(a)
def m2():
    t = 20
    print(t)
#def m3():
#   print(a)
m1()
m2()
#m3()

#local variable and global varibale

t = 300
def s1():
    t = 400  # you are commited to i am representing this value as global
    print(t)
def s2():
    print(t)
s1()
s2()
a= 200
def p1():
    global a
    a = 300
    print(a)

def p2():
    print(a)
p1()
p2()

def m1():
    a = 20
    print(a)
def m2():
    pass
m1()

#if global variable and local variable having the same name then we can access global variable inside a funtion as follws

a = 300
def m1():
    a = 200
    print(a)
    print(globals()['a'])
m1()


def m2():
    global t
    t = 200
    print(t)
def m3():
    print(t)

m2()
m3()
# a function that calls itself is known as recursive function
# the main advantages of recursive funtion is  reduce the length of the code and improves readbility
# solve complex problems easily

def fact(n):
    if n==0:
        result=1

    else:
        result = n*fact(n-1)
    return  result
print(fact(4))
print(fact(3))

# sometimes we declare a function without any name is known anonymous funtion or lambda functions
# just for instant use

#syntax
# lambda argument_list:expression
s = lambda n :2**n
print(s(3))
print(s(4))
print(s(5))

#sometimes we can pass function as argument to another function,in such cases  lambda functions are best choice
# we can use lambda functions very commonly with filter(),map(),reduce() functions because these functions expect function as argumet
'''
#filter(function,sequence)
l = [10,20,30]
l1=list(filter(lambda x:x%2==0,l))
print(l1)

l = [13,20,10,15]
l2=list(filter(lambda x:x%2!=0,l))
print(l2)


#map function
s = (12,2,4,5)
n=list(map(lambda x:2**x,s))
print(n)

t = (12,2,4,5)
t1 = (12,5,4,2)
t2=list(map(lambda x,y : x+y,t,t1))

print(t2)


#reduce function
# it gives you single element after sequence of reduction on condition

from functools import *
b = [1,2,3,4,5]
b1=reduce(lambda x,y:x*y,b)
print(b1)

# in python everything is treated as object
# functions also internally created as objects only

def f1():
    print('hello')
f1()
print(id(f1))
# function aliasing
# for the existing function we can give another name,which is nothing but aliasing.

def wish(name):
    print('his name is :',name)

greet=wish
wish('malli')
greet('yamini')
print(id(greet))
print(id(wish))
del wish
greet('manasa')

# we can declare a function inside the existing function or another function,we can call it as nested function
def outer():
    print('this is outer function')
    def inner():
        print('this is inner function')
    print('outer function calling inner function')
    inner()
outer()# here outer function first calls the outer then after printing ,inner funciton also executed.
# inner function is a local to outer function and hence it is not possible to call directly from outside of
#outer()function

def outer():
    print('outer function started')
    def inner():
        print('inner function execution')
    print('outer function returning inner function')
    return inner

f1=outer()
f1()
f1()

# we can pass function as argument to another function
# map(function,sequence)
# filter(function,sequence)
# reduce(function,sequence)

# decorator is a function which can take funcion as argument a and extend its functionality and returns
# modified function with extended functionality
# the main objective of decorator function is extend the functionality of existing functions without modifies that function





# nested function

def outerFun(a, b):
    square = a**2
    def innerFun(a,b):
        return a+b
    add = innerFun(a, b)
    return add+5

result = outerFun(5, 10)
print(result)



# recursive function

def calculateSum(num):
    if num:
        return num + calculateSum(num-1)
    else:
        return 0

res = calculateSum(10)
print(res)










