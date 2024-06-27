from django.core.mail import send_mail, EmailMessage, get_connection, send_mass_mail
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# Create your views here.


# this is only for sending the email with some text message and to, we cannot tag cc or bcc
def simple_email(request):
    send_mail(
        subject='this is simple email',
        message = 'this is simple email message',
        from_email  = 'mailtrap@demomailtrap.com',
        recipient_list= ['amithtalentplace@gmail.com',]
    )
    
    return HttpResponse('Message sent!')
    
# for more feature like, Attachment, CC, BCC we have EmailMessage
def email_message(request):
    
    email = EmailMessage(
        subject='this is simple email',
        body = 'this is email message body',
        from_email  = 'mailtrap@demomailtrap.com',
        to = ['amithtalentplace@gmail.com',],
        bcc= ['amithtalentplace@gmail.com',],
        cc = ['amithtalentplace@gmail.com',],
        reply_to= ['amithtalentplace@gmail.com',]
    )
    
    email.send()
    
    return HttpResponse('Message sent!')
    

# To send Multiple Emails at a time we use get_connection() to send emails..
def multi(request):
    email1 = EmailMessage(
        subject='this is simple email',
        body = 'this is email message body 1',
        from_email  = 'mailtrap@demomailtrap.com',
        to = ['amithtalentplace@gmail.com',],
        bcc= ['amithtalentplace@gmail.com',],
        cc = ['amithtalentplace@gmail.com',],
        reply_to= ['amithtalentplace@gmail.com',]
    )
    
    email2 = EmailMessage(
        subject='this is simple email',
        body = 'this is email message body 2',
        from_email  = 'mailtrap@demomailtrap.com',
        to = ['amithtalentplace@gmail.com',],
        bcc= ['amithtalentplace@gmail.com',],
        cc = ['amithtalentplace@gmail.com',],
        reply_to= ['amithtalentplace@gmail.com',]
    )
    
    with get_connection() as connection:
        connection.send_messages([email1, email2])

    
    return HttpResponse('Message sent!')

# To send The mass Email we can use mass 
def mass(request):
    
    message1 = ('this is simple email',# subject
               'this is email message body 2', # body
               'mailtrap@demomailtrap.com',#from
               ['amithtalentplace@gmail.com',])#to
    
    message2 = ('this is simple email',# subject
               'this is email message body 2', # body
               'mailtrap@demomailtrap.com',#from
               ['amithtalentplace@gmail.com',])#to
    
    
    message3 = ('this is simple email',# subject
               'this is email message body 2', # body
               'mailtrap@demomailtrap.com',#from
               ['amithtalentplace@gmail.com',])#to
    
    send_mass_mail([message1,message2,message3])
    
    return HttpResponse('Message sent!')
    

# to send and render the from the html content and to send, we can use render_to_string..
def html(request):
    subject='this is simple email'
    html_message = render_to_string('mail_template.html', {'message':'Hello! this is Html Email Message'})
    plain_text = strip_tags(html_message)  # used to convert html message to plain message as html_message ans send_email function accepts only message
    from_email  = 'mailtrap@demomailtrap.com'
    recipient_list = ['amithtalentplace@gmail.com',]
    
    
    send_mail(subject,plain_text,from_email,recipient_list, html_message=html_message)
    
    return HttpResponse('Message sent!')



# to send an email with attachments..
def attach(request):
    
    email = EmailMessage(
        subject='this is simple email',
        body = 'this is email message body',
        from_email  = 'mailtrap@demomailtrap.com',
        to = ['amithtalentplace@gmail.com',],
        reply_to= ['amithtalentplace@gmail.com',]
    )
    
    with open('A:/Resume/amith resume back-end.pdf', 'rb')as file: # rb is read-binary reading the file as binary.. 
        email.attach('amith',file.read(),'application/pdf') # we cna give any name for the file..
        
    email.send()
    
    return HttpResponse('Message sent!')
