def main():
    nums = [8,1,2,2,3]

    print(smaller_than_current(nums))

def smaller_than_current(nums):
    temp = sorted(nums)

    d = {}

    for i, num in enumerate(temp):
        if num not in d:
            d[num] = i

    ret = []

    for i in nums:
        ret.append(d[i])

    return ret

# def smaller_than_current(nums):
#     ret = []

#     for i in range(len(nums)):
#         count = 0

#         for j in range(len(nums)):
#             if nums[j] < nums[i]:
#                 count += 1

#         ret.append(count)

#     return ret

if __name__ == '__main__':
    main()