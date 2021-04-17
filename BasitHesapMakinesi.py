#!/usr/bin/env python
# coding: utf-8

# In[8]:


print("Yapmak istediğiniz işlemi ve sayıları giriniz.")
islem=input("islem:")
a=int(input())
b=int(input())
print("{}{}{}".format(a,islem,b))

if islem=="+":
    print("Sonuc=",a+b)
elif islem=="-":
    print("Sonuc=",a-b)
elif islem=="*":
     print("Sonuc=",a*b)
elif islem=="/":
    print("Sonuc=",a/b)


# In[ ]:




