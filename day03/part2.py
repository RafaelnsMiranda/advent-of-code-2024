import sys


PREFIX = "mul("
SUFIX = ")"
SEPARATOR = ","

DO = "do()"
DONT = "don't()"


def read_input(file):
    with open(file, "r") as file:
        file_content = file.read()
    return file_content


def parse_dos(input):

    dos = {n: DO for n in range(len(input)) if input.find(DO, n) == n}
    donts = {n: DONT for n in range(len(input)) if input.find(DONT, n) == n}
    merged_dict = {**dos, **donts}
    print(merged_dict)
    sorted_keys = sorted(list(merged_dict.keys()))
    new_input = ""
    current_do = 0
    previous = DO
    for i in sorted_keys:
        if merged_dict[i] == DO:
            if previous == DO:
                new_input += input[current_do:i]
            current_do = i
            previous = DO
        else:
            if previous == DO:
                new_input += input[current_do:i]
            previous = DONT
    return new_input


def calculate_multiplication(input):

    indexes = [n for n in range(len(input)) if input.find(PREFIX, n) == n]

    sum = 0
    for i in indexes:
        mult_string = input[i + len(PREFIX) :]
        mult_content = mult_string.split(SUFIX)[0]
        if SEPARATOR in mult_content:
            numbers = mult_content.split(SEPARATOR)
            if len(numbers) == 2 and numbers[0].isdigit() and numbers[1].isdigit():
                sum += int(numbers[0]) * int(numbers[1])
    return sum


if __name__ == "__main__":
    # input file needs to be passed as the first argument
    input_file = sys.argv[1]

    input = read_input(input_file)
    print(f"Sum of the multiplication: {calculate_multiplication(input)}")
