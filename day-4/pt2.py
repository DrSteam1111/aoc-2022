def main():
    input_file = open('input.txt', 'r')
    lines = input_file.read()

    intersecting = 0;

    for line in lines.split('\n'):
        elves = line.split(',');
        elve_left_score = elves[0].split('-');
        elve_right_score = elves[1].split('-');

        elf1 = set(range(int(elve_left_score[0]), int(elve_left_score[1])+1))
        elf2 = set(range(int(elve_right_score[0]), int(elve_right_score[1])+1))
        
        if elf1.intersection(elf2):
            intersecting += 1;

    print(intersecting)

if __name__ == '__main__':
    main()