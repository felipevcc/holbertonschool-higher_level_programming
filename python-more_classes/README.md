# Python - More Classes and Objects

## Description

* [`tests/`](./tests) - Main functions provided by Holberton School to test the files.

## Tasks

* **0. Simple rectangle**
  * [`0-rectangle.py`](./0-rectangle.py) - Empty class `Rectangle` that defines a rectangle.
* **1. Real definition of a rectangle**
  * [`1-rectangle.py`](./1-rectangle.py) - Class `Rectangle` that defines a rectangle. Based on `0-rectangle.py` with:
    * Private instance attribute: `width`.
    * Property: `def width(self)` to retrieve `width`.
    * Property setter: `def width(self, value)` to set `width`.
    * Private instance attribute: `height`.
    * Property: `def height(self)` to retrieve `height`.
    * Property setter: `def height(self, value)` to set `height`.
    * Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0)`.
* **2. Area and perimeter**
  * [`2-rectangle.py`](./2-rectangle.py) - Class `Square` that defines a square. Based on `1-rectangle.py` with:
    * Public instance method: `def area(self)` that returns the rectangle area.
    * Public instance method: `def perimeter(self)` that returns the rectangle perimeter.
* **3. String representation**
  * [`3-rectangle.py`](./3-rectangle.py) - Class `Square` that defines a square. Based on `2-rectangle.py` with:
    * Special method `__str__` to print the rectangle with the character `#`.
* **4. Eval is magic**
  * [`4-rectangle.py`](./4-rectangle.py) - Class `Square` that defines a square. Based on `3-rectangle.py` with:
    * Special method `__repr__` to return a string representation of the rectangle to be able to recreate a new instance by using `eval()`.
* **5. Detect instance deletion**
  * [`5-rectangle.py`](./5-rectangle.py) - Class `Square` that defines a square. Based on `4-rectangle.py` with:
    * Special method `__del__` that prints the message `Bye rectangle...` when an instance of `Rectangle` is deleted.
* **6. How many instances**
  * [`6-rectangle.py`](./6-rectangle.py) - Class `Square` that defines a square. Based on `5-rectangle.py` with:
    * Public class attribute `number_of_instances` that is initialized to `0`, incremented for each new instantiation, and decremened for each instance deletion.
* **7. Change representation**
  * [`7-rectangle.py`](./7-rectangle.py) - Class `Square` that defines a square. Based on `6-rectangle.py` with:
    * Public class attribute `print_symbol` that is initialized to `#`, used as symbol for string representation.
* **8. Compare rectangles**
  * [`8-rectangle.py`](./8-rectangle.py) - Class `Square` that defines a square. Based on `7-rectangle.py` with:
    * Static method `def bigger_or_equal(rect_1, rect_2)` that returns the biggest rectangle based on the area.
* **9. A square is a rectangle**
  * [`9-rectangle.py`](./9-rectangle.py) - Class `Square` that defines a square. Based on `8-rectangle.py` with:
    * Class method `def square(cls, size=0)` that returns a new Rectangle instance with `width == height == size`.

## Author
* Felipe Villamizar - [GitHub](https://github.com/felipevcc)
