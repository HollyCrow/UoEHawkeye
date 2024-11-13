from data_loading import load_innings
from bounce import calc_bounce
from graph import plot_bounce_map,plot_bounce_timeline
import pandas as pd
from datetime import datetime

def main():
    data = { # Dataframe format for output.
        "BounceX": [],
        "BounceY": [],
        "BounceFloat": [],
        "BounceTimeStamp": []
    }
    data = pd.DataFrame(data) # Convert "data" into a pandas DataFrame


    # I have a vague recollection that windows requires \ rather than / for file paths?
    inning = load_innings("./data/Coaching.csv")
    for index, row in inning.iterrows():
        # Whatever processing happens should be decided by Understanding the data 1&2.
        # This is a placeholder. Position should probably also be tracked. Later problem.
        try:
            bounce_value = calc_bounce(row)
            bounce_time = datetime.strptime(row["TrajectoryDate"]+row["TrajectoryTime"], " %Y/%m/%d %H:%M:%S") # TODO: write code to make the timestamp timezone-sensetive
            #print(bounce_time.timestamp())
            data.loc[len(data.index)] = [row["BounceX"], row["BounceY"], bounce_value, bounce_time.timestamp()]# Add each calculated bounce value to the DataFrame 
        except: 
            print("BROKEN DATA:")
            print(row)
    data.to_csv("out.csv", index=False)
    print(data)
    plot_bounce_timeline(data) # Uncomment this to run Chases plotting code. TODO: Add some sort of flag system (e.g. "./run.bat --plot")

if __name__ == "__main__":
    main()

