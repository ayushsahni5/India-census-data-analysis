#!/usr/bin/env python
# coding: utf-8

# ## Analysis of urban and rural population who speak exactly 1, exactly 2 and 3 or more languages

# In[6]:


import pandas as pd

pd.options.mode.chained_assignment = None   #to hide settingwithcopy warning

#loading c18 dataset
c18_df=pd.read_excel('Datasets/c-18.xlsx')

#rural dataframe
rural_df=c18_df[(c18_df['Unnamed: 3']=='Rural') & (c18_df['Unnamed: 4']=='Total')]
rural_df.rename(columns={'C-18 POPULATION BY BILINGUALISM, TRILINGUALISM, AGE AND SEX':'state/ut','Unnamed: 5':'2 or more rural','Unnamed: 8':'3 or more rural'},inplace=True)
rural_df=rural_df[['state/ut','2 or more rural','3 or more rural']]

#urban dataframe
urban_df=c18_df[(c18_df['Unnamed: 3']=='Urban') & (c18_df['Unnamed: 4']=='Total')]
urban_df.rename(columns={'C-18 POPULATION BY BILINGUALISM, TRILINGUALISM, AGE AND SEX':'state/ut','Unnamed: 5':'2 or more urban','Unnamed: 8':'3 or more urban'},inplace=True)
urban_df=urban_df[['state/ut','2 or more urban','3 or more urban']]

#combining rural and urban data in separate columns
c18_df=pd.merge(rural_df,urban_df)

#free memory occupied by useless dataframes
temp_list=[urban_df,rural_df]
del temp_list


#finding rural and urban total population state wise
c14_df=pd.read_excel('Datasets/c-14.xls')
c14_df.rename(columns={'Unnamed: 1':'state/ut','C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ':'age-group','Unnamed: 8':'total rural','Unnamed: 11':'total urban'},inplace=True)
c14_df=c14_df[c14_df['age-group']=='All ages']
c14_df=c14_df[['state/ut','total rural','total urban']]




#creating a dataframe which will have every required column
c18_df=pd.merge(c18_df,c14_df)
c18_df['exactly 1 rural']=c18_df['total rural']-c18_df['2 or more rural']
c18_df['exactly 2 rural']=c18_df['total rural']-c18_df['3 or more rural']-c18_df['exactly 1 rural']
c18_df['exactly 1 urban']=c18_df['total urban']-c18_df['2 or more urban']
c18_df['exactly 2 urban']=c18_df['total urban']-c18_df['3 or more urban']-c18_df['exactly 1 urban']

c18_df['u_to_r_1']=c18_df['exactly 1 urban']/c18_df['exactly 1 rural']
c18_df['u_to_r_2']=c18_df['exactly 2 urban']/c18_df['exactly 2 rural']
c18_df['u_to_r_3']=c18_df['3 or more urban']/c18_df['3 or more rural']
c18_df['u_to_r']=c18_df['total urban']/c18_df['total rural']


# 
# ### p-value calculation

# In[7]:



#note that p value will be same in all parts a,b and c because the arguments to calculate p-value will be same in all the parts
from scipy.stats import ttest_ind
from scipy import stats
c18_df['p-value'] = c18_df.apply(lambda row: stats.ttest_1samp([row.u_to_r_1, row.u_to_r_2, row.u_to_r_3], popmean=row.u_to_r)[1], axis=1)


# ## Part-c  3 or more languages

# In[8]:


#creation of output file
parta_df=c18_df[['state/ut','p-value']]
parta_df['urban-percentage']=(c18_df['3 or more urban']/c18_df['total urban'])*100
parta_df['rural-percentage']=(c18_df['3 or more rural']/c18_df['total rural'])*100
parta_df=parta_df[['state/ut','urban-percentage','rural-percentage','p-value']]
parta_df.rename(columns={'state/ut':'state-code'},inplace=True)
parta_df.to_csv('output files/geography-india-c.csv',index=False)


# ## Part-b  exactly 2 languages

# In[9]:


#creation of output file
partb_df=c18_df[['state/ut','p-value']]
partb_df['urban-percentage']=(c18_df['exactly 2 urban']/c18_df['total urban'])*100
partb_df['rural-percentage']=(c18_df['exactly 2 rural']/c18_df['total rural'])*100
partb_df=partb_df[['state/ut','urban-percentage','rural-percentage','p-value']]
partb_df.rename(columns={'state/ut':'state-code'},inplace=True)
partb_df.to_csv('output files/geography-india-b.csv',index=False)


# ## Part-a exactly 1 language

# In[10]:


#creation of output file
partc_df=c18_df[['state/ut','p-value']]
partc_df['urban-percentage']=(c18_df['exactly 1 urban']/c18_df['total urban'])*100
partc_df['rural-percentage']=(c18_df['exactly 1 rural']/c18_df['total rural'])*100
partc_df=partc_df[['state/ut','urban-percentage','rural-percentage','p-value']]
partc_df.rename(columns={'state/ut':'state-code'},inplace=True)
partc_df.to_csv('output files/geography-india-a.csv',index=False)


# In[ ]:




