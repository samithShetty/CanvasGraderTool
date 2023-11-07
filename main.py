from utils.canvas_utils.canvas_grader import CanvasGrader


if __name__ == "__main__":
    canvas = CanvasGrader()
    
    print(canvas.course.name)
    assignment = canvas.user_select_assignment()
    question_number = int(input("Select Question Number: "))
    answer_dict = canvas.get_quiz_question_answers(assignment, question_number-1)
    
    for question_id in answer_dict:
        print(f"{question_id} -> \t{answer_dict[question_id]}")
        print("\n\n") 