import hashlib


def get_string_encrypted(password: str) -> str:
	return hashlib.sha256(password.encode()).hexdigest()
