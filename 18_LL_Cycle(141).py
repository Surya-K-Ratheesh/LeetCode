def main():
    head = [3,2,0,-4]
    # According to Q in leetcode -4 has next = 2

def cycle(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

if __name__ == '__main__':
    main()