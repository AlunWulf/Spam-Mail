import smtplib
import optparse


parse_object = optparse.OptionParser()
parse_object.add_option("-t", "--target", dest="target", help="Please enter the target mail address")
parse_object.add_option("-f", "--from", dest="froms", help="Please enter the from address")
parse_object.add_option("-p","--password",dest="psword", help="Enter the password")
(user_inputs,arguments) = parse_object.parse_args()

user_target=user_inputs.target
user_from=user_inputs.froms
user_password=user_inputs.psword

if not user_target:
    print("Please enter the target mail address!!!")
    exit()

if not user_from:
    print("Please enter the from address!!!")
    exit()

number=int(input("Please write how many e-mails will be sent:"))
b=0
a=0
try:
    while a<number:
        content=("This is spam message ")
        mail=smtplib.SMTP("smtp.gmail.com",587)
        mail.ehlo()
        mail.starttls()
        mail.login(user_from,user_password)
        mail.sendmail(user_from,user_target,content)
        a=a+1
        b=b+1
        print("Send mail succesfully:",b)


except KeyboardInterrupt:
    print("\nQuit")

































