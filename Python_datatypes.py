# Databricks notebook source
var2 = 5
print('Var is greater than 10') if var2 >10 else print('Var2 is less than 10')
  

# COMMAND ----------

Type casting 

# COMMAND ----------

help(range)

# COMMAND ----------

# string,
string_type = 'single quote'
string_type="double quote"
type(string_type)

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

# MAGIC %md
# MAGIC ##### Range data Type
# MAGIC * The range() function is used to generate a sequence of numbers over time. 
# MAGIC * At its simplest, it accepts an integer and returns a range object (a type of iterable)
# MAGIC * syntax: `range(start, stop, step)`
# MAGIC * `start`	Optional. An integer number specifying at which position to start. Default is 0
# MAGIC * `stop`	Required. An integer number specifying at which position to stop (not included).
# MAGIC * `step`	Optional. An integer number specifying the incrementation. Default is 1

# COMMAND ----------

v_range = range(10,100,5) # n-1

# COMMAND ----------

print(v_range)
print(list(v_range))

# COMMAND ----------

v_range =range(5,100,5)


# COMMAND ----------

range_v = range(10)
print(type(range_v))
print(tuple(range_v))

# COMMAND ----------

v_range = range(3,10)
print('Range values are generated : ',list(v_range))
print('v_range data type is : ', type(v_range))

# COMMAND ----------

list(range(-100, -95))

# COMMAND ----------

list(range(1, 20, 5))  # Increment by 5

# COMMAND ----------

x_range = range(50,150)
print(list(x_range))
print(type(x_range))

# COMMAND ----------

range_x=range(100,120)
print(list(range_x))

# COMMAND ----------

x = range(6)	#range	
print('Range Data Type : ',type(x))
print(x)
print(list(x))
y = range(1,10)
print(list(y))

# COMMAND ----------

# MAGIC %md
# MAGIC #### String Data Type
# MAGIC * Strings are amongst the most popular types in Python. We can create them simply by enclosing characters in quotes.
# MAGIC * Python treats single quotes the same as double quotes. 
# MAGIC * Creating strings is as simple as assigning a value to a variable

# COMMAND ----------

help(x)

# COMMAND ----------

y_str = 'this is lakshya sharma trying to learn python'
x = "Hello World"	#str
print('String Data Type: ',type(x))
print(x)
print(y_str)
print(type(y_str))

# COMMAND ----------

# MAGIC %md
# MAGIC #### Int Data Type
# MAGIC * They are positive or negative whole numbers with no decimal point. Integers in Python 3 are of unlimited size.

# COMMAND ----------

a=55
a
type(a)

# COMMAND ----------

x = 34	#int	
y = 534 #int
print('Int Data Type : ',type(x))
print(x)
print(type(y))

# COMMAND ----------

# MAGIC %md
# MAGIC #### Float Data Type
# MAGIC * they represent real numbers and are written with a decimal point dividing the integer and the fractional parts. 
# MAGIC * Floats may also be in scientific notation, with E or e indicating the power of 10 (2.5e2 = 2.5 x 102 = 250).

# COMMAND ----------

x = 20.2342	#float	
print('Float Data Type : ',type(x))
print(x)

# COMMAND ----------

# MAGIC %md
# MAGIC #### List
# MAGIC * List is a collection which is ordered and changeable. Allows duplicate members.
# MAGIC * In Python lists are written with square brackets.

# COMMAND ----------

bool_v =[1,2,3,"sfsdf",True,'sdfsd']
type(bool_v)

# COMMAND ----------

a = [1,0,"this is index 2",1,2,2,2,3,4,5,6,7,8,'String','NAme',44.33,True]
print(type(a))
print(a[2])

# COMMAND ----------

x = ["apple",23,2323,34.34, "banana", "cherry",11,22,11,22,1,1,2,2,2,3,3]	#list	
print(' List Data Type : ',type(x))
print(x[2])

# COMMAND ----------

