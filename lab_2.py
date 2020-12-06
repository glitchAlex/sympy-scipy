from scipy import linalg
import matplotlib.pyplot as plt
import numpy as np

#input
file_path = 'C:\DEV\\lol2.txt'
f = open(file_path, 'r')
size = int(f.readline())
data = np.loadtxt(file_path, skiprows=1)
A = data[0:size]
b = data[size]
f.close()

#main
x = np.linspace(1, size, size)
plt.bar(x, linalg.solve(A, b), align='center')
plt.title('Solutions')
plt.grid()
plt.show()

print('\nturtle')