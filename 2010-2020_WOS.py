
# coding: utf-8

# In[3]:


import session_info
session_info.show()


# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import seaborn as sns


# In[2]:


import plotly.express as px


# In[3]:


df2010=pd.read_csv("WOS2010_full.csv")
df2015=pd.read_csv("WOS2015_full.csv")
df2020=pd.read_csv("WOS2020_full.csv")


# In[3]:


df2010.describe(percentiles=[0.25, 0.5, 0.75, 0.95, 0.96, 0.97, 0.98, 0.99, 0.995, 0.999, 0.9999]).style.format("{:.2f}")


# In[4]:


df2015.describe(percentiles=[0.25, 0.5, 0.75, 0.95, 0.96, 0.97, 0.98, 0.99, 0.995, 0.999, 0.9999]).style.format("{:.2f}")


# In[5]:


df2020.describe(percentiles=[0.25, 0.5, 0.75, 0.95, 0.96, 0.97, 0.98, 0.99, 0.995, 0.999, 0.9999]).style.format("{:.2f}")


# In[3]:


# function to get unique values
def unique(list1):

    # initialize a null list
    unique_list = []

    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    # print list
    #for x in unique_list:
     #   print(x)
    return unique_list


# In[7]:


print(len(unique(df2010['Publisher'])), 'unique publishers in 2010')
print(len(unique(df2015['Publisher'])), 'unique publishers in 2015')
print(len(unique(df2020['Publisher'])), 'unique publishers in 2020')

print(len(unique(df2010['Source Title'])), 'unique journals in 2010')
print(len(unique(df2015['Source Title'])), 'unique journals in 2015')
print(len(unique(df2020['Source Title'])), 'unique journals in 2020')


# # Combine publishers

# In[7]:


keys = df2010['Publisher'].str.contains('ELSEVIER', case=False, na=False)

unique(df2010[keys]['Publisher'])


# In[8]:


df2010['Publisher_new']=''


# In[9]:


df2010.loc[keys, 'Publisher_new']='ELSEVIER affiliates'


# In[10]:


keys_1 = df2010['Publisher'].str.contains('WILEY', case=False, na=False)
unique(df2010[keys_1]['Publisher'])


# In[11]:


df2010.loc[keys_1, 'Publisher_new']='WILEY affiliates'


# In[12]:


keys_2 = df2010['Publisher'].str.contains('SPRINGER', case=False, na=False)
unique(df2010[keys_2]['Publisher'])


# In[13]:


df2010.loc[keys_2, 'Publisher_new']='SPRINGER affiliates'


# In[14]:


keys_10 = df2010['Publisher'].str.contains('NATURE ', case=False, na=False) #add space for naturelle
unique(df2010[keys_10]['Publisher'])


# In[15]:


df2010.loc[keys_10, 'Publisher_new']='NATURE affiliates'
keys_fix = df2010['Publisher'].str.contains('SOC NATL PROTECTION NATURE ACCLIMATATION FRANCE', case=False, na=False) 
df2010.loc[keys_fix, 'Publisher_new']='SOC NATL PROTECTION NATURE ACCLIMATATION FRANCE'


# In[17]:


words=['SPRINGERNATURE', 'SPRINGER NATURE SWITZERLAND AG', 'SPRINGER NATURE, CO-PUBL CTR EXCELLENCE GENOMIC MED RES']
pattern = '|'.join(words)
result = df2010.loc[~df2010['Publisher'].str.contains(pattern, case=False)]
df2010.loc[df2010['Publisher'].str.contains(pattern, case=False),'Publisher_new']='SPRINGERNATURE'
df2010[df2010['Publisher']=='SPRINGER NATURE SWITZERLAND AG']


# In[16]:


words2=['Routledge', 'Taylor & Francis']
tnfpattern='|'.join(words2)
keys_3 = df2010['Publisher'].str.contains(tnfpattern, case=False, na=False)
unique(df2010[keys_3]['Publisher'])
df2010.loc[keys_3, 'Publisher_new']='Routledge T&F affiliates'


# In[18]:


keys_4 = df2010['Publisher'].str.contains('IEEE', case=False, na=False)
unique(df2010[keys_4]['Publisher'])
df2010.loc[keys_4, 'Publisher_new']='IEEE affiliates'
keys_5 = df2010['Publisher'].str.contains('Wiley-IEEE', case=False, na=False)
df2010.loc[keys_5, 'Publisher_new']='WILEY affiliates'


# In[19]:


keys_6 = df2010['Publisher'].str.contains('SAGE ', case=False, na=False)
unique(df2010[keys_6]['Publisher'])
df2010.loc[keys_6, 'Publisher_new']='SAGE affiliates'


# In[20]:


