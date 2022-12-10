from sys import argv

def main():
    fully_contained_pairs = 0
    with open(argv[1], 'r', encoding='utf8') as input_file:
        for line in input_file.readlines():
            range1, range2 = line.strip().split(',')

            lower_limit1, upper_limit1 = range1.split('-')
            lower_limit1, upper_limit1 = int(lower_limit1), int(upper_limit1)

            lower_limit2, upper_limit2 = range2.split('-')
            lower_limit2, upper_limit2 = int(lower_limit2), int(upper_limit2)
            
            if lower_limit2 <= lower_limit1 <= upper_limit1 <= upper_limit2 or \
                lower_limit1 <= lower_limit2 <= upper_limit2 <= upper_limit1:
                fully_contained_pairs += 1
    print(fully_contained_pairs)

if __name__ == "__main__":
    main()
