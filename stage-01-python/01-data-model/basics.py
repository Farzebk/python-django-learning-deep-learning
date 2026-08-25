# Python Data Model — Basics

# Lists
skills = ["Python", "Django", "SQL"]

# Tuples
coordinates = (19.87, 75.34)

# Sets
unique_skills = {"Python", "Django", "Python"}

# Dictionaries
developer = {
    "name": "Developer",
    "skills": skills,
}

# List comprehension
uppercase_skills = [skill.upper() for skill in skills]

# Dictionary comprehension
skill_lengths = {
    skill: len(skill)
    for skill in skills
}

print("Skills:", skills)
print("Coordinates:", coordinates)
print("Unique skills:", unique_skills)
print("Developer:", developer)
print("Uppercase:", uppercase_skills)
print("Skill lengths:", skill_lengths)
