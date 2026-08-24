def main():
    nums = [1,12,-5,-6,50,3]
    k = 4

    print(max_avg(nums, k))

def max_avg(nums, k):
    n = len(nums)
    cur_sum = 0 

    for i in range(k):
        cur_sum += nums[i]

    max_avg = cur_sum / k

    for i in range(k, n):
        cur_sum += nums[i]
        cur_sum -= nums[i - k]

        avg = cur_sum / k
        max_avg = max(max_avg, avg)

    return max_avg

if __name__ == '__main__':
    main()