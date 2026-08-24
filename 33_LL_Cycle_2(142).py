def main():
    head = [3,2,0,-4]

def LL_cycle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            slow = head

            while slow != fast:
                slow = slow.next
                fast = fast.next

            return slow

        return None

def brute(head):
    temp = head
    my_set = set()

    while temp is not None:
        if temp in my_set:
            return temp

        my_set.add(temp)
        temp = temp.next

    return None


if __name__ == '__main__':
    main()