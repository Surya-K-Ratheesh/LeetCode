def main():
    head = [1,2,3,4,5]

def odd_even(head):
    if head is None or head.next is None:
        return head

    odd = head
    even = head.next
    even_head = even

    while even is not None and even.next is not None:
        odd.next = odd.next.next
        odd = odd.next

        even.next = even.next.next
        even = even.next

    odd.next = even_head

    return head


def brute(head):
    if head is None or head.next is None:
        return head

    values = []
    temp = head

    while temp:
        values.append(temp.val)
        temp = temp.next.next if temp.next else None

    temp = head.next
    while temp:
        values.append(temp.val)
        temp = temp.next.next if temp.next else None

    temp = head
    index = 0

    while temp is not None:
        temp.val = values[index]
        index += 1
        temp = temp.next

    return head

if __name__ == '__main__':
    main()