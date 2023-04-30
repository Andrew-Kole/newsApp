import smtplib, ssl
import modules.acc_info_giver as ag


def send_mail(message):
    host = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(ag.get_username(), ag.get_password())
        server.sendmail(ag.get_username(), ag.get_receiver(), message)