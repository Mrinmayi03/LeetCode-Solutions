def anagram(s,t):
    array = [0]*26

    for c in s:
        array[ord(c) - ord('a')] += 1
    for c in t:
        array[ord(c) - ord('a')] -= 1
    
    return all(val == 0 for val in array)