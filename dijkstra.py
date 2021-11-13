import sys

class Graph():
    def __init__(self, vertices):
# ********* Insert your code here ************** #
 
# ***********************************************#
                    
    def printSolution(self, dist):
# ********* Insert your code here ************** #
 
# ***********************************************#


    
    def minDistance(self, dist, sptSet):

# ********* Insert your code here ************** #
 
# ***********************************************#
        
    def dijkstra(self, src):
        print("Vertex  Distance from Source")
        for node in range(self.V):
            print(node, " ", dist[node])

def main():
    g = Graph(5)
    g.graph=[[0,3,0,7,0],[3,0,4,2,0],[0,4,0,5,6],[7,2,5,0,4],[0,0,6,4,0]]
    g.dijkstra(0)
    
    

if __name__ == '__main__':
    main()



