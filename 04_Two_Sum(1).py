def main():
    nums = [2, 7, 11, 15]
    target = 9

    # n = int(input("Enter the number of elements in the array: "))
    #     nums = []
    
    #     for i in range(n):
    #         nums.append(int(input(f"Enter element {i+1}: ")))
    
    #     target = int(input("Enter the target sum: "))

    print(two_sum(nums, target))

def two_sum(nums, target):
    hash_map = {} #val, index

    for i, num in enumerate(nums):
        diff = target - num

        if diff in hash_map:
            return [hash_map[diff], i]

        hash_map[num] = i

# def two_sum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return nums[i], nums[j]

if __name__ == "__main__":
    main()