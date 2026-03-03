def main():
    append_to_file("Enter file name: ")
    print("Saved.")

def append_to_file(prompt):
    file_name = input(prompt)
    with open(file_name, "a", encoding="utf-8") as f:
        new_insert = input("Enter the newline content: ")
        f.write(f"{new_insert}\n")

if __name__ == "__main__":
    main()