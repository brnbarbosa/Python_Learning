def main():
    pairs = [("paid", 2), ("open", 2), ("overdue", 1)]
    sorted_pairs = sorted(pairs, key=lambda pair: (-pair[1], pair[0]))
    print(sorted_pairs)


if __name__ == "__main__":
    main()
