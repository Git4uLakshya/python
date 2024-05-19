# Databricks notebook source
# MAGIC %md
# MAGIC ####  Function
# MAGIC * The keyword def introduces a function definition. 
# MAGIC * It must be followed by the function name and the parenthesized list of formal parameters. 
# MAGIC * The statements that form the body of the function start at the next line, and must be indented.
# MAGIC * A function is a block of code which only runs when it is called.
# MAGIC
# MAGIC * You can pass data, known as parameters, into a function.
# MAGIC
# MAGIC * A function can return data as a result.

# COMMAND ----------

#UN-Named statemetns
def named_state(a,b):
  print("Hello from a function")
  print("Statement two")
  print("Statement Three")
  return a+b
named_state(5,6)

# COMMAND ----------

def add(a,b):
  return a+b

add(1,2)

# COMMAND ----------

lambda_ref = lambda a,b : a+b

# COMMAND ----------

lambda_ref(1,2)

# COMMAND ----------

named_state(4,5)

# COMMAND ----------

def add_values(a,b=12):
  print('A Value is : ',a)
  print('B Value is :',b)
  c = a+b
  print('C value is : ',c)
  return c

# COMMAND ----------

add_values(10,40)

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Creating Function

# COMMAND ----------

#Creating Function
def my_func():
  print("Hello from a function")
  print("Statement two")
  print("Statement Three")
#Calling or Executing function
my_func()

# COMMAND ----------



# COMMAND ----------

#Creating a function with two arguments  a and b
def my_sum(a,b):
  print('Sum of a and b value is : ',a+b)
  return a+b
#calling or executing a function
my_sum(90,20)

# COMMAND ----------



# COMMAND ----------

my_func()

# COMMAND ----------

total_value =add_value(5,6)
print(total_value)

# COMMAND ----------

def my_sum(a,b):
  print('A value is : ',a)
  print('B value is : ',b)

# COMMAND ----------

my_sum(5,4)

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Calling Or Executing Funciton

# COMMAND ----------

my_func()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Arguments (parameters)
# MAGIC * Information can be passed into functions as arguments.
# MAGIC
# MAGIC #### Function arguments: positional, keyword
# MAGIC
# MAGIC * A function is most useful when arguments are passed to the function. 
# MAGIC * New values for times are processed inside the function. 
# MAGIC * This function is also a ``'positional' argument, vs a keyword` argument. 
# MAGIC * Positional arguments are processed in the order they are created in.

# COMMAND ----------

def my_func(fname,age):
  print("My Name is : ",fname)
  print("MY Age is : ",age)
my_func(23,'lak')

# COMMAND ----------

# MAGIC %md
# MAGIC ### Positional Arguments are processed in order
# MAGIC

# COMMAND ----------

#Positional Arguments are processed in order
def my_fc(fname,age):
  print("My Name is : ",fname)
  print("MY Age is : ",age)
my_fc(age=305,fname="Raveendra")

# COMMAND ----------

# MAGIC %md
# MAGIC #### Keyword Arguments are processed by key, value and can have default values
# MAGIC * You can also send arguments with the key = value syntax.
# MAGIC * One handy feature of keyword arguments is that you can set defaults and only change the defaults you want to change.
# MAGIC

# COMMAND ----------

my_func(age=55,fname="Rajkumar")
# optional

# COMMAND ----------

my_func(age=55,fname="Eswar")

# COMMAND ----------

def addition(a,b):
   print(f" Sum Of {a} + {b}  is  {a+b}")

# COMMAND ----------

addition(10,20)

# COMMAND ----------

def my_function(child1, child2, child3):
  print("The youngest child is " + child1)
  print("The youngest child is " + child2)
  print("The youngest child is " + child3)

# COMMAND ----------

my_function(child2="param1",child3="param2",child1="param3")

# COMMAND ----------

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


# COMMAND ----------

def check_even_list(num_list):
    # Go through each number
    # Declare empty list
    even=[]
    for number in num_list:
        # Once we get a "hit" on an even number, we return True
        if number % 2 == 0:
          # append if number is even number using append method
          even.append(number)
             
        # Don't do anything if its not even
        else:
            pass
    # Notice the indentation! This ensures we run through the entire for loop    
    return even
  
check_even_list([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])

# COMMAND ----------

def check_odd_list(num_list):
    # Go through each number
    # Declare empty list
    odd=[]
    for number in num_list:
        # Once we get a "hit" on an even number, we return True
        if number % 2 == 1:
          # append number if its odd number
          odd.append(number)
             
        # Don't do anything if its not even
        else:
            pass
    # Notice the indentation! This ensures we run through the entire for loop    
    return odd
  
check_odd_list([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Default Parameter Value
# MAGIC * The following example shows how to use a default parameter value.
# MAGIC
# MAGIC * If we call the function without argument, it uses the default value:

# COMMAND ----------

def my_function(name,age,loc = "India"):
  print("My Name is  : ",name)
  print("My Age is : ",age)
  print("I am from : ",loc)
# Calling a function without 3rd argument. it will considar default value.
my_function("Ravi",33)

# COMMAND ----------

my_function("Ravi",33,'Chennai')

# COMMAND ----------


my_function("Sweden")
my_function("US")
my_function()
my_function("Brazil")

# COMMAND ----------

def squareroot(x):
  return x * x


# COMMAND ----------

squareroot(100)

# COMMAND ----------

print(squareroot(3))
print(squareroot(5))

# COMMAND ----------

# MAGIC %md
# MAGIC #### Variable Number of Arguments   (`*args`)
# MAGIC * In cases where you don’t know the exact number of arguments that you want to pass to a function, 
# MAGIC * you can use the following syntax with *args:

# COMMAND ----------

def my_sum(*args):
   return sum(args)
my_sum(1,2,3,4,5,6,9)

# COMMAND ----------

my_sum(1,2,3,4,5,6,9)

# COMMAND ----------

def key_value_pair(**kvargs):
  print("key value pair data : ",kvargs)
  

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC ### Nested functions

# COMMAND ----------

def func_outside():
  x= 'outside'
  print(x)
  def func_inside():  # Local objects 
    x='inside'
    print(x)  
  func_inside()
func_outside()

# COMMAND ----------

func_outside()

# COMMAND ----------

func_inside()

# COMMAND ----------

def function1(): # outer function
    x = 2 # A variable defined within the outer function
    print('x value is before updating : ',x)
    x = 8
    print('x value is after update ',x)    
    def function2(a): # inner function
       # Let's define a new variable within the inner function
       # rather than changing the value of x of the outer function
        x = 10
        print('inner function x value is : ',x)
        print ('Inner Function Value : ',a+x)
        return x
    print('Before executing func x : ' ,x)
    y=function2(3)
    print('inner function x value is : ',y)
    print ('after executing Func x : ',x) 
    # to display the value of x of the outer function
function1()

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC ##### The pass Statement
# MAGIC * function definitions cannot be empty, but if you for some reason have a function definition with no content, 
# MAGIC * put in the pass statement to avoid getting an error.

# COMMAND ----------

def func():
  pass

# COMMAND ----------

func()

# COMMAND ----------

named_state