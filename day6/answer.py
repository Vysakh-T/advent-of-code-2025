import pandas
operations_map = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}

def star1():
    answer = 0
    with open("input.txt", "r") as file:
        data = file.readlines()
    for i in range(len(data)-1):
        data[i] = [int(x) for x in data[i].strip().split()]
    operations = data[-1].strip().split()
    for i in range(len(operations)):
        local_answer = data[0][i]
        # print(local_answer)
        for j in range(1,len(data)-1):
            local_answer = operations_map[operations[i]](local_answer, data[j][i])
        answer += local_answer
    return answer

def star2():
    answer = 0
    with open("test_input.txt", "r") as file:
        data = file.readlines()
    for i in range(len(data)):
        data[i] = data[i].strip()
        print(data[i])
    return answer

def main():
    print(star1())
    print(star2())


if __name__ == "__main__":
    main()
