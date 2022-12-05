def main():
    input_file = open("input.txt", "r")
    lines = input_file.readlines()

    higest_calories = 0;
    current_value = 0;

    for line in lines:
        if (line.isspace()):
            if (higest_calories < current_value):
                higest_calories = current_value;
            current_value = 0;
            continue;
        current_value += int(line)

    print(higest_calories)

if __name__ == '__main__':
    main()