from src.authentification.users_data import get_users_data


def authenticate_user(username: str, password: str):
	users_data = get_users_data()
	# TODO : add a hash function to compare the password
	if username in users_data.keys() and password == users_data[username]:
		return f'{username} logged in sucessfully !'
	return False