keys_fix2 = df2010['Publisher'].str.contains('CORNELL UNIV SAGE SCHOOL PHILOSOPHY', case=False, na=False) 
df2010.loc[keys_fix2, 'Publisher_new']='CORNELL UNIV SAGE SCHOOL PHILOSOPHY'
keys_7 = df2010['Publisher'].str.contains('Oxford', case=False, na=False)
df2010[keys_7]['Publisher'].value_counts()
df2010.loc[keys_7, 'Publisher_new']='Oxford affiliates'
df2010['Publisher_new'].value_counts()


# In[21]:


keys_8 = df2010['Publisher'].str.contains('SPIE', case=False, na=False)
df2010[keys_8]['Publisher'].value_counts()
df2010.loc[keys_8, 'Publisher_new']='SPIE affiliates'
key_9=df2010['Publisher'].str.contains('SOC ETUDES ROBESPIERRISTES', case=False, na=False)
df2010.loc[key_9, 'Publisher_new']='SOC ETUDES ROBESPIERRISTE'


# In[22]:


df2010['Publisher_new'] = np.where(df2010['Publisher_new'] == '', df2010['Publisher'], df2010['Publisher_new'])


# In[23]:


words3=['BMJ', 'B M J']
bmjpattern='|'.join(words3)
keys_10 = df2010['Publisher'].str.contains(bmjpattern, case=False, na=False)
df2010[keys_10]['Publisher'].value_counts()
df2010.loc[keys_10, 'Publisher_new']='BMJ PUBLISHING' #not adding affiliates here since 2020 data only contains BMJ


# In[24]:


keys_11 = df2010['Publisher'].str.contains('MARY ANN', case=False, na=False)
df2010[keys_11]['Publisher'].value_counts()
df2010.loc[keys_11, 'Publisher_new']='MARY ANN LIEBERT, INC' #not adding affiliates since comma difference only


# In[35]:


df2010['Publisher_new'].value_counts().nlargest(25)


# In[26]:


len(df2010[df2010['Publisher']=='MDPI']) #rank 77, not even in top 100 if we hadn't combined


# In[27]:


df2010['Publisher'].value_counts().nlargest(110) #rank 110


# In[28]:


#combining for 2020
keys = df2020['Publisher'].str.contains('ELSEVIER', case=False, na=False)
df2020['Publisher_new']=''
df2020.loc[keys, 'Publisher_new']='ELSEVIER affiliates'
keys_1 = df2020['Publisher'].str.contains('WILEY', case=False, na=False)
df2020.loc[keys_1, 'Publisher_new']='WILEY affiliates'
keys_2 = df2020['Publisher'].str.contains('SPRINGER', case=False, na=False)
df2020.loc[keys_2, 'Publisher_new']='SPRINGER affiliates'
keys_10 = df2020['Publisher'].str.contains('NATURE ', case=False, na=False) #add space for naturelle
df2020.loc[keys_10, 'Publisher_new']='NATURE affiliates'
words=['SPRINGERNATURE', 'SPRINGER NATURE SWITZERLAND AG', 'SPRINGER NATURE, CO-PUBL CTR EXCELLENCE GENOMIC MED RES']
pattern = '|'.join(words)
result = df2020.loc[~df2020['Publisher'].str.contains(pattern, case=False)]
df2020.loc[df2020['Publisher'].str.contains(pattern, case=False),'Publisher_new']='SPRINGERNATURE'
words2=['Routledge', 'Taylor & Francis']
tnfpattern='|'.join(words2)
keys_3 = df2020['Publisher'].str.contains(tnfpattern, case=False, na=False)
df2020.loc[keys_3, 'Publisher_new']='Routledge T&F affiliates'
keys_4 = df2020['Publisher'].str.contains('IEEE', case=False, na=False)
df2020.loc[keys_4, 'Publisher_new']='IEEE affiliates'
keys_5 = df2020['Publisher'].str.contains('Wiley-IEEE', case=False, na=False)
df2020.loc[keys_5, 'Publisher_new']='WILEY affiliates'
keys_6 = df2020['Publisher'].str.contains('SAGE ', case=False, na=False)
df2020.loc[keys_6, 'Publisher_new']='SAGE affiliates'
keys_7 = df2020['Publisher'].str.contains('Oxford', case=False, na=False)
df2020.loc[keys_7, 'Publisher_new']='Oxford affiliates'
keys_8 = df2020['Publisher'].str.contains('SPIE', case=False, na=False)
df2020.loc[keys_8, 'Publisher_new']='SPIE affiliates'
key_9=df2020['Publisher'].str.contains('SOC ETUDES ROBESPIERRISTES', case=False, na=False)
df2020.loc[key_9, 'Publisher_new']='SOC ETUDES ROBESPIERRISTE'
df2020['Publisher_new'] = np.where(df2020['Publisher_new'] == '', df2020['Publisher'], df2020['Publisher_new'])


# In[30]:


