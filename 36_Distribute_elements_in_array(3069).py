def main():
    nums = [1,2,4]

    arr1 = []
    arr2 = []
    res = []

    arr1.append(nums[0])
    arr2.append(nums[1])

    for i in range(2, len(nums)):
        if arr1[-1] > arr2[-1]:
            arr1.append(nums[i])

        else:
            arr2.append(nums[i])

    res = arr1 + arr2

    print(res)

    # for i in range(len(nums)):
    #     arr1.append(nums[i])
    #     arr2.append(nums[i]+1)
    #     break

    # print(arr1, arr2)

    # while l < len(nums):
    #     arr1.append(nums[l])
    #     l += 2

    # while r < len(nums):
    #     arr2.append(nums[r])
    #     r += 2

    # arr1.extend(arr2)

    # print(arr1)


if __name__ == '__main__':
    main()