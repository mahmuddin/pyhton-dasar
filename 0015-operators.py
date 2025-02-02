print("Python Arithmetic Operators:")
print(10 + 5)  # Addition

x = 5
y = 3
print(x - y)  # Subtraction

x = 5
y = 3
print(x * y)  # Multiplication

x = 12
y = 3
print(x / y)  # Division
x = 5
y = 2
print(x % y)  # Modulus

x = 2
y = 5
print(x ** y)  # same as 2*2*2*2*2

x = 15
y = 2
# the floor division // rounds the result down to the nearest whole number
print(x // y)
print("\n")

print("Python Assignment Operators:")
x = 5
print(x)

x = 5
x += 3
print(x)

x = 5
x -= 3
print(x)

x = 5
x *= 3
print(x)

x = 5
x /= 3
print(x)

x = 5
x %= 3
print(x)

x = 5
x //= 3
print(x)

x = 5
x **= 3
print(x)

# 5: 101
# 3: 011
# Performing the bitwise AND operation:
# 101 (5) & 011 (3) = 001
# So, the result of the bitwise AND operation is 1,
x = 5
x &= 3  # bitwise AND
print(x)

# 5: 101
# 3: 011
# 101 (5) | 011 (3) = 111
# So, the result of the bitwise OR operation is 7,
x = 5
x |= 3  # bitwise OR
print(x)

# 101 (5) ^ 011 (3) = 110
x = 5
x ^= 3  # bitwise XOR
print(x)

# 5: 101
# 101 (5) >> 3 = 000
x = 5
x >>= 3  # right shift
print(x)

x = 5
x <<= 3  # left shift
print(x)

print(x := 3)  # x = 3
print("\n")

print("Python Comparison Operators:")
x = 5
y = 3
print(x == y)  # returns False because 5 is not equal to 3

x = 5
y = 3
print(x != y)  # returns True because 5 is not equal to 3

x = 5
y = 3
print(x > y)  # returns True because 5 is greater than 3

x = 5
y = 3
print(x < y)  # returns False because 5 is not less than 3

x = 5
y = 3
print(x >= y)  # returns True because five is greater, or equal, to 3

x = 5
y = 3
print(x <= y)  # returns False because 5 is neither less than or equal to 3
print("\n")

print("Python Logical Operators:")
x = 5
# returns True because 5 is greater than 3 AND 5 is less than 10
print(x > 3 and x < 10)

x = 5
# returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)
print(x > 3 or x < 4)

x = 5
# returns False because not is used to reverse the result
print(not (x > 3 and x < 10))
print("\n")

print("Python Identity Operators:")
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
# returns True because z is the same object as x
print(x is z)

# returns False because x is not the same object as y, even if they have the same content
print(x is y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y
print(x == y)

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

# returns False because z is the same object as x
print(x is not z)

# returns True because x is not the same object as y, even if they have the same content
print(x is not y)

# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y
print(x != y)
print("\n")

print("Python Membership Operators:")
x = ["apple", "banana"]
# returns True because a sequence with the value "banana" is in the list
print("banana" in x)

x = ["apple", "banana"]
# returns True because a sequence with the value "pineapple" is not in the list
print("pineapple" not in x)
print("\n")

print("Python Bitwise Operators:")
print(6 & 3)
"""
The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""

print(6 | 3)
"""
The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
7 = 0000000000000111
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""

print(6 ^ 3)
"""
The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
5 = 0000000000000101
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""

print(~3)
"""
The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).

Inverted 3 becomes -4:
 3 = 0000000000000011
-4 = 1111111111111100

Decimal numbers and their binary values:
 4 = 0000000000000100
 3 = 0000000000000011
 2 = 0000000000000010
 1 = 0000000000000001
 0 = 0000000000000000
-1 = 1111111111111111
-2 = 1111111111111110
-3 = 1111111111111101
-4 = 1111111111111100
"""

print(3 << 2)
"""
The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off:

If you push 00 in from the left:
 3 = 0000000000000011
becomes
12 = 0000000000001100

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""

print(8 >> 2)
"""
The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.

If you move each bit 2 times to the right, 8 becomes 2:
 8 = 0000000000001000
becomes
 2 = 0000000000000010
Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""
print("\n")

print("Operator Precedence:")
print((6 + 3) - (6 + 3))

"""
Parenthesis have the highest precedence, and need to be evaluated first.
The calculation above reads 9 - 9 = 0
"""

print(100 + 5 * 3)
"""
Multiplication has higher precedence than addition, and needs to be evaluated first.
The calculation above reads 100 + 15 = 115
"""

print(100 + ~3)

"""
Bitwise NOT has higher precedence than addition, and needs to be evaluated first.
The calculation above reads 100 + -4 = 96
"""

print(8 >> 4 - 2)

"""
Bitwise right shift has a lower precedence than subtraction, and we need to calculate the subtraction first.
The calculation above reads 8 >> 2 = 2

More explanation:
The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.

If you move each bit 2 times to the right, 8 becomes 2:
 8 = 0000000000001000
becomes
 2 = 0000000000000010

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""
print(5 + 4 - 7 + 3)

"""
Additions and subtractions have the same precedence, and we need to calculate from left to right.
The calculation above reads:
5 + 4 = 9
9 - 7 = 2
2 + 3 = 5
"""
