from graph import *


class DFS:
    def __init__(self):
        
        self.graph = None

        #Initializing core variables
        self.time = 0
        self.colors = {}
        self.path = []

        self.discovery_time = {}
        self.completion_time = {}

        self.previous = {}

        self.forest = []

        self.tree = []

    def _dfs_visit(self, vertice):
        
        #Adding vertice to path and painting it grey
        self.path.append(vertice)
        self.colors[vertice] = "grey"



        #Updating time counter and assigning discovery time to the current vertice.
        self.time += 1
        self.discovery_time[vertice] = self.time


        self.tree.append(vertice)

        #Runs through the neighbours of the current vertice
        #and visits the nodes that were not visited yet.
        for neighbour in self.graph.get_neighbours(vertice):
            if(self.colors[neighbour] == "white"):
                self.previous[neighbour] = vertice
                self._dfs_visit(neighbour)
        self.colors[vertice] = "black"

        #Updating time counter and assigning finish time.
        self.time += 1
        self.completion_time[vertice] = self.time


    def dfs(self, graph):
        #Initializing two dicts to store information about each
        #vertice.
        self.graph = graph
        self.colors = {id : "white" for id in graph.vertices}
        self.previous = {id : None for id in graph.vertices}

        for vertice in graph.vertices:
            if(self.colors[vertice] == "white"):
                
                #Local tree to build forest later
                self.tree = []            
                self._dfs_visit(vertice)
                self.forest.append(self.tree)

        print("PATH: ", self.path)
        print("FOREST: ", self.forest)
        return self.path
        
