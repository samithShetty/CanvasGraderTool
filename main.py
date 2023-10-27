from canvasapi import Canvas
from config import CANVAS_TOKEN, CANVAS_URL, COURSE_CODE
import utils


if __name__ == "__main__":
    # Initialize a new Canvas object
    canvas = Canvas(CANVAS_URL, CANVAS_TOKEN)

    course = canvas.get_course(COURSE_CODE)
    print(course.name)

    quiz = utils.list_select(course.get_quizzes())
    submissions = [sub for sub in quiz.get_submissions()]
    question = utils.list_select(submissions[0].get_submission_question())
    print(question)