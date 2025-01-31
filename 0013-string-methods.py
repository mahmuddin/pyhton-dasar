print("Capitalize:")
txt = "hello, and welcome to my world."
x = txt.capitalize()
print(x)

txt = "python is FUN!"
x = txt.capitalize()
print(x)

txt = "36 is my age."
x = txt.capitalize()
print(x)
print("\n")

print("Casefold:")
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)
print("\n")

print("Center:")
txt = "banana"
x = txt.center(20)
print(x)

txt = "banana"
x = txt.center(20, "O")
print(x)
print("\n")

print("Encode:")
txt = "My name is Ståle"
x = txt.encode()
print(x)
print("\n")

txt = "My name is Ståle"
print(txt.encode(encoding="ascii", errors="backslashreplace"))
print(txt.encode(encoding="ascii", errors="ignore"))
print(txt.encode(encoding="ascii", errors="namereplace"))
print(txt.encode(encoding="ascii", errors="replace"))
print(txt.encode(encoding="ascii", errors="xmlcharrefreplace"))
print("\n")

print("Endswith:")
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

txt = "Hello, welcome to my world."
x = txt.endswith("my world.")
print(x)

txt = "Hello, welcome to my world."
x = txt.endswith("my world.", 5, 11)
y = txt.endswith("my world.", 18, len(txt))
print(x)
print(y)

print('Check if the string ends with either the phrase "world." or "castle.":')
txt = "Hello, welcome to my castle."
x = txt.endswith(("world.", "castle."))
print(x)

# Materi selengkapnya mengenai string methods bisa di lihat di:
# https://www.w3schools.com/python/python_strings_methods.asp
