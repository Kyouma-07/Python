# Creating a dictionary to store information about a person
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "email": "alice@example.com"
}

# Accessing values using keys
print("Name:", person["name"])
print("Age:", person["age"])
print("City:", person["city"])
print("Email:", person["email"])

# Modifying a value
person["age"] = 31

# Adding a new key-value pair
person["job"] = "Engineer"

# Iterating through the dictionary
print("\nDictionary items:")
for key, value in person.items():
    print(key + ":", value)
