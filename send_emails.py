import smtplib
import email.message

def send_legit_email(sender, recipient):
    msg = email.message.Message()
    msg['Subject'] = "Team Meeting Reminder"
    msg['From'] = sender
    msg['To'] = recipient
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload("""
    <html>
    <body>
        <p>Hi Team,</p>
        <p>This is a reminder for our team meeting on Tuesday at 2 PM in the conference room.</p>
        <p>Please come prepared to discuss the project progress.</p>
        <p>Regards,<br>Project Lead</p>
    </body>
    </html>
    """)

    s = smtplib.SMTP('localhost', 1025)
    s.sendmail(sender, [recipient], msg.as_string())
    s.quit()

def send_phishing_email_invoice(sender, recipient):
    msg = email.message.Message()
    msg['Subject'] = "Your Netflix Subscription Invoice"
    msg['From'] = sender
    msg['To'] = recipient
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload("""
    <html>
    <body>
        <p>Dear Valued Customer,</p>
        <p>Your latest Netflix invoice is attached.  Please remit payment by the due date.</p>
        <p>To update your payment details, click <a href="http://localhost:8000/phishing_warning.html">here</a>.</p>
        <p>Thank you for your continued support.</p>
        <p>Sincerely,<br>The Netflix Team</p>
    </body>
    </html>
    """)

    s = smtplib.SMTP('localhost', 1025)
    s.sendmail(sender, [recipient], msg.as_string())
    s.quit()

def send_phishing_email_security(sender, recipient):
    msg = email.message.Message()
    msg['Subject'] = "Security Alert: Unusual Sign-in Activity"
    msg['From'] = sender
    msg['To'] = recipient
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload("""
    <html>
    <body>
        <p>Dear User,</p>
        <p>We have detected unusual sign-in activity on your account.  For your protection, please verify your account details immediately by clicking <a href="http://localhost:8000/phishing_warning.html">here</a>.</p>
        <p>Failure to verify your account may result in temporary suspension.</p>
        <p>Sincerely,<br>Account Security Team</p>
    </body>
    </html>
    """)

    s = smtplib.SMTP('localhost', 1025)
    s.sendmail(sender, [recipient], msg.as_string())
    s.quit()

def send_phishing_email_password(sender, recipient):
    msg = email.message.Message()
    msg['Subject'] = "Google Password Reset Request"
    msg['From'] = sender
    msg['To'] = recipient
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload("""
    <html>
    <body>
        <p>Hello,</p>
        <p>We received a request to reset your Google password. If you did not make this request, please ignore this email.</p>
        <p>To reset your password, click <a href="http://localhost:8000/phishing_warning.html">here</a>.</p>
        <p>Thanks,<br>The Google Team</p>
    </body>
    </html>
    """)

    s = smtplib.SMTP('localhost', 1025)
    s.sendmail(sender, [recipient], msg.as_string())
    s.quit()

if __name__ == '__main__':
    send_legit_email('teamlead@example.com', 'recipient@example.com')
    send_phishing_email_invoice('billing@netflix.com', 'recipient@example.com')
    send_phishing_email_security('security@accounts.com', 'recipient@example.com')
    send_phishing_email_password('no-reply@accounts.google.com', 'recipient@example.com')
    print("Emails sent!")
