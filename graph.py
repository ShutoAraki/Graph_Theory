'''
@author: Shuto Araki
@date: 09/25/2019
'''

class Node(object):
  def __init__(self, id, name=""):
    self.id = id
    self.inflow = []
    self.outflow = []
    self.name = str(id) if name == "" else name
  
  def __hash__(self):
    return self.id
  
  def __eq__(self, other):
    return self.id == other.id
  
  def __repr__(self):
    return "Node " + self.name


class Edge(object):
  def __init__(self, from_node, to_node, cost=0.0):
    self.from_node = from_node
    self.to_node = to_node
    self.cost = cost

  def get_reverse_edge(self):
    return Edge(self.to_node, self.from_node, self.cost)
  
  def __hash__(self):
    return (self.from_node, self.to_node, self.cost).__hash__()

  def __repr__(self):
    return str(self.from_node.name) + " -" + str(self.cost) + "-> " + str(self.to_node.name)


class Graph(object):
  def __init__(self, vertex_set, edge_set, directed=True):
    '''
    vertex_set: A set of Node objects
    edge_set: A set of Node tuples
    '''
    self.vertices = vertex_set
    self.edges = edge_set.copy()
    if not directed:
      for edge in edge_set:
        reverse_edge = edge.get_reverse_edge()
        self.edges.add(reverse_edge)
    
    for v in self.vertices:
      for edge in self.edges:
        if edge.from_node == v:
          v.outflow.append(edge.to_node)
        if edge.to_node == v:
          v.inflow.append(edge.from_node)


  def get_cost(self, i, j):
    for edge in self.edges:
      if edge.from_node == i and edge.to_node == j:
        return edge.cost
    print("Such edge does not exist.")
  

  def dijkstra_path(self, source):
    '''
    Find shortest paths from a given source to 
    all other vertices in this graph
    '''
    print(f"Shortest paths starting from {source}")
    # Initialize lists and dictionaries
    nodes = list(self.vertices)
    S = []
    d = dict(zip(nodes, [float('inf')] * len(self.vertices)))
    Sc = d.copy()
    d[source] = 0
    pred = {}
    pred[source] = None

    iteration = 0
    while len(S) < len(nodes):
      print(f"Iteration #{iteration}")
      print("\tDistance labels so far")
      print("\t", d)
      print("\tPredecessors so far")
      print("\t", pred)
      i = list(Sc.keys())[0]
      for node, cost in Sc.items():
        if cost < Sc[i]:
          i = node
      S.append(i)
      del Sc[i]
      for j in i.outflow:
        if d[j] > d[i] + self.get_cost(i, j):
          print(f"\tUpdate the cost from {i} to {j}: the new cost is {d[i] + self.get_cost(i, j)}")
          d[j] = d[i] + self.get_cost(i, j)
          pred[j] = i
      iteration += 1
    
    print("Final Result:")
    print("Distances", d)
    print("Predecessors", pred)
    print()


  def _print_matrix(self, matrix):
    V = len(matrix)
    for i in range(V):
      print(*matrix[i])


  def all_pairs(self):
    print(f"Shortest paths between all possible pairs")
    V = len(self.vertices)
    ans_matrix = [[0 if i == j else float('inf') for i in range(V)] for j in range(V)]
    for edge in self.edges:
      i = edge.from_node.id - 1
      j = edge.to_node.id - 1
      ans_matrix[i][j] = edge.cost
    
    for i in range(V):
      for j in range(V):
        for k in range(V):
          ans_matrix[i][j] = min(ans_matrix[i][j], ans_matrix[i][k] + ans_matrix[k][j])
    
    self._print_matrix(ans_matrix)