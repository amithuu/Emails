import mailtrap as mt
from django.http import HttpResponse

def simple(request):
    mail = mt.Mail(
        sender = 'mailtrap@demomailtrap.com',
        to = ['amithtalentplace@gmail.com',],
        subject='this is simple email',
        text = 'this is email message body',
    )

    client = mt.MailtrapClient(token='c5426bf29fdebf2d744c8520d9d2a724')
    
    client.send(mail)
    
    return HttpResponse('Message sent !')
