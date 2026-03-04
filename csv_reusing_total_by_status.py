import csv_total_by_status


def main():
    csv_dict = csv_total_by_status.totals_by_status("Enter csv file name: ")
    print(csv_dict)


if __name__ == "__main__":
    main()
