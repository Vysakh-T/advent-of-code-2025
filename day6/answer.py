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
    for i in range(len(data)-1):
        data[i] = data[i].strip().split()
    operations = data[-1].strip().split()
    data.pop()
    # rotate data using matrix rotation
    rotated_data = pandas.DataFrame(data).T.values.tolist()
    for i in range(len(rotated_data)):
        max_len=len(max(rotated_data[i], key=len))
        rotated_data[i] = [x.rjust(max_len) for x in rotated_data[i]]
    new_rotated_data = []
    for i in range(len(rotated_data)):
        new_rotated_data.append([])
        for j in range(len(rotated_data[i])):
            temp = ""
            for k in range(len(rotated_data[i][j])):
                temp += rotated_data[i][j][k] if rotated_data[i][j][k] != " " else "0"
            new_rotated_data[i].append(int(temp))
    print(new_rotated_data)
    # local_answer = operations_map[operations[i]](local_answer, data[j][i])
    # answer += local_answer
    return answer

def main():
    print(star1())
    print(star2())


if __name__ == "__main__":
    main()
