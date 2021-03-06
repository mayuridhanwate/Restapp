# Generated by Django 2.1.5 on 2019-04-03 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('people', models.IntegerField()),
                ('booking_date_time_start', models.DateTimeField()),
                ('booking_date_time_end', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
                ('opening_time', models.IntegerField()),
                ('closing_time', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField()),
                ('status', models.CharField(blank=True, choices=[('R', 'Reserved'), ('Non', 'Non_Reserved')], max_length=50)),
                ('restaurant', models.ForeignKey(null=True, on_delete='models.CASCADE', to='orders.Restaurant')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='table',
            field=models.ForeignKey(null=True, on_delete='models.CASCADE', to='orders.Table'),
        ),
    ]
