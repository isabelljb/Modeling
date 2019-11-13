#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Import packages
import numpy as np
import pandas as pd
#import dataset to dataframe
data = pd.read_excel("/Users/data.xlsx", sheet_name='input')
data.drop_duplicates()
data[data.DEFQTR > '2007-12-31']
data.head(5)
#Find out data types in data frame columns
print(data.dtypes)
#Modify the date data type
ts = pd.DatetimeIndex(data['ACTQTR'])
ts

#Summarize total charge off data by date
data.groupby(['ACTQTR'])['TotalNet'].sum()
data.groupby(['Segment', 'DEFQTR']).count()
data.groupby(['UniqueID','Segment']).size().reset_index().rename(columns={0:'count'})
data2= data.groupby(['Segment', 'DEFQTR'])['TotalNet'].sum()

#Alternative way to use group by function to aggregate data
pivot = data.pivot_table(index=['Segment', 'DEFQTR'], values=['TotalNet'], aggfunc='sum')
pivot['TotalNet']

#Sorting the dataset
type(data['QTRDIFF'])
data.sort_values('QTRDIFF')
data.groupby(['Segment', 'DEFQTR']).first().reset_index()

