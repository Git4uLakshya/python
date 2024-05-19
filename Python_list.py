# Databricks notebook source
# MAGIC %md
# MAGIC ##### Python DataStructures or  Collections  (Arrays)
# MAGIC * There are four collection data types in the Python programming language:
# MAGIC
# MAGIC * List is a collection which is ordered and changeable. Allows duplicate members.[,]
# MAGIC * Tuple is a collection which is ordered and unchangeable(immutable). Allows duplicate members.(,)
# MAGIC * Set is a collection which is unordered and unindexed. No duplicate members.{,}
# MAGIC * Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.{name:'ravi',age:55}

# COMMAND ----------

# MAGIC %md
# MAGIC #### LIST
# MAGIC * Python knows a number of compound data types, used to group together other values. The most versatile is the list, which can be written as a list of comma-separated values (items) between square brackets []. Lists might contain items of different types, but usually the items all have the same type.
# MAGIC
# MAGIC * List is a collection which is ordered and changeable. Allows duplicate members.
# MAGIC * In Python lists are written with square brackets.
# MAGIC * Note:  Python Lists replace Arrays (from most programming languages)
# MAGIC

# COMMAND ----------

list_a = [10,11,12,13,14,15,16,17,18,19,20]
list_a[-5:-1]
# range (N-1)

# COMMAND ----------

mylist = ["Green","Green", "Red", "Yello",1,1,2,3,4,True,False]
print(mylist)
type(mylist)

# COMMAND ----------

lista=[1,2,3,4]
print(lista)
lista[3]=44
print(lista)

# COMMAND ----------

a_list = ["test1","test2",1,2,3,4,2,3,4,5,6,6,7,8,8,9,10]
print(a_list[-10 : -5])

# COMMAND ----------

a_list = [1,2,3,4,5,6,7,8,9,10]
print(a_list[-6:-2])

# COMMAND ----------

print(a_list[-1])

# COMMAND ----------

mylist = ["Green", "Red", "Yello"]
print('Minus one (-1) Index : ',mylist[-1])
print('Minus two (-2) Index : ',mylist[-2])
print('Minus three (-3) Index : ',mylist[-3])

# COMMAND ----------

print(mylist[0])

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Range of Indexes
# MAGIC * lists can be indexed and sliced
# MAGIC * You can specify a range of indexes by specifying where to start and where to end the range.
# MAGIC
# MAGIC * When specifying a range, the return value will be a new list with the specified items.

# COMMAND ----------

mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
mylist[0:3]

# COMMAND ----------

mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
mylist[:6]

# COMMAND ----------

mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
mylist[2:]

# COMMAND ----------

# MAGIC %md
# MAGIC #### Updating existing item using `indexes`

# COMMAND ----------

mylist = ["Jan", "Feb", "Mar","Apr"]
mylist[3]="Nov"
mylist

# COMMAND ----------

mylist = ["Jan", "Feb", "Mar","Apr"]
print("Before Updating : ",mylist[0:])
mylist[3] = "Dec"
print("After Updating : ",mylist[0:])

# COMMAND ----------

help(mylist)

# COMMAND ----------

list=[1,2,2]
help(list)

# COMMAND ----------

# MAGIC %md
# MAGIC * Inserting  or appending new item or value into LIST using `append`

# COMMAND ----------

mylist = ["Jan", "Feb", "Mar","Apr"]
print('before adding new value :',mylist)
mylist.append(["May","June","Jul"])
print('After adding new value : ',mylist)

# COMMAND ----------

# MAGIC %md
# MAGIC * if we want add any value inbetween we can go with `insert` specifying index value

# COMMAND ----------

mylist = ["Jan", "Mar", "Apr"]
print('Before inserting :',mylist)
mylist.insert(1, "Feb")
print('After inserting : ',mylist)

# COMMAND ----------

list_b =['val1','val1','va2','val3']
list_b.index('val3')

# COMMAND ----------

help(mylist)

# COMMAND ----------

# MAGIC %md
# MAGIC #### extend
# MAGIC extend takes a list as an argument and appends all of the elements
# MAGIC

# COMMAND ----------

