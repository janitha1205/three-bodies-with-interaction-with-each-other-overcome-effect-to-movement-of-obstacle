import numpy as np
import matplotlib.pyplot as plt
mobs=0.3
m=5.9
x1=1.5
x3=3.5
x2=2.9
y1=0.2
y3=0.5
y2=2.5
x1dot=0
y1dot=0
x2dot=0
y2dot=0
x3dot=0
y3dot=0
dt=0.0001
t=0

x0=0.2
y0=0.2
v0x=10.3
v0y=10.2
t11=[]

x01=np.sqrt((x1-x2)**2+(y1-y2)**2)
x02=np.sqrt((x2-x3)**2+(y2-y3)**2)
x03=np.sqrt((x1-x3)**2+(y1-y3)**2)
x11=[]
y11=[]
x22=[]
y22=[]
x33=[]
y33=[]
x00=[]
y00=[]
d10_l=(x1-x0)**3+(y1-y0)**3
d20_l=(x2-x0)**3+(y2-y0)**3
d30_l=(x3-x0)**3+(y3-y0)**3
while t<10:

        d10=(x1-x0)**3+(y1-y0)**3
        d20=(x2-x0)**3+(y2-y0)**3
        d30=(x3-x0)**3+(y3-y0)**3
        theta1=np.arctan2((y1-y0),(x1-x0))+np.pi/2      
        theta2=np.arctan2((y2-y0),(x2-x0))+np.pi/2
        theta3=np.arctan2((y3-y0),(x3-x0))+np.pi/2
        if d10_l>=d10:
            F10=mobs/d10
        else:
            F10=0
        if d20_l>=d20:
            F20=mobs/d20
        else:
            F20=0
        if d30_l>=d30:
            F30=mobs/d30
        else:
            F30=0   

        
        d10_l=d10
        d20_l=d20
        d30_l=d30
        d12=np.sqrt((x1-x2)**2+(y1-y2)**2)
        d13=np.sqrt((x1-x3)**2+(y1-y3)**2)
        d23=np.sqrt((x2-x3)**2+(y2-y3)**2)
        theta12=np.arctan2((y1-y2),(x1-x2))
        theta13=np.arctan2((y1-y3),(x1-x3))
        theta23=np.arctan2((y2-y3),(x2-x3))
        k12=0.3
        k13=0.5
        k23=0.1
        F12=k12*(-d12+x01)
        F13=k13*(-d13+x03)
        F23=k23*(-d23+x02)


        x1dotdot=(F10*np.cos(theta1)+F12*np.cos(theta12)+F13*np.cos(theta13))/m
        y1dotdot=(F10*np.sin(theta1)+F12*np.sin(theta12)+F13*np.sin(theta13))/m


        x2dotdot=(F20*np.cos(theta2)+F12*np.cos(theta12)+F23*np.cos(theta23))/m
        y2dotdot=(F20*np.sin(theta2)+F12*np.sin(theta12)+F23*np.sin(theta23))/m


        x3dotdot=(F30*np.cos(theta3)+F23*np.cos(theta23)+F13*np.cos(theta13))/m
        y3dotdot=(F30*np.sin(theta3)+F23*np.sin(theta23)+F13*np.sin(theta13))/m

        x1dot+=x1dotdot*dt
        y1dot+=y1dotdot*dt

        x1+=x1dot*dt
        y1+=y1dot*dt 

        x2dot+=x2dotdot*dt
        y2dot+=y2dotdot*dt

        x2+=x2dot*dt
        y2+=y2dot*dt 

        x3dot+=x3dotdot*dt
        y3dot+=y3dotdot*dt

        x3+=x3dot*dt
        y3+=y3dot*dt

        x11.append(x1)
        y11.append(y1)
        x22.append(x2)
        y22.append(y2)
        x33.append(x3)
        y33.append(y3)
        x00.append(x0)
        y00.append(y0)   
        t11.append(t)

        t+=dt
        x0+=v0x*dt
        y0+=v0y*dt    

# 3. Plot each line individually and assign a 'label' for the legend
plt.plot(x11, y11, color='blue', label='particle 1')
#plt.plot(t11, y11, color='red',   label='y11')
plt.plot(x22, y22, color='green', label='particle 2')
#plt.plot(t11, y22, color='purple', label='y22')
plt.plot(x33, y33, color='orange', label='particle 3')
#plt.plot(t11, y33, color='brown', label='y33')
plt.plot(x00, y00, color='black', label='obstacle')
# 4. Add titles, labels, and turn on the grid
plt.title("Plotting Multiple Lines")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)

# 5. Display the legend (uses the 'label' tags from step 3)
plt.legend()

# 6. Show the final graph
plt.show()
