from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import EmailMessage


@shared_task
def send_mail(subject, sender, receiver, html_content):
    '''
    Celery task to send email
    '''
    try:
        mail = EmailMessage(subject, html_content, sender, [receiver])
        mail.content_subtype = "html"  # Main content is now text/html
        mail.send()
        result = 'success'

    except:
        result = 'fail'

    return result