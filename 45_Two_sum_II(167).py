def main():
    nums = [2,7,11,15]
    target = 13

    print(two_pointer(nums, target))

def two_pointer(nums, target):
    i, j = 0, len(nums)-1

    while i < j:
        if nums[i] + nums[j] == target:
            return [i+1, j+1]

        elif nums[i] + nums[j] < target:
            i += 1

        else:
            j -= 1

    return None


if __name__ == '__main__':
    main()