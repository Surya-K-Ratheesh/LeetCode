def main():
    head = [3,2,0,-4]

def cycle_length(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            slow = slow.next
            count = 1

            while slow != fast:
                slow = slow.next
                count += 1

            return count

    return 0


def brute(head):
    temp = head
    my_dict = {}
    travel = 0

    while temp is not None:
        if temp in my_dict:
            return travel - my_dict[temp]

        my_dict[temp] = travel
        travel += 1
        temp = temp.next

    return 0

if __name__ == '__main__':
    main()