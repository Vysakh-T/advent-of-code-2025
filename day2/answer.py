def star1():
    with open("input.txt", "r") as file:
        data = file.readlines()
        answer = 0
        for line in data:
            line = line.strip()
            ranges = line.split(",")
            for in_range in ranges:
                in_range = in_range.split("-")
                in_range = int(in_range[0]), int(in_range[1])
                for i in range(in_range[0], in_range[1] + 1):
                    # if len odd ignore
                    # if len even add split middle and check if equal
                    if len(str(i)) % 2 == 0:
                        left = str(i)[: len(str(i)) // 2]
                        right = str(i)[len(str(i)) // 2 :]
                        if left == right:
                            answer += i
        return answer


def star2():
    with open("input.txt", "r") as file:
        data = file.readlines()
        answer = 0
        for line in data:
            line = line.strip()
            ranges = line.split(",")
            for in_range in ranges:
                in_range = in_range.split("-")
                in_range = int(in_range[0]), int(in_range[1])
                for i in range(in_range[0], in_range[1] + 1):
                    factors = [j for j in range(1, len(str(i))) if len(str(i)) % j == 0]
                    for j in factors:
                        # print("j", j)
                        # divide in j parts and check if equal
                        parts = [str(i)[k : k + j] for k in range(0, len(str(i)), j)]
                        if len(set(parts)) == 1:
                            answer += i
                            # print(i, parts)
                            break

        return answer


def main():
    print(star1())
    print(star2())


if __name__ == "__main__":
    main()
