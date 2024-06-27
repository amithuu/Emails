from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_login_email(email):
        subject ='Thankyou for signings in'
        html_message = render_to_string('mail.html', {'email':email})
        plain_text =strip_tags(html_message)
        from_email='amithtalentplace@gmail.com'
        recipient_list=[email,]
        
        send_mail(subject,plain_text, from_email, recipient_list, html_message)


def send_login_credentials(email,username, password):
        subject ='Thankyou for Logging in'
        html_message = render_to_string('login_credentials.html', {'email':email,'username':username, 'password':password})
        plain_text =strip_tags(html_message)
        from_email='amithtalentplace@gmail.com'
        recipient_list=[email,]
        
        send_mail(subject,plain_text, from_email, recipient_list, html_message)