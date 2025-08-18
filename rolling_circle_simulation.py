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

#initial plot before animation
line,=axe.plot(x,y_upper)
line2,=axe.plot(x,y_lower)
line3, =axe.plot([x[0],h],[y_upper[0],k])
scatter =axe.scatter(h,k)

#frame_list
frame_list=list(enumerate(list(range(1,21,1))+list(range(19,-1,-1))))

#animation function
def update(frame_tuple):
    #forward rolling
    frame_index,frame = frame_tuple
    if frame_index <= 19:
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
    
    # reverse animation (backward rolling)
    else:
        reverse_y_lower=[]
        reverse_y_upper=[]
        _new_x=np.linspace(frame,frame +10,500)
        _new_h=frame+5
        for ele in _new_x:
            _val=r**2-(ele-_new_h)**2
            if _val >= 0:
                reverse_y_upper.append(math.sqrt(_val) + k)
                reverse_y_lower.append(- math.sqrt(_val) + k)
            else:
                reverse_y_upper.append(np.nan)
                reverse_y_lower.append(np.nan)
        line.set_xdata(_new_x)
        line.set_ydata(reverse_y_upper)
        line2.set_xdata(_new_x)
        line2.set_ydata(reverse_y_lower)
        line3.set_xdata([_new_x[(frame*25)-1],_new_h] if frame>0 else [frame,_new_h])
        line3.set_ydata([reverse_y_lower[(frame*25)-1],k] if frame >0 else [5,k])
        scatter.set_offsets(np.c_[_new_h, k])
        scatter.set_color("Cadetblue")
        line.set_color("orange")
        line2.set_color("orange")
        
    return line,line2,line3,scatter


animation=FuncAnimation(fig=fig,func=update,frames=frame_list,interval=50,repeat=False)
axe.set_xlim(0, 60)
axe.set_ylim(0, 60)
axe.set_aspect('equal', adjustable='box')
plt.grid(True)
plt.title("Rolling circle simulation")
plt.show()