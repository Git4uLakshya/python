# Databricks notebook source
# MAGIC %md
# MAGIC ## Exception and Error Handling
# MAGIC * Until now error messages haven’t been more than mentioned, but if you have tried out the examples you have probably seen some. 
# MAGIC * There are (at least) two distinguishable kinds of errors: syntax errors and exceptions.
# MAGIC
# MAGIC ### Exceptions
# MAGIC * Even if a statement or expression is syntactically correct, it may cause an error when an attempt is made to execute it. 
# MAGIC * Errors detected during execution are called exceptions and are not unconditionally fatal: 
# MAGIC * you will soon learn how to handle them in Python programs. 
# MAGIC * Most exceptions are not handled by programs, however, and result in error messages as shown here

# COMMAND ----------

a=5
b=0
# data level
# code level
# system level
print('a data type is : ',type(a))
print('b data type is : ',type(b))
print(a/b)


# COMMAND ----------

# MAGIC %md
# MAGIC ### Handling Exceptions
# MAGIC * It is possible to write programs that handle selected exceptions. 

# COMMAND ----------

# MAGIC %md
# MAGIC #### Try Block 
# MAGIC * - here we can write our code - main execution code we can write in try block
# MAGIC #### Exception Block
# MAGIC * - here we can handle whichever excpetion or error thorowing by try block

# COMMAND ----------



# COMMAND ----------

a=55
b=0
try:
  c=a/b
  print(c)
except Exception as e:
  print(e)


# COMMAND ----------

a = 4
b = 4
try : 
    c = a+b
    print('Try Block c value is  : ' ,c)
except Exception as e:
    
    print("Exception error message: => ",e) 
    print(Exception)
    print(e)

# COMMAND ----------

# MAGIC %md
# MAGIC * Multiple Exception handling

# COMMAND ----------

def divbyzero(x,y):
    try:
        return x/y
    except Exception as e:
        print('Exception raised - Please verify : ',e)
divbyzero(5,0)


# COMMAND ----------

divbyzero(5,0)

# COMMAND ----------

def divbyzero(x,y):
    try:
        return x/y
    except ZeroDivisionError as e:
        print('ZeroDivisionError and error message :',e)
    except Exception as e:
        print('Others Exception  error message : ',e)
divbyzero(5,0)

# COMMAND ----------

locals()['__builins__']

# COMMAND ----------

list_a=[1,2,3,4]
list_a[10]

# COMMAND ----------

#Calling function with second argument with zero (0)
divbyzero(10,'1')

# COMMAND ----------

divbyzero(10,0)

# COMMAND ----------

def int_func(x,y):
    z = 0
    try: 
        z = x + y
        
    except:
        print('Please input only integer or float value')
        
    return z



# COMMAND ----------

int_func(1,'4')

# COMMAND ----------

a = 33
b = 78
a_list = [1,1,2,3]
try : 
    c = a/b
    e = a_list[0]
    print(e)
except ZeroDivisionError:
    print("Handled ZeroDivisionError")
    
else:
    print('this is else block : ',c)



# COMMAND ----------

