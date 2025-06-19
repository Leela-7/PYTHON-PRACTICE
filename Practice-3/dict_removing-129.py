# Initial dictionary
data = {
    'name': 'Naresh',
    'age': 25,
    'city': 'Hyderabad',
    'email': 'naresh@example.com'
}

print("Original Dictionary:")
print(data)

# 1. Using del keyword
del data['email']
print("\nAfter using del to remove 'email':")
print(data)

# 2. Using pop method
removed_value = data.pop('city')
print(f"\nAfter using pop to remove 'city' (value was: {removed_value}):")
print(data)

# 3. Using popitem method (removes last inserted item)
last_item = data.popitem()
print(f"\nAfter using popitem to remove last item {last_item}:")
print(data)

# 4. Using clear method (removes all items)
data.clear()
print("\nAfter using clear to remove all items:")
print(data)
