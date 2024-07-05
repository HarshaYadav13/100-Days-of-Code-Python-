import datetime as dt
import smtplib
import random

my_email = "@gmail.com"
password = ""
receiver_email = "@gmail.com"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=receiver_email,
                            msg=f"Subject:Quote Of The Day😊\n\n{quote}"
                            )
        connection.close()
