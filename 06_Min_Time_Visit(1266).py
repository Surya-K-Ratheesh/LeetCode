def main():
    points = [[1,1],[3,4],[-1,0]]

    print(min_time_to_visit_all_points(points))

def min_time_to_visit_all_points(points):
    res = 0
    x1, y1 = points.pop()

    while points:
        x2, y2 = points.pop()
        res += max(abs(x2-x1), abs(y2-y1))
        x1, y1 = x2, y2

    return res


if __name__ == '__main__':
    main()