# Generated by Django 3.2.8 on 2021-11-02 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_name', models.CharField(max_length=200)),
                ('animal_type', models.CharField(choices=[('Dog', 'dog'), ('Cat', 'cat'), ('Bird', 'bird'), ('Reptile', 'reptile'), ('Rabbit', 'rabbit'), ('Fish', 'fish'), ('Unknown', 'unkown')], default='Unkown', max_length=50)),
                ('breed', models.CharField(default='Unkown', max_length=100)),
                ('age', models.IntegerField(default=0)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vetoffice.owner')),
            ],
            options={
                'ordering': ['pet_name'],
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('appointmentID', models.BigAutoField(primary_key=True, serialize=False)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vetoffice.patient')),
            ],
        ),
    ]
