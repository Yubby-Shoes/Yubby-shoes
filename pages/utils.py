from django.core.mail import EmailMessage


class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['email_subject'],
            body=data['email_body'],
            to=[data['to_email']]
        )
        email.send()


# To send email use following format

# email_body = 'Hello, Your customer has ordered following shoes'
# data = {
#     'email_body': email_body,
#     'to_email': store_email,
#     'email_subject': 'Customer order {{product_info}}'
# }
# Util.send_email(data)
