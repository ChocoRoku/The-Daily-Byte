# Given two binary strings (strings containing only 1s and 0s)
# return their sum (also as a binary string).
# 
# Note: neither binary string will contain leading 0s unless the string itself is 0

def add_binary(num1, num2):
    # get decimal numbers
    deci_1 = get_decimal(num1)
    deci_2 = get_decimal(num2)

    sum = deci_1 + deci_2

    # return the binary number of the sum
    return get_binary(sum)

def get_decimal(num):
    decimal = 0
    num = num[::-1]
    for i in range(len(num)-1, -1, -1):
        if(num[i] == '1'):
            decimal += 2**(i)

    return decimal

def get_binary(num):
    binary = ''
    binary_lst = []
    i = 1
    while((num/i)>=1):
        binary_lst.append(i)
        i *= 2
    while(binary_lst):
        if(num-binary_lst[-1] >=0):
            binary += '1'
            num -= binary_lst[-1]
            num-binary_lst[-1]
        else:
            binary += '0'

        binary_lst.pop(-1)

    return binary


if __name__ == "__main__":

    print(add_binary('10101010', '11001100'))
    print(get_binary(374))
    print(get_decimal('101110110')) # is 374