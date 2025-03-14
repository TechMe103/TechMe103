student = {
    "name": "Sanika",
    "Sub": {
        "chem": 97,
        "phy": 98,
        "maths": 98
    }
}

print(list(student.keys())) # Corrected
print(len(list(student.keys()))) # Added parentheses
print(student.values()) # Corrected
print(student.items()) # Corrected
print(student["name"]) # Corrected
print(student.get("name")) # Corrected

# No need to print the update method as it returns None
student.update({"city": "Delhi"})

# Alternatively, you can use a new dictionary to update:
new_dict = {"city": "Delhi"}
student.update(new_dict)

print(student) # Corrected
