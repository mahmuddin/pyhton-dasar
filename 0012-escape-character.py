txt = "We are the so-called \"Vikings\" from the north."
print(txt)
print("\n")

print("Single Quote:")
txt = 'It\'s alright.'
print(txt)
print("\n")

print("Backslash:")
txt = "This will insert one \\ (backslash)."
print(txt)
print("\n")

print("New Line:")
txt = "Hello\nWorld!"
print(txt)
print("\n")

print("Carriage Return:")
txt = "Hello\rWorld!"
print(txt)
print("\n")

print("Tab:")
txt = "Hello\tWorld!"
print(txt)
print("\n")

print("Backspace:")
# This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt)
print("\n")

print("Form Feed:")
# Form Feed (FF) erases the entire line:
txt = "Hello \fWorld!"
print(txt)
print("\n")

print("Octal value:")
# A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt)
print("\n")

print("Hex value:")
# A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)
print("\n")
