def main():
    gas = [1,2,3,4,5] 
    cost = [3,4,5,1,2]

    print(greedy(gas, cost))

def greedy(gas, cost):
    if sum(gas) < sum(cost):
        return -1

    n = len(gas)
    start = 0
    total = 0
    current_tank = 0

    for i in range(n):
        total += gas[i] - cost[i]
        current_tank += gas[i] - cost[i]

        if current_tank < 0:
            start = i + 1
            current_tank = 0

    return start

if __name__ == '__main__':
    main()