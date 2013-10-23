import sys


def BFS(adj_list, source):
	'''
	Breadth First Search Algorithm
	
	Works on both undirected and directed graphs

	Args:
		adj_list: a dictionary where the keys are vertex ids, and the values are lists of vertex ids.
				  each pair of key-value_j, for value_j \in adj_list[key], constitutes an edge.
		source: the id of the vertex that acts as a starting point for the algorithm

	Returns:
		explored: a set of ids of all reachable vertices from the source vertex
	'''
	explored, frontier = {source}, [source]

	while frontier:
		v = frontier.pop(0)
		for w in adj_list[v]:
			if w not in explored:
				explored.add(w)
				frontier.append(w)

	return explored



if __name__ == "__main__":
	# Expects a filename (adjacency list), and an id (source vertex)
	if len(sys.argv) < 3: sys.exit("Error: No filename or source vertex id")
	filename, source = sys.argv[1], int(sys.argv[2])

	adj_list = {}
	with open(filename, 'r') as f:
		# Builds the adjacency list
		for line in f:  # v w1 w2 w3 ...
			vertices = line.split()
			adj_list[int(vertices[0])] = [int(v) for v in vertices[1:]]

	explored = BFS(adj_list, source)
	print(explored)
