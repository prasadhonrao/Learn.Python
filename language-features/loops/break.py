languages = ["Python", "Scala", "Haskell", "F#", "C#", "JavaScript"]

for lang in languages:
    if (lang == "Haskell"):
        print("Found Haskell !!!", end='\n')
        break
    print(lang, end=' ')