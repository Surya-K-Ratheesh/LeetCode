def main():
    greed = [2, 6, 8, 1, 4]
    cookies = [4, 2, 7, 1, 2, 3]

    # greed = [1,2,3]
    # cookies = [1,1]

    print(greedy_two_pointer(greed, cookies))
    # print(brute(greed, cookies))

def greedy_two_pointer(greed, cookies):
    sorted_greed = sorted(greed)
    sorted_cookies = sorted(cookies)
    count = 0
    i = j = 0

    while i < len(sorted_greed) and j < len(sorted_cookies):
        if sorted_greed[i] <= sorted_cookies[j]:
            count += 1
            i += 1

        j += 1

    return count

def brute(greed, cookies):
    sorted_greed = sorted(greed)
    sorted_cookies = sorted(cookies)
    n, m = len(sorted_greed), len(sorted_cookies)
    count = 0

    for i in range(n):
        for j in range(m):
            if sorted_cookies[j] >= sorted_greed[i]:
                count += 1
                m -= 1
                sorted_cookies.pop(j)
                break

    return count

if __name__ == '__main__':
    main()