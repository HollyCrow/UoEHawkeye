# Written based on (and largly copied from) the code by Chase Lawler (Feel free to replace this as you see fit)

import pandas as pd
import matplotlib.pyplot as plt

def plot(innings): # Bounces using the dataframe from main()
    # Code from here on is written pretty much entirly by Chase

    # 1st plot: Scatter plot for bounce positions
    plt.figure(figsize=(10, 6))
    plt.scatter(innings["BounceX"], innings["BounceY"], label='Bounce Position', alpha=0.6)
    plt.title("Ball Bounce Position")
    plt.xlabel("X Position (m)")
    plt.ylabel("Y Position (m)")
    plt.grid()
    plt.legend()
    plt.show()  # Show the first plot
    
    # 2nd plot: Trajectory data
    plt.figure(figsize=(10, 6))
    for index, row in innings.iterrows():
        points_x = [20.12, row["BounceX"], 0]
        points_z = [row["BowlerReleaseZposition"], 0, row["StumpsZ"]] # The caps consistency in the dataset is agravating - Holly
        plt.plot(points_x, points_z, marker='o', alpha=0.3)

    plt.title("Bowler Trajectory")
    plt.xlabel("X Position (m)")
    plt.ylabel("Z Position (m)")
    plt.grid()
    plt.show()  # Show the second plot
