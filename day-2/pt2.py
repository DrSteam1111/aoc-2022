shape_map = {
    'A': 1,
    'B': 2,
    'C': 3
}

to_draw_map = {
    'A': 'A',
    'B': 'B',
    'C': 'C',
}

to_lose_map = {
    'A': 'C',
    'B': 'A',
    'C': 'B'
}

to_win_map = {
    'A': 'B',
    'B': 'C',
    'C': 'A',
}

needed_outcome_map = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win'
}

outcome_map = {
    'win': 6,
    'draw': 3,
    'lose': 0
}


def main():
    input_file = open('input.txt', 'r');
    lines = input_file.readlines();

    total_scores = 0;

    for line in lines:
        stripped = line.strip();
        choices = stripped.split(' ');

        needed_outcome = needed_outcome_map[choices[1]]

        match needed_outcome:
            case 'win':
                total_scores += shape_map[to_win_map[choices[0]]] + outcome_map[needed_outcome];
                continue;

            case 'draw':
                total_scores += shape_map[to_draw_map[choices[0]]] + outcome_map[needed_outcome];
                continue;

            case 'lose':
                total_scores += shape_map[to_lose_map[choices[0]]] + outcome_map[needed_outcome];
                continue;

    print(total_scores);
    

if __name__ == '__main__':
    main()