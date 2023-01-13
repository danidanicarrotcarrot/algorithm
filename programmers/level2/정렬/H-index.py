def solution(citations):
    citations.sort()
    for idx, value in enumerate(citations):
        if len(citations) - idx <= value:
            return len(citations) - idx
    return 0