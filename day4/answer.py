def star1():
    rolls_matrix = []
    with open("input.txt", "r") as file:
        rolls_matrix = file.readlines()
    max_adj_count = 4
    answer = 0
    for i in range(len(rolls_matrix)):
        line = rolls_matrix[i].strip()
        for j in range(len(line)):
            if line[j] == "@":
                adj_count = 0
                if i > 0 and rolls_matrix[i - 1][j] == "@":
                    adj_count += 1
                if i < len(rolls_matrix) - 1 and rolls_matrix[i + 1][j] == "@":
                    adj_count += 1
                if j > 0 and rolls_matrix[i][j - 1] == "@":
                    adj_count += 1
                if j < len(line) - 1 and rolls_matrix[i][j + 1] == "@":
                    adj_count += 1
                if i > 0 and j > 0 and rolls_matrix[i - 1][j - 1] == "@":
                    adj_count += 1
                if i > 0 and j < len(line) - 1 and rolls_matrix[i - 1][j + 1] == "@":
                    adj_count += 1
                if i < len(rolls_matrix) - 1 and j > 0 and rolls_matrix[i + 1][j - 1] == "@":
                    adj_count += 1
                if i < len(rolls_matrix) - 1 and j < len(line) - 1 and rolls_matrix[i + 1][j + 1] == "@":
                    adj_count += 1
                if adj_count < max_adj_count:
                    answer += 1
    return answer

def forklift_rolls(rolls_matrix):
    max_adj_count = 4
    answer = 0
    for i in range(len(rolls_matrix)):
        line = rolls_matrix[i].strip()
        for j in range(len(line)):
            if line[j] == "@":
                adj_count = 0
                if i > 0 and rolls_matrix[i - 1][j] == "@":
                    adj_count += 1
                if i < len(rolls_matrix) - 1 and rolls_matrix[i + 1][j] == "@":
                    adj_count += 1
                if j > 0 and rolls_matrix[i][j - 1] == "@":
                    adj_count += 1
                if j < len(line) - 1 and rolls_matrix[i][j + 1] == "@":
                    adj_count += 1
                if i > 0 and j > 0 and rolls_matrix[i - 1][j - 1] == "@":
                    adj_count += 1
                if i > 0 and j < len(line) - 1 and rolls_matrix[i - 1][j + 1] == "@":
                    adj_count += 1
                if i < len(rolls_matrix) - 1 and j > 0 and rolls_matrix[i + 1][j - 1] == "@":
                    adj_count += 1
                if i < len(rolls_matrix) - 1 and j < len(line) - 1 and rolls_matrix[i + 1][j + 1] == "@":
                    adj_count += 1
                if adj_count < max_adj_count:
                    answer += 1
                    line = line[:j] + "." + line[j + 1:]
                    rolls_matrix[i] = line
    return answer

def star2():
    rolls_matrix = []
    with open("input.txt", "r") as file:
        rolls_matrix = file.readlines()
    answer = 0
    prev_answer = 0
    while answer==0 or answer>prev_answer:
        prev_answer = answer
        answer += forklift_rolls(rolls_matrix)
    return answer


def main():
    print(star1())
    print(star2())


if __name__ == "__main__":
    main()
