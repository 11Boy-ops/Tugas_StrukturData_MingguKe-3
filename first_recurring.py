def karakter_pertama_berulang(s):
    dilihat = set()
    for c in s:
        if c in dilihat:
            return c
        dilihat.add(c)
    return None

# Contoh
print(karakter_pertama_berulang("DBCABA"))  # Output: 'B'
print(karakter_pertama_berulang("ABCD"))    # Output: None