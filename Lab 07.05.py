'''Lab 07.05'''
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
    def delete(self, data):
        '''delete'''
        root = self.root
        rea = None
        if root.get_data() is None:
            return None
        if root.get_left() and data < root.data:
            rea = root.left.delete(data)
            if rea != None and rea != data and rea.is_empty():
                root.set_left(None)
                rea = data
            elif rea != None and rea != data:
                root.set_left(rea)
                rea = data
            return rea
        if root.get_right() and data > root.data:
            rea = root.right.delete(data)
            if rea != None and rea != data and rea.is_empty():
                root.set_right(None)
                rea = data
            elif rea != data and rea != None:
                root.set_right(rea)
                rea = data
            return rea
        if data == root.data:
            if root.get_left() == None and root.get_right() == None:
                root.set_data(None)
            elif root.get_left() == None:
                self.set_root(root.right.get_root())
            elif root.get_right() == None:
                self.set_root(root.left.get_root())
            else:
                max_num = root.left.find_max()
                self.delete(root.left.find_max())
                root.set_data(max_num)
            return self
        print("Delete Error,", data, "is not found in Binary Search Tree.")
        return None
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
    while 1:
        text = input()
        if text == "Done":
            break
        condition, data = text.split(": ")
        if condition == "I":
            my_bst.insert(int(data))
        elif condition == "D":
            my_bst.delete(int(data))
        else:
            print("Invalid Condition")
    my_bst.traverse()
main()
