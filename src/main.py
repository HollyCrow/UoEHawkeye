from data_loading import load_innings
from bounce import calc_bounce
from graph import plot
import pandas as pd

def main():
    data = { # Dataframe format for output.
        "BounceX": [],
        "BounceY": [],
        "BounceFloat": [],
            #"BounceDateTime": []
    }
    data = pd.DataFrame(data) # Convert "data" into a pandas DataFrame


    # I have a vague recollection that windows requires \ rather than / for file paths?
    inning = load_innings("./data/Coaching.csv")
    for index, row in inning.iterrows():
        # Whatever processing happens should be decided by Understanding the data 1&2.
        # This is a placeholder. Position should probably also be tracked. Later problem.
        try:
            bounce_value = calc_bounce(row)
            data.loc[len(data.index)] = [row["BounceX"], row["BounceY"], bounce_value]#, datetime.strptime(row["TrajectoryDate"]+""+row["TrajectoryTime"], "%Y/%m/%d %H:%M:%S")] # Add each calculated bounce value to the DataFrame
        except:
            print(row["TrajectoryDate"]+""+row["TrajectoryTime"])
            print("Broken data")
    data.to_csv("out.csv", index=False)
    print(data)
    plot(data) # Uncomment this to run Chases plotting code. TODO: Add some sort of flag system (e.g. "./run.bat --plot")

if __name__ == "__main__":
    main()

