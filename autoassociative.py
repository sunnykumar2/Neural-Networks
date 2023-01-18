import numpy as np
n = int(input("Enter Epochs- "))
#lr = float(input("Enter learning rate- "))

y = []
x = [[0 for i in range(5)] for j in range(3)]
print("\nEnter space separated X1,X2,X3,X4 and Y for the 3 classes-\n")
for i in range(3):
    z = input().split(' ')
    for j in range(4):
        x[i][j] = float(z[j])
    x[i][4] = 1
    y.append(float(z[4]))

w = [0, 0, 0, 0, 0]

for i in range(n):
    for j in range(3):
        v = 0
        for l in range(5):
            v = v+w[l]*x[j][l]
        if v > 5:
            o = 5
        elif v < -5:
            o = -5
        else:
            o = 0
        if o != y[j]:
            for k in range(4):
                w[k] = w[k]+lr*(y[j]-o)*x[j][k]
            w[6] = w[6]+lr*(y[j]-o)

print("\n\nPridections-")

z = input("Enter 4 inputs- ").split(' ')
for j in range(4):
    z[j] = float(z[j])
v = 0
for l in range(4):
    v = v+w[l]*z[l]
v += w[4]
if v > 5:
    print("Predicted class is the first class")
elif v < -5:
    print("Predicted class is the third class")
else:
    print("Predicted class is the second class")
