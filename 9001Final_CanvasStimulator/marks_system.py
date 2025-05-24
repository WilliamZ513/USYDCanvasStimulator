
def load_marks():
    try:
        ns = {}
        with open('marks_data.py', 'r', encoding='utf-8') as f:
            exec(f.read(), ns)
        return ns.get('marks', {})
    except FileNotFoundError:
        return {}

def save_marks(d):
    with open('marks_data.py', 'w', encoding='utf-8') as f:
        f.write('marks = ' + repr(d))

def get_mark(username, course, title):
    m = load_marks().get(username, {})
    return m.get((course, title))

def set_mark(username, course, title, score):
    d = load_marks()
    if username not in d:
        d[username] = {}
    d[username][(course, title)] = score
    save_marks(d)
