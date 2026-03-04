import csv


def main():
    calculation: dict = totals_by_status("Enter the csv file name: ")
    print(calculation)


def totals_by_status(prompt) -> dict:
    csv_file_name = input(prompt)
    with open(csv_file_name, "r", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        count: dict = {"paid": 0, "open": 0, "overdue": 0}
        for row in reader:
            status = row["status"].strip().lower()
            count[status] = count.get(status, 0) + 1

        return count


if __name__ == "__main__":
    main()