#BMJ and Mary Ann Liebert not needed for 2020
keys_11 = df2020['Publisher'].str.contains('MARY ANN', case=False, na=False)
df2020[keys_11]['Publisher'].value_counts()


# In[36]:


df2020['Publisher_new'].value_counts().nlargest(25)


# In[ ]:


#Combining for 2015


# In[39]:


keys = df2015['Publisher'].str.contains('ELSEVIER', case=False, na=False)
print(unique(df2015[keys]['Publisher']))


# In[40]:


df2015['Publisher_new']=''
df2015.loc[keys, 'Publisher_new']='ELSEVIER affiliates'
keys_1 = df2015['Publisher'].str.contains('WILEY', case=False, na=False)
print(unique(df2015[keys_1]['Publisher']))


# In[41]:


df2015.loc[keys_1, 'Publisher_new']='WILEY affiliates'
keys_2 = df2015['Publisher'].str.contains('SPRINGER', case=False, na=False)
print(unique(df2015[keys_2]['Publisher']))


# In[42]:


df2015.loc[keys_2, 'Publisher_new']='SPRINGER affiliates'
keys_10 = df2015['Publisher'].str.contains('NATURE ', case=False, na=False) #add space for naturelle
unique(df2015[keys_10]['Publisher'])


# In[43]:


df2015.loc[keys_10, 'Publisher_new']='NATURE affiliates'
keys_fix = df2015['Publisher'].str.contains('SOC NATL PROTECTION NATURE ACCLIMATATION FRANCE', case=False, na=False) 
df2015.loc[keys_fix, 'Publisher_new']='SOC NATL PROTECTION NATURE ACCLIMATATION FRANCE'


# In[44]:


words=['SPRINGERNATURE', 'SPRINGER NATURE SWITZERLAND AG', 'SPRINGER NATURE, CO-PUBL CTR EXCELLENCE GENOMIC MED RES']
pattern = '|'.join(words)
result = df2015.loc[~df2015['Publisher'].str.contains(pattern, case=False)]
df2015.loc[df2015['Publisher'].str.contains(pattern, case=False),'Publisher_new']='SPRINGERNATURE'
#df2015[df2015['Publisher']=='SPRINGER NATURE SWITZERLAND AG']


# In[45]:


words2=['Routledge', 'Taylor & Francis']
tnfpattern='|'.join(words2)
keys_3 = df2015['Publisher'].str.contains(tnfpattern, case=False, na=False)
unique(df2015[keys_3]['Publisher'])
df2015.loc[keys_3, 'Publisher_new']='Routledge T&F affiliates'


# In[46]:


keys_4 = df2015['Publisher'].str.contains('IEEE', case=False, na=False)
unique(df2015[keys_4]['Publisher'])
df2015.loc[keys_4, 'Publisher_new']='IEEE affiliates'
keys_5 = df2015['Publisher'].str.contains('Wiley-IEEE', case=False, na=False)
df2015.loc[keys_5, 'Publisher_new']='WILEY affiliates'


# In[47]:


keys_6 = df2015['Publisher'].str.contains('SAGE ', case=False, na=False)
print(unique(df2015[keys_6]['Publisher']))
df2015.loc[keys_6, 'Publisher_new']='SAGE affiliates'


# In[48]:


keys_fix2 = df2015['Publisher'].str.contains('CORNELL UNIV SAGE SCHOOL PHILOSOPHY', case=False, na=False) 
df2015.loc[keys_fix2, 'Publisher_new']='CORNELL UNIV SAGE SCHOOL PHILOSOPHY'
keys_7 = df2015['Publisher'].str.contains('Oxford', case=False, na=False)
df2015[keys_7]['Publisher'].value_counts()
df2015.loc[keys_7, 'Publisher_new']='Oxford affiliates'
df2015['Publisher_new'].value_counts()


# In[49]:


keys_8 = df2015['Publisher'].str.contains('SPIE', case=False, na=False)
df2015[keys_8]['Publisher'].value_counts()
df2015.loc[keys_8, 'Publisher_new']='SPIE affiliates'
key_9=df2015['Publisher'].str.contains('SOC ETUDES ROBESPIERRISTES', case=False, na=False)
df2015.loc[key_9, 'Publisher_new']='SOC ETUDES ROBESPIERRISTE'


# In[50]:


df2015['Publisher_new'] = np.where(df2015['Publisher_new'] == '', df2015['Publisher'], df2015['Publisher_new'])


# In[52]:


words3=['BMJ', 'B M J']
bmjpattern='|'.join(words3)
keys_10 = df2015['Publisher'].str.contains(bmjpattern, case=False, na=False)
df2015[keys_10]['Publisher'].value_counts()


# In[32]:


#df2015.loc[keys_10, 'Publisher_new']='BMJ PUBLISHING GROUP' #not adding affiliates here since 2020 data only contains BMJ


