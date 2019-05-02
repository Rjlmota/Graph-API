from graph import *
from vertice import *
class AdjacencyList(Graph):

    def __init__(self, vertices):
        super().__init__(vertices)
        self.vertices = {x: Vertice(x) for x in vertices}
        

    def add_edge(self, id_1, id_2):
        self.vertices[id_1].add_neighbour(self.vertices[id_2])
        if( self.is_digraph and id_1 != id_2):
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

teste = AdjacencyList(['a', 'b', 'c'])
teste.add_edge("a", "b")
teste.add_edge("b", "c")
teste.print_graph()
print(teste.is_eulerian())