import random
response = input("should I roll the dice? [y/n]: ")
no = random.randint(1,6)


if response == "y":
    if no == 1:
        print("[-----]")
        print("[-----]")
        print("[--0--]")
        print("[-----]")
        print("[-----]")
    if no == 2:
        print("[-----]")
        print("[-0---]")
        print("[-----]")
        print("[---0-]")
        print("[-----]")
    if no == 3:
        print("[-----]")
        print("[-0---]")
        print("[--0--]")
        print("[---0-]")
        print("[-----]")
    if no == 4:
        print("[-----]")
        print("[-0-0-]")
        print("[-----]")
        print("[-0-0-]")
        print("[-----]")
    if no == 5:
        print("[-----]")
        print("[-0-0-]")
        print("[--0--]")
        print("[-0-0-]")
        print("[-----]")
    if no == 6:
        print("[-----]")
        print("[-0-0-]")
        print("[-0-0-]")
        print("[-0-0-]")
        print("[-----]")
    