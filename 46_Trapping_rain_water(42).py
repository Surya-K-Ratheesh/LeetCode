def main():
    height = [0,1,0,2,1,0,1,3,2,1,2,1]

    print(two_pointer(height))
    # print(prefix_suffix(height))

def two_pointer(height):
    left = 0
    right = len(height) - 1
    max_left = max_right = 0
    total = 0

    while left < right:
        max_left = max(max_left, height[left])
        max_right = max(max_right, height[right])

        if max_left < max_right:
            water = max_left - height[left]
            total += water
            left += 1

        else:
            water = max_right - height[right]
            total += water
            right -= 1

    return total

def prefix_suffix(height):
    n = len(height)
    water_level = 0

    prefix = [0] * n
    prefix[0] = height[0]

    suffix = [0] * n
    suffix[n-1] = height[n-1]

    for i in range(1, n):
        prefix[i] = max(prefix[i-1], height[i])

    for i in range(n-2, -1, -1):
        suffix[i] = max(suffix[i+1], height[i])

    for i in range(n):
        water_level += min(prefix[i], suffix[i]) - height[i]

    return water_level

if __name__ == '__main__':
    main()