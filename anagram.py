def anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    hitung = {}
    for c in s1:
        hitung[c] = hitung.get(c, 0) + 1
    for c in s2:
        if c not in hitung:
            return False
        hitung[c] -= 1
        if hitung[c] < 0:
            return False
    return True

# Contoh
print(anagram("listen", "silent"))  # True
print(anagram("hello", "world"))    # False