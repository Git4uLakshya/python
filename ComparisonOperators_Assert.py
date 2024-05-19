# Databricks notebook source
# MAGIC %md
# MAGIC # Comparison Operators 
# MAGIC
# MAGIC In this lecture we will be learning about Comparison Operators in Python. These operators will allow us to compare variables and output a Boolean value (True or False). 
# MAGIC
# MAGIC If you have any sort of background in Math, these operators should be very straight forward.
# MAGIC
# MAGIC First we'll present a table of the comparison operators and then work through some examples:
# MAGIC
# MAGIC <h2> Table of Comparison Operators </h2><p>  In the table below, a=3 and b=4.</p>
# MAGIC
# MAGIC <table class="table table-bordered">
# MAGIC <tr>
# MAGIC <th style="width:10%">Operator</th><th style="width:45%">Description</th><th>Example</th>
# MAGIC </tr>
# MAGIC <tr>
# MAGIC <td>==</td>
# MAGIC <td>If the values of two operands are equal, then the condition becomes true.</td>
# MAGIC <td> (a == b) is not true.</td>
# MAGIC </tr>
# MAGIC <tr>
# MAGIC <td>!=</td>
# MAGIC <td>If values of two operands are not equal, then condition becomes true.</td>
# MAGIC <td>(a != b) is true</td>
# MAGIC </tr>
# MAGIC <tr>
# MAGIC <td>&gt;</td>
# MAGIC <td>If the value of left operand is greater than the value of right operand, then condition becomes true.</td>
# MAGIC <td> (a &gt; b) is not true.</td>
# MAGIC </tr>
# MAGIC <tr>
# MAGIC <td>&lt;</td>
# MAGIC <td>If the value of left operand is less than the value of right operand, then condition becomes true.</td>
# MAGIC <td> (a &lt; b) is true.</td>
# MAGIC </tr>
# MAGIC <tr>
# MAGIC <td>&gt;=</td>
# MAGIC <td>If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.</td>
# MAGIC <td> (a &gt;= b) is not true. </td>
# MAGIC </tr>
# MAGIC <tr>
# MAGIC <td>&lt;=</td>
# MAGIC <td>If the value of left operand is less than or equal to the value of right operand, then condition becomes true.</td>
# MAGIC <td> (a &lt;= b) is true. </td>
# MAGIC </tr>
# MAGIC </table>

# COMMAND ----------

# MAGIC %md
# MAGIC Let's now work through quick examples of each of these.
# MAGIC
# MAGIC #### Equal

# COMMAND ----------

33 == 33

# COMMAND ----------

33 == 44

# COMMAND ----------

# MAGIC %md
# MAGIC Note that <code>==</code> is a <em>comparison</em> operator, while <code>=</code> is an <em>assignment</em> operator.

# COMMAND ----------

# MAGIC %md
# MAGIC #### Not Equal

# COMMAND ----------

10 != 20

# COMMAND ----------

40 != 40

# COMMAND ----------

# MAGIC %md
# MAGIC #### Greater Than

# COMMAND ----------

44 > 22

# COMMAND ----------

33 > 11

# COMMAND ----------

# MAGIC %md
# MAGIC #### Less Than

# COMMAND ----------

21 < 41

# COMMAND ----------

23 < 13

# COMMAND ----------

# MAGIC %md
# MAGIC #### Greater Than or Equal to

# COMMAND ----------

24 >= 24

# COMMAND ----------

23 >= 12

# COMMAND ----------

# MAGIC %md
# MAGIC #### Less than or Equal to

# COMMAND ----------

23 <= 23

# COMMAND ----------

21 <= 41

# COMMAND ----------

# MAGIC %md
# MAGIC #### Python Logical Operators
# MAGIC |Operator|	Description	| Examples
# MAGIC |----|-----|----
# MAGIC |__and__ 	|Returns True if both statements are true	|x < 5 and  x < 10	
# MAGIC |__or__	|Returns True if one of the statements is true	|x < 5 or x < 4	
# MAGIC |__not__	|Reverse the result, returns False if the result is true	|not(x < 5 and x < 10)	
# MAGIC

# COMMAND ----------

10<20 and 20<30


# COMMAND ----------

10 < 30 > 20


