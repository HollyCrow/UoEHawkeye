from data_loading import load_innings
from bounce import calc_bounce
from graph import plot
import pandas as pd

def main():
    data = { # Dataframe format for output.
        "BounceX": [],
        "BounceY": [],
        "BounceFloat": []
    }
    data = pd.DataFrame(data) # Convert "data" into a pandas DataFrame


    # I have a vague recollection that windows requires \ rather than / for file paths?
    inning = load_innings("./data/data.csv")
    for index, row in inning.iterrows():
        # Whatever processing happens should be decided by Understanding the data 1&2.
        # This is a placeholder. Position should probably also be tracked. Later problem.
        bounce_value = calc_bounce(row)
        data.loc[len(data.index)] = [row["BounceX"], row["BounceY"], bounce_value] # Add each calculated bounce value to the DataFrame
    data.to_csv("out.csv", index=False)
    print(data)
    #plot(inning) # Uncomment this to run Chases plotting code. TODO: Add some sort of flag system (e.g. "./run.bat --plot")

if __name__ == "__main__":
    main()

