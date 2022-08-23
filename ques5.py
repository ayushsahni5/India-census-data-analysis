#!/usr/bin/env python
# coding: utf-8

# ### Refining C-14 dataset

# In[2]:


import pandas as pd

pd.options.mode.chained_assignment = None   #to hide settingwithcopy warning

age_wise_pop=pd.read_excel('Datasets/c-14.xls')
#refining c-14 dataset
age_wise_pop=age_wise_pop.rename(columns={'C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ':'age-group','Unnamed: 1':'state-code','Unnamed: 5':'tot people'})
age_wise_pop=age_wise_pop[['state-code','age-group','tot people']]
age_wise_pop=age_wise_pop[(age_wise_pop['age-group']=='5-9')|(age_wise_pop['age-group']=='10-14')|(age_wise_pop['age-group']=='15-19')|(age_wise_pop['age-group']=='20-24')|(age_wise_pop['age-group']=='25-29')|(age_wise_pop['age-group']=='30-34')|(age_wise_pop['age-group']=='35-39')|(age_wise_pop['age-group']=='40-44')|(age_wise_pop['age-group']=='45-49')|(age_wise_pop['age-group']=='50-54')|(age_wise_pop['age-group']=='55-59')|(age_wise_pop['age-group']=='60-64')|(age_wise_pop['age-group']=='65-69')|(age_wise_pop['age-group']=='70-74')|(age_wise_pop['age-group']=='75-79')|(age_wise_pop['age-group']=='80+')]


#MERGING AGE_GROUPS IN C_14: c-14 dataset contains age groups 30-34,35-39,40-44,...  whereas c-18 dataset contains age groups 30-49,50-69,70+  so I will merge age groups in c-14 to make it like c-18
#to make c-14 and c-18 similar, our only option is to merge ages in c-14. We cant break ages in c-18 according to c-14
my_df=pd.DataFrame()
k=0
while k<len(age_wise_pop):
       
    if (k%16)==5:   #this position is of 30-34 age group. From here onwards we have to perform 3 mergings
        
        #making 30-49 age group
        tot_pop=age_wise_pop['tot people'].iloc[k]+age_wise_pop['tot people'].iloc[k+1]+age_wise_pop['tot people'].iloc[k+2]+age_wise_pop['tot people'].iloc[k+3]
        my_df=my_df.append({'state-code':age_wise_pop['state-code'].iloc[k],'age-group':'30-49','tot people':tot_pop},ignore_index=True)
        k=k+4
        
        #making 50-69 age group
        tot_pop=age_wise_pop['tot people'].iloc[k]+age_wise_pop['tot people'].iloc[k+1]+age_wise_pop['tot people'].iloc[k+2]+age_wise_pop['tot people'].iloc[k+3]
        my_df=my_df.append({'state-code':age_wise_pop['state-code'].iloc[k],'age-group':'50-69','tot people':tot_pop},ignore_index=True)
        k=k+4
        
        #making 70+ age group
        tot_pop=age_wise_pop['tot people'].iloc[k]+age_wise_pop['tot people'].iloc[k+1]+age_wise_pop['tot people'].iloc[k+2]
        my_df=my_df.append({'state-code':age_wise_pop['state-code'].iloc[k],'age-group':'70+','tot people':tot_pop},ignore_index=True)
        k=k+3
        
    else:
        my_df=my_df.append(age_wise_pop.iloc[k])
        k=k+1
        
        
my_df=my_df[['state-code','age-group','tot people']]

#######################Now age groups have been merged according to c-18 census dataset##################



# ### Refining C-18 dataset

# In[3]:


age_wise_3ormore=pd.read_excel('Datasets/c-18.xlsx')
age_wise_3ormore=age_wise_3ormore.rename(columns={'C-18 POPULATION BY BILINGUALISM, TRILINGUALISM, AGE AND SEX':'state-code','Unnamed: 3':'TRU', 'Unnamed: 4':'age-group','Unnamed: 8':'people speaking 3 or more'})
age_wise_3ormore=age_wise_3ormore[['state-code','TRU','age-group','people speaking 3 or more']]

#removing irrelevant rows from c-18 dataframe
age_wise_3ormore=age_wise_3ormore[(age_wise_3ormore['age-group']=='5-9')|(age_wise_3ormore['age-group']=='10-14')|(age_wise_3ormore['age-group']=='15-19')|(age_wise_3ormore['age-group']=='20-24')|(age_wise_3ormore['age-group']=='25-29')|(age_wise_3ormore['age-group']=='30-49')|(age_wise_3ormore['age-group']=='50-69')|(age_wise_3ormore['age-group']=='70+')]
age_wise_3ormore=age_wise_3ormore[(age_wise_3ormore['TRU']=='Total')]

#removing irrelevant columns from c-18
age_wise_3ormore=age_wise_3ormore[['state-code','age-group','people speaking 3 or more']]


# ### Finding required ratio of people speaking 3 or more languages to total no of people in that age group

# In[4]:


my_df=pd.merge(my_df,age_wise_3ormore)
my_df['ratio']=my_df['people speaking 3 or more']/my_df['tot people']

#finding max ratio for each state-code
idx = my_df.groupby(['state-code'])['ratio'].transform(max) == my_df['ratio']
my_df=my_df[idx]
my_df['percentage']=my_df['ratio']*100


# In[5]:


#creating age-india.csv file
my_df=my_df[['state-code','age-group','percentage']]
my_df.rename(columns={'state-code':'state/ut'},inplace=True)
my_df.to_csv('output files/age-india.csv',index=False)


# In[ ]:




