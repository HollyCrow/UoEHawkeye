# For combining and refining that god-awful dataset
# Also I have done the "proper" and "maintainable" thing of not editing the original data-set in this program,
# which I would just like to clarify has made my life a living hell.

import os
import pandas as pd
import math

# Coloumn titles for Coaching and Trends csv files.
Coaching_columns = ["OverNumber", "BallNumber", "BowlerName", "BatsmanName", "BatsmansHand", "BowlerReleaseSpeed",
                    "BounceX", "BounceY", "StumpsY", "StumpsZ", "Swing", "Deviation", "RunsScored", "ShotLandingX",
                    "ShotLandingY", "TrajectoryTime", "TrajectoryDate", "BounceVelocity", "OutOfBounceAngle",
                    "DropAngle", "AngleLeavingBowlersHand", "ShotPlayed", "ShotType", "BowlerReleaseYposition",
                    "BowlerReleaseZposition", "AccelerationX", "AccelerationY", "AccelerationZ"]
# I am assuming that the last coloum should be accZ

Trends_columns = ["Innings", "Over", "Ball", "BounceX_trends", "BounceY_trends", "BounceTime", "AccX", "AccY", "AccZ",
                  "PreVelX", "PreVelY", "PreVelZ", "PostVelX", "PostVelY", "PostVelZ", "PostAccX", "PostAccY",
                  "PostAccZ", "lastUpdateTime", "KalmanFilterType", "Predicted", "Quality", "Warning", "NoSwing",
                  "xPositionAtBatsman", "BowlingEnd", "TRJname", "CoefficientOfRestitution", "COF",
                  "PaceBounceRatio", "SeamMovement"]

# Final order of coloumns (BEFORE ANY REMOVALS)
# This should be reordered as needed.
Combined_columns = [
    "ID",
"--- 1 ---",
    "BounceX", "BounceY", "BounceX_trends", "BounceY_trends", "BounceTime",
    "BowlerReleaseSpeed", "BowlerReleaseYposition", "BowlerReleaseZposition", "AngleLeavingBowlersHand",
    "StumpsY", "StumpsZ",
    "AccelerationX", "AccelerationY", "AccelerationZ", "AccX", "AccY", "AccZ",
    "PreVelX", "PreVelY", "PreVelZ",
    "PostVelX", "PostVelY", "PostVelZ",
    "PostAccX", "PostAccY", "PostAccZ",
    "Swing", "Deviation", "ShotLandingX", "ShotLandingY", "OutOfBounceAngle", "DropAngle",
"--- 2 ---",
    "CoefficientOfRestitution", "COF", "SeamMovement", "PaceBounceRatio",
"--- 3 ---",
    "BowlingEnd", "ShotPlayed", "ShotType", "BowlerName", "BatsmanName", "BatsmansHand",
    "RunsScored", "TrajectoryTime", "TrajectoryDate",
"--- 4 ---",
    "Innings", "OverNumber", "Over", "BallNumber", "Ball", "BounceVelocity",
    "lastUpdateTime", "KalmanFilterType", "Predicted", "Quality", "Warning", "NoSwing",
    "xPositionAtBatsman", "BowlingEnd", "TRJname"
]

# All columns that should be deleted in the distil_combined() function.
combined_coloumns_to_delete = []
trends_coloumns_to_delete = []  # these bottom two aren't implemented.
coaching_coloumns_to_delete = []


def get_game_id(root):  # Create a UID for games (To be added to each inning id to make it easily findable).
    # It really annoys me that the Lord's games have the ' in their directory. Makes tree look super ugly

    root = root.split("/")  # Get the two directories (This has a .replace("bad_data/", "") for the id0 system)
    # id0 = root[0][:9][-6:]
    # e.g. "UK_22_JUN". I am hoping this is specific enough for future data? I would like it not to be too lengthy.
    # This is just the subdirectory.

    # id1 = root[1].split("_1")[0]  # Get the game title, cutting off the ugly ID number used by hawkeye.

    return root[-1]  # In retrospect, I will just shove it all in one dir of games.


def combine_pair(coaching, trends):  # Combine Coaching_n.csv and Trends_n.csv
    # Add a primary key for combining:
    if (trends.columns.values.tolist()[0] != "Innings"):
        trends.columns = Trends_columns

    trends = trends.set_axis(Trends_columns, axis=1)
    ID = []
    for inning_index, row in coaching.iterrows():
        ID.append(str(row["BallNumber"]) + "_" + str(row["OverNumber"]))
    coaching["ID"] = ID
    ID = []
    for inning_index, row in trends.iterrows():
        ID.append(str(row["Ball"]) + "_" + str(row["Over"]))  # Yes: the Trends.csv is formated by somebody with
        # what is charitably described as a brain doused in petrol and scrubbed with a scrub-daddy. EVERY. FUCKING.
        # COLUMN. NAME.; begines with an extra fucking space. The amount of my fucking life (and, contrary to this
        # numb-nuts opinions; I only get one of those) that was wasted by this glue sniffers stupid fucking
        # formatting istfg. # Update: I have fixed their shite for them. Be happy.
    trends["ID"] = ID
    return pd.merge(coaching, trends, on="ID", how="inner")


