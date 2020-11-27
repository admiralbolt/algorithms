min = 1
max = 9
power = 1

powerful_numbers = []

def digit_count(n):
    return len(str(n))

while min <= max:
    for i in range(min, max + 1):
        if digit_count(i ** power) == power:
            powerful_numbers.append((i, power))
        elif digit_count(i ** power) < power:
            min += 1

    power += 1

print(powerful_numbers)
print(len(powerful_numbers))
