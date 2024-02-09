'''Lab 10'''
class Student():
    '''class'''
    def __init__(self, std_id, name, gpa):
        '''init'''
        self.__std_id = std_id
        self.__name = name
        self.__gpa = gpa
    def get_std_id(self):
        '''get_std_id'''
        return self.__std_id
    def get_name(self):
        '''get_name'''
        return self.__name
    def get_gpa(self):
        '''get_gpa'''
        return self.__gpa
    def print_detail(self):
        '''print_detail'''
        print("ID:", self.get_std_id())
        print("Name:", self.get_name())
        print("GPA: %0.2f" % self.get_gpa())

class ProbHash():
    '''class'''
    def __init__(self, size):
        '''init'''
        self.__hash_table = [None]*size
        self.__size = size
    def hash(self, key):
        '''hash'''
        return key % self.__size
    def rehash(self, key):
        '''rehash'''
        # เริ่มนับตั้งแต่จุดที่ทำการ hash
        for i in range(self.hash(key), len(self.__hash_table)):
            if self.__hash_table[i] == None:
                return i

        # เริ่มนับตั้งแต่ต้นไปถึงจุดที่ทำการ hash
        for i in range(self.hash(key)):
            if self.__hash_table[i] == None:
                return i
    def insert_data(self, std):
        '''insert_data'''
        # เช็คว่าข้อมูลเต็มยัง
        if None not in self.__hash_table:
            print('The list is full.', std.get_std_id(), 'could not be inserted.')
            return

        # ทำการเข้า hash function เพื่อหา index
        index_one = self.hash(std.get_std_id())

        # เช็คว่าใน index นั้นมีข้อมูลหรือยัง
        if self.__hash_table[index_one] == None:
            self.__hash_table[index_one] = std
            print('Insert', std.get_std_id(), 'at index', index_one)
            return

        # ทำการเข้า linear probing เพื่อหาช่อง index ที่ข้แมูลยังว่า
        index_two = self.rehash(std.get_std_id())
        self.__hash_table[index_two] = std
        print('Insert', std.get_std_id(), 'at index', index_two)
        return
    def search_data(self, std_id):
        '''search_data'''
        # เก็บจำนวนที่ข้อมูลแสดงได้
        num = 0

        # นับตั้งแต่เริ่มไปจนจบของมูลของ hash_table
        for i in range(len(self.__hash_table)):
            if self.__hash_table[i] == None:
                continue
            if self.__hash_table[i].get_std_id() == std_id:
                print('Found', std_id, 'at index', i)
                self.__hash_table[i].print_detail()
                num += 1

        # แสดงเมื่อไม่มีข้อมูลออกมาเลย
        if num == 0:
            print(std_id, 'does not exist.')

def main():
    '''main'''
    import json
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
        if condition == "I":
            std_in = json.loads(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hashtable.insert_data(std)
        elif condition == "S":
            print("------")
            student = hashtable.search_data(int(data))
            if student is not None:
                student.print_detail()
            print("------")
        else:
            print("Invalid Condition!")
main()
