import random
import argparse
from collections import defaultdict

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

# command line arguments
parser = argparse.ArgumentParser(description='Cookie run collab')
parser.add_argument('--multi', '-m', help='Roll multiple times', action='store_true')
args = parser.parse_args()

# input is (cookie_name, probability)
cookies = [
    ["Moonlight Cookie", 0.013],
    ["Pitaya Dragon Cookie", 0.013],
    ["Wind Archer Cookie", 0.013],
    ["Sea Fairy Cookie", 0.013],
    ["Millenial Tree Cookie", 0.013],
    ["Dark Enchantress Cookie", 0.013],
    ["Fire Spirit Cookie", 0.013],
    ["Birthday Cake Cookie", 0.03],
    ["Cocoa Cookie", 0.03],
    ["Prophet Cookie", 0.03],
    ["Pirate Cookie", 0.03],
    ["Roguefort Cookie", 0.03],
    ["Dark Choco Cookie", 0.03],
    ["Wizard Cookie", 0.03],
    ["Ion Cookie", 0.03],
    ["Angel Cookie", 0.12],
    ["Alchemist Cookie", 0.12],
    ["Rockstar Cookie", 0.12],
    ["Knight Cookie", 0.12],
    ["Ninja Cookie", 0.12],
    ["Cheesecake Cookie", 0.12],
]

cookies = sorted(cookies, key=lambda x: x[1])

# dict from probability to list of cookies
cookies_group = defaultdict(list)

for cookie, probability in cookies:
    # Group the cookies by probability
    cookies_group[probability].append(cookie)

for cookie_probability, cookie_list in cookies_group.items():
    print(f"Cookies with probability {cookie_probability * 100}%:")
    for cookie in cookie_list:
        print(cookie)
    print()

cookie_names = [cookie[0] for cookie in cookies]
cookie_probabilities = [cookie[1] for cookie in cookies]
# print(cookie_names)
# print(cookie_probabilities)

rolls = 1
if args.multi:
    rolls = int(input("Enter how many rolls: "))
    print(f"Rolling {rolls} times.")
else:
    print("Rolling once.")

received_cookies = random.choices(population=cookie_names, weights=cookie_probabilities, k=rolls)
for roll in received_cookies:
    print(f"You have received {roll}.")
