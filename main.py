import smtplib, ssl, themes
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "sender@gmail.com"
receiver_emails = [
    "w@gmail.com",
    "j@hotmail.com",
    "o@hotmail.com",
    "b@hotmail.com",
    "d@gmail.com",
    "g@hotmail.nl",
]
mail_header = """
    Hier zijn je twee themas , zoek voor ieder thema een bijpassend cadeau en pak deze anoniem volgens het thema in.
    Wie welk cadeau krijgt wordt pas met kerst geloot dus je weet nog niet voor wie je wat koopt.
    Cadeautjes dus creatief en appart inpakken zodat we met kerst 12 mooi thematisch ingepakte cadeau's hebben om te verloten.
    Budget: max 20 Euro per cadeau.

    Je themas zijn: """

port = 465
password = input("Password : ")

context = ssl.create_default_context()


def send_emails():
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        for receiver in receiver_emails:
            theme1 = themes.get_rnd_theme()
            theme2 = themes.get_rnd_theme()
            mail = MIMEText(mail_header + theme1 + " en " + theme2, "plain")
            message = MIMEMultipart()
            message["Subject"] = "Kerst Themas"
            message["From"] = sender_email
            message["To"] = receiver
            message.attach(mail)
            server.sendmail(sender_email, receiver, message.as_string())


send_emails()
