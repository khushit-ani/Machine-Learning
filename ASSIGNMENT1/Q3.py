import numpy as np

import matplotlib.pyplot as plt

x = []
y = []

print("Enter 5 x values:")
for i in range(5):
    x.append(float(input()))

print("Enter 5 y values:")
for i in range(5):
    y.append(float(input()))

# Convert to NumPy arrays
x = np.array(x)
y = np.array(y)

n = len(x)

sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x2 = np.sum(x * x)

m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
c = (sum_y - m * sum_x) / n

print("\nRegression Equation:")
print(f"y = {m}x + {c}")

y_pred = m * x + c

print("\nIndividual Errors:")
for i in range(n):
    print(f"Point ({x[i]}, {y[i]}): Error = {y[i] - y_pred[i]}")

plt.scatter(x, y)
plt.plot(x, y_pred)
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Linear Regression with Individual Errors")
plt.show()
