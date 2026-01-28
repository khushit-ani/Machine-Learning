import numpy as np
import pandas as p

r=int(input("enter no of rows"))
c=int(input("enter no of columns"))
a=[]

for i in range(r):
    row=[]
    for j in range(c):
        row.append(int(input()))
    a.append(row)

print("\noriginal list:\n",a)

np_2a=np.array(a)
print("\n2d numpy array:\n",np_2a)

np_a=np_2a.flatten()
print("\n1d numpy array:\n",np_a)

pd_series = p.Series(np_a)
print("\nPandas Series:\n",pd_series)

p_series=p.Series(a)
print("\npandas series:\n",p_series)

df=p.DataFrame(np_2a)
p_1d=df.stack()
print("\n1d panda array:\n",p_1d)

