database = open('input.txt')


def parse_line(line):
    counts, char, password = line.strip().split()

    counts = counts.split('-')

    return int(counts[0]), int(counts[1]), char[:-1], password


lines = [parse_line(line) for line in database.readlines()]


def part_one(lines):
    valid_passwords = 0

    for minimum, maximum, char, password in lines:
        count = 0

        for c in password:
            if c == char:
                count += 1

        if minimum <= count <= maximum:
            valid_passwords += 1

    return valid_passwords


print(part_one(lines))


def part_two(lines):
    valid_passwords = 0

    for i, j, char, password in lines:
        # This is one way to implement XOR
        if ((password[i-1] == char) != (password[j-1] == char)):
            valid_passwords += 1

    return valid_passwords


print(part_two(lines))
