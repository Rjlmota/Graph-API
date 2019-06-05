import graph
import dfs
import bfs
class GraphMatrix(graph.Graph):


    def __init__(self, vertices, is_digraph = False):
        super().__init__(vertices, is_digraph)

        length = len(vertices)
        self.matrix = [[0 for x in range(length)] for y in range(length)]
        self.vertices = vertices


    def add_edge(self, a, b):
        if(a not in self.vertices or b not in self.vertices):
            print("Vertice not found")
        
        #Assigning variables for code readability
        index_a = self.vertices.index(a)
        index_b = self.vertices.index(b)

        self.matrix[index_a][index_b] = 1
        if(not self._is_digraph):
            self.matrix[index_b][index_a] = 1
            
            
    def print_graph(self):
        print(" ", end = '  ') #Initial padding
        [print(x, end = '  ') for x in self.vertices] #Printing column labels
        print() # \n
        for i in range(len(self.vertices)): #Iterates through each line of the matrix based on the vertices array.
            print(self.vertices[i], self.matrix[i])

    
    def is_eulerian(self):
        for row in self.matrix:
            if(sum(row)%2 == 1):
                return False
        return True
    
    def is_eulerian_open(self):
        odd_counter = 0
        for row in self.matrix:
            if((sum(row) % 2) == 1):
                odd_counter += 1
                
        if(odd_counter == 2):
            return True
        return False

    def get_neighbours(self, vertice):
        neighbours = []
        index = self.vertices.index(vertice)
        for i in range(len(self.vertices)):
            if(self.matrix[index][i] == 1):
                neighbours.append(self.vertices[i])
        return neighbours


    def is_neighbour(self, a, b):
        a_index = self.vertices.index(a)
        b_index = self.vertices.index(b)

        if(self.matrix[a_index][b_index] == 1):
            return True
        else:
            return False




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
teste = GraphMatrix(['a', 'b', 'c'])
teste.add_edge("a", "b")
teste.add_edge("b", "c")
teste.print_graph()

search = dfs.DFS()
print(search.dfs(teste))   


search = bfs.BFS()

print(search.run(teste, "a"))