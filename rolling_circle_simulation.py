import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import math

r,k,h=5,5,5
x=np.linspace(h-r,h+r,500)
y_upper=[]
y_lower=[]
for e in x:
    y_upper_value= math.sqrt((r**2) - ((e-h)**2)) + k
    y_upper.append(y_upper_value)
    y_lower_value=-math.sqrt((r**2) - ((e-h)**2)) + k
    y_lower.append(y_lower_value)


fig,axe=plt.subplots()
line,=axe.plot(x,y_upper)
line2,=axe.plot(x,y_lower)
line3, =axe.plot([x[0],h],[y_upper[0],k])
scatter =axe.scatter(h,k)
def update(frame):
    new_y_lower_value=[]
    new_y_upper_value=[]
    new_x=np.linspace(frame,frame+10,500)
    new_h=frame+5
    for ele in new_x:
        val = r**2 - (ele - new_h)**2
        if val >= 0:
            new_y_upper_value.append(math.sqrt(val) + k)
            new_y_lower_value.append(-math.sqrt(val) + k)
        else:
            new_y_upper_value.append(np.nan)
            new_y_lower_value.append(np.nan)
    line3.set_xdata([new_x[(frame*25)-1],new_h])
    line3.set_ydata([new_y_upper_value[(frame*25)-1],k])
    line.set_xdata(new_x)
    line.set_ydata(new_y_upper_value)
    line2.set_xdata(new_x)
    line2.set_ydata(new_y_lower_value)
    scatter.set_offsets(np.c_[new_h, k])
    scatter.set_color("Cadetblue")
    line.set_color("blue")
    line2.set_color("blue")
    


    return line,line2,line3,scatter

animation=FuncAnimation(fig=fig,func=update,frames=range(1,21,1),interval=50,repeat=False)



axe.set_xlim(0, 60)
axe.set_ylim(0, 50)
plt.grid(True)
plt.show()