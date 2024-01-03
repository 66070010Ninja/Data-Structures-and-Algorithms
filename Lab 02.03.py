'''test'''
class ArrayStack:
    '''class'''
    def __init__(self):
        '''init'''
        self.size = 0
        self.data = []
 
    def push(self, input_data):
        '''push'''
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1
 
    def pop(self):
        '''pop'''
        if self.size != 0:
            self.size -= 1
            num = self.data.pop(-1)
            return num
        else:
            print("Underflow: Cannot pop data from an empty list")
            return None
 
    def is_empty(self):
        '''is_empty'''
        if self.size != 0:
            return False
        else:
            return True
 
    def get_stack_top(self):
        '''get_stack_top'''
        if self.data != []:
            return self.data[-1]
        else:
            print("Underflow: Cannot get stack top from an empty list")
            return None
 
    def get_size(self):
        '''get_size'''
        return self.size
 
    def print_stack(self):
        '''print_stack'''
        print(self.data)
 
def main():
    '''main'''
    stack1 = ArrayStack()
    data = [[] for _ in range(int(input()))]
    for _ in range(int(input())):
        stack1.push(input())
 
    num = 0
    while not stack1.is_empty():
        data[num % len(data)].append(stack1.pop())
        num += 1
 
    start = 1
    for i in data:
        print("Group %d: "%start, end='')
        print(*i, sep=", ")
        start += 1
main()
