

lst = [
    "goodbye, people",
    "cruel people",
    "hello goodbye",
    "people hello",
    "goodbye hello",
    "people goodbye",
]

for cool_num, something_else in enumerate(lst):
    print(f"{cool_num} the saying of the day is \"{something_else}\"")

print()

print("======================= Cookie Run Collab =======================")

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
