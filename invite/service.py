import smtplib
from email.message import EmailMessage

from invite.model import Invite
from settings import settings


def send_email(invite_obj: Invite):
    msg = EmailMessage()
    msg.set_content(
        f"http://localhost:5173/admin/register/?token={invite_obj.token}")  # TODO change for production problably use .env

    msg["Subject"] = "Invite Confirmation"
    msg["From"] = f"noreply@{settings.APP_NAME}.com"
    msg["To"] = invite_obj.email

    with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as smtp:  # TODO should be SMTP_SSL
        smtp.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
        smtp.send_message(msg)
