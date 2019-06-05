import graph

class BFS:
    qeue = []
    
    def __init__(self):
        self.discovery = {}
        self.color = {}
        self.previous = {}
        self.path = []
        self.graph = None
    def run(self, graph, root):
    
        self.graph = graph
        self.discovery = {x : 9*10**31 for x in graph.vertices}
        self.color = {x : "branco" for x in graph.vertices}
        self.previous = {x : None for x in graph.vertices}


        if(root not in self.graph.vertices):
            exit(1)


        self.discovery[root] = 0
        self.color[root] = "cinza"
        self.qeue.append(root)

        while(len(self.qeue) != 0):
            u = self.qeue.pop(0)
            self.path.append(u)
            for neighbour in self.graph.get_neighbours(u):
                if(self.color[neighbour] == "branco"):
                    self.color[neighbour] = "cinza"
                    self.previous[neighbour] = u
                    self.qeue.append(neighbour)
            self.color[u] = "preto"

        return self.path


    