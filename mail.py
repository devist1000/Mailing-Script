import smtplib
import csv
import re
 
email = ""      #email address
password = ""   # passwprd
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(username, password)

#where db.cse is the name of the database file
with open('db.csv') as data:
	row = csv.DictReader(data)
	for line in row:
		name = line['fullname']
		msg = "Hey"+name+" ! Hope you're having a good time!"
		add = line['email']
		server.sendmail(email, add, msg)

server.quit()
