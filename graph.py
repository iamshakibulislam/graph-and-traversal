
class graph:
    def __init__(self):
        
        self.graph_structure = {}
        
        
    def add_connection(self,first_item,second_item):
        if first_item not in self.graph_structure:
            self.graph_structure[first_item] = []
            self.graph_structure[first_item].append(second_item)
            
        else:
            self.graph_structure[first_item].append(second_item)
            
        
        if second_item not in self.graph_structure:
            self.graph_structure[second_item] = []
            self.graph_structure[second_item].append(first_item)
            
        else:
            self.graph_structure[second_item].append(first_item)
            
        return self.graph_structure
        
    def BreadthFirstSearch(self,start_item):
        visited = []
        queue = []
        
        queue.append(start_item)
        #visited.append(start_item)
        
        while queue :
            
            slice=queue.pop(0)
            if slice not in visited:
                visited.append(slice)
            
                for item in self.graph_structure[slice]:
                    queue.append(item)
            
        
        return visited
            
            
            
        

g=graph()

g.add_connection(1,2)
g.add_connection(2,3)
g.add_connection(3,1)
g.add_connection(4,1)
g.add_connection(5,3)
print(g.graph_structure)

print(g.BreadthFirstSearch(2))
        
        