num_list=[1,2,3,4,5,6,7,7,7,6,6,5,5,8,8,9,9,]
print(type(num_list))
print(num_list)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Tuple
# MAGIC * Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# MAGIC * In Python tuples are written with round brackets.
# MAGIC
# MAGIC

# COMMAND ----------

a_tuple=(1,2,3,4)
type(a_tuple)

# COMMAND ----------

x = ("apple", 12,1212,121.12,"banana", "cherry")	#tuple	
print('Tuple Data Type : ', type(x))
print(x[0])

# COMMAND ----------

num_tuple = (1,2,3,4,5,6,6,7,7,8,8,9,9,10)
print(type(num_tuple))
print(num_tuple)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Dictionary
# MAGIC * Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# MAGIC
# MAGIC * In Python dictionaries are written with curly brackets, and they have keys and values.
# MAGIC
# MAGIC

# COMMAND ----------

x = {"name" : "John", "age" : 36,"loc":"Bangalore"}	#dict	
print('Dictionary Data Type : ',type(x))
print(x['loc'])

# COMMAND ----------

a_set = set()


# COMMAND ----------

# MAGIC %md
# MAGIC #### Sets
# MAGIC * A set is a collection which is unordered and unindexed.  No duplicate members.
# MAGIC
# MAGIC * In Python, sets are written with curly brackets.
# MAGIC
# MAGIC

# COMMAND ----------

x = {"apple", "banana", "cherry","cherry"}	#set	
print('Set Data Type : ',type(x))
print(x)

# COMMAND ----------

a_set = {1,1,1,2,2,2,3,4,4,5,5,5,6,7,8,9}
a_set

# COMMAND ----------

# MAGIC %md
# MAGIC #### frozenset()
# MAGIC * The frozenset() is an inbuilt function is Python which takes an iterable object as input and makes them immutable. Simply it freezes the iterable objects and makes them unchangeable.
# MAGIC

# COMMAND ----------

x = frozenset({"apple", "banana", "cherry"})	#frozenset	
print('Frozenset Data Type : ',type(x))
print(x)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Bool
# MAGIC * The boolean data type is either True or False. In Python, boolean variables are defined by the True and False keywords.

# COMMAND ----------

a=False
b=True
print('variable a type is : ',type(a))
print('variable b type is : ',type(b))

# COMMAND ----------

num =0
bool(num)
# y or n  or True or False or 1 or 0 or active or inactive

# COMMAND ----------

x = False	#bool	
print('Bool Data Type : ',type(x))
print(x)

# COMMAND ----------

bool_f=False
print(type(bool_f))
print(bool_f)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Bytes
# MAGIC * Return a new "bytes" object, which is an immutable sequence of small integers in the range 0 <= x < 256, print as ASCII characters when displayed. bytes is an immutable version of bytearray – it has the same non-mutating methods and the same indexing and slicing behavior.

# COMMAND ----------

x = b"Hello"	#bytes	
print('Bytes Data Type : ',type(x))
print(x)

# COMMAND ----------

type(x)

# COMMAND ----------

# MAGIC %md
# MAGIC #### bytearray()
# MAGIC * bytearray() method returns a bytearray object which is an array of given bytes. It gives a mutable sequence of integers in the range 0 <= x < 256.
# MAGIC * The difference between bytes() and bytearray() is that bytes() returns an object that cannot be modified, and bytearray() returns an object that can be modified.
# MAGIC

# COMMAND ----------

# Converting inter into bytearray
x = bytearray([14]) 	#bytearray	
print('Byte Array Data Type : ',type(x))
print(x)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Memoryview()
# MAGIC * The memoryview() function returns a memory view object from a specified object.
# MAGIC * A memory view is a safe way to expose the buffer protocol in Python.
# MAGIC * It allows you to access the internal buffers of an object by creating a memory view object.

# COMMAND ----------

x = memoryview(bytes(5))	#memoryview
print('Memory View Data Type : ',type(x))
x = memoryview(b"Hello")
print(x)
#return the Unicode of the first character
print(x[0])
#return the Unicode of the second character
print(x[1])

# COMMAND ----------

