print("======================= Bonuses =======================")
print()

lst = [
    "Free Relay",
    "Coins +50%",
    "Unlimited Stamina",
    "Free Relay",
    "Free Rescues",
    "Unlimited Stamina",
    "20% More Trophies",
]

for cool_num, something_else in enumerate(lst, start=1):
    print(f"Day {cool_num} of the week has: {something_else}")

print()

print("======================= Cookie Run Collab =======================")
print()

cookies = [
    ["Moonlight Cookie", 1],
    ["Pitaya Dragon Cookie", 1],
    ["Wind Archer Cookie", 10],
    ["Sea Fairy Cookie", 5],
    ["Millenial Tree Cookie", 10],
    ["Dark Enchantress Cookie", 70],
    ["Fire Spirit Cookie", 3],
]

for cookie, probability in cookies:
    print(f"This cookie is named {cookie}")
    print(f"The probability of getting {cookie} is {probability}%")
    print()
