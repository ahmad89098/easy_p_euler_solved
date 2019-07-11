# ProjectEuler
# Problem 2: Even Fibonacci numbers
# by ahmad89098

fib_numbers = [1, 2]
numbers_less_than_four_million = []
even_numbers = []

# Use fib_numbers to store all the fibonacci numbers
# Use numbers_less_than_four_million to store the numbers less than 4 million
# Use even_numbers to store all the even numbers
# In the end, we basically add all these numbers together


first_number = 1
second_number = 2

total = 0

# Execute the fibonacci sequence and then add to total independently

while first_number < 4000000:
    first_number = first_number + second_number
    fib_numbers.append(first_number)
    second_number = first_number + second_number
    fib_numbers.append(second_number)

for number in fib_numbers:
    if number < 4000000:
        numbers_less_than_four_million.append(number)

for number in numbers_less_than_four_million:
    if number % 2 == 0:
        even_numbers.append(number)

for number in even_numbers:
    total = total + number

print(total)