a = 44
b = 1
d = [1,2,3,4]
try : 
    c = a/b
    print('result for division is',a
    e = d[9]
    print('Try Block ',e)
    
except ZeroDivisionError as e:
    print("Execution is caught ZeroDivisionError : ",e)
except IndexError as e:
    print("Exception is caught is list index out of range : ",e)
    
else:# only if Try block is True this will be executed.
    print('Else Block : ',c)
    print('Else Block : ',e)
    

# COMMAND ----------

a = 66
b = 33
d = []
try : 
    
    c = a/b
    e = d[5]
except:
    print('Exception is caught')
else:
    print(c)
    


# COMMAND ----------

a = 44
b = 66
d = []
try : 
    c = a/b
    e = d[5]
    print(e)
except Exception as e:
    print("Exception Error Message :  " +str(e))
    # email alert
    # inserting into error table
    # inserting into error log file
    
    
else:
    print(c)
print("Good Tracking")


# COMMAND ----------

a = 88
b = 0
d = [1,2,3,4,5]
try : 
    c = a/b
    e = d[0]
    print('Try Blob list index zero value :',e)

except ZeroDivisionError: # this block will be executed only if Try block is returning False
    print("Handle ZeroDivisionError") 
except Exception as e: # this block will be executed only if Try block is returning False
  print("others ")
    
else: # this block will be executed only if Try block is returning True
    print('Else Blob c value ' ,c)
    
finally: # if Try block is returning True or False 
    print("Finally will always exuted if we get any exception or not")

# COMMAND ----------

# MAGIC %md
# MAGIC #### Exception Handling with `ELSE`

# COMMAND ----------

a = 88
b = 0
d = [1,2,3,4,5,6,6]
try : 
    c = a/b
    e = d[5]
    print('inside Try Block : ',c)
except ZeroDivisionError:
    print("Handle ZeroDivisionError")
except IndexError:
    print("Exception is caught is list index out of range")
else:
    print('in else block :' ,c)
finally:
    print("Finally will always exuted if we get any exception or not")

# COMMAND ----------

class Student():
    def __init__(self,name,age):
        if age > 80 or age <16:
            raise Exception("Age can not be greater than 80 or less than 16")
        self.name = name
        self.age = age
        
class StudentAgeException(Exception):
    pass
        

# COMMAND ----------

age = 44
st = Student("Hello", age)
print(st.age)


# COMMAND ----------

try:
     raise NameError('HiThere')
except NameError:
     print('Manually Excpetion raised by using raise ')

# COMMAND ----------

import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

# COMMAND ----------

import sys
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

# COMMAND ----------

# MAGIC %md
# MAGIC ### File Handling
# MAGIC ### Reading and Writing Files
# MAGIC * `open()` returns a file object, and is most commonly used with two arguments: `open(filename, mode)`.
# MAGIC ### Write to an Existing File
# MAGIC * To write to an existing file, you must add a parameter to the open() function:
# MAGIC
# MAGIC * "a" - Append - will append to the end of the file
# MAGIC
# MAGIC * "w" - Write - will overwrite any existing content
# MAGIC
# MAGIC * "r" - Read - Reading data from existing file

# COMMAND ----------

x = "This is a  new text message"
with open ("/tmp/abc.txt", "a") as file:
    file.write(x+"\n")
    file.write(x+"\n")
    file.write(x)
    file.close()
    

# COMMAND ----------

dbutils.fs.mv("file:/tmp/abc.txt","dbfs:/tmp/abc.txt")

# COMMAND ----------

dbutils.fs.head("dbfs:/tmp/abc.txt")

# COMMAND ----------

# MAGIC %md
# MAGIC ### Open And Reading a File
# MAGIC * To open the file, use the built-in open() function.
# MAGIC
# MAGIC * The open() function returns a file object, which has a read() method for reading the content of the file:

# COMMAND ----------

with open ("/tmp/abc.txt", "w") as file:
    content=file.write("this is sample data \n")
    print(content)

# COMMAND ----------

with open("/tmp/abc.txt","r") as rfile:
  data = rfile.read()
  print(data)

# COMMAND ----------

x = "This is a  sample message"
with open ("abc.txt", "a") as file:
    file.write(x+"\n")

# COMMAND ----------

with open ("abc.txt", "r") as file:
    content=file.read()
    print(content)

# COMMAND ----------

filename='ravi.txt'

try:
    with open(filename) as file_object:
        contents=file_object.read()
        print(contents)
except FileNotFoundError:
    print(f"sorry ,the file {filename} does not exist")

# COMMAND ----------

filename='abcs.txt'

try:
    with open(filename) as file_object:
        contents=file_object.read()
        print(contents)
except FileNotFoundError:
    print(f"sorry ,the file {filename} does not exist")

# COMMAND ----------

locals()[]

# COMMAND ----------

def divide_numbers(a, b):
    try:
        result = a / b
        print(f"The result of {a} / {b} is {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Invalid data types for division.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print("Division completed successfully.")
    finally:
        print("Division operation finished.")

# Example usage:
divide_numbers(10, 2)       # This will print: "The result of 10 / 2 is 5.0\nDivision completed successfully.\nDivision operation finished."
divide_numbers(5, 0)        # This will print: "Error: Cannot divide by zero.\nDivision operation finished."
divide_numbers(10, "abc")   # This will print: "Error: Invalid data types for division.\nDivision operation finished."
divide_numbers(10, [])      # This will print: "An unexpected error occurred: unsupported operand type(s) for /: 'int' and 'list'\nDivision operation finished."


# COMMAND ----------

