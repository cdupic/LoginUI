from src.authentification.users_data import get_users_data, add_new_user


def add_user(username: str, password: str):
	users_data = get_users_data()
	if username in users_data.keys():
		return f'{username} is already taken'
	# TODO : add a hash function to store the password
	users_data[username] = password
	add_new_user(users_data)
	return f'Welcome {username} !'


