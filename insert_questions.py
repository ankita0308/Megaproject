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

# Function to insert a question into the database
def insert_questions(question_text, option_a, option_b, option_c, option_d, correct_option):
    query = "INSERT INTO questions (question_text, option_a, option_b, option_c, option_d, correct_option) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (question_text, option_a, option_b, option_c, option_d, correct_option)
    cursor.execute(query, values)
    db.commit()

# Example usage to add questions to the database
insert_questions("What is the capital of France?", "Paris", "Berlin", "London", "Madrid", "A")
insert_questions("Which planet is known as the Red Planet?", "Mars", "Venus", "Jupiter", "Saturn", "A")
insert_questions("Who wrote the play 'Romeo and Juliet'?", "William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain", "A")

# Close the database connection
db.close()