def distil_combined(combined, game_id, day_number):  # Rearrange and remove columns where necessary. Also assign IDs
    ID = []
    for inning_index, row in combined.iterrows():
        ID.append(row["ID"] + "_" + str(day_number) + "_" + game_id)  # Make ID universal.
    combined["ID"] = ID
    # This leaves the final UID as follows:
    #   BallNumber_OverNumber_day_GameFile
    # This can be rearranged without much issue if need be.

    combined["--- 1 ---"] = "" # Create seperator columns
    combined["--- 2 ---"] = ""
    combined["--- 3 ---"] = ""
    combined["--- 4 ---"] = ""

    combined = combined[Combined_columns]
    combined = combined.drop(combined_coloumns_to_delete, axis=1)

    # print(game_id)
    # print(combined)
    # print("uwu")

    # combined['ID_reverse'] = combined['ID'].str[::-1]
    # combined = combined.sort_values(by='ID_reverse')
    # combined = combined.drop(["ID_reverse"], axis=1)


    return combined


def save_combined(combined, path):  # Save
    combined.to_csv(path, index=False)


os.system("rm -rf distilled_data; mkdir distilled_data")
games = {}  # Array of all game dataframes

for root, subdirs, files in os.walk("bad_data"):  # I would make "bad_data" name agnostic;
    # but let's be honest, nobody else is ever going to use this code.
    innings = {}  # Array of pandas DataFrames to contain combined Coaching and Trends, to be spat back out into the directory.
    game_id = get_game_id(root)  # Get ID of game.
    for file in files:
        if file.endswith(".csv") and ("Coaching" in file or "Trends" in file):
            # Find which # csv it is (These are unique per game)
            # (Basically just get the n in Coaching_n.csv or Trends_n.csv)
            index = (file.replace(".csv", "").replace("Coaching_", "").replace("Trends_", ""))

            try:  # Check if files are actually readable csv and skip if not.
                pd.read_csv(os.path.join(root, file))
            except:
                print("FAILED TO LOAD FILE AS CSV /\\: " + os.path.join(root, file))
                continue  # If reading the csv failed: skip this file. (This is mostly just for the empty files)

            if not index in innings:  # Check if the other file in the Coaching-Trends pair has already been read
                # If not: Create the pair in the innings array.
                innings[index] = {
                    "Coaching": pd.read_csv(os.path.join(root, file), names=Coaching_columns) if (
                            "Coaching" in file) else pd.DataFrame,
                    "Trends": pd.read_csv(os.path.join(root, file)) if ("Trends" in file) else pd.DataFrame,
                }
            else:  # If the inning pair does exist: Add to innings array and process combination.
                if "Coaching" in file:
                    # This whole thing could probably be reduced to one line.
                    innings[index]["Coaching"] = pd.read_csv(os.path.join(root, file), names=Coaching_columns)
                else:
                    innings[index]["Trends"] = pd.read_csv(os.path.join(root, file))

                combined = combine_pair(innings[index]["Coaching"], innings[index]["Trends"])
                # if combined.empty:
                #     continue
                combined = distil_combined(combined, game_id, index)
                innings[index] = combined

                # save_combined(combined, os.path.join( # Save to combined_n.csv (Reaplced with full game csv's from now on.
                #     root.replace("bad_data", "distilled_data"),
                #     file.replace("Coaching", "innings").replace("Trends", "innings")))

                for inning_index, row in combined.iterrows():
                    if round(math.isnan(row["BounceY"]) or math.isnan(row["BounceY_trends"]) or
                             row["BounceY"] * 100) != round(row["BounceY_trends"] * 100):
                        print(str(row["BounceY"]) + " - " + str(row["BounceY_trends"]))
                        print(os.path.join(root.replace("bad_data", "distilled_data"),
                                           file.replace("Coaching", "innings").replace("Trends", "innings")))
                        combined.drop([inning_index])
                        break

            # Get the absolute path of the current file
            file_path = os.path.join(root, file)

    if not innings == {}:  # If there was actually a game here.
        # print(root.replace("bad_data/", ""))
        # games[root.replace("bad_data/", "").split("/")[1]] = pd.concat(innings, ignore_index=True) # Kinda unnesesary.
        innings = dict(sorted(innings.items()))
        pd.concat(innings, ignore_index=True).to_csv(os.path.join("distilled_data", game_id + ".csv"),
                                                     index=False)  # Save.
