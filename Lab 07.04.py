'''Lab 07.04'''
class BSTNode:
    '''class'''
    def __init__(self, data=None):
        '''__init__'''
        self.data = data
        self.left = None
        self.right = None
    def get_data(self):
        '''get_data'''
        return self.data
    def set_data(self, data):
        '''set_data'''
        self.data = data
    def get_left(self):
        '''get_left'''
        return self.left
    def set_left(self, left):
        '''set_left'''
        self.left = left
    def get_right(self):
        '''get_right'''
        return self.right
    def set_right(self, right):
        '''set_right'''
        self.right = right

class BST:
    '''class'''
    def __init__(self, root=None):
        '''__init__'''
        self.root = BSTNode(root)
    def get_root(self):
        '''get_root'''
        return self.root
    def set_root(self, root):
        '''set_root'''
        self.root = root
    def insert(self, data):
        '''INSER'''
        root = self.root
        if root.data is None:
            root.set_data(data)
            return
        if root.data == data:
            return
        if data < root.data:
            if root.left:
                root.left.insert(data)
                return
            root.left = BST(data)
            return
        if root.right:
            root.right.insert(data)
            return
        root.right = BST(data)
    def preorder(self):
        '''preorder'''
        root = self.root
        if root.data:
            print("-> " + str(root.data), end=" ")
        if root.left:
            root.left.preorder()
        if root.right:
            root.right.preorder()
        return
    def is_empty(self):
        '''emp'''
        if self.root == None or self.root.data == None:
            return True
        return False

    def inorder(self):
        '''In'''
        root = self.root
        if root.left:
            root.left.inorder()
        if root.data:
            print("-> " + str(root.data), end=" ")
        if root.right:
            root.right.inorder()
        return
    def postorder(self):
        '''post'''
        root = self.root
        if root.left:
            root.left.postorder()
        if root.right:
            root.right.postorder()
        if root.data:
            print("-> " + str(root.data), end=" ")
        return
    def traverse(self):
        '''Tra'''
        if self.is_empty():
            return print("This is an empty binary search tree.")
        print('Preorder: ', end='')
        self.preorder()
        print()
        print('Inorder: ', end='')
        self.inorder()
        print()
        print('Postorder: ', end='')
        self.postorder()
        print()
    def find_min(self):
        '''min'''
        root = self.root
        ans = root.data
        if root.left:
            ans = root.left.find_min()
        return ans
    def find_max(self):
        '''max'''
        root = self.root
        ans = root.data
        if root.right:
            ans = root.right.find_max()
        return ans

def main():
    '''Main'''
    my_bst = BST()
    for _ in range(int(input())):
        my_bst.insert(int(input()))
    my_bst.traverse()
    print("Max:", my_bst.find_max())
    print("Min:", my_bst.find_min())
main()
