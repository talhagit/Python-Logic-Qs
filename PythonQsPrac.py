"""Python Questions"""

"""
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""

def find_num(start,end):
    list=[]
    for i in range(start,end):
        if (i%7==0) and (i%5!=0):
          print (i)
          list.append(str(i))
    print(','.join(list))
        

find_num(100,150)


"""Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line."""

def find_fact(number):
    if number==0:
        return 1
    return number*find_fact(number-1)

print(find_fact(4))

"""With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
"""
def square(num):
    dic={}
    for i in range(1,num+1):
        dic[i]=i*i
    print(dic)
        
square(4)

"""Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:

Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods."""

class InOutString(object):
    def __init__(self):
        self.s=""
    
    def getstring(self):
        self.s = input
    
    def printstring(self):
        print(self.s)
        
        
s=InOutString()
s.getstring()
s.printstring()

"""Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24"""

import math

def getSR(*args):
    C=50
    H=30
    #item=[x for x in args.strip(',')]
    for ind in args:
        print(math.sqrt(C*H*ind))
        
getSR(2,3,4)
        
"""Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""

for i in range(1000,2222):
    istr=str(i)
    if (int(istr[0])%2==0) and (int(istr[1])%2==0) and (int(istr[2])%2==0) and (int(istr[3])%2==0):
        print(i)
        
"""Write a program that accepts a sentence and calculate the number of letters and digits."""

s='This is a test 123'
data={'Digits':0,'Char':0}
for d in s:
    if d.isdigit():
        data['Digits']+=1
    if d.isalpha():
        data['Char']+=1
print(data['Digits'],data['Char'])        

"""
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
   """
def tran(s):
    values=0
    for i in s.split(' '):
        if i[0]=="D":
            value=int(i[1:len(i)])
            values+=value
        if i[0]=="W":
            value=int(i[1:len(i)])
            values-=value
    return values
        #print(i[1:len(i)])

tran('D100 D200 W150')
     

"""A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1"""
import re
def passcheck(s):
    passw=[]
    items=[x for x in s.split(',')]
    for p in items:
        if len(p)<6 or len(p)>12:
            continue
        else:
            pass
        if not re.search("[a-z]",p):
            continue
        elif not re.search("[0-9]",p):
            continue
        elif not re.search("[A-Z]",p):
            continue
        elif not re.search("[$#@]",p):
            continue
        elif re.search("\s",p):
            continue
        else:
            pass
        passw.append(p)
        print (','.join(passw))
            
        
            
passcheck('ABd1234@1,a F1#,2w3E*,2We3345')

#class Person:
#    # Define the class parameter "name"
#    name = "Person"
#    
#    def __init__(self, name = None):
#        # self.name is the instance parameter
#        self.name = name
#
#jeffrey = Person("Jeffrey")
#print ("%s name is %s" % (Person.name, jeffrey.name))
#
#nico = Person()
#nico.name = "Nico"
#print "%s name is %s" % (Person.name, nico.name)

"""Write a function to compute 5/0 and use try/except to catch the exceptions."""

def check():
    return 5/0

try:
    check()
except ZeroDivisionError:
    print ('/ 0 Error occurs')
except Exception:
    print ("Exception called")

"""Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10]."""
lists=[1,2,3,4,5,6,7,8,9,0]
squared=map(lambda x:x**2,lists)
print(set(squared))
        
    

