import numpy as np
import pandas as p

n=int(input("enter no of elements "))
a=[]
print("enter elements")
for i in range(n):
    a.append(int(input()))

np_arr=np.array(a)
p_series=p.Series(a)
p_dataframe = p.DataFrame(a, columns=["Values"])


print("\nOriginal Python List:", a)
print("\nNumPy Array:")
print(np_arr)

print("\nPandas Series:")
print(p_series)

print("\nPandas DataFrame:")
print(p_dataframe)
