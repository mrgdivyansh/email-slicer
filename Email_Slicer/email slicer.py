#program to slice a given email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def slic(e):
    Username,Domain=e.split("@")
    return Username,Domain
def send(e):
    Username, Domain = slic(e)

    # Sender and receiver email addresses
    sender_email = "guptaanshu0508@gmail.com"
    receiver_mail = e

    # Your email account credentials
    password = "gxwpxrsptfrshlov"
    a=input("Wants to give a message to send on the provided mail(Y/N)?")
    if a=="y" or a=="Y":
        su=input("Enter the Subject of the email:")
        b=input("Enter the body of the email:")

    # Email content
    subject = su
    body = b
    if Domain=="gmail.com":
        # Connect to the SMTP server
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(sender_email, password)
    if Domain=="yahoo.com":
        # Connect to the SMTP server
        server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
        server.starttls()
        server.login(sender_mail, password)
    if Domain=="outlook.com":
        # Connect to the SMTP server
        server = smtplib.SMTP("smtp.outlook.com", 587)
        server.starttls()
        server.login(sender_mail, password)
                
        

    # Create the email message
    message = f"Subject: {subject}\n\n{body}"

    # Send the email
    server.sendmail(sender_email,e, message)

    # Disconnect from the server
  #  server.quit()


    print("Email sent successfully!")

    




e=input("Enter the mail id: ")
a=e.count("@")
if a!=1:
    print("PLEASE ENTER A VALID EMAIL ID!!")
ch=1
while ch and ch!=4:
    print('''1.Wants to get username or domain
2.Wants to send only mail 
3.Wants to send mail and also get the username and domain
4.Exit
''')
    ch=int(input("Enter your choice: "))
    if ch==1:
        u,d=slic(e)
        print("Username: ",u)
        print("Domain: ",d)
    elif ch==2:
        send(e)
    elif ch==3:
        both(e)
    else:
        break
        print("Thank you for your time!!")
