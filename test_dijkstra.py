import pytest
import dijkstra

def test_huf(capfd):

    g = dijkstra.Graph(5)
    g.graph=[[0,3,0,7,0],[3,0,4,2,0],[0,4,0,5,6],[7,2,5,0,4],[0,0,6,4,0]]

    g.dijkstra(0)
    
    out, err = capfd.readouterr()
    print(out)
    a="Vertex  Distance from Source\n0   0\n1   3\n2   7\n3   5\n4   9\n"    
    assert str(out) == a

def test_huf1(capfd):
    g = dijkstra.Graph(5)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
		[4, 0, 8, 0, 0, 0, 0, 11, 0],
		[0, 8, 0, 7, 0, 4, 0, 0, 2],
		[0, 0, 7, 0, 9, 14, 0, 0, 0],
		[0, 0, 0, 9, 0, 10, 0, 0, 0],
		[0, 0, 4, 14, 10, 0, 2, 0, 0],
		[0, 0, 0, 0, 0, 2, 0, 1, 6],
		[8, 11, 0, 0, 0, 0, 1, 0, 7],
		[0, 0, 2, 0, 0, 0, 6, 7, 0]
		]

    g.dijkstra(0)
    
    out, err = capfd.readouterr()
    #print(out)
    a="Vertex  Distance from Source\n0   0\n1   4\n2   12\n3   19\n4   28\n"    
    assert str(out) == a