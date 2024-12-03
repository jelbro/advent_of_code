def main():
    valid_tests = 0
    TEST_FILE = "input.txt"
    total_tests = 0

    with open(TEST_FILE, "r") as file:
        for line in file:
            total_tests += 1

            numbers = split_into_numbers(line)
            numbers_copy = numbers.copy()

            if line_is_valid(numbers):
                valid_tests += 1
                print(f"{numbers} is valid")
            else:
                removed_number = None
                for i in range(len(numbers)):
                    if removed_number == None:
                        removed_number = numbers[i]
                        numbers_copy.pop(i)
                        if line_is_valid(numbers_copy):
                            valid_tests += 1
                            print(f"{numbers_copy} is valid")
                            break
                        else:
                            numbers_copy.insert(i, removed_number)
                            continue
                    else:
                        removed_number = numbers[i]
                        numbers_copy.pop(i)
                        if line_is_valid(numbers_copy):
                            valid_tests += 1
                            print(f"{numbers_copy} is valid")
                            break
                        else:
                            numbers_copy.insert(i, removed_number)
                            continue

    print(f"total_tests: {total_tests} valid_tests: {valid_tests} total: {valid_tests}")


def split_into_numbers(l):
    numbers = l.split()
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])

    return numbers


def line_is_valid(line):
    prev_num = None
    valid = True
    asc = False
    desc = False

    for num in line:
        if prev_num == None:
            prev_num = num
            continue

        else:
            difference = num - prev_num

            if (abs(difference) < 1) or (abs(difference) > 3):
                valid = False

            if num > prev_num:
                asc = True

            elif num < prev_num:
                desc = True

            prev_num = num

    if asc and desc:
        valid = False

    return valid


if __name__ == "__main__":
    main()
