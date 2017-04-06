
# coding: utf-8

# In[19]:

import pandas as pd
import os
import calendar


# In[20]:

current_path =os.path.expanduser('~')
current_path =os.path.join(current_path,'Assignment 3')
current_path =os.path.join(current_path,'Data')


# In[21]:

df = pd.read_csv( current_path + '\\vehicle_collisions.csv')   #read csv file


# In[22]:

df['DATE'] = pd.to_datetime(df['DATE']) #convert date to datetime format


# In[23]:

df['YEAR'] , df['MONTH'] = df['DATE'].dt.year , df['DATE'].dt.month # extract year and month from the date and create new columns


# In[24]:

df1 = df[df['YEAR'] == 2016]  #create a new dataframe of records with year value 2016


# In[25]:

total_accidents = df1.groupby('MONTH').count().reset_index() #count the total number of accidents for each month 


# In[26]:

total_nyc = total_accidents[['MONTH','UNIQUE KEY']]  # create another dataframe with selected columns


# In[27]:

df2 = df1[df1['BOROUGH'] == 'MANHATTAN'] # create dataframe for records of incidents that happened in Manhattan
accidents_in_mhtn = df2.groupby('MONTH').count().reset_index() #count the total number of accidents in Manhattan in each month


# In[28]:

total_mhtn = accidents_in_mhtn[['MONTH','UNIQUE KEY']] 


# In[29]:

df3 = pd.merge(total_mhtn, total_nyc, on ='MONTH' ) #merge two dataframes on column MONTH


# In[30]:

df3['MONTH'] = df3['MONTH'].apply(lambda x: calendar.month_abbr[x])  #change the integer value of month to name


# In[31]:

df3=df3.rename(columns = {'UNIQUE KEY_x':'MANHATTAN' , 'UNIQUE KEY_y': 'NYC'}) #rename the column names
df3['PERCENTAGE'] = df3['MANHATTAN'] / df3['NYC'] #calculate percentage using values of columns in dataframe
output = df3.head()
print(output)


# In[14]:

df3.to_csv(os.getcwd()+ '\\Q1_Part_1_Output.csv', index = False)

