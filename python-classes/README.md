# Python - Classes and Objects

## Description

* [`tests/`](./tests) - Main functions provided by Holberton School to test the files.

## Tasks

* **0. My first square**
  * [`0-square.py`](./0-square.py) - Empty class `Square` that defines a square.
* **1. Square with size**
  * [`1-square.py`](./1-square.py) - Class `Square` that defines a square. Based on `0-isquare.py` with:
    * Private instance attribute: `size`
    * Instantiation with `size`
* **2. Size validation**
  * [`2-square.py`](./2-square.py) - Class `Square` that defines a square. Based on `1-square.py` with:
    * Instantiation with optional `size`: `def __init__(self, size=0)`
    * If a provided `size` attribute is not an integer, a `TypeError` exception is raised with the message `must be an integer`.
    * If a provided `size` attribute is less than `0`, a `ValueError` exception is raised with the message `size must be >= 0`.
* **3. Area of a square**
  * [`3-square.py`](./3-square.py) - Class `Square` that defines a square. Based on `2-square.py` with:
    * Public instance attribute `def area(self)` that returns the current square area.
* **4. Access and update private attribute**
  * [`4-square.py`](./4-square.py) - Class `Square` that defines a square. Based on `3-square.py` with:
    * Property `def size(self):` to retrieve the private instance attribute `self`.
    * Property setter `def size(self, value):` to set `self`.
* **5. Printing a square**
  * [`5-square.py`](./5-square.py) - Class `Square` that defines a square. Based on `4-square.py` with:
    * Public instance method `def my_print(self):` that prints the square with the character `#` to standard output (if `size` == 0 -> prints an empty line).
* **6. Coordinates of a square**
  * [`6-square.py`](./6-square.py) - Class `Square` that defines a square. Based on `5-square.py` with:
    * Private instance attribute `position`.
    * Property `def position(self):` to retreive `position`.
    * Property setter `def position(self, value):` to set `position`.
    * Instantiation with optional `size` and `position`: `def __init__(self, size=0, position=(0, 0))`
    * If a provided `position` attribute is not a tuple of two integers, a `TypeError` exception is raised with the message `position must be a tuple of 2 positive integers`.

## Author
* Felipe Villamizar - [GitHub](https://github.com/felipevcc)
