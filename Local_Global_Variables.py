# Databricks notebook source
# MAGIC %md
# MAGIC #### Local Vs Global Variables
# MAGIC * if we want to change the Global Variable value inside functions Use `GLOBAL` Keyword..

# COMMAND ----------

age=55
print(age)

# COMMAND ----------

def func():
  global age
  age=45
  print('My Age is : ',age)

# COMMAND ----------

func()
print(age)

# COMMAND ----------

y = 55
print('first value :',y)
y=66
print('Updated value : ',y)
def func():
  y=100
  print('inside function Y variable value is : ',y)
func()
print('after function out side Y value is : ',y)

# COMMAND ----------

print('Before calling a function y value is : ',y)
func()
print('after execution a function y value is : ',y)

# COMMAND ----------

def myfunc():  
  global y
  y = 77
  print('Inside Function x Variable value is : ',y)


# COMMAND ----------

myfunc()
## Verifying y variable value is updated or not.


# COMMAND ----------

print(y)
## Still its not updated.

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Chaning the Variable Scope from Local To Global Using `GLOBAL` keyword.

# COMMAND ----------

x = "Global  Variable"
print('Before Updating Global Variable :',x)

def myfunc():  
  global x
  x = "Local  Variable"
  print('Inside Function x Variable value is : ',x)

myfunc()

print("After Updating Global Variable : ",x)

# COMMAND ----------

myfunc()

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Using `GLOBAL` keyword to changing value

# COMMAND ----------

x = "Global Variable"

print('Before Updating Global Variable :',x)
def myfunc():
  global x
  x = "Local  Variable"
  print('inside function X variable value : ',x)

myfunc()

print("After Updating Global Variable : ",x)

# COMMAND ----------

print(x)

# COMMAND ----------

x='this is sample text variable'
print(x)

# COMMAND ----------

x=44
print(x)

# COMMAND ----------

print(age)