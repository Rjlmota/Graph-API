import graph

class BFS():

    self.qeue = []

    def __init__(graph):
        self.graph = graph
        self.discovery = {x : 9*10**31 for x in graph.vertices}
        self.color = {x : "branco" for x in graph.vertices}
        self.previous = {x : None for x in graph.vertices}

    def run(root):
        self.discovery[root] = 0
        self.color[root] = "cinza"
        qeue.append(root)

        while(len(qeue) != 0):
            u = qeue.pop[0]
            for neighbour in u.neighbours:
                if(self.color[neighbour] == "branco"):
                    self.color[neighbour] = "cinza"
                    self.antecessor[neighbour] = u
                    qeue.append(neighbour)
            self.color[u] = preto


            