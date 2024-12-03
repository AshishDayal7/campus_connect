# test_email.py
from django.core.mail import send_mail
from django.conf import settings

def test_email():
    try:
        send_mail(
            subject='Campus Connect Test Email',
            message='This is a test email from Campus Connect.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['your-test-email@gmail.com'],  # Replace with your email
            fail_silently=False,
        )
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")