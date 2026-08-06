def main():
    prices = [7,1,5,3,6,4]
    # prices = [7,6,4,3,1]

    print(buy_sell(prices))

def buy_sell(prices):
    l, r = 0, 1
    maxP = 0

    while r != len(prices):
        if prices[l] < prices[r]:
            prof = prices[r] - prices[l]
            maxP = max(prof, maxP)

        else:
            l = r

        r += 1

    return maxP

if __name__ == '__main__':
    main()