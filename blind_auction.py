import art
print(art.logo)

should_continue = True
details = {}

while should_continue:
    name = (input("What is your name?: "))
    bid = (input("Enter your bid amount: $"))
    details[name] = bid
    others = input(("Are there any other bidders? Yes or no ")).lower()
    if others == "no":
        should_continue = False
    else:
        print("\n" * 100)


highest_bid = 0
winner = ""
for name, bid in details.items():
    bid = int(bid)
    if bid > highest_bid:
        highest_bid = bid
        winner = name

print(f"{winner} has the highest bid with ${highest_bid}")
















