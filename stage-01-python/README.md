# Stage 1 — Python for Real

## Goal

Build the Python fundamentals needed to understand the Django
codebase I work with.

The focus is not learning Python broadly. These are the
Python concepts that are important for understanding the project.

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
```

📂 `05-modules-imports/`

---

## 6. Type Hints

Understand how Python code communicates expected types.

### Important concepts

- Basic type hints
- `Optional`
- `Dict`
- `List`
- `Any`
- `Generator`
- `Union`
- Function parameter types
- Return types
- Static vs runtime typing

📂 `06-type-hints/`

---

## 7. Decorators

Understand what Python is actually doing when you see:

```python
@something
```

### Important concepts

- Functions as objects
- Functions returning functions
- Decorators
- `@decorator`
- `functools.wraps`
- Django decorators
- Celery decorators

📂 `07-decorators/`

---

## 8. Generators & `yield`

Understand iteration and streaming.

### Important concepts

- Iterable
- Iterator
- `iter()`
- `next()`
- Generators
- `yield`
- Generator expressions
- Generator exhaustion

### Project connection

Understand how `yield` relates to LLM streaming.

📂 `08-generators/`

---

## 9. Context Managers

Understand:

```python
with something():
    ...
```

### Important concepts

- `with`
- Context managers
- `__enter__`
- `__exit__`
- `contextlib`
- Files
- Database transactions
- Locks

📂 `09-context-managers/`

---

## 10. Async / Await

Understand the basics of asynchronous Python.

### Important concepts

- Synchronous vs asynchronous code
- `async def`
- `await`
- Coroutines
- Event loop — conceptually
- Async I/O
- Async Django
- Django Channels
- Async LangChain

### Goal

Be able to read async Python in the project without
getting lost.

📂 `10-async-await/`

---

## 11. Virtual Environments & Poetry

Understand how the project manages Python dependencies.

### Important concepts

- Virtual environments
- `venv`
- Poetry
- `pyproject.toml`
- Dependencies
- Lockfiles
- `poetry install`
- `poetry add`
- `poetry run`

📂 `11-poetry/`

---

# Practice

Don't just watch tutorials.

For important concepts:

1. Learn the concept.
2. Write a small example.
3. Experiment with it.
4. Break it intentionally.
5. Understand why it broke.
6. Find the same concept in the real project.
7. Explain what the project is doing.

---

# Stage 1 Exit Test

Open:

`intelligence/ai_models/services/model_factory.py`

Explain every line out loud.

I should understand:

- Imports
- Classes
- Methods
- `self`
- Type hints
- Control flow
- Exceptions
- Return values
- Why the code is structured this way

If something is still mysterious, identify the Python
concept I need to learn and study that concept.

---

# Key Principle

> Learn the Python concept → find it in the real codebase →
> understand why it is being used.
