def main():
    nums = [3,9,2,1,7] 
    k = 3
    num = []
    count = {}
    n = len(nums)

    for i in range(k):
        num.append(nums[i])
        count[nums[i]] = 1

    for i in range(k, n):
        num.append(nums[i])
        num.pop(0)

        for v in set(num):
            count[v] = count.get(v, 0) + 1

    best = -1
    for v, c in count.items():
        if c == 1:
            best = max(best, v)

    print(best)
        
if __name__ == '__main__':
    main()