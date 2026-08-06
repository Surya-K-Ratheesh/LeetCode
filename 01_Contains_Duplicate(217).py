def main():
    nums = [1, 2, 3, 4, 5, 1]
    # nums = [1, 2, 3, 4, 5]

    print(duplicate(nums))

def duplicate(nums):
    if len(set(nums)) != len(nums):
        return True

    else:
        return False

if __name__ == "__main__":
    main()