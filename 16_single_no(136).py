def main():
    nums = [4,1,2,1,2]

    xor = single(nums)

    print(f"Unique number in list = {xor}")

def single(nums):
    xor = 0

    for i in nums:
        xor = xor ^ i

    return xor

# def single(nums):
#     ret = 0

#     for i in range(len(nums)):
#         count = 0

#         for j in range(len(nums)):
#             if nums[i] == nums[j]:
#                 count += 1

#         if count == 1:
#             res = nums[i]

#     return res 

if __name__ == '__main__':
    main()