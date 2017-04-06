
# coding: utf-8

# In[1]:

import pandas as pd
import os
import re


# In[2]:

current_path =os.path.expanduser('~')
current_path =os.path.join(current_path,'Assignment 3')
current_path =os.path.join(current_path,'Data')


# In[3]:

df = pd.read_csv( current_path + '\\movies_awards.csv')   #read csv file


# In[4]:

df1= df['Awards']    # create new dataframe with only Awards column
df1 = pd.DataFrame(df1)  # convert series to Dataframe
df1 = df1.dropna()   # drop all the rows that have value NaN in Awards column
#df1.head(20)


# In[5]:

df1['Awards_won'] = df1['Awards'].apply(lambda x : (re.findall(r"(\d+) win", x))) # for each row find the number of wins 
df1['Awards_won'] = df1['Awards_won'].apply(lambda x : [0] if len(x)==0 else x)   # if string does not contain "win" set value to 0
df1['Awards_won'] = df1['Awards_won'].apply(lambda x : list(map(int,x))[0])       # convert array to int
#df1.head(10)


# In[6]:

df1['Awards_nominated'] = df1['Awards'].apply(lambda x : (re.findall(r"(\d+) nom", x)))
df1['Awards_nominated'] = df1['Awards_nominated'].apply(lambda x : [0] if len(x)==0 else x)
df1['Awards_nominated'] = df1['Awards_nominated'].apply(lambda x : list(map(int,x))[0])
#df1.head(30)


# In[7]:

df1['Prime_Awards_nominated'] = df1['Awards'].apply(lambda x : (re.findall(r"Nominated for (\d+) Prime", x)))
df1['Prime_Awards_nominated'] = df1['Prime_Awards_nominated'].apply(lambda x : [0] if len(x)==0 else x)
df1['Prime_Awards_nominated'] = df1['Prime_Awards_nominated'].apply(lambda x : list(map(int,x))[0])
df1['Awards_nominated'] = df1['Awards_nominated'] + df1['Prime_Awards_nominated']
#df1.head(30)


# In[8]:

df1['Oscar_Awards_nominated'] = df1['Awards'].apply(lambda x : (re.findall(r"Nominated for (\d+) Oscar", x)))
df1['Oscar_Awards_nominated'] = df1['Oscar_Awards_nominated'].apply(lambda x : [0] if len(x)==0 else x)
df1['Oscar_Awards_nominated'] = df1['Oscar_Awards_nominated'].apply(lambda x : list(map(int,x))[0])
df1['Awards_nominated'] = df1['Awards_nominated'] + df1['Oscar_Awards_nominated']
#df1.head(30)


# In[9]:

df1['Golden_Globe_Awards_nominated'] = df1['Awards'].apply(lambda x : (re.findall(r"Nominated for (\d+) Golden", x)))
df1['Golden_Globe_Awards_nominated'] = df1['Golden_Globe_Awards_nominated'].apply(lambda x : [0] if len(x)==0 else x)
df1['Golden_Globe_Awards_nominated'] = df1['Golden_Globe_Awards_nominated'].apply(lambda x : list(map(int,x))[0])
df1['Awards_nominated'] = df1['Awards_nominated'] + df1['Golden_Globe_Awards_nominated']
#df1.head(30)


# In[10]:

df1['BAFTA_Awards_nominated'] = df1['Awards'].apply(lambda x : (re.findall(r"Nominated for (\d+) BAFTA", x)))
df1['BAFTA_Awards_nominated'] = df1['BAFTA_Awards_nominated'].apply(lambda x : [0] if len(x)==0 else x)
df1['BAFTA_Awards_nominated'] = df1['BAFTA_Awards_nominated'].apply(lambda x : list(map(int,x))[0])
df1['Awards_nominated'] = df1['Awards_nominated'] + df1['BAFTA_Awards_nominated']
#df1.head(20)


# In[11]:

df1['Prime_Awards_won'] = df1['Awards'].apply(lambda x : (re.findall(r"Won (\d+) Prime", x)))
df1['Prime_Awards_won'] = df1['Prime_Awards_won'].apply(lambda x : [0] if len(x)==0 else x)
df1['Prime_Awards_won'] = df1['Prime_Awards_won'].apply(lambda x : list(map(int,x))[0])
df1['Awards_won'] = df1['Awards_won'] + df1['Prime_Awards_won']
#df1.head(20)


# In[12]:

df1['Oscar_Awards_won'] = df1['Awards'].apply(lambda x : (re.findall(r"Won (\d+) Oscar", x)))
df1['Oscar_Awards_won'] = df1['Oscar_Awards_won'].apply(lambda x : [0] if len(x)==0 else x)
df1['Oscar_Awards_won'] = df1['Oscar_Awards_won'].apply(lambda x : list(map(int,x))[0])
df1['Awards_won'] = df1['Awards_won'] + df1['Oscar_Awards_won']
#df1.head(20)


# In[13]:

df1['Golden_Globe_Awards_won'] = df1['Awards'].apply(lambda x : (re.findall(r"Won (\d+) Golden", x)))
df1['Golden_Globe_Awards_won'] = df1['Golden_Globe_Awards_won'].apply(lambda x : [0] if len(x)==0 else x)
df1['Golden_Globe_Awards_won'] = df1['Golden_Globe_Awards_won'].apply(lambda x : list(map(int,x))[0])
df1['Awards_won'] = df1['Awards_won'] + df1['Golden_Globe_Awards_won']
#df1.head(20)


# In[14]:

df1['BAFTA_Awards_won'] = df1['Awards'].apply(lambda x : (re.findall(r"Won (\d+) BAFTA", x)))
df1['BAFTA_Awards_won'] = df1['BAFTA_Awards_won'].apply(lambda x : [0] if len(x)==0 else x)
df1['BAFTA_Awards_won'] = df1['BAFTA_Awards_won'].apply(lambda x : list(map(int,x))[0])
df1['Awards_won'] = df1['Awards_won'] + df1['BAFTA_Awards_won']
#df1.head(50)


# In[15]:

output = df1.head()
print(output)


# In[16]:

df1.to_csv(os.getcwd()+ '\\Q4_Part_1_Output.csv', index = False)   # write to csv file

