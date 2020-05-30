''' GENERIC BINARY TREE IMPLEMENTATION

        BINARY TREE <NODE>
            ROOT 
                Stores the reference to the root Node.
            
            INSERT <Key>
                If left is empty inserts as left child.
                Else If right is empty inserts as right child.
                Else randomly selects a child and repeat.
            
            SEARCH <Data>
                Uses level order to traverse the tree,
                Returns the first node where <Data> matches the Key.
            
            REMOVE <Key>
                Searches the node to be removed. 
                If node to be removed has both left and right child, 
                    then REMOVE(leftmost child) 
                    and replaces at node's position. 
                Else links parent and child (if exists).
            
            TRAVERSE <MethodName>
                Traverses the tree using the <MethodName> passed,
                Prints the output in a 1D Array.
            
            PREETYPRINT
                Prints in 2D tree format.
'''

import random

class Node:
    def __init__(self, data = None):
        self.key = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, node = None):
        self.root = node
    
    def insert(self, key):
        if not self.root:
            self.root = Node(key)
            return True
        
        return self.__insertHelper(key, self.root)
        
    def search(self, key):
        if self.root:
            queue = [self.root]
            
            while queue:
                node = queue.pop(0)
                if key == node.key: return node
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            
        return None
    
    def remove(self, key):
        if key == self.root.key:
            node = self.root
            
            if not node.left and not node.right:
                self.root = None
                
            elif not node.left or not node.left:
                self.root = node.left or node.right
                
            else: # Replace root with leftmost node in the tree.
                lNode = node.left
                lParent = node
                while lNode.left:
                    lParent = lNode
                    lNode = lNode.left
                    
                if lParent == node:
                    lNode.left = node.right 
                else :
                    lParent.left = lNode.right
                    lNode.left = node.left
                    lNode.right = node.right
                    
                self.root = lNode
        else:
            nodeParent = self.__searchParent(key)
            nodePos = 'left' if nodeParent.left.key == key else 'right'
            node = nodeParent.__getattribute__(nodePos)
            
            if nodeParent.left and nodeParent.right and node.left and node.right:
                lNode = node.left
                lParent = node
                while lNode.left:
                    lParent = lNode
                    lNode = lNode.left
                    
                if lParent == node:
                    lNode.left = node.right 
                else :
                    lParent.left = lNode.right
                    lNode.left = node.left
                    lNode.right = node.right
                    
                nodeParent.__setattr__(nodePos, lNode)
                
            elif not nodeParent.left or not nodeParent.right:
                nodeParent.left, nodeParent.right = node.left, node.right
                
            else:
                nodeParent.__setattr__(nodePos, node.left or node.right)
        
        node.left = node.right = None
        return node
    
    def traverse(self, orderFunc='inOrder') :
        orderDict = {
            'inOrder' : self.__inOrder, 
            'preOrder' : self.__preOrder, 
            'postOrder' : self.__postOrder, 
            'levelOrder' : self.__levelOrder, 
            'spiralOrder' : self.spiralOrder, 
            'verticalOrder' : self.verticalOrder, 
            'inorderReverse' : self.__inOrderReverse, 
            'levelOrderReverse' : self.levelOrderReverse 
            }
        
        print('\n\n' + orderFunc + ' traversal :', end=' ')
        if orderFunc in orderDict and self.root :
            orderDict[orderFunc](self.root)
    
    def prettyPrint(self):
        print('___________ Printing Binary Tree ___________\n')
        self.__printHelper(self.root, 0, False)
        print('____________________________________________')
    
    def __insertHelper(self, key, node):
        if not node.left : 
            node.left = Node(key)
            return True
        
        if not node.right : 
            node.right = Node(key)
            return True
        
        choice = random.choice([1,0])
        return self.__insertHelper(key, node.left if choice else node.right)
    
    def __searchParent(self, key):
        if self.root:
            if key == self.root.key: 
                return None
             
            queue = [self.root]
            
            while queue:
                node = queue.pop(0)
                if node.left: 
                    if key == node.left.key:
                        return node
                    queue.append(node.left)
                if node.right: 
                    if key == node.right.key:
                        return node
                    queue.append(node.right)
            
        return None
    
    def __inOrder(self, node):
        if node:
            self.__inOrder(node.left)
            print(node.key, end=', ')
            self.__inOrder(node.right)
        
    def __preOrder(self, node): 
        if node:
            print(node.key, end=', ')
            self.__preOrder(node.left)
            self.__preOrder(node.right)
    
    def __postOrder(self, node):
        if node:
            self.__postOrder(node.left)
            self.__postOrder(node.right)
            print(node.key, end=', ')
            
    def __levelOrder(self, node):
        self.levelOrder()
            
    def levelOrder(self):
        if self.root:
            queue = [self.root]
            
            while queue:
                node = queue.pop(0)
                print(node.key, end=', ')
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        
    def spiralOrder(self, node): pass
    
    def verticalOrder(self, node): pass
    
    def __inOrderReverse(self, node):
        if node:
            self.__inOrderReverse(node.right)
            print(node.key, end=', ')
            self.__inOrderReverse(node.left)
        
    def levelOrderReverse(self, node): pass
    
    def __printHelper(self, node, indent, isleftChild):
        if node:
            text = '       ' * indent + ('\\----' if isleftChild else '/----')
            
            self.__printHelper(node.right, indent+1, False)
            print(text,node.key)
            self.__printHelper(node.left, indent+1, True)

if __name__=='__main__':
    
    tree = BinaryTree()
    
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)
    tree.insert(6)
    tree.insert(7)
    tree.insert(8)
    tree.insert(9)
    tree.insert(10)
    tree.insert(11)
    tree.insert(12)
    tree.insert(13)
    tree.insert(14)
    tree.insert(15)
    tree.insert(16)
    tree.insert(17)
    tree.insert(18)
    tree.insert(19)
    
    #tree.traverse('inOrder')
    tree.prettyPrint()