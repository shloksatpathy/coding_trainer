#include <stdio.h>
#include <string.h>

const char *ROOMS[5] = {"hall", "kitchen", "library", "garden", "vault"};
const char *DIRS[4] = {"north", "east", "south", "west"};
const int EXITS[5][4] = {{2, -1, 3, 1}, {-1, 0, -1, -1}, {-1, 4, 0, -1}, {0, -1, -1, -1}, {-1, -1, -1, -1}};
const int VAULT = 4;

int main(void) {
    int room = 0, key_room = 3, has_key = 0, n;
    char cmd[20], arg[20];
    scanf("%d", &n);
    for (int i = 0; i < n && room != VAULT; i++) {
        scanf("%19s", cmd);
        if (strcmp(cmd, "go") == 0) {
            scanf("%19s", arg);
            int d = 0;
            while (d < 4 && strcmp(DIRS[d], arg) != 0) {
                d++;
            }
            if (d == 4 || EXITS[room][d] == -1) {
                printf("You can't go %s.\n", arg);
            } else if (EXITS[room][d] == VAULT && !has_key) {
                printf("The vault is locked.\n");
            } else {
                room = EXITS[room][d];
                printf("You are in the %s.\n", ROOMS[room]);
                if (room == VAULT) {
                    printf("You found the treasure!\n");
                }
            }
        } else if (strcmp(cmd, "take") == 0) {
            scanf("%19s", arg);
            if (key_room == room) {
                printf("You take the key.\n");
                has_key = 1;
                key_room = -1;
            } else {
                printf("There is no key here.\n");
            }
        } else {
            printf("%s: exits", ROOMS[room]);
            for (int d = 0; d < 4; d++) {
                if (EXITS[room][d] != -1) {
                    printf(" %s", DIRS[d]);
                }
            }
            if (key_room == room) {
                printf(" (key here)");
            }
            printf("\n");
        }
    }
    if (room != VAULT) {
        printf("You give up in the %s.\n", ROOMS[room]);
    }
    return 0;
}
