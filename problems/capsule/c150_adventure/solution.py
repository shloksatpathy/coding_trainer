ROOMS = ["hall", "kitchen", "library", "garden", "vault"]
DIRS = ["north", "east", "south", "west"]
EXITS = [[2, -1, 3, 1], [-1, 0, -1, -1], [-1, 4, 0, -1], [0, -1, -1, -1], [-1, -1, -1, -1]]
VAULT = 4

room = 0
key_room = 3
has_key = False
n = int(input())
for i in range(n):
    words = input().split()
    if words[0] == "go":
        d = DIRS.index(words[1]) if words[1] in DIRS else -1
        if d == -1 or EXITS[room][d] == -1:
            print(f"You can't go {words[1]}.")
        elif EXITS[room][d] == VAULT and not has_key:
            print("The vault is locked.")
        else:
            room = EXITS[room][d]
            print(f"You are in the {ROOMS[room]}.")
            if room == VAULT:
                print("You found the treasure!")
                break
    elif words[0] == "take":
        if key_room == room:
            print("You take the key.")
            has_key = True
            key_room = -1
        else:
            print("There is no key here.")
    else:
        exits = []
        for d in range(4):
            if EXITS[room][d] != -1:
                exits.append(DIRS[d])
        extra = " (key here)" if key_room == room else ""
        print(f"{ROOMS[room]}: exits {' '.join(exits)}{extra}")
if room != VAULT:
    print(f"You give up in the {ROOMS[room]}.")
