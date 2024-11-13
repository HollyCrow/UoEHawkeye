# Written based on (and largly copied from) the code by Chase Lawler (Feel free to replace this as you see fit)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def plot_bounce_map(innings): # Bounces using the dataframe from main()
    # 1st plot: Scatter plot for bounce positions
    
    # Fix the plot to the pitch size and dimentions
    plt.figure(figsize=(10, 6))
    plt.xlim(-11.28, 11.28)
    plt.ylim(-1.82, 1.83)

    # Draw the wickets
    currentAxis = plt.gca()
    currentAxis.add_patch(Rectangle((10.06, -0.2), 0.125, 0.4, facecolor="none", ec='k', lw=2))
    currentAxis.add_patch(Rectangle((-10.06, -0.2), -0.125, 0.4, facecolor="none", ec='k', lw=2))
    
    # Draw all the bounce datapoints. abs(x-0.5)*2 to make it a bit more obvios because pretty much every datapoint is between 0.5 and 1.
    #plt.scatter(innings["BounceX"], innings["BounceY"], c="green",alpha=[abs(x - 0.5)*2 for x in innings["BounceFloat"]],label='Bounce Position',s=200)
    x = innings["BounceFloat"].to_numpy()
    plt.scatter(innings["BounceX"], innings["BounceY"], cmap="YlGn",c=(x-np.min(x))/(np.max(x)-np.min(x)),label='Bounce Position',s=200, edgecolors='black', linewidth=1)
    plt.title("Ball Bounce Position")
    plt.xlabel("X Position (m)")
    plt.ylabel("Y Position (m)")
    plt.grid()
    plt.legend()
    plt.show()  # Show the first plot

def plot_bounce_timeline(innings):
    plt.figure()
    plt.ylim(0, 1)
    plt.scatter(innings["BounceTimeStamp"], innings["BounceFloat"], c=innings["BounceFloat"])
    plt.xlabel("Time / Seconds")
    plt.ylabel("Bounce Float / Unitless")
    plt.title("Bouncyness Over Time")
    plt.grid()
    plt.legend()
    plt.show()
