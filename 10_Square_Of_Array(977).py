from collections import deque

def main():
    nums = [-4,-1,0,3,10]

    print(sq_array(nums))

def sq_array(nums):
    ans = deque()
    l, r = 0, len(nums)-1

    while l <= r:
        left, right = abs(nums[l]), abs(nums[r])

        if left > right:
            ans.appendleft(left**2)
            l += 1

        else:
            ans.appendleft(right**2)
            r -= 1

    return list(ans)


# DIVIDE AND MERGE
# def sq_array(nums):
#     if not nums:
#         return nums

#     if nums[0] > 0:
#         return [num**2 for num in nums]

#     m = 0
#     for i, n in enumerate(nums):
#         if n >= 0:
#             m = i
#             break

#     A, B = nums[m:], [-1*n for n in reversed(nums[:m])]

#     def merge(A, B):
#         a = b = 0
#         ret = []

#         while a < len(A) and b < len(B):
#             if A[a] < B[b]:
#                 ret.append(A[a])
#                 a += 1

#             else:
#                 ret.append(B[b])
#                 b += 1

#         if a < len(A):
#             ret.extend(A[a:])
#         else:
#             ret.extend(B[b:])

#         return [n**2 for n in ret]

#     print(merge(A,B))


# SIMPLEST METHOD
# def sq_array(nums):
#     sq_list = [num**2 for num in nums]
#     sq_list.sort()

#     return sq_list

if __name__ == '__main__':
    main()