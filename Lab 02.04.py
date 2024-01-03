'''test'''
class ArrayStack:
    '''class'''
    def __init__(self):
        '''init'''
        self.size = 0
        self.item = []
 
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
            self.item.append(input_data)
            self.size += 1
 
    def pop(self):
        '''pop'''
        if self.size != 0:
            self.size -= 1
            num = self.item.pop(-1)
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
        if self.item != []:
            return self.item[-1]
        else:
            print("Underflow: Cannot get stack top from an empty list")
            return None
 
    def get_size(self):
        '''get_size'''
        return self.size
 
    def print_stack(self):
        '''print_stack'''
        print(self.item)
 
def copy_stack(stack1, stack2):
    '''copy_stack'''
    stack2.item = list(stack1.item)
    stack2.size = stack1.size
 
def main():
    '''main'''
    def print_status():
        """Print all stacks"""
        print("This is stack 1 (%d): " % stack1.get_size(), end='')
        stack1.print_stack()
        print("This is stack 2 (%d): " % stack2.get_size(), end='')
        stack2.print_stack()
        print("This is stack 3 (%d): " % stack3.get_size(), end='')
        stack3.print_stack()
        print("This is stack 4 (%d): " % stack4.get_size(), end='')
        stack4.print_stack()
        print()
 
 
    stack1 = ArrayStack()
    stack2 = ArrayStack()
    stack3 = ArrayStack()
    stack4 = ArrayStack()
 
    # เพิ่มข้อมูลใน Stack1
    for _ in range(int(input())):
        stack1.push(input())
 
    # เพิ่มข้อมูลใน Stack2
    for _ in range(int(input())):
        stack2.push(input())
 
    temp1, temp2, temp3, temp4 = id(stack1), id(
        stack2), id(stack3), id(stack4)
 
    print("Copy Stack 2 to Stack 4")
    copy_stack(stack2, stack4)
    print_status()
 
    print("Copy Stack 1 to Stack 3")
    copy_stack(stack1, stack3)
    stack1.push("A")
    print_status()
 
    print("Copy Stack 2 to Stack 1")
    copy_stack(stack2, stack1)
    stack2.push("B")
    print_status()
 
    print("Copy Stack 3 to Stack 2")
    copy_stack(stack3, stack2)
    stack3.push("C")
    print("Copy Stack 1 to Stack 3")
    copy_stack(stack1, stack3)
    stack1.push("D")
    print("Copy Stack 2 to Stack 4")
    copy_stack(stack2, stack4)
    stack2.push("E")
    print_status()
 
    print(temp1 == id(stack1), temp2 == id(stack2),\
    temp3 == id(stack3), temp4 == id(stack4))
 
main()
