#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df= pd.read_csv("SampleSuperstore.csv") #Load data set
df


# In[3]:


#Read dataset
df.dtypes


# In[4]:


df.shape


# In[5]:


df.describe()


# In[6]:


df.info()


# In[7]:


#summary for the numerical column
df.describe(include='all') 


# In[8]:


# Univariate analysis - analysis of people buying from superstore
df['Segment'].value_counts()


# In[9]:



df['Segment'].value_counts()/len(df['Segment'])*100


# In[10]:


barchart= (df['Segment'].value_counts()/len(df['Segment'])*100).plot(kind='bar',color='r')


# ### 50% people belong to Consumer class, 20%- 30% people belong to Corporate and Home offices

# In[11]:


#initialize ship mode for superstore
df['Ship Mode'].value_counts()


# In[12]:


M = (df['Ship Mode'].value_counts()/len(df['Ship Mode'])*100)


# In[13]:


M


# In[14]:



M.plot(kind= 'bar', color='b')


# #### very less % of deliveries ere made on same day 10-20% deliveries belongs to first and second class most of the deliveries belongs to the standard class

# In[15]:


#analysis categories of items in superstore
df['Category'].value_counts()


# In[16]:



c = (df['Category'].value_counts())/len(df['Category'])*100
c.plot(kind = 'bar',color='g')


# ### most of the category belongs to office supplies 20-25%belongs to furniture and technology

# In[17]:


#analyse sub-categoryof items in the superstore 
((df['Sub-Category'].value_counts())/len(df['Sub-Category'])*100).plot(kind = 'bar')


# ### 9-15% sub-category comes under office supplies 2-8%sub-category comes under technology and furniture

# # Bivariate analysis

# In[18]:


fig, ax = plt.subplots()
colors = {'Consumer':'red','Corporate':'blue','Home Office':'green'}
ax.scatter(df['Sales'],df['Profit'],c = df['Segment'].apply(lambda x :colors[x]))
plt.show()


# ### more profit observed in consumer segment

# In[19]:


df.pivot_table(values='Sales',index='Segment',columns='Discount', aggfunc='median')


# In[20]:


df.pivot_table(values ='Profit', index= 'Segment', columns= 'Discount', aggfunc = 'median')


# In[21]:


temp_df = df.loc[(df['Segment']=='Consumer')&(df['Discount']==0.1)]
temp_df['Profit'].plot.hist(bins= 50)


# In[22]:


temp_df = df.loc[(df['Segment']=='Consumer')&(df['Discount']==0.2)]
temp_df['Profit'].plot.hist(bins= 50)


# In[23]:


temp_df = df.loc[(df['Segment']=='Corporate')&(df['Discount']==0.8)]
temp_df['Profit'].plot.hist(bins= 50)


# In[24]:


temp_df = df.loc[(df['Segment']=='Consumer')&(df['Discount']==0.8)]
temp_df['Profit'].plot.hist(bins= 50)


# ###  when superstore offers discount less 40% superstore runs on profit, if discount>50% superstore runs on loss

# In[25]:


temp_df = df.loc[(df['Category']=='Furniture')&(df['Discount']==0.2)]
temp_df['Profit'].plot.hist(bins= 50)


# In[26]:


temp_df = df.loc[(df['Category']=='Technology')&(df['Discount']<=0.3)]
temp_df['Profit'].plot.hist(bins= 50)


# In[27]:


temp_df = df.loc[(df['Category']=='Technology')&(df['Discount']>=0.3)]
temp_df['Profit'].plot.hist(bins= 50)


# ### when discount <=30%, sales had profit when discount >30%, Sales had a huge loss

# In[28]:


temp = df.groupby(['Segment','Discount']).Profit.median()
temp.plot(kind = 'bar',stacked= True)


# #### Above graphs depict the sceario of profit of all segments when following discount was offered by superstore.

# In[45]:


plt.figure(figsize = (12,4))
sns.set(font_scale=1, palette= "viridis")
sns.barplot(data = df , x = "Region",y = "Profit" ,hue = "Category")
plt.show()


# ### Losses are inccured in Furniture Cateory irrespective to ship mode in Central Region

# In[49]:


#Grouping Data by Region and only slicing Data for Central Region from whole Data Set
gb_Central = list(df.groupby("Region"))[0][1]


# In[50]:


# Investing Further in cenral Region 
plt.figure(figsize = (12,4))
sns.set(font_scale=1.5, palette= "viridis")
sns.barplot(data = gb_Central, x = "Category",y = "Profit" ,hue = "Ship Mode")
plt.title("Investigation of central region: Profit making(by Ship Mode)")
plt.show()


# ### Losses are inccured in Furniture Cateory irrespective to ship mode in Central Region

# In[51]:


# Slicing Furniture Data from whole data set
gb_Category_Furniture =list(list(df.groupby("Region"))[0][1].groupby("Category"))[0][1]


# In[52]:


#Investigating individual performance by states in the central region
plt.figure(figsize = (12,8))
sns.set(font_scale=1, palette= "viridis")
sns.barplot(data = gb_Category_Furniture , x = "State",y = "Profit" ,hue = "Sub-Category")
plt.title("Investigation of Central Region Furniture Category: Profit Analysis(by Sub Category)", fontsize = 20)
plt.show()


# In[53]:


plt.figure(figsize = (12,8))
sns.set(font_scale=1, palette= "viridis")
sns.barplot(data = gb_Category_Furniture , x = "State",y = "Profit" ,hue = "Segment")
plt.title("Investigation of Central Region Furniture Category: Profit Analysis(by Segment)", fontsize = 20)
plt.show()


# In[54]:


plt.figure(figsize = (12,8))
sns.set(font_scale=1, palette= "viridis")
sns.barplot(data = gb_Category_Furniture , x = "State",y = "Discount" ,hue = "Sub-Category")
plt.title("Discounts provided by each state", fontsize = 20)
plt.show()


# In[38]:


sns.catplot("Ship Mode", hue="Segment", data=df, kind="count", aspect=1.5, palette="Set1")


# In[ ]:





# In[30]:


plt.figure(figsize=(8,5))
sns.countplot(x=df['Ship Mode'])


# In[37]:


plt.figure(figsize=(20,8))
sns.countplot(x=df['Sub-Category'])
plt.xticks(rotation=90)


# In[34]:


ds_tech=df[(df['Category']=="Technology")]


# In[35]:


plt.figure(figsize=[12,8])
ax = sns.barplot(x="Sub-Category", y="Sales", data=ds_tech, palette="magma")
plt.xlabel("Subcategories",fontsize=15)
plt.ylabel("Sales",fontsize=15)


# In[39]:


Top_10_Sales = df.groupby("State").Sales.sum().nlargest(n =10)
Top_10_Profits = df.groupby("State").Profit.sum().nlargest(n =10)


# In[40]:


Top_10_Sales.index


# In[41]:


Top_10_Profits.index


# In[42]:


plt.style.use('seaborn')
Top_10_Sales.plot(kind ='bar', figsize =(14,8), fontsize =14)
plt.xlabel("States", fontsize =13)
plt.ylabel("Total Sales",fontsize =13)
plt.title("Top 10 States by Sales",fontsize =16)
plt.show()


# In[43]:


plt.style.use('seaborn')
Top_10_Profits.plot(kind ='bar', figsize =(14,8), fontsize =14)
plt.xlabel("States", fontsize =13)
plt.ylabel("Total Profits",fontsize =13)
plt.title("Top 10 States by Profits",fontsize =16)
plt.show()


# In[ ]:




