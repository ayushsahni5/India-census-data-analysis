#!/usr/bin/env python
# coding: utf-8

# ## Ratio of population speaking languages three or more to exactly two

# In[6]:


'''Note that ratio of population speaking three or more language to exactly two language is same as ratio of
column 'percent three' to column 'percent two'. '''


import pandas as pd

pd.options.mode.chained_assignment = None   #to hide settingwithcopy warning

#Here, I will use percent-india.csv file generated in ques1
ques4_df1=pd.read_csv('output files/percent-india.csv')


# $$\frac{(percent \quad three)}{(percent \quad two)}=\frac{\text{(who speak 3 or more)*100/total population}}{\text{(who speak excatly 2)*100/total population}}$$
# $$ $$
# $$=\frac{\text{who speak 3 or more}}{\text{who speak exactly 2}}$$

# In[7]:


#computing 3-or-more to exactly-2 language ratio
ques4_df1['3 to 2 ratio']=ques4_df1['percent-three']/ques4_df1['percent-two']
ques4_df1.sort_values(by=['3 to 2 ratio'],ascending=False,inplace=True)  # sorting in descending order by column '3 to 2 ratio'
ques4_df2=ques4_df1.tail(n=3)   #taking last 3 rows
ques4_df2.sort_values(by=['3 to 2 ratio'],inplace=True)
ques4_df2=ques4_df2[['state-code']]
ques4_df1=ques4_df1.head(n=3)   #taking first 3 rows
ques4_df1=ques4_df1[['state-code']]
ques4_df1=pd.merge(ques4_df1,ques4_df2,how='outer')
ques4_df1.to_csv('output files/3-to-2-ratio.csv',index=False)


# In[ ]:




