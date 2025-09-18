from django.db.models.signals import post_save
from django.dispatch import receiver

from clients.models import Client
from common.mail import send_email
import uuid


@receiver(signal=post_save, sender = Client)
def post_registration(sender:Client, instance:Client, created:bool, **kwargs):

    if created:
        print(instance.code_experetion_date)
        send_email(
            template= "activation.html",
            to = instance.email,
            context={
                    "username": instance.username,
                    "code": (f"http://127.0.0.1:8000/activate/{instance.pk}/?code={instance.activation_code}"),
                }
        )
        return
    return
