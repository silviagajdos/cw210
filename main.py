import re
from collections import Counter 

class Node:
    stringsFromTuple=""

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        
    #METHOD FOR INSERING NODES TO BINARY TREE
    def insertNode(self, data):
        if self.data is None:
            self = Node(data)
        elif self.data > data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insertNode(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insertNode(data)
        return self
        
    #COUNT FREQUENCY OF ONE WORD IN BINARY TREE
    def frequency(self, key, Frequency = []): 
        if self.data == key:
		#IF FOUND, LIST APPENDED
            Frequency.append(self.data)
        if self.left is not None:
            self.left.frequency(key)
        if self.right is not None:
            self.right.frequency(key)
	
	#LENGTH OF THE LIST DETERMINES NUMBER OF ACCURANCY OF THE WORD
        finalCount = len(Frequency)
        return finalCount
            
    #FUNCTION TO FIND THE LEAF WITH MINIMUM VALUE --leftmost 
    def minimumNodeValue( node): 
        curNode = node 
        while(curNode.left is not None): 
            curNode = curNode.left  
        return curNode  
    
    #NON ORDERED TREE
    def preOrder(self):
      print (self.data)
      if self.left is not None:
          self.left.preOrder()
      if self.right is not None:
          self.right.preOrder()
        
    #DELETE THE NODE AND REORGANIZE TREE WITHOUT THAT NODE     
    def deleteNode(root, data): 
        if root is None: 
            return root  

        #FIND THE DESIRED NODE
        if data < root.data: 
            root.left = Node.deleteNode(root.left, data) 
        elif(data > root.data): 
            root.right = Node.deleteNode(root.right, data) 
        else: 
            if root.left is None : 
                value = root.right  
                root = None 
                return value 
              
            elif root.right is None : 
                value = root.left  
                root = None
                return value 
  
            #WHEN NODE HAS 2 CHILDREN
            value = Node.minimumNodeValue(root.right) 
  
            #REPLACE IN ORDER SUCCESSOR TO THE NODE 
            root.data = value.data 
  
            #DELETE IN ORDER SUCCESSOR
            root.right = Node.deleteNode(root.right , value.data) 
		
        return root    

#BUILD TREE FROM TEXT FILE
def buildTree(file_name):
    tree = None
    list = 0
    result = ""

    #WORDS THAT DO NOT COUNT STORE IN THE LIST
    exclusion_list = 'a the'.split()

    #FILE MANIPULATION
    with open(file_name) as string:
      content = string.readlines()
      #READ ONLY SONNETS FROM REQUIERED LINES
      for i in range(252,2868):
        result+=((content[i]))
      #REMOVE DIGITS
      stringFinal = re.sub("\d+", "", result)  
      list = stringFinal.split(' ')
      #ONLY NOT EMPTY LINES
      list[:] = [x for x in list if x]  
    
      #COUNTER FOR RETURNING 66MOST COMMON WORDS IN THE LIST FOR BINARY TREE EXCLUDING "A" AND "THE"
      counter = Counter(list)
      for x in exclusion_list:
        if x in counter:
          del counter[x]
      most_common = counter.most_common(66)
      print('66 most common words in Sonnets besides "the" and "a": ', most_common)
	
      #EXTRACT STRINGS FROM COUNTER TUPLE AND SAVE INTO NEW FILE
      stringsFromTuple, numbers = zip(*most_common)
      with open('graf.txt', 'w') as f:
        for item in stringsFromTuple:
          f.write("%s\n" % item)

      tree = Node(list[0])
      for i in list[1:]:
       
          tree.insertNode(i)
        
      return tree

tree = buildTree('Shakespear.txt')
print('-------------delete---------------------')
d= tree.deleteNode('presented') 
d= tree.preOrder()
