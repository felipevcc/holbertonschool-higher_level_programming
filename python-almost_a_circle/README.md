# Python - Almost a circle

This project was developed in object-oriented programming with three classes, a base and two other subclasses to represent rectangles and squares. Tests were also created for all classes using the `unittest` module.

This project contains these topics:
* Imports
* Exceptions
* Private attributes
* Getter/setter
* Class/static methods
* Inheritance
* File I/O
* *args and **kwargs
* JSON serialization/deserialization
* Unittesting

[`main_files/`](./main_files) - Main functions provided by Holberton School to test the files.

## Tests

* [`tests/test_models/`](./tests/test_models): Test files using `unittest`:
  * [`test_base.py`](./tests/test_models/test_base.py)
  * [`test_rectangle.py`](./tests/test_models/test_rectangle.py)
  * [`test_square.py`](./tests/test_models/test_square.py)

## Classes

<details close>
<summary> <strong> Base </strong> </summary>

[`base.py`](./models/base.py) - Represents the "base" class for all other classes in the project. Includes:

* Private class attribute `__nb_objects = 0`.
* Public instance attribute `id`.
* Class constructor `def __init__(self, id=None)`.
  * If `id` is `None`, increments `__nb_objects` and assigns its value to the public instance attribute `id`.
  * Otherwise, sets the public instance attribute `id` to the provided `id`.
* Static method `def to_json_string(list_dictionaries)` that returns the JSON string representation of `list_dictionaries`.
  * If `list_dictionaries` is `None` or empty, returns the string `"[]"`.
* Class method `def save_to_file(cls, list_objs)` that writes the JSON string representation of `list_objs` to a file.
  * The parameter `list_objs` is a list of instances who inherits of `Base`.
  * If `list_objs` is `None`, saves an empty list.
  * The file is saved with the name `<classname>.json`.
  * Overwrites the file if it already exists.
* Static method `def from_json_string(json_string)` that returns the list of the JSON string representation `json_string`.
  * The parameter `json_string` is a string representing a list of dictionaries.
  * If `json_string` is `None` or empty, the function returns an empty list.
* Class method `def create(cls, **dictionary)` that returns an instance with all attributes already set.
  * Instantiates an object with the attributes given in `**dictionary`.
* Class method `def load_from_file(cls)` that returns a list of instances.
  * Reads from the JSON file `<classname>.json`.
  * If the file doesn't exist, the function returns an empty list.

</details>


<details close>
<summary> <strong> Rectangle </strong> </summary>

[`rectangle.py`](./models/rectangle.py) - Represents a rectangle. Inherits from `Base` with:

* Private instance attributes `__width`, `__height`, `__x`, and `__y`.
  * Each private instance attribute features its own getter/setter.
* Class constructor `def __init__(self, width, height, x=0, y=0, id=None)`.
  * If either of `width`, `height`, `x`, or `y` is not an integer, raises a `TypeError` exception with the message `<attribute> must be an integer`.
  * If either of `width` or `height` is <= 0, raises a `ValueError` exception with the message `<attribute> must be > 0`.
  * If either of `x` or `y` is less than 0, raises a `ValueError` exception with the message `<attribute> must be >= 0`.
* Public method `def area(self)` that returns the area of the `Rectangle` instance.
* Public method `def display(self)` that prints the `Rectangle` instance to `stdout` using the character `#`.
  * Prints new lines for the `y` coordinate and spaces for the `x` coordinate.
* Overwrite the `__str__` method to returns a `Rectangle` instance in the format `[Rectangle] (<id>) <x>/<y> - <width>/<height>`.
* Public method `def update(self, *args, **kwargs)` that updates an instance of a `Rectangle` with the given attributes.
  * `*args` is supplied in the following order:
    * 1st: `id`.
    * 2nd: `width`.
    * 3rd: `height`.
    * 4th: `x`.
    * 5th: `y`.
  * `**kwargs` is a dictionary of new key/value attributes to update the `Rectangle` instance.
  * `**kwargs` is skipped if `*args` exists.
* Public method `def to_dictionary(self)` that returns the dictionary representation of a `Rectangle` instance.

</details>


<details close>
<summary> <strong> Square </strong> </summary>

[`square.py`](./models/square.py) - Represents a square. Inherits from `Rectangle` with:

* Class constructor `def __init__(self, size, x=0, y=0, id=None)`.
  * The `width` and `height` of the `Rectangle` superclass are assigned using the value of `size`.
* Overwrite the `__str__` method to print a `Square` instance in the format `[Square] (<id>) <x>/<y> - <size>`.
* Public method `def update(self, *args, **kwargs)` that updates an instance of a `Square` with the given attributes.
  * `*args` must be supplied in the following order:
    * 1st: `id`.
    * 2nd: `size`.
    * 3rd: `x`.
    * 4th: `y`.
  * `**kwargs` is a dictoinary of new key/value attributes to update the `Square` instance.
  * `**kwargs` is skipped if `*args` exists.
* Public method `def to_dictionary(self)` that returns the dictionary representation of a `Square` instance.

</details>

## Author
* Felipe Villamizar - [GitHub](https://github.com/felipevcc)