type(x)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Complex integer data type
# MAGIC * Complex numbers have a real and imaginary part, which are each implemented using double in C. 
# MAGIC * To extract these parts from a complex number z, use z.real and z.imag.
# MAGIC
# MAGIC
# MAGIC * Returns a complex number constructed from arguments
# MAGIC * Complex numbers are specified as `<real part>+<imaginary part>j`.  
# MAGIC * J (or j) represents the square root of -1 (which is an imaginary number)
# MAGIC * Syntax `complex(re,im) ` a complex number with real part re, imaginary part im. im defaults to zero.	
# MAGIC * Complex numbers have a real and imaginary part, which are each implemented using double in C. To extract these parts from a complex number z, use z.real and z.imag.

# COMMAND ----------

x = 10+55j	#complex	(method or function )
print('Complex Data Type : ',type(x))
print(x) 
print('real value  : ' ,x.real)
print('image value : ',x.imag)

# COMMAND ----------

a = 6+4j
b = 3+2j
print("Below are the various functions we can use with complex numbers:")
print("1->Addition of two complex numbers:",a+b)
print("2->Addition of two complex numbers:",a-b)
print("3->Addition of two complex numbers:",a*b)
print("4->Addition of two complex numbers:",a/b)
#print("5->Addition of two complex numbers:",a//b) -->TypeError: can't take floor of complex number.
#print("6->Addition of two complex numbers:",a%b)--> TypeError: can't mod complex numbers.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ####  Date & Time Types
# MAGIC

# COMMAND ----------

import datetime
x = datetime.datetime.now()
print(x)
type(x)

# COMMAND ----------

help(x)

# COMMAND ----------

# MAGIC %md
# MAGIC #### strftime()
# MAGIC * The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:
# MAGIC
# MAGIC * Options
# MAGIC
# MAGIC %a	Weekday, short version	Wed	
# MAGIC %A	Weekday, full version	Wednesday	
# MAGIC %w	Weekday as a number 0-6, 0 is Sunday	3	
# MAGIC %d	Day of month 01-31	31	
# MAGIC %b	Month name, short version	Dec	
# MAGIC %B	Month name, full version	December	
# MAGIC %m	Month as a number 01-12	12	
# MAGIC %y	Year, short version, without century	18	
# MAGIC %Y	Year, full version	2018	
# MAGIC %H	Hour 00-23	17	
# MAGIC %I	Hour 00-12	05	
# MAGIC %p	AM/PM	PM	
# MAGIC %M	Minute 00-59	41	
# MAGIC %S	Second 00-59	08	
# MAGIC %f	Microsecond 000000-999999	548513	
# MAGIC %z	UTC offset	+0100	
# MAGIC %Z	Timezone	CST	
# MAGIC %j	Day number of year 001-366	365	
# MAGIC %U	Week number of year, Sunday as the first day of week, 00-53	52	
# MAGIC %W	Week number of year, Monday as the first day of week, 00-53	52	
# MAGIC %c	Local version of date and time	Mon Dec 31 17:41:00 2018	
# MAGIC %x	Local version of date	12/31/18	
# MAGIC %X	Local version of time	17:41:00	
# MAGIC %%	A % character	%

# COMMAND ----------



# COMMAND ----------

help(today_date)

# COMMAND ----------

help(today_date)

# COMMAND ----------

import datetime

today_date = datetime.datetime.now()

print('Date : ',today_date)
print('Year : ',today_date.year)
print('Month : ',today_date.month)
print('Day : ',today_date.day)
print(today_date.strftime("%A"))
print(today_date.strftime("%a"))
print(today_date.strftime("%B"))
print(today_date.strftime("%b"))
print(today_date.strftime("%H"))
print(today_date.strftime("%I"))

# COMMAND ----------

help(datetime)

# COMMAND ----------

import datetime

x = datetime.datetime(2020, 5, 17, 23, 23, 10)

print(x)

# COMMAND ----------

import time;      # This is required to include time module.

