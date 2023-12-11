# Generated by Django 5.0 on 2023-12-11 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tobe', '0002_alter_tobe_description_alter_tobe_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tobe',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='tobe',
            name='status',
            field=models.CharField(choices=[('notstarted', 'notstarted'), ('inprogress', 'inprogress'), ('completed', 'completed')], default='notstarted', max_length=17),
        ),
    ]