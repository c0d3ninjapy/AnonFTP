from Tkinter import *
import ftplib
import tkMessageBox

# Anonymous FTP v1.0 Login by c0d3ninja
# Instagram: c0d3ninja
# Discord: discord.gg/JV6pu5q

root = Tk()
root.title("Anonymous FTP Login.")
root.configure(bg="black")
label = Label(root, text="[::Anonymous FTP::]")
label.config(bg="black", fg="white")
label.config(font=("Courier", 30))
label.grid(row=0)
labelframe = LabelFrame(root)
labelframe.config(bg="black", padx=5, pady=10)
labelframe.grid(row=2, column=0)
labelframe2 = LabelFrame(root)
labelframe2.config(bg="black", padx=5, pady=10)
labelframe2.grid(row=4, column=0)
labelframe3 = LabelFrame(root)
labelframe3.config(bg="black", padx=5, pady=10)
labelframe3.grid(row=3, column=0)
txtscroll = Text(labelframe2)
txthost = Text(labelframe)
txtport = Text(labelframe)
lblhost = Label(labelframe, text="Host: ")
lblhost.config(bg="black", fg="white")
lblhost.grid(row=1, column=0, sticky=W)
txthost.config(width=25, height=1, fg="white")
txthost.grid(row=1, column=1, pady=5, padx=5)

def version():
	tkMessageBox.showinfo("Version", "AnonFTP V1.0 by c0d3ninja")

def anonlogin():
	try:
		ftp = ftplib.FTP(txthost.get("1.0", 'end-1c'))
		ftp.login('anonymous', 'anonymous')
		txtscroll.insert(END, (str(txthost.get("1.0", 'end-1c')) + " " + "Anonymous FTP logon successful!!"))
		txtscroll.insert(END, "\n")
		txtscroll.insert(END, "\n")
		welcome = ftp.getwelcome()
		txtscroll.insert(END, welcome)
		txtscroll.insert(END, "\n")
		txtscroll.insert(END, "\n")
		data = []
		ftp.dir(data.append)
		ftp.quit()
		for line in data:
			txtscroll.insert(END, line + "\n")
	except Exception as e:
		txtscroll.insert(END, (str(txthost.get("1.0", 'end-1c')) + " " + "Anonymous FTP logon failed"))
b = Button(labelframe, text="LOGIN", fg="white", command=anonlogin)
b.grid(row=2, column=1)

scrollbar = Scrollbar(labelframe2)
scrollbar.grid(row=3, column=1, sticky="ns")
txtscroll.config(width=60, height=20, bg="black", fg="white")
txtscroll.grid(row=3, pady=10, sticky=W)
scrollbar.config(bg="black", command=txtscroll.yview)
txtscroll.config(yscrollcommand=scrollbar.set)

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Version", command=version)
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)

root.mainloop()
