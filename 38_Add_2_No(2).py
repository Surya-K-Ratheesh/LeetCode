def main():
    l1 = [2,4,3]
    l2 = [5,6,4]
    # Output: [7,0,8]
    # Explanation: 342 + 465 = 807.

    class ListNode:
        def __init__(self, val = 0, next = None):
            self.val = val
            self.next = next

    class solution:
        def add_no(self, l1, l2):
            dummy_head = ListNode(0)
            tail = dummy_head
            carry = 0

            while l1 is not None or l2 is not None or carry != 0:
                digit_1 = l1.val if l1 is not None else 0
                digit_2 = l2.val if l2 is not None else 0

                sum = digit_1 + digit_2 + carry
                digit = sum % 10
                carry = sum // 10

                new_node = ListNode(digit)
                tail.next = new_node
                tail = tail.next

                l1 = l1.next if l1 is not None else None
                l2 = l2.next if l2 is not None else None

            result = dummy_head.next
            dummy_head.next = None

            return result

if __name__ == '__main__':
    main()
