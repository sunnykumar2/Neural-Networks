#!/usr/bin/env python
# coding: utf-8



import numpy as np
import matplotlib.pyplot as plt



#Input for NAND
dataset = np.array([[1, 1, 1], [1, -1, 1], [-1, 1, 1], [-1, -1, 1]]) 
out = np.array([-1, 1, 1, 1])

#Input for NOR
dataset1 = np.array([[-1, -1, 1], [-1, 1, 1], [1, -1, 1], [1, 1, 1]]) 
out1 = np.array([1, -1, -1, -1])


# In[19]:


#Hyper-paramters initialisation
w = np.zeros((3), "int") #Weights for NAND initialised with 0
w1 = np.zeros((3), "int") #Weights for NOR initialised with 0
epochs = 10
alpha = 1  #Learning Rate



for i in range(epochs):
    for j in range(4):
        w = w + alpha*out[j]*dataset[j,:] #Element wise addition in numpy array

      
for i in range(epochs):
    for j in range(4):
        w1 = w1 + alpha*out1[j]*dataset1[j,:]





print("Weights corresponding to NAND after 10 epochs: ", end = " ")
print(w)
print("Weights corresponding to NOR after 10 epochs: ", end = " ")
print(w1)



xx = np.arange(-4, 4)
plt.scatter(dataset[:, 0], dataset[:, 1], color='r')
plt.plot(xx, (-w[2]-xx*w[1])/w[0], color='b')
plt.xlabel("x-axis")
plt.ylabel("y-axis")




xx = np.arange(-4, 4)
plt.scatter(dataset1[:,0], dataset1[:,1], color='r')
plt.plot(xx, (-w1[2]-xx*w1[1])/w1[0], color='b')
plt.xlabel("x-axis")
plt.ylabel("y-axis")



dataset = np.array([[1, 1, 1], [1, 0, 1], [0, 1, 1], [0, 0, 1]]) 
out = np.array([1, 0, 0, 0])
w = np.zeros((3), "int") 
epochs = 10
alpha = 1 

for i in range(epochs):
    for j in range(4):
        w = w + alpha*out[j]*dataset[j,:] 

print("Weights corresponding to NAND after 10 epochs: ", end = " ")
print(w)

xx = np.arange(-4, 4)
plt.scatter(dataset[:, 0], dataset[:, 1], color='r')
plt.plot(xx, (-w[2]-xx*w[1])/w[0], color='b')
plt.xlabel("x-axis")
plt.ylabel("y-axis")



