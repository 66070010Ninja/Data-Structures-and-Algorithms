'''Lab 01.05 - Point'''
class Point:
    '''Point'''
    def __init__(self, num_x=0, num_y=0):
        '''init'''
        self.set_coordinates(num_x, num_y)
 
    def set_coordinates(self, num_x, num_y):
        '''sc'''
        self.num_x = num_x
        self.num_y = num_y
 
    def get_coordinates(self):
        '''ge'''
        num = (self.num_x, self.num_y)
        return num
 
    def calculate_distance(self, other_point):
        '''cd'''
        num = ((other_point.num_x - self.num_x)**2 + (other_point.num_y - self.num_y)**2) ** 0.5
        return num
 
def main():
    '''main'''
    point01 = Point(float(input()), float(input()))
    point02 = Point(float(input()), float(input()))
    point01.get_coordinates()
    point02.get_coordinates()
    print("%0.2f"%(Point.calculate_distance(point01, point02)))
main()
