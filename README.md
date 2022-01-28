This is a graph script. <br>
Add connection to the graph --> instance.add_connection(item1,item2) <br>
traverse the graph -- > instance.BreadthFirstSearch(any item) <br>

Example:<br>

g=graph()<br>

g.add_connection(1,2)<br>
g.add_connection(2,3)<br>
g.add_connection(3,1)<br>
g.add_connection(4,1)<br>
g.add_connection(5,3)<br>


print(g.graph_structure)

print(g.BreadthFirstSearch(2))
