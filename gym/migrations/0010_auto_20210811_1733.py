# Generated by Django 3.2.4 on 2021-08-11 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_alter_receptionist_shop'),
        ('gym', '0009_alter_grouptraining_training_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='grouptraining',
            name='signed_members',
            field=models.ManyToManyField(related_name='signed', to='people.GymMember'),
        ),
        migrations.DeleteModel(
            name='GroupTrainingSchedule',
        ),
    ]