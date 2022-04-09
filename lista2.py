
from collections import defaultdict
#Thyago do Nascimento Pereira RGM:23439386 5ºsemestre de ciência da computação

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.Graph = defaultdict(list)
        self.Time = 0

    def addEdge(self, n, v):
        self.Graph[n].append(v)
        self.Graph[v].append(n)

    def bridgeUtil(self, n, vizinho, ponte, low, disc):

        vizinho[n] = True

        disc[n] = self.Time
        low[n] = self.Time
        self.Time += 1

        for v in self.Graph[n]:

            if vizinho[v] == False:
                ponte[v] = n
                self.bridgeUtil(v, vizinho, ponte, low, disc)

                low[n] = min(low[n], low[v])

                if low[v] > disc[n]:
                    print("%d %d" % (n, v))


            elif v != ponte[n]:
                low[n] = min(low[n], disc[v])

    def printfraph(self):
        # for x in range(1, self.Graph._len_()):
        #   print(f"{self.Graph[x]} ", end="")
        for y in range(1, self.V):
            print(f"")
            for z in range(1, self.V):
                if z in self.Graph[y]:
                    print(f"{z} ", end="")
                else:
                    print("0 ", end="")
        print("")

    def bridge(self):

        vizinho = [False] * (self.V)
        disc = [float("Inf")] * (self.V)
        low = [float("Inf")] * (self.V)
        ponte = [-1] * (self.V)

        for i in range(self.V):
            if vizinho[i] == False:
                self.bridgeUtil(i, vizinho, ponte, low, disc)


    Graph = [
   [0,1,1,1,0,0],
   [1,0,1,0,0,0],
   [1,1,0,0,1,1],
   [1,0,0,0,0,0],
   [0,0,1,0,0,1],
   [0,0,1,0,1,0],
]


g1 = Graph(7)
g1.addEdge(1, 2)
g1.addEdge(1, 3)
g1.addEdge(1, 4)
g1.addEdge(2, 3)
g1.addEdge(3, 5)
g1.addEdge(3, 6)
g1.addEdge(5, 6)
g1.printfraph()
print("as Aresta(s) que são ponte é:")
g1.bridge()

