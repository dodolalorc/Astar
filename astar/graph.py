from point import Point

class AGraph(object):

    def __init__(self) -> None:
        self.n = 0
        self.m = 0
        self.vertices = []
        self.neighbors = {}

    def build_graph(self, points: list[Point], cell_size: int, boundary: tuple[int, int, int, int]) -> None:
        vertex_set = {p.vertex : p for  p in points if p.connected }
        self.vertices = points
        self.n = len(vertex_set)
        for p in points:
            if not p.connected:
                continue
            nei = []
            possible_nei = [
                (p.x + cell_size, p.y),
                (p.x - cell_size, p.y),
                (p.x, p.y + cell_size),
                (p.x, p.y - cell_size),
            ]
            for x, y in possible_nei:
                if x < boundary[0] or x > boundary[2] or y < boundary[1] or y > boundary[3]:
                    continue
                nei_vertex = next((v for v, p in vertex_set.items() if p.x == x and p.y == y), None)
                if nei_vertex is not None:
                    nei.append(vertex_set[nei_vertex])
            for u in nei:
                self.neighbors.setdefault(p.vertex, []).append(u.vertex)
                self.neighbors.setdefault(u.vertex, []).append(p.vertex)
                self.m += 1
        for k, _ in self.neighbors.items():
            self.neighbors[k] = list(set(self.neighbors[k]))
        self.m /= 2
    
    def __str__(self) -> str:
        s = f"Graph : vertex num -> {self.n}, edge num -> {self.m}\n"
        for vertex, neighbors in self.neighbors.items():
            s += f"({vertex}, {neighbors})\n"
        return s


    def neighbor(self, vertex: int) -> list[int]:
        return self.neighbors.get(vertex, [])

