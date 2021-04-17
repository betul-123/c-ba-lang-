#!/usr/bin/env python
# coding: utf-8

# In[4]:


print(*range(0,20))


# In[6]:


print(*range(0,36,5))


# In[8]:


a="python"
a[::-1]


# In[9]:


liste=[1,2,3,4,5]
liste.pop(3)
liste


# In[10]:


liste.append(7)


# In[11]:


liste


# In[15]:


print(liste.sort())


# In[17]:


liste1=[1,2,3,4,5,6]
liste2=[i for i in liste1]
liste2


# In[18]:


liste3=[(1,2),(3,4),(5,6)]
liste4=[i*j for i,j in liste3]
liste4


# In[20]:


liste5=[[1,2,3],[4,5,6],[7,8,9,10]]
liste6=[x for i in liste5  for x in i]
liste6


# In[21]:


liste5=[[1,2,3],[4,5,6],[7,8,9,10]]
liste6=list()


# In[22]:


liste6


# In[23]:


for i in liste5:
    for x in i:
        liste6.append(x)
print(liste6)


# In[27]:


name="Betul"
password="12345"
i=3
while i>0:
      kullanici_Adi=input("Lütfen kullanici adınızı giriniz.")
      sifre=input("Lütfen sifrenizi giriniz.")
      if name==kullanici_Adi and sifre==password:
            print("Sisteme giris yapılıyor.")
            break
      else:
            print("Kullanici adi ya da parola hatali")
            i-=1


# In[ ]:





# In[ ]:




