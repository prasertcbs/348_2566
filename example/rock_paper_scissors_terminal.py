import random


def play(player):
    # m = ("r", "p", "s")
    # computer = random.choice(m)
    # computer = m[random.randrange(len(m))]
    d = {"r": "rock", "p": "paper", "s": "scissors"}
    # t = {"r": "rock", "p": "paper", "s": "✌"}
    # t = {"r": "\u270a", "p": "\u270b", "s": "\u270c"}
    computer = random.choice(list(d.keys()))
    if player == computer:
        result = "tie"
    elif player == "r" and computer == "s":
        result = "you win"
    elif player == "p" and computer == "r":
        result = "you win"
    elif player == "s" and computer == "p":
        result = "you win"
    else:
        result = "you lose"
    # print("you: {} <-> computer: {} -> {}".format(t[player], t[computer], result))
    return d[player], d[computer], result


def play_better(player):
    # m = ("r", "p", "s")
    # computer = random.choice(m)
    # computer = m[random.randrange(len(m))]
    d = {"r": "rock", "p": "paper", "s": "scissors"}
    # t = {"r": "rock", "p": "paper", "s": "✌"}
    # t = {"r": "\u270a", "p": "\u270b", "s": "\u270c"}
    computer = random.choice(list(d.keys()))
    if player == computer:
        result = "tie"
    elif (player == "r" and computer == "s") \
            or (player == "p" and computer == "r") \
            or (player == "s" and computer == "p"):
        result = "you win"
    else:
        result = "you lose"
    # print("you: {} <-> computer: {} -> {}".format(t[player], t[computer], result))
    return d[player], d[computer], result


if __name__ == '__main__':
    # print("\u270a")
    # print("\u0e01")
    # print("\u2660")

    while True:
        player = input("[r]ock, [p]aper, [s]cissors, e[x]it -> ")
        if player == "x":
            break
        else:
            p, com, result = play(player)
            print("you: {} <-> computer: {} -> {}".format(p, com, result))
