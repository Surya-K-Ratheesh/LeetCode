def main():
    S = "CADBZABCD"

    print(longest(S))

    # print(brute(S))

def longest(S):
    dict = {}
    left = right = 0
    n = len(S)
    maxi = 0

    while right < n:
        if S[right] in dict:
            left = max(left, dict[S[right]]+1)

        count_ch = right - left + 1
        maxi = max(maxi, count_ch)
        dict[S[right]] = right

        right += 1

    return maxi


# def brute(S):
#     maxi = 0
#     n = len(S)

#     for i in range(n):
#         my_set = set()

#         for j in range(i, n):
#             if S[j] in my_set:
#                 break

#             maxi = max(maxi, j-i+1)
#             my_set.add(S[j])

#     return maxi


if __name__ == "__main__":
    main()
