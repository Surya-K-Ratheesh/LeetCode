def main():
    head = [1,2,3,4,5]

    print(middle(head))

def middle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

if __name__ == '__main__':
    main()