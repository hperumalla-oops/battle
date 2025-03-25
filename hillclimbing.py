#chhose random starting point x
## evaluate f(x)
## x'=x+small step
## if f(x') >f(x) move to that, else stay there
#continue untel no better neighbour exists

import random
import matplotlib.pyplot as plt

def f(x):
    return (x - 2) ** 2 + 5 


x_val=[]
y_val=[]

x=0
step=1
maxiter=1000
for i in range(0,maxiter):
    x_new=x +random.randint(-step,step)/1000
    if f(x)<f(x_new):
        x=x_new
        x_val.append(x)
        y_val.append(f(x))
        

print(x, f(x))

plt.xlabel("x")  # add X-axis label
plt.ylabel("f(x)")  # add Y-axis label
plt.title("hill climbing")
plt.plot(x_val, y_val)  # Plot the chart
plt.show()


