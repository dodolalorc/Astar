from proceso import Sketch
from search import A_Star
from graph import AGraph
import random
from point import Point


WIDTH, HEIGHT = 1500, 1000

ROWS, COLUMNS = 20, 20

CELL_PADDING = 6
CELL_SIZE = 40
CELL_DEFAULT = "#FFF"
CELL_NONE = "#000"
CELL_START = "#75F871"
CELL_END = "#EE8DB9"
CELL_PATH = "#C1F0FF"
CELL_EXPORLE = "#FFE8C1"

TEXT_COLOR = "#000"
TEXT_SIZE = 8

def init_gird() -> None:
    left, top = line_padding, col_padding
    right = left + COLUMNS * CELL_SIZE

    for i in range(ROWS * COLUMNS):
        c = random.random()
        p = Point(i, left, top)
        if c > 0.3:
            connect_set.append(i)
            point_list.append(p)
            p5.fill(CELL_DEFAULT)
            p5.rect(left, top, CELL_SIZE - 2, CELL_SIZE - 2)
        else:
            p.connected = False
            point_list.append(p)
            p5.fill(CELL_NONE)
            p5.rect(left, top, CELL_SIZE - 2, CELL_SIZE - 2)
        
        left += CELL_SIZE
        if left == right:
            left = line_padding
            top += CELL_SIZE

def setup():
    global solved, path, explore, graph, start_index, end_index
    p5.create_canvas(WIDTH, HEIGHT)
    p5.background("#C1BCBE")
    p5.no_stroke()
    p5.frame_rate(10)

    init_gird()

    start_index, end_index = random.choice(connect_set), random.choice(connect_set)

    
    p5.fill(CELL_START)
    start = point_list[start_index]
    left, top = start.x, start.y
    p5.rect(left, top, CELL_SIZE - 2, CELL_SIZE - 2)
    p5.fill(TEXT_COLOR)
    p5.text_align(p5.CENTER, p5.CENTER)
    p5.text_size(16)
    p5.text("Start", left + CELL_SIZE / 2, top + CELL_SIZE / 2)

    p5.fill(CELL_END)
    end = point_list[end_index]
    left, top = end.x, end.y
    p5.rect(left, top, CELL_SIZE - 2, CELL_SIZE - 2)
    p5.fill(TEXT_COLOR)
    p5.text_align(p5.CENTER, p5.CENTER)
    p5.text_size(16)
    p5.text("End", left + CELL_SIZE / 2, top + CELL_SIZE / 2)

    graph.build_graph(point_list, CELL_SIZE, (line_padding, col_padding, line_padding + COLUMNS * CELL_SIZE, col_padding + ROWS * CELL_SIZE))
    solved, p, explore = startSearch()
    path = set(p)


def draw() -> None:
    global path, count, solved, explore, play
    if p5.is_mouse_pressed:
        play = True
    if solved and play:
        if count >= len(explore):
            p5.no_loop()
            return
        
        start = point_list[start_index]
        end = point_list[end_index]

        for v_idx in explore[count]:
            if v_idx == start_index or v_idx == end_index:
                continue
            v = point_list[v_idx]
            left, top = v.x, v.y
            if v_idx in path:
                p5.fill(CELL_PATH)
                p5.rect(left, top, CELL_SIZE - 2, CELL_SIZE - 2)
                p5.fill(TEXT_COLOR)
                p5.text_align(p5.CENTER, p5.CENTER)
                p5.text_size(TEXT_SIZE)
                p5.text(f"h = {int(abs(v.x - end.x) / CELL_SIZE + abs(v.y - end.y) / CELL_SIZE)}\ng = {int(abs(v.x - start.x) / CELL_SIZE + abs(v.y - start.y) / CELL_SIZE)} \nh+g = {int(abs(v.x - end.x) / CELL_SIZE + abs(v.y - end.y) / CELL_SIZE + abs(v.x - start.x) / CELL_SIZE + abs(v.y - start.y) / CELL_SIZE)}", left + CELL_SIZE / 2, top + CELL_SIZE / 2)
            else:
                p5.fill(CELL_EXPORLE)
                p5.rect(left, top, CELL_SIZE - 2, CELL_SIZE - 2)
                p5.fill(TEXT_COLOR)
                p5.text_align(p5.CENTER, p5.CENTER)
                p5.text_size(TEXT_SIZE)
                p5.text(f"h = {int(abs(v.x - end.x) / CELL_SIZE + abs(v.y - end.y) / CELL_SIZE)}\ng = {int(abs(v.x - start.x) / CELL_SIZE + abs(v.y - start.y) / CELL_SIZE)} \nh+g = {int(abs(v.x - end.x) / CELL_SIZE + abs(v.y - end.y) / CELL_SIZE + abs(v.x - start.x) / CELL_SIZE + abs(v.y - start.y) / CELL_SIZE)}", left + CELL_SIZE / 2, top + CELL_SIZE / 2)
        count += 1
    elif not solved:
        p5.text_align(p5.CENTER, p5.CENTER)
        p5.text_size(32)
        p5.fill(TEXT_COLOR)
        p5.text("No solution", WIDTH / 2, 32)
        p5.no_loop()


def startSearch() -> tuple[bool, list[int], dict]:
    model = A_Star(start=point_list[start_index].vertex, end=point_list[end_index].vertex, graph=graph)
    model.search()
    if model.is_solved:
        return (True, model.path(), model._explore)
    else:
        return (False, None, None)

point_list = []

p5 = Sketch()
p5.describe("A* Algorithm")

line_padding, col_padding = WIDTH / 2 - COLUMNS / 2 * CELL_SIZE, HEIGHT / 2 - ROWS / 2 * CELL_SIZE

connect_set = []

start_index, end_index = None, None

graph = AGraph()

solved, path, explore, play = None, None, None, False
count = 0

p5.run_sketch(setup=setup, draw=draw)

