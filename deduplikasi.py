def deduplikasi(lst):
    seen = set()
    hasil = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            hasil.append(item)
    return hasil

# Contoh penggunaan
data = [3, 1, 2, 1, 3, 4]
print(deduplikasi(data))  # Output: [3, 1, 2, 4]