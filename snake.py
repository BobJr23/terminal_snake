import os, random, time, threading, keyboard as kb
from termcolor import colored

keyopp = {"a": "d", "s": "w", "w": "s", "d": "a"}

direction, prev = "d", "sus"
apple = [5, 5]

cord = {"head": [0, 2], "tail": [0, 0], "body0": [0, 1]}


def graphics(asdf):
    new = [[], [], [], [], [], [], [], []]
    print("________________________________________")
    for y in range(8):
        for x in asdf[y]:
            new[y].append("-" if x == 0 else colored("C", "green"))
    # APPLE ADD
    # print
    new[apple[0]][apple[1]] = colored("O", "red")

    # PRINT
    for iz in range(8):
        print(" ".join(new[iz]), "|")
    print("________________________________________")


def change(dir):
    cordlen = len(cord.keys()) - 2

    cop = [  # 9 tall, 21 long
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    temp = cord["head"].copy()
    if dir == "d":
        cord["head"][1] += 1
    elif dir == "a":
        cord["head"][1] -= 1
    elif dir == "s":
        cord["head"][0] += 1
    else:
        cord["head"][0] -= 1

    if apple == cord["head"]:
        while apple in cord.values():
            apple[0], apple[1] = random.randint(1, 7), random.randint(1, 19)

        cordlen += 1
        cord[f"body{cordlen-1}"] = cord["tail"].copy()
    cord["tail"] = cord[f"body{cordlen-1}"].copy()
    for x in range(1, cordlen):
        cord[f"body{cordlen-x}"] = cord[f"body{cordlen-x-1}"]
    cord["body0"] = temp
    for x, y in cord.values():
        try:
            if cop[x][y] == 1:
                print("ran into urself")
                return "quit"
            cop[x][y] = 1
        except IndexError:
            print("offmap")
            return "quit"
    return cop


def check():
    global direction
    while True:
        if kb.is_pressed("w"):
            direction = "w"
        elif kb.is_pressed("a"):
            direction = "a"
        elif kb.is_pressed("s"):
            direction = "s"
        elif kb.is_pressed("d"):
            direction = "d"
        time.sleep(0.01)


x = threading.Thread(target=check, daemon=True)
x.start()
while True:
    # CLEAR
    os.system("cls")
    # CHECK FOR KEYS

    asdf = change(direction)
    if asdf == "quit":
        print("quiting...")
        break
    graphics(asdf)
    # UPDATE WAIT
    time.sleep(0.2)
