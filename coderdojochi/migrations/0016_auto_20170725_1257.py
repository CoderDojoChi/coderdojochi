# Generated by Django 1.10.5 on 2017-07-25 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coderdojochi', '0015_donation_referral_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='session',
            old_name='announced_date',
            new_name='announced_date_guardians',
        ),
        migrations.AddField(
            model_name='session',
            name='announced_date_mentors',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
