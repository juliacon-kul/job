# Generated by Django 2.2.6 on 2022-03-13 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20220301_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='parent_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Element'),
        ),
    ]