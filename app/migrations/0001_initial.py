# Generated by Django 2.2.6 on 2022-03-16 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('href', models.CharField(max_length=255)),
                ('label', models.CharField(max_length=255)),
                ('children', models.CharField(blank=True, default=0, max_length=255)),
                ('parent_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Element')),
            ],
        ),
    ]
