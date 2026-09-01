def main():
    nums = [1,1,1,2,2,3]
    k = 2

    hash_map = {}
    res = []

    for i in range(len(nums)):
        hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1

    sorted_hash = sorted(hash_map.items(), key = lambda x: x[1])

    for i in range(1, k+1):
        res.append(sorted_hash[-i][0])

    print(res)

if __name__ == '__main__':
    main()