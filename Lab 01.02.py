'''test'''
def main():
    '''main'''
    import json
    my_list = json.loads(input())
    higth = 0
    low = my_list[0]
    avg = 0
    for i in my_list:
        avg += i
        if i > higth:
            higth = i
        if i < low:
            low = i
    avg = avg/len(my_list)
    text = (higth, low, round(avg, 2))
    print(text)
main()
