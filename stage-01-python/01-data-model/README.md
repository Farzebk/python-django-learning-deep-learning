# Python Data Model

## Goal

Understand how Python's core data structures and objects work.

The goal is not just to know the syntax, but to understand what
Python is doing when data is assigned, modified, compared, copied,
or passed between functions.

---

# 1. Python Objects & Variables

Understand the basic object model behind Python variables.

### Learn

- Objects
- Variables
- References
- Assignment
- `type()`
- `id()`

### Questions I should be able to answer

- What is a Python object?
- What is a variable?
- What happens when I assign one variable to another?
- What does `id()` represent?
- What does `type()` tell me?

📄 `01-basics.py`

---

# 2. Lists

Understand Python's most commonly used mutable collection.

### Learn

- Creating lists
- Indexing
- Adding and removing items
- Iterating
- List methods
- Mutable behavior

### Questions I should be able to answer

- Why can a list be modified?
- What happens when two variables reference the same list?
- What is the difference between `append()` and `extend()`?

📄 `02-lists.py`

---

# 3. Tuples

Understand immutable sequence objects.

### Learn

- Creating tuples
- Indexing
- Unpacking
- Immutability
- When tuples are useful

### Questions I should be able to answer

- Why can't I modify a tuple?
- Can a tuple contain mutable objects?
- When would I use a tuple instead of a list?

📄 `03-tuples.py`

---

# 4. Dictionaries

Understand key-value data structures used heavily in APIs,
configuration, and Django code.

### Learn

- Keys and values
- Creating dictionaries
- Accessing values
- `.get()`
- `.keys()`
- `.values()`
- `.items()`
- Updating dictionaries
- Nested dictionaries

### Questions I should be able to answer

- What can be used as a dictionary key?
- What's the difference between `dict[key]` and `dict.get(key)`?
- How do I safely access optional data?

📄 `04-dictionaries.py`

---

# 5. Sets

Understand collections of unique values.

### Learn

- Creating sets
- Unique values
- Adding and removing values
- Membership
- Union
- Intersection
- Difference

### Questions I should be able to answer

- Why does a set remove duplicates?
- When would a set be better than a list?

📄 `05-sets.py`

---

# 6. Mutability & Immutability

Understand one of the most important parts of Python's object
behavior.

### Learn

- Mutable objects
- Immutable objects
- Lists
- Dictionaries
- Sets
- Tuples
- Strings
- Integers
- Assignment vs modification

### Questions I should be able to answer

- What does mutable actually mean?
- Why does modifying one variable sometimes change another?
- Which common Python objects are mutable?
- Which common Python objects are immutable?

📄 `06-mutability.py`

---

# 7. Object References

Understand how variables refer to objects in memory.

### Learn

- Variables as references
- Multiple references to one object
- Assignment
- Passing objects around
- Assignment vs copying

### Questions I should be able to answer

- What actually happens with `a = b`?
- Why can changing `b` affect `a`?
- Does assigning a list create a new list?

📄 `07-object-references.py`

---

# 8. Equality vs Identity

Understand the difference between comparing values and
comparing object identity.

### Learn

- `==`
- `is`
- Equality
- Identity
- `id()`

### Questions I should be able to answer

- What does `==` compare?
- What does `is` compare?
- When should I use `is`?
- Why is `is None` commonly used?

Example:

```python
a == b
a is b
```

📄 `08-equality-identity.py`

---

# 9. Truthiness & None

Understand how Python evaluates objects in conditions.

### Learn

- Truthy values
- Falsy values
- `None`
- `is None`
- `is not None`
- Boolean context

### Common falsy values

```text
False
None
0
""
[]
{}
set()
()
```

### Questions I should be able to answer

- Why does `if []:` evaluate to false?
- Why use `is None` instead of `== None`?
- How does truthiness affect Django code?

📄 `09-truthiness-none.py`

---

# 10. Indexing & Slicing

Understand how Python accesses parts of sequences.

### Learn

- Positive indexes
- Negative indexes
- Slicing
- Slice start
- Slice stop
- Slice step

### Practice

```python
items[0]
items[-1]
items[1:4]
items[:3]
items[::2]
```

### Questions I should be able to answer

- What happens when an index doesn't exist?
- How does slicing differ from indexing?
- Does slicing modify the original list?

📄 `10-indexing-slicing.py`

---

# 11. Unpacking

Understand how Python assigns multiple values at once.

### Learn

