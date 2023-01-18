import numpy as np
import random
s = ["10101", "10111", "11100", "10001"]
val = 1/len(s[0])
for j in range(len(s)):
    for i in range(len(s[j])):
        x = random.random()
        if(x < val):
            if(s[j][i] == '0'):
                s[j][i] = '1'
            elif(s[j][i] == '1'):
                s[j][i] = '0'
for j in range(len(s)):
    print(s[j])
