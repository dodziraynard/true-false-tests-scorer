def calculate_score(correct_answers: dict, student_answers: dict) -> int:
    scores = 0
    for i, answer in enumerate(correct_answers):
        if answer.lower() == "x":
            continue
        scores += 1 if answer.lower() == student_answers[i].lower() else -1
    return scores


# Dictionary for keeping student_id and scores
student_id_and_score = {}
student_id = ""

# Enter correct answers separated by space
correct_answers = input().strip().split()

while True:
    # Enter student id and the answers all separated by space
    input_data = input().strip().split()
    student_id, answers = input_data[0], input_data[1:]
    if student_id == "999":
        break
    scores = calculate_score(correct_answers, answers)
    student_id_and_score.update({student_id: scores})

# Printing the output
for student_id, score in student_id_and_score.items():
    print(f"{student_id} {score} marks")
