# Generated by Django 4.0.6 on 2022-08-08 23:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0015_remove_post_categoria_id_post_categoria_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='categoria_id',
            new_name='categoria',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='usuario_id',
            new_name='usuario',
        ),
    ]