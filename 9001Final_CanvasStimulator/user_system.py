def load_users():
    try:
        with open('user_data.py', 'r') as f:
            ns = {}
            exec(f.read(), ns)
            return ns.get('users', {})
    except FileNotFoundError:
        return {}

def save_users(users):
    with open('user_data.py', 'w') as f:
        f.write('users = ' + repr(users))

def register_user(username, password):
    users = load_users()
    if username in users:
        raise ValueError('Unikey already registered, please log in.')
    users[username] = password
    save_users(users)

def login_user(username, password):
    users = load_users()
    return users.get(username) == password