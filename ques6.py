#!/usr/bin/env python
# coding: utf-8

# # Analysis of population based on literacy group

# In[4]:


'''literate w/o edu level is absent in c-19 so remove it
removing literate column because its finer subdivisions are present'''
import pandas as pd

pd.options.mode.chained_assignment = None   #to hide settingwithcopy warning


# ## Processing C-8 dataset

# In[5]:


#loading c8 dataset into dataframe
c8_df=pd.read_excel('Datasets/c-8.xlsx')

#keeoing only these : combined age group(rather than 5-9,10-14 ,etc) and total population(urban + rural combined) 
c8_df=c8_df[(c8_df['C-8  EDUCATIONAL LEVEL BY AGE AND SEX FOR POPULATION AGE 7 AND ABOVE - 2011']=='All ages')&(c8_df['Unnamed: 4']=='Total')]
#renaming columns
c8_df.rename(columns={'Unnamed: 1':'state/ut','Unnamed: 9':'Illiterate','Unnamed: 18':'Literate but below primary','Unnamed: 21':'Primary but below middle','Unnamed: 24':'Middle but below matric/secondary','Unnamed: 27':'Matric','Unnamed: 30':'Intermed','Unnamed: 33':'Non tech diploma','Unnamed: 36':'Tech diploma','Unnamed: 39':'Graduate and above'},inplace=True)
#keeing only relevant columns
c8_df=c8_df[['state/ut','Illiterate','Literate but below primary','Primary but below middle','Middle but below matric/secondary','Matric','Intermed','Non tech diploma','Tech diploma','Graduate and above']]

#MERGING and summing the columns 'matric' , 'intermediate', 'non-tech diploma', 'tech diploma' to make new column 'Matric/secondary but below graduate'
#I am doing this to make it consistent with C19 dataset
c8_df['Matric/Secondary but below graduate']=c8_df['Matric']+c8_df['Intermed']+c8_df['Non tech diploma']+c8_df['Tech diploma']
#filtering unwanted columns
c8_df=c8_df[['state/ut','Illiterate','Literate but below primary','Primary but below middle','Middle but below matric/secondary','Matric/Secondary but below graduate','Graduate and above']]

#changing the structure of dataframe table using python's melt function to make it easier to to merge with C19 dataframe
c8_df=c8_df.melt(id_vars=["state/ut"], var_name="edu level", value_name='total people')
c8_df=c8_df.sort_values(by=['state/ut']) #sorting by state/ut


# In[6]:


#loading C19 dataset
c19_df=pd.read_excel('Datasets/c-19.xlsx')
c19_df.rename(columns={'C-19 POPULATION BY BILINGUALISM, TRILINGUALISM, EDUCATIONAL LEVEL AND SEX':'state/ut','Unnamed: 3':'TRU','Unnamed: 4':'edu level','Unnamed: 8':'3 or more'},inplace=True)
c19_df=c19_df[['state/ut','TRU','edu level','3 or more']]
c19_df=c19_df.loc[6:,] #rows number 0 to 5 are useless
c19_df=c19_df[(c19_df['TRU']=='Total')&(c19_df['edu level']!='Total')]# keeping only total(rural+urban) and total education level
c19_df=c19_df[c19_df['edu level']!='Literate']  #removing literate rows
c19_df=c19_df[['state/ut','edu level','3 or more']]


# In[7]:


#mergin c8 and c19
merged_df=pd.merge(c8_df,c19_df)
merged_df['percentage']=(merged_df['3 or more']/merged_df['total people'])*100


# ### Finding literacy group for each state that has the highest percentage of people speaking three languages or more

# In[8]:


idx = merged_df.groupby(['state/ut'])['percentage'].transform(max) == merged_df['percentage']
merged_df=merged_df[idx]
merged_df=merged_df[['state/ut','edu level','percentage']]
merged_df.rename(columns={'edu level':'literacy-group'},inplace=True)

#Creation of output file
merged_df.to_csv('output files/literacy-india.csv',index=False)


# In[ ]:




