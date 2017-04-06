
# coding: utf-8

# In[1]:

import pandas as pd
import os
import calendar


# In[2]:

current_path =os.path.expanduser('~')
current_path =os.path.join(current_path,'Assignment 3')
current_path =os.path.join(current_path,'Data')


# In[3]:

df = pd.read_csv( current_path + '\\vehicle_collisions.csv')   #read csv file


# In[4]:

acc_each_borough = df.groupby('BOROUGH').count().reset_index() #count the total number of accidents for each borough


# In[5]:

acc_each_borough['MORE_VEHICLES_INVOLVED'] = acc_each_borough['VEHICLE 4 TYPE']  #Number of accidents which involved 4 or more vehicles


# In[6]:

acc_each_borough['THREE_VEHICLES_INVOLVED'] = acc_each_borough['VEHICLE 3 TYPE'] - acc_each_borough['MORE_VEHICLES_INVOLVED'] #Calculating Number of accidents which involved 3 vehicles


# In[7]:

acc_each_borough['TW0_VEHICLES_INVOLVED'] = acc_each_borough['VEHICLE 2 TYPE'] - acc_each_borough['VEHICLE 3 TYPE']  #Calculating Number of accidents which involved 2 vehicles


# In[8]:

acc_each_borough['ONE_VEHICLE_INVOLVED'] = acc_each_borough['VEHICLE 1 TYPE'] - acc_each_borough['VEHICLE 2 TYPE']  #Calculating Number of accidents which involved only 1 vehicle


# In[9]:

acc_each_borough = acc_each_borough[['BOROUGH','ONE_VEHICLE_INVOLVED','TW0_VEHICLES_INVOLVED','THREE_VEHICLES_INVOLVED','MORE_VEHICLES_INVOLVED']]
print(acc_each_borough)


# In[11]:

acc_each_borough.to_csv(os.getcwd()+ '\\Q1_Part_2_Output.csv', index = False)

