def main():
    s = "AABABBA"
    k = 1

    print(sliding_window(s, k))

def sliding_window(s, k):
    count = {}
    left = max_length = max_freq = 0
    n = len(s)

    for right in range(n):
        count[s[right]] = count.get(s[right], 0) + 1
        max_freq = max(max_freq, count[s[right]])

        while (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

if __name__ == '__main__':
    main()