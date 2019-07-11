# ProjectEuler
# Problem 1: Multiples of 3 and 5
# by ahmad89098

total = 0

for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        total = total + i

print(total) 