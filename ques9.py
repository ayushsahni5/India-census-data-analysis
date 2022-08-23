#!/usr/bin/env python
# coding: utf-8

# # Analysis based on literacy group for males and females separately

# In[22]:


import pandas as pd

pd.options.mode.chained_assignment = None   #to hide settingwithcopy warning

#loading and refining c8 dataset
c8_df=pd.read_excel('Datasets/c-8.xlsx')
c8_df=c8_df[(c8_df['C-8  EDUCATIONAL LEVEL BY AGE AND SEX FOR POPULATION AGE 7 AND ABOVE - 2011']=='All ages')&(c8_df['Unnamed: 4']=='Total')]
c8_df.rename(columns={'Unnamed: 1':'state/ut','Unnamed: 10':'Illiterate males','Unnamed: 11':'Illiterate females','Unnamed: 19':'Literate but below primary males','Unnamed: 20':'Literate but below primary females','Unnamed: 22':'Primary but below middle males','Unnamed: 23':'Primary but below middle females','Unnamed: 25':'Middle but below matric/secondary males','Unnamed: 26':'Middle but below matric/secondary females','Unnamed: 28':'Matric males','Unnamed: 29':'Matric females','Unnamed: 31':'Intermed males','Unnamed: 32':'Intermed females','Unnamed: 34':'Non tech diploma males','Unnamed: 35':'Non tech diploma females','Unnamed: 37':'Tech diploma males','Unnamed: 38':'Tech diploma females','Unnamed: 40':'Graduate and above males','Unnamed: 41':'Graduate and above females'},inplace=True)
c8_df=c8_df[['state/ut','Illiterate males','Illiterate females','Literate but below primary males','Literate but below primary females','Primary but below middle males','Primary but below middle females','Middle but below matric/secondary males','Middle but below matric/secondary females','Matric males','Matric females','Intermed males','Intermed females','Non tech diploma males','Non tech diploma females','Tech diploma males','Tech diploma females','Graduate and above males','Graduate and above females']]

#MERGING and summing the columns 'matric males' , 'intermediate' males, 'non-tech diploma males', 'tech diploma males' to make new column 'Matric/secondary but below graduate males'
#I am doing this to make it consistent with C19 dataset
c8_df['Matric/Secondary but below graduate males']=c8_df['Matric males']+c8_df['Intermed males']+c8_df['Non tech diploma males']+c8_df['Tech diploma males']
#Doing the above for females also
c8_df['Matric/Secondary but below graduate females']=c8_df['Matric females']+c8_df['Intermed females']+c8_df['Non tech diploma females']+c8_df['Tech diploma females']

#keeping only relevant columns
c8_df=c8_df[['state/ut','Illiterate males','Illiterate females','Literate but below primary males','Literate but below primary females','Primary but below middle males','Primary but below middle females','Middle but below matric/secondary males','Middle but below matric/secondary females','Matric/Secondary but below graduate males','Matric/Secondary but below graduate females','Graduate and above males','Graduate and above females']]

#changing the strucure of c18 dataframe using python's melt function. This will be useful when we will merge c8 and c19
c8_df=c8_df.melt(id_vars=["state/ut"], var_name="edu level", value_name='tot')

c8_df=c8_df.sort_values(by=['state/ut','edu level'])  


# ### Making C8 dataset similar to C19 dataset (converting columns of C8 into rows)

# In[23]:


myl=list(c8_df['tot'])
list_males=[]
list_fem=[]
for i in range(len(myl)):
    if i%2==0:
        list_fem.append(myl[i])
    else:
        list_males.append(myl[i])
        
c8_df.replace(to_replace=' males',value='',regex=True,inplace=True)
c8_df.replace(to_replace=' females',value='',regex=True,inplace=True)
c8_df=c8_df.groupby(['state/ut','edu level']).sum()
c8_df=c8_df.reset_index()  #resetting index because groupby has been applied(Groupby changes how we access the indices)
c8_df=c8_df[['state/ut','edu level']]

#finding total males and females in each literacy groups and creating new columns for them
c8_df['males']=pd.DataFrame(list_males)
c8_df['females']=pd.DataFrame(list_fem)


# ### Processing C19 dataset

# In[24]:


c19_df=pd.read_excel('Datasets/c-19.xlsx')
c19_df.rename(columns={'C-19 POPULATION BY BILINGUALISM, TRILINGUALISM, EDUCATIONAL LEVEL AND SEX':'state/ut','Unnamed: 3':'TRU','Unnamed: 4':'edu level','Unnamed: 6':'2 or more males','Unnamed: 7':'2 or more females','Unnamed: 9':'3 or more males','Unnamed: 10':'3 or more females'},inplace=True)
c19_df=c19_df[['state/ut','TRU','edu level','2 or more males','2 or more females','3 or more males','3 or more females']]
c19_df=c19_df.loc[6:,]
c19_df=c19_df[(c19_df['TRU']=='Total')&(c19_df['edu level']!='Total')]
c19_df=c19_df[c19_df['edu level']!='Literate']
c19_df=c19_df[['state/ut','edu level','2 or more males','2 or more females','3 or more males','3 or more females']]


