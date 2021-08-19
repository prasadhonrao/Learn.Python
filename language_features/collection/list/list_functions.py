# list methods
languages = ["Python", "Scala", "Haskell", "F#"]
print(languages)

# slice
print(languages[0:]) # slice till the end
print(languages[1:3])
print(languages[-1:])

# reverse a list using slice
print(languages[::-1])

# add to list at specific position
languages.insert(1, "C#")
print(languages)

# append to list
languages.append("Clojure")
print(languages)

# extend a list
tools = ["Git", "Vim", "Mercurial", "VSCode"]
languages.extend(tools)
print(languages)

# copy list using slice
functional_languages = languages[:]
print(functional_languages)

# identity and value equality check
print(languages == functional_languages) # equality
print(languages is functional_languages) # identity

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

# remove last element
last_element = languages.pop()
print(last_element)
print(languages)

# remove all elements
languages.clear()
print(languages)