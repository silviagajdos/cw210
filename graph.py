class Vertex(object):
    def __init__(self, node):
            self.node = node
            self.edges = []
            self.tentativeWeight = float('inf')

class ExampleGraph(object):
    def __init__(self):
             self.vertices = {}
             
   #STRUCTURE FOR CREATING A GRAPH             
    def addVertex(self, node):
        if node not in self.vertices:
                self.vertices[node] = Vertex(node)
        else:
             print('Vertex does exist' % node)
 
    def addEdge(self, vertexA, vertexB):
            if vertexB not in self.vertices.get(vertexA).edges:
                self.vertices.get(vertexA).edges.append(vertexB)
                self.vertices.get(vertexB).edges.append(vertexA)
            else:
                 print(' Edge does exist' % (vertexA, vertexB))
         
    #IMPLEMENTED DEPTH_FIRST SEARCH WHICH CHECK IF TWO NODES ARE CONNECTED
    def isPath(self, VertexS, VertexT):
            stack = []
            visited = []
            Found = False
            stack.append(VertexS)
            while len(stack) > 0:
                x = stack.pop()
                 
                #CONDITION WHEN TARGET WAS FOUND 
                if x == VertexT: 
                            visited.append(x)
                            Found = True
                            break
                #WHEN TARGET WAS FOUND
                if x not in visited:
                            visited.append(x)
                            if len(e.vertices.get(x).edges) == 1:
                                 visited.pop(-1)
                            for i in e.vertices.get(x).edges:
                                 stack.append(i)
    
            #SAVE RESULT
            f = open('path.txt', 'w')
            if Found:
                f.write(str('Path between:'+str(VertexS)+' and '+str(VertexT)+' was found: '))
                f.write(str(visited))

            else:
                 f.write(str('Path between:'+str(VertexS)+' and '+str(VertexT)+' was not found'))
            f.close()
            return Found
        
   #By running isPath function between nodes, 
   #checks if the graph is strongly connected
   def isConnected(self):
        Connected=True
        for k in self.vertices:
            for l in self.vertices:
                if k != l:
                    Connected *= e.isPath(k,l) 
        # result changes to "False" if any instance is of value "False"
        if Connected:
                return True
        else:
                return False
            
if __name__ == '__main__':
    
        # Generate a  graph from 66Words file
        e = ExampleGraph()
        with open('66words.txt', 'r') as g:
          for x in g:
            e.addVertex(x)

            #VERTECIES NOT IMPLEMENTED. COULDNT COMPARE IF WORDS IN THE SAME SONNET
            #e.addVertex()

        print(e.isConnected())
