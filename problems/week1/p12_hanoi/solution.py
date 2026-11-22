def hanoi(n, src, dst, via, moves):
    if n == 0:
        return
    hanoi(n - 1, src, via, dst, moves)
    print(f"Move disk {n} from {src} to {dst}")
    moves[0] += 1
    hanoi(n - 1, via, dst, src, moves)

n = int(input())
moves = [0]
hanoi(n, "A", "C", "B", moves)
print(f"Total moves: {moves[0]}")
