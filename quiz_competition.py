import tkinter as tk
import mysql.connector

# Create a MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="quizdb"
)

# Create a cursor to interact with the database
cursor = db.cursor()

# Create a Tkinter window
root = tk.Tk()
root.title("Quiz Competition")

# Create labels, radio buttons, and a submit button for the quiz
question_label = tk.Label(root, text="")
option_a = tk.Radiobutton(root, text="", value="A")
option_b = tk.Radiobutton(root, text="", value="B")
option_c = tk.Radiobutton(root, text="", value="C")
option_d = tk.Radiobutton(root, text="", value="D")
submit_button = tk.Button(root, text="Submit")

# Initialize variables to keep track of question and score
question_id = 1
score = 0

# Function to load the next question
def load_question():
    global question_id
    # Fetch the next question from the database
    cursor.execute("SELECT * FROM questions WHERE id = %s", (question_id,))
    question = cursor.fetchone()

    if question:
        question_id, question_text, option_1, option_2, option_3, option_4, correct_option = question
        question_label.config(text=question_text)
        option_a.config(text=option_1, variable=var)
        option_b.config(text=option_2, variable=var)
        option_c.config(text=option_3, variable=var)
        option_d.config(text=option_4, variable=var)
    else:
        # No more questions, end the quiz
        question_label.config(text=f"Quiz Over! Your Score: {score} / 3")
        option_a.config(state="disabled")
        option_b.config(state="disabled")
        option_c.config(state="disabled")
        option_d.config(state="disabled")
        submit_button.config(state="disabled")

# Function to check the answer and load the next question
def check_answer():
    global question_id, score
    selected_option = var.get()
    # Fetch the correct answer from the database
    cursor.execute("SELECT correct_option FROM questions WHERE id = %s", (question_id,))
    correct_answer = cursor.fetchone()[0]

    if selected_option == correct_answer:
        score += 1

    if question_id < 10:
        question_id += 1
        load_question()
    else:
        # Quiz is over after 10 questions
        question_label.config(text=f"Quiz Over! Your Score: {score} / 3")
        option_a.config(state="disabled")
        option_b.config(state="disabled")
        option_c.config(state="disabled")
        option_d.config(state="disabled")
        submit_button.config(state="disabled")

# Set the default selected option to None
var = tk.StringVar()
var.set(None)

# Load the first question
load_question()

# Place widgets in the window
question_label.pack()
option_a.pack()
option_b.pack()
option_c.pack()
option_d.pack()
submit_button.config(command=check_answer)
submit_button.pack()

root.mainloop()
