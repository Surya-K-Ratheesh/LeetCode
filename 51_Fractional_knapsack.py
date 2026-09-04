# Given two arrays, val[] and wt[] , representing the values and weights of items, and an integer capacity representing the maximum weight a knapsack can hold, determine the maximum total value that can be achieved by putting items in the knapsack. You are allowed to break items into fractions if necessary.
# Return the maximum value as a double, rounded to 6 decimal places.

# Examples :

# Input: val[] = [60, 100, 120], wt[] = [10, 20, 30], capacity = 50
# Output: 240.000000
# Explanation: By taking items of weight 10 and 20 kg and 2/3 fraction of 30 kg. Hence total price will be 60+100+(2/3)(120) = 240

def main():
    value = [100, 60, 100, 200]
    weights = [20, 10, 50, 50]
    w = 90

    print(greedy(value, weights, w))

def greedy(value, weights, w):
    arr = list(zip(value, weights))
    sorted_arr = sorted(arr, key= lambda x: x[0]//x[1], reverse=True)
    curr_weight = 0
    final_value = 0

    for i in range(0,  len(sorted_arr)):
        if curr_weight + sorted_arr[i][1] <= w:
            curr_weight += sorted_arr[i][1]
            final_value += sorted_arr[i][0]

        else:
            remain = w - curr_weight
            cost = sorted_arr[i][0] / sorted_arr[i][1] * remain
            final_value += cost
            break

    return final_value
             
    

if __name__ == '__main__':
    main()