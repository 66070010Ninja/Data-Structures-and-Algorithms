'''Lab 05.01'''
class DataNode:
    '''class'''
    def __init__(self, data=None):
        '''__init__'''
        self.__data = data
        self.__next = None
    def get_data(self):
        '''get_data'''
        return self.__data
    def set_data(self, data):
        '''set_data'''
        self.__data = data
    def get_next(self):
        '''get_next'''
        return self.__next
    def set_next(self, next):
        '''set_next'''
        self.__next = next
def main():
    '''main'''
    text = DataNode()
    text.set_data(input())
    print(text.get_data())
    print(text.get_next())
main()
