def main():
    counts = {"paid": 2, "open": 2, "overdue": 1, "canceled": 5}
    try:
        print(top_statuses(counts, 2))
    except ValueError as e:
        print(e)


def top_statuses(counts: dict[str, int], k: int) -> list[str]:
    if k < 0:
        raise ValueError("k must be non-negative")

    sorted_counts = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    topk = sorted_counts[:k]
    formatted = [f"{status}: {count}" for status, count in topk]
    return formatted


if __name__ == "__main__":
    main()
