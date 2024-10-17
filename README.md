# UoEHawkeye
**Project for processing innings data for cricket matches, with the goal of mapping the bounciness of the pitch.**

Structure of project:

```
UoEHawkeye/
├── src
|   ├── main.py 	- Header file
|   ├── bounce.py 	- main file for actual calculations
|   └── data_loading.py	- CSV loader with pandas
├── data
|   └── data.csv	- Sample dataset
├── README.md
└── run.bat		- File to run project (works on both linux and windows)
```

**Pandas data structure:**\
load_innings() returns a pandas **DataFrame**.\
Rows are iterated through in main(), and handed off to calc_bounce() in *bounce.py*.\
The values (as specified in "File Format Explanation.pdf") can be accessed by `inning["VALUE NAME"]`

**Data loading:**\
*data.csv* is modified from "Analysis_sample_fixed.csv" to add the column titles.\
There is an extra column which I have titled "no_idea", as I haven't the faintest idea what it is.

