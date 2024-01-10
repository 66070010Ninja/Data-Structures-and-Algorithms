'''Lab 05.02'''
class DataNode:
    '''class'''
    def __init__(self, data=None):
        '''__init__'''
        self.data = data
        self.next = None
    def get_data(self):
        '''get_data'''
        return self.data
    def set_data(self, data):
        '''set_data'''
        self.data = data
    def get_next(self):
        '''get_next'''
        return self.next
    def set_next(self, data):
        '''set_next'''
        self.next = data

class SinglyLinkedList:
    '''class'''
    def __init__(self):
        '''__init__'''
        self.count = 0
        self.head = None
    def insert_last(self, data):
        '''insert_last'''
        new = DataNode(data)
        self.count += 1
        if self.head is None:
            self.head = new
        else:
            move = self.head
            while move.next:
                move = move.next
            move.next = new
    def traverse(self):
        '''traverse'''
        printval = self.head
        if printval == None:
            print("This is an empty list.")
        while printval is not None:
            print(printval.data, end="")
            printval = printval.next
            if printval is not None:
                print(" -> ", end="")

def main():
    '''main'''
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        mylist.insert_last(input())
    mylist.traverse()
main()
