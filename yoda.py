import random,ast


def masterYoda():
    quot = []
    with open('quotes.txt', 'r') as f:
        s = f.read()
        a = ast.literal_eval(s)
        for i in a:
            quot.append(i)
        print(random.choice(quot))
            

print("\n")
masterYoda()

