print("Loop Through a List")
print("Print all items in the list, one by one:")
thelist = ["apple", "banana", "cherry"]
for item in thelist:
    print(item)

print("\n")

print("Loop Through the Index Numbers")
print("Print all items by referring to their index number:")
thelist = ["apple", "banana", "cherry"]
for i in range(len(thelist)):
    print(thelist[i])

print("\n")
print("Using a While Loop")
print("Print all items, using a while loop to go through all the index numbers:")
thelist = ["apple", "banana", "cherry"]
i = 0
while i < len(thelist):
    print(thelist[i])
    i += 1

print("\n")
print("Looping Using List Comprehension")
print("A short hand for loop that will print all items in alist:")
thislist = ["apple", "banana", "cherry"]
[print(item) for item in thislist]