# COMMAND ----------

print(10<30 and 30>20)
print(not(10<30 and 30>20))


# COMMAND ----------

# MAGIC %md
# MAGIC It's important to note that Python is checking both instances of the comparisons. We can also use or to write comparisons in Python. For example:
# MAGIC
# MAGIC

# COMMAND ----------

11==11 or 111==11


# COMMAND ----------

11==22 or 22<33


# COMMAND ----------

# MAGIC %md
# MAGIC #### enumerate
# MAGIC * enumerate is a very useful function to use with for loops
# MAGIC * Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object. 
# MAGIC * This enumerate object can then be used directly in for loops or be converted into a list of tuples using list() method.

# COMMAND ----------

for i,letter in enumerate('pyspark'):
    print("At index {} the letter is {}".format(i,letter))

# COMMAND ----------

# MAGIC %md
# MAGIC #### zip()
# MAGIC * The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together

# COMMAND ----------

list_a = [1,2,3,4,5]
list_b = [3,4,5,6,7,8,9,10]

x = zip(list_a, list_b)  # its create zip object.
print(list(x))

# COMMAND ----------

# MAGIC %md
# MAGIC #### min() and max() Functions
# MAGIC * Quickly check the minimum or maximum of a list with these functions

# COMMAND ----------

list_a = [1,2,3,4,5]
print('min value : ',min(list_a))
print('max value : ',max(list_a))

# COMMAND ----------

# MAGIC %md
# MAGIC #### isinstance(object,type)
# MAGIC * The isinstance() function returns True if the specified object is of the specified type, otherwise False. 

# COMMAND ----------

test = isinstance(5, int)
print(test)
print(isinstance("test",str))

# COMMAND ----------

# MAGIC %md
# MAGIC #### reversed(list)
# MAGIC * The reversed() function returns a reversed iterator object.

# COMMAND ----------

list = ["a", "b", "c", "d"]
result = reversed(list)
for x in result:
  print(x)

# COMMAND ----------

# MAGIC %md
# MAGIC #### sorted(list)
# MAGIC * The sorted() function returns a sorted list of the specified iterable object.
# MAGIC * `sorted(iterable, key=key, reverse=reverse)
# MAGIC `
# MAGIC

# COMMAND ----------

a = ("b", "g", "a", "d", "f", "c", "h", "e")
x = sorted(a)
print(x)

# COMMAND ----------

a = ("b", "g", "a", "d", "f", "c", "h", "e")
x = sorted(a,reverse=True)
print(x)

# COMMAND ----------

# MAGIC %md
# MAGIC ##### globals()
# MAGIC * The globals() function returns the global symbol table as a dictionary - key value pair data of all objects
# MAGIC *  Python interpreter maintains a data structure containing information about each identifier appearing in the program's source code. This information is about the type, value, scope level, and location of an identifier (also called symbol)

# COMMAND ----------

var = globals()
print(var)

# COMMAND ----------

# MAGIC %md
# MAGIC #### locals()
# MAGIC * locals() returns the global and local symbols table respectively. Python interpreter maintains a data structure containing information about each identifier appearing in the program's source code. This information is about the type, value, scope level, and location of an identifier (also called symbol)

# COMMAND ----------

loc = locals()
print(loc)

# COMMAND ----------

def sum(x,y):
        z=x+y
        print ('global symbol list:', globals())
        print ('local symbol list:', locals())
        return z
sum(1,2)

# COMMAND ----------

# MAGIC %md
# MAGIC #### len()
# MAGIC * len() function will give length of object or no of items in object

# COMMAND ----------

list_a = [1,2,3,4,5]
print('no of items : ',len(list_a)) 

# COMMAND ----------

# MAGIC %md
# MAGIC #### random
# MAGIC * Python comes with a built in random library. There are a lot of functions included in this random library, so we will only show you two useful functions for now.

# COMMAND ----------

from random import shuffle
list_a = [1,2,3,4,5]
shuffle(list_a)
list_a

# COMMAND ----------

from random import randint
# Return random integer in range [a, b], including both end points.
randint(0,100)

# COMMAND ----------

# MAGIC %md
# MAGIC #### split()

# COMMAND ----------

string = "this is sample string which i can split into words based on space"
output = string.split(" ")
output

