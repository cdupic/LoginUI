from dotenv import load_dotenv
from src.app import LoginGUI


if __name__ == '__main__':
	load_dotenv()
	app = LoginGUI()
	app.mainloop()
