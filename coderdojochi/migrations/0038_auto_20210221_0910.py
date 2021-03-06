# Generated by Django 3.1.6 on 2021-02-21 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coderdojochi', '0037_auto_20210118_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='assistant',
            field=models.ManyToManyField(blank=True, help_text="A mentor with 'Assistant' role, is active (user and mentor), background check passed, and avatar approved.", limit_choices_to={'avatar_approved': True, 'background_check': True, 'is_active': True, 'user__groups__name': 'Assistant', 'user__is_active': True}, related_name='session_assistant', to='coderdojochi.Mentor'),
        ),
        migrations.AlterField(
            model_name='session',
            name='instructor',
            field=models.ForeignKey(help_text="A mentor with 'Instructor' role, is active (user and mentor), background check passed, and avatar approved.", limit_choices_to={'avatar_approved': True, 'background_check': True, 'is_active': True, 'user__groups__name': 'Instructor', 'user__is_active': True}, on_delete=django.db.models.deletion.CASCADE, related_name='session_instructor', to='coderdojochi.mentor'),
        ),
    ]
