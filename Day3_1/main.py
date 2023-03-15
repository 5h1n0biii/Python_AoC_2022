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


if __name__ == '__main__':
    input_lines = read_input('input.txt')
    total_sum = 0
    for line in input_lines:
        found = False
        for i in range(0, int(len(line)/2)):
            for j in range(int(len(line)/2), len(line)):
                if line[i] == line[j]:
                    total_sum += get_alphabet_val(line[i])
                    found = True
                    break
            if found:
                break
    print(total_sum)