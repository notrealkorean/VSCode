camel = input("camelCase: ")
final = str()

for char in camel:
    if char.isupper():
        char = "_" + char
    final = final + char.lower()

print(final)