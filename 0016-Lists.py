thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

list1 = ["abc", 34, True, 40, "male"]
print(list1)

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

print("Using the list() constructor to make a List:")
thislist = list(("apple", "banana", "cherry"))
print(thislist)
print("\n")

print("Access Items:")
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# This will return the items from position 2 to 5.
# Remember that the first item is position 0,
# and note that the item in position 5 is NOT included
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# This example returns the items from the beginning to, but NOT including, "kiwi":
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# This will return the items from index 2 to the end.
# Remember that index 0 is the first item, and index 2 is the third
print(thislist[2:])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
print(thislist[-4:-1])

thislist = ["apple", "banana", "cherry"]
# Check if "apple" is present in the list:
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

print("\n")

print("Python - Change List Items:")
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]\
    # Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
# Change the second value by replacing it with two new values:
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
# Change the second and third value by replacing it with one value:
thislist[1:3] = ["watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")  # Insert "watermelon" as the third item:
print(thislist)

print("To add an item to the end of the list, use the append() method:")
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

print("Insert an item as the second position:")
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")  # Insert an item as the second position:
print(thislist)

print("Add the elements of tropical to thislist:")
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

print("Add elements of a tuple to a list:")
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

print('Remove "banana":')
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

print('Remove the first occurrence of "banana":')
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

print("Remove the second item:")
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

print("Remove the last item:")
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

print("Remove the first item:")
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

print("Delete the entire list:")
thislist = ["apple", "banana", "cherry"]
del thislist

# The clear() method empties the list.
# The list still remains, but it has no content.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