# In[53]:


keys_11 = df2015['Publisher'].str.contains('MARY ANN', case=False, na=False)
df2015[keys_11]['Publisher'].value_counts()
#df2015.loc[keys_11, 'Publisher_new']='MARY ANN LIEBERT, INC' #not adding affiliates since comma difference only


# In[57]:


df2015['Publisher_new'].value_counts().nlargest(31) #MDPI ranked 31 after combining, 52 before combining


# In[3]:


keys_12 = df2010['Publisher'].str.contains('GEOLOGICAL SOC AMER', case=False, na=False)
df2010[keys_12]['Publisher'].value_counts()


# In[4]:


df2010.loc[keys_12, 'Publisher_new']='GEOLOGICAL SOC AMER, INC'


# In[5]:


keys_12 = df2015['Publisher'].str.contains('GEOLOGICAL SOC AMER', case=False, na=False)
df2015[keys_12]['Publisher'].value_counts()


# In[6]:


df2015.loc[keys_12, 'Publisher_new']='GEOLOGICAL SOC AMER, INC'


# In[7]:


keys_12 = df2020['Publisher'].str.contains('GEOLOGICAL SOC AMER', case=False, na=False)
df2020[keys_12]['Publisher'].value_counts()


# In[8]:


df2020.loc[keys_12, 'Publisher_new']='GEOLOGICAL SOC AMER, INC'


# In[9]:


#update files:
df2010.to_csv("WOS2010_full.csv", index=False)
df2015.to_csv("WOS2015_full.csv", index=False)
df2020.to_csv("WOS2020_full.csv", index=False)


# ### Look at weird pubs and journals
# 
# pubs in both years - corresponding ranks in both years: scatterplots of their ranks
# look at publishers in common - 2010 and 2020

# In[4]:


pubs10=pd.DataFrame()
pubs20=pd.DataFrame()


# In[5]:


pubs10['Pub']=df2010['Publisher_new']
pubs20['Pub']=df2020['Publisher_new']


# In[6]:


pubs10['Counts'] = pubs10.groupby('Pub')['Pub'].transform('count')
pubs20['Counts'] = pubs20.groupby('Pub')['Pub'].transform('count')


# In[7]:


pubs10=pubs10.drop_duplicates()
pubs20=pubs20.drop_duplicates()


# In[14]:


pubs10


# In[8]:


pubs10['Rank']=pubs10['Counts'].rank(ascending=False)
pubs20['Rank']=pubs20['Counts'].rank(ascending=False)


# In[25]:


pubs20


# In[9]:


mergedpubs= pd.merge(pubs10, pubs20, how='outer', on='Pub', suffixes=('_10', '_20'))


# In[16]:


mergedpubs


# In[10]:


mergedpubs=mergedpubs.dropna(axis=0)


# In[20]:


mergedpubs


# In[21]:


#plt.figure(figsize=(12, 7))
fig, ax = plt.subplots(figsize=(12, 7))
plt.scatter(mergedpubs.Rank_10, mergedpubs.Rank_20)
plt.show()


# In[133]:


#pip install plotly


# In[13]:


#import plotly.express as px


# In[11]:


fig = px.scatter(mergedpubs, x=mergedpubs.Rank_10, y=mergedpubs.Rank_20, color=mergedpubs.Pub)
fig.update_layout(showlegend=False, width=900, height=900)
fig.show()


# In[92]:


pattern='SOPHIA PUBLICATIONS'
mask = df2010['Publisher'].str.contains(pattern, case=False, na=False)
df2010[mask]


# In[93]:


mask = df2020['Publisher'].str.contains(pattern, case=False, na=False)
df2020[mask]


# In[12]:


#merging first then plotting if it affects the ranks
df_10= pd.DataFrame({'Pub': mergedpubs['Pub'], 'Counts': mergedpubs['Counts_10']})
df_20= pd.DataFrame({'Pub': mergedpubs['Pub'], 'Counts': mergedpubs['Counts_20']})


# In[13]:


df_10['Rank']=df_10['Counts'].rank(ascending=False)
df_20['Rank']=df_20['Counts'].rank(ascending=False)


# In[14]:


merging= pd.merge(df_10, df_20, how='outer', on='Pub', suffixes=('_10', '_20'))


# In[22]:


merging


# In[15]:


fig = px.scatter(merging, x=merging.Rank_10, y=merging.Rank_20, color=merging.Pub)
fig.update_layout(showlegend=False, width=900, height=900)
fig.show()


# In[16]:


merging['Rank change']= merging['Rank_10']-merging['Rank_20']


# In[17]:


merging[merging['Rank change']==0]


# In[18]:


merging[merging['Rank change']>0]


# In[19]:


merging[merging['Rank change']<0]


# In[33]:


