from src.authentification.users_data import get_users_data
from src.authentification.password_encrypted import get_string_encrypted


def authenticate_user(username: str, password: str):
	users_data = get_users_data()
	if username in users_data.keys() and get_string_encrypted(password) == users_data[username]:
		return f'{username} logged in successfully !', 1
	return 'Wrong username or password', 0
