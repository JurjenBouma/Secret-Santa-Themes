import random

themes = [
    "Gróóóót!",
    "Net een James Bond film",
    "Spreekwoorden",
    "Frylân Boppe!",
    "Super fout, maar wel leuk",
    "Suriname",
    "Zuipen!",
    "Ik wil CHOCOLADE!",
    "Boerderij",
    "Puur Bouma",
    "Australië",
    "Kinderachtig",
]


def get_rnd_theme():
    result = ""
    if len(themes) > 0:
        rnd_index = random.randint(0, len(themes) - 1)
        result = themes.pop(rnd_index)
    return result
