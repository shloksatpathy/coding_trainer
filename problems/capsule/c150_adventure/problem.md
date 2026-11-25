# C150 · Checkpoint: a text adventure

A tiny game. The map (north is up):

```
           library ── vault
            │
kitchen ── hall
            │
           garden
```

More precisely: from the hall you can go north to the library, west to the kitchen and south to the garden; from the library south to the hall and east to the vault; from the kitchen east to the hall; from the garden north to the hall. The key lies in the garden, and the vault is locked without it. You start in the hall.

The first line has `n`; then come `n` commands, one per line. Answer each with one line:

- `go DIR` (north, east, south or west): `You are in the ROOM.`, or `You can't go DIR.` if there is no way, or `The vault is locked.` when going to the vault without the key.
- `take key`: `You take the key.` if it lies in this room, otherwise `There is no key here.`
- `look`: `ROOM: exits DIRS` with the room's exits in the order north, east, south, west separated by spaces, followed by ` (key here)` if the key lies there.

Entering the vault also prints `You found the treasure!` and ends the game: ignore any remaining commands. If the commands run out first, print `You give up in the ROOM.`

**Example**

Input (also in `in.txt`):
```
7
look
go north
go east
go south
go south
look
take key
```
Output:
```
hall: exits north south west
You are in the library.
The vault is locked.
You are in the hall.
You are in the garden.
garden: exits north (key here)
You take the key.
You give up in the garden.
```

**Focus:** checkpoint for module 15 and the whole capsule: modelling a world as data (rooms, an exit table and a few state variables) and a loop that reads commands, updates the state and reports.
