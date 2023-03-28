def read_input(filename):
    with open(filename, 'r') as f:
        lines = f.read().strip()
    return lines


def start_of_msg_marker(input, char_amount):
    buffer = []
    for i, char in enumerate(input):
        buffer.append(char)
        if len(buffer) > char_amount:
            buffer.pop(0)
        if len(buffer) == char_amount and len(set(buffer)) == char_amount:
            return i + 1
    return -1


if __name__ == "__main__":
    input_lines = read_input('input.txt')
    print(start_of_msg_marker(input_lines, 14))
