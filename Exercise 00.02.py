'''Exercise 00.02'''
def main():
    '''Ex'''
    num_a = input()
    num_b = float(input())
    if num_a == 'Outdoor' and num_b/60 >= 4:
        print(True)
    elif num_a == 'Indoor' and num_b/60 >= 8:
        print(True)
    else:
        print(False)
main()
