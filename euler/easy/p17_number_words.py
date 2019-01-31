digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

# Think of sub division like this:
#  Let l_d = 1-9
#  Let l_t = 11-19
# Then, for each tens place (twenty-x, thirty-x)
# We can calculate the sum as len(twenty) * 10 + l_d
# We can find the total sum for all numbers under one hundred, and then
# the hundered place can be found similarly:
# len(onehundredand) * 100 + l_h
# The total sum for the hundreds being: l_h + len(100) * 100 + l_h + len(200) + l_h ... + len(900) + l_h
# OR 10 * l_h + len(100) + len(200) + ... + len(900) + len(1000)

length_digits = sum([len(d) for d in digits])
length_teens = sum([len(d) for d in teens])
length_tens = 0
for tens_place in tens:
  length_tens += length_digits + 10 * len(tens_place)


l_h = length_digits + len("ten") + length_teens + length_tens

l_final = 10 * l_h + sum([len(d + "hundredand") for d in digits]) * 100 + len("onethousand") - len("and") * 9

print(l_final)
