# from pydantic import validate_arguments
import math as m

class Place: # aka Vertice

    # @validate_arguments
    def __init__(self, id: int):
        self.id = id
        self.distance = m.inf
        self.predecessor = None
        self.color = 'WHITE'
        self.finished = None

class City: # aka Graph

    # @validate_arguments
    def __init__(self, vertices: int, edges: int):
        self.num_of_places = vertices
        self.num_of_roads = edges
        self.adjMatrix = [[0] * vertices for i in range(vertices)] # initialize matrix
        self.adjMatrixTrans = [[0] * vertices for i in range(vertices)] # initialize matrix
        self.adjMatrixTrans_sorted = self.adjMatrixTrans.copy()
        self.poi = [Place(i) for i in range(1, vertices + 1)] # list of places in this city
        self.new_index = [i for i in range(vertices)]
        self.poi_sorted = self.poi.copy()
    
    # @validate_arguments
    def build_road(self, plan: str):
        a, b, c = plan.split()
        # เช็ค c if c == 1 --> [a][b] = 1 else if c == 2 --> [a][b] = 1 = [b][a]
        a = int(a) - 1
        b = int(b) - 1
        c = int(c)
        if c == 1:
            self.adjMatrix[a][b] = 1
            self.adjMatrixTrans[b][a] = 1
        else:
            self.adjMatrix[a][b] = 1
            self.adjMatrix[b][a] = 1
            self.adjMatrixTrans[b][a] = 1
            self.adjMatrixTrans[a][b] = 1
        