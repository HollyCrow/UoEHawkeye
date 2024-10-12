from data_loading import load_innings

def main():
    print("Hello, World!")
    # I have a vague recollection that windows requires \ rather than / for file paths?
    inning = load_innings("./holly/data.csv")
    print(inning[0])


if __name__ == "__main__":
    main()