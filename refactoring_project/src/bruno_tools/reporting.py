def top_statuses(counts: dict[str, int], k: int) -> list[str]:
    if k < 0:
        raise ValueError("k must be a non-negative integer.")

    sorted_counts = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return [f"{status}: {count}" for status, count in sorted_counts[:k]]
