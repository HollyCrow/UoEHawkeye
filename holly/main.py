from data_loading import load_innings

def main():
    # I have a vague recollection that windows requires \ rather than / for file paths?
    inning = load_innings("./holly/data.csv")
    print(inning)


if __name__ == "__main__":
    main()