from math import floor
import sys
import pygame 

# 1 is wall and 2 is start and end 
#           ID = x
# IDX = y

class Node:
    def __init__(self, manhattan = 0, travelled = 0, left = None, right = None, up = None, down = None, wall = False):
        self.manhattan = manhattan
        self.travelled = travelled
        self.val = self.manhattan + self.travelled
        self.left = left
        self.right = right
        self.up = up
        self.down = down
        self.wall = wall
    def set_left(self, left):
        self.left = left
    def get_left(self):
        return self.left
    def set_right(self, right):
        self.right = right
    def get_right(self):
        return self.right
    def set_up(self, up):
        self.up = up
    def get_up(self):
        return self.up
    def set_down(self, down):
        self.down = down
    def get_down(self):
        return self.down
    def get_val(self):
        return self.val
    def set_manhattan(self, manhattan_value):
        self.manhattan = manhattan_value
    def get_manhattan(self):
        return self.manhattan
    def set_travelled(self, distance):
        self.travelled = distance
    def get_travelled(self):
        return self.travelled
    def update_val(self):
        self.val = self.manhattan + self.travelled
    def is_wall(self):
        if self.wall == True:
            return True
        else:
            return False
    def set_wall(self, wall_status):
        self.wall = wall_status
    
def link_graph(graph):
    
    xlen = len(graph[0])
    ylen = len(graph)
    
    for i in range(0, ylen):
        for j in range(0, xlen):
            if j == 0 and i == 0 and xlen > 2 and ylen > 2:
                graph[i][j].set_right(graph[i][j + 1])
                graph[i][j].set_down(graph[i + 1][j])
            elif j == xlen - 1 and i == ylen - 1 and xlen > 2 and ylen > 2:
                graph[i][j].set_up(graph[i - 1][j])
                graph[i][j].set_left(graph[i][j - 1])
            elif j == 0 and i == ylen - 1 and xlen > 2 and ylen > 2:
                graph[i][j].set_right(graph[i][j + 1])
                graph[i][j].set_up(graph[i - 1][j])
            elif j == xlen - 1 and i == 0 and xlen > 2 and ylen > 2:
                graph[i][j].set_left(graph[i][j - 1])
                graph[i][j].set_down(graph[i + 1][j])
            elif j != 0 and j != xlen - 1 and i == 0 and xlen > 2 and ylen > 2:
                graph[i][j].set_left(graph[i][j - 1])
                graph[i][j].set_right(graph[i][j + 1])
                graph[i][j].set_down(graph[i + 1][j])
            elif j != 0 and j != xlen - 1 and i == ylen - 1 and xlen > 2 and ylen > 2:
                graph[i][j].set_left(graph[i][j - 1])
                graph[i][j].set_right(graph[i][j + 1])
                graph[i][j].set_up(graph[i - 1][j])
            elif j == 0 and i != 0 and i != ylen - 1 and xlen > 2 and ylen > 2:
                graph[i][j].set_up(graph[i - 1][j])
                graph[i][j].set_right(graph[i][j + 1])
                graph[i][j].set_down(graph[i + 1][j])
            elif j == xlen - 1 and i != 0 and i != ylen - 1 and xlen > 2 and ylen > 2:
                graph[i][j].set_up(graph[i - 1][j])
                graph[i][j].set_left(graph[i][j - 1])
                graph[i][j].set_down(graph[i + 1][j])
            else:
                if xlen > 2 and ylen > 2:
                    graph[i][j].set_up(graph[i - 1][j])
                    graph[i][j].set_left(graph[i][j - 1])
                    graph[i][j].set_down(graph[i + 1][j])
                    graph[i][j].set_right(graph[i][j + 1])
    return graph

def print_nodes(graph):
    
    ylen = len(graph)
    xlen = len(graph[0])
    
    for i in range(0, ylen):
        for j in range(0, xlen):
            print(graph[i][j].get_val(), end = ' ')
        print('\n')

def manhattan(currx, curry, nx, ny):
    distance = abs(currx - nx) + abs(curry - ny)
    return distance

