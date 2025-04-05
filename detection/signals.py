import logging
from django.contrib.auth.signals import user_login_failed
from django.dispatch import receiver
from django.utils.timezone import now
from django.core.mail import send_mail
from django.conf import settings
from .models import Threat

# Logger for security events
security_logger = logging.getLogger("django.security")

@receiver(user_login_failed)
def login_failed_handler(sender, credentials, request, **kwargs):
    """Handles failed login attempts: logs them as threats, sends email alerts, and writes to security logs."""
    
    username = credentials.get("username", "Unknown User")
    ip_address = get_client_ip(request) if request else "Unknown IP"

    # Log the failed login attempt in the database
    threat = Threat.objects.create(
        threat_type="Failed Login Attempt",  # Ensure this matches your model field
        severity="High",
        details=f"Failed login from IP: {ip_address}, Username: {username}",
        detected_at=now()
    )

    # Log the security event
    security_logger.warning(f"FAILED LOGIN ATTEMPT: Username={username}, IP={ip_address}, Time={now()}")

    # Send an email alert
    send_failed_login_alert(username, ip_address)

    print(f"[ALERT] Failed login attempt detected: {threat}")

def get_client_ip(request):
    """Safely extracts the client's IP address."""
    if not request:
        return "Unknown IP"
    
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]
    return request.META.get('REMOTE_ADDR', 'Unknown IP')  # Use a fallback if no IP is found

def send_failed_login_alert(username, ip_address):
    """Sends an email alert for a failed login attempt."""
    subject = "🚨 Security Alert: Failed Login Attempt Detected!"
    message = (
        f"⚠️ A failed login attempt was detected on your system.\n\n"
        f"🔹 **Username Attempted:** {username}\n"
        f"🔹 **IP Address:** {ip_address}\n"
        f"🔹 **Time of Attempt:** {now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        f"🔍 Please review your system logs and take necessary security measures.\n\n"
        f"Stay Safe,\nCybersecurity System"
    )

    # Ensure email settings exist
    if not getattr(settings, "DEFAULT_FROM_EMAIL", None):
        print("⚠️ Email alert skipped: DEFAULT_FROM_EMAIL is not set in settings.py")
        return

    recipients = ["morangaesther010@gmail.com", "security@example.com"]  # Add more if needed

    try:
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,  # Ensure this is set in settings.py
            recipients,
            fail_silently=False,
        )
        print(f"✅ Email alert sent to {', '.join(recipients)}")
    except Exception as e:
        security_logger.error(f"❌ Failed to send email alert: {e}")
