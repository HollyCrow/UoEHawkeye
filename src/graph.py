# Written based on (and largly copied from) the code by Chase Lawler (Feel free to replace this as you see fit)

import pandas as pd
import matplotlib.pyplot as plt

def plot(innings): # Bounces using the dataframe from main()
    # 1st plot: Scatter plot for bounce positions
    
    plt.figure(figsize=(10, 6))
    plt.scatter(innings["BounceX"], innings["BounceY"], c="green",alpha=innings["BounceFloat"],label='Bounce Position')
    plt.title("Ball Bounce Position")
    plt.xlabel("X Position (m)")
    plt.ylabel("Y Position (m)")
    plt.grid()
    plt.legend()
    plt.show()  # Show the first plot
