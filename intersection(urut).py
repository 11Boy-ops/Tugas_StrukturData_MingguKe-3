def irisan_urut(arr1, arr2):
    set2 = set(arr2)
    hasil = []
    for item in arr1:
        if item in set2 and item not in hasil:
            hasil.append(item)
    return hasil

print(irisan_urut(a, b))  # Output: [2, 3]