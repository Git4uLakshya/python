# Databricks notebook source
# MAGIC %md
# MAGIC ## __Indentation__
# MAGIC * Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.

# COMMAND ----------

var1=55 # True or False 
if var1>40:
  print('50 is greater than 40')

  

# COMMAND ----------

a=-2
if a<0:
  print('its positive number')
  print('another statement')
  print('3rd statement')
else:
  print('its Negative number')

print('multiple statements')

# COMMAND ----------

x=55
if x%2 == 0: 
    print('x is even')
else :
    print('x is odd')

# COMMAND ----------

x=10
y=66
if x <=y:
    print('x is less than y')
elif x >y:
    print('x is greater than y')
else:
    print('x and y are equal')

# COMMAND ----------

x=88
y=88
if x == y:
    print('x and y are equal')
    if x < y:
        print('x is less than y')
    else:
        print('Others or else')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')

# COMMAND ----------

A=900
a=500
b=800
if A<b:
  print("A is greater than B : ",A)
  print("this is another statement")
  print("this 3rd statement")
else:
  print("this is else statement")

# COMMAND ----------

a=33
b=66
if a>b:
  print('A value is Greater than B value : ',a)
else:
  print("its Else Blob: A is Less Than B : ",b)

# COMMAND ----------

a = 99
b = 88
if b > a:
print("b is greater than a and B Value is : " ,b)
else:
  print(' A is Greater than B And A value is : ',a)

# COMMAND ----------

#If statement, without indentation (will raise an error):
a = 33
b = 200
if b > a:
  print("b is greater than a") # you will get an error}
else:
  print('this is else')

# COMMAND ----------

# MAGIC %md
# MAGIC ### __Elif__
# MAGIC * The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition"
# MAGIC

# COMMAND ----------

a = 100

if a==200:
  print("a value is 200")
elif a>200:
  print("a value is more than 200")
elif a<200:
  print('a value is less than 200')
else:
  print('last else statements')

# COMMAND ----------

# MAGIC %md
# MAGIC #### Else
# MAGIC * The else keyword catches anything which isn't caught by the preceding conditions.

# COMMAND ----------

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b",a)

# COMMAND ----------

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# COMMAND ----------

# MAGIC %md
# MAGIC * __Short Hand If__
# MAGIC * If you have only one statement to execute, you can put it on the same line as the if statement.

# COMMAND ----------

a=9
b=88
if a < b: print("b is greater than a")

# COMMAND ----------

# MAGIC %md
# MAGIC * __Short Hand If ... Else __
# MAGIC * If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:

# COMMAND ----------

a = 700
b = 550
print('A is greater than b Statement',a) if a > b else print('a is less than b Statement',b)

# COMMAND ----------

# MAGIC %md
# MAGIC * One line if else statement, with 3 conditions:
# MAGIC
# MAGIC * This technique is known as Ternary Operators, or Conditional Expressions.
# MAGIC
# MAGIC * Ternary operators also known as conditional expressions are operators that evaluate something based on a condition being true or false. It was added to Python in version 2.5. It simply allows to test a condition in a single line replacing the multiline if-else making the code compact.

# COMMAND ----------

a = 400
b = 400
print("A Greater Than B : ",b) if a > b else print("its a equal to B =") if a == b else print("B is Greater Than A",a)

# COMMAND ----------

#Test if a is greater than b, AND if c is greater than a
a = 600
b = 563
c = 670
if a > b and b > c:
  print("Both conditions are True")
else:
  print('Both conditions are not True...')

# COMMAND ----------

a = 200
b = 33
c = 500
if (a > b and  a > c):
  print("At least one of the conditions is True")
else:
  print("else statement ")

# COMMAND ----------

print(True and False)

# COMMAND ----------

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

# COMMAND ----------

# MAGIC %md
# MAGIC * __Nested If__
# MAGIC * You can have if statements inside if statements, this is called nested if statements.

# COMMAND ----------

x = 5

if x < 10:
  print("below ten,")  
  if x > 20:
    print("and also below 10!")
  else:
    print("but not above 10.")
else:
  print('actual X value is : ',x)
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# COMMAND ----------

a=55

if a<10:
  pass
else:
  print('this is sample pass statement')

# COMMAND ----------

a=55
if a > 10:
  pass
else:
  pass

# COMMAND ----------

# MAGIC %md
# MAGIC * __The pass Statement__
# MAGIC *  if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

# COMMAND ----------

a = 33
b = 200

if b > a:
  pass

# COMMAND ----------

