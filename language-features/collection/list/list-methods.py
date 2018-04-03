# list methods
languages = ["Python", "Scala", "Haskell", "F#"]
print(languages)

#slice
print(languages[0:]) #slice till the end
print(languages[1:3])
print(languages[-2:])

# reverse a list using slice
print(languages[::-1])

# append to list
languages.append("Clojure")
print(languages)

# copy list using slice
functional_languages = languages[:]
print(functional_languages)

print(languages == functional_languages)
print(languages is functional_languages)

# copy list using copy
functional_languages = languages.copy()

# copy list using constructor
functional_languages = list(languages)

# element exists check
print("Python" in languages)
print("C#" in languages)

# delete an element
del languages[0]
print("Python exist? {0}".format("Python" in languages))

