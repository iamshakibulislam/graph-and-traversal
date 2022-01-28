This is a graph script.
Add connection to the graph --> instance.add_connection(item1,item2)
traverse the graph -- > instance.BreadthFirstSearch(any item)

Example:

g=graph()

g.add_connection(1,2)
g.add_connection(2,3)
g.add_connection(3,1)
g.add_connection(4,1)
g.add_connection(5,3)


print(g.graph_structure)

print(g.BreadthFirstSearch(2))
