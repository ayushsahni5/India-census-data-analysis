#!/usr/bin/env python
# coding: utf-8

# # Analysis based on age-group of males and females

# In[30]:


import pandas as pd

age_wise_pop=pd.read_excel('Datasets/c-14.xls')

pd.options.mode.chained_assignment = None   #to hide settingwithcopy warning

#refining c-14 dataset
age_wise_pop=age_wise_pop.rename(columns={'C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ':'age-group','Unnamed: 1':'state-code','Unnamed: 6':'tot males','Unnamed: 7':'tot females'})
age_wise_pop=age_wise_pop[['state-code','age-group','tot males','tot females']]
age_wise_pop=age_wise_pop[(age_wise_pop['age-group']=='5-9')|(age_wise_pop['age-group']=='10-14')|(age_wise_pop['age-group']=='15-19')|(age_wise_pop['age-group']=='20-24')|(age_wise_pop['age-group']=='25-29')|(age_wise_pop['age-group']=='30-34')|(age_wise_pop['age-group']=='35-39')|(age_wise_pop['age-group']=='40-44')|(age_wise_pop['age-group']=='45-49')|(age_wise_pop['age-group']=='50-54')|(age_wise_pop['age-group']=='55-59')|(age_wise_pop['age-group']=='60-64')|(age_wise_pop['age-group']=='65-69')|(age_wise_pop['age-group']=='70-74')|(age_wise_pop['age-group']=='75-79')|(age_wise_pop['age-group']=='80+')]


#c-14 dataset contains age groups 30-34,35-39,40-44,...  whereas c-18 dataset contains age groups 30-49,50-69,70+  so I will merge age groups in c-14 to make it like c-18
#to make c-14 and c-18 similar, our only option is to merge ages in c-14. We cant break ages in c-18 according to c-14
my_df=pd.DataFrame()
k=0
while k<len(age_wise_pop):
       
    if (k%16)==5:   #this position is of 30-34 age group. From here onwards we have to perform 3 mergings
        
        #making 30-49 age group
        tot_males=age_wise_pop['tot males'].iloc[k]+age_wise_pop['tot males'].iloc[k+1]+age_wise_pop['tot males'].iloc[k+2]+age_wise_pop['tot males'].iloc[k+3]
        tot_females=age_wise_pop['tot females'].iloc[k]+age_wise_pop['tot females'].iloc[k+1]+age_wise_pop['tot females'].iloc[k+2]+age_wise_pop['tot females'].iloc[k+3]
        my_df=my_df.append({'state-code':age_wise_pop['state-code'].iloc[k],'age-group':'30-49','tot males':tot_males,'tot females':tot_females},ignore_index=True)
        k=k+4
        
        #making 50-69 age group
        tot_males=age_wise_pop['tot males'].iloc[k]+age_wise_pop['tot males'].iloc[k+1]+age_wise_pop['tot males'].iloc[k+2]+age_wise_pop['tot males'].iloc[k+3]
        tot_females=age_wise_pop['tot females'].iloc[k]+age_wise_pop['tot females'].iloc[k+1]+age_wise_pop['tot females'].iloc[k+2]+age_wise_pop['tot females'].iloc[k+3]
        my_df=my_df.append({'state-code':age_wise_pop['state-code'].iloc[k],'age-group':'50-69','tot males':tot_males,'tot females':tot_females},ignore_index=True)
        k=k+4
        
        #making 70+ age group
        tot_males=age_wise_pop['tot males'].iloc[k]+age_wise_pop['tot males'].iloc[k+1]+age_wise_pop['tot males'].iloc[k+2]
        tot_females=age_wise_pop['tot females'].iloc[k]+age_wise_pop['tot females'].iloc[k+1]+age_wise_pop['tot females'].iloc[k+2]
        my_df=my_df.append({'state-code':age_wise_pop['state-code'].iloc[k],'age-group':'70+','tot males':tot_males,'tot females':tot_females},ignore_index=True)
        k=k+3
        
    else:
        my_df=my_df.append(age_wise_pop.iloc[k])
        k=k+1
        
        
