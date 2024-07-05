from datetime import datetime
import pandas
import random
import smtplib

my_email = "@gmail.com"
password = ""


today = (datetime.now().month, datetime.now().day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}

if today in birthdays_dict:
    birthday_details = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as file:
        content = file.read()
        content = content.replace("[NAME]", birthday_details["name"])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_details["email"],
                            msg=f"Subject:Happy Birthday\n\n{content}"
        )




