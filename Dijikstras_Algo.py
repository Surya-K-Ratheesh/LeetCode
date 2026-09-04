import heapq

def main():
    adj_list = {
        0 : [[1, 4], [2, 4]],
        1 : [[0, 4], [2, 2]],
        2 : [[0, 4], [1, 2], [3, 3], [4, 1], [5, 6]],
        3 : [[2, 3], [5, 2]],
        4 : [[2, 1], [5, 3]],
        5 : [[2, 6], [3, 2], [4, 3]] 
    }
    src = 0

    nodes = len(adj_list)
    distance = [float('inf') for _ in range(nodes)]
    distance[src] = 0

    priority_queue = [[0, src]]

    while len(priority_queue) != 0:
        curr_dist, node = heapq.heappop(priority_queue)

        if curr_dist > distance[node]:
            continue

        for adjNode, weight in adj_list[node]:
            dist_travel  = curr_dist + weight

            if dist_travel < distance[adjNode]:
                distance[adjNode] = dist_travel
                heapq.heappush(priority_queue, [dist_travel, adjNode])

    print(distance)

if __name__ == '__main__':
    main()