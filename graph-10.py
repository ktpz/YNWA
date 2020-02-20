import numpy as np
import matplotlib.pyplot as plt
import math

#Plot the quadratic function y = ax2 + bx + c
#Varying each coefficient [a, b, c] separately while the other coefficients are fixed (at values a = 1, b = 0, c = 0)

#Iterate these 5 coefficients and plot each line
coefs = [-2, -1, 0, 1, 2]

#set up the plot and 3 subplots (to show the effect of varying each coefficient)
f, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=True, figsize=(18, 6))

#some x values to plot
x = np.linspace(-2, 2, 30)

for idx, val in enumerate([ax1, ax2, ax3]):

    for v in coefs:        
        a, b, c = 1, 0, 0

        if idx == 0:
            a = v
        elif idx == 1:
            b = v
        else:
            c = v

        y = a * (x**2) + (b * x) + c

        val.plot(x, y, label="Coeficient is " + str(coefs[v]))

        val.axhline(y=0, color='k')
        val.axvline(x=0, color='k')    
        val.grid()
        val.legend(loc='lower center')

plt.show()