from django.db import models
from django.utils.timezone import now

class Threat(models.Model):
    THREAT_SEVERITY_CHOICES = [
        ('Critical', 'Critical'),
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]

    threat_type = models.CharField(
        max_length=255, 
        default="Unknown Threat",
        help_text="Type of detected threat (e.g., SQL Injection, XSS, Phishing)."
    )
    severity = models.CharField(
        max_length=50, 
        choices=THREAT_SEVERITY_CHOICES, 
        default='Low', 
        help_text="Threat severity level."
    )
    details = models.TextField(
        default="No details provided",  # 🔹 Fixed the lambda issue
        help_text="Detailed information about the detected threat."
    )
    detected_at = models.DateTimeField(
        default=now, 
        help_text="Timestamp when the threat was detected."
    )
    
    source_ip = models.GenericIPAddressField(
        null=True, blank=True, 
        help_text="IP address of the attacker or source."
    )
    user_agent = models.CharField(
        max_length=500, 
        null=True, blank=True, 
        help_text="User agent of the attacker's device."
    )
    reported_by = models.CharField(
        max_length=255, 
        null=True, blank=True, 
        help_text="Source reporting the threat (e.g., system module, admin, automated detector)."
    )

    def __str__(self):
        return f"{self.threat_type} - {self.severity} (Detected at {self.detected_at})"
