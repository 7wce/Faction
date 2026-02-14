import string
import random

letters = string.ascii_letters.lower()
numbers = "1234567890"

def gen(option):
    if option.lower() == "four":
        fiveletter = ''.join(random.choice(letters.lower()) for _ in range(4))
        return fiveletter
    elif option.lower() == "five":
        fiveletter = ''.join(random.choice(letters.lower()) for _ in range(5))
        return fiveletter
    elif option.lower() == "words":
        return None
    elif option.lower() == "random":
        fiveletter = ''.join(random.choice(letters.lower()) for _ in range(8))
        return fiveletter
    elif option.lower() == "lnb":
        chars = [
            random.choice(letters.lower()),
            random.choice(letters.lower()),
            random.choice(numbers),
            random.choice(numbers),
        ]

        random.shuffle(chars)
        return ''.join(chars)