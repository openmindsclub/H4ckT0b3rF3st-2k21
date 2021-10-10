<h1 align="center">Game of Life</h1>

<p align="center">
  <a href="#project-description">Project description</a>   |  
  <a href="#your-task">Your Task</a>   |  
  <a href="#requirements">Requirements</a>   |  
  <a href="#run-the-project">Run the project</a>     |
  <a href="#configuration">Configuration</a>     |
</p>

<br>



## Project description
this is an implementation of conway's Game of life, with python and pygame.
The Game is a 0 player game (it's a simulation) when each cell is represented by a square, it can be alive or dead. and for each generation it's evolve following the rules bellow
* if a dead cell is surrounded by exactly 3 alive cells then she will be alive in the next generation as if by reproduction.
* if an alive cell is surrounded by 2 or 3 alive cells it will survive on the next generation.
* if an alive cell is surrounded by less than 2 (or more than 3) alive cells, it will die as if by underpopulation (resp by overpopulation).
[for more information about the game check this wikipedia page](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)


## Tasks

* Add more configurations in the initial config file.
* Add the option to make the initial configuration random, and interesting.
* Make the screen resizable and add the zoom and unzoom functionality.

You can also make improvements that aren't listed here.

## Requirements
* python3
* pygame

## Run the project
1. Create a virtual environment
```bash
python3 -m venv env
```
2. activate virtual environment
```bash
source env/bin/activate
```
3. Install requirments
```bash
pip install requirements.txt
```

>if it doesn't work try
>```bash
>pip install pygame
>```

4. run
```bash
python game_of_life.py
```

## Configuration
there are some configurations you can do to the JSON file *config.json*

you can
1. adjust the the size of the window by modifying these parameters
```JSON
"screen_size_width":1200,
"screen_size_height":800,
```
2. modify the background color (color of the dead cells), and the cell color.
```JSON
"background_color":"darkslategray",
"cell_color":"tomato",
```
3. or the size of a cell wich will impact the number of cells in the board (smaller size imply more cells).
```JSON
"cell_size_width":12,
"cell_size_height":12,
```
The last paramater is the initial configuration and it represent the coordinate of cells alive at the begining of the simulation

## How to play it
you can add a living cell by taping the left click with the mousse, and delete a living cell with the right click.

you can use the spacebar to pause/unpause the simulation

you can use the backspace to reset the simulation (you'll kill all the cells)
