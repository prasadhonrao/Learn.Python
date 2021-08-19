# dict key can have different data types, including nested dictionary
# dict keys are immutable and must be unique
# dict values are mutable

customers = { 
    1: 'Prasad', 
    2: 'Scott', 
    3: 'John',
    "four": 'Bill',
}
print(type(customers))
print(customers)
print(customers[1])
print("Dictionary length is {0}".format(len(customers)))
print(customers.keys()) # get all keys
print(customers.values()) # get all values
print(customers.items()) # get all keys and values

# declear a dictionary using dict()
premium_customers = dict(name='John', age=25, address='New York')
print(premium_customers)

# use get method to get a value using key, and pass default value if key doesn't exists in the dictionary
first = customers.get('11', 'unknown value')
print(first)

# add new key to dictionary
customers['5'] = "Clojure"
first = customers.get('11', 'unknown value')
print(first)

# --------------------------------------------------------------------------------------------
# combining dictionary and list

dictionaryList = [
    {"firstName": "Prasad", "lastName": "Honrao"},
    {"firstName": "Scott", "lastName": "Hanselman"},
    {"firstName": "Bill", "lastName": "Gates"}
]

print(dictionaryList)

# Dictionary of dictionaries
europe = {
    'spain': { 'capital':'madrid', 'population':46.77 },
    'france': { 'capital':'paris', 'population':66.03 },
    'germany': { 'capital':'berlin', 'population':80.62 },
    'norway': {'capital': 'oslo', 'population': 5.084}
}

# Print out the capital of France
print(europe['france']['capital'])

# Create sub-dictionary data
data = {'capital':'', 'population':0}

# Add data to europe under key 'italy'
europe['italy'] = data
print(europe)