def read_input(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines


if __name__ == '__main__':
    input_lines = read_input('input.txt')
    total_sum = 0
    for line in input_lines:
        split_line = line.split(",")
        from1, to1 = map(int, split_line[0].split("-"))
        from2, to2 = map(int, split_line[1].split("-"))
        if (to2 >= from1) and (from2 <= to1):
            total_sum += 1
    print(total_sum)