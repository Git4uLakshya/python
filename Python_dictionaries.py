# Databricks notebook source
# MAGIC %md
# MAGIC ##### Python Collections or Data Structures (Arrays)
# MAGIC * There are four collection data types in the Python programming language:
# MAGIC
# MAGIC * List is a collection which is ordered and changeable. Allows duplicate members.[]
# MAGIC * Tuple is a collection which is ordered and unchangeable. Allows duplicate members.()
# MAGIC * Set is a collection which is unordered and unindexed. No duplicate members.{}
# MAGIC * Dictionary(associative arrays) is a collection which is unordered, changeable and indexed. No duplicate members.{}

# COMMAND ----------

# MAGIC %md
# MAGIC #### Dictionary
# MAGIC * A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

# COMMAND ----------

list_a = [11,22,33,44]
set_a = {1,2}
dict = {"key1":"value1","key2":"value2",}
dict
# own index ( keys) - key-value pair data set.

# COMMAND ----------

for k,v in dict.items():
  print('keys : ',k)
  print('values : ',v)
for k in dict.keys():
  print('keys : ',k)
for v in dict.values():
  print('values : ',v)

# COMMAND ----------

# items - both keys and values
# keys - only keys
# values - only values
get()

# COMMAND ----------

dict_a = {'a':10,'b':11,'c':13,'d':True}
dict_a

# COMMAND ----------

thisdict = {"brand": "Mahindra","model": "XUV300","year": 2019,"year": 2021}
print(thisdict)
type(thisdict)

# COMMAND ----------

for a in thisdict:
  print('dict keys are : ',a)
  print('dict values are : ',thisdict[a])

# COMMAND ----------

for i in thisdict.keys():
  print('Dict values : ',thisdict[i])

# COMMAND ----------

for i,j in thisdict.items():
  print("dict values : ",(i,j))
thisdict.get('brand')

# COMMAND ----------

# MAGIC %md
# MAGIC * Accessing Items
# MAGIC * You can access the items of a dictionary by referring to its key name, inside square brackets

# COMMAND ----------

thisdict = {"brand": "Mahindra","model": "XUV300","year": 2019}
thisdict['model']

# COMMAND ----------

thisdict.items()

# items() - key-value pair un-packed
# values() - only values
# keys() - only keys
# get(key) - return value

# COMMAND ----------

# MAGIC %md
# MAGIC *  There is also a method called __`get()`__ that will give you the same result

# COMMAND ----------

thisdict = {"brand": "Mahindra","model": "XUV300","year": 2019}
print(thisdict["brand"])

# COMMAND ----------

# MAGIC %md
# MAGIC * __Change Values__
# MAGIC * You can change the value of a specific item by referring to its key name

# COMMAND ----------

thisdict = {"brand": "Mahindra","model": "XUV300","year": 2019}
thisdict["year"] = "2021"
print('Updated Year key value Is : ',thisdict["year"])
print(thisdict)

# COMMAND ----------

dicta ={'a':1,'b':2,'c':3}
dir(dicta)

# COMMAND ----------

# MAGIC %md
# MAGIC * __Loop Through a Dictionary__
# MAGIC * You can loop through a dictionary by using a for loop.
# MAGIC * When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
# MAGIC

# COMMAND ----------

thisdict["model"]

# COMMAND ----------

thisdict = {"brand": "Mahindra","model": "XUV300","year": 2019}
#Print all key names in the dictionary, one by one:
for a in thisdict:
  print("Dictinary Key Name : ",a)
  print('Dictionary Value  :',thisdict[a])

# COMMAND ----------

print(thisdict['year'])

# COMMAND ----------

#Print all values in the dictionary, one by one
for x in thisdict:
  print('Dictionary key Name: ',x) 
  print('Dictionary key values: ',thisdict[x]) 

# COMMAND ----------

# MAGIC %md
# MAGIC * You can also use the values() method to return values of a dictionary

# COMMAND ----------

for a in thisdict.values():
  print('Keys :',a)

# COMMAND ----------

# MAGIC %md
# MAGIC * You can also use the items() method to return keys and values of a dictionary

# COMMAND ----------

thisdict = {"brand": "Mahindra","model": "XUV300","year": 2019}
for a,b in thisdict.items():
  print('Keys :',a)
  print('Values : ',b)

# COMMAND ----------

# MAGIC %md
# MAGIC * Getting key names using keys() method

# COMMAND ----------

