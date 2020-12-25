camel = input()
result = ""
for _ in camel:
    if _.islower():
        result += _
    elif _.isupper():
        if camel.find(_) > 0:
            result += "_"
        result += _.lower()
print(result)