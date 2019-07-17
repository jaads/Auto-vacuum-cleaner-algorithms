# Searching for dirt
This project is about an abstraction of a robotic vacuum cleaner, which cleans multiple rooms using different search algorithms. 

The rooms are illustrated within a `.txt` file which can be found in the `maps` folder. A `numpy` matrix had been used to navigate the cleaner through the room. 

The algorithms in use are _uninformed search algorithms_, in fact
* Breadth First Search
* Depth First Search and

## Measuring problem-solving performance
Let $b$ be the branching factor and $d$ the depth and $m$ max. depth.

|Algorithmus|Complete|Optimal|Space complexity|Time complexity
|---|---|---|---|---|
|Breadth First Search|Yes|Yes|$O(b^d)$|$O(b^d)$|
|Depth First Search|Yes|No|$O(bm)$|$O(b^m)$|


## How to use
1. Install required packages using `pip install -r requirements.txt` (e.g. in a `venv`).
2. Change into `src` directory and run the desired algorithms, e.g. `python depth_first_search.py`.
During search, each and every step is printed to the console. The responsible function in the helper file needs to be adopted on a Windows based computer.

This project was created as part of a assignment during the course _Artificial Intelligence_ in the University of Applied Science Bonn-Rhein-Sieg.
