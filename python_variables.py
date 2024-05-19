# Databricks notebook source
# MAGIC %md
# MAGIC #### Common Usefull functions

# COMMAND ----------

# MAGIC %md
# MAGIC * help()
# MAGIC * type()
# MAGIC * print()
# MAGIC * dir()

# COMMAND ----------

name='this is ravi'
NAME = 'this is Vicky'
print(NAME)
print(name)

# COMMAND ----------

list = [1,2,3]
dir(list)

# COMMAND ----------

print('this is sample print function')

# COMMAND ----------

# MAGIC %md
# MAGIC #### Waht is Python Identifier?
# MAGIC * Python Identifier is the name we give to identify a `variable`, `list`, `tuple`, `sets`, `dictionary`, `function`, `class`, `module` or other `object`. That means whenever we want to give an entity a name, that’s called identifier.
# MAGIC
# MAGIC * Sometimes `variable` and `identifier` are often misunderstood as same but they are not. Well for clarity, let’s see what is a variable?
# MAGIC

# COMMAND ----------

v_name = "Ravi"
v_Name = "Khadar"
v_age = 35
v_status = 'true'  # True  true or False
# Variable - single - 

# COMMAND ----------

v_name="Ram"
print(v_name)

# COMMAND ----------

# print() -printing data
# type() - for verifying data type
# dir() - getting inforation about supporting functions or methods or classes....
# help() - complete note about object
v_age=45
type(v_status)

# COMMAND ----------

# MAGIC %md
# MAGIC #### What is a Variable in Python?
# MAGIC * A variable, as the name indicates is something whose value is changeable over time. In fact a variable is a memory location where a value can be stored. * Later we can retrieve the value to use. But for doing it we need to give a nickname to that memory location so that we can refer to it. That’s identifier, the nickname.
# MAGIC

# COMMAND ----------

name='Raj'
location="Bangalore"
age=32
v2=33.0
bool_true = True
bool_false = False

# COMMAND ----------

# upper case variable names -
PATH ="/location/temp/customer"
USERNAME="system"
PASSWORD ="232fsdf"

# COMMAND ----------

v_customerName="ram"

# COMMAND ----------

v_num1 =55 #140351035169184
v_num2=900 #140350630499824
v_num3=1000 #140350630499856
# 1 to 256 

# COMMAND ----------

id(v_num3)

# COMMAND ----------

age=25
AGE=33

# COMMAND ----------

get_saledate()
getSaleDate()

func_get_saledate()

# COMMAND ----------

type(age)

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Memory allocation for integer variables

# COMMAND ----------

a=100
b=555
print('a variable id is : ',id(a))
print('b variable id is : ',id(b))

# COMMAND ----------

id(a)

# COMMAND ----------

# here you can find same object id. Bcz python memory utilization it will store all integers in memory.
# if you are creating different variable with same value. it will use existing storage location and value to avoid more memory utilization.
# this numbers will be used for range [-5,256]
c=100
d=555
a=100
print('c variable id is : ',id(c))
print('d variable id is : ',id(d))
print('a variable id is : ',id(a))

# COMMAND ----------

# inside python list 55 value also having same id.
li =[11,22,55]
print(id(li[2]))

# COMMAND ----------

# above 256 its giving different id. So if you have any integers between range [-5,256] then it will reuse the memory.
a=300
b=300
print(id(a))
print(id(b))

# COMMAND ----------

#constant values
# host name, path,username,password.....
HOST_NAME=''
USER_NAME=''
PORT_NO=
PASSWORD

# COMMAND ----------

v_age=35
age_v=35
gv_age=
age_gv=

# COMMAND ----------

a=44
help(a)

# COMMAND ----------

type(age)

# COMMAND ----------

# MAGIC %sh /usr/bin/python

# COMMAND ----------

#TARGET_FILE_LOCATION='test'
print(TARGET_FILE_LOCATION)

# COMMAND ----------

# MAGIC %md
# MAGIC * local variables we can create starting with v_* name
# MAGIC * Global variables we can create starting with gv_* name
# MAGIC * Global Variables example: 
# MAGIC * * any source system and target paths(file locations) which is using entire project
# MAGIC * * common parameters which is unsing entire project like username and keys...
# MAGIC * * if any variable which is using in other notebooks we can create as gv_* variables.

# COMMAND ----------

# MAGIC %md
# MAGIC #### What is print()?
# MAGIC * The print() function prints the specified message to the screen, or other standard output device.
# MAGIC * The message can be a string, or any other object, the object will be converted into a string before written to the screen.

# COMMAND ----------

var="this is variable"
print('this is sample print string printing on screen using print() function ',var)

# COMMAND ----------

num1=55
num2='11'
print(str(num1)+num2)


# COMMAND ----------

