import smtplib

my_email = "abc@gmail.com"
password = ""

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="xyz@gmail.com", msg="Hello")
connection.close()
