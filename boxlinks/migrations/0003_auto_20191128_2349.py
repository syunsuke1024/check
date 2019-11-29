# Generated by Django 2.1.7 on 2019-11-28 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boxlinks', '0002_auto_20191127_2236'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='links',
            options={'verbose_name': 'リンク集', 'verbose_name_plural': 'リンク集'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'user'},
        ),
        migrations.AlterField(
            model_name='links',
            name='link',
            field=models.CharField(max_length=255, verbose_name='リンク先'),
        ),
        migrations.AlterField(
            model_name='links',
            name='memo',
            field=models.CharField(blank=True, max_length=255, verbose_name='備考'),
        ),
    ]