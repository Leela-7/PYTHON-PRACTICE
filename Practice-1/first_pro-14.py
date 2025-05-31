# Demonstrating slicing in Python

# Define a sample string
sample_string = "Hello, World!"

# Slicing examples
print("Original String:", sample_string)
print("Slice [0:5]:", sample_string[0:5])  # First 5 characters
print("Slice [7:]:", sample_string[7:])    # From index 7 to the end
print("Slice [:5]:", sample_string[:5])    # From start to index 5
print("Slice [-6:]:", sample_string[-6:])  # Last 6 characters
print("Slice [::2]:", sample_string[::2])  # Every second character
print("Slice [::-1]:", sample_string[::-1])  # Reverse the string