def play(grid, coords):
    starting = coords[0]
    ending = coords[1]
    starty = starting[0]
    startx = starting[1]
    endy = ending[0]
    endx = ending[1]
    currx = 0
    curry = 0
    prev = []
    first_run = True
    while True:
        options = []
        if first_run == True:
            currx = startx
            curry = starty
        if curry == endy and currx == endx:
            return prev
        temp = grid[curry][currx]
        temp_distance = temp.get_travelled() + 1
        if temp.get_up() != None:
            if temp.get_up().is_wall() == False:
                up_temp = temp.get_up()
                up_temp.set_manhattan(manhattan(currx = currx, curry = curry - 1, nx = endx, ny = endy))
                up_temp.set_travelled(temp_distance)
                up_temp.update_val()
                options.append(up_temp.get_val())
            else:
                options.append(999)
        else:
            options.append(999)
        if temp.get_down() != None:
            if temp.get_down().is_wall() == False:
                down_temp = temp.get_down()
                down_temp.set_manhattan(manhattan(currx = currx, curry = curry + 1, nx = endx, ny = endy))
                down_temp.set_travelled(temp_distance)
                down_temp.update_val()
                options.append(down_temp.get_val())
            else:
                options.append(999)
        else:
            options.append(999)
        if temp.get_left() != None:
            if temp.get_left().is_wall() == False:
                left_temp = temp.get_left()
                left_temp.set_manhattan(manhattan(currx = currx - 1, curry = curry, nx = endx, ny = endy))
                left_temp.set_travelled(temp_distance)
                left_temp.update_val()
                options.append(left_temp.get_val())
            else:
                options.append(999)
        else:
            options.append(999)
        if temp.get_right() != None:
            if temp.get_right().is_wall() == False:
                right_temp = temp.get_right()
                right_temp.set_manhattan(manhattan(currx = currx + 1, curry = curry, nx = endx, ny = endy))
                right_temp.set_travelled(temp_distance)
                right_temp.update_val()
                options.append(right_temp.get_val())
            else:
                options.append(999)
        else:
            options.append(999)
        min_idx = options.index(min(options))
        if min_idx == 0:
            prev.append([curry, currx])
            curry = curry - 1
            #best node is up
        elif min_idx == 1:
            prev.append([curry, currx])
            curry = curry + 1
            #best node is down
        elif min_idx == 2:
            prev.append([curry, currx])
            currx = currx - 1
            #best node is left
        elif min_idx -- 3:
            prev.append([curry, currx])
            currx = currx + 1
            #best node is right
        else:
            print('Big Error')
        first_run = False
            
                
if __name__ == "__main__":
    width = 900
    height = 900
    clicks = 0
    icon = pygame.image.load('greed.jpeg')
    size = (width, height)
    num_squares = sys.argv[1]
    bsize = int(width) / int(num_squares)
    all_boxes = []
    grid_map = []
    start_end = []
    start = []
    end = []
    prev = []
    pygame.init()
    
    print(f'The bsize is : {bsize}')
    
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Greedy Pathfinding')
    pygame.display.set_icon(icon)
    screen.fill((255,255,255))
    for y in range(0, height, int(bsize)):
        row = []
        grid_row = []
        for x in range(0, width, int(bsize)):
            temp = Node()
            rect = pygame.Rect(x, y, bsize - 1, bsize - 1)
            row.append([rect, (0, 0, 0)])
            grid_row.append(temp)
        all_boxes.append(row)
        grid_map.append(grid_row)
    graph_linked = link_graph(grid_map)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for idx, j in enumerate(all_boxes):
                    for id, unit in enumerate(j):
                        rect, color = unit
                        if rect.collidepoint(event.pos):
                            if color == (0, 0, 0) and clicks < 2:
                                unit[1] = (0, 255, 0)
                                start_end.append([idx, id])
                                clicks += 1
                            elif color == (0, 255, 0):
                                unit[1] = (0, 0, 0)
                                start_end.pop(-1)
                                clicks -= 1
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                for idx, j in enumerate(all_boxes):
                    for id, unit in enumerate(j):
                        rect, color = unit
                        if rect.collidepoint(event.pos):
                            if color == (0, 0, 0):
                                graph_linked[idx][id].set_wall(True)
                                unit[1] = (255, 0, 0)
                            elif color == (255, 0, 0):
                                graph_linked[idx][id].set_wall(False)
                                unit[1] = (0, 0, 0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                sol = []
                sol = play(grid = graph_linked, coords = start_end)
                for i in range(1, len(sol)):
                    temp = sol[i]
                    yv = temp[0]
                    xv = temp[1]
                    square = all_boxes[yv][xv]
                    square[1] = (255, 165, 0)
                
        for r in all_boxes:
            for item in r:
                rec, color = item
                pygame.draw.rect(screen, color, rec)
        pygame.display.update()

