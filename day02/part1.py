import sys


def convert_input_2_lists(file):

    levels = []
    with open(file) as f:
        for line in f:
            level = list(map(int, line.split()))
            levels.append(level)
        return levels


def is_level_safe(level):
    def condition(i, j, increasing):
        return (i > j if increasing else i < j) and (
            abs(i - j) >= 1 and abs(i - j) <= 3
        )

    # Check for increasing or decreasing condition
    return all(
        condition(i, j, increasing=True) for i, j in zip(level, level[1:])
    ) or all(condition(i, j, increasing=False) for i, j in zip(level, level[1:]))


def count_safe_levels(levels):
    return [is_level_safe(level) for level in levels].count(True)


if __name__ == "__main__":
    # input file needs to be passed as the first argument
    input_file = sys.argv[1]

    levels = convert_input_2_lists(input_file)
    print(f"Amount of safe levels: {count_safe_levels(levels)}")