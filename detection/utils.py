# detection/utils.py

from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings

def send_threat_alert(threat):
    subject = f"🚨 [ALERT] {threat.type} ({threat.severity}) Detected!"
    
    text_message = f"""
    A new cybersecurity threat has been detected.
    
    Type: {threat.type}
    Severity: {threat.severity}
    Detected At: {threat.detected_at.strftime('%Y-%m-%d %H:%M:%S')}

    Recommended Actions:
    - Review logs for details.
    - Mitigate the threat immediately.
    - Contact security personnel if necessary.
    
    *This is an automated message. Do not reply.*
    """

    html_message = f"""
    <html>
    <body>
        <h2 style="color: red;">🚨 Cybersecurity Threat Alert 🚨</h2>
        <p>A new <b>{threat.type}</b> threat has been detected in your system. Immediate action is required.</p>
        <hr>
        <p><strong>🔹 Threat Type:</strong> {threat.type}</p>
        <p><strong>🔹 Severity Level:</strong> <span style="color: {'red' if threat.severity == 'Critical' else 'orange' if threat.severity == 'High' else 'blue' if threat.severity == 'Medium' else 'green'};">
            {threat.severity}</span></p>
        <p><strong>🔹 Detected At:</strong> {threat.detected_at.strftime('%Y-%m-%d %H:%M:%S')}</p>
        <hr>
        <h3>📌 Recommended Actions:</h3>
        <ul>
            <li>🔍 Review logs for more details.</li>
            <li>🛡️ Mitigate the threat immediately.</li>
            <li>📞 Contact security personnel if necessary.</li>
        </ul>
        <p style="color: gray;">This is an automated message. Do not reply.</p>
    </body>
    </html>
    """

    recipients = [
        'morangaesther010@gmail.com',  
        'security_team@example.com',  
        'it_support@example.com'
    ]

    email = EmailMultiAlternatives(subject, text_message, settings.DEFAULT_FROM_EMAIL, recipients)
    email.attach_alternative(html_message, "text/html")
    email.send()
