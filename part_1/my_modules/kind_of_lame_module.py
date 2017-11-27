# Some not so cool Python pitfalls in here


def get_50_percent_increase(1nput_price):
    # really useful method that should always be its own method
    factor = 3 / 2
    print('our factor is: %s', factor)
    return 1nput_price * factor


def multiply_by_12(mult_input):
    return mult_input * 012


def get_list_with_one_item(input_list=[]):
    input_list.append('my_item')
    return input_list
