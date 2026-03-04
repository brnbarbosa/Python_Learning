import csv


def main():
    count_paid = read_row_status("Enter csv file name: ")

    print(f"Paid count: {count_paid}")


def read_row_status(prompt) -> int:
    csv_file_name = input(prompt)
    with open(csv_file_name, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        count: int = 0
        for row in reader:
            if row["status"].strip().lower() == "paid":
                count += 1

    return count


if __name__ == "__main__":
    main()
