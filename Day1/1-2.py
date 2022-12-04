def main():
    current_max = -1
    total_calories = 0
    first = second = third = -1
    with open('1.txt', 'r') as input_file:
        for line in input_file.readlines():
            line_stripped = line.strip()
            if line_stripped:
                total_calories += int(line)
                continue
            if total_calories > first:
                third = second
                second = first
                first = total_calories
            elif total_calories > second:
                third = second
                second = total_calories
            elif total_calories > third:
                third = total_calories

            total_calories = 0

    sum_of_max_three = first + second + third
    print(sum_of_max_three)

if __name__ == "__main__":
    main()