localtime = time.localtime(time.time())
print ("Local current time is :", localtime)
type(localtime)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Data Type Conversion
# MAGIC
# MAGIC * str() : Used to convert integer into a string.
# MAGIC * int(a,base) : This function converts any data type to integer. ‘Base’ specifies the base in which string is if data type is string.
# MAGIC * float() : This function is used to convert any data type to a floating point number
# MAGIC * ord() : This function is used to convert a character to integer.
# MAGIC * hex() : This function is to convert integer to hexadecimal string.
# MAGIC * oct() : This function is to convert integer to octal string.
# MAGIC * tuple() : This function is used to convert to a tuple.
# MAGIC * set() : This function returns the type after converting to set.
# MAGIC * list() : This function is used to convert any data type to a list type.
# MAGIC * dict() : This function is used to convert a tuple of order (key,value) into a dictionary.
# MAGIC * complex(real,imag) : : This function converts real numbers to complex(real,imag) number.
# MAGIC * chr(number) : : This function converts number to its corresponding ASCII character.
# MAGIC
# MAGIC
# MAGIC
# MAGIC

# COMMAND ----------

complex_num = 8+4j
complex_num1 =4+3j
print(complex_num-complex_num1)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Convert String To Bytes
# MAGIC

# COMMAND ----------

string = "This is sample String."
# string with encoding 'utf-8'
bytes = bytes(string, 'utf-8')
print(bytes)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Convert int to bytes ..

# COMMAND ----------

#int
#str

# COMMAND ----------

a=10
b='88'
print(a+int(b))

# COMMAND ----------

a=10
b='88'
print(a+int(b))

# COMMAND ----------

c=str(a)+b
print(c)

# COMMAND ----------

#create a variable with integer value.
a=100
print("The type of variable having value", a, " is ", type(a))
#create a variable with float value.
b=10.2345
print("The type of variable having value", b, " is ", type(b))
#create a variable with complex value. (real part + img part)
c=100+3j
print("The type of variable having value", c, " is ", type(c))

# COMMAND ----------

v1 = int(2.7) # 2
v2 = int(-3.9) # -3
v3 = int("2") # 2
v4 = int("11", 16) # 17, base 16
v6 = float(2) # 2.0
v7 = float("2.7") # 2.7
v8 = float("2.7E-2") # 0.027
v9 = float(False) # 0.0
vA = float(True) # 1.0
vB = str(4.5) # "4.5"
vC = str([1, 3, 5]) # "[1, 3, 5]"
vD = bool(0) # False; bool fn since Python 2.2.1
vE = bool(3) # True
vF = bool([]) # False - empty list
vG = bool([False]) # True - non-empty list
vH = bool({}) # False - empty dict; same for empty tuple
vI = bool("") # False - empty string
vJ = bool(" ") # True - non-empty string
vK = bool(None) # False
vL = bool(len) # True
vM = set([1, 2])
vN = list(vM)
vO = list({1: "a", 2: "b"}) # dict -> list of keys
vP = tuple(vN)
vQ = list("abc") # ['a', 'b', 'c']


# COMMAND ----------

# MAGIC %md
# MAGIC #### sys.getsizeof()
# MAGIC * Return the size of an object in bytes. The object can be any type of object. 
# MAGIC * All built-in objects will return correct results, but this does not have to hold true for third-party extensions as it is implementation specific.

# COMMAND ----------

import sys
a='this is no data'
sys.getsizeof(a)

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Program to print ASCII Value of a character
# MAGIC * ord() : It coverts the given string of length one, return an integer representing the unicode code point of the character. 
# MAGIC * For example, ord(‘a’) returns the integer 97.

# COMMAND ----------

char='!'
print("The ASCII value of ",char," is : ",ord(char))
char='*'
print("The ASCII value of ",char," is : ",ord(char))
char='%'
print("The ASCII value of ",char," is : ",ord(char))
char='$'
print("The ASCII value of ",char," is : ",ord(char))
char='&'
print("The ASCII value of ",char," is : ",ord(char))
char='-'
print("The ASCII value of ",char," is : ",ord(char))
char='='
print("The ASCII value of ",char," is : ",ord(char))