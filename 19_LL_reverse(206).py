def main():
    head = [1,2,3,4,5]

def rev(head):
    prev = None
    current = head

    while current is not None:
        next_pointer = current.next
        current.next = prev

        prev = current
        current = next_pointer

    head = prev

    return prev

if __name__ == '__main__':
    main()