'''
Executing several tasks simultaneously is the concept of multitasking
Process based multitasking----each task is separate independent process----listen music,write code,download a file
thread based multitasking------separate independent of the same program---this is suitable for programming level
whether process based or thread based executing of multitasking improves the performance and reduce the response time
To develope web and application servers
to develop multimedia graphics,animation,video games
where ever group of independent jobs are available,then it is highly recommended to execute simultaneously instead of
one by one . such type of cases we should go for multithreading
developing multithreading programs is easily in python
by using threads we can implement multithreading programs
by default main thread available
creating thread without class
creating thread with extending thread class
creating thread without extending thread clas


from threading import *
def display():
    for i in range(1,11):
        print('child third')
t=Thread(target=display())   #cannot provide exact output varied machine to machine
t.start()
for i in range(1,11):
    print('main thread')

# thread is a predefined class in threading module which can be used to create our own threads
#below program without  multithreading

from threading import *
import time
def double(numbers):
    for i in numbers:
        time.sleep(1)
        print('doubles:',i*i)

def squares(numbers):
    for t in numbers:
        time.sleep(1)
        print('square:',t *2)
numbers = [1,2,3,4,5]
begintime = time.time()

double(numbers)
squares(numbers)

print('the total time taken :',time.time()-begintime)


#with multithreading
from threading import *
import time
def doubles(numbers):
    for i in numbers:
        time.sleep(1)
        print('doubles:',i*i)

def squares(numbers):
    for t in numbers:
        time.sleep(1)
        print('squares:',t**2)
numbers=[1,2,3,4,5]
begintime = time.time()
t1 = Thread(target=doubles,args=(numbers,))
t2 = Thread(target=squares,args=(numbers,))
t1.start()
t2.start()
print('total time takene:',time.time()-begintime)

#getting name of the thread,setting name of the thread
from threading import *
print('threading name:',current_thread().getName())
current_thread().setName('pawan kalyan')
print('threading name :',current_thread().getName())
print('threading name :',current_thread().name)

#thread identification number(ident)
#for everythread internally a unique identification number is available

def test():
    print('child thread')
t = Thread(target=test)
t.start()
print('child thread identification number :',t.ident)


#Active_thread()----this function returns number of active threads currently running
from threading import *
import time
def test():
    print(current_thread().getName(),'started')
    time.sleep(3)
    print(current_thread().getName(),'ended')
print('the number of active threads :',active_count())
t1 = Thread(target=test,name='childthread1')
t1.start()
print('the number of active threads:',active_count())
time.sleep(5)
print('the number of active threads :',active_count())'''

# if a thread wants to wait until completing some other thread then we should go for join() method
from  threading import *
import time
'''def display():
    for i in range(10):
        print('seetha thread')
        time.sleep(2)
t = Thread(target=display)
t.start()
t.join() # this line execu ted by main thread
for i in range(10):
    print('rama thread')'''


# join() method works with time based also
# in this thread wants to wait some time after that it executed

'''def dss():
    for i in range(10):
        print('seetha thread')
        time.sleep(2)
n = Thread(target=dss)
n.start()
n.join(5)
for i in range(10):
    print('rama thread')'''

#Daemon threads ---the threads which are running in the background are called daemon threads
# the main objective of daemon threads is supportive ot non-daemon thread.

#synchronization---multiple threads are executing simultaneously if there is a chance of data inconsistency problems


'''def display(name):
    for i in range(10):
        print('good morning:',end='')
        time.sleep(2)
        print(name)
t = Thread(target=display,args=('yuvaraj',))
t2 = Thread(target=display,args=('mahesh',))
t.start()
t2.start()'''

#in synchronization threads are executed one by one we are overcome data inconsistency problems

# the main applications used to synchronization is ---online reservation system,funds transfer from joint accounts
# we can implement synchronization using --Lock,Rlock,semaphore
'''
locks are the most fundamental mechanisms provided by  threading module,lock hold the one thread 
at a time,if any other thread required the same lock it will wait until the thread releae lock(washroom,telephone booth)
s = lock()
a thread can acquire the lock by using acquire method
s.acquire()
a thread can release the lock by using release method
s.release()

To call release method compulsory there should be owner of that lock,thread should has the lock already ,

from  threading import *
import time
l = Lock()
def display(name):
    l.acquire()
    for i in range(10):
        print('good morning:',end='')
        time.sleep(2)
        print(name)
    l.release()

t = Thread(target=display,args=('mahesh',))
t1 = Thread(target=display,args=('madhu',))
t2 = Thread(target=display,args=('malli',))
t.start()
t1.start()
t2.start()'''


# in the above At a time only one thread is executed display() method and hence we will get regular output
# there is a problem wih simple lock,--- doesn't care which thread is locked
#RLock()----only owner thread can acquire the lock multiple times
#the number of acquire () and release() methods should be matched


'''from threading import *
import time
l=RLock()
def factorial(n):
    l.acquire()
    if n==0:
        return 1
    else:
        result = n*factorial(n-1)
    l.release()
    return result

def result(n):
    print('factorial of ',n,'is:',factorial(n))
t = Thread(target=result,args=(5,))
t1 = Thread(target=result,args=(6,))

t.start()
t1.start()'''



# in the case of Lock and RLock only one thread is allowed to execute
# sometimes our requirement is to particular number of threads are allowed to access(like at a time 10 members to access database)
#(four access the network connection)--and this time we should go for semaphore concept



from threading import *
import time
s = Semaphore(2)
def display(name):
    s.acquire()
    for i in range(10):
        print('good morning :',end='')
        time.sleep(2)
        print(name)
    s.release()
t = Thread(target=display,args=('mahesh',))
t2 = Thread(target=display,args=('malli',))
t3 = Thread(target=display,args=('yamini',))
t4 = Thread(target=display,args=('siva',))
t.start()
t2.start()
t3.start()
t4.start()

# the main advantage of synchronization  is to overcome the datainconsistency problems
# the disadvantage is wait more time for execution