- Basic unpacking
- Multiple assignment
- `*` unpacking
- Nested unpacking

### Practice

```python
first, second = values
```

```python
first, *middle, last = values
```

### Questions I should be able to answer

- What happens if the number of values doesn't match?
- What does `*` do during unpacking?
- Where does unpacking appear in real Python code?

📄 `11-unpacking.py`

---

# 12. Comprehensions

Understand Python's concise syntax for building collections.

### Learn

- List comprehensions
- Dictionary comprehensions
- Set comprehensions
- Conditions
- Nested comprehensions

### Practice

```python
[x * 2 for x in numbers]
```

```python
[x for x in numbers if x > 10]
```

```python
{name: len(name) for name in names}
```

### Questions I should be able to answer

- How does a comprehension compare to a normal loop?
- When does a comprehension improve readability?
- When is a normal loop better?
- When does a nested comprehension become difficult to read?

📄 `12-comprehensions.py`

---

# 13. Nested Data Structures

Understand data structures that contain other data structures.

### Learn

- Lists containing dictionaries
- Dictionaries containing lists
- Nested dictionaries
- Lists of dictionaries
- JSON-like structures
- Accessing nested data

Example:

```python
users = [
    {
        "name": "John",
        "skills": ["Python", "Django"]
    }
]
```

### Questions I should be able to answer

- How do I access nested data?
- How do I safely access optional nested values?
- Where do these structures appear in APIs?
- How does this relate to Django and LLM responses?

📄 `13-nested-data.py`

---

# 14. Copying

Understand the difference between references, shallow copies,
and deep copies.

### Learn

- Assignment
- Shallow copy
- Deep copy
- `copy.copy()`
- `copy.deepcopy()`
- Nested mutable objects

### Questions I should be able to answer

- Does assigning a list create a copy?
- Does `list.copy()` copy nested objects?
- When do I need `deepcopy()`?
- Why does copying matter with nested dictionaries and lists?

📄 `14-copying.py`

---

# 15. Practice

This file should contain exercises combining the concepts
from the entire Data Model section.

### Practice should include

- Lists
- Dictionaries
- Sets
- Tuples
- Mutability
- Object references
- `==` vs `is`
- Truthiness
- `None`
- Indexing and slicing
- Unpacking
- Comprehensions
- Nested data
- Copying

### Rule

Do not look at previous solutions while solving the practice
problems.

First predict the output, then run the code and explain why
the result occurred.

📄 `15-practice.py`

---

# 🔎 Django / Project Connection

After learning each concept, find where it appears in the
real Django codebase.

Look for:

- Lists passed between services
- Dictionaries representing API data
- Nested JSON
- `.get()` calls
- `None` checks
- Truthy/falsy checks
- List comprehensions
- Dictionary comprehensions
- Unpacking
- Mutable objects
- Copies of data

For each useful example, try to answer:

1. What Python concept is being used?
2. What is the code doing?
3. Why is this data structure appropriate here?
4. What would happen if the data changed?
5. Could the code behave differently because of mutability
   or object references?

The goal is:

> Learn the concept → find it in the real codebase →
> understand why it is being used.

---

# 🧪 Practice Method

For important concepts:

1. Learn the concept.
2. Write a small example yourself.
3. Predict what the code will do.
4. Run it.
5. Intentionally change or break it.
6. Understand why the behavior changed.
7. Find the same concept in the real project.
8. Explain the project code in your own words.

Do not use the practice files as a place to copy tutorial
examples. They should contain experiments that helped me
understand the concept.

---

# 🏁 Final Understanding Test

Before considering the Data Model section understood, I should
be able to explain:

1. What a Python object is
2. How variables reference objects
3. Mutable vs immutable objects
4. `==` vs `is`
5. Truthy vs falsy values
6. `None`
7. Lists vs tuples vs sets vs dictionaries
8. Indexing and slicing
9. Unpacking
10. Comprehensions
11. Nested data structures
12. Shallow vs deep copying

I should also be able to predict the output of unfamiliar
examples before running them.

---

# 🔗 Connection to the Django Codebase

The concepts in this section should eventually help me read
and understand code such as:

```text
intelligence/ai_models/services/model_factory.py
```

When I encounter a list, dictionary, comprehension, `None`
check, unpacking, or object passed between services, I should
understand what Python is doing without needing AI to explain
the basic language behavior.

---

# Key Principle

> Don't memorize Python behavior.
>
> Predict it, run it, explain it, and then find it in the
> real codebase.
