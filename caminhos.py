import graph_matrix as mtx
import graph_adj as adj
import dfs
import operator

def warshall(graph):
	matrix = [row[:] for row in graph.matrix]
	n = len(graph.vertices)
	for k in range(n):
		for i in range(n):
			for j in range(n):
				if(matrix[i][j] == 1 or (matrix[i][k] == 1 and matrix[k][j] == 1)):
					matrix[i][j] = 1

	return matrix



def topologic_sort(graph):
	search = dfs.DFS()
	search.dfs(graph)
	#sorted(d.items(), key=lambda x: x[1])
	print(search.completion_time)
	
	return (sorted(search.completion_time.items(), key=operator.itemgetter(1), reverse=True))
	#print(sorted(search.completion_time.items, key = lambda x: x[1]))


def strongly_connected(graph):
	
	
	print("DFS em Grafo")
	search = dfs.DFS()
	search.dfs(graph)

	_finished = (sorted(search.completion_time.items(), key=operator.itemgetter(1), reverse=True))

	finished = []
	for item in _finished:
		finished.append(item[0])


	transgraph = None
	if isinstance(graph, adj.AdjacencyList):
		transgraph = adj.AdjacencyList(finished)
	elif isinstance(graph, mtx.GraphMatrix):
		transgraph = mtx.GraphMatrix(finished)

	for x in graph.vertices:
		for y in graph.vertices:
			if(graph.is_neighbour(x, y)):
				transgraph.add_edge(y, x)


	#transgraph.print_graph()

	print("DFS em Grafo'") 
	search2 = dfs.DFS()
	search2.dfs(transgraph)

	print("COMPONENTES FORTEMENTE CONECTADOS:")
	print(search2.forest)
	return(search2.forest)



teste = mtx.GraphMatrix(['a', 'b', 'c', 'd', 'e', 'f'], True)
teste.add_edge("a", "b")
teste.add_edge("b", "c")
teste.add_edge("c", "d")
teste.add_edge("d", "a")

#Second tree
teste.add_edge("e", "f")
teste.add_edge("f", "e")

teste.print_graph()

print("Componentes fortemente conectados: ")
strongly_connected(teste)


#print(warshall(teste))
#print(topologic_sort(teste))