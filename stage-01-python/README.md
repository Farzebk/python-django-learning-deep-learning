# Stage 1 — Python for Real

## Goal

Build the Python fundamentals needed to understand the
Django codebase I work with.

The focus is not learning Python broadly. These are the
Python concepts that are important for understanding the
project.

---

## 1. Data Model

Understand how Python's core data structures and objects work.

### Important concepts

- Lists
- Dictionaries
- Sets
- Tuples
- Mutability
- Immutability
- Object references
- `==` vs `is`
- Truthiness
- `None`
- Indexing and slicing
- Unpacking
- `*` unpacking
- List comprehensions
- Dictionary comprehensions
- Set comprehensions
- Nested data structures
- Shallow vs deep copy

### Why it matters

These concepts appear constantly when working with Django,
JSON/API data, services, and database results.

📂 `01-data-model/`

---

## 2. Functions

Understand how Python functions behave and how arguments
are passed.

### Important concepts

- Function parameters
- Positional arguments
- Keyword arguments
- Default arguments
- `*args`
- `**kwargs`
- Keyword-only arguments
- Return values
- Functions as objects
- Scope
- Mutable default argument trap

### Why it matters

Functions are everywhere in Django views, services,
utilities, callbacks, and decorators.

📂 `02-functions/`

---

## 3. Classes

Understand Python's object-oriented model.

### Important concepts

- Classes and objects
- `__init__`
- `self`
- Instance attributes
- Instance methods
- Class attributes
- Inheritance
- Method overriding
- `super()`
- `@classmethod`
- `@staticmethod`
- `@property`

### Why it matters

The project is service-class heavy. Understanding classes
is essential for reading the backend.

📂 `03-classes/`

---

## 4. Exceptions

Understand how Python handles errors.

### Important concepts

- `try`
- `except`
- `else`
- `finally`
- `raise`
- Built-in exceptions
- Custom exceptions
- Exception inheritance
- Reading tracebacks

### Project connection

Understand why `ImproperlyConfigured` is used in
`model_factory.py`.

📂 `04-exceptions/`

---

## 5. Modules & Imports

Understand how Python organizes and loads code.

### Important concepts

- Modules
- Packages
- `__init__.py`
- Absolute imports
- Relative imports
- Import paths
- Circular imports

Example:

```python
from ..models import AIModel
