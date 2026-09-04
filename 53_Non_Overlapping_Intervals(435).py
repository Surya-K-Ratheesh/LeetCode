def main():
    intervals = [[1,100],[11,22],[1,11],[2,12]]
    print(greedy(intervals))

def greedy(intervals):
    count = 0
    sorted_interval = sorted(intervals, key= lambda x:x[1])
    last_end = sorted_interval[0][1]

    for i in range(1, len(sorted_interval)):
        if sorted_interval[i][0] >= last_end:
            last_end = sorted_interval[i][1]

        else:
            count += 1

    return count


if __name__ == '__main__':
    main()