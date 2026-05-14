import random
r = random.randint(1, 5)

def helloworld(text: str) -> str:
    if r == 1:
        print("Hello world!")
        return "Hello World!"
    else:
        print(text)
        return text
