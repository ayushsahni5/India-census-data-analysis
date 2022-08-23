#!/usr/bin/env python
# coding: utf-8

# In[1]:


#all libraries will be imported in this block
import numpy as np
import pandas as pd

pd.options.mode.chained_assignment = None   #to hide settingwithcopy warning
####################################################


# # Part-a  Using only Mother tongue column

# #### A test code to find constitution of c-17 dataframe that we are going to use

# In[2]:


'''NOTE: In ques it has been asked to use Mother tongue. Though in C17 dataset it has not been explicitly mentioned
that the column 'Total speaker of language' is mother tongue but after cross checking it with C16 dataset(there it
has been explicitly mentioned column name is mother tongue) i found that no. of people is same in both of them for 
those columns. Hence C17 dataset column 'Total speaker of language' is the mother tongue language. So, here
i will be using C17 dataset only'''

test_df=pd.read_excel('Datasets/north/c-17-jammu & kashmir.XLSX')

'''The dataframe columns are named as Unnamed:1,Unnamed:2,... .By cross check I found that the column having language 
name is "Unnamed: 3" and the number of speakers of that language is present in the next column "Unnamed: 4" in 
the same row number 5.'''
# test_df['Unnamed: 3'].iloc[5] ---> this command gives output "ASSAMESE"  and the next column in same row gives 8340
test_df=test_df[['Unnamed: 3','Unnamed: 4']]   

'''now I have filtered this dataframe. It now has column1:language-name and column2:number-of-people-who-speak-that-language.
I will now do this for each state/UT and sum up the number of speakers of every language in each region(NORTH,SOUTH,WEST,EAST,
 NORTH-EAST,CENTRAL)'''
test_df=test_df   #no use of this line. Only used to hide previous comment being shown in output while running script
####################################################


# ## Processing actual data

# ### North Zone

# In[3]:


'''Jammu & Kashmir'''
my_df=pd.read_excel('Datasets/north/c-17-jammu & kashmir.XLSX')
my_df=my_df[['Unnamed: 3','Unnamed: 4']]

#performing union operation of mother tongue, 2nd lang and 3rd lang column
my_df=my_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})


my_df=my_df.dropna()   #remove NaN rows
my_df=my_df.loc[5: ,]  #remove useless rows 
#now this JK dataframe has languages and number of people who speak that language

#Now I will make a dictionary so that searching for certain language will be quicker while summing up number of speakers of certain language in a region
JK_dict=dict(zip(my_df['language-name'] , my_df['speakers']))

#Now, I am going to do this for every state and UT
'''Punjab'''
my_df=pd.read_excel('Datasets/north/c-17-punjab.XLSX')
my_df=my_df[['Unnamed: 3','Unnamed: 4']]
my_df=my_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
my_df=my_df.dropna()   #remove NaN rows
my_df=my_df.loc[5: ,]  #remove useless rows 
PN_dict=dict(zip(my_df['language-name'] , my_df['speakers']))

'''Himachal pradesh'''
my_df=pd.read_excel('Datasets/north/c-17-himachal pradesh.XLSX')
my_df=my_df[['Unnamed: 3','Unnamed: 4']]
my_df=my_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
my_df=my_df.dropna()   #remove NaN rows
my_df=my_df.loc[5: ,]  #remove useless rows 
HP_dict=dict(zip(my_df['language-name'] , my_df['speakers']))

'''Haryana'''
my_df=pd.read_excel('Datasets/north/c-17-haryana.XLSX')
my_df=my_df[['Unnamed: 3','Unnamed: 4']]
my_df=my_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
my_df=my_df.dropna()   #remove NaN rows
my_df=my_df.loc[5: ,]  #remove useless rows 
HR_dict=dict(zip(my_df['language-name'] , my_df['speakers']))

'''Uttarakhand'''
my_df=pd.read_excel('Datasets/north/c-17-uttarakhand.XLSX')
my_df=my_df[['Unnamed: 3','Unnamed: 4']]
my_df=my_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
my_df=my_df.dropna()   #remove NaN rows
my_df=my_df.loc[5: ,]  #remove useless rows 
UK_dict=dict(zip(my_df['language-name'] , my_df['speakers']))


'''Delhi'''
my_df=pd.read_excel('Datasets/north/c-17-delhi.XLSX')
my_df=my_df[['Unnamed: 3','Unnamed: 4']]
my_df=my_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
my_df=my_df.dropna()   #remove NaN rows
my_df=my_df.loc[5: ,]  #remove useless rows 
DL_dict=dict(zip(my_df['language-name'] , my_df['speakers']))


'''Chandigarh'''
my_df=pd.read_excel('Datasets/north/c-17-chandigarh.XLSX')
my_df=my_df[['Unnamed: 3','Unnamed: 4']]
my_df=my_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
my_df=my_df.dropna()   #remove NaN rows
my_df=my_df.loc[5: ,]  #remove useless rows 
CN_dict=dict(zip(my_df['language-name'] , my_df['speakers']))



# ### Creation of north_df which stores all languages spoken in this region with their respective number of speakers 

# In[4]:


#making a dataframe from each dictionary
north_df1=pd.DataFrame(CN_dict.items(),columns=['language','speakers'])
north_df2=pd.DataFrame(DL_dict.items(),columns=['language','speakers'])
north_df3=pd.DataFrame(UK_dict.items(),columns=['language','speakers'])
north_df4=pd.DataFrame(HR_dict.items(),columns=['language','speakers'])
north_df5=pd.DataFrame(HP_dict.items(),columns=['language','speakers'])
north_df6=pd.DataFrame(PN_dict.items(),columns=['language','speakers'])
north_df7=pd.DataFrame(JK_dict.items(),columns=['language','speakers'])

#taking union of those dataframes
north_df=pd.merge(north_df1,north_df2,how='outer')
north_df=pd.merge(north_df,north_df3,how='outer')
north_df=pd.merge(north_df,north_df4,how='outer')
north_df=pd.merge(north_df,north_df5,how='outer')
north_df=pd.merge(north_df,north_df6,how='outer')
north_df=pd.merge(north_df,north_df7,how='outer')

