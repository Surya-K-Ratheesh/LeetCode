def main():
    s = "anagram" 
    t = "nagaram"

    print(anagram(s, t))

def anagram(s, t):
    if len(s) != len(t):
        return False

    s_dict = {}
    t_dict = {}

    for i in range(len(s)):
        s_dict[s[i]] = s_dict.get(s[i], 0) + 1
        t_dict[t[i]] = t_dict.get(t[i], 0) + 1

    return s_dict == t_dict

# def anagram(s, t):
#     s_sorted = "".join(sorted(s))
#     t_sorted = "".join(sorted(t))

#     l = r = 0
    
#     if len(s_sorted) != len(t_sorted):
#         return False

#     while l < len(s_sorted) and r < len(t_sorted):
#         if s_sorted[l] != t_sorted[r]:
#             return False

#         l += 1
#         r += 1

#     return True

    

if __name__ == '__main__':
    main()