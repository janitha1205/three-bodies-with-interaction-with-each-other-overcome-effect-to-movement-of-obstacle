import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
def fobs(x,y,x0,y0):
  d=np.sqrt((x-x0)**2+(y-y0)**2)
  kobs=10
  return kobs/d**2
def target(x,y,xd,yd):
  d=np.sqrt((x-xd)**2+(y-yd)**2)
  ktar=100
  return ktar*d,ktar/d**2
def focus(x,y,xd,yd,x0,y0):
    tar_score,ftar=target(x,y,xd,yd)
    fob=fobs(x,y,x0,y0)
    if ftar>fob:
        kv=0.003
        V=kv*tar_score
        theta=np.atan((yd-y)/(xd-x) )
        return V*np.cos(theta),V*np.sin(theta)
    else:
        theta=np.atan(fob/ftar)
        kob=0.3
        v=fob*kob
        return v*np.cos(theta),v*np.sin(theta)
        
mobs=10
m=5.9
x1=1.5
x3=3.5
x2=2.9
y1=0.2
y3=0.5
y2=2.5

xd1,yd1,xd2,yd2,xd3,yd3=10.5,7.2,3.9,7.5,5.5,8.5
dt=0.01
t=0

x0=3.2
y0=1.2
v0x=-0.10
v0y=-0.10
t11=[]

x11=[]
x22=[]
x33=[]
y11=[]
y22=[]
y33=[]
x00=[]
y00=[]

while t<40:

     

      
       

        vx1,vy1=focus(x1,y1,xd1,yd1,x0,y0)
       


        vx2,vy2=focus(x2,y2,xd2,yd2,x0,y0)

        vx3,vy3=focus(x3,y3,xd3,yd3,x0,y0)




        x1+=vx1*dt
        y1+=vy1*dt 


        x2+=vx2*dt
        y2+=vy2*dt 



        x3+=vx3*dt
        y3+=vy3*dt

        x0+=v0x*dt
        y0+=v0y*dt

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


# 1. Define your X and Y arrays (Example: a spiral path)
# Replace these with your own numpy arrays or lists
theta = t11
x_data = x22
y_data = y22
num_frames = len(x_data)  # Total number of frames in the animation

trajectories = [
    {"name": "particle A", "color": "teal",     "x": x11,     "y": y11},
    {"name": "particle B", "color": "crimson",  "x": x22, "y": y22},
    {"name": "particle C", "color": "darkorange","x": x33, "y": y33},
    {"name": "Obstacle", "color": "black","x": x00, "y": y00},
]

# 2. Setup the plot canvas
fig, ax = plt.subplots(figsize=(8, 8))
ax.grid(True, linestyle='--', alpha=0.5)
ax.set_title("Multi-Trajectory Tracker", fontsize=12, fontweight='bold')

# Find global min/max bounds across all trajectories to set static plot limits
all_x = np.concatenate([t["x"] for t in trajectories])
all_y = np.concatenate([t["y"] for t in trajectories])
ax.set_xlim(np.min(all_x) - 1, np.max(all_x) + 1)
ax.set_ylim(np.min(all_y) - 1, np.max(all_y) + 1)

# 3. Create plot objects dynamically and store them in lists
lines = []
dots = []

for t in trajectories:
    # Build trail line
    line, = ax.plot([], [], color=t["color"], alpha=0.5, linewidth=2, label=f"{t['name']} Trail")
    lines.append(line)
    # Build leading dot particle
    dot, = ax.plot([], [], marker='o', color=t["color"], markersize=8, label=t["name"])
    dots.append(dot)

ax.legend(loc='lower right')

# Create a telemetry text container anchored to the top-left corner
telemetry_text = ax.text(
    0.05, 0.95, '', 
    transform=ax.transAxes, 
    fontsize=9, 
    fontfamily='monospace',
    verticalalignment='top', 
    bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.8, edgecolor='gray')
)

# 4. Initialization function
def init():
    for line, dot in zip(lines, dots):
        line.set_data([], [])
        dot.set_data([], [])
    telemetry_text.set_text('')
    # Return all graphical elements that change
    return lines + dots + [telemetry_text]

# 5. Animation update loop (runs for every frame index 'i')
def update(i):
    text_output = f"Frame: {i:03d} / {num_frames}\n"
    text_output += "=" * 25 + "\n"
    
    # Iterate through each trajectory index and update its respective line/dot
    for idx, t in enumerate(trajectories):
        # Update trailing path line segment
        lines[idx].set_data(t["x"][:i+1], t["y"][:i+1])
        
        # Update current step head dot position
        current_x = t["x"][i]
        current_y = t["y"][i]
        dots[idx].set_data([current_x], [current_y])
        
        # Append telemetry data for this specific point to the screen readout
        text_output += f"{t['name']}: X={current_x:5.2f} | Y={current_y:5.2f}\n"
        
    telemetry_text.set_text(text_output.strip())
    
    # Return flat list of updated artists
    return lines + dots + [telemetry_text]

# 6. Instantiate and run animation
ani = FuncAnimation(
    fig, 
    update, 
    frames=len(x11), 
    init_func=init, 
    interval=40, 
    blit=True
)

# Uncomment to render video file output:
# ani.save('multi_trajectory.mp4', writer='ffmpeg', fps=25)

plt.show()


