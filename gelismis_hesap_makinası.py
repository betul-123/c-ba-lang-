#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
from math import *
print("------------------------------------------------------\n"
       "1=acos(x, /)\n"
    
       "2=acosh(x, /)\n"
    
        "3=asin(x, /)\n"
        "Return the arc sine (measured in radians) of x.\n"
    
        "4=asinh(x, /)\n"
        "Return the inverse hyperbolic sine of x.\n"
    
         "5=atan(x, /)\n"
          " Return the arc tangent (measured in radians) of x.\n"
    
         "7=atanh(x, /)\n"
         "Return the inverse hyperbolic tangent of x.\n"
    
         "8=comb(n, k, /)\n"
         "Number of ways to choose k items from n items without repetition and without order.\n"
        
         "Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates\n"
         " to zero when k > n.\n"
        
         "Also called the binomial coefficient because it is equivalent\n"
         "to the coefficient of k-th term in polynomial expansion of the\n"
         "expression (1 + x)**n."        
        "Raises TypeError if either of the arguments are not integers.\n"
        "Raises ValueError if either of the arguments are negative.\n"
      
        "9= cos(x, /)\n"
        "Return the cosine of x (measured in radians).\n"
    
        "10=cosh(x, /)\n"
        "Return the hyperbolic cosine of x.\n"
    
        "11=degrees(x, /)\n"
        "Convert angle x from radians to degrees.\n"
    
    
        "12=sin(x, /)\n"
        "Return the sine of x (measured in radians).\n"
    
        "13=sinh(x, /)\n"
         "Return the hyperbolic sine of x.\n"
    
        "14=sqrt(x, /)\n"
        "Return the square root of x.\n"
    
        "15=tan(x, /)\n"
         "Return the tangent of x (measured in radians).\n"
    
       "16=tanh(x, /)\n"
        "Return the hyperbolic tangent of x.\n"
    
   "  --------------------------------------------------------------------- ")
    
def hesap_makinesi(x):
    islem=int(input("Lütfen yapmak istediğiniz işlemi seçiniz."))
    if islem==1:
        math.acos(x)
    elif islem==2:
        math.asin(x)
    elif islem==3:
        math.acosh(x)
    elif islem==4:
        math.asinh(x)
    elif islem==5:
        math.atan(x)
    
    elif islem==7:
        math.atanh(x)
    elif islem==8:
        k=int(input())
        math.comb(x,k)
    elif islem==9:
        math.cos(x)
    elif islem==10:
        math.cosh(x)
    elif islem==11:
        math.degrees(x)
    elif islem==12:
        math.sin(x)
    elif islem==13:
        math.sinh(x)
    elif islem==14:
        math.sqrt(x)
    elif islem==15:
        math.tan(x)
    elif islem==16:
        math.tanh(x)
        return True
while True:
    x=int(input())
    print(hesap_makinesi(x))
    
        
        


# In[ ]:




