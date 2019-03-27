class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class Tree:
    def __init__(self):
        self.root = None


    def add(self, value):
        if(self.root == None):
            self.root = Node(value)
        else:
            self.addNode(value, self.root)

    def addNode(self, value, obj):
        if(value < obj.value):
            if(obj.left != None):
                self.addNode(value, obj.left)
            else:
                obj.left = Node(value)
        else:
            if(obj.right != None):
                self.addNode(value, obj.right)
            else:
                obj.right = Node(value)


    def printTree(self):
        if(self.root != None):
            self.pT(self.root)

    def pT(self, obj):
        '''
             8
            / \\
           6   9
          /
         4      
        /
       3
      / \        
     1   8
    '''
        if(obj != None):
            self.pT(obj.left)
            self.pT(obj.right)
   
            print (str(obj.value) + ' ')
            
tree = Tree()
tree.add(8)
tree.add(6)
tree.add(9)
tree.add(4)
tree.add(3)
tree.add(1)
tree.add(8)


tree.printTree()
print(Tree.pT.__doc__)
