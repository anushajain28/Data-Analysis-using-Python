
# coding: utf-8

# In[1]:

import pandas as pd
import os
import numpy as np
import calendar


# In[2]:

current_path =os.path.expanduser('~')
current_path =os.path.join(current_path,'Assignment 3')
current_path =os.path.join(current_path,'Data')


# In[3]:

df = pd.read_csv( current_path + '\\employee_compensation.csv')   #read csv file


# In[4]:

df1 = df[df['Year Type'] == 'Calendar'] #filter data for calender year only


# In[5]:

df2 = df1[['Job Family' , 'Employee Identifier']] # create a dataframe with columns Job Family & Employee Identifier


# In[6]:

df3 = df1.groupby(['Employee Identifier']).mean() # Calculate mean values of salaries etc for each employee


# In[7]:

df3 = df3[df3['Overtime'] > (.05 * df3['Salaries'])].reset_index() #consider employees with overtime salaries greater than 5% of salaries


# In[8]:

df4 = pd.merge(df3, df2, on ='Employee Identifier') #merge two dataframes on column Employee Identifier


# In[9]:

df5 = df4.groupby(['Job Family']).mean() #calculate mean of total benefits and compensation for each job family


# In[10]:

df5['Percent_Total_Benefit'] = (df5['Total Benefits'] / df5['Total Compensation'] * 100) # calculate percent of total benefits
output = df5[['Total Benefits', 'Total Compensation' , 'Percent_Total_Benefit']]
result = output.head() 
print(result)


# In[11]:

output.to_csv(os.getcwd()+ '\\Q2_Part_2_Output.csv')