mylist = ["Jan", "Feb", "Mar","Apr"]
monthlist = ["May","June","Jul"]
mylist.extend(monthlist)
mylist

# COMMAND ----------

# MAGIC %md
# MAGIC #### List Length
# MAGIC * To determine how many items a list has, use the len() function:

# COMMAND ----------

lenlist = [1,2,3,4,5,6,7,8,9,10]
len(lenlist)

# COMMAND ----------

# MAGIC %md
# MAGIC #### SORT
# MAGIC * sort arranges the elements of the list from low to high

# COMMAND ----------

unsortlist = ['a','d','e','c','f','h','g','b']
unsortlist.sort()
unsortlist

# COMMAND ----------

unsortlist = ['a','d','e','c','f','h','g','b']
unsortlist.sort(reverse=True)
unsortlist

# COMMAND ----------

# just reversing entire list items.
list =[1,2,3,3,1,2,8,9,10,4,5]
list.reverse()
list

# COMMAND ----------

# MAGIC %md
# MAGIC * Removing individual items from LISt we ca use `remove` method with value

# COMMAND ----------

mylist = ["Jan", "Feb", "Mar","Apr"]
print('Before Removing :',mylist)
mylist.remove("Feb")
print('After removing :',mylist)

# COMMAND ----------

# MAGIC %md
# MAGIC * Remove last item from list is `pop()` it will be removed last item from list

# COMMAND ----------

mylist = ["jan", "feb", "mar","apr"]
mylist.append("dec")
removed_var=mylist.pop()
print(mylist)
print(removed_var)

# COMMAND ----------

mylist = ["jan", "feb", "mar","apr"]
removed_var=mylist.pop(1)
print(mylist)
print(removed_var)

# COMMAND ----------

# len()
# del 
var=55
print('before deleting ' ,var)
del var
print('after deleting ',var)

# COMMAND ----------

mylist = ["jan", "feb", "mar"]
del mylist[0]
print(mylist)

# COMMAND ----------

mylist = ["jan", "jan", "jan"]
mylist.clear()
print(mylist)

# COMMAND ----------

mylist = ["jan", "jan", "jan"]
del mylist
print(mylist)

# COMMAND ----------

a_list = [1,2,3,4,5,6,7,8,9,9,10]

# COMMAND ----------

sum(a_list)

# COMMAND ----------

mylist = ["jan", "feb", "mar"]
mylist.clear()
print(mylist)

# COMMAND ----------

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)
print(type(list1))

# COMMAND ----------

# MAGIC %md
# MAGIC #### COPY
# MAGIC * You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
# MAGIC
# MAGIC * There are ways to make a copy, one way is to use the built-in List method copy().

# COMMAND ----------

thislist = ["apple", "banana", "cherry"]
copylist=thislist
thislist.append("kiwi")
print('thislist values : ',thislist)
print('copylist values : ',copylist)

# COMMAND ----------

print(list2)

# COMMAND ----------

thislist = ["vikranth", "reshwanth", "Pragna","Ravi","Raj"]
mylist = thislist.copy()
print(mylist)
type(mylist)

# COMMAND ----------

a=[1,2,3,4,5,6,7,8,7,7,45,45,5,7]
sum(a)

# COMMAND ----------

# list Count
list_count = ['a', 'e', 'i', 'o', 'i', 'u','I','i']

print(list_count.count('i'))
 

# COMMAND ----------

# vowels list
vowels = ['RAJ', 'RAM', 'KHADAR', 'RAVI', 'PRASAD', 'MAHESH','SRI']

# index of 'RAM' in  
print('Index of KHADAR :',vowels.index('KHADAR'))
print('Index of MAHESH :',vowels.index('MAHESH'))

# COMMAND ----------

list1 = ['apple', 'banana', 'cherry']
list1.sort()
print(list1)

# COMMAND ----------

a.sort(reverse = True)
a

# COMMAND ----------

cars = [1,44,2,34,100,36]

cars.sort()
print(cars)

# COMMAND ----------

 list.clear()

# COMMAND ----------

# sorted will support single datatype
list_num = [4,3,1,2,5,6]
sorted(list_num)

# COMMAND ----------

list_str = ["g","h","a","b","c","d","e","i"]
sorted(list_str)