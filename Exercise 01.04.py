'''Exercise 01.04 - Bangna Trad'''
def main():
    '''main'''
    num = float(input())
    if 0 <= num and num <= 5.032:
        print('Bangkok')
    elif 5.032 < num and num <= 35.477:
        print('Samut Prakarn')
    elif 35.477 < num and num <= 52.900:
        print('Chachoengsao')
    elif 52.900 < num and num <= 58.855:
        print('Chon Buri')
    else:
        print('InValid')
main()
