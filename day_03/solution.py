import os
import re


def get_input_data(path: str) -> str:
    abs_path = os.path.join(os.path.dirname(__file__), path)
    with open(abs_path, "r") as file:
        return file.read()


def main() -> None:
    input_data = get_input_data("input.txt")

    # Part 1

    pattern_p1 = re.compile(r"mul\((\d+),(\d+)\)")
    matches_p1 = pattern_p1.findall(input_data)

    total_p1 = sum(int(a) * int(b) for a, b in matches_p1)

    print("Sum of MUL statements:", total_p1)

    # Part 2
    pattern_p2 = re.compile(r"mul\((\d+),(\d+)\)|(don\'t\(\))|(do\(\))")
    matches_p2 = pattern_p2.findall(input_data)

    total_p2, do_mul = 0, True
    for a, b, dont, do in matches_p2:
        if do:
            do_mul = True
        elif dont:
            do_mul = False
        else:
            if do_mul:
                total_p2 += int(a) * int(b)

    print("Sum of MUL statements with DO and DON'T:", total_p2)


if __name__ == "__main__":
    main()
