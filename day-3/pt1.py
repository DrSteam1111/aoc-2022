priority_map = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
    'A': 27,
    'B': 28,
    'C': 29,
    'D': 30,
    'E': 31,
    'F': 32,
    'G': 33,
    'H': 34,
    'I': 35,
    'J': 36,
    'K': 37,
    'L': 38,
    'M': 39,
    'N': 40,
    'O': 41,
    'P': 42,
    'Q': 43,
    'R': 44,
    'S': 45,
    'T': 46,
    'U': 47,
    'V': 48,
    'W': 49,
    'X': 50,
    'Y': 51,
    'Z': 52,
}

def main():
    input_file = open('input.txt', 'r')
    lines = input_file.readlines()

    total_priority = 0;

    for line in lines:
        stripped = line.strip();
        line_length = len(stripped);
        first_slice = slice(0, line_length//2)
        secound_slice = slice(line_length//2, line_length)

        first_compartment = stripped[first_slice]
        secound_compartment = stripped[secound_slice]

        duplicates = [];

        for first_compartment_item in first_compartment:
            for secound_compartment_item in secound_compartment:
                if first_compartment_item == secound_compartment_item and not first_compartment_item in duplicates:
                    total_priority += priority_map[first_compartment_item]
                    duplicates.append(first_compartment_item);

    print(total_priority)



if __name__ == '__main__':
    main()