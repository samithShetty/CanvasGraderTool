import canvasapi
from config import CANVAS_TOKEN, CANVAS_URL, COURSE_CODE
from utils.input_utils import list_select, list_select_index
from utils.html_utils import html_to_text

class CanvasGrader:
    def __init__(self) -> None:
        self.canvas = canvasapi.Canvas(CANVAS_URL, CANVAS_TOKEN)
        self.course = self.canvas.get_course(COURSE_CODE)
    
    def user_select_assignment(self, *include_groups) -> canvasapi.assignment.Assignment:
        return list_select(self.course.get_assignments(include = include_groups))
    
    def user_select_question(self, quiz: canvasapi.assignment.Assignment):
        return quiz.get_submissions(include = ["submission_history"])
    
    def get_assignment_submissions(self, assignment: canvasapi.assignment.Assignment, *include_groups):
        submissions = assignment.get_submissions(include = include_groups)
        submission_dict = dict()
        #Insert submission_dict logic
    
    # Returns ID of selected question variant
    def select_question_variation(self, quiz_assignment, question_index) -> int:
        submissions = quiz_assignment.get_submissions(include = ["submission_history"])
        question_ids = set()
        submission_datas = []
        try:
            for submission in submissions:
                submission_datas.append(submission.submission_history[0]["submission_data"])
        except KeyError: # Student did not submit assignment
            pass

        for sub_data in submission_datas:
            question_ids.add(sub_data[question_index]["question_id"])


        quiz = self.course.get_quiz(quiz_assignment.quiz_id)
        questions_text = [html_to_text(quiz.get_question(q_id).question_text) for q_id in question_ids]
        question_index = list_select_index(questions_text)
        
        return list(question_ids)[question_index]

    def get_quiz_question_answers(self, quiz_assignment, question_index, strip_chars = [' ', '\n']):
        submissions = quiz_assignment.get_submissions(include = ["submission_history"])
        submission_dict = dict()
        for s in submissions:
            try:
                question_submission = s.submission_history[0]["submission_data"][question_index]
                question_id = question_submission["question_id"]
                answer = html_to_text(question_submission["text"])
                for char in strip_chars:
                    answer = answer.replace(char, '')
                
                if question_id not in submission_dict:
                    submission_dict[question_id] = dict()
                submission_dict[question_id][answer] = submission_dict[question_id].get(answer,0) + 1
            
            except KeyError as e: # Student did not submit assignment
                pass

        return submission_dict