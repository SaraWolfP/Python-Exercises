
name = str(input("Insert something:")).strip(" ")
snakecase = ' '

for i in name:
    if i.isupper():
        if i == name[0]:
            snakecase += i.lower()
        else:
            snakecase += "_"+i.lower()
    else:
        snakecase += i


print(snakecase)
print(type(snakecase))
