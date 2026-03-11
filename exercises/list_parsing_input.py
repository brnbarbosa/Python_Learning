def main():
    try: 
        user_input_lst : list= getting_user_input("Enter integers separated by spaces: ")
        print(f"Count: {len(user_input_lst)}")
        print(f"Sum: {sum(user_input_lst)}")
        print(f"Min: {min(user_input_lst)}")
        print(f"Max: {max(user_input_lst)}")
        
    except ValueError as e:
        print("Invalid input.")

def getting_user_input(prompt) -> list[int]:
    user_input = input(prompt)
    input_list : list = user_input.split()

    nums : list = [int(p) for p in input_list]
    return nums


"""def getting_user_input(prompt) -> dict:
    user_input = input(prompt)
    input_list : list = user_input.split()

    for i in range(0, len(input_list)):
        if int(input_list[i]) is None:
            raise ValueError()
        else:
            input_list[i] = int(input_list[i])

    parsing_input : dict = {
        "Count: ": len(input_list),
        "Sum: ": sum(input_list),
        "Min: ": min(input_list),
        "Max: ": max(input_list)
    }

    return parsing_input   
"""

if __name__ == "__main__":
    main()