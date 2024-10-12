import pandas

def load_innings(path):
    data = pandas.read_csv(path)
    return data