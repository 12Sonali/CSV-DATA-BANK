# Generated by Django 4.2.7 on 2024-02-14 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=49)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('ifsc', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('branch', models.CharField(max_length=74)),
                ('address', models.CharField(max_length=195)),
                ('contact', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=26)),
                ('bank_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.bank')),
            ],
        ),
    ]
