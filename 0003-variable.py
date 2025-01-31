x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(x)
print(y)
print(z)
print("\n")


x = 5
y = "John"
print(type(x))
print(type(y))
print("\n")

x = "John"
print(x)
# is the same as
x = 'John'
print(x)
print("\n")

a = 4
A = "Sally"
# A will not overwrite a
print(a)
print("\n")

print("Many values to Multiple Variables print:")
x, y, z = "Orange", "Apple", "Banana"
print(x)
print(y)
print(z)
print("\n")

print("One Value to Multiple Variables print:")
x = y = z = "Orange"
print(x)
print(y)
print(z)
print("\n")

print("Unpack Collections:")
fruits = ["Apple", "Orange", "Banana"]
x, y, z = fruits
print(x)
print(y)
print(z)
print("\n")

# Output Variables
x = "Python is awesome"
print(x)
print("\n")

print("Output Multiple Variables:")
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
print("\n")

print("Output Multiple Variables:")
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
print("\n")

print("Output Multiple Variables:")
x = 5
y = 10
print(x + y)
print("\n")

print("Output Multiple Variables:")
x = 5
y = "John"
print(x, y)
print("\n")

print("Global Variables:")
x = "awesome"
print("\n")


def myFunc():
    print("Pyhton is " + x)


myFunc()
print("\n")

print("Local Variables:")
x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)


myfunc()

print("Python is " + x)
print("\n")


print("Global keyword:")


def myFunc():
    global x
    x = "fantastic"


myFunc()
print("Python is " + x)
print("\n")

print("Global keyword 2:")
x = "awesome"


def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)
