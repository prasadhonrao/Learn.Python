programming_languages = ["Python", "Scala", "Haskell", "F#", "C#", "JavaScript"]

for lang in programming_languages:
    if (lang == "Haskell"):
        print("Found Haskell !!!", end='\n')
        break
    print(lang, end=' ')


# Another example to use break in for loop
number_of_attempts = 0

for _ in range(10):
    if (int(input()) % 7 == 0):
        print("Got you!")
        break
    number_of_attempts = number_of_attempts + 1

if number_of_attempts == 10:
    print("All attempts finished")
