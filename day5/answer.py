import bisect

def star1():
    fresh_range_map = dict()
    lower_bound_list = []
    answer = 0
    with open("input.txt", "r") as file:
        while True:
            ranges = file.readline()
            if ranges == "\n":
                break
            ranges = ranges.strip()
            fresh_range_map[int(ranges.split("-")[0])] = int(ranges.split("-")[1])
            lower_bound_list.append(int(ranges.split("-")[0]))
        lower_bound_list.sort()
        # print(lower_bound_list, fresh_range_map)
        while True:
            ingredient = file.readline()
            if not ingredient:
                break
            ingredient = int(ingredient.strip())
            # binary search lower bound list for nearest lower bound
            lower_bound = bisect.bisect_left(lower_bound_list, ingredient)-1
            if lower_bound == len(lower_bound_list):
                lower_bound -= 1
            elif lower_bound == -1:
                lower_bound = 0
            # print(lower_bound)
            # print(lower_bound_list[lower_bound], fresh_range_map[lower_bound_list[lower_bound]], ingredient)
            if ingredient >= lower_bound_list[lower_bound] and ingredient <= fresh_range_map[lower_bound_list[lower_bound]]:
                answer += 1
    return answer

def star2():
    return

def main():
    print(star1())
    # print(star2())


if __name__ == "__main__":
    main()
