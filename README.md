# UoEHawkeye
**Project for processing innings data for cricket matches, with the goal of mapping the bounciness of the pitch.**

Currently the data loading is split into multiple projects, as listed below:

## Holly (Pandas version):
```
UoEHawkeye/
└── holly/
    ├── main.py
    ├── data_loading.py
    ├── bounce.py
    └── data.csv
```
*main.py* - Header file.\
*data_loader.py* - csv loader with pandas\
*bounce.py* - main file for actual calculations\
*data.csv* - sample dataset for games

**Pandas data structure:**\
load_innings() returns a pandas **DataFrame**.\
Rows are iterated through in main(), and handed off to calc_bounce() in *bounce.py*.\
The values (as specified in "File Format Explanation.pdf") can be accessed by `inning["VALUE NAME"]`

**Data loading:**\
*data.csv* is modified from "Analysis_sample_fixed.csv" to add the column titles.\
There is an extra column which I have titled "no_idea", as I haven't the faintest idea what it is.

