def main():
    nums = [2,2,1,1,1,2,2]

    print(optimal(nums))

def optimal(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num

        count += 1 if num == candidate else -1

    return candidate

def hashh(nums):
    hash_map = {}
    
    for num in nums:
        hash_map[num] = hash_map.get(num, 0) + 1
    
    
    sorted_hash = sorted(hash_map.items(), key = lambda x: x[1])
    return (sorted_hash[-1][0])

if __name__ == '__main__':
    main()