#bringing in a column of total males and females in each literacy group
c19_df=pd.merge(c19_df,c8_df)

#finnding number of males and females who speak exactly 1 language
c19_df['exactly 1 males']=c19_df['males']-c19_df['2 or more males']
c19_df['exactly 1 females']=c19_df['females']-c19_df['2 or more females']

#finding number of males and females speaking exactly 2 languages
c19_df['exactly 2 males']=c19_df['males']-c19_df['3 or more males']-c19_df['exactly 1 males']
c19_df['exactly 2 females']=c19_df['females']-c19_df['3 or more females']-c19_df['exactly 1 females']

c19_df=c19_df[['state/ut','edu level','exactly 1 males','exactly 1 females','exactly 2 males','exactly 2 females','3 or more males','3 or more females','males','females']]
#This modified c19_df will be used in parts a,b and c


# ## Part-a  3 or more

# In[25]:


parta_df1=c19_df[['state/ut','edu level','3 or more males','males']]
parta_df1['ratio-males']=parta_df1['3 or more males']/parta_df1['males']

#finding age group having max ratio-males
idx = parta_df1.groupby(['state/ut'])['ratio-males'].transform(max) == parta_df1['ratio-males']
parta_df1=parta_df1[idx]

parta_df1.rename(columns={'edu level':'literacy-group-males'},inplace=True)



parta_df2=c19_df[['state/ut','edu level','3 or more females','females']]
parta_df2['ratio-females']=parta_df2['3 or more females']/parta_df2['females']

#finding age group having max ratio-males
idx = parta_df2.groupby(['state/ut'])['ratio-females'].transform(max) == parta_df2['ratio-females']
parta_df2=parta_df2[idx]

parta_df2.rename(columns={'edu level':'literacy-group-females'},inplace=True)

parta_df1=pd.merge(parta_df1,parta_df2)
parta_df1=parta_df1[['state/ut','literacy-group-males','ratio-males','literacy-group-females','ratio-females']]


# ### Creation of output file

# In[26]:


parta_df1.to_csv('output files/literacy-gender-a.csv',index=False)


# # 
# ## Part-b  exactly 2

# In[27]:


partb_df1=c19_df[['state/ut','edu level','exactly 2 males','males']]
partb_df1['ratio-males']=partb_df1['exactly 2 males']/partb_df1['males']

#finding age group having max ratio-males
idx = partb_df1.groupby(['state/ut'])['ratio-males'].transform(max) == partb_df1['ratio-males']
partb_df1=partb_df1[idx]

partb_df1.rename(columns={'edu level':'literacy-group-males'},inplace=True)



partb_df2=c19_df[['state/ut','edu level','exactly 2 females','females']]
partb_df2['ratio-females']=partb_df2['exactly 2 females']/partb_df2['females']

#finding age group having max ratio-males
idx = partb_df2.groupby(['state/ut'])['ratio-females'].transform(max) == partb_df2['ratio-females']
partb_df2=partb_df2[idx]

partb_df2.rename(columns={'edu level':'literacy-group-females'},inplace=True)

partb_df1=pd.merge(partb_df1,partb_df2)
partb_df1=partb_df1[['state/ut','literacy-group-males','ratio-males','literacy-group-females','ratio-females']]


# ### Creation of output file

# In[28]:


partb_df1.to_csv('output files/literacy-gender-b.csv',index=False)


# # 
# ## Part-c exactly 1

# In[29]:


partc_df1=c19_df[['state/ut','edu level','exactly 1 males','males']]
partc_df1['ratio-males']=partc_df1['exactly 1 males']/partc_df1['males']

#finding age group having max ratio-males
idx = partc_df1.groupby(['state/ut'])['ratio-males'].transform(max) == partc_df1['ratio-males']
partc_df1=partc_df1[idx]

partc_df1.rename(columns={'edu level':'literacy-group-males'},inplace=True)



partc_df2=c19_df[['state/ut','edu level','exactly 1 females','females']]
partc_df2['ratio-females']=partc_df2['exactly 1 females']/partc_df2['females']

#finding age group having max ratio-males
idx = partc_df2.groupby(['state/ut'])['ratio-females'].transform(max) == partc_df2['ratio-females']
partc_df2=partc_df2[idx]

partc_df2.rename(columns={'edu level':'literacy-group-females'},inplace=True)

partc_df1=pd.merge(partc_df1,partc_df2)
partc_df1=partc_df1[['state/ut','literacy-group-males','ratio-males','literacy-group-females','ratio-females']]


# ### Creation of output file

# In[30]:


partc_df1.to_csv('output files/literacy-gender-c.csv',index=False)


# In[ ]:




