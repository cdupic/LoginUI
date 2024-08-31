import tkinter as tk
import subprocess
import pathlib




class LoginGUI(tk.Tk):

	__slots__ = []

	def __init__(self, root_path=None):
		super().__init__()

		self.title('Login')
		self.geometry("925x500")
		self.configure(bg='#cee1e8')



	def signin(event=None):  # Updated to take an event argument for binding
		username = user.get()
		code = password.get()

		if username == id_author and code == password_author:
			root.destroy()
			open_app()
		else:
			messagebox.showerror("ID failure", "Invalid")

	image_entreprise = PhotoImage(file='images/photo_fond.png')
	Label(root, image=image_entreprise, bg="#cee1e8").place(x=0, y=0)

	frame = Frame(root, width=400, height=350, bg="#cee1e8")
	frame.place(x=500, y=100)

	heading = Label(frame, text='Welcome Back', fg='#429EA6', bg="#cee1e8", font=('Microsoft YaHei UI Light', 23, 'bold'))
	heading.place(x=100, y=5)

	def on_enter(e):
		user.delete(0, 'end')

	def on_leave(e):
		name = user.get()
		if name == '':
			user.insert(0, 'Username')

	user = Entry(frame, width=25, fg='#4C5C68', border=0, bg=background_login_color,
				 font=('Microsoft YaHei UI Light', 10, 'bold'))
	user.place(x=90, y=100)
	user.insert(0, 'Username')
	user.bind('<FocusIn>', on_enter)
	user.bind('<FocusOut>', on_leave)

	Frame(frame, width=250, height=2, bg="black").place(x=80, y=125)

	def on_enter_password(e):
		password.delete(0, 'end')
		password.config(show='*')

	def on_leave_password(e):
		code = password.get()
		if not code:
			password.config(show='')
			password.insert(0, 'password')

	password = Entry(frame, width=25, fg='#4C5C68', border=0, bg="#cee1e8",
					 font=('Microsoft YaHei UI Light', 10, 'bold'))
	password.place(x=90, y=150)
	password.insert(0, 'password')
	password.bind('<FocusIn>', on_enter_password)
	password.bind('<FocusOut>', on_leave_password)

	Frame(frame, width=250, height=2, bg="black").place(x=80, y=175)

	Button(frame, width=20, pady=7, text='Start', bg='#57a1f8', fg='white', border=0, command=signin).place(x=125, y=204)

	# Bind the Enter key to the signin function
	root.bind('<Return>', signin)

	root.mainloop()


