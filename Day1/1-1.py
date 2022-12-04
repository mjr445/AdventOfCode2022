def main():
    current_max = -1
    total_calories = 0
    with open('1-1.txt', 'r') as input_file:
        for line in input_file.readlines():
            line_stripped = line.strip()
            if line_stripped:
                total_calories += int(line)
                continue

            if total_calories > current_max:
                current_max = total_calories
            total_calories = 0
    print(current_max)

if __name__ == "__main__":
    main()