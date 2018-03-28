languages = ["Python", "Scala", "Haskell", "F#", "C#", "JavaScript"]

for lang in languages:
    if (lang == "Haskell"):
        print("Found Haskell !!!", end='\n')
        break
    print(lang, end=' ')

# Another example to break continuous loop using a condition
while True:
    response = input()
    if (int(response) % 7 == 0):
        break