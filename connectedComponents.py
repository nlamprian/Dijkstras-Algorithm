import sys
from bfsAlgorithm import BFS


def connectedComponents(adj_list):
	'''
	Computes the connected components of an undirected graph

	Args:
		adj_list: a dictionary where the keys are vertex ids, and the values are lists of vertex ids.
				  each pair of key-value_j, for value_j \in adj_list[key], constitutes an edge.

	Returns:
		cc: a list of sets, where each set holds the vertex ids of the corresponding connected component
	'''
	explored, cc = set(), []

	for v in adj_list:
		if v not in explored:
			c = BFS(adj_list, v)
			explored |= c
			cc.append(c)

	return cc



if __name__ == "__main__":
	# Expects a filename (adjacency list)
	if len(sys.argv) < 2: sys.exit("Error: No filename")
	filename = sys.argv[1]

	adj_list = {}
	with open(filename, 'r') as f:
		# Builds the adjacency list
		for line in f:  # v w1 w2 w3 ...
			vertices = line.split()
			adj_list[int(vertices[0])] = [int(v) for v in vertices[1:]]

	ccs = connectedComponents(adj_list)
	print(ccs)
