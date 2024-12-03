import sys


PREFIX = "mul("
SUFIX = ")"
SEPARATOR = ","


def read_input(file):
    with open(file, "r") as file:
        file_content = file.read()
    return file_content


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
