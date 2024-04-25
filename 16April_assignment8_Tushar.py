import numpy as np
import matplotlib.pyplot as plt


y  = [140,155,159,179,192,200,212,215]
x1 = [60,62,67,70,71,72,75,78]
x2 = [22,25,24,20,15,14,14,11]

plt.scatter(x1,y)
plt.scatter(x2,y)

n = len(x1)

X1_square = []
for i in x1:
  X1_square.append(i*i)

X2_square = []
for i in x2:
  X2_square.append(i*i)

X1_y = []
for i in range(len(y)):
  X1_y.append(x1[i] * y[i])

X2_y = []
for i in range(len(y)):
  X2_y.append(x2[i] * y[i])

X1_X2 = []
for i in range(len(x2)):
  X1_X2.append(x1[i] * x2[i])

x1_2 = sum(X1_square) - (sum(x1) * sum(x1))/n;
x2_2 = sum(X2_square) - (sum(x2) * sum(x2))/n
x1_y = sum(X1_y) - (sum(x1) * sum(y)) / n
x2_y = sum(X2_y) - (sum(x2) * sum(y)) / n
x1_x2 = sum(X1_X2) - (sum(x1) * sum(x2)) / n

b1 = (x2_2 * x1_y - x1_x2 * x2_y) / (x1_2 * x2_2 - (x1_x2 * x1_x2))
print(b1)

b2 = (x1_2 * x2_y - x1_x2 * x1_y) / (x1_2 * x2_2 - x1_x2 * x1_x2)
print(b2)

b0 = sum(y)/len(y) - b1 * sum(x1)/len(x1) - b2 * sum(x2)/len(x2)
print(b0)

def mlr(x1,x2):
  return b0 + b1 * x1 + b2 * x2