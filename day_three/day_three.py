import re


def main():
    INPUT_FILE = "input.txt"
    pattern = r"mul\((\d+),(\d+)\)"
    correct_patterns = 0

    with open(INPUT_FILE, "r") as file:
        match = re.search(pattern, file)
        if match:
            correct_patterns += match.group(1) * match.group(2)
        else:
            pass

    print(correct_patterns)


if __name__ == "__main__":
    main()
