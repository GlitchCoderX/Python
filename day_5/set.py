# ==============================
# 📌 Python Set Notes
# ==============================

# ✅ Creating Sets
s1 = {1, 2, 3}              # With values
s2 = set([1, 2, 2, 3])      # Duplicates removed -> {1, 2, 3}
s3 = set()                  # Empty set (NOT {} because {} = dictionary)

# ✅ Properties
# - No duplicates
# - Unordered (no indexing)
# - Mutable (can add/remove items)

# ✅ Adding & Removing
s1.add(4)              # Add single element
s1.update([5, 6])      # Add multiple elements
print(s1)              # {1, 2, 3, 4, 5, 6}

s1.remove(6)           # Remove element (Error if not found)
s1.discard(10)         # Remove if exists (No error if not found)
x = s1.pop()           # Remove random element
s1.clear()             # Empty the set

# ✅ Set Operations (Math-like)
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)     # Union -> {1, 2, 3, 4, 5, 6}
print(a & b)     # Intersection -> {3, 4}
print(a - b)     # Difference -> {1, 2}
print(a ^ b)     # Symmetric Difference -> {1, 2, 5, 6}

# ✅ Membership
print(3 in a)    # True
print(10 not in a)  # True

# ✅ Useful Example
unique_names = {"Nahid", "Araf", "Nahid"}  # Duplicates removed
print(unique_names)   # {'Nahid', 'Araf'}
