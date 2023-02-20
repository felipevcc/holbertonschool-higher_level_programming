# Python - Input/Output

## Description

* [`tests/`](./tests) - Main functions provided by Holberton School to test the files and `.txt` or `.json` files to manage them.

## Tasks

* **0. Read file**
  * [`0-read_file.py`](./0-read_file.py) - Function that reads a text file (`UTF8`) and prints it to stdout.
* **1. Write to a file**
  * [`1-write_file.py`](./1-write_file.py) - Function that writes a string to a text file (`UTF8`) and returns the number of characters written.
* **2. Append to a file**
  * [`2-append_write.py`](./2-append_write.py) - Function that appends a string at the end of a text file (`UTF8`) and returns the number of characters added.
* **3. To JSON string**
  * [`3-to_json_string.py`](./3-to_json_string.py) - Function that returns the JSON representation of an object (string).
* **4. From JSON string to Object**
  * [`4-from_json_string.py`](./4-from_json_string.py) - Function that returns an object (Python data structure) represented by a JSON string.
* **5.  Save Object to a file**
  * [`5-save_to_json_file.py`](./5-save_to_json_file.py) - Function that writes an Object to a text file, using a JSON representation.
* **6. Create object from a JSON file**
  * [`6-load_from_json_file.py`](./6-load_from_json_file.py) - Function that creates an Object from a “JSON file”.
* **7. Load, add, save**
  * [`7-add_item.py`](./7-add_item.py) - Script that adds all arguments to a Python list, and then save them to a file.
* **8. Class to JSON**
  * [`8-class_to_json.py`](./8-class_to_json.py) - Function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object.
* **9. Student to JSON**
  * [`9-student.py`](./9-student.py) - Class `Student` that defines a student with:
    * Public instance attributes `first_name`, `last_name`, and `age`.
    * Instantiation with `first_name`, `last_name`, and `age`: `def __init__(self, first_name, last_name, age)`.
    * Public method `def to_json(self)` that retrieves a dictionary representation of a `Student` instance.
* **10. Student to JSON with filter**
  * [`10-student.py`](./10-student.py) - Class `Student` that defines a student. Based on `9-student.py` with:
    * Public method `def to_json(self, attrs=None)` that retrieves a dictionary representation of a `Student` instance.
    * If `attrs` is a list of strings, only attribute names contained in this list must be retrieved. Otherwise, all attributes must be retrieved.
* **11. Student to disk and reload**
  * [`11-student.py`](./11-student.py) - Class `Student` that defines a student. Based on `10-student.py` with:
    * Public method `def reload_from_json(self, json)` that replaces all attributes of the `Student` instance using the key/value pairs listed in `json`.
    * The method assumes `json` is a dictionary containing attributes with name/value corresponding to key/value.
* **12. Pascal's Triangle**
  * [`12-pascal_triangle.py`](./12-pascal_triangle.py) - Function that returns a list of lists of integers representing the Pascal’s triangle of `n`.

## Author
* Felipe Villamizar - [GitHub](https://github.com/felipevcc)