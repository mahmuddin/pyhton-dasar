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
print("\n")

print('Python String expandtabs() Method:')
txt = "H\te\tl\tl\to"
x = txt.expandtabs(2)
print(x)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))
print("\n")

print('Python String find() Method:')
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

x = txt.find("e")
print(x)

# Where in the text is the first occurrence of the letter "e" when you only search between position 5 and 10?:
x = txt.find("e", 5, 10)
print(x)

# If the value is not found, the find() method returns -1, but the index() method will raise an exception:
print(txt.find("q"))
# print(txt.index("q"))  # IndexError: substring not found
print("\n")

print('Python String format() Method:')
# Insert the price inside the placeholder, the price should be in fixed point, two-decimal format:
txt = "For only {price:.2f} dollars!"
print(txt.format(price=49))
# named indexes:
txt1 = "My name is {fname}, I'm {age}".format(fname="John", age=36)
# numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("John", 36)
# empty placeholders:
txt3 = "My name is {}, I'm {}".format("John", 36)

print(txt1)
print(txt2)
print(txt3)

# To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.
# Use "<" to left-align the value:
txt = "We have {:<8} chickens."
print(txt.format(49))

# To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.
# Use ">" to right-align the value:
txt = "We have {:>8} chickens."
print(txt.format(49))

# To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.
# Use "^" to center-align the value:
txt = "We have {:^8} chickens."
print(txt.format(49))

# To demonstrate, we insert the number 8 to specify the available space for the value.
# Use "=" to place the plus/minus sign at the left most position:
txt = "The temperature is {:=8} degrees celsius."
print(txt.format(-5))

# Use "+" to always indicate if the number is positive or negative:
txt = "The temperature is between {:+} and {:+} degrees celsius."
print(txt.format(-3, 7))

# Use "%" to convert the number into a percentage format:
txt = "You scored {:%}"
print(txt.format(0.25))
# Or, without any decimals:
txt = "You scored {:.0%}"
print(txt.format(0.25))


# Materi selengkapnya mengenai string methods bisa di lihat di:
# https://www.w3schools.com/python/python_strings_methods.asp
