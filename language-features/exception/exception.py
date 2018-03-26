student = {
    "firstName": "Prasad",
    "lastName": "Honrao",
    "age": 37
}

try:
    #try to get wrong value from dictionary
    last_name = student["last_name"]
except KeyError as error:
    print("Exception thrown!")
    print(error)

print("Done!")