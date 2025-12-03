def star1():
    with open("input.txt", "r") as file:
        data = file.readlines()
    instructions = data
    x = 50
    zero_count = 0
    for instruction in instructions:
        direction, steps = instruction[0], instruction[1:]
        steps = int(steps)
        if direction == "R":
            x = (x + steps) % 100
        elif direction == "L":
            x = abs((x - steps) % 100)
        if x == 0:
            zero_count += 1

    return zero_count


def star2():
    with open("test_input.txt", "r") as file:
        data = file.readlines()
    instructions = data
    x = 50
    zero_count = 0
    for instruction in instructions:
        direction, steps = instruction[0], instruction[1:]
        steps = int(steps)
        x_temp = x - steps if direction == "L" else x + steps
        x = abs(x_temp % 100)
        if x_temp != x or x == 0:
            zero_count += abs(x_temp // 100) or 1
            print(
                "instruction",
                instruction,
                "x_temp",
                x_temp,
                "x",
                x,
                "zero_count",
                zero_count,
            )
            continue
        # elif x == 0:
        #     zero_count += 1
        #     continue

    return zero_count


def star2_BruteForce():
    with open("test_input.txt", "r") as file:
        data = file.readlines()
    instructions = data
    x = 50
    zero_count = 0
    for instruction in instructions:
        direction, steps = instruction[0], instruction[1:]
        steps = int(steps)
        if direction == "L":
            for i in range(steps):
                if x == 0:
                    x = 99
                else:
                    x -= 1
                if x == 0:
                    zero_count += 1
        elif direction == "R":
            for i in range(steps):
                if x == 99:
                    x = 0
                else:
                    x += 1
                if x == 0:
                    zero_count += 1
    return zero_count


def main():
    print(star1())
    # print(star2())
    print(star2_BruteForce())


if __name__ == "__main__":
    main()
