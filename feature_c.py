"""Feature C: Notification system."""

def send_email(to, subject, body):
    """Send an email notification."""
    return {"status": "sent", "to": to, "subject": subject}

def send_sms(phone, message):
    """Send an SMS notification."""
    return {"status": "sent", "phone": phone}

