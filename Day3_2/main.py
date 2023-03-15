def read_input(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines

def get_alphabet_val(letter):
    alphabet = {}
    for k in range(26):
        alphabet[chr(ord('a') + k)] = k + 1
        alphabet[chr(ord('A') + k)] = k + 27
    return alphabet[letter]

def comp_lines(line1, line2, line3):
    for letter in line1:
        if letter in line2 and letter in line3:
            return letter
    return None


if __name__ == '__main__':
    input_lines = read_input('input.txt')
    total_sum = 0
    for i in range(0, len(input_lines), 3):
        letter = comp_lines(input_lines[i], input_lines[i + 1], input_lines[i + 2])
        total_sum += get_alphabet_val(letter)
    print(total_sum)