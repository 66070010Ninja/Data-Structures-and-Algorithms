'''Lab 05.05'''
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

    def insert_front(self, data):
        '''insert_front'''
        new = DataNode(data)
        self.count += 1
        if self.head is None:
            self.head = new
        else:
            new.next = self.head
        self.head = new

    def insert_before(self, node, data):
        '''insert_before'''
        new = DataNode(data)
        val = self.head
        if val == None:
            print('Cannot insert, ' + node + ' does not exist.')
            return
        if val.data == node:
            self.insert_front(data)
            self.count += 1
            return
        while val.next is not None:
            tmps = val.next
            if tmps.data == node:
                new.next = tmps
                val.next = new
                self.count += 1
                return
            val = val.next
        print('Cannot insert, ' + node + ' does not exist.')

    def delete(self, data):
        '''delete'''
        val = self.head
        con = False
        if val == None:
            print("Cannot delete, " + data + " does not exist.")
            return
        if val.data == data:
            self.head = val.next
            val = None
            self.count -= 1
            return
        while val is not None:
            if val.data == data:
                con = True
                self.count -= 1
                break
            prev = val
            val = val.next
        if con == False:
            print("Cannot delete, " + data + " does not exist.")
        if val == None:
            return
        prev.next = val.next
        val = None

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
        text = input()
        condition, data = text.split(": ")
        if condition == "F":
            mylist.insert_front(data)
        elif condition == "L":
            mylist.insert_last(data)
        elif condition == "B":
            mylist.insert_before(*data.split(", "))
        elif condition == "D":
            mylist.delete(data)
        else:
            print("Invalid Condition!")
    mylist.traverse()
main()
