#!/usr/bin/env python
# coding: utf-8

# In[109]:


for i in range(2000,3201):
    if i%7 == 0 and i%5 != 0:
        print(i,)


# In[3]:


first_name = input()
last_name =  input()
print("%s %s"%(last_name,first_name))
print("{} {}".format(last_name,first_name))
print("{1} {0}".format(first_name,last_name))
print(last_name+" "+first_name)


# In[55]:


import math
d = 12
r = d/2
v = (4*math.pi*r*r*r)/3
print(v)


# In[56]:


v = ''
for i in range(0,6):
    print(i * '*')
    if i == 5:
        for j in range(1,i):
            #print(j)
            print((i-j) * '*')


# In[54]:


string = input()
rev = ''
for i in string:
    rev = i + rev
print(rev)
    


# In[110]:


print("WE, THE PEOPLE OF INDIA, \n\t having solemnly resolved to constitute India into a SOVEREIGN,! \n \t \t SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC \n \t \t and to secure to all its citizens")