merging[merging['Rank change']>0].describe()


# In[31]:


merging[merging['Rank change']<0].describe()


# In[20]:


sns.histplot(merging, x='Rank change')
plt.show()


# Likely a Cauchy Distribution

# In[21]:


import statsmodels.api as sm


# In[22]:


fig = sm.qqplot(merging['Rank change'])
plt.show()


# In[25]:


journal_10=pd.DataFrame({'Title': df2010['Source Title']})
journal_20=pd.DataFrame({'Title': df2020['Source Title']})


# In[26]:


journal_10['Counts'] = journal_10.groupby('Title')['Title'].transform('count')
journal_20['Counts'] = journal_20.groupby('Title')['Title'].transform('count')


# In[27]:


journal_10['JRank']=journal_10['Counts'].rank(ascending=False)
journal_20['JRank']=journal_20['Counts'].rank(ascending=False)


# In[28]:


# drop duplicates here when re-running
journal_10=journal_10.drop_duplicates()
journal_20=journal_20.drop_duplicates()


# In[29]:


Jmerging= pd.merge(journal_10, journal_20, how='outer', on='Title', suffixes=('_10', '_20'))


# In[30]:


#Jmerging=Jmerging.drop_duplicates()
#Jmerging


# In[31]:


Jmerging=Jmerging.dropna(axis=0)


# In[11]:


Jmerging


# In[15]:


fig = px.scatter(Jmerging, x=Jmerging.JRank_10, y=Jmerging.JRank_20, color=Jmerging.Title)
fig.update_layout(showlegend=False, width=900, height=900)
fig.show()


# In[32]:


Jmerging['Rank change']= Jmerging['JRank_10']-Jmerging['JRank_20']


# In[33]:


fig = sm.qqplot(Jmerging['Rank change'])
plt.show()


# In[34]:


sns.histplot(Jmerging, x='Rank change')
plt.show()


# In[35]:


#merging first then plotting if it affects the ranks
df_10= pd.DataFrame({'Title': Jmerging['Title'], 'Counts': Jmerging['Counts_10']})
df_20= pd.DataFrame({'Title': Jmerging['Title'], 'Counts': Jmerging['Counts_20']})


# In[36]:


df_10['Rank']=df_10['Counts'].rank(ascending=False)
df_20['Rank']=df_20['Counts'].rank(ascending=False)


# In[37]:


merging= pd.merge(df_10, df_20, how='outer', on='Title', suffixes=('_10', '_20'))


# In[39]:


merging['Rank change']= merging['Rank_10']-merging['Rank_20']


# In[40]:


merging.head()


# In[41]:


sns.histplot(merging, x='Rank change')
plt.show()


# In[42]:


fig = sm.qqplot(merging['Rank change'])
plt.show()


# In[44]:


fig = px.scatter(merging, x=merging.Rank_10, y=merging.Rank_20, color=merging.Title)
fig.update_layout(showlegend=False, width=700, height=700)
fig.show()


# # UR Data

# In[26]:


pattern='(University of Rochester)|URMC'
mask = df2010['Authors with Aff text'].str.contains(pattern, case=False, na=False)
df2010[mask].head()


# In[27]:


UR2010 = df2010[mask]
UR2010.describe()


# In[28]:


mask = df2015['Authors with Aff text'].str.contains(pattern, case=False, na=False)
UR2015 = df2015[mask]
UR2015.describe()


# In[29]:


mask = df2020['Authors with Aff text'].str.contains(pattern, case=False, na=False)
UR2020 = df2020[mask]
UR2020.describe()


# In[12]:


fig, ax =plt.subplots(1,3, figsize=(14,7))
sns.histplot(UR2010, x="Number of Affiliations", binwidth=2, ax=ax[0]).set_title("2010")
sns.histplot(UR2015, x="Number of Affiliations", binwidth=2, ax=ax[1]).set_title("2015")
sns.histplot(UR2020, x="Number of Affiliations", binwidth=2, ax=ax[2]).set_title("2020")
fig.suptitle("Distribution plot for affiliations in UR's data")
plt.show()


# In[13]:


fig, ax =plt.subplots(1,3, figsize=(12,8))
sns.histplot(UR2010, x="No. of Authors", binwidth=2, ax=ax[0]).set_title("2010")
sns.histplot(UR2015, x="No. of Authors", binwidth=2, ax=ax[1]).set_title("2015")
sns.histplot(UR2020, x="No. of Authors", binwidth=2, ax=ax[2]).set_title("2020")
fig.suptitle("Distribution plot for authors in UR's data")
plt.show()


# In[14]:


UR10subset=UR2010[UR2010['No. of Authors']<=25]
UR15subset=UR2015[UR2015['No. of Authors']<=25]
UR20subset=UR2020[UR2020['No. of Authors']<=25]


# In[15]:


