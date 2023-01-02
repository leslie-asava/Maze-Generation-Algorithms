import pygame 
from generator import generate_maze

pygame.init()

CELL_BORDER = (255,255,255)
CELL_LINE_WIDTH = 2

screen = pygame.display.set_mode((640,640))

maze = generate_maze(20,20)

def visualize_maze(maze):
    start_y = 20
    side_x = 30
    side_y = 30

    line_width = 2

    for row in maze:
        start_x = 20
        for cell in row:
            # Left border
            if cell.left_wall:
                pygame.draw.line(screen, CELL_BORDER, (start_x, start_y), (start_x, start_y + side_y), CELL_LINE_WIDTH)

            # Right border
            if cell.right_wall:
                pygame.draw.line(screen, CELL_BORDER, (start_x + side_x, start_y), (start_x + side_x, start_y + side_y), CELL_LINE_WIDTH)

            # Top border
            if cell.top_wall:
                pygame.draw.line(screen, CELL_BORDER, (start_x, start_y), (start_x + side_x, start_y), CELL_LINE_WIDTH)

            # Bottom border
            if cell.bottom_wall:
                pygame.draw.line(screen, CELL_BORDER, (start_x, start_y + side_y), (start_x + side_x, start_y + side_y), CELL_LINE_WIDTH)

            start_x += side_x

        start_y += side_y
        pygame.display.update()

visualize_maze(maze)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    

    pygame.display.flip()

pygame.quit()

