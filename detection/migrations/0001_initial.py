# Generated by Django 5.1.7 on 2025-03-29 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Threat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Malware', 'Malware'), ('Phishing', 'Phishing'), ('DDoS', 'DDoS'), ('Unauthorized Access', 'Unauthorized Access')], max_length=50)),
                ('severity', models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Critical', 'Critical')], max_length=20)),
                ('description', models.TextField()),
                ('detected_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
