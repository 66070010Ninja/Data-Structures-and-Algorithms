'''Lab 01.03 - SwapVar'''
def convert_string_to_tuples(text_in):
    '''a'''
    values = text_in.strip('()').split(', ')
    return tuple(map(float, values))
def main():
    '''a'''
    num_a = convert_string_to_tuples(input())
    num_b = (float(num_a[1]), float(num_a[0]))
    print(num_b)
main()