my_df=my_df[['state-code','age-group','tot males','tot females']]   #this  dataframe will be used later so we will not change it .


# ### Part-a  3 or more languages

# In[31]:


#loading c18 dataset
age_wise_3ormore=pd.read_excel('Datasets/c-18.xlsx')
age_wise_3ormore=age_wise_3ormore.rename(columns={'C-18 POPULATION BY BILINGUALISM, TRILINGUALISM, AGE AND SEX':'state-code','Unnamed: 3':'TRU', 'Unnamed: 4':'age-group','Unnamed: 9':'males speaking 3 or more','Unnamed: 10':'females speaking 3 or more'})
age_wise_3ormore=age_wise_3ormore[['state-code','TRU','age-group','males speaking 3 or more','females speaking 3 or more']]

#removing irrelevant rows from c-18 dataframe
age_wise_3ormore=age_wise_3ormore[(age_wise_3ormore['age-group']=='5-9')|(age_wise_3ormore['age-group']=='10-14')|(age_wise_3ormore['age-group']=='15-19')|(age_wise_3ormore['age-group']=='20-24')|(age_wise_3ormore['age-group']=='25-29')|(age_wise_3ormore['age-group']=='30-49')|(age_wise_3ormore['age-group']=='50-69')|(age_wise_3ormore['age-group']=='70+')]
age_wise_3ormore=age_wise_3ormore[(age_wise_3ormore['TRU']=='Total')]

#removing irrelevant columns from c-18
age_wise_3ormore=age_wise_3ormore[['state-code','age-group','males speaking 3 or more','females speaking 3 or more']]

my_df2=pd.merge(my_df,age_wise_3ormore)

#FOR MALES
my_df3=my_df2[['state-code','age-group']]
my_df3['ratio-males']=my_df2['males speaking 3 or more']/my_df2['tot males']
#finding max ratio males who speak 3 or more language for each state-code
idx = my_df3.groupby(['state-code'])['ratio-males'].transform(max) == my_df3['ratio-males']
my_df3=my_df3[idx]
my_df3.rename(columns={'age-group':'age-group-males'},inplace=True)


#FOR FEMALES
my_df4=my_df2[['state-code','age-group']]
my_df4['ratio-females']=my_df2['females speaking 3 or more']/my_df2['tot females']
#finding max ratio females who speak 3 or more language for each state-code
idx = my_df4.groupby(['state-code'])['ratio-females'].transform(max) == my_df4['ratio-females']
my_df4=my_df4[idx]
my_df4.rename(columns={'age-group':'age-group-females'},inplace=True)


# #### Creation of part-a output file

# In[32]:


my_df3=pd.merge(my_df3,my_df4)
my_df3.rename(columns={'state-code':'state/ut'},inplace=True)
my_df3.to_csv('output files/age-gender-a.csv',index=False)


# # 
# ### Part-b exactly 2 languages

# In[33]:


c18_df=pd.read_excel('Datasets/c-18.xlsx')
#C-18 dataframe column names
#'C-18 POPULATION BY BILINGUALISM, TRILINGUALISM, AGE AND SEX' denotes state code
#'Unnamed: 1' denotes district code
#'Unnamed: 2' denotes country/state/UT
#'Unnamed: 3' denotes Total/rural/urban 
#'Unnamed: 4' denotes Age-group(Total,5-9 age,10-14 age,...)
#'Unnamed: 5' denotes number of males+females who speak 2 or more language
#'Unnamed: 6' denotes number of males who speak 2 or more language
#'Unnamed: 7' denotes number of females who speak 2 or more language
#'Unnamed: 8' denotes number of males+females who speak 3 or more language
#'Unnamed: 9' denotes number of males who speak 3 or more language
#'Unnamed: 10' denotes number of females who speak 3 or more language
c18_df=c18_df[(c18_df['Unnamed: 3']=='Total') & (c18_df['Unnamed: 4']!='Total')& (c18_df['Unnamed: 4']!='Age not stated')]  #removing rural/urban rows. Also removing 'Total' age-group rows
c18_df=c18_df[['C-18 POPULATION BY BILINGUALISM, TRILINGUALISM, AGE AND SEX','Unnamed: 4','Unnamed: 6','Unnamed: 7','Unnamed: 9','Unnamed: 10']]
c18_df=c18_df.rename(columns={'C-18 POPULATION BY BILINGUALISM, TRILINGUALISM, AGE AND SEX':'state-code','Unnamed: 4':'age-group','Unnamed: 6':'males who speak 2 or more','Unnamed: 7':'females who speak 2 or more','Unnamed: 9':'males who speak 3 or more','Unnamed: 10':'females who speak 3 or more'})

