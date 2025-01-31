x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(x)
print(y)
print(z)


x = 5
y = "John"
print(type(x))
print(type(y))

x = "John"
print(x)
# is the same as
x = 'John'
print(x)

a = 4
A = "Sally"
# A will not overwrite a
print(a)

print("Many values to Multiple Variables print")
x, y, z = "Orange", "Apple", "Banana"
print(x)
print(y)
print(z)

print("One Value to Multiple Variables print")
x = y = z = "Orange"
print(x)
print(y)
print(z)

print("Unpack Collections")
fruits = ["Apple", "Orange", "Banana"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output Variables
x = "Python is awesome"
print(x)

print("Output Multiple Variables")
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

print("Output Multiple Variables")
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

print("Output Multiple Variables")
x = 5
y = 10
print(x + y)

print("Output Multiple Variables")
x = 5
y = "John"
print(x, y)

print("Global Variables")
x = "awesome"


def myFunc():
    print("Pyhton is " + x)


myFunc()

print("Local Variables")
x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)


myfunc()

print("Python is " + x)

print("Global keyword")


def myFunc():
    global x
    x = "fantastic"


myFunc()
print("Python is " + x)

print("Global keyword 2")
x = "awesome"


def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)
