# Quiz Game

# Questions and answers
questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "Who wrote 'Romeo and Juliet'?", "answer": "Shakespeare"},
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "Which planet is known as the Red Planet?", "answer": "Mars"},
    {"question": "What is the largest ocean on Earth?", "answer": "Pacific"}
]

# Function to ask the user questions and check their answers
def ask_question(question_data):
    question = question_data["question"]
    correct_answer = question_data["answer"]

    # Ask the question
    user_answer = input(question + " ").strip()

    # Validate input: check if it's alphabetic (for non-numeric answers)
    if user_answer.isalpha():
        user_answer = user_answer.capitalize()  # Capitalize to match the correct answer format

    return user_answer == correct_answer

# Function to start the quiz game
def quiz_game():
    score = 0
    total_questions = len(questions)

    print("Welcome to the Quiz Game!\n")

    for idx, question_data in enumerate(questions):
        print(f"Question {idx + 1}:")
        
        # Ask question and check answer
        if ask_question(question_data):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {question_data['answer']}\n")

    # Final score
    print(f"Your final score is {score} out of {total_questions}.")
    
    if score == total_questions:
        print("Excellent! You got all the answers correct!")
    elif score > total_questions / 2:
        print("Good job! You did well.")
    else:
        print("Better luck next time!")

# Run the quiz game
quiz_game()