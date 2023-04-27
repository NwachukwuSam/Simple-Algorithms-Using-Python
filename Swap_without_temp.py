def swap_without_temp(first, second):
    first = first + second
    second = first - second

    first = first - second
    return first, second


first = int(input("Enter first Number: "))
second = int(input("Enter second Number: "))
swap = swap_without_temp(first, second)
print(swap)
