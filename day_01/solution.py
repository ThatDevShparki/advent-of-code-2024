import os
from collections import Counter


def get_input_data(path: str) -> list[tuple[int, int]]:
    abs_path = os.path.join(os.path.dirname(__file__), path)
    with open(abs_path, "r") as file:
        input_data: list[tuple[int, int]] = []
        for line in file:
            a, b = map(int, line.strip().split())
            input_data.append((a, b))
        return input_data


def main() -> None:
    input_data = get_input_data("input.txt")
    list_a, list_b = zip(*input_data)
    list_a_sorted = sorted(list_a)
    list_b_sorted = sorted(list_b)

    # Part 1
    min_distances = map(lambda x, y: abs(x - y), list_a_sorted, list_b_sorted)
    sum_min_distances = sum(min_distances)
    print("Sum of minimum distances:", sum_min_distances)

    # Part 2
    counter_a = Counter(list_a_sorted)
    counter_b = Counter(list_b_sorted)
    common_values = set((counter_a & counter_b).keys())

    similarity_score = 0
    for value in common_values:
        similarity_score += counter_a[value] * counter_b[value] * value

    print("Similarity score:", similarity_score)


if __name__ == "__main__":
    main()
