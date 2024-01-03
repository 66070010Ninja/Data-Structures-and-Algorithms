'''test'''
class ArrayStack:
    '''class'''
    def __init__(self):
        '''init'''
        self.size = 0
        self.data = []
        self.flsh = False
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
            num = self.data.pop(0)
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
    def is_parentheses_matching(self, text):
        '''a'''
        op_list = ["[", "{", "("]
        close_list = ["]", "}", ")"]
        stack = []
        start = True
        for i in text:
            if i in op_list:
                stack.append(i)
            elif i in close_list:
                pos = close_list.index(i)
                if (len(stack) > 0) and (op_list[pos] == stack[len(stack)-1]):
                    stack.pop()
                else:
                    print("Underflow: Cannot pop data from an empty list")
                    start = False
        if len(stack) == 0 and start == True:
            print("Parentheses in " + text + " are matched")
            print(True)
        else:
            print("Parentheses in " + text + " are unmatched")
            print(self.flsh)
 
def main():
    '''main'''
    data = ArrayStack()
    data.is_parentheses_matching(input())
main()
