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
    names = ["Walter", "Skyler", "Jesse", "Saul", "Mike", \
              "Hank", "Marie", "Kim", "Gustavo", "Salamanca"]
 
    def print_status():
        """Print all stacks"""
        print("This is stack 1 (%d): " % stack01.get_size(), end='')
        stack01.print_stack()
        print("This is stack 2 (%d): " % stack02.get_size(), end='')
        stack02.print_stack()
        print("This is stack 3 (%d): " % stack03.get_size(), end='')
        stack03.print_stack()
        print()
 
    stack01 = ArrayStack()
    stack02 = ArrayStack()
    stack03 = ArrayStack()
    for _ in range(len(names) // 2):
        stack01.push(names.pop())
        stack02.push(names.pop())
    print_status()
 
    while not stack01.is_empty() and not stack02.is_empty():
        stack03.push(stack01.get_stack_top())
        stack03.push(stack02.pop())
    print_status()
 
    for _ in range(stack03.get_size() + 1):
        stack03.pop()
    print_status()
 
    while not stack01.is_empty():
        temp = stack01.pop()
        stack02.push(temp)
        stack03.push(temp)
    print_status()
 
    while not stack02.is_empty():
        temp = stack02.pop()
        print(temp)
    print()
    print_status()
 
    while not stack03.is_empty():
        stack02.push(stack03.pop())
    print_status()
main()
