def main():
    prices = {"coffee": 8, "sandwich": 15}
    price = get_price(prices)
    if price is None: 
        print("Item not found.")
    else:
        print(f"That costs {price}.")

 
def get_price(prices) -> int | None: # hints type that this function should return
    prompt = "What do you want? "
    user_input = input(prompt).strip().lower()
    return prices.get(user_input) # returning direct from where I get the function return value expect

if __name__ == "__main__":
    main()