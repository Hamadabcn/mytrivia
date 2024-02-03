class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

def play_game():
    # Create a list of questions
    questions = [
        Question('What is the capital of France?', 'Paris'),
        Question('Which planet is known as the "Red Planet"?', 'Mars'),
        Question('Who painted the Mona Lisa?', 'Leonardo da Vinci'),
        Question('What is the largest ocean in the world?', 'Pacific'),
        Question('What is the chemical symbol for the element Oxygen?', 'O'),
    ]

    score = 0 # Initialize score

    for question in questions:
        user_answer = input(question.question + ' ')
        if user_answer.lower() == question.answer.lower():
            print('Correct!')
            score += 1
        else:
            print('Incorrect!')

    print('Your score is', score, 'out of', len(questions))

play_game()