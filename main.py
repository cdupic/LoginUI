import pathlib
from src.app import LoginGUI


if __name__ == '__main__':
	app = LoginGUI(root_path=str(pathlib.Path(__file__).parent.resolve()))
	app.mainloop()
