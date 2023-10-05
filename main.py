from canvasapi import Canvas
from config import CANVAS_TOKEN, CANVAS_URL

# Initialize a new Canvas object
canvas = Canvas(CANVAS_URL, CANVAS_TOKEN)

course = canvas.get_course(206137)
print(course.name)
