def main():
    nums = [1, 2, 3, 4]

    # brute(nums)
    print(optimal(nums))

def optimal(nums):
    n = len(nums)
    prefix = [1] * n
    suffix = [1] * n
    answer = []

    for i in range(1, n):
        prefix[i] = prefix[i-1] * nums[i-1]

    for i in range(n-2, -1, -1):
        suffix[i] = suffix[i+1] * nums[i+1]

    for i in range(n):
        answer.append(prefix[i] * suffix[i])

    return answer

def brute(nums):
    res = []

    for i in range(len(nums)):
        prod = 1
        for j in range(len(nums)):
            if i == j:
                continue
            else:
                prod = prod * nums[j]
                print(prod)
                
        res.append(prod)

    print(res)
            

if __name__ == '__main__':
    main()