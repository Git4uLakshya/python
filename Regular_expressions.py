# Databricks notebook source
# MAGIC %md
# MAGIC #### Regular expressions
# MAGIC * Regular expressions are almost their own little programming language for searching and parsing strings. As a matter of fact, entire books have been written on the topic of regular expressions. In this chapter, we will only cover the basics of regular expressions. For more detail on regular expressions, see: <https://docs.python.org/3/library/re.html>
# MAGIC
# MAGIC * The regular expression library re must be imported into your program before you can use it. The simplest use of the regular expression library is the search() function. The following program demonstrates a trivial use of the search function.
# MAGIC * using string methods like `split` and `find` and using lists and string slicing to extract portions of the lines.

# COMMAND ----------

# MAGIC %md
# MAGIC * `findall`	Returns a list containing all matches
# MAGIC * `search`	Returns a Match object if there is a match anywhere in the string
# MAGIC * `split`	Returns a list where the string has been split at each match
# MAGIC * `sub` 	Replaces one or many matches with a string

# COMMAND ----------

list={}

# COMMAND ----------

import re
help(re)

# COMMAND ----------

import re

txt = "This is sample program where you can list of words in this text"
x = re.findall("\s", txt)
print(x)
#type(x)

# COMMAND ----------

import re

txt = "how to use regular expresssion"
x = re.search("\s", txt)
print(x)

# COMMAND ----------

import re

txt = "How to use search in regular expression"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())

# COMMAND ----------

import re

txt = "How to use split in regular expression"
x = re.split("\s", txt)
print(x)

# COMMAND ----------

# MAGIC %md
# MAGIC * The sub() function replaces the matches with the text of your choice:
# MAGIC
# MAGIC

# COMMAND ----------

import re

txt = "How to substitue value in regular expression"
x = re.sub("\s", "TEST", txt)
print(x)

# COMMAND ----------

import re

pattern = '^\D+'
test_string = 'python relugar expressions learn with 22 examples'
result = re.match(pattern, test_string)
if result:
  print("Search successful.",result)
else:
  print("Search unsuccessful.",result)	

# COMMAND ----------

# MAGIC %md
# MAGIC ##### \d
# MAGIC * it will return all numbers [0-9] in single digit format

# COMMAND ----------

# Program to extract numbers from a string
import re

string = 'if you are 2 see that 4th row 5th column and 77 records'
pattern = '\d'
result = re.findall(pattern, string) 
print(result)

# COMMAND ----------

# MAGIC %md
# MAGIC ##### \d+
# MAGIC * it will return all numbers [0-9] in group format

# COMMAND ----------

# Program to extract numbers from a string
import re

string = 'find employee details in 40th row 2nd file and 30th column % & *  '
pattern = '\d+'
result = re.findall(pattern, string) 
print(result)

# COMMAND ----------

# MAGIC %md
# MAGIC ##### \D
# MAGIC * it will return all characters [a-zA-Z] in single character format

# COMMAND ----------

# Program to extract numbers from a string
import re

string = 'are you able to find 40th employee in 2nd column % & *'
pattern = '\D'
result = re.findall(pattern, string) 
print(result)

# COMMAND ----------

# Program to extract numbers from a string
import re

string = 'yes i found in 2nd row 5th column and 10 duplicate records'
pattern = '\D+'
result = re.findall(pattern, string) 
print(result)

# COMMAND ----------

# MAGIC %md
# MAGIC ##### \w
# MAGIC * it will return all characters as individual like `[a-zA-Z0-9_]`

# COMMAND ----------

# Program to extract numbers from a string
import re

string = 'yes i found in 2nd row 5th column and 10 duplicate records'
pattern = '\w'
result = re.findall(pattern, string) 
print(result)

# COMMAND ----------

# Program to extract numbers from a string
import re

string = 'yes i found in 2nd row 5th column and 10 duplicate records'
pattern = '\w+'
result = re.findall(pattern, string) 
print(result)

# COMMAND ----------

# MAGIC %md
# MAGIC ##### \W
# MAGIC * opposite of \w and its equal to `[^a-zA-Z0-9_].`

# COMMAND ----------

# Program to extract numbers from a string
import re

string = 'yes i found in 2nd row 5th column and 10 duplicate records'
pattern = '\W'
result = re.findall(pattern, string) 
print(result)