import numpy as np
import pandas as p

r=int(input("Enter no of rows "))
c=int(input("Enter no of columns "))
a=[]

print("Enter elements")
for i in range(r):
    row=[]
    for j in range(c):
        row.append(int(input()))
    a.append(row)

print("\nOriginal list:\n",a)

np_2a=np.array(a)
print("\n2d numpy array:\n",np_2a)

np_a=np_2a.flatten()
print("\n1d numpy array:\n",np_a)

pd_series = p.Series(np_a)
print("\nPandas Series:\n")
for i, val in enumerate(pd_series):
    print(f"{i} -> {val}")


