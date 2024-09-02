from src.authentification.users_data import get_users_data, add_new_user
from src.authentification.password_encrypted import get_string_encrypted


def add_user(username: str, password: str):
	users_data = get_users_data()
	print(1, password, 1)
	if username in users_data.keys():
		return f'{username} is already taken', 0
	elif username == '' or password == '':
		return 'Username\password can\'t be empty', 0
	elif ' ' in username or ' ' in password:
		return 'Username\password can\'t contain spaces', 0

	users_data[username] = str(get_string_encrypted(password))
	add_new_user(users_data)
	return f'Welcome {username} !', 1
