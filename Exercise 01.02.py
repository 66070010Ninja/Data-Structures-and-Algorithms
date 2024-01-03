'''test'''
class Food:
    '''food'''
    def __init__(self, list_food):
        '''init'''
        self.list_food = list_food
    def random_foods(self):
        '''random'''
        (self.list_food).sort()
    def list_foods(self):
        '''list_foods'''
        print(self.list_food)
def main():
    '''main'''
    num = Food(['Pizza', 'Fried Chicken', 'Hamburger', 'Steak'])
    num.random_foods()
    num.list_foods()
main()