c18_df=pd.merge(c18_df,my_df)  #merging is costly operation. If code takes more time to run then it can be replaced with append function.

#finding lingualism columns for males and females
c18_df['males who speak exactly 1']=c18_df['tot males']-c18_df['males who speak 2 or more']
c18_df['females who speak exactly 1']=c18_df['tot females']-c18_df['females who speak 2 or more']
c18_df['males who speak exactly 2']=c18_df['tot males']-c18_df['males who speak exactly 1']-c18_df['males who speak 3 or more']
c18_df['females who speak exactly 2']=c18_df['tot females']-c18_df['females who speak exactly 1']-c18_df['females who speak 3 or more']



new_df=c18_df[['state-code','age-group','males who speak exactly 2','tot males']]
new_df['ratio-males']=new_df['males who speak exactly 2']/new_df['tot males']

#for each state, finding highest ratio of males
idx = new_df.groupby(['state-code'])['ratio-males'].transform(max) == new_df['ratio-males']
new_df=new_df[idx]


new_df2=c18_df[['state-code','age-group','females who speak exactly 2','tot females']]
new_df2['ratio-females']=new_df2['females who speak exactly 2']/new_df2['tot females']

#for each state, finding the highest ratio of females
idx = new_df2.groupby(['state-code'])['ratio-females'].transform(max) == new_df2['ratio-females']
new_df2=new_df2[idx]


# ### Creation of part-b file

# In[34]:


new_df.rename(columns={'age-group':'age-group-males','state-code':'state/ut'},inplace=True)
new_df2.rename(columns={'age-group':'age-group-females','state-code':'state/ut'},inplace=True)
new_df=new_df[['state/ut','age-group-males','ratio-males']]
new_df2=new_df2[['state/ut','age-group-females','ratio-females']]
new_df=pd.merge(new_df,new_df2)
new_df.to_csv('output files/age-gender-b.csv',index=False)


# # 
# ## Part-c Exactly 1 language

# In[35]:


new_df=c18_df[['state-code','age-group','males who speak exactly 1','tot males']]
new_df['ratio-males']=new_df['males who speak exactly 1']/new_df['tot males']

#for each state, finding the highest ratio of males who speak exactly 1 language
idx = new_df.groupby(['state-code'])['ratio-males'].transform(max) == new_df['ratio-males']
new_df=new_df[idx]


new_df2=c18_df[['state-code','age-group','females who speak exactly 1','tot females']]
new_df2['ratio-females']=new_df2['females who speak exactly 1']/new_df2['tot females']

#for each state, finding the highest ratio of females who speak exactly 1 language
idx = new_df2.groupby(['state-code'])['ratio-females'].transform(max) == new_df2['ratio-females']
new_df2=new_df2[idx]


# ### Creation of part-c file

# In[36]:


new_df.rename(columns={'age-group':'age-group-males','state-code':'state/ut'},inplace=True)
new_df2.rename(columns={'age-group':'age-group-females','state-code':'state/ut'},inplace=True)
new_df=new_df[['state/ut','age-group-males','ratio-males']]
new_df2=new_df2[['state/ut','age-group-females','ratio-females']]
new_df=pd.merge(new_df,new_df2)
new_df.to_csv('output files/age-gender-c.csv',index=False)


# In[ ]:




