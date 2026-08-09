def main():
    nums = [-1,0,1,2,-1,-4]

    print(three_sum(nums))

def three_sum(nums):
    triplets = []
    nums.sort()

    for i, val in enumerate(nums):
        if (i > 0) and val == nums[i-1]:
            continue

        left = i + 1
        right = (len(nums)-1)

        while left < right:
            currentSum = val + nums[left] + nums[right]

            if currentSum < 0:
                left += 1

            elif currentSum > 0:
                right -= 1

            else:
                triplets.append([val, nums[left], nums[right]])
                left += 1

                while (left < right) and (nums[left] == nums[left-1]):
                    left += 1

    return triplets

if __name__ == '__main__':
    main()