# Generated by Django 5.1.2 on 2024-10-26 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0003_rename_tipe_ropa_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ropa',
            old_name='brand',
            new_name='marca',
        ),
        migrations.RenameField(
            model_name='ropa',
            old_name='size',
            new_name='talle',
        ),
        migrations.RenameField(
            model_name='ropa',
            old_name='type',
            new_name='tipo',
        ),
    ]
