<h1 align="center">Sudoku solver</h1>

<p align="center">
  <a href="#what-is-a-sudoku">What is a sudoku</a>     |
  <a href="#project-description">Project description</a>   |  
  <a href="#your-task">Your Task</a>   |  
  <a href="#requirements">Requirements</a>   |  
  <a href="#run-the-project">Run the project</a>     |
</p>

<br>

We all spent countless hours trying to solve a sudoku in our life, so to avoid this we created a sudoku solver that does it automatically.
What do you mean that's where the fun is? The real fun is to find a way to automate a game ;)

## What is a sudoku
For thoses how spent the last 20 years in a cave, a sudoku is a number-placement puzzle where the objective is to fill a 9×9 grid with digits so that each column, each row, and each of the nine 3×3 subgrids that compose the grid contain all of the digits from 1 to 9 [wikipedia article](https://en.wikipedia.org/wiki/Sudoku).

## Project description
This project implement the backtracking algorithm to solve a 9*9 sudoku, it also provide a basic template to add other methods to solve a sudoku.
Basically we choose one of the instances in `initial_instances.json` and solve it using the backtracking algorithm

## Your Task
You can improve the project in many ways

* Having a sudoku solver on console is nice, but a UI is better with these kind of games, so you can as a user interface with the library or technology you like.
* You can improve the `initial_instances.json` file by adding other starting sudoku configuration.
* You can do better by making an UI that unable a user to add a starting sudoku configuration.
* As we saw with this project we love automating stuffs so wouldn't it be better to write a sudoku generator, that generate starting sudoku configuration ?
* The backtracking Algorithm works just fine, but there are plenty of other methods to solve a sudoku, wh don't you try to write an alternate method ?

You can also make improvements that aren't listed here.

## Requirements
Python

## Run the project
To run the code you must execute `solver.py`
```
python3 solver.py
```

The initial sudoku instances are the json file `initial_instances.json`

* you can pass the one you want to solve as an argument with the arg `-b`.
For exemple to choose the second instance (the indexes start at 0).
```
python3 solver.py -b 1
```
you can achieve the same thing by modifying the `default_board` argument in `initial_instances.json`

* you can also choose an empty instance with the -empty argument
```
python3 solver.py -empty
```

* or a random one from the json file `initial_instances.json` with the -random argument
```
python3 solver.py -random
```
