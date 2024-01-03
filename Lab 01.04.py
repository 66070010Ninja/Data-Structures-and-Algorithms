'''Lab 01.04 - Rectangle'''
class Rectangle:
    '''R'''
    def __init__(self, height, width):
        '''init'''
        self.height = height
        self.width = width
    def calculate_area(self):
        '''ca'''
        num = (self.width*self.height)
        return num
    def calculate_perimeter(self):
        '''cp'''
        num = ((self.width+self.height)*2)
        return num
def main():
    '''a'''
    rectangle = Rectangle(float(input()), float(input()))
    condition = input()
    if condition == "area":
        result = rectangle.calculate_area()
    else:
        result = rectangle.calculate_perimeter()
    print("%.2f" % result)
main()