for x in thisdict.keys():
  print('Dictionary Key is : ',x)

# COMMAND ----------

# MAGIC %md
# MAGIC * __Check if Key Exists__
# MAGIC * To determine if a specified key is present in a dictionary use the in keyword

# COMMAND ----------

thisdict = {"brand": "Mahindra","model": "XUV300","year": 2020}
v_col="model"
if  v_col in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
else:
  print("NO Value is not available in Dict")

# COMMAND ----------

# MAGIC %md
# MAGIC * __Dictionary Length__
# MAGIC * To determine how many items (key-value pairs) a dictionary has, use the len() function.
# MAGIC

# COMMAND ----------

print(len(thisdict))

# COMMAND ----------

# MAGIC %md 
# MAGIC * __Adding Items__
# MAGIC * Adding an item to the dictionary is done by using a new index key and assigning a value to it

# COMMAND ----------

thisdict = {"brand": "Mahindra","model": "XUV300","year": 2020}
thisdict["color"] = "red"
thisdict["year"] = 2021
print(thisdict)

# COMMAND ----------

# MAGIC %md
# MAGIC * __Removing Items__
# MAGIC * There are several methods to remove items from a dictionary

# COMMAND ----------

thisdict = {"brand": "Mahindra","model": "XUV300","year": 2020}
#The pop() method removes the item with the specified key name
print("Before removing Dict items :",thisdict)
thisdict.pop("year")
print('After removing item : ',thisdict)

# COMMAND ----------

# MAGIC %md
# MAGIC * The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead)

# COMMAND ----------

thisdict = {"brand": "Mahindra","model": "XUV300","year": [2020,2019.2021]}
print("Before removing Dict items :",thisdict)
thisdict.popitem()
print('after removing dit items : ',thisdict)

# COMMAND ----------

# MAGIC %md
# MAGIC * The del keyword removes the item with the specified key name

# COMMAND ----------

a_list=[1,2,3,4,5,5,6]
print(a_list)
del a_list[2]
print(a_list)

# COMMAND ----------

thisdict = {"brand": "Mahindra","model": "XUV300","year": 2020}
print(thisdict)
del thisdict["model"]
print(thisdict)

# COMMAND ----------

# MAGIC %md
# MAGIC * The del keyword can also delete the dictionary completely

# COMMAND ----------

thisdict = {"brand": "Mahindra","model": "XUV300","year": 2020}
clear(thisdict)
print(thisdict) #this will cause an error because "thisdict" no longer exists.

# COMMAND ----------

help(thisdict)

# COMMAND ----------

# MAGIC %md
# MAGIC * The clear() method empties the dictionary

# COMMAND ----------

# len
# del (delete)
# this all are python common functions we can use or apply on any object like vairbales, collections...

# COMMAND ----------

thisdict = {"brand": "Mahindra","model": "XUV300","year": 2020}
thisdict.clear()
print(thisdict)
type(thisdict)

# COMMAND ----------

# MAGIC %md
# MAGIC * __Copy a Dictionary__
# MAGIC * You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
# MAGIC
# MAGIC * There are ways to make a copy, one way is to use the built-in Dictionary method copy()

# COMMAND ----------

thisdict = {"brand": "Mahindra","model": "XUV300","year": 2020}
print(thisdict)
mydict = thisdict.copy()
print(mydict)
type(mydict)

# COMMAND ----------

# MAGIC %md
# MAGIC * Make a copy of a dictionary with the dict() function

# COMMAND ----------

mydict = dict(thisdict)
print(mydict)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Nested Dictionaries
# MAGIC * A dictionary can also contain many dictionaries, this is called nested dictionaries.

# COMMAND ----------

myFriends = {"friend1" : {"name" : "Raj","year" : 1981},
             "friend2" : {"name" : "Prasad","year" : [1984,1955]},
             "friend3" : {"name" : "Mahesh","year" : 1985},
             "friend4" : {"name" : "Sridhar","year" : 1986}
            }
print(myFriends['friend2']["year"])

# COMMAND ----------

myFriends["friend2"]["year"]

# COMMAND ----------

# MAGIC %md
# MAGIC * The `dict()` Constructor
# MAGIC * It is also possible to use the dict() constructor to make a new dictionary

# COMMAND ----------

#thisdict = dict([('a',5),('b',6)])
dict_d =  dict(a=55,b=66)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)

# COMMAND ----------

dict_d