name="ravi"
print('My Name is : ',name)
print('Type of Name variable is : ',type(name))

# COMMAND ----------

age=33   # int variable
print(age)
name='ravi' # String variable
print(name)
# Get the variable type using type() function
print('age Variable Type is :',type(age))
print('name Variable Type is :',type(name))


# COMMAND ----------

# Local Variables (v_)  # Creating local variables naming as v_variable_name
# Global Variables (gv_) # Creating global variables naming as gv_variable_name
#Another way which we can follow local and global variables managing in Upper case and lower case

v_age=55
gv_age=33
age=55
AGE=44
print(v_age)

# COMMAND ----------

num_1=4
num_2=2
print(num_1**num_2)

# COMMAND ----------

age="35"
age_v ="35"
a= type(age_v)
print(age + age_v,a)
# converting string to integer  int()


# COMMAND ----------

a='10'
b=20

#a+b
#int
#str
print('this is variale a value : ',a)
print('this is variable b value : ',b)
print('sum of a and b values is : ',a+str(b))

# COMMAND ----------

c='textvalue'
print(int(c))

# COMMAND ----------

# MAGIC %md
# MAGIC #### Creating Variable and Assigning a Values...
# MAGIC

# COMMAND ----------

a=b=c=d=e=55
a='sample'
print('a value is : ',a)
print('b value is : ',b)
print('c value is : ',c)
print('d value is : ',d)
print('e value is : ',e)
a

# COMMAND ----------

print('this is sample variable a Value : '+a)
type(a)
# + for addition or concatication

# COMMAND ----------

print(type(var))

# COMMAND ----------

num_v=10
NUM_V=15
print(NUM_V)

# COMMAND ----------

NAME='RAVI','RAM'
print(NAME)

# COMMAND ----------

ipaddress_v='193.12.12.4'
print(ipaddress_v)

# COMMAND ----------

id1=66
id2=77
print(id1+id2)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Strings
# MAGIC * Besides numbers, Python can also manipulate strings, which can be expressed in several ways. They can be enclosed in single quotes ('...') or double quotes ("...") with the same result 2. \ can be used to escape quotes:

# COMMAND ----------

print('spam eggs')  # single quotes
print('doesn\'t') # use \' to escape the single quote...
print("doesn't") # ...or use double quotes instead
print('"Yes," they said.')
print("\"Yes,\" they said.")
print('"Isn\'t," they said.')

# COMMAND ----------

# MAGIC %md
# MAGIC #### Numbers
# MAGIC * The interpreter acts as a simple calculator: you can type an expression at it and it will write the value. Expression syntax is straightforward: the operators +, -, * and / work just like in most other languages (for example, Pascal or C); parentheses (()) can be used for grouping. For example:

# COMMAND ----------

