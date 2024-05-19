# Databricks notebook source
# MAGIC %md
# MAGIC #### Python  Lambda  Function
# MAGIC * A lambda function is a small anonymous function.
# MAGIC
# MAGIC * A lambda function can take any number of arguments, but can have one line expression.
# MAGIC
# MAGIC *  Syntax
# MAGIC `lambda arguments : expression`
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC
# MAGIC %md
# MAGIC <img src='https://i1.faceprep.in/Companies-1/python-lambda-functions-new.png' width=500 height =500>

# COMMAND ----------

def sum_of(a,b):
  
  return a*b

# COMMAND ----------

sum_of(10,2)

# COMMAND ----------

lambda_x = lambda a,b : a*b
lambda_x(4,5)

# COMMAND ----------


lambda_x(10,3)

# COMMAND ----------

x = lambda a,b : a * b
print(x(50,40))

# COMMAND ----------

type(x)

# COMMAND ----------

def my_fuc(a,b):
  return a*b

# COMMAND ----------

my_fuc(10,20)

# COMMAND ----------

# MAGIC %md
# MAGIC * Multiply argument a with argument b and return the result:
# MAGIC
# MAGIC

# COMMAND ----------

x = lambda a : (a+100,a+200)
print(x(10))

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC ##### Summarize argument a, b, and c and return the result:
# MAGIC
# MAGIC

# COMMAND ----------

x = lambda a, b, c : a * b * c *100

# COMMAND ----------

print(x(5, 6, 2))

# COMMAND ----------

map(func)

# COMMAND ----------

# RDD
my_rdd =sc.parallelize([1, 5, 4, 6, 8, 11, 3, 12])

new_list = my_rdd.map(lambda x: x * x)

print('original rdd values : ',my_rdd.collect())
print('after map with lamdba : ',new_list.collect())

# COMMAND ----------

# RDD
my_rdd =sc.parallelize([1, 5, 4, 6, 8, 11, 3, 12])

new_list = my_rdd.map(lambda x: x * x)
print('original rdd values : ',my_rdd.collect())
print('after map with lamdba : ',new_list.collect())

# COMMAND ----------

divide = lambda val : val/2
print(list(map(divide,[11,12,13,14])))