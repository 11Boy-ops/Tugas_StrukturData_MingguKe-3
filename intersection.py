def irisan(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    return list(set1 & set2)

# Contoh
a = [1, 2, 2, 3]
b = [2, 3, 4]
print(irisan(a, b))  # Output: [2, 3] (urutan tidak dijamin)