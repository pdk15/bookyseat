from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
import time
from .models import Booking, EmailLog


def send_booking_email(booking):

    try:

        html_content = render_to_string(
            'emails/booking_confirmation.html',
            {'booking': booking}
        )

        email = EmailMultiAlternatives(
            subject='Movie Ticket Confirmation',
            body='Booking Confirmed',
            to=[booking.user.email]
        )

        email.attach_alternative(
            html_content,
            "text/html"
        )

        email.send()

        EmailLog.objects.create(
            booking=booking,
            status='SUCCESS'
        )

    except Exception as e:

        EmailLog.objects.create(
            booking=booking,
            status='FAILED',
            error_message=str(e)
        )

def send_booking_email(booking):
    
    for attempt in range(3):

        try:

            html_content = render_to_string(
                'emails/booking_confirmation.html',
                {'booking': booking}
            )

            email = EmailMultiAlternatives(
                subject='Movie Ticket Confirmation',
                body='Booking Confirmed',
                to=[booking.user.email]
            )

            email.attach_alternative(
                html_content,
                "text/html"
            )

            email.send()

            EmailLog.objects.create(
                booking=booking,
                status='SUCCESS'
            )

            return

        except Exception as e:

            if attempt == 2:
                EmailLog.objects.create(
                    booking=booking,
                    status='FAILED',
                    error_message=str(e)
                )

            time.sleep(5)