import random
import time

quiz_game_name = "BrainTeaser Challenge"

questions = [
    {
        "question": "What is the capital of france?",
        "options": ["A) Paris", "B) London", "C) Berlin", "D) Madrid"],
        "correct_answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
        "correct_answer": "B"
    },
    {
        "question": "What is 7 * 8?",
        "options": ["A) 56", "B) 64", "C) 49", "D) 42"],
        "correct_answer": "A"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
        "correct_answer": "C"
    },
    {
        "question": "Who wrote the play Romeo and Juliet?",
        "options": ["A) William Shakespeare", "B) Charles Dickens", "C) Jane Austen", "D) Mark Twain"],
        "correct_answer": "A"
    },
    {
        "question": "What is the capital of Japan?",
        "options": ["A) Beijing", "B) Seoul", "C) Tokyo", "D) Bangkok"],
        "correct_answer": "C"
    },
    {
        "question": "Which gas is the most abundant in Earth's atmosphere?",
        "options": ["A) Oxygen", "B) Carbon dioxide", "C) Nitrogen", "D) Hydrogen"],
        "correct_answer": "C"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["A) African elephant", "B) Blue whale", "C) Giraffe", "D) Polar bear"],
        "correct_answer": "B"
    },
    {
        "question": "Which planet is known as the 'Morning Star' or 'Evening Star'?",
        "options": ["A) Mars", "B) Venus", "C) Mercury", "D) Saturn"],
        "correct_answer": "B"
    },
    {   "question": "Who painted the 'Mona Lisa'?",
        "options": ["A) Vincent van Gogh", "B) Pablo Picasso", "C) Leonardo da Vinci", "D) Michaelangelo"],
        "correct_answer": "C"
    },
    {    "question": "What is the chemical symbol of water?",
        "options": ["A), Wt", "B) H2O", "C) Ho", "D) Wa"],
        "correct_answer": "B"
    },
    {
        "question": "Which planet is known for its beautiful rings?",
        "options": ["A) Neptune", "B) Uranus", "C) Saturn", "D) Pluto"],
        "correct_answer": "C"
    },
    {
        "question": "What is the capital of Italy?",
        "options": ["A) Rome", "B) Milan", "C) Venice", "D) Florence"],
        "correct_answer": "A"
    }
]

def display_welcome_message():
    print(f"Welcome to {quiz_game_name}!")
    print("You will have 15 seconds to answer each question.")
    print("Type the letter corresponding to your answer and press Enter.")
    print("Press Enter to start the quiz...")

def ask_question_with_timer(question_obj, time_limit):
    print(question_obj['question'])
    for option in question_obj['options']:
        print(option)

    start_time = time.time()
    user_answer = input("Enter the letter of your answer (A, B, C, or D):").strip().upper()
    end_time = time.time()

    if end_time - start_time > time_limit:
        print("Time's up! You took too long to answer.")
        return False
    
    if user_answer == question_obj["correct_answer"]:
        print("Correct!")
        return True
    else:
        print("Incorrect. The correct answer is:", question_obj["correct_answer"])
        return False
    
def play_round(questions, round_num):
    random.shuffle(questions)
    score = 0
    
    if round_num == 1:
        display_welcome_message()
        input()
        print("Let's get started!\n")
        time.sleep(2)

    asked_questions = []
    
    while questions:
        available_questions = [q for q in questions if q not in asked_questions]
        if not available_questions:
            break
        
        question = random.choice(available_questions)
        asked_questions.append(question)
    
    for i, question in enumerate(questions, start=1):
        if i == 1:
            print("\n")
            print(f"Round {round_num}")
            print("\n")

    if ask_question_with_timer(question, time_limit=15):
        score += 1
        time.sleep(1)

        questions.remove(question)

    return score

def replay_quiz():
    replay = input("Do you want to replay the quiz? (yes/no): ")
    return replay.lower() == "yes"

def main():
    num_rounds = 6
    
    while True:
        total_score = 0

        for round_num in range(1, num_rounds + 1):
          round_score = play_round(questions, round_num)
          print(f"Round {round_num} Score: {round_score}")
          total_score += round_score

        print("Quiz completed: Your total score:", total_score)
        if total_score < 5:
            print("You've failed the quiz. Better look next time!")

        if not replay_quiz():
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()