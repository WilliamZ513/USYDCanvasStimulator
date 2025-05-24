import marks_system

DEFAULT_ASSIGNMENTS = {
    'COMP9001': [{'title': 'Intro Quiz',   'due_date': '2025-06-01'}],
    'COMP9601': [{'title': 'Unit1 Task',   'due_date': '2025-06-05'}],
    'DATA5207': [{'title': 'Data Lab',     'due_date': '2025-06-10'}],
    'INFO6007': [{'title': 'Info Project', 'due_date': '2025-06-15'}],
    'COMP9120': [{'title': 'SQL Finalquiz','due_date': '2025-06-16'}],
    'COMP9123': [{'title': 'Assignment3',  'due_date': '2025-06-02'}],
    'COMP5318': [{'title': 'project 2',    'due_date': '2025-05-29'}],
    'INFO5990': [{'title': 'ProjectReport','due_date': '2025-06-21'}],
    'STAT5002': [{'title': 'Final Test',   'due_date': '2025-06-04'}],
    'COMP9123': [{'title': 'Assignment 6', 'due_date': '2025-06-09'}],
    'INFO5992': [{'title': 'Presentation', 'due_date': '2025-06-14'}],
    'COMP5003': [{'title': 'DataLab 3',    'due_date': '2025-05-27'}],
}

def load_assignments():
    try:
        ns = {}
        with open('assignment_data.py', 'r', encoding='utf-8') as f:
            exec(f.read(), ns)
        return ns.get('course_assignments', {})
    except FileNotFoundError:
        return {}

def save_assignments(d):
    with open('assignment_data.py', 'w', encoding='utf-8') as f:
        f.write('course_assignments = ' + repr(d))

def create_default_assignments(course_code):
    ca = load_assignments()
    if course_code not in ca:
        ca[course_code] = DEFAULT_ASSIGNMENTS.get(course_code, [])
        save_assignments(ca)

def list_assignments(course_code):
    ca = load_assignments()
    return ca.get(course_code, [])

QUIZ_QUESTIONS = [
    ("Python is a statically typed language. True or False?",        "False"),
    ("Indentation in Python defines code blocks. True or False?",     "True"),
    ("The keyword 'def' is used to define a class in Python. True or False?", "False"),
    ("Lists in Python are mutable. True or False?",                   "True"),
    ("Tuples in Python can be modified after creation. True or False?",      "False"),
]

def take_quiz(username):

    existing = marks_system.get_mark(username, 'COMP9001', 'Intro Quiz')
    if existing is not None:
        print(f"You have already taken this quiz. Your score: {existing}")
        return

    print("COMP9001 Intro Quiz — 5 Ture Or False (20 marks for each)")
    score = 0
    for idx, (question, answer) in enumerate(QUIZ_QUESTIONS, start=1):
        while True:
            resp = input(f"{idx}. {question} ").strip().upper()
            if resp in ('T', 'F'):
                break
            print("Please answer with T or F.")
        if resp == answer[0].upper():
            score += 20

    print(f"Quiz completed. Your total score: {score}")
    marks_system.set_mark(username, 'COMP9001', 'Intro Quiz', score)