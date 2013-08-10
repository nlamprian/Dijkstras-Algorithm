''' Dijkstra's Algorithm (Computing Shortest Paths)
    Input:  adj_list - a dictionary with vertices as keys,
                       and edges as values in the form of list of neighboring vertices
            s - source vertex
    Output: cc - a list of sets, where every set represents a connected component '''

import sys
from connectedComponents import connectedComponents
from heap import Heap


def dijkstrasAlgorithm(adj_list,spDists,s):
	# frontier is a heap data structure that holds all the candidate vertices
	# to be considered on a next step for exploration
	explored, frontier = [], Heap(element=(0,s))
	
	while frontier.length(): # as long as there are candidate destination vertices, explore them
		key,v = frontier.extractMin() # get the next shortest distance-destination pair
		explored.append(v) # add the destination to the list with the ones that already explored
		spDists[v-1] = key # record the distance from the source vertex to that destination vertex

		for w,length in adj_list[v]: # investigate the neighboring vertices of the vertex that was just explored
			if w not in explored: # if a neighboring vertex w is not already explored
				score = spDists[v-1] + length # compute the distance from the source vertex to the vertex w through v
				if frontier.get(w): # if the vertex w was met before through a different path...
					heapNode = frontier.delete(w) # compare the two distances...
					score = min(score, heapNode[0]) # and keep the minimum distance
				frontier.insert((score,w)) # add vertex w to the prospective destination to be considered next


def initSPDists(adj_list,cc):
	spDists = [float('inf') for i in range(len(adj_list))]
	for v in range(1,len(adj_list)+1): # if you want to set some default value
		# for all vertices that are not in the component containing the source vertex,
		# define their shortest-path distance from the source vertex to be 1000000
		if v not in cc: spDists[v-1] = 1000000
	return spDists


def graph(filename):
	# the file is assumed to have, for every vertex v and every edge(v,w) with weight j,
	# a line in the following format: v w1,j1 w2,j2 w3,j3 ...
	adj_list, cc_adjlist = {}, {}
	with open(filename, 'r') as f:
		for line in f:
			nodes = line.split()
			adjVertexList, ccVertexList = [], []
			sN = int(nodes[0])
			for node in nodes[1:]:
				n = [int(i) for i in node.split(',')]
				adjVertexList.append((n[0],n[1]))
				ccVertexList.append(n[0])
			adj_list[sN] = adjVertexList # adjVertexList = [(vertex,length),(vertex,length),...]
			cc_adjlist[sN] = ccVertexList # ccVertexList = [vertex,vertex,...]
	return adj_list, cc_adjlist


if __name__ == "__main__":
	if len(sys.argv) < 3: sys.exit("Error: No input filename or source vertex.")
	filename, s = sys.argv[1], int(sys.argv[2]) # source vertex
	# goal vertices whose distance from the source vertex to return
	ret_vertices = [7,37,59,82,99,115,133,165,188,197]
	adj_list, cc_adjlist = graph(filename) # build the adjancency list

	ccs = connectedComponents(cc_adjlist) # compute the connected components
	for j,cc in enumerate(ccs): # find the component that includes the source vertex
		if s in cc: break
	cc = ccs[j] # keep the component containing the source vertex
	
	spDists = initSPDists(adj_list,cc) # initialize shortest-path distances
	dijkstrasAlgorithm(adj_list,spDists,s)
	ret_spdists = [str(spDists[i-1]) for i in ret_vertices]
	print(','.join(ret_spdists))
	# print(spDists)
