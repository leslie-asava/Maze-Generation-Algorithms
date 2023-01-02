import random

class Cell():
    def __init__(self):

        self.index = 0

        # Start with every wall existing
        self.top_wall = True
        self.bottom_wall = True
        self.left_wall = True
        self.right_wall = True

        self.top_neighbor = None
        self.bottom_neighbor = None
        self.left_neighbor = None
        self.right_neighbor = None

        self.neighbors = [self.top_neighbor, self.bottom_neighbor, self.left_neighbor, self.right_neighbor]

    def remove_wall(self, direction):
        if direction == "left":

            self.left_wall = False
            neighbor = self.left_neighbor

            if neighbor != None:
                neighbor.right_wall = False

        elif direction == "right":
            
            self.right_wall = False
            neighbor = self.right_neighbor

            if neighbor != None:
                neighbor.left_wall = False

        elif direction == "top":
            
            self.top_wall = False
            neighbor = self.top_neighbor

            if neighbor != None:
                neighbor.bottom_wall = False

        elif direction == "bottom":
            
            self.bottom_wall = False
            neighbor = self.bottom_neighbor

            if neighbor != None:
                neighbor.top_wall = False

    def __str__(self) -> str:
        try:
            top = self.top_neighbor.index
        except:
            top = None
        try:
            bottom = self.bottom_neighbor.index
        except:
            bottom = None
        try:
            left = self.left_neighbor.index
        except:
            left = None
        try:
            right = self.right_neighbor.index
        except:
            right = None
        output = "top:%s, bottom:%s, left:%s, right:%s"%(top, bottom, left, right)

        return output

cell_list = []

def generate_maze(WIDTH, HEIGHT):

    global cell_list
    cell_list = []

    previous_cell = None

    index = 0

    for row in range(HEIGHT):
        for column in range(WIDTH):
            current_cell = Cell()
            current_cell.index = index

            if column == 0:
                current_cell.left_neighbor = None
                previous_cell = current_cell

            else:
                current_cell.left_neighbor = previous_cell

            if column == WIDTH:
                current_cell.right_neighbor = None

            else:
                previous_cell.right_neighbor = current_cell

            
            index += 1

            cell_list.append(current_cell)
            previous_cell = current_cell

    index = 0

    for row in range(HEIGHT):
        for column in range(WIDTH):

            current_cell = cell_list[index]

            if row == 0:
                current_cell.top_neighbor = None

            else:
                current_cell.top_neighbor = cell_list[((row - 1) * WIDTH) + column]

            if row == HEIGHT- 1:
                current_cell.bottom_neighbor = None

            else:
                current_cell.bottom_neighbor = cell_list[((row + 1) * WIDTH) + column]

            index += 1

    visited = []
    stack = []

    initial_cell = cell_list[0]

    visited.append(initial_cell)
    stack.append(initial_cell)

    while len(stack):
        current_cell = stack.pop()

        print(current_cell)

        neighbors = [current_cell.top_neighbor, current_cell.bottom_neighbor, current_cell.left_neighbor, current_cell.right_neighbor]
        unvisited_neighbors = []
        
        for cell in neighbors:
            if cell not in visited and cell != None:

                unvisited_neighbors.append(cell)
                if current_cell not in stack and current_cell != None:
                    stack.append(current_cell)

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

                

    
    # Reshape array into m x n matrix
    row_list = []

    index = 0
    for i in range(HEIGHT):
        column_list = []
        for j in range(WIDTH):
            column_list.append(cell_list[index])

            index += 1

        row_list.append(column_list)

    return row_list
