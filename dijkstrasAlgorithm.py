import sys
from connectedComponents import connectedComponents
from heap import Heap


def dijkstrasAlgorithm(adj_list, source, connectedComponent = None):
	'''
	Dijkstra's Shortest Path Algorithm

	Args:
		adj_list: an adjacency list (w/ edge weights), realized as a dictionary
				  in the form adj_list[vertex1] = [(vertex2,length2),(vertex3,length3),...].
		source: the id of the vertex that acts as a starting point for the algorithm
		conComponent: if the graph is not connected, this is going to be a set with the vertices
					  of the connected component containing the source vertex.

	Returns:
		sPDists: a dictioary with the shortest-path distances from the source vertex
	'''
	sPDists = initSPDists(adj_list, connectedComponent)
	explored, frontier = [], Heap(element = (0,source))
	
	while frontier.length():
		distance, vertex = frontier.extractMin()
		explored.append(vertex)
		sPDists[vertex] = distance

		for w,length in adj_list[vertex]:
			if w not in explored:
				# Computes the distance from the source vertex to vertex w through the vertex v
				score = sPDists[vertex] + length
				if frontier.get(w):  # If vertex w was met before through a different path,
					wNode = frontier.delete(w)
					score = min(score, wNode[0])  # it compares the two distances and keeps the minimum
				frontier.insert((score,w)) # Adds vertex w back to the heap

	return sPDists


def initSPDists(adj_list, connectedComponent):
	'''
	Initializes the shortest-path distances (to the value 'Inf')

	If the graph is not connected, if offers the ability to set a default value
	to all vertices not in the connected component containing a source vertex.

	Args:
		adj_list: an adjacency list
		conComponent: a set with the vertices of the connected component containing the source vertex,
					  or None if the graph is connected.

	Returns:
		sPDists: a dictionary that is going to hold the shortest-path distances
	'''
	sPDists = {vertex: float('inf') for vertex in adj_list}

	if connectedComponent:
		defaultValue = 1000000
		for vertex in adj_list:
			if vertex not in cc: sPDists[vertex] = defaultValue

	return sPDists


def graph(filename):
	'''
	Builds the adjacency list of a graph

	Assumptions:
		There is a line, in the file, for every vertex v and every edge(v,w) with weight j,
		in the form v w1,j1 w2,j2 w3,j3 ... wk,jk

	Args:
		filename: the name of the file containing an adjacency list to be parsed

	Returns:
		adj_list: an adjacency list (w/ edge weights), realized as a dictionary
				  in the form adj_list[vertex1] = [(vertex2,length2),(vertex3,length3),...]
		cc_adjlist: an adjacency list (w/o edge weights), realized as a dictionary
					in the form cc_adjlist[vertex1] = [vertex2,vertex3,...]
	'''
	adj_list, cc_adjlist = {}, {}

	with open(filename, 'r') as f:
		for line in f:
			nodes = line.split()
			adjVertexList, ccVertexList = [], []
			sourceVertex = int(nodes[0])

			for node in nodes[1:]:
				vertex, weight = [int(i) for i in node.split(',')]
				adjVertexList.append((vertex,weight))
				ccVertexList.append(vertex)

			adj_list[sourceVertex] = adjVertexList
			cc_adjlist[sourceVertex] = ccVertexList

	return adj_list, cc_adjlist



if __name__ == "__main__":
	if len(sys.argv) < 3: sys.exit("Error: No filename or source vertex id")
	filename, source = sys.argv[1], int(sys.argv[2])
	# goal vertices whose distances from the source vertex are to be returned
	returnedVertices = [7,37,59,82,99,115,133,165,188,197]
	
	adj_list, cc_adjlist = graph(filename)

	ccs = connectedComponents(cc_adjlist)  # Computes the connected components,
	for j,cc in enumerate(ccs):  # finds the component that includes the source vertex,
		if source in cc: break
	cc = ccs[j]  # and keeps the component containing the source vertex
	
	sPDists = dijkstrasAlgorithm(adj_list, source, cc)

	returnedSPDists = [str(sPDists[vertex]) for vertex in returnedVertices]
	print(','.join(returnedSPDists))
	# print(sPDists)
