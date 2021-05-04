#syntax errors ---the errors which occur invalid syntax are called syntax errors
#Runtime errors ----The errors which occur while execution of the programm..
# once all syntax errors are corrected then only program execution starts
#runtime errors also call it as exceptions----while execution of the program something goes wrong
# because of end user input or programming logic or memory problems etc then we will get runtime errors.
#print(10/0)
#print(10/'ten')
'''x=int(input('enter number:'))
print(x)'''
#exception handling concepts applicable for runtime errors not syntax errors
#exception ---an unexpected event that disturbs normal flow of program  is called exception
#eg ;--zero division error,type error,value error,file not found error,eof error,sleeping error
#we should not block our resource and we should not miss anything
# we have to define alternative way to rest of the program execution
#within the try block if anywhere exception raised then rest of the try block not executed eventhough
#we handled that exception
#if try with multiple except blocks available
# single except block that can handle multiple exceptions
#except(zero division error,value error)as msg:
# default except block also available---it should be last in multiple except block
#finally block----it is not recommended to maintain clean up code
#whether exception raised or not raised and whether exception handled or not handled --such type of
# best place is nothing but finally block
#the main purpose of finally block is to maintain clean up code
#ry:
   # Risky code
#except:
 #   Handling code

#finally:
 #   cleanup code
#there is only one situation finally block won't be executed when ever we are using os._exit(0)
# we can take ty-except-finally blocks inside try or except or finally blocks i.e ..nesting of
# try- except-finally is possible
'''try:
    ---
    ----
    ---
    try:
        ----
        ----
    except:
        ----
        ---
        ---
    finally:
        -----
except:
    -----
    -----
finally:
    -----
    -----'''


#contro flow of nested try-except-finally:
#we can use else with try-except-finally
#else block will be executed if and only if there is no exceptions raised in try block
'''try:
 #   -----
    ------
except:
    -----
    -----
else:
    ----
    ----'''

#whenever we are writing else block compulsory except block shoulb be there i.e without except
#block we cnnot write else block

#try-except-else-finally order is important
#two types of exceptions
#pre-defined exceptions----pvm is responsible for pre-defined exceptions
#user defined exceptions-----programmer is responsible to define
# hence we have to raise explicitly based on our requirement using raise keyword
#eg;--insufficient funds,tooyoung ,tooold ,invalidinput

class TooYoungException(Exception):
    def __init__(self,arg):
        self.msg=arg
class TooOldException(Exception):
    def __init__(self,arg):
        self.msg = arg

age=int(input('enter age :'))
if age > 60:
    raise TooOldException('please wait some more time')
elif age < 18:
    raise TooYoungException ('you are wait more time')
else:
    print('you will get ')



#generally  we have to take risky code outer try block and too much risky code we have to take inner
#try block if any exception raised in inner try block inner except block will executed.if any exception
#raised at outer block outer except block will executed



