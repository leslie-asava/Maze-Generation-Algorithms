"""
----------------------------------------------------------------------
ALGORITHM
----------------------------------------------------------------------

- Choose the initial cell, mark it as visited and push it to the stack
- While the stack is not empty
    - Pop a cell from the stack and make it a current cell
    - If the current cell has any neighbours which have not been visited
        - Push the current cell to the stack
        - Choose one of the unvisited neighbours
        - Remove the wall between the current cell and the chosen cell
        - Mark the chosen cell as visited and push it to the stack

----------------------------------------------------------------------

"""
import random

def generate(cell_list):
    visited = []
    stack = []

    initial_cell = cell_list[0]

    visited.append(initial_cell)
    stack.append(initial_cell)

    # Iterate while stack is not empty
    while len(stack):
        # Pop cell at the top of the stack
        current_cell = stack.pop()

        neighbors = [current_cell.top_neighbor, current_cell.bottom_neighbor, current_cell.left_neighbor, current_cell.right_neighbor]
        unvisited_neighbors = []
        
        # Look up unvisited neighbors
        for cell in neighbors:
            if cell not in visited and cell != None:

                unvisited_neighbors.append(cell)
                if current_cell not in stack and current_cell != None:
                    stack.append(current_cell)

        # If there exists an unvisited neighbor
        if len(unvisited_neighbors):
            chosen_cell = random.choice(unvisited_neighbors)

            if current_cell.top_neighbor == chosen_cell:
                current_cell.remove_wall("top")

            elif current_cell.bottom_neighbor == chosen_cell:
                current_cell.remove_wall("bottom")

            elif current_cell.left_neighbor == chosen_cell:
                current_cell.remove_wall("left")

            elif current_cell.right_neighbor == chosen_cell:
                current_cell.remove_wall("right")

            visited.append(chosen_cell)
            stack.append(chosen_cell)

    return cell_list, "Randomized Iterative DFS Algorithm"