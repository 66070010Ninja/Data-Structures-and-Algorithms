'''Lab 01.06 - Elevator'''
class Elevator:
    '''Lab'''
    def __init__(self, max_floor):
        '''init'''
        self.current_floor = 1
        self.max_floor = max_floor
    def go_to_floor(self, floor):
        '''go to floor'''
        if floor > self.max_floor:
            print('Invalid Floor!')
            return True
        else:
            self.current_floor = floor
            return True
    def report_current_floor(self):
        '''report current floor'''
        print(self.current_floor)
        return False
def main():
    '''main'''
    level_max = Elevator(int(input()))
    num = True
    while num:
        level = input()
        if level == 'Done':
            num = level_max.report_current_floor()
        else:
            level = int(level)
            num = level_max.go_to_floor(level)
main()
