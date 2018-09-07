# Databricks notebook source
# MAGIC %python
# MAGIC import pickle
# MAGIC a = ['test value','test value 2','test value 3']
# MAGIC 
# MAGIC file_Name = "testfile"
# MAGIC # open the file for writing
# MAGIC fileObject = open(file_Name,'wb') 
# MAGIC 
# MAGIC # this writes the object a to the
# MAGIC # file named 'testfile'
# MAGIC testdmp =pickle.dump(a,fileObject)  
# MAGIC type(testdmp)
# MAGIC 
# MAGIC class MyClass():
# MAGIC     def __init__(self):
# MAGIC         self.i_var = '1000'
# MAGIC           

# COMMAND ----------

foo = MyClass()
#foo.class_var

pickle.dumps(foo, protocol=0)

# COMMAND ----------

import pickle as pl
class TestClass():
  def __init__(self):
    self.xxx = 'yyy'
       
t = TestClass()
t.xxx

type(t)
#dmp = pl.dumps(t)
#type(dmp)

# COMMAND ----------

import dill

# COMMAND ----------


import pickle
class Animal:
   def __init__(self, number_of_paws, color):
      self.color = color
      self.number_of_paws = number_of_paws
       
class Sheep(Animal):
   def __init__(self, color):
       Animal.__init__(self, 4, color)

mary = Sheep("white")
print (str.format("My sheep mary is {0} and has {1} paws", mary.color, mary.number_of_paws))
my_pickled_mary = pickle.dumps(mary, protocol=0)
print ("Would you like to see her pickled? Here she is!")
print (my_pickled_mary)    


# COMMAND ----------

import pickle
pickle.compatible_formats

# COMMAND ----------

import sys
print(sys.version)

# COMMAND ----------

import dill as dl 
class test(): 
  def __init__(self):
    self.xxx='YYYY'
t = test() 
t.xxx
dmd=dl.dumps(t,protocol=0)
type(dmd)

# COMMAND ----------

import datetime
import pytz
import time


def get_time():
  date = datetime.datetime.now(tz=pytz.utc)
  current_time = date.astimezone(pytz.timezone('US/Pacific')).time()
  return current_time
 

# COMMAND ----------

  
get_time()

# COMMAND ----------

# MAGIC %sh  lsb_release -a

# COMMAND ----------

# MAGIC %sh java -version

# COMMAND ----------

# MAGIC %sh sudo apt-get install openjdk-8-dbg

# COMMAND ----------

# MAGIC 
# MAGIC %sh sudo apt-get install openjdk-8-dbg

# COMMAND ----------

# MAGIC %sh sudo apt-get -y --allow-change-held-packages install openjdk-8-jdk

# COMMAND ----------

# MAGIC %ls  /var/cache/apt/archives/lock

# COMMAND ----------

# MAGIC %sh apt-get install aptitude

# COMMAND ----------

# MAGIC %sh sudo apt-get update

# COMMAND ----------

# MAGIC %sh sudo apt-get upgrade

# COMMAND ----------

# MAGIC 
# MAGIC %sh rm /var/lib/dpkg/lock

# COMMAND ----------

# MAGIC %sh sudo apt-get install openjdk-8-dbg=8u162-b12-0ubuntu0.16.04.2

# COMMAND ----------

# MAGIC %sh sudo apt-get upgrade 

# COMMAND ----------

#%sh sudo apt-get install openjdk-8-jdk
%sh ls /var/cache/apt/archives/lock

# COMMAND ----------

# MAGIC %sh cat /var/log/apt/term.log

# COMMAND ----------

# MAGIC %sh ls -ltr /

# COMMAND ----------

import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

plt.figure(1).show()


# COMMAND ----------

# MAGIC %sh cat /var/log/apt/term.log

# COMMAND ----------

# MAGIC %sh pwd

# COMMAND ----------

# MAGIC %python
# MAGIC dbutils.widgets.get("pickle_issue")

# COMMAND ----------



# COMMAND ----------

# MAGIC %scala
# MAGIC dbutils.notebook.getContext.notebookPath

# COMMAND ----------

# MAGIC %sh sudo apt-get install -y libblas-dev liblapack-dev 

# COMMAND ----------

# MAGIC %sh sudo apt-get -y --allow-change-held-packages install libblas-dev liblapack-dev 

# COMMAND ----------

dbutil.

# COMMAND ----------

#37

# COMMAND ----------

#38

# COMMAND ----------

#41

# COMMAND ----------

#42

# COMMAND ----------

#44

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------

# MAGIC %sh ls -ltr /home

# COMMAND ----------

# MAGIC %scala dbfs ls

# COMMAND ----------

# MAGIC %md Hello Mark Down

# COMMAND ----------

# MAGIC %md Another Mark Down Message 99