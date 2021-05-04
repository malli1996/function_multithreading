s = 'sun raises in the east'
print(s)
t = s.split()

q=[t[j][::-1] for j in range(0,len(t),2)]
print(q)



# A function which doesn't contain any name is called lambda function or anonymous function
# lambda argument:expression
a=lambda a:a*2
a=a(10)
print(a)

name = input('enter your name:')
name1 = name[::-1]
if name==name1:
    print('name is palindrome')
else:
    print('name is not palindrome')

print('context managers are allocate and deallocate the resources')





# context managers are used to allocate and release the resources ,Example of context managers are with statement
# implementing context managers in class using __enter__,__exit__
# we are also implementing context managers are using generators,decorators.
# common use case of context managers are locking and unlocing the resources and closing opening the files.





# A decorator is a design pattern in python it allow the user to add new functionality to an
# existing object without modifying its structure.



