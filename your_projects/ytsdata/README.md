# YTS Data

## Description:
Using [the YTS API](https://yts.mx/api) to browse, search and download movies from the Command Line.


## Dependencies:

- Python
    - 'requests' module
    - 'PyInquirer' module: `pip install PyInquirer`

## How to run the project
If you are in the root folder (same as Readme.md):  
`python ytsdata`

## The progress of the project
The project is in development, right now the principal API calls are defined in `ytsdata/yts_api.py` the next step is extending the CLI by giving the user the possibility to do more things (check ratings, get more details about a movie...etc) 