fig, ax =plt.subplots(1,3, figsize=(14,7), sharey=True)
sns.histplot(UR10subset, x="Number of Affiliations", binwidth=2, color="green", ax=ax[0]).set_title("2010")
sns.histplot(UR15subset, x="Number of Affiliations", binwidth=2, color="green", ax=ax[1]).set_title("2015")
sns.histplot(UR20subset, x="Number of Affiliations", binwidth=2, color="green", ax=ax[2]).set_title("2020")
fig.suptitle("Distribution plot for affiliations in UR's data with Authors<=25")
plt.show()


# In[16]:


fig, ax =plt.subplots(1,3, figsize=(14,7), sharey=True)
sns.histplot(UR10subset, x="No. of Authors", binwidth=2, color="green", ax=ax[0]).set_title("2010")
sns.histplot(UR15subset, x="No. of Authors", binwidth=2, color="green", ax=ax[1]).set_title("2015")
sns.histplot(UR20subset, x="No. of Authors", binwidth=2, color="green", ax=ax[2]).set_title("2020")
fig.suptitle("Distribution plot for authors in UR's data with Authors<=25")
plt.show()


# In[17]:


fig, ax =plt.subplots(1,3, figsize=(14,7), sharey=True)
sns.histplot(UR10subset, x="No. of Authors with Aff", binwidth=2, color="green", ax=ax[0]).set_title("2010")
sns.histplot(UR15subset, x="No. of Authors with Aff", binwidth=2, color="green", ax=ax[1]).set_title("2015")
sns.histplot(UR20subset, x="No. of Authors with Aff", binwidth=2, color="green", ax=ax[2]).set_title("2020")
fig.suptitle("Distribution plot for authors with affiliations in UR's data with Authors<=25")
plt.show()


# In[18]:


UR10supset=UR2010[UR2010['No. of Authors']>25]
UR15supset=UR2015[UR2015['No. of Authors']>25]
UR20supset=UR2020[UR2020['No. of Authors']>25]


# In[19]:


fig, ax =plt.subplots(1,3, figsize=(14,7), sharey=True)
sns.histplot(UR10supset, x="Number of Affiliations", binwidth=2, color="purple", ax=ax[0])
sns.histplot(UR15supset, x="Number of Affiliations", binwidth=2, color="purple", ax=ax[1])
sns.histplot(UR20supset, x="Number of Affiliations", binwidth=2, color="purple", ax=ax[2])
fig.suptitle("Distribution plot for affiliations in UR's data with Authors>25")
plt.show()


# In[20]:


fig, ax =plt.subplots(1,3, figsize=(14,9), sharey=True, sharex=True)
sns.histplot(UR10supset, x="Number of Affiliations", binwidth=2, color="purple", ax=ax[0])
sns.histplot(UR15supset, x="Number of Affiliations", binwidth=2, color="purple", ax=ax[1])
sns.histplot(UR20supset, x="Number of Affiliations", binwidth=2, color="purple", ax=ax[2])
fig.suptitle("Distribution plot for affiliations in UR's data with Authors>25")
plt.show()


# In[21]:


#fig, ax =plt.subplots(1,3, figsize=(14,7))
#sns.histplot(UR10supset, x="No. of Authors with Aff", binwidth=2, color="purple", ax=ax[0]).set_title("2010")
#sns.histplot(UR15supset, x="No. of Authors with Aff", binwidth=2, color="purple", ax=ax[1]).set_title("2015")
#sns.histplot(UR20supset, x="No. of Authors with Aff", binwidth=2, color="purple", ax=ax[2]).set_title("2020")
#fig.suptitle("Distribution plot for Authors having affiliations in UR's data with Authors>25")
#plt.show()


# In[22]:


#fig, ax =plt.subplots(1,2, figsize=(14,7))
g1 = sns.displot(UR10supset, x="No. of Authors with Aff", binwidth=2, color="purple")
g2 = sns.displot(UR15supset, x="No. of Authors with Aff", binwidth=2, color="purple")
g3 = sns.displot(UR20supset, x="No. of Authors with Aff", binwidth=2, color="purple")
mean1=round((UR10supset["No. of Authors with Aff"].mean()),2)
med1=round((UR10supset["No. of Authors with Aff"].median()),2)
mean2=round((UR15supset["No. of Authors with Aff"].mean()),2)
med2=round((UR15supset["No. of Authors with Aff"].median()),2)
mean3=round((UR20supset["No. of Authors with Aff"].mean()),2)
med3=round((UR20supset["No. of Authors with Aff"].median()),2)
sd1 = round(np.std(UR10supset["No. of Authors with Aff"]),2)
sd2 = round(np.std(UR15supset["No. of Authors with Aff"]),2)
sd3 = round(np.std(UR20supset["No. of Authors with Aff"]),2)
fig.suptitle("Distribution plot for UR data having >25 authors") #histogram
x_var="No. of Authors with Aff"
for (row, col, hue_idx), data in g1.facet_data():
    # Skip empty data
    if not data.values.size:
        continue

    # Get the ax for `row` and `col`
    ax = g1.facet_axis(row, col)
    # Set the `vline`s using the var `x_var`
    ax.axvline(data[x_var].mean(), c="k", ls="-", lw=1.0)
    ax.axvline(data[x_var].median(), c="orange", ls="--", lw=1.0)
    ax.set_title("2010")
