#Write a function that accepts a list of tuples containing the name of the student and their score, sort them by the score from high to low.
def sort_student_score(name_score: list) -> list:
    return sorted(name_score, key=lambda x: x[1], reverse = True)
