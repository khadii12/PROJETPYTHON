# Generated by Django 4.1.5 on 2023-02-19 20:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('tel', models.IntegerField(validators=[django.core.validators.RegexValidator(message='entrer un nombre valide', regex='^(1[1-9]|2[1-2,4,7,8]|3[1-5]|3[7-8]|4[1-9]|5[1,3-5]|6[1-9]|7[1,3,4,5,7,9]|8[1-9]|9[1-9]){1}[0-9]{8,9}$')])),
            ],
        ),
        migrations.CreateModel(
            name='Salle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('type', models.CharField(choices=[('VIP', 'vip'), ('NORMAL', 'Normal')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('type', models.CharField(choices=[('VIP', 'vip'), ('NORMAL', 'Normal')], max_length=50)),
                ('disponiblité', models.BooleanField(default=True)),
                ('salle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Reservation.salle')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_reservation', models.DateTimeField()),
                ('disponiblité', models.BooleanField(default=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reservation.client')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reservation.table')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation_salle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_reservation', models.DateTimeField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reservation.client')),
                ('salle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reservation.salle')),
            ],
        ),
    ]
