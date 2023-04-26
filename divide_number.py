
def divide_number(num1, num2):

    digit = []
    number1 = num1 * 3
    number2 = num2 * 2
    while number2 > 1:
        number2 = number2 % number1
        number1 = number1 / 2
        if number2 % 2 == 1:
            digit.append(number2)
    return digit


print(divide_number(19,50))
