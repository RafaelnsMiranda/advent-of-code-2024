import sys


def convert_input_2_lists(file):
    list_1 = []
    list_2 = []

    with open(file) as f:
        for line in f:
            item1, item2 = map(int, line.split())
            list_1.append(item1)
            list_2.append(item2)
    return list_1, list_2


def find_total_distance(list1, list2):
    list1.sort()
    list2.sort()

    return sum([abs(list1[i] - list2[i]) for i in range(len(list1))])


def calculate_similarity_score(list1, list2):

    intersection_list = [value for value in list1 if value in list2]

    return sum(
        [
            (list1[i] * list2.count(list1[i]))
            for i in range(len(list1))
            if list1[i] in intersection_list
        ]
    )


if __name__ == "__main__":
    # input file needs to be passed as the first argument
    input_file = sys.argv[1]

    list1, list2 = convert_input_2_lists(input_file)

    total_distance = find_total_distance(list1, list2)
    print(f"total distance: {total_distance}")

    similarity_score = calculate_similarity_score(list1, list2)
    print(f"Similarity score: {similarity_score}")
