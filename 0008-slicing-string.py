# Note: The first character has index 0.
print("Slicing Strings:")
b = "Hello, World!"
print(b[2:5])
print("\n")

print("Slice from the start:")
b = "Hello, World!"
print(b[:5])
print("\n")


print("Slice to the end:")
b = "Hello, World!"
print(b[2:])
print("\n")

print("Negative indexing:")
# Get the characters:
# From: "o" in "World!" (position -5)
# To, but not included: "d" in "World!" (position -2):
b = "Hello, World!"
print(b[-5:-2])  # result: "orl"
print("\n")

x = 'Welcome'
print(x[3:5])  # result: 'co'
