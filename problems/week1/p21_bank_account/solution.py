class Account:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amt):
        if amt > self.balance:
            print("Insufficient")
        else:
            self.balance -= amt

acc = Account()
while True:
    parts = input().split()
    if parts[0] == "Q":
        break
    if parts[0] == "D":
        acc.balance += int(parts[1])
    elif parts[0] == "W":
        acc.withdraw(int(parts[1]))
    elif parts[0] == "B":
        print(acc.balance)
