# Python - Inheritance

## Description

* [`tests/`](./tests) - Main functions provided by Holberton School to test the files and `.txt` files for testing using `Doctest`.

## Tasks

* **0. Lookup**
  * [`0-lookup.py`](./0-lookup.py) - Function that returns the list of available attributes and methods of an object.
* **1. My list**
  * [`1-my_list.py`](./1-my_list.py) - Class `MyList` that inherits from `list` with:
    * Public instance method `def print_sorted(self)` that prints the list in
    ascending sorted order.
  * [`tests/1-my_list.txt`](./tests/1-my_list.txt) - Test file with `Doctest`.
* **2. Exact same object**
  * [`2-is_same_class.py`](./2-is_same_class.py) - Function that returns `True` if the object is exactly an instance of the specified class ; otherwise `False`.
* **3. Same class or inherit from**
  * [`3-is_kind_of_class.py`](./3-is_kind_of_class.py) - Function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise `False`.
* **4. Only sub class of**
  * [`4-inherits_from.py`](./4-inherits_from.py) - Function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise `False`.
* **5. Geometry module**
  * [`5-base_geometry.py`](./5-base_geometry.py) - Empty class `BaseGeometry`.
* **6. Improve Geometry**
  * [`6-base_geometry.py`](./6-base_geometry.py) - Class `BaseGeometry`. Based on `5-base_geometry.py` with:
    * Public instance method `def area(self)` that raises an `Exception` with the message `area() is not implemented`.
* **7. Integer validator**
  * [`7-base_geometry.py`](./7-base_geometry.py) - Class `BaseGeometry`. Based on `6-base_geometry.py` with:
    * Public instance method `def integer_validator(self, name, value)` that validates the parameter `value`.
    * The parameter `value` must be an `int`, otherwise, a `TypeError` exception is raised with the message `<name> must be an integer`.
    * The parameter `value` must be greater than `0`, otherwise, a `ValueError` exception is raised with the message `<value> must be greater than 0`.
  * [`tests/7-base_geometry.txt`](./tests/7-base_geometry.txt) - Test file with `Doctest`.
* **8. Rectangle**
  * [`8-rectangle.py`](./8-rectangle.py) - Class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`) with:
    * Instantiation with `width` and `height`: `def __init__(self, width, height)`.
    * Private attributes `width` and `height` - validated with `integer_validator`.
* **9. Full rectangle**
  * [`9-rectangle.py`](./9-rectangle.py) - Class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`). Based on `8-rectangle.py` with:
    * Implementation of the method `area()`.
    * Special method `__str__` to print the following rectangle description: `[Rectangle] <width>/<height>`.
* **10. Square #1**
  * [`10-square.py`](./10-square.py) - Class `Square` that inherits from `Rectangle` (`9-rectangle.py`) with:
    * Instantiation with `size`: `def __init__(self, size)`.
    * Private attribute `size` - validated with `integer_validator`.
    * Implementation of the `area()` method.
* **11. Square #2**
  * [`11-square.py`](./11-square.py) - Class `Square` that inherits from `Rectangle` (`9-rectangle.py`). Based on `10-square.py` with:
    * Special method `__str__` to print the square description: `[Square] <width>/<height>`.

## Author
* Felipe Villamizar - [GitHub](https://github.com/felipevcc)