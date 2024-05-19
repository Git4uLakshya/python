# Databricks notebook source
# MAGIC %md
# MAGIC ##### Python Collections (Arrays)
# MAGIC * There are four collection data types in the Python programming language:
# MAGIC
# MAGIC * List is a collection which is ordered and changeable. Allows duplicate members. []
# MAGIC * Tuple is a collection which is ordered and unchangeable. Allows duplicate members. ()
# MAGIC * Set is a collection which is unordered and unindexed. No duplicate members. {}
# MAGIC * Dictionary is a collection which is unordered, changeable and indexed. No duplicate members. {}

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC #### Tuple
# MAGIC * A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
# MAGIC * Python tuple is much like a list except that it is immutable or unchangeable once created. 
# MAGIC * Tuples use parentheses and creating them is as easy as putting different items separated by a comma between parentheses. 

# COMMAND ----------

tuple1 = (1,2,3,4,5)
tuple1[:3]

# COMMAND ----------

a_tuple = (1,1,2,2,2,3,3,3,3,4,4,5,'Sample','Python','Pyspark')
print(type(a_tuple))
print(a_tuple)

# COMMAND ----------

a_tuple[0:10]

# COMMAND ----------

help(a_tuple)

# COMMAND ----------

a_tuple.count(5)

# COMMAND ----------

# MAGIC %md
# MAGIC # Slicing
# MAGIC * If you omit the first index, the slice starts at the beginning. If you omit the second, the slice goes to the end. So if you omit both, the slice is a copy of the whole list.
# MAGIC

# COMMAND ----------

mytuple = ("apple", "banana", "cherry","kiwi","mango","orange","dragen")
print(mytuple)
print(mytuple[:4])

# COMMAND ----------

mytuple = ("apple", "banana", "cherry","kiwi","mango","orange","dragen")
print(mytuple)
print(mytuple[3:])

# COMMAND ----------

mytuple = ("apple", "banana", "cherry")
print('Tuple Values: ',mytuple)
print('Tuple values by index value 1: ',mytuple[0])

# COMMAND ----------

# MAGIC %md
# MAGIC #### Negative Indexing
# MAGIC * Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.

# COMMAND ----------

mytuple = ("apple", "banana", "cherry")
print('Negative Index -1 Value: ',mytuple[-1])

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC #### Range of Indexes
# MAGIC * You can specify a range of indexes by specifying where to start and where to end the range.
# MAGIC
# MAGIC When specifying a range, the return value will be a new tuple with the specified items.

# COMMAND ----------

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5]) 

# COMMAND ----------

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-5:-3])

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC #### Change Tuple Values
# MAGIC * Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# MAGIC
# MAGIC * But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
# MAGIC

# COMMAND ----------

tuple_a = (1,2,3,4,5)
list_a = list(tuple_a)
list_a[1]=44
tuple_a = tuple(list_a)
tuple_a

# COMMAND ----------

x = ("apple", "banana", "cherry")
x = list(x)  # Converting TUPLE into LIST
x[2] = "kiwi"  # Updating a value based index in LIST
x = tuple(x)  # Converting back to TUPLE From LIST
print(x)
print('X type is : ',type(x))

# COMMAND ----------

y[2] = "kiwi"
x = tuple(y)
print(x)
print('X type is : ',type(x))
print('y type is :',type(y))
y

# COMMAND ----------

type(x)
y = list(x)
print(y)

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Loop Through a Tuple
# MAGIC * You can loop through the tuple items by using a for loop.

# COMMAND ----------

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)


# COMMAND ----------

# MAGIC %md
# MAGIC * Check if Item Exists
# MAGIC * To determine if a specified item is present in a tuple use the in keyword:

# COMMAND ----------

val="bananas"
thistuple = ("apple", "banana", "cherry")
if val in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
else:
  print("No, This Item is not available in this tuple")
  
  

# COMMAND ----------

# MAGIC %md
# MAGIC * Tuple Length
# MAGIC * To determine how many items a tuple has, use the len() method

# COMMAND ----------

thistuple = ("apple", "banana", "cherry",1,2,3,'')
print(len(thistuple))

# COMMAND ----------

var=55
print(var)
del var

# COMMAND ----------

print(var)

# COMMAND ----------

# MAGIC %md
# MAGIC * Remove Items
# MAGIC * Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely
# MAGIC * The del keyword can delete the tuple completely
# MAGIC

# COMMAND ----------

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error NameError: name 'thistuple' is not defined

# COMMAND ----------

# MAGIC %md
# MAGIC * Join Two Tuples
# MAGIC * To join two or more tuples you can use the + operator

# COMMAND ----------

tuple1 = ("a", "b" , "c","d") # its similar to append option. just it will add end of the tuple.
tuple2 = ("e","f","g")
tuple3 = tuple1 + tuple2
print(tuple3)
type(tuple3)

# COMMAND ----------

# MAGIC %md 
# MAGIC ##### Slicing the Tuple
# MAGIC * Slicing a tuple is similar to slicing a list. 

# COMMAND ----------

tuple1 = ('Python', 'Julia', 1, 3.1415)
tuple1[1:3]

# COMMAND ----------

# MAGIC %md
# MAGIC #### The tuple() Constructor
# MAGIC * It is also possible to use the tuple() constructor to make a tuple.

# COMMAND ----------

a=(12,34,45,45,56,56)
print(type(a))

# COMMAND ----------

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
type(thistuple)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Nested Tuples
# MAGIC * It is also possible to create a tuple of tuples or tuple of lists. 

# COMMAND ----------

list1 = ['Python', 'pyspark', 1, 3.1415]
list2 = [('a', 'b'), ('c', 'd')]  # List of tuples is possible too!
tuple1 = (1, 2, 3, 4, 5)
tuple2 = tuple(list1 + list2)+ tuple1  # Concatenating the list and converting to tuple.
#Then adding two tuples and appening it in another tuple
tuple2