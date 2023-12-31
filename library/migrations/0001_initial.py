# Generated by Django 4.2.4 on 2023-08-11 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=10)),
                ('isbn13', models.CharField(max_length=13)),
                ('publisher', models.CharField(max_length=30)),
                ('num_pages', models.CharField(max_length=40)),
                ('per_day_charge', models.DecimalField(decimal_places=2, default=5, max_digits=6)),
                ('qty', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('number', models.CharField(max_length=13)),
                ('debt', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('aadhar_number', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Lended',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateField()),
                ('due_date', models.DateField()),
                ('returned', models.BooleanField(default=False)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.member')),
            ],
        ),
    ]
