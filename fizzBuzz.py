
def fizz_buzz(_self, number):
    while number <= 100:
        if number % 3 == 0 & number % 5 == 0:
            print("FIZZBUZZ")
        elif number % 3 == 0:
            print("FIZZ")
        elif number % 5 == 0:
            print("BUZZ")
        else:
            print(number)
        number += 1

fizz_buzz(number = int(input("Enter a number: ")))