prices = {
    "coffee": 8,
    "sandwich": 15
}

def get_user_choice(prompt, prices=prices):
    choice = input(prompt).strip().lower()

    if choice in prices:
        print(f"That costs {prices[choice]}.")
    else:
        print("Item not found.")

get_user_choice("what do you want? ")