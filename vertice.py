class Vertice:
    def __init__(self, id):
        self.id = id
        self.neighbours = []
        self.color = "branco"
    
    def add_neighbour(self, vertice):
        self.neighbours.append(vertice)

    
    def is_neighbour(self, vertice):
        if(vertice in self.neighbours):
            return True
        return False
