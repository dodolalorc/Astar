from search import A_Star
from graph import AGraph
import random
from point import Point


WIDTH, HEIGHT = 1000, 800

ROWS, COLUMNS = 30, 30

CELL_PADDING = 6
CELL_SIZE = 20
CELL_DEFAULT = "#FFF"
CELL_NONE = "#000"
CELL_START = "#75F871"
CELL_END = "#EE8DB9"
CELL_PATH = "#C1F0FF"
CELL_EXPORLE = "#FFE8C1"

def init_gird() -> None:
    left, top = line_padding, col_padding
    right = left + COLUMNS * CELL_SIZE

    for i in range(ROWS * COLUMNS):
        c = random.random()
        p = Point(i, left, top)
        if c > 0.3:
            point_list.append(p)
        else:
            p.connected = False
            point_list.append(p)
        
        left += CELL_SIZE
        if left == right:
            left = line_padding
            top += CELL_SIZE

def setup():
    init_gird()


def draw() -> None:
    graph.build_graph(point_list, CELL_SIZE, (line_padding, col_padding, line_padding + COLUMNS * CELL_SIZE, col_padding + ROWS * CELL_SIZE))
    start()


def start() -> None:
    model = A_Star(start=point_list[start_index].vertex, end=point_list[end_index].vertex, graph=graph)
    model.search()
    

point_list = []

line_padding, col_padding = WIDTH / 2 - COLUMNS / 2 * CELL_SIZE, HEIGHT / 2 - ROWS / 2 * CELL_SIZE

start_index, end_index = random.randint(0, ROWS * COLUMNS), random.randint(0, ROWS * COLUMNS)

graph = AGraph()

setup()

draw()

