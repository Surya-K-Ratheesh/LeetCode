def main():
    nums = [0,1,0,3,12]

    print(two_pointer(nums))
    # brute(nums)

def two_pointer(nums):
    i = 0
    j = 1

    while j < len(nums):
        if nums[i] == 0 and nums[j] !=0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

        j += 1

    return nums

def brute(nums):
    n = len(nums)
    zeros = []
    non_zeros = []

    for i in range(n):
        if nums[i] == 0:
            zeros.append(nums[i])

        else:
            non_zeros.append(nums[i])

    nums[:len(non_zeros)] = non_zeros
    nums[len(non_zeros):] = zeros

    print(nums)

if __name__ == '__main__':
    main()