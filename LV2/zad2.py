import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6), delimiter=",", skiprows=1)


mpg=data[:,0]
hp=data[:,3]
tw=data[:,5]
cln=data[:,1]
plt.scatter(mpg,hp, s=tw*5)

plt.xlabel('mpg')
plt.ylabel('hp')
plt.title('zad 2')
plt.show()

print(mpg.min())
print(mpg.max())
print(mpg.mean())

print(mpg[cln>6].min())
print(mpg[cln>6].max())
print(mpg[cln>6].mean())