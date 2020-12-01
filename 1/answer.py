from collections import Counter

expenses = open('input.txt')

values = Counter()
needle = 2020

for i in expenses.readlines():
    # strip newline
    value = int(i[:-1])
    values.update([value])


def find_pair_that_sums_to(values, expected_sum):
    for i in values:
        if (expected_sum - i) in values:
            if not is_false_positive(values, [i, expected_sum - i]):
                return i, expected_sum - i


def is_false_positive(values, possible_answer):
    c = Counter(possible_answer)
    for k, v in c.items():
        if values[k] < v:
            return True

    return False


# Part one
a, b = find_pair_that_sums_to(values, needle)
print(a * b)

# Part two
for i in values:
    res = find_pair_that_sums_to(values, needle - i)

    if res is not None:
        a, b = res

        if not is_false_positive(values, [a, b, i]):
            print(a * b * i)
            break
