# Generated by Django 4.2.13 on 2024-12-08 03:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_alter_reply_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='id',
            field=models.CharField(default=uuid.UUID('5a6d3f62-4a20-4ff4-b478-38cd1fc3a79a'), editable=False, max_length=100, primary_key=True, serialize=False),
        ),
    ]
