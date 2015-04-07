Python Birds
===========

Educational project to teach basic Object Orientation in Python Language.

Python version used: 3.4

Take a look at videos. Even in portuguese, is possible to see the graphics ;): [Python Birds](https://www.youtube.com/watch?v=b899h0lNd7U&list=PLA05yVJtRWYTm0sIa6n56UpCjCsR5ekla)

# Installing

Install [Python 3](https://www.python.org/download/).

Download the version containing only the [project structure](https://github.com/pythonprobr/pythonbirds/archive/training.zip)

Tests are under "testes" package and define the classes behavior.
Run all tests by executing:

    python testloader.py
    
Detailed explanation about classes and methods are found on [Simplified Game](#simplified-game)

## Development sequence

Start development with actors.py, following respective tests under actor_tests.py.
Next go to phase.py with its respective tests fase_teste.py.

You can run the game any time by executing:

    python graphics_tk.py

## How to play

Use "arrow down" or up to move the angle arrow. Use "space" or "enter" to launch a bird.
 
[Python Birds](https://www.youtube.com/watch?v=b899h0lNd7U&list=PLA05yVJtRWYTm0sIa6n56UpCjCsR5ekla)

## script actors.py

The module containing all project's actors.

## script phase.py

Module containing the class representing a Phase. Also contains the class Point to represent a Cartesian Point (x, y) plus a character representing the image to be shown.

## script graphics_tk.py

Logic to play the game with graphics on TKInter.


# Simplified Game

1. Actors are points on Cartesian Plan. 
2. Bird's speed is slow, so at each step the point move to a neighbor point.
3. Actors collision occurs considering the point as a center of a square with side equals to 2 times on "interval".

The detailed specification of game can be found next.

## Classe Actor

Base class for all game's actors.

### calculate_position method

Receives game's time (float) as a parameter and  returns a tuple with 2 elements: horizontal position(x) as the first element and
 vertical position (y) as second.


### status attribute

An actors has its status Active or Destroyed.
 
### clash method

Executes clash logic between two actors. It must occur only with both actor active if they are neighbors. Each actor
must keep clash time to calculate it's position accordingly.
Interval is a parameters to indicate a square with side 2 times "interval" that represents each point.
Its default value is 1.

## character method

It must return 'A' when actor is active and '+' otherwise. The return value depend on game's time.

## Class Obstacle

Class representing a obstacle which can be destroyed by birds. Inherits from Actor. its representing character when active is 
"O".


## Class Pig

Class representing pigs. Inherits from  Actor. Its character is "@" when Active and " " (empty string) other else.

## Bird

Base class for all birds. Each concrete type has a specific launch velocity (v). The player choose the birds launch angle (teta) in grads. 
The launch follow kinematic equation given gravity (G) of 10 m/s^2.

### launch method

Receives the launch angle and time. These values must be stored to further kinematic calculations.
Remember that time for equation is delta_t = T_end - T_start


### ground_clash method

Every bird clashing with ground (y<=0) must be destroyed.

### launched method

Must return True bird was already launched and False other else.

### Launching

Either if bird is not yet launched or if game's time is less the launch time, it must hold on initial position.
  
If it was launched and has active status, its position must be calculated based on kinematic equation.
delta_t is going to be game's time minus launch's time.
  
Other else it must return the clash position.

#### _calculate_horizontal_position method

Formula X=X0+v*cos(teta)*delta_t.

#### _calculate_vertical_position method

Fórmula Y=Y0+v*sen(teta)delta_t-(G*delta_t^2)/2.
    

## Class RedBirds

Bird class representing red birds. Its velocity is 20 m/s. Its active character is "R". Its destroyed character is "r"

## Class YellowBirds

Bird class representing yellow birds. Its velocity is 30 m/s. Its active character is "Y". Its destroyed character is "y"

## Class Phase

Responsible to hold actors and transform them into cartesian points on screen.

### add_obstacles method

Adds obstacles to phase.

### add_pigs  method

Adds pigs to phase.

### add_birds

Adds birds to phase.

### status method

Returns game's status. There are 3 possible values:

1. VICTORY indicating player's victory. It happens when all pigs are dead.
2. ON_GOING indication the game's is still running.
3. DEFEAT indicating player's lose. It happens when there is one pig active at least but there is no active bird.


### launch method

Receive launch angle and time as parameters. Must delegate launch to the first bird not launched on list.

### calculate_point method:

Execute game's logic on each step. Returns the points to be show at screen. 
It must:

1. Calculate each bird position;
2. Verify if bird clashed against an obstacle, pig or ground;
2. Transforms each actor in a point using _to_point method.

### Have Fun!!!!

Powered by [Python Pro](http://adm.python.pro.br)