print(6//2)
print(6/2)

# COMMAND ----------

print(2 + 2)
print(50 - 5*6) 
print((50 - 5*6) / 4)
print(8 / 5)  # division always returns a floating point number

# COMMAND ----------

# MAGIC %md
# MAGIC * Division (/) always returns a float. To do floor division and get an integer result (discarding any fractional result) you can use the `//` operator; to calculate the remainder you can use %:

# COMMAND ----------

print(17 / 3)  # classic division returns a float
print(17 // 3)  # floor division discards the fractional part
print(17 % 3) # the % operator returns the remainder of the division
print(5 * 3 + 2)  # result * divisor + remainder

# COMMAND ----------

# MAGIC %md
# MAGIC * it is possible to use the ** operator to calculate powers

# COMMAND ----------

print (5 ** 2) # 5 Squared
print (2 ** 7) # 2 to the power of 7

# COMMAND ----------

# MAGIC %md
# MAGIC * The equal sign (=) is used to assign a value to a variable. 
# MAGIC * `+` for Concatenating two strings for string data type variables

# COMMAND ----------

a='Vikranth'
b='Reddy'
c= a + b # + working as Concatenation operator
print(c)

# COMMAND ----------

a = 10
b = 111
c = a+b  # + working as adition operator
print(c)

# COMMAND ----------

num=10
name='Ravi'
myfloat = 5.90
print(num)
print(name)
print(myfloat)
print("num variable Data type is : ",type(num))
print('name variable Data type is : ' , type(name))
print('myfloat variable data type is : ',type(myfloat))

# COMMAND ----------

# MAGIC %md
# MAGIC #### Multiple Assignment
# MAGIC * Python allows you to assign a single value to several variables simultaneously

# COMMAND ----------

name=12
print("this is sample variable value : ",name)

# COMMAND ----------

a = b = c =55
print('a variable Value is : ',a)
print('b variable Value is : ',b)
print('c variable Value is : ',c)

# COMMAND ----------

a,b=55,66

# COMMAND ----------

V1='55'
print(type(V1))
V2='TEST'
print(type(V2))

# COMMAND ----------

a=55
a=66

# COMMAND ----------

num1=5
num2=9
print('The average of the numbers you entered is', (num1+num2)/2)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Adding two int variables.

# COMMAND ----------

id=128

print('This is my TEXT Variable : ',type(id) )

# COMMAND ----------

""" Declare a variable and initialize it"""
A = '5'
a = '10'
#printing Variable
print('Variable value is :',A)
print('Variable value is :',a)
#verifying Data Type  using TYPE()
print('Variable Type A Is : ',type(A))
print('Variable Type a Is : ',type(a))
# Adding two variables
print('Sum of A plus a : ',int(A)+int(a))


# COMMAND ----------

# MAGIC %md
# MAGIC #### Adding String & Interger Variables
# MAGIC * Data Type Conversions using
# MAGIC * int
# MAGIC * str

# COMMAND ----------

# Declare a variable and initialize it
A = "55"
B = 66
print(A+str(B))

# COMMAND ----------

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
print(x,y,z)

# COMMAND ----------

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
print(x,y,z,w)

# COMMAND ----------

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
x,y,z

# COMMAND ----------

# Declare a variable and initialize it
A = "55"
B = 66
C = int(A)+B
C

# COMMAND ----------

# Declare a variable and initialize it
A = "55"
B = 66
C = int(A)+B
#printing Variable
print('Variable value is A :',A)
print('Variable value is B :',B)
#verifying Data Type  using TYPE()
print('Variable Type A Is : ',type(A))
print('Variable Type B Is : ',type(B))
# Adding two variables
print('Sum of A plus B : ',A+str(B))
print('Type of A + STR(B) : ',type(A+str(B)))
print('Sum of A Plus B : ',C)

# COMMAND ----------

# Declare a variable and initialize it
A = "55"
B = 66
#printing Variable
print('Variable value is A :',A)
print('Variable value is B :',B)
#verifying Data Type  using TYPE()
print('Variable Type A Is : ',type(A))
print('Variable Type B Is : ',type(B))
# Adding two variables
print('Sum of A plus B : ',int(A)+B)
print('Type of int(A) + B : ',type(int(A)+B))


# COMMAND ----------

# MAGIC %md
# MAGIC #### Delete a variable using DEL 

# COMMAND ----------

A=55
print(A)
del A
print(A)

# COMMAND ----------

table_name='customer'
total_rows=534
print("Total Number of records processed {} for {} ".format(total_rows,table_name))

# COMMAND ----------

# MAGIC %md
# MAGIC #### F-strings 
# MAGIC * F-Strings provide a way to embed expressions inside string literals, using a minimal syntax. It should be noted that an f-string is really an expression evaluated at run time, not a constant value. In Python source code, an f-string is a literal string, prefixed with 'f', which contains expressions inside braces. The expressions are replaced with their values.  

# COMMAND ----------

c_count= 40
target_count=30
reject=10
fstring = f'source count is : {c_count} target count is : {target_count} rejected count is : {reject}'
print(fstring)

# COMMAND ----------

c_count= 40
target_count=30
reject=10
print('customer data processed',c_count)

print('customer data process completed and source count :{c} target count : {b} and rejected count :{a}  '.format(a=c_count,b=target_count,c=reject)) 
# position based 
# Index based  - indexes start with zero (0)
# refrenced 

# COMMAND ----------

name="Suresh"
age=35
string=f'this is : {name} And My age is : {age}'
print(string)

# COMMAND ----------

name='Sai Ram'
age = 28
f_string = f'My Name is : {name} and My Age is : {age}'
print(f_string)

# COMMAND ----------

a=55
b='ravi'
print(f'a value is : {a} , b variable value is : {b}')
fstring=f'Hi.. sample F String text A value: {a} And B Value is : {b}'
print(fstring)

# COMMAND ----------

x=55
y=66
str = f"X variable value is: {x} test for f-strings Y variable value is : {y}"
str

# COMMAND ----------

list(range(1,10))

# COMMAND ----------

name='RAVIT'
len(name)
# items - no of items (n-1) = 100(99)
# if u are using range (min) and max - items

# COMMAND ----------

# MAGIC %md
# MAGIC #### Python indexes
# MAGIC * left to right 0 to n
# MAGIC * right to left -1 to -n
# MAGIC * indexes max value (n-1)

# COMMAND ----------

100 (99),1000(999)

# COMMAND ----------

# MAGIC %md
# MAGIC #### format() function
# MAGIC * `str.format()` is one of the string formatting methods in Python3, which allows multiple substitutions and value formatting. This method lets us concatenate elements within a string through positional formatting.
# MAGIC * __Syntax__  : `{ } .format(value)`
# MAGIC
# MAGIC   Parameters : `(value)` : Can be an integer, floating point numeric constant, string, characters or even variables.
# MAGIC
# MAGIC   Returntype : Returns a formatted string with the value passed as parameter in the placeholder position.
# MAGIC * The placeholders can be identified using named indexes {price}, numbered indexes {0}, or even empty placeholders {}.
# MAGIC
# MAGIC

# COMMAND ----------

name="raj"
age=35
print('my name is {b} and my age is : {a} '.format(a=age,b=name))

# COMMAND ----------

name='Reshwanth'
age=25
sal=2000
commission=200
total_salary= sal+commission
print('My Name is : {0} And My Age is : {1} , my total salary is : {2}'.format(age,total_salary,name))

# COMMAND ----------

# empty place holders and it will occupy based on position based left to right
print('My Name is {name} and I am living in {loc} '.format(name='Ravi',loc='BAngalore'))

# COMMAND ----------

#index value based placeholders
print("this is a {2} sample {1} format {0} function usage example ".format(55,66,77))

# COMMAND ----------

print("I am working in {a} and i like programming {b} ".format(a='IT',b='Python '))

# COMMAND ----------

# the str.format() method 
# using format option we can pass values using curly brackets {}
print ("{}    function example .".format("FORMAT-STRIN G")) 
# using format option for a  value stored in a variable 
str = "Sample text printing using format function in {}"
print (str.format("Python")) 


# COMMAND ----------

age=35
name='Ravi'
# formatting a string using a numeric constant 
print("My Name is {} & I'm {} years old".format(name,age))

# COMMAND ----------


print("My Name is {a} & I'm {b} years old".format(a=name,b=age))

# COMMAND ----------

print('i like {0} programming and {1} data '.format('Python','Big '))

# COMMAND ----------

# MAGIC %md
# MAGIC #### {field_name:conversion}
# MAGIC More parameters can be included within the curly braces of our syntax. Use the format code syntax {field_name:conversion}, where field_name specifies the index number of the argument to the str.format() method, and conversion refers to the conversion code of the data type.
# MAGIC
# MAGIC * s – strings
# MAGIC * d – decimal integers (base-10)
# MAGIC * f – floating point display
# MAGIC * c – character
# MAGIC * b – binary
# MAGIC * o – octal
# MAGIC * x – hexadecimal with lowercase letters after 9
# MAGIC * X – hexadecimal with uppercase letters after 9
# MAGIC * e – exponent notation 

# COMMAND ----------

# Convert base-10 decimal integers  
# to floating point numeric constants 
print ("This site is {0:f}% securely {1}!!".format(100, "encrypted")) 
  
# To limit the precision 
print ("My average of this {0} was {1:.2f}%".format("semester", 78.234876)) 
  
# For no decimal places 
print ("My average of this {0} was {1:.0f}%".format("semester", 78.234876)) 
  
# Convert an integer to its binary or 
# with other different converted bases. 
print("The {0} of 100 is {1:b}".format("binary", 100)) 
          
print("The {0} of 100 is {1:o}".format("octal", 100)) 

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Using “%s” keyword

# COMMAND ----------

loc='Bangalore'
name='Ravi'
print("my name is : %s And i am living in : %s "%(name,loc))

# COMMAND ----------

x=55
y=44.4443
print("this is integer %f and this is float value : %f "%(x,y))

# COMMAND ----------

# type conversion for calculations
# format conversion

# COMMAND ----------

a='RESHWANTH'
b='VIKRANTH'
print("sample example  : String1 %s String2 %s" % (a, b))
print("Sample Example : String1 {} String2 {}".format(a, b))

# COMMAND ----------

print("{!s}".format("this"))
print("{:s}".format("that"))

# COMMAND ----------

print("{} , {}".format(1, 1.23))
print("%d , %f"%(1, 1.23)) 

# COMMAND ----------

s = "thistestfortesting"

print("The characters with odd index are '%s'" %s[1::2]) #(skipping every 2 indexes )


# COMMAND ----------

s = "Hey there! what should this string be?"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))

# COMMAND ----------

# MAGIC %md
# MAGIC #### Data Types...
# MAGIC * 1) STR
# MAGIC * 2) INT
# MAGIC * 3) FLOAT
# MAGIC * 4) COMPLEX
# MAGIC * 5) LIST
# MAGIC * 6) TUPLE
# MAGIC * 7) RANGE
# MAGIC * 8) DICT
# MAGIC * 9) SET
# MAGIC * 10) FROZENSET
# MAGIC * 11) BOOL
# MAGIC * 12) BYTES
# MAGIC * 13) BYTEARRAY
# MAGIC * 14) MEMORYVIEW

# COMMAND ----------

