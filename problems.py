'''
From 8th edition, Operations Research an introduction by H.A. Taha
Solved by Shuto Araki (@ShutoAraki)
'''

from graph import Node, Edge, Graph

'''
Problem set 6.3B page 250, 251
1. 
The network defined by the following graph gives the distances in miles
between pairs of cities 1, 2, ..., and 8. Use Dijkstra's algorithm
to find the shortest route between the following cities.
(a) Cities 1 and 8
(b) Cities 1 and 6
(c) Cities 4 and 8
(d) Cities 2 and 6
'''
# Graph definition
vertex_set1 = {Node(i) for i in range(1, 9)}
edge_set1 = {
  Edge(Node(1), Node(2), 1),
  Edge(Node(1), Node(3), 2),
  Edge(Node(2), Node(3), 1),
  Edge(Node(2), Node(4), 5),
  Edge(Node(2), Node(5), 2),
  Edge(Node(3), Node(4), 2),
  Edge(Node(3), Node(5), 1),
  Edge(Node(3), Node(6), 4),
  Edge(Node(4), Node(5), 3),
  Edge(Node(4), Node(6), 6),
  Edge(Node(4), Node(7), 8),
  Edge(Node(5), Node(6), 3),
  Edge(Node(5), Node(7), 7),
  Edge(Node(6), Node(7), 5),
  Edge(Node(6), Node(8), 2),
  Edge(Node(7), Node(8), 6)
}

graph1 = Graph(vertex_set1, edge_set1)

graph1.dijkstra_path(Node(1))
'''
Final Result:
Distances {Node 1: 0, Node 2: 1, Node 3: 2, Node 4: 4, Node 5: 3, Node 6: 6, Node 7: 10, Node 8: 8}
Predecessors {Node 1: None, Node 2: Node 1, Node 3: Node 1, Node 4: Node 3, Node 5: Node 2, Node 6: Node 3, Node 7: Node 5, Node 8: Node 6}
Thus, the answer to (a) is 1 -> 3 -> 6 -> 8 and (b) is 1 -> 3 -> 6
'''

graph1.dijkstra_path(Node(4))
'''
Final Result:
Distances {Node 1: inf, Node 2: inf, Node 3: inf, Node 4: 0, Node 5: 3, Node 6: 6, Node 7: 8, Node 8: 8}
Predecessors {Node 4: None, Node 6: Node 4, Node 5: Node 4, Node 7: Node 4, Node 8: Node 6}
Thus, the answer to (c) is 4 -> 6 -> 8
'''
graph1.dijkstra_path(Node(2))
'''
Final Result:
Distances {Node 1: inf, Node 2: 0, Node 3: 1, Node 4: 3, Node 5: 2, Node 6: 5, Node 7: 9, Node 8: 7}
Predecessors {Node 2: None, Node 4: Node 3, Node 5: Node 2, Node 3: Node 2, Node 6: Node 3, Node 7: Node 5, Node 8: Node 6}
Thus, the answer to (d) is 2 -> 3 -> 6
'''


'''~
Problem set 6.3B page 250, 251
2. 
Use Dijkstra's algorithm to find the shortest route between node 1 and 
every other node in the network below.
'''
vertex_set2 = {Node(i) for i in range(1, 8)}
edge_set2 = {
  Edge(Node(1), Node(2), 5),
  Edge(Node(1), Node(3), 1),
  Edge(Node(2), Node(4), 7),
  Edge(Node(2), Node(5), 1),
  Edge(Node(2), Node(6), 6),
  Edge(Node(3), Node(2), 2),
  Edge(Node(3), Node(4), 6),
  Edge(Node(3), Node(5), 7),
  Edge(Node(4), Node(3), 7),
  Edge(Node(4), Node(6), 4),
  Edge(Node(4), Node(7), 6),
  Edge(Node(5), Node(4), 3),
  Edge(Node(5), Node(6), 5),
  Edge(Node(5), Node(7), 9),
  Edge(Node(6), Node(2), 7),
  Edge(Node(6), Node(7), 2)
}
graph2 = Graph(vertex_set2, edge_set2)
graph2.dijkstra_path(Node(1))
'''
Final Result:
Distances {Node 1: 0, Node 2: 3, Node 3: 1, Node 4: 7, Node 5: 6, Node 6: 11, Node 7: 13}
Predecessors {Node 1: None, Node 3: Node 1, Node 2: Node 3, Node 4: Node 3, Node 6: Node 2, Node 5: Node 2, Node 7: Node 4}
Thus, the answer to this question is
1 -> 3 -> 2
1 -> 3
1 -> 3 -> 4
1 -> 3 -> 2 -> 5
1 -> 3 -> 2 -> 6
1 -> 3 -> 4 -> 7
'''


'''
Problem set 6.3C page 256
3.
The Tell-All mobile-phone campany services six geographical areas.
The satellite distances (in miles) among the six areas are given
in the following graph. Tell0All needs to determine the most efficient 
message routes that should be estrablished between each two areas in 
the network.
'''
vertex_set3 = {Node(i) for i in range(1, 7)}
edge_set3 = {
  Edge(Node(1), Node(2), 700),
  Edge(Node(1), Node(3), 200), 
  Edge(Node(2), Node(3), 300), 
  Edge(Node(2), Node(4), 200), 
  Edge(Node(2), Node(6), 400), 
  Edge(Node(3), Node(4), 700), 
  Edge(Node(3), Node(5), 600), 
  Edge(Node(4), Node(5), 300), 
  Edge(Node(4), Node(6), 100), 
  Edge(Node(5), Node(6), 500)
}
graph3 = Graph(vertex_set3, edge_set3, directed=False)
graph3.all_pairs()

''' Outout
Shortest paths between all possible pairs
0 500 200 700 800 800
500 0 300 200 500 300
200 300 0 500 600 600
700 200 500 0 300 100
800 500 600 300 0 400
800 300 600 100 400 0

Thus, the answer is
Node 1 to 2: 500
Node 1 to 3: 200
Node 1 to 4: 700
Node 1 to 5: 800
Node 1 to 6: 800
Node 2 to 3: 300
Node 2 to 4: 200
Node 2 to 5: 500
Node 2 to 6: 300
Node 3 to 4: 500
Node 3 to 5: 600
Node 3 to 6: 600
Node 4 to 5: 300
Node 4 to 6: 100
Node 5 to 6: 400
'''