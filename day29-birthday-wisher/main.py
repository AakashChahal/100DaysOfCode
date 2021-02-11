# import smtplib
#
# my_email = "chahalaakash.17@gmail.com"
# connection = smtplib.SMTP("smtp.gmail.com", 587)
# connection.ehlo()
# connection.starttls()
# connection.login(my_email, "password@secondemail")
# connection.sendmail(my_email, "aakash.chahal62@gmail.com", "Subject:hello\n\nHello")
# connection.close()
import datetime as dt
print(dt.datetime.now().weekday())
