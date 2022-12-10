from sys import argv

ASCII_BARRIER = ord('a')
LOWERCASE_FACTOR = ASCII_BARRIER - 1
UPPERCASE_FACTOR = ord('A') - 27

def main():
    total_priority_sum = 0
    with open(argv[1], 'r', encoding='utf8') as input_file:
        line_num = 0
        shared_letters = set()
        for line in input_file:
            line_num += 1

            rucksack = line.strip()
            rucksack_set = set(rucksack)
            if line_num % 3 == 0:
                print(rucksack_set.intersection(shared_letters))
                shared_letter = rucksack_set.intersection(shared_letters).pop()
                ascii_value = ord(shared_letter)
                if ascii_value >= ASCII_BARRIER:
                    priority_value = ascii_value - LOWERCASE_FACTOR
                else:
                    priority_value = ascii_value - UPPERCASE_FACTOR
                total_priority_sum += priority_value
            elif line_num % 3 == 1:
                shared_letters = rucksack_set
            elif line_num % 3 == 2:
                shared_letters = rucksack_set.intersection(shared_letters)

    print(total_priority_sum)

if __name__ == "__main__":
    main()
