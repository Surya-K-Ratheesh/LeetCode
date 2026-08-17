def main():
    height = [1,8,6,2,5,4,8,3,7]

    print(rain(height))

def rain(height):
    l = 0
    r = len(height)-1
    cap = []

    while l < r:
        h = min(height[l], height[r])
        area = (r - l) * h
        cap.append(area)

        if height[l] < height[r]:
            l += 1

        else:
            r -= 1

    return max(cap)

# BRUTE FORCE
# def rain(height):
#     cap = []

#     for l in range(len(height)):
#         for r in range(l+1, len(height)):
#             h = min(height[l], height[r])
#             cap.append(h * (r-l))

#     print(max(cap))


if __name__ == '__main__':
    main()