'''After taking union there are multiple rows having language 'ASSAMESE'(similarly other languages also are present multiple times).
And this north_df contains data from all the regions.So if I group it on basis of language column and find sum of
'speakers' column within each group , I will get the total number of people who speak that language in whole region'''
north_df=north_df.groupby(['language']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal if we store and re-load dataframe again
north_df.to_csv('Datasets/north/north-df.csv')  #storing dataframe
north_df=pd.read_csv('Datasets/north/north-df.csv')  #reloading the dataframe
north_df=north_df.sort_values(by='speakers',ascending=False).head(30)  #taking only top three rows


        #north_df[north_df['language']=='HINDI ']-->for cross checking whether my code gives correct number of hindi speakers    #It has been found that the string 'HINDI' is not present in the census but rather it is 'HINDI ' i.e. a 'space' at end. There are other such languages also.


# ### West Zone

# In[5]:


'''Rajasthan'''
RJ_df=pd.read_excel('Datasets/west/c-17-rajasthan.XLSX')
RJ_df=RJ_df[['Unnamed: 3','Unnamed: 4']]
RJ_df=RJ_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
RJ_df=RJ_df.dropna()   #remove NaN rows
RJ_df=RJ_df.loc[5: ,]  #remove useless rows 
RJ_dict=dict(zip(RJ_df['language-name'] , RJ_df['speakers']))


'''Gujarat'''
GJ_df=pd.read_excel('Datasets/west/c-17-gujarat.XLSX')
GJ_df=GJ_df[['Unnamed: 3','Unnamed: 4']]
GJ_df=GJ_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
GJ_df=GJ_df.dropna()   #remove NaN rows
GJ_df=GJ_df.loc[5: ,]  #remove useless rows 
GJ_dict=dict(zip(GJ_df['language-name'] , GJ_df['speakers']))

'''Maharashtra'''
MH_df=pd.read_excel('Datasets/west/c-17-maharashtra.XLSX')
MH_df=MH_df[['Unnamed: 3','Unnamed: 4']]
MH_df=MH_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
MH_df=MH_df.dropna()   #remove NaN rows
MH_df=MH_df.loc[5: ,]  #remove useless rows 
MH_dict=dict(zip(MH_df['language-name'] , MH_df['speakers']))

'''Goa'''
GA_df=pd.read_excel('Datasets/west/c-17-goa.XLSX')
GA_df=GA_df[['Unnamed: 3','Unnamed: 4']]
GA_df=GA_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
GA_df=GA_df.dropna()   #remove NaN rows
GA_df=GA_df.loc[5: ,]  #remove useless rows 
GA_dict=dict(zip(GA_df['language-name'] , GA_df['speakers']))

'''Dadra & Nagar Haveli'''
DNH_df=pd.read_excel('Datasets/west/c-17-dadra & nagar haveli.XLSX')
DNH_df=DNH_df[['Unnamed: 3','Unnamed: 4']]
DNH_df=DNH_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
DNH_df=DNH_df.dropna()   #remove NaN rows
DNH_df=DNH_df.loc[5: ,]  #remove useless rows 
DNH_dict=dict(zip(DNH_df['language-name'] , DNH_df['speakers']))

'''Daman & Diu'''
DND_df=pd.read_excel('Datasets/west/c-17-daman & diu.XLSX')
DND_df=DND_df[['Unnamed: 3','Unnamed: 4']]
DND_df=DND_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
DND_df=DND_df.dropna()   #remove NaN rows
DND_df=DND_df.loc[5: ,]  #remove useless rows 
DND_dict=dict(zip(DND_df['language-name'] , DND_df['speakers']))


# ### Creation of west_df which stores all languages spoken in this region with their respective number of speakers

# In[6]:


#making a dataframe from each dictionary
west_df1=pd.DataFrame(RJ_dict.items(),columns=['language','speakers'])
west_df2=pd.DataFrame(GJ_dict.items(),columns=['language','speakers'])
west_df3=pd.DataFrame(MH_dict.items(),columns=['language','speakers'])
west_df4=pd.DataFrame(GA_dict.items(),columns=['language','speakers'])
west_df5=pd.DataFrame(DNH_dict.items(),columns=['language','speakers'])
west_df6=pd.DataFrame(DND_dict.items(),columns=['language','speakers'])


#taking union of those dataframes
west_df=pd.merge(west_df1,west_df2,how='outer')
west_df=pd.merge(west_df,west_df3,how='outer')
west_df=pd.merge(west_df,west_df4,how='outer')
west_df=pd.merge(west_df,west_df5,how='outer')
west_df=pd.merge(west_df,west_df6,how='outer')


'''After taking union there are multiple rows having language 'ASSAMESE'(similarly other languages also are present multiple times).
And this west_df contains data from all the regions.So if I group it on basis of language column and find sum of
'speakers' column within each group , I will get the total number of people who speak that language in whole region'''
west_df=west_df.groupby(['language']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal if we store and re-load dataframe again
west_df.to_csv('Datasets/west/west-df.csv')  #storing dataframe
west_df=pd.read_csv('Datasets/west/west-df.csv')  #reloading the dataframe

west_df=west_df.sort_values(by='speakers',ascending=False).head(3)  #taking only top three rows


# ### Central Zone

# In[7]:


'''Madhya Pradesh'''
MP_df=pd.read_excel('Datasets/central/c-17-madhya pradesh.XLSX')
MP_df=MP_df[['Unnamed: 3','Unnamed: 4']]
MP_df=MP_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
MP_df=MP_df.dropna()   #remove NaN rows
MP_df=MP_df.loc[5: ,]  #remove useless rows 
MP_dict=dict(zip(MP_df['language-name'] , MP_df['speakers']))

'''Uttar Pradesh'''
UP_df=pd.read_excel('Datasets/central/c-17-uttar pradesh.XLSX')
UP_df=UP_df[['Unnamed: 3','Unnamed: 4']]
UP_df=UP_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
UP_df=UP_df.dropna()   #remove NaN rows
UP_df=UP_df.loc[5: ,]  #remove useless rows 
UP_dict=dict(zip(UP_df['language-name'] , UP_df['speakers']))

'''Chhattisgarh'''
CG_df=pd.read_excel('Datasets/central/c-17-chhattisgarh.XLSX')
CG_df=CG_df[['Unnamed: 3','Unnamed: 4']]
CG_df=CG_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
CG_df=CG_df.dropna()   #remove NaN rows
CG_df=CG_df.loc[5: ,]  #remove useless rows 
CG_dict=dict(zip(CG_df['language-name'] , CG_df['speakers']))


# ### Creation of central_df which stores all languages spoken in this region with their respective number of speakers

# In[8]:


#making a dataframe from each dictionary
central_df1=pd.DataFrame(MP_dict.items(),columns=['language','speakers'])
central_df2=pd.DataFrame(UP_dict.items(),columns=['language','speakers'])
central_df3=pd.DataFrame(CG_dict.items(),columns=['language','speakers'])



#taking union of those dataframes
central_df=pd.merge(central_df1,central_df2,how='outer')
central_df=pd.merge(central_df,central_df3,how='outer')



'''After taking union there are multiple rows having language 'ASSAMESE'(similarly other languages also are present multiple times).
And this central_df contains data from all the regions.So if I group it on basis of language column and find sum of
'speakers' column within each group , I will get the total number of people who speak that language in whole region'''
central_df=central_df.groupby(['language']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal if we store and re-load dataframe again
central_df.to_csv('Datasets/central/central-df.csv')  #storing dataframe
central_df=pd.read_csv('Datasets/central/central-df.csv')  #reloading the dataframe

central_df=central_df.sort_values(by='speakers',ascending=False).head(3)  #taking only top three rows


# ### East Zone

# In[9]:


'''Bihar'''
BH_df=pd.read_excel('Datasets/east/c-17-bihar.XLSX')
BH_df=BH_df[['Unnamed: 3','Unnamed: 4']]
BH_df=BH_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
BH_df=BH_df.dropna()   #remove NaN rows
BH_df=BH_df.loc[5: ,]  #remove useless rows 
BH_dict=dict(zip(BH_df['language-name'] , BH_df['speakers']))

'''West Bengal'''
WB_df=pd.read_excel('Datasets/east/c-17-west bengal.XLSX')
WB_df=WB_df[['Unnamed: 3','Unnamed: 4']]
WB_df=WB_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
WB_df=WB_df.dropna()   #remove NaN rows
WB_df=WB_df.loc[5: ,]  #remove useless rows 
WB_dict=dict(zip(WB_df['language-name'] , WB_df['speakers']))

'''Odisha'''
#In census data the spelling is odisha and its actual code is OD but since in assignment question it is written OR so I will write its code as OR but spelling I will use Odisha 
OR_df=pd.read_excel('Datasets/east/c-17-odisha.XLSX')
OR_df=OR_df[['Unnamed: 3','Unnamed: 4']]
OR_df=OR_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
OR_df=OR_df.dropna()   #remove NaN rows
OR_df=OR_df.loc[5: ,]  #remove useless rows 
OR_dict=dict(zip(OR_df['language-name'] , OR_df['speakers']))

'''Jharkhand'''
JH_df=pd.read_excel('Datasets/east/c-17-jharkhand.XLSX')
JH_df=JH_df[['Unnamed: 3','Unnamed: 4']]
JH_df=JH_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
JH_df=JH_df.dropna()   #remove NaN rows
JH_df=JH_df.loc[5: ,]  #remove useless rows 
JH_dict=dict(zip(JH_df['language-name'] , JH_df['speakers']))


# ### Creation of east_df which stores all languages spoken in this region with their respective number of speakers

# In[10]:


#making a dataframe from each dictionary
east_df1=pd.DataFrame(BH_dict.items(),columns=['language','speakers'])
east_df2=pd.DataFrame(WB_dict.items(),columns=['language','speakers'])
east_df3=pd.DataFrame(OR_dict.items(),columns=['language','speakers'])
east_df4=pd.DataFrame(JH_dict.items(),columns=['language','speakers'])


#taking union of those dataframes
east_df=pd.merge(east_df1,east_df2,how='outer')
east_df=pd.merge(east_df,east_df3,how='outer')
east_df=pd.merge(east_df,east_df4,how='outer')


'''After taking union there are multiple rows having language 'ASSAMESE'(similarly other languages also are present multiple times).
And this east_df contains data from all the regions.So if I group it on basis of language column and find sum of
'speakers' column within each group , I will get the total number of people who speak that language in whole region'''
east_df=east_df.groupby(['language']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal if we store and re-load dataframe again
east_df.to_csv('Datasets/east/east-df.csv')  #storing dataframe
east_df=pd.read_csv('Datasets/east/east-df.csv')  #reloading the dataframe

east_df=east_df.sort_values(by='speakers',ascending=False).head(3)  #taking only top three rows


# ### South Zone

# In[11]:


'''Karnataka'''
KA_df=pd.read_excel('Datasets/south/c-17-karnataka.XLSX')
KA_df=KA_df[['Unnamed: 3','Unnamed: 4']]
KA_df=KA_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
KA_df=KA_df.dropna()   #remove NaN rows
KA_df=KA_df.loc[5: ,]  #remove useless rows 
KA_dict=dict(zip(KA_df['language-name'] , KA_df['speakers']))

'''Andhra Pradesh'''
AP_df=pd.read_excel('Datasets/south/c-17-andhra pradesh.XLSX')
AP_df=AP_df[['Unnamed: 3','Unnamed: 4']]
AP_df=AP_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
AP_df=AP_df.dropna()   #remove NaN rows
AP_df=AP_df.loc[5: ,]  #remove useless rows 
AP_dict=dict(zip(AP_df['language-name'] , AP_df['speakers']))

'''Tamil Nadu'''
TN_df=pd.read_excel('Datasets/south/c-17-tamil nadu.XLSX')
TN_df=TN_df[['Unnamed: 3','Unnamed: 4']]
TN_df=TN_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
TN_df=TN_df.dropna()   #remove NaN rows
TN_df=TN_df.loc[5: ,]  #remove useless rows 
TN_dict=dict(zip(TN_df['language-name'] , TN_df['speakers']))

'''Kerala'''
KL_df=pd.read_excel('Datasets/south/c-17-kerala.XLSX')
KL_df=KL_df[['Unnamed: 3','Unnamed: 4']]
KL_df=KL_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
KL_df=KL_df.dropna()   #remove NaN rows
KL_df=KL_df.loc[5: ,]  #remove useless rows 
KL_dict=dict(zip(KL_df['language-name'] , KL_df['speakers']))

'''Lakshadweep'''
LD_df=pd.read_excel('Datasets/south/c-17-lakshadweep.XLSX')
LD_df=LD_df[['Unnamed: 3','Unnamed: 4']]
LD_df=LD_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
LD_df=LD_df.dropna()   #remove NaN rows
LD_df=LD_df.loc[5: ,]  #remove useless rows 
LD_dict=dict(zip(LD_df['language-name'] , LD_df['speakers']))

'''Puducherry'''
PY_df=pd.read_excel('Datasets/south/c-17-puducherry.XLSX')
PY_df=PY_df[['Unnamed: 3','Unnamed: 4']]
PY_df=PY_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
PY_df=PY_df.dropna()   #remove NaN rows
PY_df=PY_df.loc[5: ,]  #remove useless rows 
PY_dict=dict(zip(PY_df['language-name'] , PY_df['speakers']))


# ### Creation of south_df which stores all languages spoken in this region with their respective number of speakers

# In[12]:


#making a dataframe from each dictionary
south_df1=pd.DataFrame(KA_dict.items(),columns=['language','speakers'])
south_df2=pd.DataFrame(AP_dict.items(),columns=['language','speakers'])
south_df3=pd.DataFrame(TN_dict.items(),columns=['language','speakers'])
south_df4=pd.DataFrame(KL_dict.items(),columns=['language','speakers'])
south_df5=pd.DataFrame(PY_dict.items(),columns=['language','speakers'])
south_df6=pd.DataFrame(LD_dict.items(),columns=['language','speakers'])


#taking union of those dataframes
south_df=pd.merge(south_df1,south_df2,how='outer')
south_df=pd.merge(south_df,south_df3,how='outer')
south_df=pd.merge(south_df,south_df4,how='outer')
south_df=pd.merge(south_df,south_df5,how='outer')
south_df=pd.merge(south_df,south_df6,how='outer')


'''After taking union there are multiple rows having language 'ASSAMESE'(similarly other languages also are present multiple times).
And this south_df contains data from all the regions.So if I group it on basis of language column and find sum of
'speakers' column within each group , I will get the total number of people who speak that language in whole region'''
south_df=south_df.groupby(['language']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal if we store and re-load dataframe again
south_df.to_csv('Datasets/south/south-df.csv')  #storing dataframe
south_df=pd.read_csv('Datasets/south/south-df.csv')  #reloading the dataframe

south_df=south_df.sort_values(by='speakers',ascending=False).head(3)  #taking only top three rows


# ### North-East Zone

# In[13]:


'''Assam'''
AS_df=pd.read_excel('Datasets/north-east/c-17-assam.XLSX')
AS_df=AS_df[['Unnamed: 3','Unnamed: 4']]
AS_df=AS_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
AS_df=AS_df.dropna()   #remove NaN rows
AS_df=AS_df.loc[5: ,]  #remove useless rows 
AS_dict=dict(zip(AS_df['language-name'] , AS_df['speakers']))

'''Sikkim'''
SK_df=pd.read_excel('Datasets/north-east/c-17-sikkim.XLSX')
SK_df=SK_df[['Unnamed: 3','Unnamed: 4']]
SK_df=SK_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
SK_df=SK_df.dropna()   #remove NaN rows
SK_df=SK_df.loc[5: ,]  #remove useless rows 
SK_dict=dict(zip(SK_df['language-name'] , SK_df['speakers']))


'''Meghalaya'''
MG_df=pd.read_excel('Datasets/north-east/c-17-meghalaya.XLSX')
MG_df=MG_df[['Unnamed: 3','Unnamed: 4']]
MG_df=MG_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
MG_df=MG_df.dropna()   #remove NaN rows
MG_df=MG_df.loc[5: ,]  #remove useless rows 
MG_dict=dict(zip(MG_df['language-name'] , MG_df['speakers']))


'''Tripura'''
TR_df=pd.read_excel('Datasets/north-east/c-17-tripura.XLSX')
TR_df=TR_df[['Unnamed: 3','Unnamed: 4']]
TR_df=TR_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
TR_df=TR_df.dropna()   #remove NaN rows
TR_df=TR_df.loc[5: ,]  #remove useless rows 
TR_dict=dict(zip(TR_df['language-name'] , TR_df['speakers']))


'''Arunachal Pradesh'''
AR_df=pd.read_excel('Datasets/north-east/c-17-arunachal pradesh.XLSX')
AR_df=AR_df[['Unnamed: 3','Unnamed: 4']]
AR_df=AR_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
AR_df=AR_df.dropna()   #remove NaN rows
AR_df=AR_df.loc[5: ,]  #remove useless rows 
AR_dict=dict(zip(AR_df['language-name'] , AR_df['speakers']))


'''Manipur'''
MN_df=pd.read_excel('Datasets/north-east/c-17-manipur.XLSX')
MN_df=MN_df[['Unnamed: 3','Unnamed: 4']]
MN_df=MN_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
MN_df=MN_df.dropna()   #remove NaN rows
MN_df=MN_df.loc[5: ,]  #remove useless rows 
MN_dict=dict(zip(MN_df['language-name'] , MN_df['speakers']))


'''nagaland'''
NG_df=pd.read_excel('Datasets/north-east/c-17-nagaland.XLSX')
NG_df=NG_df[['Unnamed: 3','Unnamed: 4']]
NG_df=NG_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
NG_df=NG_df.dropna()   #remove NaN rows
NG_df=NG_df.loc[5: ,]  #remove useless rows 
NG_dict=dict(zip(NG_df['language-name'] , NG_df['speakers']))


'''Mizoram'''
MZ_df=pd.read_excel('Datasets/north-east/c-17-mizoram.XLSX')
MZ_df=MZ_df[['Unnamed: 3','Unnamed: 4']]
MZ_df=MZ_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
MZ_df=MZ_df.dropna()   #remove NaN rows
MZ_df=MZ_df.loc[5: ,]  #remove useless rows 
MZ_dict=dict(zip(MZ_df['language-name'] , MZ_df['speakers']))


'''Andaman & Nicobar'''
AN_df=pd.read_excel('Datasets/north-east/c-17-andaman & nicobar islands.XLSX')
AN_df=AN_df[['Unnamed: 3','Unnamed: 4']]
AN_df=AN_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
AN_df=AN_df.dropna()   #remove NaN rows
AN_df=AN_df.loc[5: ,]  #remove useless rows 
AN_dict=dict(zip(AN_df['language-name'] , AN_df['speakers']))


# ### Creation of north_east_df which stores all languages spoken in this region with their respective number of speakers

# In[14]:


#making a dataframe from each dictionary
north_east_df1=pd.DataFrame(AS_dict.items(),columns=['language','speakers'])
north_east_df2=pd.DataFrame(SK_dict.items(),columns=['language','speakers'])
north_east_df3=pd.DataFrame(MG_dict.items(),columns=['language','speakers'])
north_east_df4=pd.DataFrame(TR_dict.items(),columns=['language','speakers'])
north_east_df5=pd.DataFrame(AR_dict.items(),columns=['language','speakers'])
north_east_df6=pd.DataFrame(MN_dict.items(),columns=['language','speakers'])
north_east_df7=pd.DataFrame(NG_dict.items(),columns=['language','speakers'])
north_east_df8=pd.DataFrame(MZ_dict.items(),columns=['language','speakers'])
north_east_df9=pd.DataFrame(AN_dict.items(),columns=['language','speakers'])


#taking union of those dataframes
#note that this merge will remove duplicates when both the language name and no-of-speakers will be same in two states. We don't want this. But here that situation will not arise because matching of language and no-of-speakers of two states is nearly impossible
north_east_df=pd.merge(north_east_df1,north_east_df2,how='outer')
north_east_df=pd.merge(north_east_df,north_east_df3,how='outer')
north_east_df=pd.merge(north_east_df,north_east_df4,how='outer')
north_east_df=pd.merge(north_east_df,north_east_df5,how='outer')
north_east_df=pd.merge(north_east_df,north_east_df6,how='outer')
north_east_df=pd.merge(north_east_df,north_east_df7,how='outer')
north_east_df=pd.merge(north_east_df,north_east_df8,how='outer')
north_east_df=pd.merge(north_east_df,north_east_df9,how='outer')


'''After taking union there are multiple rows having language 'ASSAMESE'(similarly other languages also are present multiple times).
And this north_east_df contains data from all the regions.So if I group it on basis of language column and find sum of
'speakers' column within each group , I will get the total number of people who speak that language in whole region'''
north_east_df=north_east_df.groupby(['language']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal if we store and re-load dataframe again
north_east_df.to_csv('Datasets/north-east/north-east-df.csv')  #storing dataframe
north_east_df=pd.read_csv('Datasets/north-east/north-east-df.csv')  #reloading the dataframe

north_east_df=north_east_df.sort_values(by='speakers',ascending=False).head(3)  #taking only top three rows


# ### Creation of output file region-india.csv

# In[15]:


region_india_df=pd.DataFrame(columns=['region','language-1','language-2','language-3'])

region_india_df=region_india_df.append({'region':'North','language-1':north_df['language'].iloc[0],'language-2':north_df['language'].iloc[1],'language-3':north_df['language'].iloc[2]},ignore_index=True)

region_india_df=region_india_df.append({'region':'West','language-1':west_df['language'].iloc[0],'language-2':west_df['language'].iloc[1],'language-3':west_df['language'].iloc[2]},ignore_index=True)

region_india_df=region_india_df.append({'region':'Central','language-1':central_df['language'].iloc[0],'language-2':central_df['language'].iloc[1],'language-3':central_df['language'].iloc[2]},ignore_index=True)

region_india_df=region_india_df.append({'region':'East','language-1':east_df['language'].iloc[0],'language-2':east_df['language'].iloc[1],'language-3':east_df['language'].iloc[2]},ignore_index=True)

region_india_df=region_india_df.append({'region':'South','language-1':south_df['language'].iloc[0],'language-2':south_df['language'].iloc[1],'language-3':south_df['language'].iloc[2]},ignore_index=True)

region_india_df=region_india_df.append({'region':'North-East','language-1':north_east_df['language'].iloc[0],'language-2':north_east_df['language'].iloc[1],'language-3':north_east_df['language'].iloc[2]},ignore_index=True)


region_india_df.to_csv('output files/region-india-a.csv',index=False)


# # 
# # part-b  Using mother tongue + 2nd lang + 3rd lang

# ### North Zone

# In[16]:


'''Jammu & Kashmir'''
my_df=pd.read_excel('Datasets/north/c-17-jammu & kashmir.XLSX')
my_df=my_df[['Unnamed: 3','Unnamed: 4','Unnamed: 8','Unnamed: 9','Unnamed: 13','Unnamed: 14']]
#performing union operation of mother tongue, 2nd lang and 3rd lang column
my_df=my_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
test_df1=my_df[['Unnamed: 8','Unnamed: 9']]
test_df1.rename(columns={'Unnamed: 8':'language-name','Unnamed: 9':'speakers'},inplace=True)
test_df2=my_df[['Unnamed: 13','Unnamed: 14']]
test_df2.rename(columns={'Unnamed: 13':'language-name','Unnamed: 14':'speakers'},inplace=True)
my_df=my_df[['language-name','speakers']]
#remove NaN rows
my_df.dropna(inplace=True)
test_df1.dropna(inplace=True)
test_df2.dropna(inplace=True)
#remove useless rows 
my_df=my_df.loc[5:,]
test_df1=test_df1.loc[6:,]
test_df2=test_df2.loc[7:,]
my_df=my_df.append(test_df1)
my_df=my_df.append(test_df2)
my_df=my_df.groupby(['language-name']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal by reset_index() function
my_df=my_df.reset_index()
#now this dataframe has languages and number of people who speak that language
#Now I will make a dictionary so that searching for certain language will be quicker while summing up number of speakers of certain language in a region
JK_dict=dict(zip(my_df['language-name'] , my_df['speakers']))




#Now, I am going to do this for every state and UT
'''Punjab'''
my_df=pd.read_excel('Datasets/north/c-17-punjab.XLSX')
my_df=my_df[['Unnamed: 3','Unnamed: 4','Unnamed: 8','Unnamed: 9','Unnamed: 13','Unnamed: 14']]
#performing union operation of mother tongue, 2nd lang and 3rd lang column
my_df=my_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
test_df1=my_df[['Unnamed: 8','Unnamed: 9']]
test_df1.rename(columns={'Unnamed: 8':'language-name','Unnamed: 9':'speakers'},inplace=True)
test_df2=my_df[['Unnamed: 13','Unnamed: 14']]
test_df2.rename(columns={'Unnamed: 13':'language-name','Unnamed: 14':'speakers'},inplace=True)
my_df=my_df[['language-name','speakers']]
#remove NaN rows
my_df.dropna(inplace=True)
test_df1.dropna(inplace=True)
test_df2.dropna(inplace=True)
#remove useless rows 
my_df=my_df.loc[5:,]
test_df1=test_df1.loc[6:,]
test_df2=test_df2.loc[7:,]
my_df=my_df.append(test_df1)
my_df=my_df.append(test_df2)
my_df=my_df.groupby(['language-name']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal by reset_index() function
my_df=my_df.reset_index()
PN_dict=dict(zip(my_df['language-name'] , my_df['speakers']))



'''Himachal pradesh'''
my_df=pd.read_excel('Datasets/north/c-17-himachal pradesh.XLSX')
my_df=my_df[['Unnamed: 3','Unnamed: 4','Unnamed: 8','Unnamed: 9','Unnamed: 13','Unnamed: 14']]
#performing union operation of mother tongue, 2nd lang and 3rd lang column
my_df=my_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
test_df1=my_df[['Unnamed: 8','Unnamed: 9']]
test_df1.rename(columns={'Unnamed: 8':'language-name','Unnamed: 9':'speakers'},inplace=True)
test_df2=my_df[['Unnamed: 13','Unnamed: 14']]
test_df2.rename(columns={'Unnamed: 13':'language-name','Unnamed: 14':'speakers'},inplace=True)
my_df=my_df[['language-name','speakers']]
#remove NaN rows
my_df.dropna(inplace=True)
test_df1.dropna(inplace=True)
test_df2.dropna(inplace=True)
#remove useless rows 
my_df=my_df.loc[5:,]
test_df1=test_df1.loc[6:,]
test_df2=test_df2.loc[7:,]
my_df=my_df.append(test_df1)
my_df=my_df.append(test_df2)
my_df=my_df.groupby(['language-name']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal by reset_index() function
my_df=my_df.reset_index()
HP_dict=dict(zip(my_df['language-name'] , my_df['speakers']))



'''Haryana'''
my_df=pd.read_excel('Datasets/north/c-17-haryana.XLSX')
my_df=my_df[['Unnamed: 3','Unnamed: 4','Unnamed: 8','Unnamed: 9','Unnamed: 13','Unnamed: 14']]
#performing union operation of mother tongue, 2nd lang and 3rd lang column
my_df=my_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
test_df1=my_df[['Unnamed: 8','Unnamed: 9']]
test_df1.rename(columns={'Unnamed: 8':'language-name','Unnamed: 9':'speakers'},inplace=True)
test_df2=my_df[['Unnamed: 13','Unnamed: 14']]
test_df2.rename(columns={'Unnamed: 13':'language-name','Unnamed: 14':'speakers'},inplace=True)
my_df=my_df[['language-name','speakers']]
#remove NaN rows
my_df.dropna(inplace=True)
test_df1.dropna(inplace=True)
test_df2.dropna(inplace=True)
#remove useless rows 
my_df=my_df.loc[5:,]
test_df1=test_df1.loc[6:,]
test_df2=test_df2.loc[7:,]
my_df=my_df.append(test_df1)
my_df=my_df.append(test_df2)
my_df=my_df.groupby(['language-name']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal by reset_index() function
my_df=my_df.reset_index()
HR_dict=dict(zip(my_df['language-name'] , my_df['speakers']))



'''Uttarakhand'''
my_df=pd.read_excel('Datasets/north/c-17-uttarakhand.XLSX')
my_df=my_df[['Unnamed: 3','Unnamed: 4','Unnamed: 8','Unnamed: 9','Unnamed: 13','Unnamed: 14']]
#performing union operation of mother tongue, 2nd lang and 3rd lang column
my_df=my_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
test_df1=my_df[['Unnamed: 8','Unnamed: 9']]
test_df1.rename(columns={'Unnamed: 8':'language-name','Unnamed: 9':'speakers'},inplace=True)
test_df2=my_df[['Unnamed: 13','Unnamed: 14']]
test_df2.rename(columns={'Unnamed: 13':'language-name','Unnamed: 14':'speakers'},inplace=True)
my_df=my_df[['language-name','speakers']]
#remove NaN rows
my_df.dropna(inplace=True)
test_df1.dropna(inplace=True)
test_df2.dropna(inplace=True)
#remove useless rows 
my_df=my_df.loc[5:,]
test_df1=test_df1.loc[6:,]
test_df2=test_df2.loc[7:,]
my_df=my_df.append(test_df1)
my_df=my_df.append(test_df2)
my_df=my_df.groupby(['language-name']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal by reset_index() function
my_df=my_df.reset_index()
UK_dict=dict(zip(my_df['language-name'] , my_df['speakers']))



'''Delhi'''
my_df=pd.read_excel('Datasets/north/c-17-delhi.XLSX')
my_df=my_df[['Unnamed: 3','Unnamed: 4','Unnamed: 8','Unnamed: 9','Unnamed: 13','Unnamed: 14']]
#performing union operation of mother tongue, 2nd lang and 3rd lang column
my_df=my_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
test_df1=my_df[['Unnamed: 8','Unnamed: 9']]
test_df1.rename(columns={'Unnamed: 8':'language-name','Unnamed: 9':'speakers'},inplace=True)
test_df2=my_df[['Unnamed: 13','Unnamed: 14']]
test_df2.rename(columns={'Unnamed: 13':'language-name','Unnamed: 14':'speakers'},inplace=True)
my_df=my_df[['language-name','speakers']]
#remove NaN rows
my_df.dropna(inplace=True)
test_df1.dropna(inplace=True)
test_df2.dropna(inplace=True)
#remove useless rows 
my_df=my_df.loc[5:,]
test_df1=test_df1.loc[6:,]
test_df2=test_df2.loc[7:,]
my_df=my_df.append(test_df1)
my_df=my_df.append(test_df2)
my_df=my_df.groupby(['language-name']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal by reset_index() function
my_df=my_df.reset_index()
DL_dict=dict(zip(my_df['language-name'] , my_df['speakers']))



'''Chandigarh'''
my_df=pd.read_excel('Datasets/north/c-17-chandigarh.XLSX')
my_df=my_df[['Unnamed: 3','Unnamed: 4','Unnamed: 8','Unnamed: 9','Unnamed: 13','Unnamed: 14']]
#performing union operation of mother tongue, 2nd lang and 3rd lang column
my_df=my_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
test_df1=my_df[['Unnamed: 8','Unnamed: 9']]
test_df1.rename(columns={'Unnamed: 8':'language-name','Unnamed: 9':'speakers'},inplace=True)
test_df2=my_df[['Unnamed: 13','Unnamed: 14']]
test_df2.rename(columns={'Unnamed: 13':'language-name','Unnamed: 14':'speakers'},inplace=True)
my_df=my_df[['language-name','speakers']]
#remove NaN rows
my_df.dropna(inplace=True)
test_df1.dropna(inplace=True)
test_df2.dropna(inplace=True)
#remove useless rows 
my_df=my_df.loc[5:,]
test_df1=test_df1.loc[6:,]
test_df2=test_df2.loc[7:,]
my_df=my_df.append(test_df1)
my_df=my_df.append(test_df2)
my_df=my_df.groupby(['language-name']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal by reset_index() function
my_df=my_df.reset_index()

CN_dict=dict(zip(my_df['language-name'] , my_df['speakers']))


# ### Creation of north_df which stores all languages spoken in this region with their respective number of speakers 

# In[17]:


#making a dataframe from each dictionary
north_df1=pd.DataFrame(CN_dict.items(),columns=['language','speakers'])
north_df2=pd.DataFrame(DL_dict.items(),columns=['language','speakers'])
north_df3=pd.DataFrame(UK_dict.items(),columns=['language','speakers'])
north_df4=pd.DataFrame(HR_dict.items(),columns=['language','speakers'])
north_df5=pd.DataFrame(HP_dict.items(),columns=['language','speakers'])
north_df6=pd.DataFrame(PN_dict.items(),columns=['language','speakers'])
north_df7=pd.DataFrame(JK_dict.items(),columns=['language','speakers'])

#taking union of those dataframes
north_df=pd.merge(north_df1,north_df2,how='outer')
north_df=pd.merge(north_df,north_df3,how='outer')
north_df=pd.merge(north_df,north_df4,how='outer')
north_df=pd.merge(north_df,north_df5,how='outer')
north_df=pd.merge(north_df,north_df6,how='outer')
north_df=pd.merge(north_df,north_df7,how='outer')

'''After taking union there are multiple rows having language 'ASSAMESE'(similarly other languages also are present multiple times).
And this north_df contains data from all the regions.So if I group it on basis of language column and find sum of
'speakers' column within each group , I will get the total number of people who speak that language in whole region'''
north_df=north_df.groupby(['language']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal if we store and re-load dataframe again
north_df.to_csv('Datasets/north/north-df.csv')  #storing dataframe
north_df=pd.read_csv('Datasets/north/north-df.csv')  #reloading the dataframe
north_df=north_df.sort_values(by='speakers',ascending=False).head(30)  #taking only top three rows


        #north_df[north_df['language']=='HINDI ']-->for cross checking whether my code gives correct number of hindi speakers    #It has been found that the string 'HINDI' is not present in the census but rather it is 'HINDI ' i.e. a 'space' at end. There are other such languages also.


# ### West Zone

# In[18]:


'''Rajasthan'''
my_df=pd.read_excel('Datasets/west/c-17-rajasthan.XLSX')
my_df=my_df[['Unnamed: 3','Unnamed: 4','Unnamed: 8','Unnamed: 9','Unnamed: 13','Unnamed: 14']]
#performing union operation of mother tongue, 2nd lang and 3rd lang column
my_df=my_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
test_df1=my_df[['Unnamed: 8','Unnamed: 9']]
test_df1.rename(columns={'Unnamed: 8':'language-name','Unnamed: 9':'speakers'},inplace=True)
test_df2=my_df[['Unnamed: 13','Unnamed: 14']]
test_df2.rename(columns={'Unnamed: 13':'language-name','Unnamed: 14':'speakers'},inplace=True)
my_df=my_df[['language-name','speakers']]
#remove NaN rows
my_df.dropna(inplace=True)
test_df1.dropna(inplace=True)
test_df2.dropna(inplace=True)
#remove useless rows 
my_df=my_df.loc[5:,]
test_df1=test_df1.loc[6:,]
test_df2=test_df2.loc[7:,]
my_df=my_df.append(test_df1)
my_df=my_df.append(test_df2)
my_df=my_df.groupby(['language-name']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal by reset_index() function
my_df=my_df.reset_index()
RJ_dict=dict(zip(my_df['language-name'] , my_df['speakers']))


'''Gujarat'''
my_df=pd.read_excel('Datasets/west/c-17-gujarat.XLSX')
my_df=my_df[['Unnamed: 3','Unnamed: 4','Unnamed: 8','Unnamed: 9','Unnamed: 13','Unnamed: 14']]
#performing union operation of mother tongue, 2nd lang and 3rd lang column
my_df=my_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
test_df1=my_df[['Unnamed: 8','Unnamed: 9']]
test_df1.rename(columns={'Unnamed: 8':'language-name','Unnamed: 9':'speakers'},inplace=True)
test_df2=my_df[['Unnamed: 13','Unnamed: 14']]
test_df2.rename(columns={'Unnamed: 13':'language-name','Unnamed: 14':'speakers'},inplace=True)
my_df=my_df[['language-name','speakers']]
#remove NaN rows
my_df.dropna(inplace=True)
test_df1.dropna(inplace=True)
test_df2.dropna(inplace=True)
#remove useless rows 
my_df=my_df.loc[5:,]
test_df1=test_df1.loc[6:,]
test_df2=test_df2.loc[7:,]
my_df=my_df.append(test_df1)
my_df=my_df.groupby(['language-name']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal by reset_index() function
my_df=my_df.reset_index()
GJ_dict=dict(zip(my_df['language-name'] , my_df['speakers']))

'''Maharashtra'''
my_df=pd.read_excel('Datasets/west/c-17-maharashtra.XLSX')
my_df=my_df[['Unnamed: 3','Unnamed: 4','Unnamed: 8','Unnamed: 9','Unnamed: 13','Unnamed: 14']]
#performing union operation of mother tongue, 2nd lang and 3rd lang column
my_df=my_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
test_df1=my_df[['Unnamed: 8','Unnamed: 9']]
test_df1.rename(columns={'Unnamed: 8':'language-name','Unnamed: 9':'speakers'},inplace=True)
test_df2=my_df[['Unnamed: 13','Unnamed: 14']]
test_df2.rename(columns={'Unnamed: 13':'language-name','Unnamed: 14':'speakers'},inplace=True)
my_df=my_df[['language-name','speakers']]
#remove NaN rows
my_df.dropna(inplace=True)
test_df1.dropna(inplace=True)
test_df2.dropna(inplace=True)
#remove useless rows 
my_df=my_df.loc[5:,]
test_df1=test_df1.loc[6:,]
test_df2=test_df2.loc[7:,]
my_df=my_df.append(test_df1)
my_df=my_df.groupby(['language-name']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal by reset_index() function
my_df=my_df.reset_index()
MH_dict=dict(zip(my_df['language-name'] , my_df['speakers']))

'''Goa'''
my_df=pd.read_excel('Datasets/west/c-17-goa.XLSX')
my_df=my_df[['Unnamed: 3','Unnamed: 4','Unnamed: 8','Unnamed: 9','Unnamed: 13','Unnamed: 14']]
#performing union operation of mother tongue, 2nd lang and 3rd lang column
my_df=my_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
test_df1=my_df[['Unnamed: 8','Unnamed: 9']]
test_df1.rename(columns={'Unnamed: 8':'language-name','Unnamed: 9':'speakers'},inplace=True)
test_df2=my_df[['Unnamed: 13','Unnamed: 14']]
test_df2.rename(columns={'Unnamed: 13':'language-name','Unnamed: 14':'speakers'},inplace=True)
my_df=my_df[['language-name','speakers']]
#remove NaN rows
my_df.dropna(inplace=True)
test_df1.dropna(inplace=True)
test_df2.dropna(inplace=True)
#remove useless rows 
my_df=my_df.loc[5:,]
test_df1=test_df1.loc[6:,]
test_df2=test_df2.loc[7:,]
my_df=my_df.append(test_df1)
my_df=my_df.groupby(['language-name']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal by reset_index() function
my_df=my_df.reset_index()
GA_dict=dict(zip(my_df['language-name'] , my_df['speakers']))

'''Dadra & Namyr Haveli'''
my_df=pd.read_excel('Datasets/west/c-17-dadra & nagar haveli.XLSX')
my_df=my_df[['Unnamed: 3','Unnamed: 4','Unnamed: 8','Unnamed: 9','Unnamed: 13','Unnamed: 14']]
#performing union operation of mother tongue, 2nd lang and 3rd lang column
my_df=my_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
test_df1=my_df[['Unnamed: 8','Unnamed: 9']]
test_df1.rename(columns={'Unnamed: 8':'language-name','Unnamed: 9':'speakers'},inplace=True)
test_df2=my_df[['Unnamed: 13','Unnamed: 14']]
test_df2.rename(columns={'Unnamed: 13':'language-name','Unnamed: 14':'speakers'},inplace=True)
my_df=my_df[['language-name','speakers']]
#remove NaN rows
my_df.dropna(inplace=True)
test_df1.dropna(inplace=True)
test_df2.dropna(inplace=True)
#remove useless rows 
my_df=my_df.loc[5:,]
test_df1=test_df1.loc[6:,]
test_df2=test_df2.loc[7:,]
my_df=my_df.append(test_df1)
my_df=my_df.groupby(['language-name']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal by reset_index() function
my_df=my_df.reset_index()
DNH_dict=dict(zip(my_df['language-name'] , my_df['speakers']))

'''Daman & Diu'''
my_df=pd.read_excel('Datasets/west/c-17-daman & diu.XLSX')
my_df=my_df[['Unnamed: 3','Unnamed: 4','Unnamed: 8','Unnamed: 9','Unnamed: 13','Unnamed: 14']]
#performing union operation of mother tongue, 2nd lang and 3rd lang column
my_df=my_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
test_df1=my_df[['Unnamed: 8','Unnamed: 9']]
test_df1.rename(columns={'Unnamed: 8':'language-name','Unnamed: 9':'speakers'},inplace=True)
test_df2=my_df[['Unnamed: 13','Unnamed: 14']]
test_df2.rename(columns={'Unnamed: 13':'language-name','Unnamed: 14':'speakers'},inplace=True)
my_df=my_df[['language-name','speakers']]
#remove NaN rows
my_df.dropna(inplace=True)
test_df1.dropna(inplace=True)
test_df2.dropna(inplace=True)
#remove useless rows 
my_df=my_df.loc[5:,]
test_df1=test_df1.loc[6:,]
test_df2=test_df2.loc[7:,]
my_df=my_df.append(test_df1)
my_df=my_df.groupby(['language-name']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal by reset_index() function
my_df=my_df.reset_index()
DND_dict=dict(zip(my_df['language-name'] , my_df['speakers']))


# ### Creation of west_df which stores all languages spoken in this region with their respective number of speakers

# In[19]:


#making a dataframe from each dictionary
west_df1=pd.DataFrame(RJ_dict.items(),columns=['language','speakers'])
west_df2=pd.DataFrame(GJ_dict.items(),columns=['language','speakers'])
west_df3=pd.DataFrame(MH_dict.items(),columns=['language','speakers'])
west_df4=pd.DataFrame(GA_dict.items(),columns=['language','speakers'])
west_df5=pd.DataFrame(DNH_dict.items(),columns=['language','speakers'])
west_df6=pd.DataFrame(DND_dict.items(),columns=['language','speakers'])


#taking union of those dataframes
west_df=pd.merge(west_df1,west_df2,how='outer')
west_df=pd.merge(west_df,west_df3,how='outer')
west_df=pd.merge(west_df,west_df4,how='outer')
west_df=pd.merge(west_df,west_df5,how='outer')
west_df=pd.merge(west_df,west_df6,how='outer')


'''After taking union there are multiple rows having language 'ASSAMESE'(similarly other languages also are present multiple times).
And this west_df contains data from all the regions.So if I group it on basis of language column and find sum of
'speakers' column within each group , I will get the total number of people who speak that language in whole region'''
west_df=west_df.groupby(['language']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal if we store and re-load dataframe again
west_df.to_csv('Datasets/west/west-df.csv')  #storing dataframe
west_df=pd.read_csv('Datasets/west/west-df.csv')  #reloading the dataframe

west_df=west_df.sort_values(by='speakers',ascending=False).head(3)  #taking only top three rows


# ### Central Zone

# In[20]:


'''Madhya Pradesh'''
my_df=pd.read_excel('Datasets/central/c-17-madhya pradesh.XLSX')
my_df=my_df[['Unnamed: 3','Unnamed: 4','Unnamed: 8','Unnamed: 9','Unnamed: 13','Unnamed: 14']]
#performing union operation of mother tongue, 2nd lang and 3rd lang column
my_df=my_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
test_df1=my_df[['Unnamed: 8','Unnamed: 9']]
test_df1.rename(columns={'Unnamed: 8':'language-name','Unnamed: 9':'speakers'},inplace=True)
test_df2=my_df[['Unnamed: 13','Unnamed: 14']]
test_df2.rename(columns={'Unnamed: 13':'language-name','Unnamed: 14':'speakers'},inplace=True)
my_df=my_df[['language-name','speakers']]
#remove NaN rows
my_df.dropna(inplace=True)
test_df1.dropna(inplace=True)
test_df2.dropna(inplace=True)
#remove useless rows 
my_df=my_df.loc[5:,]
test_df1=test_df1.loc[6:,]
test_df2=test_df2.loc[7:,]
my_df=my_df.append(test_df1)
my_df=my_df.append(test_df2)
my_df=my_df.groupby(['language-name']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal by reset_index() function
my_df=my_df.reset_index()
MP_dict=dict(zip(my_df['language-name'] , my_df['speakers']))

'''Uttar Pradesh'''
my_df=pd.read_excel('Datasets/central/c-17-uttar pradesh.XLSX')
my_df=my_df[['Unnamed: 3','Unnamed: 4','Unnamed: 8','Unnamed: 9','Unnamed: 13','Unnamed: 14']]
#performing union operation of mother tongue, 2nd lang and 3rd lang column
my_df=my_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
test_df1=my_df[['Unnamed: 8','Unnamed: 9']]
test_df1.rename(columns={'Unnamed: 8':'language-name','Unnamed: 9':'speakers'},inplace=True)
test_df2=my_df[['Unnamed: 13','Unnamed: 14']]
test_df2.rename(columns={'Unnamed: 13':'language-name','Unnamed: 14':'speakers'},inplace=True)
my_df=my_df[['language-name','speakers']]
#remove NaN rows
my_df.dropna(inplace=True)
test_df1.dropna(inplace=True)
test_df2.dropna(inplace=True)
#remove useless rows 
my_df=my_df.loc[5:,]
test_df1=test_df1.loc[6:,]
test_df2=test_df2.loc[7:,]
my_df=my_df.append(test_df1)
my_df=my_df.append(test_df2)
my_df=my_df.groupby(['language-name']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal by reset_index() function
my_df=my_df.reset_index()
UP_dict=dict(zip(my_df['language-name'] , my_df['speakers']))

'''Chhattisgarh'''
my_df=pd.read_excel('Datasets/central/c-17-chhattisgarh.XLSX')
my_df=my_df[['Unnamed: 3','Unnamed: 4','Unnamed: 8','Unnamed: 9','Unnamed: 13','Unnamed: 14']]
#performing union operation of mother tongue, 2nd lang and 3rd lang column
my_df=my_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
test_df1=my_df[['Unnamed: 8','Unnamed: 9']]
test_df1.rename(columns={'Unnamed: 8':'language-name','Unnamed: 9':'speakers'},inplace=True)
test_df2=my_df[['Unnamed: 13','Unnamed: 14']]
test_df2.rename(columns={'Unnamed: 13':'language-name','Unnamed: 14':'speakers'},inplace=True)
my_df=my_df[['language-name','speakers']]
#remove NaN rows
my_df.dropna(inplace=True)
test_df1.dropna(inplace=True)
test_df2.dropna(inplace=True)
#remove useless rows 
my_df=my_df.loc[5:,]
test_df1=test_df1.loc[6:,]
test_df2=test_df2.loc[7:,]
my_df=my_df.append(test_df1)
my_df=my_df.append(test_df2)
my_df=my_df.groupby(['language-name']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal by reset_index() function
my_df=my_df.reset_index()
CG_dict=dict(zip(my_df['language-name'] , my_df['speakers']))


# ### Creation of central_df which stores all languages spoken in this region with their respective number of speakers

# In[21]:


#making a dataframe from each dictionary
central_df1=pd.DataFrame(MP_dict.items(),columns=['language','speakers'])
central_df2=pd.DataFrame(UP_dict.items(),columns=['language','speakers'])
central_df3=pd.DataFrame(CG_dict.items(),columns=['language','speakers'])



#taking union of those dataframes
central_df=pd.merge(central_df1,central_df2,how='outer')
central_df=pd.merge(central_df,central_df3,how='outer')



'''After taking union there are multiple rows having language 'ASSAMESE'(similarly other languages also are present multiple times).
And this central_df contains data from all the regions.So if I group it on basis of language column and find sum of
'speakers' column within each group , I will get the total number of people who speak that language in whole region'''
central_df=central_df.groupby(['language']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal if we store and re-load dataframe again
central_df.to_csv('Datasets/central/central-df.csv')  #storing dataframe
central_df=pd.read_csv('Datasets/central/central-df.csv')  #reloading the dataframe

central_df=central_df.sort_values(by='speakers',ascending=False).head(3)  #taking only top three rows


# ### East Zone

# In[22]:


'''Bihar'''
my_df=pd.read_excel('Datasets/east/c-17-bihar.XLSX')
my_df=my_df[['Unnamed: 3','Unnamed: 4','Unnamed: 8','Unnamed: 9','Unnamed: 13','Unnamed: 14']]
#performing union operation of mother tongue, 2nd lang and 3rd lang column
my_df=my_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
test_df1=my_df[['Unnamed: 8','Unnamed: 9']]
test_df1.rename(columns={'Unnamed: 8':'language-name','Unnamed: 9':'speakers'},inplace=True)
test_df2=my_df[['Unnamed: 13','Unnamed: 14']]
test_df2.rename(columns={'Unnamed: 13':'language-name','Unnamed: 14':'speakers'},inplace=True)
my_df=my_df[['language-name','speakers']]
#remove NaN rows
my_df.dropna(inplace=True)
test_df1.dropna(inplace=True)
test_df2.dropna(inplace=True)
#remove useless rows 
my_df=my_df.loc[5:,]
test_df1=test_df1.loc[6:,]
test_df2=test_df2.loc[7:,]
my_df=my_df.append(test_df1)
my_df=my_df.append(test_df2)
my_df=my_df.groupby(['language-name']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal by reset_index() function
my_df=my_df.reset_index()
BH_dict=dict(zip(my_df['language-name'] , my_df['speakers']))

'''West Bengal'''
my_df=pd.read_excel('Datasets/east/c-17-west bengal.XLSX')
my_df=my_df[['Unnamed: 3','Unnamed: 4','Unnamed: 8','Unnamed: 9','Unnamed: 13','Unnamed: 14']]
#performing union operation of mother tongue, 2nd lang and 3rd lang column
my_df=my_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
test_df1=my_df[['Unnamed: 8','Unnamed: 9']]
test_df1.rename(columns={'Unnamed: 8':'language-name','Unnamed: 9':'speakers'},inplace=True)
test_df2=my_df[['Unnamed: 13','Unnamed: 14']]
test_df2.rename(columns={'Unnamed: 13':'language-name','Unnamed: 14':'speakers'},inplace=True)
my_df=my_df[['language-name','speakers']]
#remove NaN rows
my_df.dropna(inplace=True)
test_df1.dropna(inplace=True)
test_df2.dropna(inplace=True)
#remove useless rows 
my_df=my_df.loc[5:,]
test_df1=test_df1.loc[6:,]
test_df2=test_df2.loc[7:,]
my_df=my_df.append(test_df1)
my_df=my_df.append(test_df2)
my_df=my_df.groupby(['language-name']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal by reset_index() function
my_df=my_df.reset_index()
WB_dict=dict(zip(my_df['language-name'] , my_df['speakers']))

'''Odisha'''
#In census data the spelling is odisha and its actual code is OD but since in assignment question it is written OR so I will write its code as OR but spelling I will use Odisha 
my_df=pd.read_excel('Datasets/east/c-17-odisha.XLSX')
my_df=my_df[['Unnamed: 3','Unnamed: 4','Unnamed: 8','Unnamed: 9','Unnamed: 13','Unnamed: 14']]
#performing union operation of mother tongue, 2nd lang and 3rd lang column
my_df=my_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
test_df1=my_df[['Unnamed: 8','Unnamed: 9']]
test_df1.rename(columns={'Unnamed: 8':'language-name','Unnamed: 9':'speakers'},inplace=True)
test_df2=my_df[['Unnamed: 13','Unnamed: 14']]
test_df2.rename(columns={'Unnamed: 13':'language-name','Unnamed: 14':'speakers'},inplace=True)
my_df=my_df[['language-name','speakers']]
#remove NaN rows
my_df.dropna(inplace=True)
test_df1.dropna(inplace=True)
test_df2.dropna(inplace=True)
#remove useless rows 
my_df=my_df.loc[5:,]
test_df1=test_df1.loc[6:,]
test_df2=test_df2.loc[7:,]
my_df=my_df.append(test_df1)
my_df=my_df.append(test_df2)
my_df=my_df.groupby(['language-name']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal by reset_index() function
my_df=my_df.reset_index()
OR_dict=dict(zip(my_df['language-name'] , my_df['speakers']))

'''Jharkhand'''
my_df=pd.read_excel('Datasets/east/c-17-jharkhand.XLSX')
my_df=my_df[['Unnamed: 3','Unnamed: 4','Unnamed: 8','Unnamed: 9','Unnamed: 13','Unnamed: 14']]
#performing union operation of mother tongue, 2nd lang and 3rd lang column
my_df=my_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
test_df1=my_df[['Unnamed: 8','Unnamed: 9']]
test_df1.rename(columns={'Unnamed: 8':'language-name','Unnamed: 9':'speakers'},inplace=True)
test_df2=my_df[['Unnamed: 13','Unnamed: 14']]
test_df2.rename(columns={'Unnamed: 13':'language-name','Unnamed: 14':'speakers'},inplace=True)
my_df=my_df[['language-name','speakers']]
#remove NaN rows
my_df.dropna(inplace=True)
test_df1.dropna(inplace=True)
test_df2.dropna(inplace=True)
#remove useless rows 
my_df=my_df.loc[5:,]
test_df1=test_df1.loc[6:,]
test_df2=test_df2.loc[7:,]
my_df=my_df.append(test_df1)
my_df=my_df.append(test_df2)
my_df=my_df.groupby(['language-name']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal by reset_index() function
my_df=my_df.reset_index()
JH_dict=dict(zip(my_df['language-name'] , my_df['speakers']))


# ### Creation of east_df which stores all languages spoken in this region with their respective number of speakers

# In[23]:


#making a dataframe from each dictionary
east_df1=pd.DataFrame(BH_dict.items(),columns=['language','speakers'])
east_df2=pd.DataFrame(WB_dict.items(),columns=['language','speakers'])
east_df3=pd.DataFrame(OR_dict.items(),columns=['language','speakers'])
east_df4=pd.DataFrame(JH_dict.items(),columns=['language','speakers'])


#taking union of those dataframes
east_df=pd.merge(east_df1,east_df2,how='outer')
east_df=pd.merge(east_df,east_df3,how='outer')
east_df=pd.merge(east_df,east_df4,how='outer')


'''After taking union there are multiple rows having language 'ASSAMESE'(similarly other languages also are present multiple times).
And this east_df contains data from all the regions.So if I group it on basis of language column and find sum of
'speakers' column within each group , I will get the total number of people who speak that language in whole region'''
east_df=east_df.groupby(['language']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal if we store and re-load dataframe again
east_df.to_csv('Datasets/east/east-df.csv')  #storing dataframe
east_df=pd.read_csv('Datasets/east/east-df.csv')  #reloading the dataframe

east_df=east_df.sort_values(by='speakers',ascending=False).head(3)  #taking only top three rows


# ### South Zone

# In[24]:


'''Karnataka'''
my_df=pd.read_excel('Datasets/south/c-17-karnataka.XLSX')
my_df=my_df[['Unnamed: 3','Unnamed: 4','Unnamed: 8','Unnamed: 9','Unnamed: 13','Unnamed: 14']]
#performing union operation of mother tongue, 2nd lang and 3rd lang column
my_df=my_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
test_df1=my_df[['Unnamed: 8','Unnamed: 9']]
test_df1.rename(columns={'Unnamed: 8':'language-name','Unnamed: 9':'speakers'},inplace=True)
test_df2=my_df[['Unnamed: 13','Unnamed: 14']]
test_df2.rename(columns={'Unnamed: 13':'language-name','Unnamed: 14':'speakers'},inplace=True)
my_df=my_df[['language-name','speakers']]
#remove NaN rows
my_df.dropna(inplace=True)
test_df1.dropna(inplace=True)
test_df2.dropna(inplace=True)
#remove useless rows 
my_df=my_df.loc[5:,]
test_df1=test_df1.loc[6:,]
test_df2=test_df2.loc[7:,]
my_df=my_df.append(test_df1)
my_df=my_df.append(test_df2)
my_df=my_df.groupby(['language-name']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal by reset_index() function
my_df=my_df.reset_index()
KA_dict=dict(zip(my_df['language-name'] , my_df['speakers']))

'''Andhra Pradesh'''
my_df=pd.read_excel('Datasets/south/c-17-andhra pradesh.XLSX')
my_df=my_df[['Unnamed: 3','Unnamed: 4','Unnamed: 8','Unnamed: 9','Unnamed: 13','Unnamed: 14']]
#performing union operation of mother tongue, 2nd lang and 3rd lang column
my_df=my_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
test_df1=my_df[['Unnamed: 8','Unnamed: 9']]
test_df1.rename(columns={'Unnamed: 8':'language-name','Unnamed: 9':'speakers'},inplace=True)
test_df2=my_df[['Unnamed: 13','Unnamed: 14']]
test_df2.rename(columns={'Unnamed: 13':'language-name','Unnamed: 14':'speakers'},inplace=True)
my_df=my_df[['language-name','speakers']]
#remove NaN rows
my_df.dropna(inplace=True)
test_df1.dropna(inplace=True)
test_df2.dropna(inplace=True)
#remove useless rows 
my_df=my_df.loc[5:,]
test_df1=test_df1.loc[6:,]
test_df2=test_df2.loc[7:,]
my_df=my_df.append(test_df1)
my_df=my_df.append(test_df2)
my_df=my_df.groupby(['language-name']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal by reset_index() function
my_df=my_df.reset_index()
AP_dict=dict(zip(my_df['language-name'] , my_df['speakers']))

'''Tamil Nadu'''
my_df=pd.read_excel('Datasets/south/c-17-tamil nadu.XLSX')
my_df=my_df[['Unnamed: 3','Unnamed: 4','Unnamed: 8','Unnamed: 9','Unnamed: 13','Unnamed: 14']]
#performing union operation of mother tongue, 2nd lang and 3rd lang column
my_df=my_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
test_df1=my_df[['Unnamed: 8','Unnamed: 9']]
test_df1.rename(columns={'Unnamed: 8':'language-name','Unnamed: 9':'speakers'},inplace=True)
test_df2=my_df[['Unnamed: 13','Unnamed: 14']]
test_df2.rename(columns={'Unnamed: 13':'language-name','Unnamed: 14':'speakers'},inplace=True)
my_df=my_df[['language-name','speakers']]
#remove NaN rows
my_df.dropna(inplace=True)
test_df1.dropna(inplace=True)
test_df2.dropna(inplace=True)
#remove useless rows 
my_df=my_df.loc[5:,]
test_df1=test_df1.loc[6:,]
test_df2=test_df2.loc[7:,]
my_df=my_df.append(test_df1)
my_df=my_df.append(test_df2)
my_df=my_df.groupby(['language-name']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal by reset_index() function
my_df=my_df.reset_index()
TN_dict=dict(zip(my_df['language-name'] , my_df['speakers']))

'''Kerala'''
my_df=pd.read_excel('Datasets/south/c-17-kerala.XLSX')
my_df=my_df[['Unnamed: 3','Unnamed: 4','Unnamed: 8','Unnamed: 9','Unnamed: 13','Unnamed: 14']]
#performing union operation of mother tongue, 2nd lang and 3rd lang column
my_df=my_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
test_df1=my_df[['Unnamed: 8','Unnamed: 9']]
test_df1.rename(columns={'Unnamed: 8':'language-name','Unnamed: 9':'speakers'},inplace=True)
test_df2=my_df[['Unnamed: 13','Unnamed: 14']]
test_df2.rename(columns={'Unnamed: 13':'language-name','Unnamed: 14':'speakers'},inplace=True)
my_df=my_df[['language-name','speakers']]
#remove NaN rows
my_df.dropna(inplace=True)
test_df1.dropna(inplace=True)
test_df2.dropna(inplace=True)
#remove useless rows 
my_df=my_df.loc[5:,]
test_df1=test_df1.loc[6:,]
test_df2=test_df2.loc[7:,]
my_df=my_df.append(test_df1)
my_df=my_df.append(test_df2)
my_df=my_df.groupby(['language-name']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal by reset_index() function
my_df=my_df.reset_index()
KL_dict=dict(zip(my_df['language-name'] , my_df['speakers']))

'''Lakshadweep'''
my_df=pd.read_excel('Datasets/south/c-17-lakshadweep.XLSX')
my_df=my_df[['Unnamed: 3','Unnamed: 4','Unnamed: 8','Unnamed: 9','Unnamed: 13','Unnamed: 14']]
#performing union operation of mother tongue, 2nd lang and 3rd lang column
my_df=my_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
test_df1=my_df[['Unnamed: 8','Unnamed: 9']]
test_df1.rename(columns={'Unnamed: 8':'language-name','Unnamed: 9':'speakers'},inplace=True)
test_df2=my_df[['Unnamed: 13','Unnamed: 14']]
test_df2.rename(columns={'Unnamed: 13':'language-name','Unnamed: 14':'speakers'},inplace=True)
my_df=my_df[['language-name','speakers']]
#remove NaN rows
my_df.dropna(inplace=True)
test_df1.dropna(inplace=True)
test_df2.dropna(inplace=True)
#remove useless rows 
my_df=my_df.loc[5:,]
test_df1=test_df1.loc[6:,]
test_df2=test_df2.loc[7:,]
my_df=my_df.append(test_df1)
my_df=my_df.append(test_df2)
my_df=my_df.groupby(['language-name']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal by reset_index() function
my_df=my_df.reset_index()
LD_dict=dict(zip(my_df['language-name'] , my_df['speakers']))

'''Puducherry'''
my_df=pd.read_excel('Datasets/south/c-17-puducherry.XLSX')
my_df=my_df[['Unnamed: 3','Unnamed: 4','Unnamed: 8','Unnamed: 9','Unnamed: 13','Unnamed: 14']]
#performing union operation of mother tongue, 2nd lang and 3rd lang column
my_df=my_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
test_df1=my_df[['Unnamed: 8','Unnamed: 9']]
test_df1.rename(columns={'Unnamed: 8':'language-name','Unnamed: 9':'speakers'},inplace=True)
test_df2=my_df[['Unnamed: 13','Unnamed: 14']]
test_df2.rename(columns={'Unnamed: 13':'language-name','Unnamed: 14':'speakers'},inplace=True)
my_df=my_df[['language-name','speakers']]
#remove NaN rows
my_df.dropna(inplace=True)
test_df1.dropna(inplace=True)
test_df2.dropna(inplace=True)
#remove useless rows 
my_df=my_df.loc[5:,]
test_df1=test_df1.loc[6:,]
test_df2=test_df2.loc[7:,]
my_df=my_df.append(test_df1)
my_df=my_df.append(test_df2)
my_df=my_df.groupby(['language-name']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal by reset_index() function
my_df=my_df.reset_index() 
PY_dict=dict(zip(my_df['language-name'] , my_df['speakers']))


# ### Creation of south_df which stores all languages spoken in this region with their respective number of speakers

# In[25]:


#making a dataframe from each dictionary
south_df1=pd.DataFrame(KA_dict.items(),columns=['language','speakers'])
south_df2=pd.DataFrame(AP_dict.items(),columns=['language','speakers'])
south_df3=pd.DataFrame(TN_dict.items(),columns=['language','speakers'])
south_df4=pd.DataFrame(KL_dict.items(),columns=['language','speakers'])
south_df5=pd.DataFrame(PY_dict.items(),columns=['language','speakers'])
south_df6=pd.DataFrame(LD_dict.items(),columns=['language','speakers'])


#taking union of those dataframes
south_df=pd.merge(south_df1,south_df2,how='outer')
south_df=pd.merge(south_df,south_df3,how='outer')
south_df=pd.merge(south_df,south_df4,how='outer')
south_df=pd.merge(south_df,south_df5,how='outer')
south_df=pd.merge(south_df,south_df6,how='outer')


'''After taking union there are multiple rows having language 'ASSAMESE'(similarly other languages also are present multiple times).
And this south_df contains data from all the regions.So if I group it on basis of language column and find sum of
'speakers' column within each group , I will get the total number of people who speak that language in whole region'''
south_df=south_df.groupby(['language']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal if we store and re-load dataframe again
south_df.to_csv('Datasets/south/south-df.csv')  #storing dataframe
south_df=pd.read_csv('Datasets/south/south-df.csv')  #reloading the dataframe

south_df=south_df.sort_values(by='speakers',ascending=False).head(3)  #taking only top three rows


# ### North-East Zone

# In[26]:


'''Assam'''
my_df=pd.read_excel('Datasets/north-east/c-17-assam.XLSX')
my_df=my_df[['Unnamed: 3','Unnamed: 4','Unnamed: 8','Unnamed: 9','Unnamed: 13','Unnamed: 14']]
#performing union operation of mother tongue, 2nd lang and 3rd lang column
my_df=my_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
test_df1=my_df[['Unnamed: 8','Unnamed: 9']]
test_df1.rename(columns={'Unnamed: 8':'language-name','Unnamed: 9':'speakers'},inplace=True)
test_df2=my_df[['Unnamed: 13','Unnamed: 14']]
test_df2.rename(columns={'Unnamed: 13':'language-name','Unnamed: 14':'speakers'},inplace=True)
my_df=my_df[['language-name','speakers']]
#remove NaN rows
my_df.dropna(inplace=True)
test_df1.dropna(inplace=True)
test_df2.dropna(inplace=True)
#remove useless rows 
my_df=my_df.loc[5:,]
test_df1=test_df1.loc[6:,]
test_df2=test_df2.loc[7:,]
my_df=my_df.append(test_df1)
my_df=my_df.append(test_df2)
my_df=my_df.groupby(['language-name']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal by reset_index() function
my_df=my_df.reset_index()
AS_dict=dict(zip(my_df['language-name'] , my_df['speakers']))

'''Sikkim'''
my_df=pd.read_excel('Datasets/north-east/c-17-sikkim.XLSX')
my_df=my_df[['Unnamed: 3','Unnamed: 4','Unnamed: 8','Unnamed: 9','Unnamed: 13','Unnamed: 14']]
#performing union operation of mother tongue, 2nd lang and 3rd lang column
my_df=my_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
test_df1=my_df[['Unnamed: 8','Unnamed: 9']]
test_df1.rename(columns={'Unnamed: 8':'language-name','Unnamed: 9':'speakers'},inplace=True)
test_df2=my_df[['Unnamed: 13','Unnamed: 14']]
test_df2.rename(columns={'Unnamed: 13':'language-name','Unnamed: 14':'speakers'},inplace=True)
my_df=my_df[['language-name','speakers']]
#remove NaN rows
my_df.dropna(inplace=True)
test_df1.dropna(inplace=True)
test_df2.dropna(inplace=True)
#remove useless rows 
my_df=my_df.loc[5:,]
test_df1=test_df1.loc[6:,]
test_df2=test_df2.loc[7:,]
my_df=my_df.append(test_df1)
my_df=my_df.append(test_df2)
my_df=my_df.groupby(['language-name']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal by reset_index() function
my_df=my_df.reset_index()
SK_dict=dict(zip(my_df['language-name'] , my_df['speakers']))


'''Meghalaya'''
my_df=pd.read_excel('Datasets/north-east/c-17-meghalaya.XLSX')
my_df=my_df[['Unnamed: 3','Unnamed: 4','Unnamed: 8','Unnamed: 9','Unnamed: 13','Unnamed: 14']]
#performing union operation of mother tongue, 2nd lang and 3rd lang column
my_df=my_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
test_df1=my_df[['Unnamed: 8','Unnamed: 9']]
test_df1.rename(columns={'Unnamed: 8':'language-name','Unnamed: 9':'speakers'},inplace=True)
test_df2=my_df[['Unnamed: 13','Unnamed: 14']]
test_df2.rename(columns={'Unnamed: 13':'language-name','Unnamed: 14':'speakers'},inplace=True)
my_df=my_df[['language-name','speakers']]
#remove NaN rows
my_df.dropna(inplace=True)
test_df1.dropna(inplace=True)
test_df2.dropna(inplace=True)
#remove useless rows 
my_df=my_df.loc[5:,]
test_df1=test_df1.loc[6:,]
test_df2=test_df2.loc[7:,]
my_df=my_df.append(test_df1)
my_df=my_df.append(test_df2)
my_df=my_df.groupby(['language-name']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal by reset_index() function
my_df=my_df.reset_index()
MG_dict=dict(zip(my_df['language-name'] , my_df['speakers']))


'''Tripura'''
my_df=pd.read_excel('Datasets/north-east/c-17-tripura.XLSX')
my_df=my_df[['Unnamed: 3','Unnamed: 4','Unnamed: 8','Unnamed: 9','Unnamed: 13','Unnamed: 14']]
#performing union operation of mother tongue, 2nd lang and 3rd lang column
my_df=my_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
test_df1=my_df[['Unnamed: 8','Unnamed: 9']]
test_df1.rename(columns={'Unnamed: 8':'language-name','Unnamed: 9':'speakers'},inplace=True)
test_df2=my_df[['Unnamed: 13','Unnamed: 14']]
test_df2.rename(columns={'Unnamed: 13':'language-name','Unnamed: 14':'speakers'},inplace=True)
my_df=my_df[['language-name','speakers']]
#remove NaN rows
my_df.dropna(inplace=True)
test_df1.dropna(inplace=True)
test_df2.dropna(inplace=True)
#remove useless rows 
my_df=my_df.loc[5:,]
test_df1=test_df1.loc[6:,]
test_df2=test_df2.loc[7:,]
my_df=my_df.append(test_df1)
my_df=my_df.append(test_df2)
my_df=my_df.groupby(['language-name']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal by reset_index() function
my_df=my_df.reset_index()
TR_dict=dict(zip(my_df['language-name'] , my_df['speakers']))


'''Arunachal Pradesh'''
my_df=pd.read_excel('Datasets/north-east/c-17-arunachal pradesh.XLSX')
my_df=my_df[['Unnamed: 3','Unnamed: 4','Unnamed: 8','Unnamed: 9','Unnamed: 13','Unnamed: 14']]
#performing union operation of mother tongue, 2nd lang and 3rd lang column
my_df=my_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
test_df1=my_df[['Unnamed: 8','Unnamed: 9']]
test_df1.rename(columns={'Unnamed: 8':'language-name','Unnamed: 9':'speakers'},inplace=True)
test_df2=my_df[['Unnamed: 13','Unnamed: 14']]
test_df2.rename(columns={'Unnamed: 13':'language-name','Unnamed: 14':'speakers'},inplace=True)
my_df=my_df[['language-name','speakers']]
#remove NaN rows
my_df.dropna(inplace=True)
test_df1.dropna(inplace=True)
test_df2.dropna(inplace=True)
#remove useless rows 
my_df=my_df.loc[5:,]
test_df1=test_df1.loc[6:,]
test_df2=test_df2.loc[7:,]
my_df=my_df.append(test_df1)
my_df=my_df.append(test_df2)
my_df=my_df.groupby(['language-name']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal by reset_index() function
my_df=my_df.reset_index()
AR_dict=dict(zip(my_df['language-name'] , my_df['speakers']))


'''Manipur'''
my_df=pd.read_excel('Datasets/north-east/c-17-manipur.XLSX')
my_df=my_df[['Unnamed: 3','Unnamed: 4','Unnamed: 8','Unnamed: 9','Unnamed: 13','Unnamed: 14']]
#performing union operation of mother tongue, 2nd lang and 3rd lang column
my_df=my_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
test_df1=my_df[['Unnamed: 8','Unnamed: 9']]
test_df1.rename(columns={'Unnamed: 8':'language-name','Unnamed: 9':'speakers'},inplace=True)
test_df2=my_df[['Unnamed: 13','Unnamed: 14']]
test_df2.rename(columns={'Unnamed: 13':'language-name','Unnamed: 14':'speakers'},inplace=True)
my_df=my_df[['language-name','speakers']]
#remove NaN rows
my_df.dropna(inplace=True)
test_df1.dropna(inplace=True)
test_df2.dropna(inplace=True)
#remove useless rows 
my_df=my_df.loc[5:,]
test_df1=test_df1.loc[6:,]
test_df2=test_df2.loc[7:,]
my_df=my_df.append(test_df1)
my_df=my_df.append(test_df2)
my_df=my_df.groupby(['language-name']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal by reset_index() function
my_df=my_df.reset_index()
MN_dict=dict(zip(my_df['language-name'] , my_df['speakers']))


'''nagaland'''
my_df=pd.read_excel('Datasets/north-east/c-17-nagaland.XLSX')
my_df=my_df[['Unnamed: 3','Unnamed: 4','Unnamed: 8','Unnamed: 9','Unnamed: 13','Unnamed: 14']]
#performing union operation of mother tongue, 2nd lang and 3rd lang column
my_df=my_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
test_df1=my_df[['Unnamed: 8','Unnamed: 9']]
test_df1.rename(columns={'Unnamed: 8':'language-name','Unnamed: 9':'speakers'},inplace=True)
test_df2=my_df[['Unnamed: 13','Unnamed: 14']]
test_df2.rename(columns={'Unnamed: 13':'language-name','Unnamed: 14':'speakers'},inplace=True)
my_df=my_df[['language-name','speakers']]
#remove NaN rows
my_df.dropna(inplace=True)
test_df1.dropna(inplace=True)
test_df2.dropna(inplace=True)
#remove useless rows 
my_df=my_df.loc[5:,]
test_df1=test_df1.loc[6:,]
test_df2=test_df2.loc[7:,]
my_df=my_df.append(test_df1)
my_df=my_df.append(test_df2)
my_df=my_df.groupby(['language-name']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal by reset_index() function
my_df=my_df.reset_index()
NG_dict=dict(zip(my_df['language-name'] , my_df['speakers']))


'''Mizoram'''
my_df=pd.read_excel('Datasets/north-east/c-17-mizoram.XLSX')
my_df=my_df[['Unnamed: 3','Unnamed: 4','Unnamed: 8','Unnamed: 9','Unnamed: 13','Unnamed: 14']]
#performing union operation of mother tongue, 2nd lang and 3rd lang column
my_df=my_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
test_df1=my_df[['Unnamed: 8','Unnamed: 9']]
test_df1.rename(columns={'Unnamed: 8':'language-name','Unnamed: 9':'speakers'},inplace=True)
test_df2=my_df[['Unnamed: 13','Unnamed: 14']]
test_df2.rename(columns={'Unnamed: 13':'language-name','Unnamed: 14':'speakers'},inplace=True)
my_df=my_df[['language-name','speakers']]
#remove NaN rows
my_df.dropna(inplace=True)
test_df1.dropna(inplace=True)
test_df2.dropna(inplace=True)
#remove useless rows 
my_df=my_df.loc[5:,]
test_df1=test_df1.loc[6:,]
test_df2=test_df2.loc[7:,]
my_df=my_df.append(test_df1)
my_df=my_df.append(test_df2)
my_df=my_df.groupby(['language-name']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal by reset_index() function
my_df=my_df.reset_index()
MZ_dict=dict(zip(my_df['language-name'] , my_df['speakers']))


'''Andaman & Nicobar'''
my_df=pd.read_excel('Datasets/north-east/c-17-andaman & nicobar islands.XLSX')
my_df=my_df[['Unnamed: 3','Unnamed: 4','Unnamed: 8','Unnamed: 9','Unnamed: 13','Unnamed: 14']]
#performing union operation of mother tongue, 2nd lang and 3rd lang column
my_df=my_df.rename(columns={'Unnamed: 3':'language-name' , 'Unnamed: 4':'speakers'})
test_df1=my_df[['Unnamed: 8','Unnamed: 9']]
test_df1.rename(columns={'Unnamed: 8':'language-name','Unnamed: 9':'speakers'},inplace=True)
test_df2=my_df[['Unnamed: 13','Unnamed: 14']]
test_df2.rename(columns={'Unnamed: 13':'language-name','Unnamed: 14':'speakers'},inplace=True)
my_df=my_df[['language-name','speakers']]
#remove NaN rows
my_df.dropna(inplace=True)
test_df1.dropna(inplace=True)
test_df2.dropna(inplace=True)
#remove useless rows 
my_df=my_df.loc[5:,]
test_df1=test_df1.loc[6:,]
test_df2=test_df2.loc[7:,]
my_df=my_df.append(test_df1)
my_df=my_df.append(test_df2)
my_df=my_df.groupby(['language-name']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal by reset_index() function
my_df=my_df.reset_index()
AN_dict=dict(zip(my_df['language-name'] , my_df['speakers']))


# ### Creation of north_east_df which stores all languages spoken in this region with their respective number of speakers

# In[27]:


#making a dataframe from each dictionary
north_east_df1=pd.DataFrame(AS_dict.items(),columns=['language','speakers'])
north_east_df2=pd.DataFrame(SK_dict.items(),columns=['language','speakers'])
north_east_df3=pd.DataFrame(MG_dict.items(),columns=['language','speakers'])
north_east_df4=pd.DataFrame(TR_dict.items(),columns=['language','speakers'])
north_east_df5=pd.DataFrame(AR_dict.items(),columns=['language','speakers'])
north_east_df6=pd.DataFrame(MN_dict.items(),columns=['language','speakers'])
north_east_df7=pd.DataFrame(NG_dict.items(),columns=['language','speakers'])
north_east_df8=pd.DataFrame(MZ_dict.items(),columns=['language','speakers'])
north_east_df9=pd.DataFrame(AN_dict.items(),columns=['language','speakers'])


#taking union of those dataframes
#note that this merge will remove duplicates when both the language name and no-of-speakers will be same in two states. We don't want this. But here that situation will not arise because matching of language and no-of-speakers of two states is nearly impossible
north_east_df=pd.merge(north_east_df1,north_east_df2,how='outer')
north_east_df=pd.merge(north_east_df,north_east_df3,how='outer')
north_east_df=pd.merge(north_east_df,north_east_df4,how='outer')
north_east_df=pd.merge(north_east_df,north_east_df5,how='outer')
north_east_df=pd.merge(north_east_df,north_east_df6,how='outer')
north_east_df=pd.merge(north_east_df,north_east_df7,how='outer')
north_east_df=pd.merge(north_east_df,north_east_df8,how='outer')
north_east_df=pd.merge(north_east_df,north_east_df9,how='outer')


'''After taking union there are multiple rows having language 'ASSAMESE'(similarly other languages also are present multiple times).
And this north_east_df contains data from all the regions.So if I group it on basis of language column and find sum of
'speakers' column within each group , I will get the total number of people who speak that language in whole region'''
north_east_df=north_east_df.groupby(['language']).sum()  #since groupby is applied, the structure of dataframe has been changed. It will be restored to normal if we store and re-load dataframe again
north_east_df.to_csv('Datasets/north-east/north-east-df.csv')  #storing dataframe
north_east_df=pd.read_csv('Datasets/north-east/north-east-df.csv')  #reloading the dataframe

north_east_df=north_east_df.sort_values(by='speakers',ascending=False).head(3)  #taking only top three rows


# ### Creation of output file region-india.csv

# In[28]:


region_india_df=pd.DataFrame(columns=['region','language-1','language-2','language-3'])

region_india_df=region_india_df.append({'region':'North','language-1':north_df['language'].iloc[0],'language-2':north_df['language'].iloc[1],'language-3':north_df['language'].iloc[2]},ignore_index=True)

region_india_df=region_india_df.append({'region':'West','language-1':west_df['language'].iloc[0],'language-2':west_df['language'].iloc[1],'language-3':west_df['language'].iloc[2]},ignore_index=True)

region_india_df=region_india_df.append({'region':'Central','language-1':central_df['language'].iloc[0],'language-2':central_df['language'].iloc[1],'language-3':central_df['language'].iloc[2]},ignore_index=True)

region_india_df=region_india_df.append({'region':'East','language-1':east_df['language'].iloc[0],'language-2':east_df['language'].iloc[1],'language-3':east_df['language'].iloc[2]},ignore_index=True)

region_india_df=region_india_df.append({'region':'South','language-1':south_df['language'].iloc[0],'language-2':south_df['language'].iloc[1],'language-3':south_df['language'].iloc[2]},ignore_index=True)

region_india_df=region_india_df.append({'region':'North-East','language-1':north_east_df['language'].iloc[0],'language-2':north_east_df['language'].iloc[1],'language-3':north_east_df['language'].iloc[2]},ignore_index=True)


region_india_df.to_csv('output files/region-india-b.csv',index=False)


# In[ ]:




