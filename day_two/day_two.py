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
