from enum import Enum
from typing import Any, Callable, Optional, Dict, List
from Kolejka import Queue
import graphviz


class EdgeType(Enum):
    directed = 1
    undirected = 2


class Vertex:
    data: Any
    index: int

    def __init__(self, data: Any, index: int) -> None:
        self.data = data
        self.index = index

    def __str__(self) -> str:
        return f"{self.data}"


class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]

    def __init__(self, source: Vertex, destination: Vertex, weight: Optional[float]) -> None:
        self.source = source
        self.destination = destination
        self.weight = weight

    def __str__(self) -> str:
        return f"{self.source.data} - {self.destination.data}"


class Graph:
    adjacencies: Dict[Vertex, List[Edge]]

    def __init__(self) -> None:
        self.adjacencies = {}

    def create_vertex(self, data: Any) -> Vertex:
        x: Vertex = Vertex(data, len(self.adjacencies))
        self.adjacencies[x] = []
        return x

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        self.adjacencies[source].append(Edge(source, destination, weight))

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        self.add_directed_edge(source, destination, weight)
        self.add_directed_edge(destination, source, weight)

    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        if edge.value == 1:
            self.add_directed_edge(source, destination, weight)
        else:
            self.add_undirected_edge(source, destination, weight)

    def traverse_breadth_first(self, visit: Callable[[Any], None]) -> None:
        v1: Vertex = list(self.adjacencies.keys())[0]
        o: List[Vertex] = []
        fifo: Queue = Queue()
        fifo.enqueue(v1)
        while len(fifo) != 0:
            v: Vertex = fifo.peek()
            visit(v)
            o.append(v)
            for x in self.adjacencies[v]:
                if x.destination not in o:
                    fifo.enqueue(x.destination)
                    o.append(x.destination)
            fifo.dequeue()

    def traverse_depth_first(self, visit: Callable[[Any], None]) -> None:
        v1: Vertex = list(self.adjacencies.keys())[0]
        o: List[Vertex] = []

        def dfs(v: Vertex, visited: List[Vertex], visit: Callable[[Any], None]) -> None:
            visit(v)
            visited.append(v)
            for x in self.adjacencies[v]:
                if x.destination not in visited:
                    dfs(x.destination, visited, visit)

        dfs(v1, o, visit)

    def __str__(self) -> str:
        w: str = ""
        for x in list(self.adjacencies.keys()):
            w += f" - {x.index}; {x.data} ----> ["
            for y in self.adjacencies[x]:
                w += f"{y.destination.index}: {y.destination.data}, "
            if len(self.adjacencies[x]) > 0:
                w = w[0:-2]+"]"
            else:
                w += "]"
        return w

    def show(self) -> None:
        drzewo = graphviz.Digraph()
        for x in list(self.adjacencies.keys()):
            drzewo.node(f"{x.data}")
        for x in list(self.adjacencies.keys()):
            for y in self.adjacencies[x]:
                if y.weight != None:
                    drzewo.edge(f"{x.data}", f"{y.destination}", label=f"{y.weight}")
                else:
                    drzewo.edge(f"{x.data}", f"{y.destination}")
        drzewo.render(view=True)



graf = Graph()
v0 = graf.create_vertex("v0")
v1 = graf.create_vertex("v1")
v2 = graf.create_vertex("v2")
v3 = graf.create_vertex("v3")
v4 = graf.create_vertex("v4")
v5 = graf.create_vertex("v5")
graf.add_directed_edge(v0, v1)
graf.add_directed_edge(v0, v5)
graf.add_directed_edge(v2, v1)
graf.add_directed_edge(v2, v3)
graf.add_directed_edge(v3, v4)
graf.add_directed_edge(v4, v1)
graf.add_directed_edge(v4, v5)
graf.add_directed_edge(v5, v1)
graf.add_directed_edge(v5, v2)
graf.traverse_depth_first(print)

