#!/usr/bin/python3
add_attribute = __import__('101-add_attribute').add_attribute


class MyClass():
    pass


mc = MyClass()
add_attribute(mc, "name", "John")
print(mc.name)

try:
    a = "My String"
    add_attribute(a, "name", "Bob")
    print(a.name)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))



Checking for area failure:
	 >>> test = BaseGeometry()
	 >>> test.area()
	 Traceback (most recent call last):
	 ...
	 Exception: area() is not implemented

Checking too many arguments for area:
	 >>> test.area(1)
	 Traceback (most recent call last):
         ...
	 TypeError: area() takes 1 positional argument but 2 were given

Checking integer validator for passing integer:
	 >>> test.integer_validator("integer", 1)

Checking for integer == 0:
	 >>> test.integer_validator("integer", 0)
	 Traceback (most recent call last):
         ...
         ValueError: integer must be greater than 0

Checking for integer < 0;
	 >>> test.integer_validator("integer", -5)
	 Traceback (most recent call last):
         ...
         ValueError: integer must be greater than 0

Checking for non-integer types:
	 >>> test.integer_validator("float", 1.5)
         Traceback (most recent call last):
         ...
         TypeError: float must be an integer
	 >>> test.integer_validator("complex", complex(1, 1))
         Traceback (most recent call last):
         ...
         TypeError: complex must be an integer
	 >>> test.integer_validator("string", "hello")
         Traceback (most recent call last):
         ...
         TypeError: string must be an integer
	 >>> test.integer_validator("tuple", (1, 2))
         Traceback (most recent call last):
         ...
         TypeError: tuple must be an integer
	 >>> test.integer_validator("list", [1, 2, 3])
	 Traceback (most recent call last):
         ...
         TypeError: list must be an integer
	 >>> test.integer_validator("dict", {"key": "value"})
         Traceback (most recent call last):
         ...
         TypeError: dict must be an integer
	 >>> test.integer_validator("set", {"hello", "world"})
         Traceback (most recent call last):
         ...
         TypeError: set must be an integer
	 >>> test.integer_validator("frozenset", frozenset(["hello", "world"]))
         Traceback (most recent call last):
         ...
         TypeError: frozenset must be an integer
	 >>> test.integer_validator("bytes", b"bytes")
         Traceback (most recent call last):
         ...
         TypeError: bytes must be an integer
	 >>> test.integer_validator("bytearrays", bytearray(b"bytes"))
         Traceback (most recent call last):
         ...
         TypeError: bytearrays must be an integer

Checking for no arguments to integer_validator:
	 >>> test.integer_validator()
	 Traceback (most recent call last):
         ...
	 TypeError: integer_validator() missing 2 required positional arguments: 'name' and 'value'

Checking for only 1 argument to integer_validator:
	 >>> test.integer_validator("integer")
	 Traceback (most recent call last):
         ...
	 TypeError: integer_validator() missing 1 required positional argument: 'value'

Checking for too many arguments:
	 >>> test.integer_validator("integer", 1, 2)
	 Traceback (most recent call last):
         ...
	 TypeError: integer_validator() takes 3 positional arguments but 4 were given
