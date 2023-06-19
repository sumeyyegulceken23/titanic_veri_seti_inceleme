#!/usr/bin/env python
# coding: utf-8

# In[51]:


import seaborn as sns
titanic=sns.load_dataset("titanic")
titanic.head(50)


# # Cinsiyete göre hayatta kalma oranları

# In[52]:


sns.barplot(x="sex", y="survived", data=titanic)
plt.title("Hayatta Kalma Oranı - Cinsiyete Göre")
plt.xlabel("Cinsiyet")
plt.ylabel("Hayatta Kalma Oranı")
plt.show


# bu çalışma sonucunda en çok kadınların hayatta kalmış olduğunu görüyoruz.

# # 10-50 yaş arası  hayatta kalma oranları

# In[85]:


my_figure = plt.figure(figsize=(20, 8))
my_axes = my_figure.add_axes([0.4, 0.2, 0.6, 0.6])
age_filter = (titanic["age"] >= 10) & (titanic["age"] <= 50)
filtered_data = titanic.loc[age_filter]
sns.barplot(x="age", y="survived", data=filtered_data, ax=my_axes)
my_axes.set_title("Yaşa Göre Hayatta Kalma Oranı")
my_axes.set_xlabel("Yaş")
my_axes.set_ylabel("Hayatta Kalma Oranı")
my_axes.set_xticklabels(my_axes.get_xticklabels(), rotation=45)
plt.show()


# # Yolcuların seyahat ettiği sınıfları inceleyelim

# In[67]:


pclass_counts = titanic['pclass'].value_counts()
sns.barplot(x=pclass_counts.index, y=pclass_counts.values)


# bu analiz yaklaşık 500 kişi en iyi sınıf olan 3. sınıf seyahet etmiş 

# # Yolcukuk sınıfına göre hayatta kalma oranı

# In[69]:


sns.barplot(x="pclass", y="survived", data=titanic)
plt.title("Hayatta Kalma Oranı - yolculuk sınıfına göre")
plt.xlabel("sınıf")
plt.ylabel("Hayatta Kalma Oranı")
plt.show


# Bu analiz sonucuda şunu anlıyoruz daha çok 1.sınıf(en kötü) olan da daha çok insan ölmüş.

# # yaşlara göre hayatta kalmayı inceleyelim

# In[93]:


survived_data = titanic[titanic['survived'] == 1]
survived_age_counts = survived_data['age'].value_counts().reset_index()
survived_age_counts.columns = ['age', 'count']
survived_age_counts = survived_age_counts.sort_values('count', ascending=False)
sns.barplot(x='age', y='count', data=survived_age_counts.head(10))
plt.title("En Çok Hayatta Kalan Yaşlar")
plt.xlabel("Yaş")
plt.ylabel("Hayatta Kalan Sayısı")
plt.show


# ortalama 24 yaşın daha çok hayatta kaldığını görüyoruz

# In[ ]:




