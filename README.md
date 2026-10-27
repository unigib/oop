# Python OOP Explorer

An interactive desktop application for learning the fundamentals of
object-oriented programming (OOP) in Python. This resource is prepared for
students and teaching activities at the **University of Gibraltar**. It is an
educational example and is not an official University publication.

## About the app

The app uses a vehicle example to make OOP ideas visible and interactive. A
sidebar lists the topics; selecting a topic displays a short explanation and
code sample. Choose **Run this demo** to see a live example in the output area.
The interface includes the supplied University of Gibraltar logo and matching
red accent styling.

The examples use a small class hierarchy:

```text
Vehicle (abstract base class)
└── Car
    └── ElectricCar

Garage (contains Vehicle objects)
```

The app demonstrates:

| Topic | What the example shows |
|---|---|
| Classes and objects | Creating vehicle instances with their own attributes |
| Encapsulation | Reading mileage through a read-only property |
| Inheritance | Reusing `Vehicle` and `Car` behavior in subclasses |
| Polymorphism | Calling `start()` on different vehicle types |
| Abstraction | Requiring concrete vehicle classes to implement `start()` |
| Composition | A `Garage` containing and managing vehicles |
| Class and static methods | Constructing from a dictionary and validating mileage |
| Decorators | Using `@property`, `@staticmethod`, `@classmethod`, and `@abstractmethod` |
| Special methods | Customizing an object's display with `__str__` |

## Requirements

- Python 3.9 or later
- Tkinter, which is included with most standard Python installations

No third-party Python packages are required. If Python reports that `tkinter`
is unavailable, install or enable the Tk support for your Python distribution.

## Run the application

Open a terminal in the project directory and run:

```bash
python oop_demo.py
```

On Windows, if `python` is not the Python 3 command, you can use:

```powershell
py -3 oop_demo.py
```

Select a concept from the left-hand list, read its explanation and example,
then click **Run this demo**. **Clear output** empties the results area.

## Suggested learning activities

1. Run each demonstration and identify the classes, objects, attributes, and
   methods involved.
2. Change a vehicle's make, model, mileage, or battery percentage in the
   relevant example and observe the output.
3. Add a new `Vehicle` subclass that implements its own `start()` method.
4. Add an instance of the new subclass to a `Garage` and consider how
   polymorphism lets the garage use it without knowing its concrete type.
5. Try creating a subclass without implementing `start()` and observe how the
   abstract base class prevents it from being instantiated.

## Project files

- `oop_demo.py` — application, example classes, and interactive demonstrations
- `logo.png` — image asset included in the project

## Educational note

The app is intended as a compact teaching aid. The examples demonstrate core
Python OOP patterns, not every possible OOP design technique. In particular,
Python's leading-underscore convention communicates that an attribute is
internal; it does not make that attribute strictly private.
