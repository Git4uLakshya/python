# Databricks notebook source
# MAGIC %md
# MAGIC ##### Python Collections or Data structures (Arrays)
# MAGIC * There are four collection data types in the Python programming language:
# MAGIC
# MAGIC * List is a collection which is ordered and changeable. Allows duplicate members.[]
# MAGIC * Tuple is a collection which is ordered and unchangeable. Allows duplicate members. ()
# MAGIC * Set is a collection which is unordered and unindexed. No duplicate members.{}
# MAGIC * Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.{}

# COMMAND ----------

object = {1,3,2,1,1,1,2,2,2,2,4,5,5,5,5,6,6,6,6,7,7,7}
object

# COMMAND ----------

storing multiple values and those can be multiple data types...

# COMMAND ----------

row- rowid

# COMMAND ----------

# MAGIC %md
# MAGIC #### Set
# MAGIC * A set is a collection which is unordered and unindexed. In Python, sets are written with curly brackets.

# COMMAND ----------

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
basket    # show that duplicates have been removed

# COMMAND ----------

a_sets = {11,2,2,2,2,2,111,1,1,1,1,1,1,2,3,4,5,55,5,"Rav","ram",6,6,7,7,8,9,10,'80','70'}
print(a_sets)
type(a_sets)

# COMMAND ----------

help(a_sets)

# COMMAND ----------

thisset = {"apple", "banana", "cherry"}
print(thisset)
type(thisset)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Access Items
# MAGIC * You cannot access items in a set by referring to an index or a key.
# MAGIC * But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

# COMMAND ----------

thisset = {"apple", "banana", "cherry","apple", "banana", "cherry","apple", "banana", "cherry"}
for x in thisset:
  print(x)

# COMMAND ----------

thisset = {"apple", "banana", "cherry"}

print('banana' in thisset) 

# COMMAND ----------

# list - insert(index,value) ,extend and append
# set - add() - single value , update() for multiple values ([])

# COMMAND ----------

# MAGIC %md
# MAGIC #### Add Items
# MAGIC * To add one item to a set use the add() method.
# MAGIC
# MAGIC * To add more than one item to a set use the update() method.

# COMMAND ----------

thisset = {"apple", "banana", "cherry"}
thisset.add("range")
print(thisset)

# COMMAND ----------

help(thisset)

# COMMAND ----------

# MAGIC %md
# MAGIC * Add multiple items to a set, using the __update()__ method:

# COMMAND ----------

thisset = {"apple", "banana", "cherry"}
thisset.update(["abc","test1","test2"])
print(thisset)
thisset.add("range")
print(thisset)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Get the Length of a Set
# MAGIC * To determine how many items a set has, use the __len()__ method.
# MAGIC

# COMMAND ----------

a_set ={1,2,3,4,5,6,7,8,9,10}
len(a_set)

# COMMAND ----------

len(a_set)

# COMMAND ----------

thisset = {'mango', 'grapes', 'banana', 'orange', 'apple', 'cherry'}
print(len(thisset))

# COMMAND ----------

help(thisset)

# COMMAND ----------

# list remove values - remove (),pop(),del list[] ,clear()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Remove Item
# MAGIC * To remove an item in a set, use the __remove()__, or the __discard()__ method.
# MAGIC

# COMMAND ----------

thisset = {"apple", "banana", "cherry","kiwi"}
thisset.remove("bananass")
print(thisset)

# COMMAND ----------

thisset = {"apple", "banana", "cherry","kiwi"}
thisset.discard("bananas")
print(thisset)
thisset.discard('apple')
print(thisset)

# COMMAND ----------

list_A = [1,2,3,4]
list_A.append(5)
list_A.append(6)
print('before deletion ',list_A)
list_A.pop()
print('after deletion ',list_A)
list_A.pop()
print('after deletion ',list_A)              

# COMMAND ----------

# MAGIC %md
# MAGIC #### 
# MAGIC * You can also use the __pop()__, method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.
# MAGIC
# MAGIC * The return value of the pop() method is the removed item.
# MAGIC

# COMMAND ----------

thisset = {"apple", "banana", "cherry","kiwi"}
x = thisset.pop()
print(x)
print(thisset)

# COMMAND ----------

# indexes it will follow range ()
# String,list,tuple,dict - with updatable.
# table data. rows (rowid)
# set operators ( union,intersection,minus(subtract))

# COMMAND ----------

x = thisset.pop()
print(x)

# COMMAND ----------

# MAGIC %md
# MAGIC * The __clear()__ method empties the set:

# COMMAND ----------

thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset.clear()
thisset
# {}

# COMMAND ----------

# MAGIC %md
# MAGIC * The __`del`__ keyword will delete the set completely:

# COMMAND ----------

thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

# COMMAND ----------

help(set3)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Join Two Sets
# MAGIC * There are several ways to join two or more sets in Python.
# MAGIC * You can use the union() method that returns a new set containing all items from both sets.
# MAGIC * update() method that inserts all the items from one set into another

# COMMAND ----------

set1 = {"a", "b" , "c",1,2,3,4,5,6,66,99}
set1
set2 = {1, 2, 3,"c",23,45,"test11"}
set2.intersection(set1)  # set1 - set2  # set2- set1  # difference,subtract,minus

# COMMAND ----------

set1 = {"a", "b" , "c",1,2,3,4,5,6,66,99}
set2 = {1, 2, 3,"c",23,45,"test11"}
set3 = set2.union(set1) 
set2.update(set1)
print('union set : ',set3)
print('Updating existing set : ',set2)

# COMMAND ----------

# Database set operators 
# Dataset ( similar to table)
# set operators
# 1) union - merge two sets  and its remove duplicates
# 2) intersection - getting common matching items from two sets
# 3) difference (subtract or minus) - getting A-B or Set1- Set2  # its equal to subtract or minus set operator
# unionall will return duplicate.

# COMMAND ----------

#same data type.

# COMMAND ----------

set1 ={1,2,3,4,5,6}
set2 = {3,4,5,6,7,8}
set2.intersection(set1)
# subtract , minus

# COMMAND ----------

# MAGIC %md
# MAGIC * The update() method inserts the items in set2 into set1

# COMMAND ----------

set1 = {"a", "b" , "c",1,2,3,}
set2 = {1, 2, 3,4,5,"b"}
set1.intersection(set2)
print(set1)

# COMMAND ----------

# A Set of names
names = {"Ravi", "Raj", "Ram"}

# copying using the copy() method
names2 = names.copy()
print(names)
print(names2)

# COMMAND ----------

A = {'a', 'b', 'c', 'd'}
B = {'c', 'f', 'g'}
print(A.difference(B)) # Equivalent to A-B ( it is equal to minus operator)
print(B.difference(A)) # Equivalent to B-A ( it is equal to minus operator)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Note: when we are doing data set set operators.
# MAGIC A Difference B and B Difference A will get different result set
# MAGIC but A union B, B union A and A intersection B and B intersection A will get same results.

# COMMAND ----------

A = {'a', 'b', 'c', 'd','e'}
B = {'c','d','e', 'f', 'g'}
# Equivalent to common matching values
print(A.intersection(B))

# COMMAND ----------

