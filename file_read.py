def main():
    try:
        count = read_file("Enter filename: ")
        print("Lines:", count)
    except FileNotFoundError:
        print("File not found.")

def read_file(prompt) -> int:
    count = 0
    file_name = input(prompt)
    with open(file_name, 'r', encoding="utf-8") as f:
        for line in f:
            count += 1
    
    return count
    

if __name__ == "__main__":
    main()