print("List Comprehension")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

print("\n")

print('With list comprehension you can do all that with only one line of code:')
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

print("\n")
print("The condition is like a filter that only accpets the items that evaluate to True:")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)

print("\n")

print("With no if statement:")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)

print("\n")
print("You can use the range() function to create an iterable:")
newlist = [x for x in range(10)]
print(newlist)

print("\n")
print("Accept only numbers lower than 5:")
newlist = [x for x in range(10) if x < 5]
print(newlist)

print("\n")
print("Set the values in the new list to upper case:")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)

print("\n")
print("Set all values in the new list to 'hello':")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)

print("\n")
print('Return "orange" instead of "banana":')
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
