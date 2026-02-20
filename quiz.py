#quiz app



import json

FILENAME = "questions.json"

# Load questions from JSON file
def load_questions():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Questions file not found!")
        return []

# Run quiz
def run_quiz(questions):
    score = 0
    
    for index, q in enumerate(questions, start=1):
        print(f"\nQuestion {index}: {q['question']}")
        
        for i, option in enumerate(q["options"], start=1):
            print(f"{i}. {option}")
        
        try:
            choice = int(input("Enter option number: "))
            if q["options"][choice - 1] == q["answer"]:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! Correct answer: {q['answer']}")
        except (ValueError, IndexError):
            print("Invalid input. Skipping question.")
    
    return score

# Main function
def main():
    questions = load_questions()
    
    if not questions:
        return
    
    print("===== Welcome to the Quiz App =====")
    score = run_quiz(questions)
    
    print("\n===== Quiz Finished =====")
    print(f"Your Score: {score}/{len(questions)}")
    percentage = (score / len(questions)) * 100
    print(f"Percentage: {percentage:.2f}%")

if __name__ == "__main__":
    main()