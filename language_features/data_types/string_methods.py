# Commonly used methods
print("python is a dynamic language".capitalize() )
print("python".replace("p","j"))
print("python".isalpha())
print("python".isdigit())
print("123".isdigit())
print("python3.6".isdigit())
print(("red, green, blue").split(","))

# string interpolation
language = "Python"
strength = "powerful"
print("{0} is a {1} language".format(language, strength))
print(f"{language} is a {strength} language")