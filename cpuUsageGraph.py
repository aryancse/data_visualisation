import time
import psutil
import matplotlib.pyplot as plt

## %matplotlib notebook ## uncomment if using jupyter notebook
plt.rcParams['animation.html'] = 'jshtml'   
#rc--> run and configure(.bashrc)
#rcParams used for handling default matplolib values
#plt.rcParams['lines.linewidth'] = 5  line ki width thick ho jaaegi
#plt.rcParams['lines.color'] = 'r'    line colour become red

fig = plt.figure()
ax = fig.add_subplot(111)
fig.show()

i = 0
x, y = [], []

while True:
    x.append(i)
    y.append(psutil.cpu_percent())
    
    ax.plot(x, y, color='b')
    
    fig.canvas.draw()
    
    ax.set_xlim(left=max(0, i-50), right=i+50)
    
    time.sleep(0.1)
    i += 1
    


plt.close()
