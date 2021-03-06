# Generated by Django 2.0.8 on 2019-06-25 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_venue_slogan'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='food_rating',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='food', to='core.Rating'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='wifi_rating',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wifi', to='core.Rating'),
        ),
    ]
