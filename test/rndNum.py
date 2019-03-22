import random


def rndChar():
    return chr(random.randint(65,90))

def rndCode():
    i = 0
    code = ''
    yield code
    while (i<200) :
        for j in random(6):
            code += rndChar()


print(next(code))
print([rndChar()])