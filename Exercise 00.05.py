'''Exercise 00.05'''
class Person:
    '''Person'''
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

class Project:
    '''Project'''
    def __init__(self, name, count):
        '''Ex'''
        self.projectname = name
        self.nummember = count
    def showprojectname(self):
        '''Ex'''
        print('Hello There! This is', self.projectname)
    def showmembers(self):
        '''Ex'''
        print('This project has', self.nummember, 'members')

def main_02(num):
    '''Ex'''
    list_01 = []
    for _ in range(num):
        list_01.append(input())
        input()
    for i in range(len(list_01)):
        for j in range(i+1, len(list_01)):
            if list_01[i] >= list_01[j]:
                list_01[i], list_01[j] = list_01[j], list_01[i]
    for i in range(len(list_01)):
        person = Person(list_01[i], 0)
        person.say_hello()

def main():
    '''Ex'''
    name_project = input()
    count_project = int(input())
    project = Project(name_project, count_project)
    project.showprojectname()
    project.showmembers()
    main_02(count_project)
main()
