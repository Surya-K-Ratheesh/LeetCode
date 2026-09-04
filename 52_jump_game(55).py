def main():
    nums = [2,3,1,1,4]

    print(greedy(nums))

def greedy(nums):
    max_reach = 0

    for i, jump in enumerate(nums):
        if i > max_reach:
            return False

        max_reach = max(max_reach, i + jump)

        if max_reach >= len(nums) - 1:
            return True

    return False

if __name__ == '__main__':
    main()