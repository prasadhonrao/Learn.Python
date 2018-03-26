languages = ["Python", "Scala", "Haskell", "F#", "C#", "JavaScript"]

for lang in languages:
    if (lang == "Haskell"):
        continue
        print("Found Haskell !!!", end='\n') # this statement will never be executec
    print(lang, end=' ')