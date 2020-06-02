def headline(text, align=True):
    if align:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50, "o")


print(headline("Dajeee Marco"))
print(headline("Dajeee Marco", align=False))
print(headline("Dajeee Marco", align="left"))


'''
def headline(text: str, align: bool = True) -> str:
    ...
'''

