# Generated by Django 3.0.4 on 2020-03-31 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0023_auto_20200331_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertfile',
            name='advert',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='board.Advert'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='advertfile',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
