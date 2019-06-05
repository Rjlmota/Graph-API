import graph
import graph_matrix as mtx
import graph_adj as adj

import dfs
import bfs
'''
def read_file(path):
    ygrafos = []
    with open(path) as f:
        reader = csv.reader(f, delimiter = ';')
        for row in reader:
            vertices = (row[0][1:-1]).split(",")
            #print(vertices)
            new_graph = Graph(vertices)

            edges = row[1].split(",")
            for edge in edges:
                edge = (edge[1:-1].split(" "))
                new_graph.add_edge(edge[0], edge[1])

            grafos.append(new_graph)
    return grafos



graph_list = read_file("grafos.txt")
'''

while True:
	print("INTERFACE - GRAFOS")


	while True:
		graph_type = input("l - Listas de adjacência\nm- Matriz de Adjacência\nEscolha um tipo:").lower()
		if(graph_type in ['l', 'm']):
			break
	while True:
		dir = input("O grafo é direcionado? (y/n)").lower()
		if(dir in ['y', 'n']):
			break


	if(dir == 'y'): dir = True
	else: dir = False		

	vertices = []
	print("ADICIONAR VÉRTICES")
	while True:
		vertice = input("Informe um vértice (quit para sair)-> ")
		if(vertice != "quit"):
			vertices.append(vertice)

		else:
			break


	graph = None
	if(graph_type == "m"):
		graph = mtx.GraphMatrix(vertices, dir)
	elif(graph_type == "l"):
		graph = adj.AdjacencyList(vertices, dir)

	
	print("ADICIONAR ARESTAS - e.g, 'a b' ")
	while True:
		aresta = input("Informe uma aresta (quit para sair): ")
		if(aresta == "quit"):
			break
		graph.add_edge(aresta[0], aresta[2])

	
	print("Você montou o seguinte grafo")
	graph.print_graph()

	while True:
		op = input("O que você deseja?\n1. DFS\n2.BFS\n")

		if(op == "1"):
			search = dfs.DFS()
			print("Visitados pelo DFS: ")
			print(search.dfs(graph))

		if(op == "2"):
			search = bfs.BFS()
			root = input("Informe o vértice fonte: ")
			print("Visitados pelo BFS: ")
			print(search.run(graph, root))


