# Generated by Django 2.1.5 on 2019-01-29 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Expense_App', '0004_auto_20190130_0107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expenses',
            name='modified_by',
        ),
    ]