print("2010: mean=", mean1, "; median=", med1, "; sd=", sd1, ";")

for (row, col, hue_idx), data in g2.facet_data():
    # Skip empty data
    if not data.values.size:
        continue

    # Get the ax for `row` and `col`
    ax = g2.facet_axis(row, col)
    # Set the `vline`s using the var `x_var`
    ax.axvline(data[x_var].mean(), c="k", ls="-", lw=1.0)
    ax.axvline(data[x_var].median(), c="orange", ls="--", lw=1.0) 
    ax.set_title("2015")
print("2015: mean=", mean2, "; median=", med2, "; sd=", sd2, ";")
    
for (row, col, hue_idx), data in g3.facet_data():
    # Skip empty data
    if not data.values.size:
        continue

    # Get the ax for `row` and `col`
    ax = g3.facet_axis(row, col)
    # Set the `vline`s using the var `x_var`
    ax.axvline(data[x_var].mean(), c="k", ls="-", lw=1.0)
    ax.axvline(data[x_var].median(), c="orange", ls="--", lw=1.0)  
    ax.set_title("2020")
print("2020: mean=", mean3, "; median=", med3, "; sd=", sd3, ";")


# In[23]:


round((UR20supset["No. of Authors with Aff"].median()),2)


# # Binning data by number of authors
# Bins: opt1: 0-2, 3-5, 6-8, 9-11, 12-14, 15-17, 18-20, 21+
# 
# opt 2: 0-1, 2-3, 4-5, 6-7, 8-9, 10-11, 12-13, 14-15, 16-17, 18-19, 20+
# going with opt 2

# In[24]:


binned_authors_10 = pd.cut(UR2010["No. of Authors"].astype('Int64'), [0,1,3,5,7,8,9,11,13,15,17,19,3199], include_lowest=True)


# In[25]:


UR2010['Authors binned']=binned_authors_10


# In[26]:


#sns.catplot(x='Authors binned', y='Number of Affiliations', data=UR2010, height=8)
#plt.xticks(rotation=90)
#plt.show()


# In[27]:


binned_authors_15 = pd.cut(UR2015["No. of Authors"].astype('Int64'), [0,1,3,5,7,8,9,11,13,15,17,19,5091], include_lowest=True)
UR2015['Authors binned']=binned_authors_15


# In[28]:


binned_authors_20 = pd.cut(UR2020["No. of Authors"].astype('Int64'), [0,1,3,5,7,8,9,11,13,15,17,19,5156], include_lowest=True)
UR2020['Authors binned']=binned_authors_20
#sns.catplot(x='Authors binned', y='Number of Affiliations', data=UR2020, height=8)
#plt.xticks(rotation=90)
#plt.title("2020")
#plt.show()


# In[29]:


#fig, ax =plt.subplots(1,3, figsize=(14,8))
#sns.stripplot(x='Number of Affiliations', y='Authors binned',  data=UR2010, ax=ax[0]).set_title("2010")
#sns.stripplot(x='Number of Affiliations', y='Authors binned',  data=UR2015, ax=ax[1]).set_title("2015")
#sns.stripplot(x='Number of Affiliations', y='Authors binned', data=UR2020, ax=ax[2]).set_title("2020")
#fig.suptitle("Plots for affiliations against authors after binning")
#plt.subplots_adjust(wspace = 0.4)
#plt.show()
#sns.catplot(x='Authors binned', y='Number of Affiliations', data=UR2020, height=8)
#plt.xticks(rotation=90)
#plt.title("2020")
#plt.show()


# In[30]:


print("Plots for affiliations against authors after binning")
fig, ax = plt.subplots(figsize=(8,8), sharex=True)
sns.stripplot(x='Number of Affiliations', y='Authors binned',  data=UR2010).set_title("2010")
ax.set_xlim(0,600)
plt.show()
fig, ax = plt.subplots(figsize=(8,8))
sns.stripplot(x='Number of Affiliations', y='Authors binned',  data=UR2015).set_title("2015")
ax.set_xlim(0,600)
plt.show()
fig, ax = plt.subplots(figsize=(8,8))
sns.stripplot(x='Number of Affiliations', y='Authors binned', data=UR2020).set_title("2020")
ax.set_xlim(0,600)
plt.show()
#fig.suptitle("Plots for affiliations against authors after binning")


