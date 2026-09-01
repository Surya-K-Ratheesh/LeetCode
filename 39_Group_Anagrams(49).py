from collections import Counter

def main():
    strs = ["eat","tea","tan","ate","nat","bat"]
    # [["bat"],["nat","tan"],["ate","eat","tea"]]

    print(brute(strs))

def brute(strs):
    visited = set()
    groups = []

    for i in range(len(strs)):
        if strs[i] in visited:
            continue
        visited.add(strs[i])
        group = [strs[i]]

        for j in range(i+1, len(strs)):
            if Counter(strs[i]) == Counter(strs[j]):
                group.append(strs[j])
                visited.add(strs[j])

        groups.append(group)

    return groups

def grp_anagram(strs):
    anagram_map = {}

    for s in strs:
        key = "".join(sorted(s))

        if key not in anagram_map:
            anagram_map[key] = [s]
        else:
            anagram_map[key].append(s)

    return anagram_map.values()    

if __name__ == '__main__':
    main()