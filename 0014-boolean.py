print(10 > 9)
print(10 == 9)
print(10 < 9)
print("\n")


a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

print(bool("Hello"))
print(bool(15))
print("\n")

# Almost any value is evaluated to True if it has some sort of content.

# Any string is True, except empty strings.

# Any number is True, except 0.

# Any list, tuple, set, and dictionary are True, except empty ones.
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
print("\n")

print("Some Values are False:")
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
print("\n")


class myClass():
    def __len__(self):
        return 0


myobj = myClass()
print(bool(myobj))
print("\n")

print("Functions can Return a Boolean:")


def myFunction():
    return True


print(myFunction())
print("\n")


def myFunction():
    return True


if myFunction():
    print("YES!")
else:
    print("NO!")

x = 200
print(isinstance(x, int))
