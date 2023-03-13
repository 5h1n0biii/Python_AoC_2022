def read_input(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines


if __name__ == '__main__':
    input_lines = read_input('input.txt')
    max_cal = 0
    sum_cal = 0
    for line in input_lines:
        if line.strip():
            sum_cal += int(line)
        else:
            if max_cal <= sum_cal:
                max_cal = sum_cal
            sum_cal = 0
    print(max_cal)


