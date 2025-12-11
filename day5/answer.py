import bisect

def star1():
    answer = 0
    range_list = []
    with open("input.txt", "r") as file:
        while True:
            ranges = file.readline()
            if ranges == "\n":
                break
            ranges = ranges.strip().split("-")
            range_list.append([int(ranges[0]), int(ranges[1])])
        while True:
            ingredient = file.readline()
            if not ingredient:
                break
            ingredient = int(ingredient.strip())
            for i in range_list:
                if ingredient >= i[0] and ingredient <= i[1]:
                    answer += 1
                    break
    return answer

def star2():
    return

def main():
    print(star1())
    # print(star2())


if __name__ == "__main__":
    main()
