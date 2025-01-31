print("Strings")
# You can use double or single quotes:
print("Hello")
print('Hello')

print("Quotes Inside Quotes:")
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

print("Assign String to a Variable")
a = "Hello"
print(a)
print("\n")

print("Multiline Strings:")
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
print("\n")

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
print("\n")


print("Strings are Arrays:")
a = "Hello, World!"
print(a[1])
print("\n")

print("Looping Through a String:")
for x in "banana":
    print(x)
print("\n")

print("String Length:")
a = "Hello world!"
print(len(a))
print("\n")

print("Check String:")
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
    print("free is in txt")
else:
    print("free is not in txt")
print("\n")


print("Check if NOT:")
txt = "The best things in life are free!"
print("expensive" not in txt)


txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
else:
    print("Yes, 'expensive' is present.")
