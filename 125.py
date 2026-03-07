def palindrom(s):
    clean_s = "".join(ch.lower() for ch in s if ch.isalnum())
    P1, P2 = 0, len(clean_s)-1
    while P1 < P2:
        if clean_s[P1] != clean_s[P2]:
            return False
        P1 += 1
        P2 -= 1
    
    return True