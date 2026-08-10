def main():
    nums = [1,2,3,1] 
    k = 3

    print(dupli(nums, k))

def dupli(nums, k):
    seen = set()

    for i, num in enumerate(nums):
        if num in seen:
            return True

        seen.add(num)
        if len(seen) > k:
            seen.remove(i - k)

    return False

if __name__ == '__main__':
    main()