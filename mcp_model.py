
import numpy as np
yin1,yin2,yin3,yin4=0,0,0,0


X1=[1,0,0,1]
X2=[0,1,0,1]


print("enter the gate u want to realise")
gatename = input()

if gatename=="AND":
    Y=[X1[i] & X2[i] for i in range(0,4)]
elif (gatename=="NAND"):
    Y=[~(X1[i] & X2[i]) for i in range(0,4)]



def help(myys):
    for theta in myys:
        flag=True
        for i,y in enumerate(myys):
            if y>=theta:
                v=1
            else: v=0
            if Y[i]!=v:
                
                flag=False
                break   
                 
        if flag==True: return theta   

    return -1


            


for w1 in range(-1,2):
    for w2 in range(-1,2):
        myys=[]
        for i in range(len(X1)):
            x1=X1[i]
            x2=X2[i]
            ans=w1*x1+w2*x2
            myys.append(ans)
        print("Y input values are :- ")
        for i in range(len(myys)):
            print(myys[i],end=" ")
            print()
        mytheta=help(myys)
        if mytheta !=-1:         
            print("Final value of theta is")
            print(mytheta)




