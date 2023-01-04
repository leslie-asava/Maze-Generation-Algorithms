"""
----------------------------------------------------------------------
ALGORITHM
----------------------------------------------------------------------

- Pick a random cell as the current cell and mark it as visited.
- While there are unvisited cells:
    - Pick a random neighbour.
    - If the chosen neighbour has not been visited:
        - Remove the wall between the current cell and the chosen neighbour.
        - Mark the chosen neighbour as visited.
    - Make the chosen neighbour the current cell.

----------------------------------------------------------------------

"""
import random
def generate(cell_list):
    visited = []

    current_cell = cell_list[0]

    visited.append(current_cell)

    while True:
        # While there are still unvisited cells
        exhausted = True
        for cell in cell_list:
            if cell not in visited:
                exhausted = False
                break

        # Quite loop if all have been visited
        if exhausted:
            break
        
        neighbors = [current_cell.top_neighbor, current_cell.bottom_neighbor, current_cell.left_neighbor, current_cell.right_neighbor]
        valid_neighbors = []
        
        # Remove None values
        for cell in neighbors:
            if cell != None:

                valid_neighbors.append(cell)

        if len(valid_neighbors):
            chosen_cell = random.choice(valid_neighbors)

            if chosen_cell not in visited:

                if current_cell.top_neighbor == chosen_cell:
                    current_cell.remove_wall("top")

                elif current_cell.bottom_neighbor == chosen_cell:
                    current_cell.remove_wall("bottom")

                elif current_cell.left_neighbor == chosen_cell:
                    current_cell.remove_wall("left")

                elif current_cell.right_neighbor == chosen_cell:
                    current_cell.remove_wall("right")

                visited.append(chosen_cell)

        current_cell = chosen_cell
            
    return cell_list