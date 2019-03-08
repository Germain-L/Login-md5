from tkinter import *
import Backend

root = Tk()

def destroy():
	for widget in root.winfo_children():
		widget.destroy()


def send(username, password):
	u = username.get()
	p = password.get()

	destroy()

	if Backend.check(u, p) == True:
		Label(root, text="logged in").grid()

	elif Backend.check(u, p) != True:
		Label(root, text="Failed").grid(column=0, row=3)
		main()


def newB(NewU, NewP):
	Backend.newEntry(NewU=NewU.get(), NewP=NewP.get())
	destroy()
	main()


def new():
	destroy()
	
	Label(root, text="username").grid(column=0, row=0)
	Label(root, text="password").grid(column=0, row=1)

	NewU = Entry(root)
	NewP = Entry(root, show="*")

	NewU.grid(column=1, row=0)
	NewP.grid(column=1, row=1)

	Button(root, text="Submit", command=lambda: newB(NewU, NewP)).grid(column=1, row=2)


def main():
	Label(root, text="Log in:").grid(column=0, row=0)
	Label(root, text="username:").grid(column=0, row=1)
	Label(root, text="password:").grid(column=0, row=2)

	username = Entry(root)
	password = Entry(root, show="*")

	username.grid(column=1, row=1)
	password.grid(column=1, row=2)

	b = Button(root, text="login", command= lambda : send(username, password)).grid(column=1, row=3, sticky=E)
	Button(root, text="New login", command=new).grid(column=1, row=0, sticky=E)

main()	
root.mainloop()
