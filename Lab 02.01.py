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
    text = ArrayStack()
 
    text.push("100")
    text.push(100)
    text.push("3.14")
    text.push(3.14)
    text.push("66.4a")
    text.push("Ackerman")
 
    text.print_stack()
 
    print(text.get_size())
    num02 = text.pop()
    print(num02)
    text.print_stack()
    print(text.get_size())
 
    while not text.is_empty():
        print(text.pop())
 
    print()
    print(text.pop())
    print(text.get_stack_top())
    print(num02)
 
main()
