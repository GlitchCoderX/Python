# ==============================
# 📌 Python Tuple Notes
# ==============================

# ✅ Creating Tuples
t1 = ()                  # Empty tuple
t2 = (1, 2, 3)           # With values
t3 = 1, 2, 3             # Parentheses optional
t4 = (5,)                # Single element tuple (comma required)

# ✅ Accessing Elements
fruits = ("apple", "banana", "cherry")
print(fruits[0])     # apple
print(fruits[-1])    # cherry

# ✅ Tuple Operations
print(len(fruits))          # Length -> 3
print(("a", "b") + ("c",))  # Concatenation -> ('a', 'b', 'c')
print((1, 2) * 3)           # Repetition -> (1, 2, 1, 2, 1, 2)
print("banana" in fruits)   # Membership -> True

# ✅ Immutability
# fruits[0] = "mango"   # ❌ Error (cannot modify tuple)

# ✅ Mutable inside Tuple
t = (1, [2, 3], 4)
t[1][0] = 99
print(t)   # (1, [99, 3], 4)

# ✅ Packing & Unpacking
person = ("Nahid", 21, "Bangladesh")
name, age, country = person
print(name, age, country)   # Nahid 21 Bangladesh