# In[33]:


sns.scatterplot(data=UR2010, x="No. of Authors", y="Number of Affiliations")
plt.show()


# In[36]:


#test = pd.DataFrame()
#test['Affiliations']=UR2010['Number of Affiliations']
#test['Author count']=UR2010['No. of Authors']
#test['binned_authors_10'] = pd.cut(test["Author count"].astype('Int64'), [0,1,3,5,7,8,9,11,13,15,17,19,3199], include_lowest = True)
#sns.catplot(x='binned_authors_10', y='Affiliations', data=test, height=8)
#plt.xticks(rotation=90)
#plt.show()


# In[32]:


sns.jointplot(data=UR2010, x="No. of Authors", y="Number of Affiliations", kind="reg", truncate=False)
plt.show()
sns.jointplot(data=UR2015, x="No. of Authors", y="Number of Affiliations", kind="reg", truncate=False)
plt.show()
sns.jointplot(data=UR2020, x="No. of Authors", y="Number of Affiliations", kind="reg", truncate=False)
plt.show()
#https://seaborn.pydata.org/examples/regression_marginals.html


# # UR Top affiliations
# #look at trends in bins until 20 authors

# In[36]:


binned_authors_10 = pd.cut(UR2010["No. of Authors"].astype('Int64'), [0,1,3,5,7,8,9,11,13,15,17,19,21,23,25], include_lowest=True)
UR2010['Authors binned']=binned_authors_10
binned_authors_15 = pd.cut(UR2015["No. of Authors"].astype('Int64'), [0,1,3,5,7,8,9,11,13,15,17,19,21,23,25], include_lowest=True)
UR2015['Authors binned']=binned_authors_15
binned_authors_20 = pd.cut(UR2020["No. of Authors"].astype('Int64'), [0,1,3,5,7,8,9,11,13,15,17,19,21,23,25], include_lowest=True)
UR2020['Authors binned']=binned_authors_20


# In[50]:


print("Plots for affiliations against authors after binning, limiting to 25 authors")
fig, ax = plt.subplots(figsize=(12,8), sharex=True)
sns.stripplot(x='Number of Affiliations', y='Authors binned',  data=UR2010).set_title("2010")
#ax.set_xlim(0,35)
plt.xticks(range(0,36))
plt.show()
fig, ax = plt.subplots(figsize=(12,8))
sns.stripplot(x='Number of Affiliations', y='Authors binned',  data=UR2015).set_title("2015")
#ax.set_xlim(0,35)
plt.xticks(range(0,36))
plt.show()
fig, ax = plt.subplots(figsize=(12,8))
sns.stripplot(x='Number of Affiliations', y='Authors binned', data=UR2020).set_title("2020")
#ax.set_xlim(0,35)
plt.xticks(range(0,36))
plt.show()


# In[ ]:


#pull out 1 author and how many people they work with?
#look at UR and who are our most common affiliations
#bins by # of authors - scatter plots, maybe regression
#parse 2010


# In[49]:


pattern='Tarduno'
mask = df2010['All Authors'].str.contains(pattern, case=False, na=False)
df2010[mask]


# In[51]:


mask = df2015['All Authors'].str.contains(pattern, case=False, na=False)
df2015[mask]


# In[52]:


mask = df2020['All Authors'].str.contains(pattern, case=False, na=False)
df2020[mask]


# In[70]:


pattern='Gonek, SM'
mask = UR2010['All Authors'].str.contains(pattern, case=False, na=False)
UR2010[mask]


# In[71]:


mask = UR2015['All Authors'].str.contains(pattern, case=False, na=False)
UR2015[mask]


# In[72]:


mask = UR2020['All Authors'].str.contains(pattern, case=False, na=False)
UR2020[mask]


# In[80]:


pattern='lambropoulos'
mask = UR2010['All Authors'].str.contains(pattern, case=False, na=False)
UR2010[mask]


# In[81]:


mask = UR2015['All Authors'].str.contains(pattern, case=False, na=False)
UR2015[mask]


# In[82]:


mask = UR2020['All Authors'].str.contains(pattern, case=False, na=False)
UR2020[mask]


# In[89]:


pattern='luo, jb'
mask = UR2010['All Authors'].str.contains(pattern, case=False, na=False)
UR2010[mask]


# In[90]:


mask = UR2015['All Authors'].str.contains(pattern, case=False, na=False)
UR2015[mask]


# In[91]:


mask = UR2020['All Authors'].str.contains(pattern, case=False, na=False)
UR2020[mask]


# In[96]:


len(UR2020[mask]) #43 in WOS


# In[92]:


df2010[df2010['UID']=='WOS:000286932600009'] #AFFILIATION WAS KODAK


# In[93]:


UR2010[UR2010['UID']=='WOS:000286932600009']

