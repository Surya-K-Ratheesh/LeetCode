def main():
    s = "A man, a plan, a canal: Panama"

    print(two_pointer(s))
    # print(valid_pld(s))

def two_pointer(s):
    s = s.lower()
    special_char = ' ,@:.&*#$%"!?_-+=/|{[]}():;><^~'

    for i in s:
        if i in special_char:
            s = s.replace(i,'')

    s = s.replace("'",'')

    if s == s[::-1]:
        return True

    return False


def valid_pld(s):
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    main()