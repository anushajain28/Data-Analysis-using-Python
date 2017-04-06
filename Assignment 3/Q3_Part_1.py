
# coding: utf-8

# In[1]:

import pandas as pd
import os
import calendar
import numpy as np


# In[2]:

current_path =os.path.expanduser('~')
current_path =os.path.join(current_path,'Assignment 3')
current_path =os.path.join(current_path,'Data')


# In[3]:

df = pd.read_csv( current_path + '\\cricket_matches.csv')   #read csv file


# In[10]:

df1 = df.loc[df['home'] == df['winner']] # select the records where the host is the winner


# In[14]:

df1['Score'] = np.where((df1['innings1'] == df1['winner']), df1['innings1_runs'] , df1['innings2_runs'] )  #find out the score of the winning team


# In[7]:

df2 = df1[['home', 'Score']]


# In[8]:

output = df2.groupby('home')['Score'].mean()  #calculate the average score each team
output = pd.DataFrame(output).reset_index()
print(output.head())


# In[9]:

output.to_csv(os.getcwd()+ '\\Q3_Part_1_Output.csv')

