<h1 align="center">Save The Princess Bot</h1>

<p align="center">
  <a href="#project-description">Project description</a>   |   
  <a href="#your-task">Your Task</a>   |  
  <a href="#requirements">Requirements</a>   |  
  <a href="#checkered_flag-starting">Starting</a> 
</p>

<br>

## Project description

A Princess is trapped in one of the four corners of a square grid. You are located in the center of this grid and you can only make one move at a time in one of the four directions of your choice. Can you save the Princess using the shortest past possible ?

## Your Task

In this project, we already created a simple path finding method using euclidian distance. Your goal is to create a more optimal function with a better complexity. the grid is 5x5 length, the position of the princess is in the Princess variable and the knight position is the Knight variable. Your function has to return a list of the x and y indexes of the cases of the grid of the grid that the knight passed throught to save the princess.  

## Requirements

Before starting 🏁, you need to have [Git](https://git-scm.com) and [Python](https://www.python.org/downloads/) installed.

## Starting

```bash
# Create a directory, so Git doesn't get messy, and enter it
mkdir my-dir && cd my-dir

# Start a Git repository
git init

# Track repository, do not enter subdirectory
git remote add -f origin https://github.com/openmindsclub/H4ckT0b3rF3st-2k21/

# Enable the tree check feature
git config core.sparseCheckout true

# Create a file in the path: .git/info/sparse-checkout
# That is inside the hidden .git directory that was created
# by running the command: git init
# And inside it enter the name of the sub directory you only want to clone
echo 'projects/Save_The_Princess_Bot' >> .git/info/sparse-checkout

## Download with pull, not clone
git pull origin master

#go to the SaveThePrincess.py file and copy past the YourFunction() function change it's name and start creating your funcion.

```

```Python
#After finishing your function replace FindThePath by the name of your Function

start(i,FindThePath()) ===> start(i,YourFunction())

#Compile and see the result

```

<p align="center">
<a href="#top">Back to top</a>
</p>
