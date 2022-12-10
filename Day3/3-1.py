from sys import argv

ASCII_BARRIER = ord('a')
LOWERCASE_FACTOR = ASCII_BARRIER - 1
UPPERCASE_FACTOR = ord('A') - 27

def main():
    total_priority_sum = 0
    with open(argv[1], 'r', encoding='utf8') as input_file:
        for line in input_file.readlines():

            rucksack = line.strip()
            item_length = len(rucksack) // 2
            item1 = set(rucksack[0:item_length])
            item2 = set(rucksack[item_length:])

            shared_letter = item1.intersection(item2).pop()
            ascii_value = ord(shared_letter)
            if ascii_value >= ASCII_BARRIER:
                priority_value = ascii_value - LOWERCASE_FACTOR
            else:
                priority_value = ascii_value - UPPERCASE_FACTOR
            total_priority_sum += priority_value
    print(total_priority_sum)

if __name__ == "__main__":
    main()
