# Generated by Django 3.0.6 on 2023-03-10 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oaapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('row_status', models.BooleanField(default=True)),
                ('username', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=128)),
                ('phone_number', models.CharField(blank=True, max_length=16, null=True)),
                ('email_address', models.CharField(blank=True, max_length=32, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.AlterField(
            model_name='mailhistory',
            name='row_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='salary',
            name='row_status',
            field=models.BooleanField(default=True),
        ),
    ]
