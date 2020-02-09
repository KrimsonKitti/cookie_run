import random
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

# input is (cookie_name, probability)
cookies = [
    ["Moonlight Cookie", 0.05],
    ["Pitaya Dragon Cookie", 0.08],
    ["Wind Archer Cookie", 0.2],
    ["Sea Fairy Cookie", 0.2],
    ["Millenial Tree Cookie", 0.1],
    ["Dark Enchantress Cookie", 0.3],
    ["Fire Spirit Cookie", 0.08],
]

for cookie, probability in cookies:
    print(f"This cookie is named {cookie}.")
    print(f"The probability of getting {cookie} is {probability * 100}%.")
    print()

cookie_names = [cookie[0] for cookie in cookies]
cookie_probabilities = [cookie[1] for cookie in cookies]
# print(cookie_names)
# print(cookie_probabilities)

rolls = int(input("Enter how many rolls: "))
print(f"Rolling {rolls} times.")
received_cookies = random.choices(population=cookie_names, weights=cookie_probabilities, k=rolls)
for roll in received_cookies:
    print(f"You have received {roll}.")
