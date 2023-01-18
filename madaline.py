X1 = [1, 1, -1, -1]
X2 = [1, -1, 1, -1]
R3 = [-1, 1, 1, -1]

v1 = 0.5
v2 = 0.5
b2 = 0.5
#print("Enter the value of b1,w11 and w12")
b0 = 0.3
w11 = 0.05
w21 = 0.2

#print("Enter the value of b2,w12 and w22")

b1 = 0.15
w12 = 0.1
w22 = 0.2
#alpha=(input("Enter the value of alpha"))
alpha = 0.5

f = False
epoch = 0
while(f == False):
    f = True
    print("Epoch ",end=" ")
    print(epoch)
    epoch = epoch+1
    for i in range(0, 4):
        Yin1 = b0+w11*X1[i]+w21*X2[i]
        Yin2 = b1+w12*X1[i]
        Yin2 = Yin2+w22*X2[i]
        print("Yin1 ", end=" ")
        print(Yin1)
        print("Yin2 ", end=" ")
        print(Yin2)

        if(Yin1 >= 0):
            Y1 = 1
        else:
            Y1 = -1
        if(Yin2 >= 0):
            Y2 = 1
        else:
            Y2 = -1
        print("Y1 ", end=" ")
        print(Y1)
        print("Y2 ", end=" ")
        print(Y2)
        Y3 = b2+Y1*v1+Y2*v2
        print("Y3 ", end=" ")
        print(Y3)
        if(Y3 >= 0):
            Y = 1
        else:
            Y = -1
        if(R3[i] != Y):
            print("Updating ")
            f=False
            if(R3[i] == -1):
                if(Yin1 > 0):
                    b0 = b0+alpha*(R3[i]-Yin1)
                    w11 = w11+alpha*(R3[i]-Yin1)*X1[i]
                    w21 = w21+alpha*(R3[i]-Yin1)*X2[i]
                if(Yin2 > 0):
                    b1 = b1+alpha*(R3[i]-Yin2)
                    w12 = w12+alpha*(R3[i]-Yin2)*X1[i]
                    w22 = w22+alpha*(R3[i]-Yin2)*X2[i]
            else:
                if(abs(Yin1)>abs(Yin2)):
                    b1 = b1+alpha*(R3[i]-Yin2)
                    w12 = w12+alpha*(R3[i]-Yin2)*X1[i]
                    w22 = w22+alpha*(R3[i]-Yin2)*X2[i]
                else:
                    b0 = b0+alpha*(R3[i]-Yin1)
                    w11 = w11+alpha*(R3[i]-Yin1)*X1[i]
                    w21 = w21+alpha*(R3[i]-Yin1)*X2[i]
                    

        print("b0 ", end=" ")
        print(b0)
        print("w11 ", end=" ")
        print(w11)
        print("w21 ", end=" ")
        print(w21)
        print("b1 ", end=" ")
        print(b1)
        print("w12 ", end=" ")
        print(w12)
        print("w22 ", end=" ")
        print(w22)
