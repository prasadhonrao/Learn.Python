# list - mutable sequence of objects

# declaration
languages = ["Python", "Scala", "Haskell", "F#"]
print(languages)

# multiline declaration 
languages = ['Python',
             'Scala',
             'Haskell',
             'F#']
print (languages)

# declaration using list constructor
name = list("PYTHON")
print(name)

# iterate through the list
for i in languages:
    print(i, end=' -- ')
print(' ')

# list length
print("number of chars in PYTHON : {0}".format(len(list("PYTHON"))))

# create a list from string
s = "Python is one of the most powerful programming language".split()
print(s)