from itertools import zip_longest

def read_input(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines

def stack_manager(input_lines):
    stripped_lines = [line.rstrip() for line in input_lines]
    middle = stripped_lines.index("")
    stacks = {
        stack[-1]: "".join(filter(None, stack[:-1])).lstrip()
        for stack in zip_longest(*stripped_lines[:middle])
        if stack[-1] and stack[-1].isdigit()
    }
    for line in stripped_lines[middle + 1 :]:
        _, move_amount, _, from_stack, _, to_stack = line.split()
        move_amount = int(move_amount)
        temp = stacks[from_stack]
        stacks[from_stack] = temp[move_amount:]
        stacks[to_stack] = (temp[move_amount - 1 :: -1]) + stacks[to_stack]
    return "".join(stacks[key][0] for key in sorted(stacks))



if __name__ == '__main__':
    input_lines = read_input('input.txt')
    print(stack_manager(input_lines))