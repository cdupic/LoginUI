import customtkinter as ctk

from src.authentification.signin import authenticate_user
from src.authentification.signup import add_user


class LoginGUI(ctk.CTk):

	__slots__ = ['background_frame', 'username_entry', 'password_entry', 'login_button', 'register_button']

	def __init__(self):
		super().__init__()

		self.signup_button = None
		self.signin_button = None
		self.password_entry = None
		self.username_entry = None
		self.message_box_exists = False

		self.title('Login')
		self.geometry("450x700")
		self.resizable(True, True)

		# set background color (ctk can only be black or white)
		self.background_frame = ctk.CTkFrame(self, fg_color="#F3DE8A")
		self.background_frame.pack(fill='both', expand=True)

		# set the font used in the app
		self.font = ctk.CTkFont("Helvetica", 15)

		# set the grid layout
		self.background_frame.columnconfigure(0, weight=1)
		self.background_frame.columnconfigure(1, weight=1)
		self.background_frame.columnconfigure(2, weight=1)
		self.background_frame.rowconfigure(0, weight=1)

		# set the frame containing the widgets
		self.widget_frame = ctk.CTkFrame(self.background_frame, fg_color="#EB9486")
		self.widget_frame.grid(column=1, row=0, sticky='nsew', pady=20, padx=20)

		# set the grid layout on that frame
		self.widget_frame.columnconfigure(0, weight=1)
		self.widget_frame.rowconfigure(0, weight=1)
		self.widget_frame.rowconfigure(1, weight=1)
		self.widget_frame.rowconfigure(2, weight=1)

		# set the frame for the sign in / sign up buttons
		self.button_frame = ctk.CTkFrame(self.widget_frame, fg_color="#EB9486")
		self.button_frame.grid(column=0, row=2, sticky='nsew', pady=50, padx=40)

		# set the grid layout on that frame (2 columns)
		self.button_frame.columnconfigure(0, weight=1)
		self.button_frame.columnconfigure(1, weight=1)
		self.button_frame.rowconfigure(0, weight=1)

		self.widgets()


	def widgets(self):
		self.username_entry = ctk.CTkEntry(self.widget_frame, fg_color='#4C5C68', bg_color='#C5BAAF',
										   placeholder_text='username', corner_radius=0, justify='center')
		self.username_entry.grid(column=0, row=0, sticky='nsew', pady=30, padx=20)

		self.password_entry = ctk.CTkEntry(self.widget_frame, fg_color='#4C5C68', bg_color='#C5BAAF',
										   placeholder_text='password', corner_radius=0, justify='center', show='*')
		self.password_entry.grid(column=0, row=1, sticky='nsew', pady=30, padx=20)

		self.signin_button = ctk.CTkButton(self.button_frame, text='Sign In', bg_color='#429EA6', fg_color='#AD91A3',
										   border_color='#EB9486', corner_radius=0, font=self.font, command=self.signin)
		self.signin_button.grid(column=1, row=0, sticky='nsew', padx=20, pady=20)

		self.signup_button = ctk.CTkButton(self.button_frame, text='Sign Up', bg_color='#429EA6', fg_color='#AD91A3',
										   border_color='#EB9486', corner_radius=0, font=self.font, command=self.signup)
		self.signup_button.grid(column=0, row=0, sticky='nsew', padx=20, pady=20)


	def signin(self):
		username = self.username_entry.get()
		password = self.password_entry.get()
		auth_user = authenticate_user(username, password)
		if not auth_user:
			self.clear_entries()
		if not self.message_box_exists:
			self.message_box_exists = True
			MessageBox(auth_user, self)

	def signup(self):
		username = self.username_entry.get()
		password = self.password_entry.get()
		auth_add = add_user(username, password)
		if 'taken' in auth_add:
			self.clear_entries()

		if not self.message_box_exists:
			self.message_box_exists = True
			MessageBox(auth_add, self)


	def clear_entries(self):
		self.username_entry.delete(0, 'end')
		self.password_entry.delete(0, 'end')



class MessageBox(ctk.CTkToplevel):

	def __init__(self, message_tuple: tuple, main_window):
		super().__init__()

		self.title("Message")
		self.geometry("250x100")
		self.resizable(False, False)
		self.grab_set()

		self.main_window = main_window

		self.message_id = message_tuple[1]

		self.label = ctk.CTkLabel(self, text=message_tuple[0])
		self.label.pack(pady=10)

		self.button = ctk.CTkButton(self, text="OK", command=self.close_action)
		self.button.pack(pady=10)

		self.protocol("WM_DELETE_WINDOW", self.close_action)



	def close_action(self):
		if self.message_id:
			self.main_window.destroy()
		else:
			self.main_window.clear_entries()
			self.main_window.message_box_exists = False

		try:
			self.destroy()
		except:
			pass
