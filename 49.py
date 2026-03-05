from collections import defaultdict

def anagramgroup(strs):
    map = defaultdict(list)
    for word in strs:
        array = [0] * 26
        for ch in word:
            array[ord(ch) - ord('a')] += 1
        map[tuple(array)].append(word)

    return list(map.values())