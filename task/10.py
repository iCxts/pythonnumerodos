#Write a python function that accepts a list of tuples of length 2, where each tuple contains student name and their scores respectively. The function should return the name of the student whose got maximum score. Please use map(), and max() function is strictly prohibited.
def find_max_score(records: list[tuple[str, int]]) -> str:
    if not records:
        raise ValueError("records cant be empty")

    scores = list(map(lambda record: record[1], records))
    highest_index = 0

    for i, score in enumerate(scores[1:], start=1):
        if score > scores[highest_index]:
            highest_index = i

    return records[highest_index][0]
