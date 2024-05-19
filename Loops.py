# Databricks notebook source
# MAGIC %md #### Python Loops
# MAGIC * The two types of loops discussed were for loops and while loops. for loops and while loops are two repetion structures in Python.
# MAGIC
# MAGIC * __for loop__
# MAGIC * __while loop__

# COMMAND ----------

# MAGIC %md For Loops with range()
# MAGIC * Another method to print the same statement three times is to use a for loop. 
# MAGIC * A for loop is a programming structure where a user-defined block of code runs a specified number of times. 
# MAGIC * The basic structure of a for loop in Python is below:
# MAGIC
# MAGIC
# MAGIC `for var in range(num):`
# MAGIC
# MAGIC     `code`

# COMMAND ----------

v_rage = range(1,100+1) # range MAX value (N-1)
var='PythonTraining '
for v in v_rage:
  print(v)

# COMMAND ----------

a="this is sample string"
for x in range(1,100,5):
  print('for loop',x)

# COMMAND ----------

for i in range(5):
  print(i)

# COMMAND ----------

a_list=[1,2,3,4,5,6,22,7,8,8,9,0,23]
a_list

# COMMAND ----------

for v in a_list:
  print(v*10)

# COMMAND ----------

for j in range(10,21):
  print(j)

# COMMAND ----------

for i in [5]:
  print('list of sequence values using Range : ',i)

# COMMAND ----------

for v in [1,2,3,4,5,6,6,7,8,8,9]:
  print('this is list of numbers ',v)

# COMMAND ----------

for i in ['Eswar']:
  print('My Name is : ',i)

# COMMAND ----------

# MAGIC %md 
# MAGIC * For loops with lists
# MAGIC * For loops can also be run using Python lists. 
# MAGIC * If a list is used, the loop will run as many times as there are items in the list. 
# MAGIC * The general structure is:
# MAGIC
# MAGIC `for <var> in <list>:`
# MAGIC
# MAGIC     `   <statements>`

# COMMAND ----------

my_list = ['raj','prasad','mahesh','sridhar']
for item in my_list:
    print('My Name is : ',item)

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Loooping Through a string value and reading each character by character

# COMMAND ----------

for x in "apple":
  print('BAnana Characters Are : ',x)

# COMMAND ----------

fruits = ["apple", "banana", "cherry","orange","mangao","kiwi"]

fruits.insert(10,"test1")
print(fruits.index("test1"))


# COMMAND ----------

# MAGIC %md
# MAGIC ##### The break Statement
# MAGIC * With the break statement we can stop the loop before it has looped through all the items:

# COMMAND ----------

# Stopping entire loop - BREAK
# stopping only current iteration ( 10 values - 10 iterations)

# COMMAND ----------

fruits = ["apple", "banana", "cherry","orange","mango","kiwi"]
for x in fruits:  
  
  if x == "orange":
    continue
  print(x)

# COMMAND ----------

# MAGIC %md
# MAGIC #### The continue Statement
# MAGIC * With the continue statement we can stop the current iteration of the loop, and continue with the next:

# COMMAND ----------

for i in range(60):
  if i  in [50,3,11,20]:
    continue
  print(i)
  

# COMMAND ----------

fruits = ["apple", "banana", "cherry","orange","mango","kiwi"]
for x in fruits:  
  if x == "orange":
    continue  
  print(x)

# COMMAND ----------

fruits = ["apple", "banana", "cherry","orange","mango"]
for x in fruits:
  if x in ("banana","cherry"):
    print('Inside If Condition',x)
    continue 
  print('Out side if condition ',x) 

# COMMAND ----------

# MAGIC %md #### The while Loop
# MAGIC * With the while loop we can execute a set of statements as long as a condition is true.
# MAGIC * syntax: `while condition:`
# MAGIC              `statements `

# COMMAND ----------

#Print i as long as i is less than 10 with increment by 2 
i = 0
while i < 10:
  print(i)
  i +=2

# COMMAND ----------

# MAGIC %md
# MAGIC ##### The break Statement
# MAGIC * With the break statement we can stop the loop even if the while condition is true:

# COMMAND ----------

i = 0
while i < 10:
  
  i +=1  
  if i==6 :
    break    
    
  print(i)
  
  

# COMMAND ----------

a

# COMMAND ----------

i=10
while i>3:
  print(i)
  if i ==6:
    break
  i -=1

# COMMAND ----------

# MAGIC %md
# MAGIC ##### The continue Statement
# MAGIC * With the continue statement we can stop the current iteration, and continue with the next

# COMMAND ----------

i = 0
while i < 8:
  i += 1
  if i == 5:
    continue
  print(i)

# COMMAND ----------

# MAGIC %md
# MAGIC ##### The else Statement
# MAGIC * With the else statement we can run a block of code once when the condition no longer is true

# COMMAND ----------

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

# COMMAND ----------

# MAGIC %md
# MAGIC ### Creating list using `For Loop` And `Range()`

# COMMAND ----------

my_list = [x for x in range(100)]
print(type(my_list))
print(my_list)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Creating list using `For Loop` , `If Condition ` And `Range()`

# COMMAND ----------

my_list = [x for x in range(20) if x%2==0]
print(my_list)

# COMMAND ----------

# MAGIC %md
# MAGIC ## To find sum from 0 to 1000
# MAGIC

# COMMAND ----------

v_num = 0
target_value =1000
for i in range(target_value+1):
    v_num = v_num+i
print('Sum of 1000 Values : ',v_num)

# COMMAND ----------

# MAGIC %md
# MAGIC ### To find sum from 0 to 1000 (only even)
# MAGIC

# COMMAND ----------

v_even = 0
var_list = []
for i in range(1001):
    if i%2 ==0:
        var_list.append(i)
        v_even = v_even+i

print('Sum of Even Numbers from 1 To 1000 using variable : ', v_even)
print('Sum Of Even Numbers From 1 to 1000 using list : ',sum(var_list))

# COMMAND ----------

a=10
b={"a":1,"b":2,"c":4}

# data item (values,keys)
for i in b:
  print(b[i])

# COMMAND ----------

