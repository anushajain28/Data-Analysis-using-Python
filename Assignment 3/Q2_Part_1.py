
# coding: utf-8

# In[1]:

import pandas as pd
import os
import calendar


# In[3]:

current_path =os.path.expanduser('~')
current_path =os.path.join(current_path,'Assignment 3')
current_path =os.path.join(current_path,'Data')


# In[4]:

df = pd.read_csv( current_path + '\\employee_compensation.csv')   #read csv file


# In[5]:

df1 = df[['Organization Group','Department','Total Compensation']]  # create dataframe with selected columns


# In[6]:

df2 = df1.groupby(['Organization Group','Department']).count() # group the records based on columns Organisation and Department
df2['Total Compensation'] = df1.groupby(['Organization Group','Department'])['Total Compensation'].mean() #calculate average of total compensation for each group


# In[14]:

g = df2['Total Compensation'].groupby(level=0, group_keys=False) # group by the first level of index
#res = g.apply(lambda x: x.order(ascending=False)) # sort within each group in descending order 
res = g.apply(lambda x: x.sort_values(ascending=False))
res = pd.DataFrame(res) #convert series to dataframe 
output = res.head()
#output
print (output)


# In[8]:

res.to_csv(os.getcwd()+ '\\Q2_Part_1_Output.csv') 

