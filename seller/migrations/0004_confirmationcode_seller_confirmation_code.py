# Generated by Django 4.2.3 on 2023-09-18 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0003_seller_is_seller'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfirmationCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(max_length=6)),
                ('user_id', models.BigIntegerField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='seller',
            name='confirmation_code',
            field=models.CharField(default=1, max_length=6),
            preserve_default=False,
        ),
    ]
