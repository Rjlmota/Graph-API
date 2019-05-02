from abc import ABC, abstractmethod


class Graph(ABC):
    vertices = []
    is_digraph = False

    def __init__(self, vertices, is_digraph = True):
        self.vertices = vertices
        self.is_digraph = is_digraph

    
    def print_graph(self) -> None:
        pass

    def add_edge(self, id_1 : str, id_2 : str) -> None:
        pass

    def is_eulerian(self) -> bool:
        pass
    
    def is_eulerian_open(self) -> bool:
        pass
    