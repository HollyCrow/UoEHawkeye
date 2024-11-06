# Written based on (and largly copied from) the code by Chase Lawler (Feel free to replace this as you see fit)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def plot(innings): # Bounces using the dataframe from main()
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
    plt.scatter(innings["BounceX"], innings["BounceY"], c="green",alpha=[abs(x - 0.5)*2 for x in innings["BounceFloat"]],label='Bounce Position')
    plt.title("Ball Bounce Position")
    plt.xlabel("X Position (m)")
    plt.ylabel("Y Position (m)")
    plt.grid()
    plt.legend()
    plt.show()  # Show the first plot
