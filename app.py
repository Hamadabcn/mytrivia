# Trivia Game

# Questionnaire with multiple-choice questions
questionnaire = [
    {
        'question': 'In which year was Python first released?',
        'choices': ['1991', '1995', '2000', '2005'],
        'correct_answer': '1991'
    },
    {
        'question': 'Which of the following is not a Python data type?',
        'choices': ['Integer', 'Boolean', 'String', 'Float'],
        'correct_answer': 'Boolean'
    },
    {
        'question': 'What is the capital city of France?',
        'choices': ['Paris', 'Madrid', 'Rome', 'London'],
        'correct_answer': 'Paris'
    },
    {
        'question': 'Which company developed Python?',
        'choices': ['Google', 'Apple', 'Microsoft', 'None of the above'],
        'correct_answer': 'None of the above'
    }
]

# Function to ask a question and get the user's answer
def ask_question(question, choices):
    print(question)
    for i, choice in enumerate(choices):
        print(f'{i+1}. {choice}')
    answer = input('Enter your answer (1, 2, 3, or 4): ')
    return answer

# Function to check if the user's answer is correct
def is_answer_correct(question, answer):
    return question['choices'][int(answer)-1] == question['correct_answer']

# Main game loop
score = 0
for question in questionnaire:
    user_answer = ask_question(question['question'], question['choices'])
    if is_answer_correct(question, user_answer):
        print('Correct answer!\n')
        score += 1
    else:
        print(f'Wrong answer! The correct answer is {question["correct_answer"]}.\n')

# Game summary
print(f'Game over! Your score is {score} out of {len(questionnaire)}.')
