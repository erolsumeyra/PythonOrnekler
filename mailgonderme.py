import smtplib


mail = smtplib.SMTP('smtp.gmail.com',587)

mail.ehlo()

mail.starttls()

mail.login('erolsumeyra@gmail.com','Denizbaran01')

mail.sendmail('erolsumeyra@gmail.com','bulutnizam@gmail.com','dayicim Mail geldiyse yanit verir misin')
