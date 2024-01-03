'''Exercise 00.04'''
class Person:
    '''class'''
    def __init__(self, name, age):
        '''Ex'''
        self.name = name
        self.age = age
    def get_details(self):
        '''Ex'''
        print(self.name, ', ', self.age, ' years old', sep='')
    def say_hello(self):
        '''Ex'''
        print('Hello, my name is ', self.name, '!', sep='')
def main():
    '''Ex'''
    person = Person(input(), int(input()))
    person.get_details()
    person.say_hello()
main()
