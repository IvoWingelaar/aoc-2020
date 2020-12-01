expenses = open('input.txt')

values = set()

for i in expenses.readlines():
    value = int(i[:-1])
    values.add(value)


def find_pair_that_sums_to(values, expected_sum):
    for i in values:
        if (expected_sum - i) in values:
            return i, expected_sum - i


# Part one
a, b = find_pair_that_sums_to(values, 2020)
print(a * b)

# Part two
for i in values:
    res = find_pair_that_sums_to(values, 2020 - i)

    if res is not None:
        a, b = res
        print(a * b * i)
        break
