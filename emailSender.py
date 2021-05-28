from email import message
import smtplib
from UserSignUp import User

# id , name , age , email , password
def sendMail(val):
    #print("data : "+ str(val[0]))
    from_address = "junejachirag022@gmail.com"
    to_address = str(val[3])

    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()

    message = '''
                    hi , {} 
                    welcome to our database your user id and password are listed as 
                    UID : {} ,
                    PASSWORD : {}

                    you can login with these details.
                    please don't share your ID and password with anyone.

                    Thanks and Regards.
                    Database Admin : TANISHA KHANDELWAL

    '''.format(val[1] , val[0] , val[4])

    mail.login(from_address, '9982917736')
    mail.sendmail(from_address,to_address, message)
    print("mail sent success...")
    mail.close()