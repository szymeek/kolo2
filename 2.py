import numpy as np
import matplotlib.pyplot as plt

# x = np.linspace(-2, 6, endpoint=True, num=50)
x = np.arange(-2, 6.1, 0.1)
y1 = ((-4)*(np.power(x, 2))) + ((6*x)/2) + 20
# y1 = ((-4)*(x*x)) + ((6*x)/2) + 20
y2 = (np.tan(x)) - 5

fig, (ax1, ax2, ax3) = plt.subplots(3, figsize=(10, 10))

ax1.plot(x, y1, 'ro', label='1')
ax1.grid()
ax1.set_xlim(-2, 4)
ax1.set_ylim(-25, 25)
ax1.set_yticks(np.arange(-25, 26, step=25))
ax1.legend(loc='lower center')
ax1.set_title('wykres 1')

ax2.plot(x, y2, 'b-', label='2')
ax2.grid()
ax2.set_ylim(-45, 82)
ax2.set_yticks(np.arange(-40, 81, step=20))
ax2.legend()
ax2.set_title('wykres 2')

# ax3.plot(x, y1, 'ro', x, y2, 'b-')
ax3.plot(x, y1, 'ro', label='1')
ax3.plot(x, y2, 'b-', label='2')
ax3.grid()
ax3.set_xlim(-2, 6)
ax3.set_ylim(-100, 100)
ax3.set_yticks(np.arange(-100, 100, step=25))
ax3.legend()
ax3.set_title('wykres 3')

plt.subplots_adjust(hspace=0.5)
# plt.figure(figsize=(10, 10))

plt.show()

