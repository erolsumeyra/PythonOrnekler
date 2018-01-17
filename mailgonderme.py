import smtplib


mail = smtplib.SMTP('smtp.gmail.com',587)

mail.ehlo()

mail.starttls()

mail.login('mailadresi@gmail.com','parola')

mail.sendmail('mailadresi@gmail.com','mailadresi1@gmail.com','Merhaba')
