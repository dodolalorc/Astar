class Point(object):

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y
    
    def h(self, end: int) -> int:
        return abs(self._x - self._graph.vertices[end].x) + abs(self._y - self._graph.vertices[end].y)
    
    def g(self, start: int) -> int:
        return abs(self._x - self._graph.vertices[start].x) + abs(self._y - self._graph.vertices[start].y)

    @property
    def vertex(self) -> int:
        return self._vertex_id

    def __init__(self, vertex, x, y, score=0) -> None:
        self._vertex_id = vertex
        self._x = x
        self._y = y
        self._score = score
        self.connected = True

    def __hash__(self) -> int:
        return hash(self._vertex_id)

