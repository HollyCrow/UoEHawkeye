from data_loading import load_innings
from bounce import calc_bounce

def main():
    # I have a vague recollection that windows requires \ rather than / for file paths?
    inning = load_innings("./data/data.csv")
    for index, row in inning.iterrows():
        # Whatever processing happens should be decided by Understanding the data 1&2.
        # This is a placeholder. Position should probably also be tracked. Later problem.
        bounce_value = calc_bounce(row)
        print(bounce_value)

if __name__ == "__main__":
    main()
