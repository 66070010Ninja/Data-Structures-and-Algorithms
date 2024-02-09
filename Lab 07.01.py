'''Lab 07.01'''
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

def main():
    '''main'''
    p_new = BSTNode(input())
    print(p_new.get_data())
    print(p_new.get_left())
    print(p_new.get_right())
main()
