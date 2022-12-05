shape_map = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

draw_map = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C'
}

lose_map = {
    'X': 'B',
    'Y': 'C',
    'Z': 'A'
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
        point_acc = 0;

        stripped = line.strip();
        choices = stripped.split(' ');

        is_draw = draw_map[choices[1]] == choices[0]
        if (is_draw):
            point_acc = outcome_map['draw'] + shape_map[choices[1]]
            total_scores += point_acc;
            continue;

        is_lose = lose_map[choices[1]] == choices[0]
        if  (is_lose):
            point_acc = outcome_map['lose'] + shape_map[choices[1]]
            total_scores += point_acc;
            continue;

        point_acc = outcome_map['win'] + shape_map[choices[1]];
        total_scores += point_acc;

    print(total_scores);
    

if __name__ == '__main__':
    main()