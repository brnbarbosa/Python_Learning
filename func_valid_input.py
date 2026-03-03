def main():
    user_input = get_int("Enter an integer: ")
    print(f"You entered {user_input}.")
        

def get_int(prompt) -> int:
    while True:
        user_input_txt = input(prompt)
        try:
            return int(user_input_txt)
        except ValueError:
            print("Invalid integer.")

if __name__ == "__main__":
    main()