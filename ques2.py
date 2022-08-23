#!/usr/bin/env python
# coding: utf-8

# ## Creating a dataframe suitable for calculating p value 

# In[7]:


import pandas as pd

pd.options.mode.chained_assignment = None   #to hide settingwithcopy warning

age_wise_pop=pd.read_excel('Datasets/c-14.xls')

#refining c-14 dataset. From c-14 dataset we will get total males and females in each state
age_wise_pop=age_wise_pop.rename(columns={'C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ':'age-group','Unnamed: 1':'state-code','Unnamed: 6':'tot males','Unnamed: 7':'tot females'})
age_wise_pop=age_wise_pop[['state-code','age-group','tot males','tot females']]
age_wise_pop=age_wise_pop[age_wise_pop['age-group']=='All ages']
age_wise_pop=age_wise_pop[['state-code','tot males','tot females']]



#C18 DATASET
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
c18_df=c18_df[c18_df['Unnamed: 3']=='Total']  #removing rural/urban rows. 
c18_df=c18_df[c18_df['Unnamed: 4']=='Total']  #keeping only 'Total' age-group rows
c18_df=c18_df[['C-18 POPULATION BY BILINGUALISM, TRILINGUALISM, AGE AND SEX','Unnamed: 4','Unnamed: 6','Unnamed: 7','Unnamed: 9','Unnamed: 10']]  #removing unwanted columns
c18_df=c18_df.rename(columns={'C-18 POPULATION BY BILINGUALISM, TRILINGUALISM, AGE AND SEX':'state-code','Unnamed: 4':'age-group','Unnamed: 6':'males who speak 2 or more','Unnamed: 7':'females who speak 2 or more','Unnamed: 9':'males who speak 3 or more','Unnamed: 10':'females who speak 3 or more'})

#Merging C-18 and C-14 dataframe
c18_df=pd.merge(c18_df,age_wise_pop)

#calculating number of males and females who speak exactly 1 and exactly two languages
c18_df['males who speak exactly 1']=c18_df['tot males']-c18_df['males who speak 2 or more']
c18_df['females who speak exactly 1']=c18_df['tot females']-c18_df['females who speak 2 or more']
c18_df['males who speak exactly 2']=c18_df['tot males']-c18_df['males who speak exactly 1']-c18_df['males who speak 3 or more']
c18_df['females who speak exactly 2']=c18_df['tot females']-c18_df['females who speak exactly 1']-c18_df['females who speak 3 or more']

#calculating male to female ratios for exactly one, exactly two and 3 or more languages
c18_df['m_to_f_1']=c18_df['males who speak exactly 1']/c18_df['females who speak exactly 1']
c18_df['m_to_f_2']=c18_df['males who speak exactly 2']/c18_df['females who speak exactly 2']
c18_df['m_to_f_3']=c18_df['males who speak 3 or more']/c18_df['females who speak 3 or more']
c18_df['m_to_f']=c18_df['tot males']/c18_df['tot females']


# ## Part-c  3 or more languages
# ### calculating p value

# In[8]:


from scipy.stats import ttest_ind
from scipy import stats
c18_df['p-value'] = c18_df.apply(lambda row: stats.ttest_1samp([row.m_to_f_1, row.m_to_f_2, row.m_to_f_3], popmean=row.m_to_f)[1], axis=1)


# ### Creation of part-a file

# In[9]:


parta_df=c18_df[['state-code','males who speak 3 or more','tot males','females who speak 3 or more','tot females','p-value']]
parta_df['male-percentage']=(parta_df['males who speak 3 or more']/parta_df['tot males'])*100
parta_df['female-percentage']=(parta_df['females who speak 3 or more']/parta_df['tot females'])*100
parta_df.rename(columns={'state-code':'state/ut'},inplace=True)
parta_df=parta_df[['state/ut','male-percentage','female-percentage','p-value']]
parta_df.rename(columns={'state/ut':'state-code'},inplace=True)
parta_df.to_csv('output files/gender-india-c.csv',index=False)


# ## Part-b  exactly 2 languages
# ### calculating p-value

# In[10]:


#the p-value will be same because arguments for p-value calculation are still the same


# ### creation of part-b file

# In[11]:


partb_df=c18_df[['state-code','males who speak exactly 2','tot males','females who speak exactly 2','tot females','p-value']]
partb_df['male-percentage']=(partb_df['males who speak exactly 2']/partb_df['tot males'])*100
partb_df['female-percentage']=(partb_df['females who speak exactly 2']/partb_df['tot females'])*100
partb_df.rename(columns={'state-code':'state/ut'},inplace=True)
partb_df=partb_df[['state/ut','male-percentage','female-percentage','p-value']]
partb_df.rename(columns={'state/ut':'state-code'},inplace=True)
partb_df.to_csv('output files/gender-india-b.csv',index=False)


# ## Part-a  exactly 1 language
# ### Creation of part-c file

# In[12]:


partc_df=c18_df[['state-code','males who speak exactly 1','tot males','females who speak exactly 1','tot females','p-value']]
partc_df['male-percentage']=(partc_df['males who speak exactly 1']/partc_df['tot males'])*100
partc_df['female-percentage']=(partc_df['females who speak exactly 1']/partc_df['tot females'])*100
partc_df.rename(columns={'state-code':'state/ut'},inplace=True)
partc_df=partc_df[['state/ut','male-percentage','female-percentage','p-value']]
partc_df.rename(columns={'state/ut':'state-code'},inplace=True)
partc_df.to_csv('output files/gender-india-a.csv',index=False)


# In[ ]:




