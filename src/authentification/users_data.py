import json
import pathlib


auth_path = str(pathlib.Path(__file__).parent.resolve()) + '/auth.json'


def get_users_data():
	with open(auth_path, 'r') as file:
		data = json.load(file)
	return data


def add_new_user(data_user: dict):
	with open(auth_path, 'w') as file:
		json.dump(data_user, file)
