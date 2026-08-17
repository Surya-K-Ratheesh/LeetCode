def main():
    head = [1,2,6,3,4,5,6] 
    val = 6

def rem(head, val):
    dummy_head = ListNode(-1)
    dummy_head.next = head

    current = dummy_head
    while current.next != None:
        if current.next.val == val:
            current.next = current.next.next

        else:
            current = current.next

    return dummmy_head.next

if __name__ == '__main__':
    main()