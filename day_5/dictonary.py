# ==============================
# 📌 Python Dictionary Notes
# ==============================

# ✅ Creating Dictionaries
d1 = {}                                   # Empty dictionary
d2 = {"name": "Nahid", "age": 21}         # With values
d3 = dict(country="Bangladesh", code=880) # Using dict()

# ✅ Accessing Values
print(d2["name"])        # Nahid
print(d2.get("age"))     # 21
print(d2.get("gender"))  # None (avoids error if key not found)

# ✅ Adding & Updating
d2["gender"] = "Male"    # Add new key
d2["age"] = 22           # Update value
print(d2)

# ✅ Removing Items
d2.pop("gender")         # Remove by key
d2.popitem()             # Remove last inserted pair
del d2["age"]            # Delete by key
d2.clear()               # Empty dictionary

# ✅ Iterating
person = {"name": "Nahid", "age": 21, "country": "Bangladesh"}

for key in person:
    print(key, ":", person[key])

for key, value in person.items():
    print(key, "=>", value)

# ✅ Dictionary Methods
print(person.keys())     # dict_keys(['name', 'age', 'country'])
print(person.values())   # dict_values(['Nahid', 21, 'Bangladesh'])
print(person.items())    # dict_items([('name', 'Nahid'), ('age', 21), ('country', 'Bangladesh')])

# ✅ Nesting (Dictionary inside Dictionary)
students = {
    "s1": {"name": "Araf", "age": 20},
    "s2": {"name": "Nahid", "age": 21}
}
print(students["s2"]["name"])   # Nahid
