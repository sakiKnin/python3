import tkinter as tk
from tkinter import filedialog, Text
import os, sys, subprocess

import smtplib

import yagmail

from email.message import EmailMessage

root = tk.Tk()
root.title("SENDaMAIL")

label1 = tk.Label(root, text="Send to:")
label1.pack()

email = tk.Entry(root)
email.pack()

label2 = tk.Label(root, text="Subject:")
label2.pack()

subject = tk.Entry(root)
subject.pack()

label3 = tk.Label(root, text="Message:")
label3.pack()

text = tk.Text(root, bg="white", height=25, width= 50)
text.pack()


def addAnAttachment():

	apps=[]
	def deleteFile():
		 for widget in text3.winfo_children():
				if widget==deleteFile:
					i=text3.winfo_children().index(widget)
					tempSave = text3.winfo_children()[i-1]
					print(text3.winfo_children()[i-1])
					text3.winfo_children()[i-1].destroy()
					widget.destroy()
		 
		 with open('saveAttachments.txt', 'r') as f:
				tempAttachs = f.read()
				tempAttachs = tempAttachs[0:len(tempAttachs)-1]
				attachs = tempAttachs.split(',')
				print(attachs, i)
				if i==1:
					attachs = attachs[:(i-1)] + attachs[int(i):]
				elif i>1:
					attachs = attachs[:int((i-1)/2)] + attachs[int((i+1)/2):]
				print(attachs)
				f.close()

		 with open('saveAttachments.txt', 'w') as f:
				for attach in attachs:
					f.write(attach + ',')
				f.close()
	
	filename = filedialog.askopenfilename(initialdir="/home/boris/Desktop", title="SelectFile", filetypes=(("text",".txt"),("all files",".")))
	apps.append(filename)	
	
	for app in apps:
		label= tk.Label(text3, text=app, bg = "gray")
		label.pack()
		deleteFile = tk.Button(text3, text="delete", padx=1, pady=5, fg="green", bg="#263D42", command = deleteFile )
		deleteFile.pack()
		print(label)
		print(deleteFile)	

	with open('saveAttachments.txt', 'a') as f:
		for app in apps:
			f.write(app + ',')
	f.close()

attachFile = tk.Button(root, text="Attach a file:", padx=10,pady=5, fg="green", bg="#263D42", command = addAnAttachment)
attachFile.pack()

text3 = tk.Text(root, bg="white", height=1, width= 50)
text3.pack()

def sendAnEmail():
	msg = EmailMessage()
	print(msg)
	msg['Subject'] = subject.get()
	msg['From'] = email.get()
	msg['To'] = email.get()
	msg['Body'] = text.get("0.0", "end")
	with open('saveAttachments.txt', 'r') as f:
		tempApps=f.read();
		apps=tempApps.split(",");
		aps=apps[0:len(apps)-1]
		#apps=[x for x in tempApps if x.strip()] # izbacuje razmake
		print(aps) 
	f.close()
	 
	#msg['Attachment'] = aps
	print(msg)
	s = yagmail.SMTP('xxxx','xxxx')
	s.send(msg['To'], msg['Subject'], msg['Body'], aps)

sendMail = tk.Button(root, text="Send an email", padx=10,pady=5, fg="green", bg="#263D42", command=sendAnEmail)
sendMail.pack()
try:
	os.remove('saveAttachments.txt')
except:
	f=open('saveAttachments.txt', 'x')
	os.remove('saveAttachments.txt')
root.mainloop()
