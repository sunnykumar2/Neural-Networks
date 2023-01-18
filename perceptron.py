import numpy as np

x = [1, 1, -1, -1]
y = [1, -1, -1, 1]

R1 = [1, -1, -1, -1]
R3 = [1, 1, 1, -1]
R2 = [-1, -1, 1, -1]
print("Choose options ")
print("1.AND")
print("2.OR")
print("3.ANDNOT")
option = input()
b = input("Enter the value of b")
w1 = input("Enter the value of w1")
w2 = input("Enter the value of w2")
theta = input("Enter the value of Theta ")
alpha = input("Enter the value of alpha")


def solve(x, y, R1, b, w1, w2, theta, alpha):
    epoch = 1
    f = False
    while(f == False and epoch < 5):
        f = True
        print("Epoch", end=" ")
        print(epoch)
        for i in range(0, 4):
            yin = b
            print(x[i])
            print(y[i])
            yin = yin+x[i]*w1+y[i]*w2
            print(yin)
            print("Yin for ", end=" ")
            print(i, end=" ")
            print("th pair", end=" ")
            print(yin)
            # apply activation
            Y = 0
            if(yin > theta):
                Y = 1
            else:
                Y = -1

            if(Y != R1[i]):
                w1 = w1+alpha*x[i]*R1[i]
                w2 = w2+alpha*y[i]*R1[i]
                b = b+alpha*R1[i]
                f = False
            print("After", end=" ")
            print(i, end=" ")
            print("th pair w1 ", end=" ")
            print(w1, end=" ")
            print("w2 ", end=" ")
            print(w2, end=" ")
            print("b", end=" ")
            print(b)
        print("After", end=" "),
        print(epoch, end=" "),
        print("th w1", end=" ")
        print(w1, end=" ")
        print("w2", end=" ")
        print(w2, end=" ")
        print("b", end=" ")
        print(b)
        epoch = epoch+1
    return


if(option == "AND"):
    solve(x, y, R1, b, w1, w2, theta, alpha)
elif(option == 'OR'):
    solve(x, y, R3, b, w1, w2, theta, alpha)
else:
    solve(x, y, R2, b, w1, w2, theta, alpha)
