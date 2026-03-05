def main():
    words = [" paid ", "OPEN", "overdue", " Paid"]
    print(paid_only(words))


def normalizing_list(words: list[str]) -> list[str]:
    clean: list[str] = [w.strip().lower() for w in words]
    return clean


def paid_only(words: list[str]) -> list[str]:
    return [w.strip().lower() for w in words if w.strip().lower() == "paid"]


if __name__ == "__main__":
    main()
