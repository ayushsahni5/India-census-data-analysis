#!/usr/bin/env python
# coding: utf-8

# ## Percentage of population who speak one language, two language and three or more language

# In[3]:


'''Here we need number of people who speak (a)one language (b)two language (c)three or more language.
C-18 POPULATION BY BILINGUALISM, TRILINGUALISM, AGE AND SEX dataset will be used to find the such number of people
This dataset contains columns (1)Number speaking second language and (2)Number speaking third language. By
observation it has been found that these columns mean (1)Number of people speaking 2 or more languages and
(2)Number of people speaking 3 or more languages rather than (1) Number of people speaking exactly 2 languages
and (2)Number of people speaking exactly 3 languages. This is because, for state GOA, sum of these two columns
in C-18 dataset is 1867401 while total population of GOA according to 2011 census is only 1458545.'''

import pandas as pd

c18_df=pd.read_excel('Datasets/c-18.xlsx')
#After loading  c-18 dataset into pandas dataframe, the column names given to dataframe are 'Unnamed: 1', 'Unnamed: 2'
#and so on. For now, I will use these namings only. 
#For reader's reference, these are the dataframe column names:- 

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

c18_df=c18_df[(c18_df['Unnamed: 3']=='Total') & (c18_df['Unnamed: 4']=='Total')]  #removing rural/urban rows. Also removing different age-groups rows(keeping only total age-group rows)
c18_df=c18_df[['C-18 POPULATION BY BILINGUALISM, TRILINGUALISM, AGE AND SEX','Unnamed: 5','Unnamed: 8']]  #removing unwanted columns
c18_df=c18_df.rename(columns={'C-18 POPULATION BY BILINGUALISM, TRILINGUALISM, AGE AND SEX':'state-code','Unnamed: 5':'who speak 2 or more','Unnamed: 8':'who speak 3 or more'}) #renaming columns

#loading and refining 2011 population census
population_df=pd.read_excel('Datasets/india-census-2011.xlsx')
population_df=population_df[((population_df['Level']=='STATE')|(population_df['Level']=='India'))&(population_df['TRU']=='Total') ]  #loading state and its total population
population_df=population_df[['State','TOT_P']]
population_df['State'] = population_df['State'].apply(lambda x: '{0:0>2}'.format(x))  #without this leading zeroes will be removed by python
population_df.rename(columns={'State':'state-code'},inplace=True)

#doing this we get state-code, no of speakers of 2 or more language, no of speakers of 3 or more language and total population in one single dataframe
c18_df=pd.merge(population_df,c18_df)

#finding no of people who speak exactly one language
c18_df['who speak exactly 1']=c18_df['TOT_P']-c18_df['who speak 2 or more'] #exactly one=total-atleast two ...here I am assuming there are no person who speak zero language(if there were such person then, total - atleast two = exactly one + exactly zero)

#finding no of people who speak exactly two languages
c18_df['who speak exactly 2']=c18_df['TOT_P'] - (c18_df['who speak 3 or more'] + c18_df['who speak exactly 1'])


#upto this point, if we print and see c18_df and sum up no of people who speak 1,2 and 3 or more language, you will find it consistent with 2011 census data.
#Hence our initial assumption that c18 dataset columns mean (1)Number of people speaking 2 or more languages and
#(2)Number of people speaking 3 or more languages rather than (1) Number of people speaking exactly 2 languages
#and (2)Number of people speaking exactly 3 languages was correct.
c18_df['percent-one']=(c18_df['who speak exactly 1']/c18_df['TOT_P'])*100
c18_df['percent-two']=(c18_df['who speak exactly 2']/c18_df['TOT_P'])*100
c18_df['percent-three']=(c18_df['who speak 3 or more']/c18_df['TOT_P'])*100

c18_df=c18_df[['state-code','percent-one','percent-two','percent-three']]
c18_df.to_csv('output files/percent-india.csv',index=False)


# In[ ]:




