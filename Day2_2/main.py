def read_input(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines

if __name__ == '__main__':
    input_lines = read_input('input.txt')
    sum = 0
    for line in input_lines:
        p1_turn, p2_turn = line.split()
        if p1_turn == 'A' and p2_turn == 'X':
            sum += 3 + 0
        if p1_turn == 'A' and p2_turn == 'Y':
            sum += 1 + 3
        if p1_turn == 'A' and p2_turn == 'Z':
            sum += 2 + 6
        if p1_turn == 'B' and p2_turn == 'X':
            sum += 1 + 0
        if p1_turn == 'B' and p2_turn == 'Y':
            sum += 2 + 3
        if p1_turn == 'B' and p2_turn == 'Z':
            sum += 3 + 6
        if p1_turn == 'C' and p2_turn == 'X':
            sum += 2 + 0
        if p1_turn == 'C' and p2_turn == 'Y':
            sum += 3 + 3
        if p1_turn == 'C' and p2_turn == 'Z':
            sum += 1 + 6
    print(sum)