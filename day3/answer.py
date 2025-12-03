def star1():
    with open("input.txt", "r") as file:
        data = file.readlines()
        answer = 0
        for line in data:
            line = line.strip()
            max_dig = int(line[0])
            max_ind = 0
            for i in range(1, len(line) - 1):
                if int(line[i]) > max_dig:
                    max_dig = int(line[i])
                    max_ind = i
            second_max_dig = int(line[max_ind + 1])
            for i in range(max_ind + 1, len(line)):
                if int(line[i]) > second_max_dig:
                    second_max_dig = int(line[i])
            # print("line", line, "joltage", max_dig, second_max_dig)
            answer += (max_dig * 10) + second_max_dig
        return answer


def get_max_joltage(line):
    max_dig = int(line[0])
    max_ind = 0
    for i in range(1, len(line)):
        if int(line[i]) > max_dig:
            max_dig = int(line[i])
            max_ind = i
    return max_dig, max_ind


def star2():
    with open("input.txt", "r") as file:
        data = file.readlines()
        answer = 0
        num_dig = 12
        for line in data:
            line = line.strip()
            max_list = []
            # max_ind = 0
            # max_dig = int(line[0])
            for i in range(num_dig - 1):
                max_dig, max_ind = get_max_joltage(line[: i - num_dig + 1])
                line = line[max_ind + 1 :]
                max_list.append(max_dig)
            max_dig, max_ind = get_max_joltage(line)
            max_list.append(max_dig)
            # print("line", line, "max_list", max_list)
            answer += int("".join(map(str, max_list)))
        return answer


def main():
    print(star1())
    print(star2())


if __name__ == "__main__":
    main()
