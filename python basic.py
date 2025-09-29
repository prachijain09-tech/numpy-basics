#20 august 25
#lines changed = no of times backslash n is used
# space  in print statement also gets print
#print('prahi\n\n jain')
#output will be prachi space of three lines then jain 
# 1st the code inside bracket  will run then  outside  code will get excuted .


#input  from user with printing statement without using print
'''a=input('enter 1st number ') 
b=input('enter 2nd nuber ')
c=input('enter 3rd number ')
d=input('enter 4th number ')
print(type(a))  #str 


# multiple inputs in single line
a,b,c= map(int,input().split())

#type conversion
p=int(a) 
q=float(b)
r=int(c)
s=float(d)


#direct type conversion
#a=int(input('enter 1st num'))  a will of int typpe from start no need to use extra variable 

print ('arithmetic operations on numbers are ')#error write without space from start(unexpected intent ) 
total=(p+q)
product=(q*r)
difference=(r-s)
div=(s/r)
print('results are ' , total,product,difference,div)# comma is the seperator


# all the outputs print in same line
print(f'results are \n{total}\n{product}\n{difference}\n{div}')# to print output in next line we use f string method 
print(a+b) #python takes input from user as a string so 2+2=22 '''



#concept of libraries
'''import math #math is pre defined library 
f=math.pow(2,4)  # to use  functions of library  name of (library . function) 
print(f)'''


#predefined short words in python
'''import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))'''




# area of shapes
'''import math
print('area of  various shapes ')
r=float(input('enter radius of circle '))
area_circle=math.pi*r*r
print(f'area circle {area_circle}')
        
s=float(input('enter side of square'))
area_square=s*s
print(f'area square{area_square}')
        
l=float(input('enter length of rectangle'))
b=float (input('enter breadth  of rectangle '))
area_rectangle =l*b
print(f'area rectangle{area_rectangle}')'''

#21 august 25
# converting from one  number system to another
'''x=int(input('enter a number to convert '))
y=bin(x)
print(y)'''


# using readymade functions
'''g=[0,1,2,5,7,3,9,11,45,89]
a=max(g)
b=min(g)
print(len(g))
print(a)
print(b)'''

# conditional statements [1]
'''x=6
if x>0: # use colon(:) after if condition 
     print('number is positve ')# same identation (space) is required for all the statements under print statement
     print(' positive number always greater than negative number ')
#print('hello', x ,'is positive') # this print statement is written out of if block if we want to get out of if block start  without space  at the beginning
else:
    print('negative')'''

#conditional statement [2]
''' x=int(input('enter number'))
 if x:
     print(x,' is positive')
elif x<0:
    printf(x,'  is negative')
el'''

# maximum of two numbers
'''a=int(input('enter 1st number '))
b=int(input('enter 2nd number'))
print(max(a,b),'is greater ')'''

#swapping of two numbers
'''a=int(input('enter 1st number '))
b=int(input('enter 2nd number'))
temp=a
a=b
b=temp
print(a,b)'''

# even odd program
'''x=int(input('enter number '))
if x%2==0:
    print("even")
else:
    print('odd')'''

#loops
# loops/iterative statements
# predefined function in python "Range"
#works in three ways 1) range(stop) starts from zero without including destination point/stop point 
#                    2)range (start ,stop )
#                    3) range (start , stop, step) step matlab utne se aaage bdega

'''for i in range(10):
     print('hello') # output 10 times hello 

for i in range (0,5):
          print('hello')'''#output 5 times hello 0to4 
          
'''for i in range(2,8,4):
    print('hello')''' # output 2 times hello 
     


'''my_list = ['a', 'b', 'c']
for i in range(len(my_list)): # for loop 
  print(f"The item at index {i} is {my_list[i]}")'''


'''fruits = ["apple", "banana", "cherry"]
for x in fruits: # for each loop 
  print(x,end='   ')'''

'''i = 0
while i < 6:
  print(i)
  i += 1'''

#list
''''b=[5,6,8,1,4,2,9,11,45,22,54]
b.append(2)    #append insert at the end
b.insert(index,data)# insert inserts value in the index we want to add
b.index(value)# to find index number of particular value
b.sort() #python only sorts in ascending order to sort in descending order use sort then reverse
b.reverse()
b.remove(value)
b.pop(index no )
b=b1 #  equal assign address of b in b1 both points the same memory
b1=b.copy() # new copy of b is created 
for i in b:
    print(i)'''

#slicing operator [start: stop: step]
'''h1=[1,2,3,4,5,6,7,8,9] #puri value me se ek choti value nikal de deta he subset of full set
p=h1[2:6:2]# if stop and step condition nahi likhi to start index se sare print kar dega 
a=h1[0]
b=h1[-1::-1] #end se start kiya or aage tak gaye ek ek kam karke -1 index means 9 and 9se ek ek kam karke aage jana he upto 1
print(p)
print(a)
print(h1[-1]) # python has -ve indexing also starts from last side last =-1....
print(b)'''

# reverse using slicing operator
'''x='prachi'
a=x[-1::-1]
print(a)'''


#tuple() small brackets
# can put data without brackets
#tuple can also have differnt data types members
# once element is writtern under tuple cannot be changed and data under list can be changed 
# tuple does not have predefined functions so convert tuple to list
'''t1=(1,2,6,3,9,7,4,5)
#  t1.sort()  throws error
t2=list(t1)
print(t2)
t3=sorted(t2)
print(t3)'''

# tuple has only two functions count and index
#count=  no of times a vaule is appearing in tuple
#index=position  of data in tuple
'''t1=(3,5,6,3,8,9,3,5,8,2)
a=t1.count(3)
b=t1.index(3) #gives index of 1st time data  (fundamental behaviour)
print(a,b)'''

#set 
#cant insert duplicate data if inserted  automatically get discarded
# sets dont have index,slicing operator  and dosnt maintain order 
'''s1={11,33,55,66,77,22,11,33,55,66}
print(s1)'''

# dictionary
#array 2 types numeric(accessing with index ) and associative(accessing through key and the key must be unique )
#d1={


#ATM pin program
'''pin=1234
c=0
while c!=3:
    c=c+1;
    p=int(input("Enter a Pin "))
    if p==pin:
        print("Transection Successfull")
        break
    else:
        print("Incorrect Pin", "Enter Pin Again: ")
else: # this else if of while loop while-else lekin break krne ke baad while ka else bhi break ho jayega
    print("Card Blocked","Try After Sometime")
'''

#function 
#def is a keyword to define function
'''def arithmetic_operations(a,b): # a and b are formal parameters # entry point of function
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    print( sum, sub,mul,div)
    # return keywor to exit program and return value to calling function
    return sum,sub,mul,div # returning multiple values # exit point of function
num1, num2  =map(int,input("Enter two numbers: ").split())  # actual parameters
arithmetic_operations(num1,num2 ) # calling function 
'''

#recursion 