'''Lab 07.02'''
class BSTNode:
    '''class'''
    def __init__(self, data):
        '''__init__'''
        self.data = int(data)
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
    def __init__(self):
        '''__init__'''
        self.root = BSTNode()
    def get_root(self):
        '''get_root'''
        return self.root
    def set_root(self, root):
        '''set_root'''
        self.root = root

def main():
    """Data Structures and Algorithms Lab – Binary Search Tree"""
    my_bst = BST()
    for i in range(int(input())):
        my_bst.insert(int(input()))

    print("Preorder: ", end="")
    my_bst.preorder()
main()
