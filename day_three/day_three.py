import re


def main():
    INPUT_FILE = "input.txt"
    pattern = r"mul\((\d+),(\d+)\)"
    correct_patterns = 0

    with open(INPUT_FILE, "r") as file:
        string = file.read().replace("\n", "")
        match = re.findall(pattern, string)
        for group in match:
            correct_patterns += int(group[0]) * int(group[1])

    print(correct_patterns)


if __name__ == "__main__":
    main()
