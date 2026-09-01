def main():
    nums = [100,4,200,1,3,2]

    # print(brute(nums))
    print(hashh(nums))

def hashh(nums):
    if not nums:
        return 0

    hash_map = {}
    max_len = 0

    for num in nums:
        hash_map[num] = True

    for num in hash_map:
        if num - 1 not in hash_map:
            length = 1

            while num + length in hash_map:
                length += 1

            max_len = max(max_len, length)

    return max_len

    
def brute(nums):
    if not nums:
        return 0

    i, j = 0, 1
    size = 0
    sorted_nums = sorted(set(nums))

    while i < len(sorted_nums) - 1 and j < len(sorted_nums):
        if sorted_nums[j] - sorted_nums[j-1] == 1:
            j += 1

        else:
            size = max(size, j-i)
            i = j
            j = i + 1

    size = max(size, j - i)

    return size


if __name__ == '__main__':
    main()