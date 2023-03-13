def read_input(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines


if __name__ == '__main__':
    input_lines = read_input('input.txt')
    sum_cal = 0
    sum_list = []
    for line in input_lines:
        if line.strip():
            sum_cal += int(line)
        else:
            sum_list.append(sum_cal)
            sum_cal = 0
    sum_list.sort(reverse=True)
    print(sum_list[0] + sum_list[1] + sum_list[2])
