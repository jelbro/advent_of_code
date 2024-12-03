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


"""
levels = open("input.txt", "r")
safe = 0
# For each line in the file
for level in levels:
    # Split the line into individual numbers
    nums = level.split()
    # Convert the line into numbers
    for i in range(len(nums)):
        nums[i] = int(nums[i])
    print(nums)
    # For each line in the file goingup going down and unsafe are reset
    going_up = False
    going_down = False
    unsafe = False
    prev_num = None

    # For each num in the line
    for num in nums:
        # if the current number is equal to the first index of the list
        if prev_num == None:
            prev_num = num
            # go to the next number as nothing to compare with
            continue
        else:
            # If current number is greater than the previous number e.g. c:5 > p:3
            if num > prev_num:
                # this list is going up
                going_up = True

                # if the current number minus the previous number is greater than 3. e.g. C: 6 - p: 2 = 4
                if (num - prev_num) > 3:
                    # this list is unsafe
                    unsafe = True
            # Else if current number is less than previous number e.g. c:3 < p:6
            elif num < prev_num:
                # the list is going down
                going_down = True
                # if previous number minus the current number p:6 - c:2 = 4
                if (prev_num - num) > 3:
                    # this list is unsafe
                    unsafe = True
            elif num == prev_num:
                unsafe = True
            else:
                pass
        prev_num = num
    if going_down == True and going_up == True:
        print(going_up, going_down, unsafe)
        print("unsafe")
    elif unsafe == True:
        print(going_up, going_down, unsafe)
        print("unsafe")
    else:
        print("safe")
        safe = safe + 1

print(safe)
"""
