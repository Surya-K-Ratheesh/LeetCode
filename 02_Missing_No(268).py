def main():
    nums = [3, 0, 1]

    print(missing(nums))

def missing(nums):
    return sum(range(len(nums)+1)) - sum(nums)

# def missing(nums):
#     nums.sort() #O(nlogn)

#     for i, v in enumerate(nums):
#         if i != v:
#             return v-1

#         if i == len(nums)-1:
#             return v+1

if __name__ == "__main__":
    main()