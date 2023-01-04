# Maze-Generation-Algorithms
My implementation of maze generation using various algorithms with the Python Programming Language.

# Randomized depth-first search
This algorithm, also known as the "recursive backtracker" algorithm, is a randomized version of the depth-first search algorithm.

Frequently implemented with a stack, this approach is one of the simplest ways to generate a maze using a computer. Consider the space for a maze being a large grid of cells (like a large chess board), each cell starting with four walls. Starting from a random cell, the computer then selects a random neighbouring cell that has not yet been visited. The computer removes the wall between the two cells and marks the new cell as visited, and adds it to the stack to facilitate backtracking. The computer continues this process, with a cell that has no unvisited neighbours being considered a dead-end. When at a dead-end it backtracks through the path until it reaches a cell with an unvisited neighbour, continuing the path generation by visiting this new, unvisited cell (creating a new junction). This process continues until every cell has been visited, causing the computer to backtrack all the way back to the beginning cell. We can be sure every cell is visited.

As given above this algorithm involves deep recursion which may cause stack overflow issues on some computer architectures. The algorithm can be rearranged into a loop by storing backtracking information in the maze itself. This also provides a quick way to display a solution, by starting at any given point and backtracking to the beginning.

Mazes generated with a depth-first search have a low branching factor and contain many long corridors, because the algorithm explores as far as possible along each branch before backtracking.

![image](https://user-images.githubusercontent.com/51715921/210546535-6cc0e2c1-8893-45f7-b0eb-3b4c713b36d1.png)

# Aldous-Broder algorithm
The Aldous-Broder algorithm is one of the simplest imaginable. It’s also one of the least efficient. The algorithm  works by producing uniform spanning trees. A spanning tree, is any tree that connects all the vertexes in a graph. A uniform spanning tree is one chosen randomly (and with equal probability) among all the possible spanning trees of a given graph. This algorithm is notable in that it selects from all possible spanning trees (i.e. mazes) of a given graph (i.e. field) with equal probability. Most other algorithms don't have this property.

![image](https://user-images.githubusercontent.com/51715921/210546055-292bacff-70dc-4da2-9e0b-f321195fa7bd.png)




