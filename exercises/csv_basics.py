import csv


def main():
    print(read_csv_file("Enter csv file name: "))


def read_csv_file(prompt) -> int:
    csv_file_name = input(prompt)
    with open(csv_file_name, "r") as csv_file:
        info = csv.reader(csv_file)
        next(info, None)
        count: int = 0
        for row in info:
            count += 1

    return count


if __name__ == "__main__":
    main()
