#!/usr/bin/env python
# coding: utf-8

# ## ques4-b

# In[1]:


'''Note that ratio of population speaking three or more language to exactly two language is same as ratio of
column 'percent three' to column 'percent two'. '''


import pandas as pd

pd.options.mode.chained_assignment = None   #to hide settingwithcopy warning

#Here, I will use percent-india.csv file generated in ques1
ques4_df1=pd.read_csv('output files/percent-india.csv')


# $$\frac{(percent \quad two)}{(percent \quad one)}=\frac{\text{(who speak exactly 2)*100/total population}}{\text{(who speak excatly 1)*100/total population}}$$
# $$ $$
# $$=\frac{\text{who speak exactly 2}}{\text{who speak exactly 1}}$$

# ## ratio of population speaking language exactly two to exactly one

# In[2]:


#Here I will do same thing as ques4-a but with columns percent-two and percent-one
ques4_df3=pd.read_csv('output files/percent-india.csv')
ques4_df3['2 to 1 ratio']=ques4_df3['percent-two']/ques4_df3['percent-one']
ques4_df3.sort_values(by=['2 to 1 ratio'],ascending=False,inplace=True)
ques4_df4=ques4_df3.tail(n=3)
ques4_df4.sort_values(by=['2 to 1 ratio'],inplace=True)
ques4_df4=ques4_df4[['state-code']]
ques4_df3=ques4_df3.head(n=3)
ques4_df3=ques4_df3[['state-code']]
ques4_df3=pd.merge(ques4_df3,ques4_df4,how='outer')
ques4_df3.to_csv('output files/2-to-1-ratio.csv',index=False) #column name for this ques is not mentioned in assignment pdf. So I am naming it 'state-code'


# In[ ]:




