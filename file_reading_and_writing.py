def main():
    read_and_write_file("Enter source file name: ", "Enter destination file name: ")


def read_and_write_file(source_prompt, destination_prompt):
    source_file_name = input(source_prompt)
    destination_file_name = input(destination_prompt)
    try:
        with open(source_file_name, "r", encoding="utf-8") as src:
            with open(destination_file_name, "w", encoding="utf-8") as dst:
                for line in src:
                    dst.write(line)
            print("Copied.")
    except FileNotFoundError:
        print("Source file not found.")


if __name__ == "__main__":
    main()
