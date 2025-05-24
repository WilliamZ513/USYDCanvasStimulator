COURSE_INFO = {
    'COMP9001':  {'tutor': 'Ehab',    'coordinator': 'Armin'},
    'DATA5207':  {'tutor': 'Ankit',   'coordinator': 'Saaz'},
    'INFO6007':  {'tutor': 'Daniel',  'coordinator': 'Sajjad'},
    
}

def load_user_courses(username):
    try:
        ns = {}
        with open('course_data.py', 'r', encoding='utf-8') as f:
            exec(f.read(), ns)
        return ns.get('user_courses', {}).get(username, [])
    except FileNotFoundError:
        return []

def save_user_courses(d):
    with open('course_data.py', 'w', encoding='utf-8') as f:
        f.write('user_courses = ' + repr(d))

def add_course(username, course_code):
    try:
        ns = {}
        with open('course_data.py', 'r', encoding='utf-8') as f:
            exec(f.read(), ns)
        uc = ns.get('user_courses', {})
    except FileNotFoundError:
        uc = {}

    lst = uc.setdefault(username, [])
    if course_code in lst:
        raise ValueError('Course already exists!')
    lst.append(course_code)
    save_user_courses(uc)

    import assignment_system
    assignment_system.create_default_assignments(course_code)

def delete_course(username, course_code):
    print("Please contact with student center if you want to cancel the course.")
    return

def get_course_info(course_code):
    return COURSE_INFO.get(course_code, {})