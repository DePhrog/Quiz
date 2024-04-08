
questions = [
    
    {
        "question": "Who is the tallest pokemon out of these four?",
        "options": ["A: Tyranitar", "B: Tyrantrum", "C: Beartic", "D: Melemetal"],
        "answer": "C"
        
    },
        {
        "question": "Who is the heaviest pokemon out of these four?",
        "options": ["A: Rampardos", "B: Salamance", "C: Haxorus", "D: Dusknoir"],
        "answer": "D"
        
    },
        {
        "question": "Who is the shortest pokemon out of these four?",
        "options": ["A: Caterpie", "B: Foongus", "C: Weedle", "D: Paras"],
        "answer": "B"
        
    },
        {
        "question": "Who is the lightest pokemon out of these four?",
        "options": ["A: Eevee", "B: Zorua", "C: Growlithe", "D: Vulpix"],
        "answer": "C"
        
    },
        {
        "question": "Which one of these four pokemon is not a PSEUDO Legendary (a strong pokemon rivaling the strength of legendaries but is not considered Legendary)?",
        "options": ["A: Haxorus", "B: Dragonite", "C: Goodra", "D: Tyranitar"],
        "answer": "A"
        
    },
        {
        "question": "Who is the pure grass type pokemon out of these four?",
        "options": ["A: Torterra", "B: Budew", "C: Tropius", "D: Serperior"],
        "answer": "D"
        
    },
        {
        "question": "Who is the pure ghost type pokemon out of these four?",
        "options": ["A: Gengar", "B: Banette", "C: Cofagrigus", "D: Mimikyu"],
        "answer": "B"
        
    },
        {
        "question": "Who is the dual type pokemon out of these four?",
        "options": ["A: Psyduck", "B: Purrloin", "C: Pyroar", "D: Goodra"],
        "answer": "C"
        
    },
        {
        "question": "Who is the Mythical pokemon out of these four?",
        "options": ["A: Yveltal", "B: Volcanion", "C: Hoopa Unbound", "D: Kyurem"],
        "answer": "B"
        
    },
        {
        "question": "Which one of these has a re-colored shiny?",
        "options": ["A: Charizard", "B: Venusaur", "C: Blastoise", "D: Gengar"],
        "answer": "A"
        
    },
    # Add more questions here
]# This function will define the quiz code on launch
def run_quiz(questions):
    score = 0  # Initialize score to 0 and create a variable "score" to store the value of correct answers

    # Loop through all the questions. This will follow all the questions above until finished
    for question in questions:
        print("\n" + question["question"])  # Print the question
        for option in question["options"]:
            print(option)  # Print all the answer options

        # Get the user's answer
        user_answer = input("Enter your answer (A, B, C, or D): ").strip().upper()

        # Check if the user's answer is correct
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1  # Increment score if correct
        else:
            print("Wrong answer.")

    # Print the final score from the stored variable
    print(f"\nYou got {score} out of {len(questions)} questions correct!")

run_quiz(questions)