# COMMAND ----------

# MAGIC %md
# MAGIC #### upper()
# MAGIC * Converting string into upper case using `upper()` function

# COMMAND ----------

string = "pyspark training"
output = string.upper()
output

# COMMAND ----------

# MAGIC %md
# MAGIC #### lower()
# MAGIC * Converting string into lower case using `lower()` funciton

# COMMAND ----------

string = "PYSPARK TraiNiNG"
output = string.lower()
output

# COMMAND ----------

# MAGIC %md
# MAGIC #### replace(from,to)
# MAGIC * replace character by character using `replace()` function

# COMMAND ----------

string = "DATABRICKS TRAINING"

string = string.replace('S','SSSS').replace("B","BBBB")
string


# COMMAND ----------

# MAGIC %md
# MAGIC #### strip()
# MAGIC * __`strip()`__ - Remove white spaces at the beginning and at the end of the string

# COMMAND ----------

string ="  pyspark  "
output = string.strip()
print('before strip : ',string)
print('after strip : ',output)

# COMMAND ----------

# MAGIC %md
# MAGIC #### capitalize()
# MAGIC * the capitalize() method returns a copy of the original string and converts the first character of the string to a capital (uppercase) letter while making all other characters in the string lowercase

# COMMAND ----------

string= "pyspark training"
output = string.split(" ")
for i in output:
  i = i.capitalize()
  print(i)

# COMMAND ----------

# MAGIC %md
# MAGIC #### filter(func,data) 
# MAGIC * filtering data using filter function

# COMMAND ----------

def func_odd(num):
    if num%2 ==0:
        return True

# COMMAND ----------

data =range(20)
#Named python function with filter
print(list(filter(func_odd,data)))
# Lambda function with filer
print(list(filter(lambda a: a%2==0,data)))

# COMMAND ----------

# MAGIC %md
# MAGIC #### reduce(func,list)

# COMMAND ----------

from functools import reduce
data =[1,2,3,4,5,6,7,8,9,10]
reduce(lambda x,y: x+y,data)

# COMMAND ----------

# MAGIC %md
# MAGIC #### what is recursion?
# MAGIC * Recursion is the process of defining something in terms of itself.
# MAGIC * In Python, we know that a function can call other functions. It is even possible for the function to call itself. 
# MAGIC * These types of construct are termed as recursive functions.

# COMMAND ----------

def sum_recursion(arr):
    
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum_recursion(arr[1:])
      
list=[1,2,3,4,5,6]
sum_recursion(list)

# COMMAND ----------

b=' '
str="databricks training"
str[-1]

# COMMAND ----------

def reverse_string(str):
    """
    Reverse a String using [:-1]
    """
    if len(str) <= 1:
        return str
    else:
        return str[-1] + reverse_string(str[:-1])
reverse_string("databricks training")

# COMMAND ----------

# MAGIC %md
# MAGIC ##### isupper() and islower()
# MAGIC * validating upper and lower case string using `isupper() and islower() ` functions and it will return `true` or `false`

# COMMAND ----------

string ="pyspark"
if string.isupper():
  print('its upper case')
elif string.islower():
  print('its lower case')
else:
  print('its mixed case')

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC #### List Comprehensions
# MAGIC * In addition to sequence operations and list methods, Python includes a more advanced operation called a list comprehension.
# MAGIC * __`List comprehensions`__ allow us to build out lists using a different notation. 
# MAGIC * You can think of it as essentially a one line for loop built inside of brackets. 

# COMMAND ----------

# Square numbers in range and turn into list
Square = [x**2 for x in range(0,11)]
Square

# COMMAND ----------

# Check for even numbers in a range
even = [x for x in range(11) if x % 2 == 0]
even

# COMMAND ----------

# Check for odd numbers in a range
odd = [x for x in range(20) if x % 2 == 1 ]
odd

# COMMAND ----------

lst = [ x**2 for x in [x**2 for x in range(11)]]
lst

# COMMAND ----------

# MAGIC %md
# MAGIC #### assert

# COMMAND ----------

a=5
b=5
assert (a==b),"Condition matching. A and B values are same"

# COMMAND ----------

a=5
a=7
assert (a==b),"A and B is not matching"