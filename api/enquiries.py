import smtplib, ssl
import os

from models.enquiries import Enquiry


def send_enquiry(enquiry: Enquiry):
    port = int(os.environ['SMTP_PORT'])
    smtp_server = os.environ['SMTP_SERVER']
    password = os.environ['SMTP_PASS']
    username = os.environ['SMTP_USER']

    # Create a secure SSL context
    context = ssl.create_default_context()

    message = f"Subject: Enquiry from {enquiry.name}\n\n{enquiry.message}"
    if enquiry.link:
        message += f"\n\n{enquiry.link}"
    print(message)

    try:
        server = smtplib.SMTP_SSL(smtp_server, port, context=context)
        server.login(username, password)
        res = server.sendmail(username, enquiry.email, message)
        server.quit()
        return {"sent": True, "response": res}
    except Exception as e:
        print(e)
        return {"sent": False, "message": e}
