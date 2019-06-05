from graph import *
from vertice import *
import dfs
class AdjacencyList(Graph):

    def __init__(self, vertices, is_digraph = False):
        super().__init__(vertices, is_digraph)
        self.vertices = {x: Vertice(x) for x in vertices}
        

    def add_edge(self, id_1, id_2):
        self.vertices[id_1].add_neighbour(self.vertices[id_2])
        if(id_1 != id_2 and self._is_digraph):
            self.vertices[id_2].add_neighbour(self.vertices[id_1])
    
    def print_graph(self):
        for vertice in self.vertices.values():
            print(vertice.id, end = '-> {')
            [print(neighbour.id, end = ' ') for neighbour in vertice.neighbours]
            print("}")


    def is_eulerian(self):
        for vertice in self.vertices.values():
            if(len(vertice.neighbours) % 2 == 1):
                return False
        return True

    def is_eulerian_open(self):
        odd_counter = 0
        for vertice in self.vertices.values():
            if(len(vertice.neighbours) % 2 == 1):
                odd_counter += 1    
        if(odd_counter == 2):
            return True
        else:
            return False


    def is_neighbour(self, a, b):
        if(b in self.vertices[a].get_neighbours):
            return True
        else:
            return False



    def get_neighbours(self, vertice):
        return [neighbour.id for neighbour in self.vertices[vertice].neighbours]
            
        

teste = AdjacencyList(['a', 'b', 'c'])
teste.add_edge("a", "b")
teste.add_edge("b", "c")
teste.print_graph()
print(teste.is_eulerian())

search = dfs.DFS()

print(search.dfs(teste))