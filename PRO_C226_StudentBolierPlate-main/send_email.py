import smtplib, ssl

def sendEmail(message):
	smtp_server = "smtp.gmail.com"
	port = 587 
	sender_email = "david.christian.longshore@gmail.com"
	password = "nkss dhgl miot djng"
	receiver_email = "657183@husdstudent.com"

	context = ssl.create_default_context()

	try:
		server = smtplib.SMTP(smtp_server,port)
		server.starttls(context=context) 
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email, message)
	   
	except Exception as e:
	    print(e)
