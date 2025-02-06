Quiz Game Program Overview
This Quiz Game program is a simple interactive quiz where users answer multiple-choice questions, and their performance is evaluated based on the number of correct answers. The game is structured with a series of questions and answers stored in a list of dictionaries. Below is a breakdown of how the code works:

Code Breakdown:
List of Questions and Answers:

The questions list contains dictionaries, each holding a question and the correct answer. For example:
"What is the capital of France?" → "Paris"
"Who wrote 'Romeo and Juliet'?" → "Shakespeare"
ask_question Function:

Input: This function takes a dictionary containing a question and answer.
Output: It prompts the user for an answer to the question and validates it:
If the answer is alphabetic (e.g., names of people or places), it capitalizes the input for consistency (e.g., "paris" becomes "Paris").
It then compares the user's input to the correct answer.
Return: It returns True if the answer is correct, otherwise False.
quiz_game Function:

This is the main function that runs the quiz.
Score Tracking: It initializes the score to 0, then iterates through each question in the questions list.
For each question, the ask_question() function is called to check if the user's answer is correct.
If the answer is correct, it increments the score and displays "Correct!". If wrong, it shows the correct answer.
After all the questions have been asked, it calculates and displays the user's final score.
It also provides feedback based on the score:
Excellent: All answers are correct.
Good job: More than half of the answers are correct.
Better luck next time: Less than half the answers are correct.
Running the Quiz:

The function quiz_game() is called at the end to start the quiz.
Features:
Interactive User Input: The game prompts the user for answers, which are validated and compared against the correct answers.
Score Tracking: It keeps track of how many answers the user gets right and displays feedback based on performance.
Formatted Display: The program capitalizes alphabetic answers (for consistency in comparison) and displays appropriate messages after each answer.
Feedback: After the quiz, it provides personalized feedback based on the score.
This simple quiz game provides an engaging way to test the user's knowledge and encourages learning by giving immediate feedback.
