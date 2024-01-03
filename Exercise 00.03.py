'''Exercise 00.03'''
def main():
    '''Ex'''
    list_01 = []
    for _ in range(int(input())):
        list_01.append(input())
    for i in range(len(list_01)):
        for j in range(i+1, len(list_01)):
            if list_01[i] >= list_01[j]:
                list_01[i], list_01[j] = list_01[j], list_01[i]
    for i in range(len(list_01)):
        print(list_01[i])
main()
